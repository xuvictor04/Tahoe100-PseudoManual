---
symbol: "ZFP69"
type: "gene"
col: 11953
ensembl_id: "ENSG00000187815"
name: "ZFP69 zinc finger protein"
location: "1p34.2"
module: 33
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 43
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ZFP69

*ZFP69 zinc finger protein* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +7.1, q 1e-09, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.90× (z +6.6, q 5e-09, up in 16 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.356× (z -10.7, q 7e-24, down in 27 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHST10]] (+0.65, fdr 1e-05), [[PTPN20]] (+0.64, fdr 6e-05), [[EXO5]] (+0.61, fdr 7e-06, ⚠ same locus), [[TMEM139-AS1]] (+0.56, fdr 1e-05); moves opposite to [[DLEU2]] (-0.52, fdr 1e-04), [[TCF25]] (-0.50, fdr 3e-05), [[TRIM24]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[INTS6L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +7.1 | 1e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +6.8 | 2e-09 | 13/38 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +6.6 | 5e-09 | 16/39 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +6.6 | 5e-09 | 14/36 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.6 | 5e-09 | 10/28 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +4.9 | 8e-05 | 1/5 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.40×** | +4.9 | 8e-05 | 8/38 (SW480, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +4.6 | 3e-04 | 12/38 (J82, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.5 | 4e-04 | 9/36 (RKO, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +4.2 | 0.002 | 9/38 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.1 | 0.002 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.70×** | +3.9 | 0.004 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.004 | 6/36 (PANC-1, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.35×** | +3.1 | 0.078 | 1/38 (NCI-H2347) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.356×** | -10.7 | 7e-24 | 27/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -9.2 | 7e-18 | 18/24 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.450×** | -7.8 | 9e-13 | 20/37 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.583×** | -5.4 | 1e-05 | 17/36 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.701×** | -5.2 | 2e-05 | 18/32 (NCI-H460, LoVo, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.652×** | -4.3 | 0.002 | 8/38 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.727× | -3.2 | 0.12 | 4/38 (COLO 205, SW1417, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.733× | -3.1 | 0.14 | 9/33 (NCI-H460, HCT15, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.99 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 3.62 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -13.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[LoVo (line)]] | wt | 3.18 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -11.0) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Rosiglitazone (drug)]] 5 µM 0.0713× (z -9.6) |
| [[SW480 (line)]] | alt | 3.06 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -8.6) |
| [[Hs 766T (line)]] | wt | 2.97 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0460× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 4.14 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0698× (z -9.0) |
| [[A-172 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.877 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.592 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHST10]] | +0.65 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[PTPN20]] | +0.64 | +0.68 / +0.38 | both halves | 6e-05 |  |
| [[EXO5]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 | ⚠ same locus (12.4 kb, same strand: neighbours can correlate without regulation) |
| [[TMEM139-AS1]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ZFP69B]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 | same gene group; ⚠ same locus (13.6 kb, same strand: neighbours can correlate without regulation) |
| [[TRIM32]] | +0.54 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[ZNF174]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 | same gene group |
| [[ZNF232]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 | same gene group |
| [[BOLA3-DT]] | +0.54 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[TMSB15B]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[LRRC63]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[TBX1]] | +0.52 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[B3GALT9]] | +0.52 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[RAB4A-AS1]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU2]] | -0.52 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[TCF25]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TRIM24]] | -0.49 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[SELENOM]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TOM1L2]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[INAFM1]] | -0.44 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[INTS6L]] | -0.44 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[ABCA5]] | -0.44 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[MICU1]] | -0.43 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[NIHCOLE]] | -0.43 | -0.26 / -0.44 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises ZFP69's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.71× lower at baseline in the lines without MCOLN2 | 0.013 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[WT1-AS]] | B | WT1-AS activity raises ZFP69's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.61× lower at baseline in the lines without WT1-AS | 0.048 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[SEPTIN5]] | B | SEPTIN5 activity raises ZFP69's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.38× lower at baseline in the lines without SEPTIN5 | 0.066 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[KHDC1-AS1]] | B | KHDC1-AS1 activity raises ZFP69's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without KHDC1-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7 |
| [[ARHGEF25]] | B | ARHGEF25 activity raises ZFP69's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 1.53× lower at baseline in the lines without ARHGEF25 | 0.094 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INTS6L]] | B | ZFP69 activity raises INTS6L's level | lines that do not express ZFP69 (7) vs lines expressing it (43) | 4.14× lower at baseline in the lines without ZFP69 | 0.026 | ⚠ within organs, on part of the lines; also absent: FBXL2, ETV1, KIF3C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.458). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-37.7, 23.2); signed map (21.6, 26.7). **Vector** length 38.2, 4.48% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.8 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +7.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.9 | -0.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.1 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -1.9 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -7.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.6 | -9.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -0.7 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.7 | -0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ZFP69 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,477,290-40,496,343 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZKSCAN23A, FLJ16030, ZFP69A, ZSCAN54A; previously ZNF642 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49AA0](https://www.uniprot.org/uniprotkb/Q49AA0) (Zinc finger protein 69 homolog):

> Putative transcription factor that appears to regulate lipid metabolism.

**Summary**, from NCBI Gene [339559](https://www.ncbi.nlm.nih.gov/gene/339559):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of lipid metabolic process and regulation of transcription by RNA polymerase II. Predicted to be located in nuclear lumen. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24708) · Entrez [339559](https://www.ncbi.nlm.nih.gov/gene/339559) · UniProt [Q49AA0](https://www.uniprot.org/uniprotkb/Q49AA0) · Ensembl [ENSG00000187815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187815)

## Data

Gene col 11953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11953); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11953]; `tensor/DDL_lfc|DDL_z.npy` [11953]; `embed/gene_vectors.npy` [11953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11953 or target_col == 11953). Every well: [[ZFP69 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP69.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
