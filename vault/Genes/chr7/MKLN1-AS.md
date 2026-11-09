---
symbol: "MKLN1-AS"
type: "gene"
col: 14096
ensembl_id: "ENSG00000236753"
name: "MKLN1 antisense RNA"
location: "7q32.3"
module: 35
arm: "+"
pooled_cpm: 4.61
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MKLN1-AS

*MKLN1 antisense RNA* — 7q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.81× (z +22.4, q 0e+00, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.539× (z -7.3, q 9e-11, down in 22 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.540× (z -7.3, q 9e-11, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MALINC1]] (+0.68, fdr 1e-05), [[LINC01090]] (+0.67, fdr 1e-05), [[NXT2]] (+0.67, fdr 1e-05); moves opposite to [[PIGU]] (-0.68, fdr 1e-05), [[WRAP73]] (-0.65, fdr 2e-05), [[WRN]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SATB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.81×** | +22.4 | 0e+00 | 35/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +11.7 | 2e-29 | 6/6 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +10.5 | 2e-23 | 18/23 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.6 | 7e-20 | 24/47 (SW1417, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.16×** | +9.1 | 9e-18 | 28/42 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +9.1 | 9e-18 | 19/46 (A498, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +8.5 | 1e-15 | 9/12 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +7.5 | 4e-12 | 18/35 (RKO, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +7.3 | 2e-11 | 16/34 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.4 | 1e-08 | 19/46 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +6.0 | 8e-08 | 20/47 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +5.4 | 3e-06 | 17/42 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +4.6 | 2e-04 | 9/37 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +4.3 | 6e-04 | 13/47 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.008 | 12/38 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.012 | 4/45 (Panc 03.27, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.030 | 5/46 (KATO III, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.050 | 1/43 (SW480) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -7.3 | 9e-11 | 22/34 (NCI-H2030, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.540×** | -7.3 | 9e-11 | 23/47 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -5.6 | 3e-06 | 18/46 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.675×** | -4.7 | 5e-04 | 14/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.652×** | -4.5 | 7e-04 | 13/42 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.553×** | -3.7 | 0.020 | 11/37 (Panc 03.27, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | **0.804×** | -3.7 | 0.020 | 6/47 (Panc 03.27, SNU-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.768× | -3.1 | 0.13 | 6/45 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 2.22 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.47× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 7.54 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0778× (z -8.7) |
| [[Hs 766T (line)]] | wt | 3.36 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0505× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.123× (z -9.4) |
| [[PANC-1 (line)]] | alt | 6.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 5.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +9.0) | — |
| [[SW480 (line)]] | alt | 4.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +9.6) | — |
| [[A-172 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALINC1]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[LINC01090]] | +0.67 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[NXT2]] | +0.67 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[UPK2]] | +0.67 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[BHLHE40-AS1]] | +0.67 | +0.59 / +0.45 | both halves | 3e-05 | same gene group |
| [[STX17-DT]] | +0.67 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.66 | +0.60 / +0.49 | both halves | 1e-05 | same gene group |
| [[DRAIC]] | +0.66 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.65 | +0.59 / +0.51 | both halves | 1e-05 | same gene group |
| [[SAXO1]] | +0.65 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[SPEN-AS1]] | +0.65 | +0.60 / +0.48 | both halves | 2e-05 | same gene group |
| [[HIVEP2-DT]] | +0.65 | +0.65 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGU]] | -0.68 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[WRAP73]] | -0.65 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[WRN]] | -0.64 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[NPHP4]] | -0.64 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[HERC2P9]] | -0.61 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MRPS34]] | -0.60 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[RBM6]] | -0.60 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[EIF2B3]] | -0.59 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[HERC2P2]] | -0.59 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[TTC38]] | -0.58 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[CDK5RAP1]] | -0.58 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[PUSL1]] | -0.58 | -0.50 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SATB1]] | B | SATB1 activity lowers MKLN1-AS's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.40× higher at baseline in the lines without SATB1 | 0.007 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[TOP2A]] | B | TOP2A activity lowers MKLN1-AS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SATB1-AS1]] | B | SATB1-AS1 activity lowers MKLN1-AS's level | lines that do not express SATB1-AS1 (12) vs lines expressing it (38) | 1.35× higher at baseline in the lines without SATB1-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: CMKLR2, ENSG00000289609; maybe low, not absent |
| [[CCN3]] | B | CCN3 activity lowers MKLN1-AS's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 1.35× higher at baseline in the lines without CCN3 | 0.039 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (13.6, 19.1); signed map (28.1, -1.9). **Vector** length 55.6, 7.48% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +22.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -4.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -0.9 | -2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | MKLN1 antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q32.3 — chr7:131,309,469-131,328,312 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously MKLN1-AS2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40374) · Entrez [100506881](https://www.ncbi.nlm.nih.gov/gene/100506881) · Ensembl [ENSG00000236753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236753)

## Data

Gene col 14096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14096); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14096]; `tensor/DDL_lfc|DDL_z.npy` [14096]; `embed/gene_vectors.npy` [14096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14096 or target_col == 14096). Every well: [[MKLN1-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKLN1-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
