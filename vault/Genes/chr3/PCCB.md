---
symbol: "PCCB"
type: "gene"
col: 3520
ensembl_id: "ENSG00000114054"
name: "propionyl-CoA carboxylase subunit beta"
location: "3q22.3"
module: 175
arm: "+"
pooled_cpm: 48.09
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# PCCB

*propionyl-CoA carboxylase subunit beta* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.07× (z +6.0, q 1e-06, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.656× (z -9.3, q 9e-18, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPG2]] (+0.67, fdr 7e-06), [[ALG6]] (+0.67, fdr 1e-05), [[KDM1A]] (+0.62, fdr 7e-06); moves opposite to [[TUT7]] (-0.59, fdr 1e-05), [[RNF103-CHMP3]] (-0.56, fdr 1e-05), [[RP2]] (-0.55, fdr 1e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NFIA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.07×** | +6.0 | 1e-06 | 30/48 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.43×** | +5.6 | 6e-06 | 27/46 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +5.5 | 8e-06 | 30/49 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.36×** | +4.8 | 2e-04 | 25/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.27×** | +3.8 | 0.018 | 18/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.028 | 18/48 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.23×** | +3.3 | 0.081 | 14/48 (NCI-H23, PANC-1, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.3 | 0.081 | 13/35 (HT-29, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.098 | 20/47 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3520.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.656×** | -9.3 | 9e-18 | 40/48 (J82, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.589×** | -8.4 | 1e-14 | 38/48 (HOP62, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.771×** | -5.7 | 2e-06 | 27/48 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.771×** | -4.1 | 0.005 | 24/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.772×** | -4.1 | 0.005 | 24/48 (LoVo, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.787×** | -3.8 | 0.014 | 21/48 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.787×** | -3.6 | 0.028 | 14/48 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.811×** | -3.2 | 0.096 | 15/49 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.826× | -3.0 | 0.15 | 14/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 45.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -15.6) |
| [[LoVo (line)]] | wt | 38.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -8.9) |
| [[SW480 (line)]] | alt | 41.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | [[Selinexor (drug)]] 5 µM 0.597× (z -8.9) |
| [[A-427 (line)]] | wt | 92.4 | 1 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.3) ⚠ cell-cycle shift, explains ~54% of this change | [[Selinexor (drug)]] 5 µM 0.520× (z -9.3) |
| [[C32 (line)]] | wt | 50.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.6) |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.1) |
| [[KATO III (line)]] | alt | 33.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.94× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | — |
| [[PANC-1 (line)]] | alt | 74.8 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +8.8) ⚠ cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.600× (z -8.6) |
| [[CHP-212 (line)]] | wt | 46.4 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0747× (z -10.8) |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.334× (z -8.7) |
| [[HOP62 (line)]] | alt | 29.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.307× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 63.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.0) |
| [[RKO (line)]] | wt | 92.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SHP-77 (line)]] | alt | 61.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[A-172 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 83.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 96.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG2]] | +0.67 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ALG6]] | +0.67 | +0.76 / +0.52 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[KDM1A]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[TTC13]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RNPEP]] | +0.60 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[TM7SF3]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.60 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[WHAMMP1]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[NDC1]] | +0.59 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SEC61A2]] | +0.58 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GK5]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[SNRNP40]] | +0.57 | +0.67 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | -0.59 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[RNF103-CHMP3]] | -0.56 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[RP2]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SLC31A2]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ZNF701]] | -0.55 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[ADNP2]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ATP6V1D]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ERICH1]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CELF6]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ZNF165]] | -0.52 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[RBBP6]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SLC22A1]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIA]] | B | NFIA activity raises PCCB's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without NFIA | 0.058 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[LINC00571]] | B | LINC00571 activity lowers PCCB's level | lines that do not express LINC00571 (5) vs lines expressing it (45) | 1.80× higher at baseline in the lines without LINC00571 | 0.079 | ⚠ within organs, on part of the lines; also absent: KIFC3, NDRG1, DELEC1; maybe low, not absent |
| [[GPD1L]] | C | GPD1L activity raises PCCB's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without GPD1L | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.5, -14.7); signed map (-38.8, -15.4). **Vector** length 119, 33.5% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | +5.9 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +5.9 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.9 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.2 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.7 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.1 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.5 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | propionyl-CoA carboxylase subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:136,250,340-136,337,896 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Propionyl-CoA carboxylase subunits |
| Reactome | 12 pathways, smallest: Propionyl-CoA catabolism; Defective HLCS causes multiple carboxylase deficiency; Defects in biotin (Btn) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P05166](https://www.uniprot.org/uniprotkb/P05166) (Propionyl-CoA carboxylase beta chain, mitochondrial):

> This is one of the 2 subunits of the biotin-dependent propionyl-CoA carboxylase (PCC), a mitochondrial enzyme involved in the catabolism of odd chain fatty acids, branched-chain amino acids isoleucine, threonine, methionine, and valine and other metabolites. Propionyl-CoA carboxylase catalyzes the carboxylation of propionyl-CoA/propanoyl-CoA to D-methylmalonyl-CoA/(S)-methylmalonyl-CoA. Within the holoenzyme, the alpha subunit catalyzes the ATP-dependent carboxylation of the biotin carried by …

**Summary**, from NCBI Gene [5096](https://www.ncbi.nlm.nih.gov/gene/5096):

> The protein encoded by this gene is a subunit of the propionyl-CoA carboxylase (PCC) enzyme, which is involved in the catabolism of propionyl-CoA. PCC is a mitochondrial enzyme that probably acts as a dodecamer of six alpha subunits and six beta subunits. This gene encodes the beta subunit of PCC. Defects in this gene are a cause of propionic acidemia type II (PA-2). Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:8654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8654) · Entrez [5096](https://www.ncbi.nlm.nih.gov/gene/5096) · UniProt [P05166](https://www.uniprot.org/uniprotkb/P05166) · Ensembl [ENSG00000114054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114054)

## Data

Gene col 3520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3520); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3520]; `tensor/DDL_lfc|DDL_z.npy` [3520]; `embed/gene_vectors.npy` [3520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3520 or target_col == 3520). Every well: [[PCCB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCCB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
