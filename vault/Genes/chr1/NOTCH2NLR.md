---
symbol: "NOTCH2NLR"
type: "gene"
col: 16195
ensembl_id: "ENSG00000286106"
name: "notch 2 N-terminal like R"
location: "1p11.2"
module: 52
arm: "-"
pooled_cpm: 2.25
n_lines_expressing: 41
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# NOTCH2NLR

*notch 2 N-terminal like R* — 1p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.57× (z +12.4, q 2e-32, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.781× (z -8.1, q 2e-13, down in 28 of 37 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ciclopirox (drug)]] 5 µM in 1 line (HEC-1-A 0.153×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0829×; ⚠ toxic; cell-cycle shift, explains ~32% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.107×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (HS-578T 0.0750×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF26]] (+0.72, fdr 7e-06, ⚠ same locus), [[NOTCH2NLB]] (+0.53, fdr 2e-05), [[UST]] (+0.52, fdr 3e-05), [[NOTCH2NLC]] (+0.50, fdr 1e-05); moves opposite to [[GAK]] (-0.54, fdr 4e-05), [[AREL1]] (-0.52, fdr 2e-05), [[TRAPPC10]] (-0.51, fdr 5e-05).
> It sits in the **-** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NBPF26]] → it (grade C ⚠); 4 go from it, the strongest it → [[NBPF26]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +12.4 | 2e-32 | 19/25 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +6.3 | 9e-08 | 12/24 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.4 | 1e-05 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +5.3 | 2e-05 | 16/37 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +5.1 | 4e-05 | 12/33 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.5 | 6e-04 | 7/16 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +4.1 | 0.003 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.0 | 0.005 | 7/20 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.011 | 5/28 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.011 | 7/35 (C32, H4, …) | rises with dose | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.75×** | +3.7 | 0.011 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.46×** | +3.5 | 0.025 | 2/37 (NCI-H2347, A-172) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.026 | 4/31 (SK-MEL-2, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +3.1 | 0.066 | 5/36 (NCI-H2347, A498, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.072 | 6/26 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16195.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ciclopirox (drug)]] 5 µM in 1 line (HEC-1-A 0.153×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0829×; ⚠ toxic; cell-cycle shift, explains ~32% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.107×); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (HS-578T 0.0750×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.781×** | -8.1 | 2e-13 | 28/37 (AN3 CA, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 4.12 | 0 | 2 | — | [[Ciclopirox (drug)]] 5 µM 0.153× (z -11.1) |
| [[HS-578T (line)]] | alt | 4.47 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0750× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 9.71 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0829× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.131 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.154 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.809 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.804 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.156 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.167 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.805 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.917 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*22 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF26]] | +0.72 | +0.66 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NOTCH2NLB]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 | pathway: Expression of NOTCH2NL genes |
| [[UST]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[NOTCH2NLC]] | +0.50 | +0.51 / +0.51 | both halves | 1e-05 | pathway: Expression of NOTCH2NL genes |
| [[NBPF19]] | +0.48 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[NBPF10]] | +0.47 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[WASHC4]] | +0.47 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[VPS13C]] | +0.47 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[ZC2HC1A]] | +0.46 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ZC3H6]] | +0.45 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[PCLO]] | +0.45 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[NOTCH2]] | +0.45 | +0.32 / +0.46 | both halves | 2e-04 | pathway: Pre-NOTCH Expression and Processing |
| [[ATP23]] | +0.45 | +0.53 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*78 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAK]] | -0.54 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[AREL1]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[TRAPPC10]] | -0.51 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[TMEM248]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[STRAP]] | -0.51 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[EP400P1]] | -0.51 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[MBD1]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TIMM23]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[NIPA2]] | -0.50 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[CDK11B]] | -0.50 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[STARD3]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SENP5]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBPF26]] | C | NBPF26 activity raises NOTCH2NLR's level | lines that do not express NBPF26 (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without NBPF26 | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBPF26]] | B | NOTCH2NLR activity raises NBPF26's level | lines that do not express NOTCH2NLR (9) vs lines expressing it (41) | 3.34× lower at baseline in the lines without NOTCH2NLR | 2e-04 | ⚠ within organs, on part of the lines |
| [[ZC2HC1A]] | B | NOTCH2NLR activity raises ZC2HC1A's level | lines that do not express NOTCH2NLR (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without NOTCH2NLR | 0.038 | ⚠ within organs, on part of the lines |
| [[TRAPPC10]] | B | NOTCH2NLR activity raises TRAPPC10's level | lines that do not express NOTCH2NLR (9) vs lines expressing it (41) | 1.33× lower at baseline in the lines without NOTCH2NLR | 0.094 | ⚠ within organs, on part of the lines |
| [[TUBGCP6]] | B | NOTCH2NLR activity raises TUBGCP6's level | lines that do not express NOTCH2NLR (9) vs lines expressing it (41) | 1.28× lower at baseline in the lines without NOTCH2NLR | 0.097 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (1.4, -28.7); signed map (43.9, -15.8). **Vector** length 27.7, 2.34% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +1.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +12.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.3 | +6.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.6 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +0.5 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.5 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | -1.7 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -0.9 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | -1.4 |
|  | [[Arbutin (drug)]] 0.5 µM |  | -0.6 | -1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.6 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.5 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | notch 2 N-terminal like R |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p11.2 — chr1:120,723,912-120,794,851 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 4 pathways, smallest: Expression of NOTCH2NL genes; Pre-NOTCH Transcription and Translation; Pre-NOTCH Expression and Processing |
| Matched by | ensembl_id |

UniProt [A0A096LNW5](https://www.uniprot.org/uniprotkb/A0A096LNW5) carries no function annotation.

**Summary**, from NCBI Gene [101929796](https://www.ncbi.nlm.nih.gov/gene/101929796):

> Predicted to enable calcium ion binding activity. Predicted to be involved in animal organ development; positive regulation of signal transduction; and system development. Located in nucleoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:53925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53925) · Entrez [101929796](https://www.ncbi.nlm.nih.gov/gene/101929796) · UniProt [A0A096LNW5](https://www.uniprot.org/uniprotkb/A0A096LNW5) · Ensembl [ENSG00000286106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000286106)

## Data

Gene col 16195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16195); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16195]; `tensor/DDL_lfc|DDL_z.npy` [16195]; `embed/gene_vectors.npy` [16195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16195 or target_col == 16195). Every well: [[NOTCH2NLR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOTCH2NLR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
