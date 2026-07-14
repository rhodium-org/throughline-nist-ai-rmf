#!/usr/bin/env python3
"""Generate the NIST AI RMF 1.0 throughline source from the vendored Core + Playbook data.

Two authoritative NIST inputs are vendored under ``tools/airmf-1.0/`` (both public domain —
works of the US Federal Government, 17 U.S.C. Sec. 105):

* ``core.json`` — the AI RMF Core (NIST AI 100-1, Tables 1-4): the four Function statements,
  the 19 Category statements and the 72 Subcategory outcome statements. Extracted from the
  AI RMF Core section at https://airc.nist.gov/airmf-resources/airmf/5-sec-core/.
* ``playbook.json`` — the NIST AI RMF Playbook (raw download from
  https://airc.nist.gov/docs/playbook.json): per-Subcategory ``section_about`` prose ("about
  this subcategory" / why it matters) — the per-leaf ``rationale``, the same role WCAG's
  "Intent of this Success Criterion" plays.

**UIDs are permanent.** The mapping from a Function/Category/Subcategory to a throughline UID
is derived from the items already on disk, keyed by ``attrs.source_ref`` (the AI RMF handle:
``"GOVERN"``, ``"GOVERN 1"``, ``"GOVERN 1.1"``). Anything without an item yet gets a freshly
allocated UID in document order; a UID, once allocated, never moves. Bodies regenerate from
the vendored data each run.

**The "why" spine is genuinely multi-root — the point of putting the AI RMF on the list.**
The Core is organised under four Functions (GOVERN, MAP, MEASURE, MANAGE), and those are four
genuinely different reasons the framework exists — govern the programme, map the context and
risks, measure and analyse them, manage and respond. So there are **four co-equal root
intents** (INT-0001..INT-0004), never a single "manage AI risk" umbrella that flattens every
outcome's reason-for-existing into one bland "...exists". Each Function statement *is* that
root's ``text``.

Each Category (``GOVERN 1``) is a ``user_requirement`` that ``derives_from`` its own Function
root, with the Category's Core statement as its ``text``. Each Subcategory (``GOVERN 1.1``) is
a ``system_requirement`` that ``implements`` its Category, with the Subcategory outcome
statement as ``text``, the Playbook's "about this subcategory" lead paragraph as
``rationale``, and the AI RMF id in ``attrs.source_ref``. The Core hierarchy is strict (one
Function per Category, one Category per Subcategory), so a Subcategory grounds to its Function
up implements->derives_from with no extra edge. The AI RMF grades no outcome by level (unlike
ASVS/AISVS), so there is no ``level`` attribute; editions are git tags of this one repo.

Usage:  python tools/generate.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "tools" / "airmf-1.0"
INTENTS_DIR = REPO / "intents"          # intent (Function roots), prefix INT
CATEGORIES_DIR = REPO / "categories"    # user_requirement (Categories), prefix UR
SUBCATS_DIR = REPO / "subcategories"    # system_requirement (Subcategories), prefix SR
SPEC = REPO / "docs" / "spec.md"

FUNCTION_ORDER = ["GOVERN", "MAP", "MEASURE", "MANAGE"]
FUNCTION_NAME = {
    "GOVERN": "Cultivate a culture of AI risk management",
    "MAP": "Recognise context and identify risks",
    "MEASURE": "Assess, analyse and track risks",
    "MANAGE": "Prioritise and act on risks",
}


def _squash(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _lead_paragraph(section_about: str) -> str:
    """First non-empty paragraph of the Playbook 'about this subcategory' prose."""
    for para in re.split(r"\n\s*\n", section_about or ""):
        if para.strip():
            return _squash(para)
    return ""


def _cat_of(subcat_id: str) -> str:
    """'GOVERN 1.1' -> 'GOVERN 1'."""
    fn, num = subcat_id.split()
    return f"{fn} {num.split('.')[0]}"


def _cat_sort(cat_id: str) -> tuple[int, int]:
    fn, num = cat_id.split()
    return (FUNCTION_ORDER.index(fn), int(num))


def _sub_sort(sub_id: str) -> tuple[int, int, int]:
    fn, num = sub_id.split()
    major, minor = num.split(".")
    return (FUNCTION_ORDER.index(fn), int(major), int(minor))


def _dump(path: Path, item: dict) -> None:
    path.write_text(
        yaml.safe_dump(item, sort_keys=False, allow_unicode=True, width=90),
        encoding="utf-8",
    )


def _scan(dir_: Path) -> dict[str, str]:
    ref2uid: dict[str, str] = {}
    for f in dir_.glob("*.yml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        ref = (data.get("attrs") or {}).get("source_ref")
        if ref:
            ref2uid[ref] = data["uid"]
    return ref2uid


def _max(ref2uid: dict[str, str], prefix: str) -> int:
    return max((int(u.split("-")[1]) for u in ref2uid.values()
               if u.startswith(prefix + "-")), default=0)


def generate() -> dict[str, int]:
    core = json.loads((DATA_DIR / "core.json").read_text(encoding="utf-8"))
    playbook = json.loads((DATA_DIR / "playbook.json").read_text(encoding="utf-8"))
    about = {r["title"]: _lead_paragraph(r.get("section_about", "")) for r in playbook}

    int_ref = _scan(INTENTS_DIR)
    ur_ref = _scan(CATEGORIES_DIR)
    sr_ref = _scan(SUBCATS_DIR)
    n_int = _max(int_ref, "INT") + 1
    n_ur = _max(ur_ref, "UR") + 1
    n_sr = _max(sr_ref, "SR") + 1
    counts = {"int": 0, "ur": 0, "sr": 0}

    # Functions -> root intents
    for fn in FUNCTION_ORDER:
        int_uid = int_ref.get(fn)
        if int_uid is None:
            int_uid = f"INT-{n_int:04d}"; n_int += 1; int_ref[fn] = int_uid
            counts["int"] += 1
        _dump(INTENTS_DIR / f"{int_uid}.yml", {
            "uid": int_uid,
            "type": "intent",
            "status": "approved",
            "title": f"{fn} \u2014 {FUNCTION_NAME[fn]}",
            "text": _squash(core["functions"][fn]),
            "normative": False,
            "attrs": {"source_ref": fn},
        })

    # Categories -> user_requirements
    for cat_id in sorted(core["categories"], key=_cat_sort):
        fn = cat_id.split()[0]
        ur_uid = ur_ref.get(cat_id)
        if ur_uid is None:
            ur_uid = f"UR-{n_ur:04d}"; n_ur += 1; ur_ref[cat_id] = ur_uid
            counts["ur"] += 1
        _dump(CATEGORIES_DIR / f"{ur_uid}.yml", {
            "uid": ur_uid,
            "type": "user_requirement",
            "status": "approved",
            "title": cat_id,
            "text": _squash(core["categories"][cat_id]),
            "links": [{"target": int_ref[fn], "type": "derives_from"}],
            "attrs": {"source_ref": cat_id},
        })

    # Subcategories -> system_requirements
    for sub_id in sorted(core["subcategories"], key=_sub_sort):
        cat_id = _cat_of(sub_id)
        sr_uid = sr_ref.get(sub_id)
        if sr_uid is None:
            sr_uid = f"SR-{n_sr:04d}"; n_sr += 1; sr_ref[sub_id] = sr_uid
            counts["sr"] += 1
        item = {
            "uid": sr_uid,
            "type": "system_requirement",
            "status": "approved",
            "title": f"AI RMF {sub_id}",
            "text": _squash(core["subcategories"][sub_id]),
            "links": [{"target": ur_ref[cat_id], "type": "implements"}],
            "attrs": {"source_ref": sub_id},
        }
        rationale = about.get(sub_id, "")
        if rationale:
            item["rationale"] = rationale
        _dump(SUBCATS_DIR / f"{sr_uid}.yml", item)

    return counts


SPEC_HEADER = """\
# NIST AI RMF 1.0 \u2014 throughline source

