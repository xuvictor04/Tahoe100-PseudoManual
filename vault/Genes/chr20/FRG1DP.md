---
symbol: "FRG1DP"
type: "gene"
col: 15998
ensembl_id: "ENSG00000282870"
name: "FSHD region gene 1 family member D, pseudogene"
location: "20q11.1"
module: 183
arm: "+"
pooled_cpm: 3.35
n_lines_expressing: 33
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# FRG1DP

*FSHD region gene 1 family member D, pseudogene* — 20q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.17× (z +6.6, q 3e-08, up in 1 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +4.7, q 4e-04, up in 7 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.413× (z -7.8, q 4e-12, down in 24 of 30 measured lines) ⚠ unreliable plate only. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.112×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRG1GP]] (+0.80, fdr 7e-06), [[FRG1BP]] (+0.72, fdr 7e-06), [[C1orf50]] (+0.68, fdr 7e-06); moves opposite to [[SLIT2]] (-0.60, fdr 2e-05), [[EIF4G3]] (-0.59, fdr 1e-05), [[NEK10]] (-0.55, fdr 1e-04).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FRG1JP]] → it (grade B ⚠); 4 go from it, the strongest it → [[PSMG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +6.6 | 3e-08 | 1/8 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +4.9 | 2e-04 | 11/30 (HOP62, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.7 | 4e-04 | 5/15 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +4.7 | 4e-04 | 7/26 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +4.3 | 0.002 | 8/30 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.003 | 5/30 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.006 | 10/30 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.020 | 4/25 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.48×** | +3.5 | 0.033 | 10/28 (Hs 766T, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +3.3 | 0.046 | 1/12 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +3.3 | 0.051 | 7/26 (NCI-H460, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.055 | 9/30 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.00×** | +3.2 | 0.062 | 4/26 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.413×** | -7.8 | 4e-12 | 24/30 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.638×** | -4.0 | 0.022 | 12/29 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.693× | -3.2 | 0.19 | 7/30 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | 0.503× | -3.2 | 0.19 | 8/27 (SHP-77, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.701× | -3.1 | 0.19 | 3/30 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[Olanzapine (drug)]] 5 µM |  | 0.783× | -3.0 | 0.23 | 10/30 (Hs 766T, A-427, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.112× (z -9.5) |
| [[A-172 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.505 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRG1GP]] | +0.80 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[FRG1BP]] | +0.72 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[C1orf50]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[USP30]] | +0.64 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[DUSP11]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[LINC00674]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[MINDY3]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ZNF14]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ZNF230]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[ZNF836]] | +0.62 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[FRG1FP]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MMUT]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLIT2]] | -0.60 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[EIF4G3]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[NEK10]] | -0.55 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[CYCS]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ITPR2]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[EHBP1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SCHIP1]] | -0.52 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[HOMER1]] | -0.52 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[PRKCE]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZNF407]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[IGF2BP3]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SLC20A2]] | -0.52 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1JP]] | B | FRG1JP activity raises FRG1DP's level | lines that do not express FRG1JP (23) vs lines expressing it (27) | 2.53× lower at baseline in the lines without FRG1JP | 0.065 | ⚠ within organs, on part of the lines; also absent: LSAMP, TRPV2, MSC; maybe low, not absent |
| [[FRG1FP]] | C | FRG1FP activity raises FRG1DP's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without FRG1FP | 0.091 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMG2]] | B | FRG1DP activity lowers PSMG2's level | lines that do not express FRG1DP (17) vs lines expressing it (33) | 1.32× higher at baseline in the lines without FRG1DP | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000237596, C9, GLIPR1 |
| [[MBIP]] | B | FRG1DP activity lowers MBIP's level | lines that do not express FRG1DP (17) vs lines expressing it (33) | 1.21× higher at baseline in the lines without FRG1DP | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000237596, C9, GLIPR1 |
| [[ZNF540]] | B | FRG1DP activity lowers ZNF540's level | lines that do not express FRG1DP (17) vs lines expressing it (33) | 1.37× higher at baseline in the lines without FRG1DP | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000237596, C9, GLIPR1 |
| [[PRKCA]] | B | FRG1DP activity raises PRKCA's level | lines that do not express FRG1DP (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without FRG1DP | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000237596, C9, GLIPR1 |

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.6, -5.5); signed map (-24.2, -9.9). **Vector** length 40.0, 6.05% of its response variance represented; |z| ≥ 3 in 608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.2 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.4 | +4.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.4 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.8 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.5 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | FSHD region gene 1 family member D, pseudogene |
| Locus type | pseudogene |
| Location | 20q11.1 — chr20:29,080,390-29,102,761 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51763) · Entrez [102723316](https://www.ncbi.nlm.nih.gov/gene/102723316) · Ensembl [ENSG00000282870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000282870)

## Data

Gene col 15998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15998); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15998]; `tensor/DDL_lfc|DDL_z.npy` [15998]; `embed/gene_vectors.npy` [15998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15998 or target_col == 15998). Every well: [[FRG1DP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRG1DP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
