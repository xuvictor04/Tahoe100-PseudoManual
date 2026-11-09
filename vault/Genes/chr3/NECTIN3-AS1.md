---
symbol: "NECTIN3-AS1"
type: "gene"
col: 14307
ensembl_id: "ENSG00000242242"
name: "NECTIN3 antisense RNA 1"
location: "3q13.13"
module: 10
arm: "+"
pooled_cpm: 8.77
n_lines_expressing: 31
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# NECTIN3-AS1

*NECTIN3 antisense RNA 1* — 3q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.39× (z +18.9, q 0e+00, up in 21 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.450× (z -7.2, q 3e-10, down in 19 of 27 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLG-AS1]] (+0.65, fdr 4e-05), [[GRID2]] (+0.63, fdr 2e-05), [[RAP2C-AS1]] (+0.59, fdr 5e-05); moves opposite to [[ARMC9]] (-0.55, fdr 4e-05), [[SGSM1]] (-0.47, fdr 3e-04), [[ANKS6]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CD96]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.39×** | +18.9 | 0e+00 | 21/25 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +8.2 | 7e-14 | 11/18 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +8.0 | 3e-13 | 2/7 (HOP62, A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +6.5 | 1e-08 | 1/7 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +6.3 | 3e-08 | 3/15 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.9 | 4e-07 | 9/27 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.5 | 5e-04 | 5/26 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.66×** | +4.4 | 8e-04 | 8/25 (A549, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.002 | 5/27 (SK-MEL-2, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +4.1 | 0.003 | 11/24 (SK-MEL-2, A549, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 9/22 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.016 | 7/24 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.6 | 0.016 | 6/27 (NCI-H23, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.023 | 6/26 (SK-MEL-2, RKO, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.027 | 7/24 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.029 | 7/26 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.041 | 3/25 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.041 | 7/25 (SK-MEL-2, A-172, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14307.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.450×** | -7.2 | 3e-10 | 19/27 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.561×** | -5.2 | 5e-05 | 13/25 (SNU-423, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -4.3 | 0.004 | 14/25 (HOP62, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.672×** | -3.6 | 0.047 | 13/24 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.050 | 8/26 (HS-578T, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.480×** | -3.5 | 0.050 | 9/24 (J82, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.690×** | -3.3 | 0.064 | 7/27 (A-427, SK-MEL-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -3.3 | 0.064 | 12/21 (A-427, A549, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.696× | -3.1 | 0.10 | 4/23 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.711× | -3.1 | 0.12 | 7/27 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 169 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.215× (z -10.0) |
| [[A-427 (line)]] | wt | 121 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0851× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 3.97 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.84× (z +10.7) | [[Fluvoxamine (drug)]] 0.05 µM 0.0489× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 6.36 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0754× (z -9.2) |
| [[A-172 (line)]] | wt | 3.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +12.7) | — |
| [[A549 (line)]] | wt | 5.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0817× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 3.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 4.51 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0725× (z -8.6) |
| [[SNU-423 (line)]] | alt | 3.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.31× (z +8.5) | — |
| [[A498 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.970 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLG-AS1]] | +0.65 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[GRID2]] | +0.63 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[RAP2C-AS1]] | +0.59 | +0.59 / +0.40 | both halves | 5e-05 | same gene group |
| [[TMLHE-AS1]] | +0.59 | +0.47 / +0.47 | both halves | 2e-05 | same gene group |
| [[STARD4-AS1]] | +0.58 | +0.43 / +0.47 | both halves | 3e-05 | same gene group |
| [[NPAS3]] | +0.56 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[TAFA2]] | +0.56 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[LINC01122]] | +0.56 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[CFAP418-AS1]] | +0.56 | +0.46 / +0.34 | both halves | 1e-04 | same gene group |
| [[MAD2L1-DT]] | +0.55 | +0.51 / +0.28 | both halves | 3e-04 |  |
| [[CRB1]] | +0.55 | +0.54 / +0.32 | both halves | 1e-04 |  |
| [[HDAC2-AS2]] | +0.54 | +0.48 / +0.37 | both halves | 7e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC9]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SGSM1]] | -0.47 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[ANKS6]] | -0.47 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[VPS8]] | -0.46 | -0.32 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NECTIN3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers NECTIN3-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[FLG-AS1]] | B | FLG-AS1 activity lowers NECTIN3-AS1's level | lines that do not express FLG-AS1 (22) vs lines expressing it (28) | 1.10× higher at baseline in the lines without FLG-AS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: FLRT2, CNRIP1, MARCHF4 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD96]] | B | NECTIN3-AS1 activity raises CD96's level | lines that do not express NECTIN3-AS1 (19) vs lines expressing it (31) | 2.17× lower at baseline in the lines without NECTIN3-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000228714, LINC02466, LRCH2 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (15.9, 20.0); signed map (32.3, -5.1). **Vector** length 43.6, 7.53% of its response variance represented; |z| ≥ 3 in 578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +18.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +8.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +4.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.2 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.2 | -3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | NECTIN3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q13.13 — chr3:110,888,384-111,071,553 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously PVRL3-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q1RN00](https://www.uniprot.org/uniprotkb/Q1RN00) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40813) · Entrez [100506555](https://www.ncbi.nlm.nih.gov/gene/100506555) · UniProt [Q1RN00](https://www.uniprot.org/uniprotkb/Q1RN00) · Ensembl [ENSG00000242242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242242)

## Data

Gene col 14307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14307); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14307]; `tensor/DDL_lfc|DDL_z.npy` [14307]; `embed/gene_vectors.npy` [14307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14307 or target_col == 14307). Every well: [[NECTIN3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NECTIN3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
