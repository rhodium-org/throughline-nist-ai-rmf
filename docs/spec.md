# NIST AI RMF 1.0 — throughline source

Generated from the graph. Prose between `tl:item` / `tl:table` markers is injected by
`tl docs` — edit the vendored data (`tools/airmf-1.0/*.json`) + `tools/generate.py`, not the
injected regions.

The "why" spine is **multi-root by design**: the AI RMF Core's four Functions
(GOVERN / MAP / MEASURE / MANAGE) are four distinct reasons the framework exists — four root
`intent`s, not one umbrella. Each Category is a `user_requirement` that `derives_from` its
Function; each Subcategory is a `system_requirement` that `implements` its Category, carrying
the Playbook's "about this subcategory" prose as its `rationale`. The AI RMF id lives in
`attrs.source_ref` (`"GOVERN 1.1"`); the framework grades no outcome by level.

# GOVERN — the root

<!-- tl:item INT-0001 -->
**INT-0001 — GOVERN — Cultivate a culture of AI risk management** — `intent`, status `approved`

> A culture of risk management is cultivated and present. The GOVERN function cultivates and implements a culture of risk management within organizations designing, developing, deploying, evaluating, or acquiring AI systems, and provides a structure by which AI risk management functions can align with organizational principles, policies, and strategic priorities.

**source_ref**: GOVERN
<!-- tl:end -->

## GOVERN 1

<!-- tl:item UR-0001 -->
**UR-0001 — GOVERN 1** — `user_requirement`, status `approved`

> Policies, processes, procedures, and practices across the organization related to the mapping, measuring, and managing of AI risks are in place, transparent, and implemented effectively.

*Derives from:* INT-0001