Generated from the graph. Prose between `tl:item` / `tl:table` markers is injected by
`tl docs` \u2014 edit the vendored data (`tools/airmf-1.0/*.json`) + `tools/generate.py`, not the
injected regions.

The "why" spine is **multi-root by design**: the AI RMF Core's four Functions
(GOVERN / MAP / MEASURE / MANAGE) are four distinct reasons the framework exists \u2014 four root
`intent`s, not one umbrella. Each Category is a `user_requirement` that `derives_from` its
Function; each Subcategory is a `system_requirement` that `implements` its Category, carrying
the Playbook's "about this subcategory" prose as its `rationale`. The AI RMF id lives in
`attrs.source_ref` (`"GOVERN 1.1"`); the framework grades no outcome by level.
"""


def generate_spec() -> None:
    core = json.loads((DATA_DIR / "core.json").read_text(encoding="utf-8"))
    int_ref = _scan(INTENTS_DIR)
    ur_ref = _scan(CATEGORIES_DIR)
    parts = [SPEC_HEADER]
    for fn in FUNCTION_ORDER:
        parts.append(f"# {fn} \u2014 the root\n")
        parts.append(f"<!-- tl:item {int_ref[fn]} -->\n<!-- tl:end -->\n")
        cats = sorted((c for c in core["categories"] if c.split()[0] == fn), key=_cat_sort)
        for cat_id in cats:
            parts.append(f"## {cat_id}\n")
            parts.append(f"<!-- tl:item {ur_ref[cat_id]} -->\n<!-- tl:end -->\n")
            flt = ("type == 'system_requirement' and "
                   f"attrs.get('source_ref', '').startswith('{cat_id}.')")
            parts.append(f"<!-- tl:table {flt} -->\n<!-- tl:end -->\n")
    SPEC.parent.mkdir(parents=True, exist_ok=True)
    SPEC.write_text("\n".join(parts) + "\n", encoding="utf-8")


def main() -> int:
    c = generate()
    generate_spec()
    print(f"intents:       {c['int']} new (Functions / root intents)")
    print(f"categories:    {c['ur']} new (user_requirements)")
    print(f"subcategories: {c['sr']} new (system_requirements)")
    print(f"totals: {len(list(INTENTS_DIR.glob('INT-*.yml')))} INT, "
          f"{len(list(CATEGORIES_DIR.glob('UR-*.yml')))} UR, "
          f"{len(list(SUBCATS_DIR.glob('SR-*.yml')))} SR")
    print("next: run `tl docs` to inject content, then `tl check --strict`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
