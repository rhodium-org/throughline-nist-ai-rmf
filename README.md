# throughline-nist-ai-rmf

The **NIST AI Risk Management Framework (AI RMF) 1.0** (NIST AI 100-1) expressed as a
[throughline](https://pypi.org/project/throughline/) **source** — a standalone, grounded
requirements graph that a consuming project composes with
[throughline-compose](https://github.com/timebacksolutions/throughline-compose).

This repository holds no application code. It is a directory of small YAML items with
permanent UIDs, validated by `tl check`. Consumers import it under a namespace and
reference its outcomes as `airmf:SR-0007`.

## Status

A grounded graph of
<!-- tl:count type == 'intent' -->
4
<!-- tl:end --> Function intents,
<!-- tl:count type == 'user_requirement' -->
19
<!-- tl:end --> Category requirements and
<!-- tl:count type == 'system_requirement' -->
72
<!-- tl:end --> Subcategory outcomes, published to [`docs/spec.md`](docs/spec.md). The
counts are rendered from the live graph by `tl:count`, so they cannot drift.

## Why this source is multi-root

A throughline source gets **as many root intents as the standard has genuine "why"s** — a
single umbrella root would throw away the reason each outcome exists, which is the whole
point of IDD. A single artificial `INT-0001` that every requirement ultimately hangs off is
the **anti-pattern**: it flattens four distinct governance purposes into one bland "…exists".

The AI RMF Core is organised under **four Functions**, and those are four genuinely
different reasons the framework exists — governing the programme is not the same "why" as
mapping context, measuring risk, or managing response. So this graph has **four co-equal
root intents** (all `normative: false`), each carrying its Function's own AI RMF statement as
its `text`:

| Root | Function |
|---|---|
| `INT-0001` | **GOVERN** — cultivate a culture of AI risk management |
| `INT-0002` | **MAP** — recognise context and identify risks |
| `INT-0003` | **MEASURE** — assess, analyse and track risks |
| `INT-0004` | **MANAGE** — prioritise and act on risks |

- Each of the AI RMF's **19 Categories** (`GOVERN 1`, `MAP 2`, …) is a `user_requirement`
  that `derives_from` **its own Function** (a `MAP 2` category → `INT-0002`, never a
  catch-all), carrying the Category's Core statement as its `text`.
- Each of the **72 Subcategories** (`GOVERN 1.1`, …) is a `system_requirement` that
  `implements` its Category. The Core hierarchy is strict (one Function per Category), so a
  Subcategory grounds up to a Function through `implements` → `derives_from` with no extra
  edge. Each Subcategory carries the **Playbook's "about this subcategory" lead paragraph as
  its `rationale`** — the per-leaf *why*, the same role WCAG's "Intent of this Success
  Criterion" plays.

## No levels — editions are git tags

Unlike ASVS or AISVS, the AI RMF **grades no outcome by an assurance level**, so there is no
`attrs.level` here. The only published metadata carried is:

- `attrs.source_ref` — the published AI RMF identifier (`GOVERN 1.1` for a Subcategory,
  `GOVERN 1` for a Category, `GOVERN` for a Function), never the UID.

**Editions are git tags of this one repo.** `v1.0` tags the AI RMF 1.0 edition; a future AI
RMF revision would be a new tag on this same repo. A consumer pins `airmf@v1.0`. This is the
same editions-as-tags model as `throughline-asvs`, `throughline-aisvs` and `throughline-wcag`.

## Modelling conventions

- **throughline UIDs are this source's own** (`SR-0007`…), immutable and never the AI RMF
  identifier. The AI RMF id lives in `attrs.source_ref`.
- **Item `text`** is the AI RMF Core statement (Function / Category / Subcategory outcome); a
  Subcategory's `rationale` is the Playbook's "about this subcategory" prose. All come from
  the authoritative NIST source (see `NOTICE`).
- The graph is generated from the vendored NIST data under `tools/airmf-1.0/`
  (`core.json` = the Core statements, `playbook.json` = the raw Playbook) by
  `tools/generate.py` (permanent-UID, additive). Editing the graph means editing the
  vendored data + generator, not the YAML by hand.

## Composing it

In a consuming project's `throughline.toml`:

```toml
[sources.airmf]
url = "https://github.com/timebacksolutions/throughline-nist-ai-rmf"
ref = "v1.0"
```

Then reference an outcome as `airmf:SR-0001` (legal & regulatory requirements understood) from
your own items. The AI RMF is the natural **governance-layer** partner to
[`throughline-aisvs`](https://github.com/timebacksolutions/throughline-aisvs): AISVS verifies an AI
application's *controls*, while the AI RMF frames how an organisation *governs, maps,
measures and manages* AI risk — a consumer can compose both.

## Licence

Repository structure, tooling and configuration: Apache-2.0 (see `LICENSE`). The AI RMF
Function/Category/Subcategory statements and Playbook descriptions are works of the US
Federal Government in the **public domain** (17 U.S.C. § 105) — see `NOTICE`. Authoritative
source: https://www.nist.gov/itl/ai-risk-management-framework.