**source_ref**: GOVERN 1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('GOVERN 1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | AI RMF GOVERN 1.1 |
| SR-0002 | system_requirement | approved | AI RMF GOVERN 1.2 |
| SR-0003 | system_requirement | approved | AI RMF GOVERN 1.3 |
| SR-0004 | system_requirement | approved | AI RMF GOVERN 1.4 |
| SR-0005 | system_requirement | approved | AI RMF GOVERN 1.5 |
| SR-0006 | system_requirement | approved | AI RMF GOVERN 1.6 |
| SR-0007 | system_requirement | approved | AI RMF GOVERN 1.7 |
<!-- tl:end -->

## GOVERN 2

<!-- tl:item UR-0002 -->
**UR-0002 — GOVERN 2** — `user_requirement`, status `approved`

> Accountability structures are in place so that the appropriate teams and individuals are empowered, responsible, and trained for mapping, measuring, and managing AI risks.

*Derives from:* INT-0001

**source_ref**: GOVERN 2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('GOVERN 2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0008 | system_requirement | approved | AI RMF GOVERN 2.1 |
| SR-0009 | system_requirement | approved | AI RMF GOVERN 2.2 |
| SR-0010 | system_requirement | approved | AI RMF GOVERN 2.3 |
<!-- tl:end -->

## GOVERN 3

<!-- tl:item UR-0003 -->
**UR-0003 — GOVERN 3** — `user_requirement`, status `approved`

> Workforce diversity, equity, inclusion, and accessibility processes are prioritized in the mapping, measuring, and managing of AI risks throughout the lifecycle.

*Derives from:* INT-0001

**source_ref**: GOVERN 3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('GOVERN 3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0011 | system_requirement | approved | AI RMF GOVERN 3.1 |
| SR-0012 | system_requirement | approved | AI RMF GOVERN 3.2 |
<!-- tl:end -->

## GOVERN 4

<!-- tl:item UR-0004 -->
**UR-0004 — GOVERN 4** — `user_requirement`, status `approved`

> Organizational teams are committed to a culture that considers and communicates AI risk.

*Derives from:* INT-0001

**source_ref**: GOVERN 4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('GOVERN 4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0013 | system_requirement | approved | AI RMF GOVERN 4.1 |
| SR-0014 | system_requirement | approved | AI RMF GOVERN 4.2 |
| SR-0015 | system_requirement | approved | AI RMF GOVERN 4.3 |
<!-- tl:end -->

## GOVERN 5

<!-- tl:item UR-0005 -->
**UR-0005 — GOVERN 5** — `user_requirement`, status `approved`

> Processes are in place for robust engagement with relevant AI actors.

*Derives from:* INT-0001

**source_ref**: GOVERN 5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('GOVERN 5.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0016 | system_requirement | approved | AI RMF GOVERN 5.1 |
| SR-0017 | system_requirement | approved | AI RMF GOVERN 5.2 |
<!-- tl:end -->

## GOVERN 6

<!-- tl:item UR-0006 -->
**UR-0006 — GOVERN 6** — `user_requirement`, status `approved`

> Policies and procedures are in place to address AI risks and benefits arising from third-party software and data and other supply chain issues.

*Derives from:* INT-0001

**source_ref**: GOVERN 6
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('GOVERN 6.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0018 | system_requirement | approved | AI RMF GOVERN 6.1 |
| SR-0019 | system_requirement | approved | AI RMF GOVERN 6.2 |
<!-- tl:end -->

# MAP — the root

<!-- tl:item INT-0002 -->
**INT-0002 — MAP — Recognise context and identify risks** — `intent`, status `approved`

> The context is recognized and risks related to context are identified. The MAP function establishes the context to frame risks related to an AI system, and recognizes and enumerates the interdependencies and risks of AI system activities across the AI lifecycle.

**source_ref**: MAP
<!-- tl:end -->

## MAP 1

<!-- tl:item UR-0007 -->
**UR-0007 — MAP 1** — `user_requirement`, status `approved`

> Context is established and understood.

*Derives from:* INT-0002

**source_ref**: MAP 1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MAP 1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0020 | system_requirement | approved | AI RMF MAP 1.1 |
| SR-0021 | system_requirement | approved | AI RMF MAP 1.2 |
| SR-0022 | system_requirement | approved | AI RMF MAP 1.3 |
| SR-0023 | system_requirement | approved | AI RMF MAP 1.4 |
| SR-0024 | system_requirement | approved | AI RMF MAP 1.5 |
| SR-0025 | system_requirement | approved | AI RMF MAP 1.6 |
<!-- tl:end -->

## MAP 2

<!-- tl:item UR-0008 -->
**UR-0008 — MAP 2** — `user_requirement`, status `approved`

> Categorization of the AI system is performed.

*Derives from:* INT-0002

**source_ref**: MAP 2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MAP 2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0026 | system_requirement | approved | AI RMF MAP 2.1 |
| SR-0027 | system_requirement | approved | AI RMF MAP 2.2 |
| SR-0028 | system_requirement | approved | AI RMF MAP 2.3 |
<!-- tl:end -->

## MAP 3

<!-- tl:item UR-0009 -->
**UR-0009 — MAP 3** — `user_requirement`, status `approved`

> AI capabilities, targeted usage, goals, and expected benefits and costs compared with appropriate benchmarks are understood.

*Derives from:* INT-0002

**source_ref**: MAP 3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MAP 3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0029 | system_requirement | approved | AI RMF MAP 3.1 |
| SR-0030 | system_requirement | approved | AI RMF MAP 3.2 |
| SR-0031 | system_requirement | approved | AI RMF MAP 3.3 |
| SR-0032 | system_requirement | approved | AI RMF MAP 3.4 |
| SR-0033 | system_requirement | approved | AI RMF MAP 3.5 |
<!-- tl:end -->

## MAP 4

<!-- tl:item UR-0010 -->
**UR-0010 — MAP 4** — `user_requirement`, status `approved`

> Risks and benefits are mapped for all components of the AI system including third-party software and data.

*Derives from:* INT-0002

**source_ref**: MAP 4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MAP 4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0034 | system_requirement | approved | AI RMF MAP 4.1 |
| SR-0035 | system_requirement | approved | AI RMF MAP 4.2 |
<!-- tl:end -->

## MAP 5

<!-- tl:item UR-0011 -->
**UR-0011 — MAP 5** — `user_requirement`, status `approved`

> Impacts to individuals, groups, communities, organizations, and society are characterized.

*Derives from:* INT-0002

**source_ref**: MAP 5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MAP 5.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0036 | system_requirement | approved | AI RMF MAP 5.1 |
| SR-0037 | system_requirement | approved | AI RMF MAP 5.2 |
<!-- tl:end -->

# MEASURE — the root

<!-- tl:item INT-0003 -->
**INT-0003 — MEASURE — Assess, analyse and track risks** — `intent`, status `approved`

> Identified risks are assessed, analyzed, and tracked. The MEASURE function employs quantitative, qualitative, or mixed-method tools, techniques, and methodologies to analyze, assess, benchmark, and monitor AI risk and related impacts.

**source_ref**: MEASURE
<!-- tl:end -->

## MEASURE 1

<!-- tl:item UR-0012 -->
**UR-0012 — MEASURE 1** — `user_requirement`, status `approved`

> Appropriate methods and metrics are identified and applied.

*Derives from:* INT-0003

**source_ref**: MEASURE 1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MEASURE 1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0038 | system_requirement | approved | AI RMF MEASURE 1.1 |
| SR-0039 | system_requirement | approved | AI RMF MEASURE 1.2 |
| SR-0040 | system_requirement | approved | AI RMF MEASURE 1.3 |
<!-- tl:end -->

## MEASURE 2

<!-- tl:item UR-0013 -->
**UR-0013 — MEASURE 2** — `user_requirement`, status `approved`

> AI systems are evaluated for trustworthy characteristics.

*Derives from:* INT-0003

**source_ref**: MEASURE 2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MEASURE 2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0041 | system_requirement | approved | AI RMF MEASURE 2.1 |
| SR-0042 | system_requirement | approved | AI RMF MEASURE 2.2 |
| SR-0043 | system_requirement | approved | AI RMF MEASURE 2.3 |
| SR-0044 | system_requirement | approved | AI RMF MEASURE 2.4 |
| SR-0045 | system_requirement | approved | AI RMF MEASURE 2.5 |
| SR-0046 | system_requirement | approved | AI RMF MEASURE 2.6 |
| SR-0047 | system_requirement | approved | AI RMF MEASURE 2.7 |
| SR-0048 | system_requirement | approved | AI RMF MEASURE 2.8 |
| SR-0049 | system_requirement | approved | AI RMF MEASURE 2.9 |
| SR-0050 | system_requirement | approved | AI RMF MEASURE 2.10 |
| SR-0051 | system_requirement | approved | AI RMF MEASURE 2.11 |
| SR-0052 | system_requirement | approved | AI RMF MEASURE 2.12 |
| SR-0053 | system_requirement | approved | AI RMF MEASURE 2.13 |
<!-- tl:end -->

## MEASURE 3

<!-- tl:item UR-0014 -->
**UR-0014 — MEASURE 3** — `user_requirement`, status `approved`

> Mechanisms for tracking identified AI risks over time are in place.

*Derives from:* INT-0003

**source_ref**: MEASURE 3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MEASURE 3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0054 | system_requirement | approved | AI RMF MEASURE 3.1 |
| SR-0055 | system_requirement | approved | AI RMF MEASURE 3.2 |
| SR-0056 | system_requirement | approved | AI RMF MEASURE 3.3 |
<!-- tl:end -->

## MEASURE 4

<!-- tl:item UR-0015 -->
**UR-0015 — MEASURE 4** — `user_requirement`, status `approved`

> Feedback about efficacy of measurement is gathered and assessed.

*Derives from:* INT-0003

**source_ref**: MEASURE 4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MEASURE 4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0057 | system_requirement | approved | AI RMF MEASURE 4.1 |
| SR-0058 | system_requirement | approved | AI RMF MEASURE 4.2 |
| SR-0059 | system_requirement | approved | AI RMF MEASURE 4.3 |
<!-- tl:end -->

# MANAGE — the root

<!-- tl:item INT-0004 -->
**INT-0004 — MANAGE — Prioritise and act on risks** — `intent`, status `approved`

> Risks are prioritized and acted upon based on a projected impact. The MANAGE function entails allocating risk resources to mapped and measured risks on a regular basis and as defined by the GOVERN function, so that AI risks are prioritized and acted upon based on a projected impact.

**source_ref**: MANAGE
<!-- tl:end -->

## MANAGE 1

<!-- tl:item UR-0016 -->
**UR-0016 — MANAGE 1** — `user_requirement`, status `approved`

> AI risks based on assessments and other analytical output from the MAP and MEASURE functions are prioritized, responded to, and managed.

*Derives from:* INT-0004

**source_ref**: MANAGE 1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MANAGE 1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0060 | system_requirement | approved | AI RMF MANAGE 1.1 |
| SR-0061 | system_requirement | approved | AI RMF MANAGE 1.2 |
| SR-0062 | system_requirement | approved | AI RMF MANAGE 1.3 |
| SR-0063 | system_requirement | approved | AI RMF MANAGE 1.4 |
<!-- tl:end -->

## MANAGE 2

<!-- tl:item UR-0017 -->
**UR-0017 — MANAGE 2** — `user_requirement`, status `approved`

> Strategies to maximize AI benefits and minimize negative impacts are planned, prepared, implemented, documented, and informed by input from relevant AI actors.

*Derives from:* INT-0004

**source_ref**: MANAGE 2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MANAGE 2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0064 | system_requirement | approved | AI RMF MANAGE 2.1 |
| SR-0065 | system_requirement | approved | AI RMF MANAGE 2.2 |
| SR-0066 | system_requirement | approved | AI RMF MANAGE 2.3 |
| SR-0067 | system_requirement | approved | AI RMF MANAGE 2.4 |
<!-- tl:end -->

## MANAGE 3

<!-- tl:item UR-0018 -->
**UR-0018 — MANAGE 3** — `user_requirement`, status `approved`

> AI risks and benefits from third-party entities are managed.

*Derives from:* INT-0004

**source_ref**: MANAGE 3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MANAGE 3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0068 | system_requirement | approved | AI RMF MANAGE 3.1 |
| SR-0069 | system_requirement | approved | AI RMF MANAGE 3.2 |
<!-- tl:end -->

## MANAGE 4

<!-- tl:item UR-0019 -->
**UR-0019 — MANAGE 4** — `user_requirement`, status `approved`

> Risk treatments, including response and recovery, and communication plans for the identified and measured AI risks are documented and monitored regularly.

*Derives from:* INT-0004

**source_ref**: MANAGE 4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref', '').startswith('MANAGE 4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0070 | system_requirement | approved | AI RMF MANAGE 4.1 |
| SR-0071 | system_requirement | approved | AI RMF MANAGE 4.2 |
| SR-0072 | system_requirement | approved | AI RMF MANAGE 4.3 |
<!-- tl:end -->

