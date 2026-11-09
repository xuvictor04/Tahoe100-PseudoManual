---
symbol: "WDR5B"
type: "gene"
col: 12316
ensembl_id: "ENSG00000196981"
name: "WD repeat domain 5B"
location: "3q21.1"
module: 10
arm: "+"
pooled_cpm: 2.75
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# WDR5B

*WD repeat domain 5B* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.62× (z +10.7, q 6e-24, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +10.6, q 7e-24, up in 18 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.529× (z -7.4, q 1e-10, down in 16 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.581× (z -6.3, q 9e-08, down in 19 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOCS3]] (+0.64, fdr 1e-05), [[CTBP1-DT]] (+0.62, fdr 3e-05), [[KPTN]] (+0.59, fdr 4e-05); moves opposite to [[KLHL8]] (-0.54, fdr 2e-04), [[KYAT1]] (-0.50, fdr 5e-04), [[RECK]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +10.7 | 6e-24 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +10.6 | 7e-24 | 18/35 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.38×** | +10.0 | 2e-21 | 31/45 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +10.0 | 2e-21 | 17/32 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +8.0 | 1e-13 | 2/4 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.7 | 2e-12 | 5/14 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +6.8 | 7e-10 | 14/42 (SHP-77, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +6.8 | 7e-10 | 14/33 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +6.2 | 4e-08 | 9/43 (HT-29, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.6 | 1e-06 | 10/43 (HEC-1-A, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +5.6 | 1e-06 | 9/43 (SHP-77, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.5 | 2e-06 | 4/25 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +5.5 | 2e-06 | 9/40 (HEC-1-A, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +4.3 | 7e-04 | 3/38 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.002 | 6/31 (HS-578T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Menadione (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.006 | 6/30 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +3.6 | 0.013 | 1/28 (BT-474) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.014 | 5/40 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12316.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -7.4 | 1e-10 | 16/24 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.581×** | -6.3 | 9e-08 | 19/46 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.583×** | -6.2 | 9e-08 | 17/40 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.623×** | -5.5 | 6e-06 | 14/39 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -3.6 | 0.035 | 13/42 (J82, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 0.05 µM |  | 0.753× | -3.3 | 0.10 | 6/38 (RKO, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 4.06 | 0 | 3 | — | [[Erlotinib (drug)]] 5 µM 0.0629× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 5.37 | 0 | 2 (2 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0543× (z -12.2) ⚠ transcription drop |
| [[A549 (line)]] | wt | 3.23 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0388× (z -10.5) |
| [[COLO 205 (line)]] | alt | 5.36 | 0 | 1 | — | [[Cloxacillin (sodium) (drug)]] 0.5 µM 0.0485× (z -9.2) |
| [[SW1417 (line)]] | alt | 5.10 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0945× (z -9.1) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOCS3]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[CTBP1-DT]] | +0.62 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[KPTN]] | +0.59 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[C11orf71]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[FNBP1P1]] | +0.58 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[PDCL3P4]] | +0.58 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[TMEM44-AS1]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[RELA-DT]] | +0.57 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[LINC00174]] | +0.57 | +0.67 / +0.34 | both halves | 1e-04 |  |
| [[CATSPERD]] | +0.57 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[CCT6B]] | +0.56 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[C19orf54]] | +0.56 | +0.60 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL8]] | -0.54 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[KYAT1]] | -0.50 | -0.60 / -0.23 | both halves | 5e-04 |  |
| [[RECK]] | -0.50 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[SGPP1]] | -0.50 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[GLMN]] | -0.49 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[STARD9]] | -0.49 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[ZYG11A]] | -0.48 | -0.42 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers WDR5B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.5, 13.6); signed map (28.2, -13.3). **Vector** length 40.2, 4.14% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +5.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -5.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -7.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | +0.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:122,411,846-122,416,062 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11287 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VZ2](https://www.uniprot.org/uniprotkb/Q86VZ2) (WD repeat-containing protein 5B):

> Plays a role in the proliferation of retinal pigment epithelial (RPE) cells. May function as a substrate receptor for CUL4-DDB1 ubiquitin E3 ligase complex (By similarity).

**Summary**, from NCBI Gene [54554](https://www.ncbi.nlm.nih.gov/gene/54554):

> This intronless gene encodes a protein containing several WD40 repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, including a trp-asp at the C-terminal end. The encoded protein may mediate protein-protein interactions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17826) · Entrez [54554](https://www.ncbi.nlm.nih.gov/gene/54554) · UniProt [Q86VZ2](https://www.uniprot.org/uniprotkb/Q86VZ2) · Ensembl [ENSG00000196981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196981)

## Data

Gene col 12316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12316); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12316]; `tensor/DDL_lfc|DDL_z.npy` [12316]; `embed/gene_vectors.npy` [12316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12316 or target_col == 12316). Every well: [[WDR5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
