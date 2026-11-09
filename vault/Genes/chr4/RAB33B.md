---
symbol: "RAB33B"
type: "gene"
col: 10197
ensembl_id: "ENSG00000172007"
name: "RAB33B, member RAS oncogene family"
location: "4q31.1"
module: 41
arm: "+"
pooled_cpm: 23.85
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# RAB33B

*RAB33B, member RAS oncogene family* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +16.9, q 0e+00, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.626× (z -8.8, q 5e-16, down in 23 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.740× (z -5.7, q 2e-06, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM220A]] (+0.63, fdr 7e-06), [[FAM161B]] (+0.61, fdr 3e-05), [[RNASE4]] (+0.59, fdr 1e-05); moves opposite to [[SYMPK]] (-0.62, fdr 1e-05), [[LARS2]] (-0.60, fdr 1e-05), [[SPATA5]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +16.9 | 0e+00 | 37/47 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +10.6 | 7e-24 | 32/47 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +9.2 | 5e-18 | 33/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +9.2 | 7e-18 | 34/48 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +9.1 | 9e-18 | 33/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +6.2 | 6e-08 | 21/47 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +5.6 | 2e-06 | 20/48 (NCI-H460, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.004 | 13/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.006 | 10/47 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.014 | 17/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.022 | 12/48 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.19× | +3.5 | 0.022 | 14/48 (C-33 A, LS 180, …) | two highest doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.026 | 12/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.027 | 6/48 (HS-578T, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.045 | 11/48 (C32, LoVo, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.062 | 8/48 (NCI-H1573, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.17× | +3.0 | 0.096 | 2/48 (PANC-1, hTERT-HPNE) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -8.8 | 5e-16 | 23/35 (BT-474, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.644×** | -8.7 | 1e-15 | 30/43 (SW48, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.740×** | -5.7 | 2e-06 | 22/48 (NCI-H2347, SW 1088, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.789×** | -4.7 | 4e-04 | 18/46 (COLO 205, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.820×** | -3.9 | 0.011 | 18/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **0.826×** | -3.8 | 0.016 | 16/47 (RKO, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.701×** | -3.7 | 0.021 | 15/41 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.831×** | -3.6 | 0.021 | 18/48 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.834× | -3.5 | 0.025 | 14/48 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.836× | -3.5 | 0.025 | 18/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.838× | -3.5 | 0.028 | 21/47 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.843× | -3.3 | 0.038 | 15/47 (SW480, A-172, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.080 | 11/48 (CHP-212, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.190× (z -8.6) |
| [[COLO 205 (line)]] | alt | 22.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +9.8) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.167× (z -10.5) |
| [[LS 180 (line)]] | wt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.1) | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.172× (z -9.5) |
| [[A-172 (line)]] | wt | 18.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.248× (z -10.4) |
| [[A498 (line)]] | wt | 30.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.2) | — |
| [[A549 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 44.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -8.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 23.4 | 0 | 1 | — | [[SBI-0640756 (drug)]] 5 µM 0.0904× (z -8.6) |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.101× (z -8.9) ⚠ toxic |
| [[HT-29 (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.9) | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0924× (z -10.2) ⚠ toxic |
| [[KATO III (line)]] | alt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.5) | — |
| [[LoVo (line)]] | wt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 35.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +15.6) | — |
| [[NCI-H2347 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.147× (z -10.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +12.6) | — |
| [[A-427 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM220A]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[FAM161B]] | +0.61 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[RNASE4]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LNX2]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[NAGK]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[WDR47]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PRKAB2]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[BUD31]] | +0.57 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[CHCHD7]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[RAB1A]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 | same gene group; pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 453 |
| [[ANG]] | +0.56 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[ZBTB41]] | +0.56 | +0.67 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYMPK]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[LARS2]] | -0.60 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[SPATA5]] | -0.58 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[TANGO6]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[RTEL1]] | -0.55 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[C1orf159]] | -0.55 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[GNL3L]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[LYRM4]] | -0.54 | -0.60 / -0.44 | both halves | 3e-05 | STRING 553 |
| [[EFTUD2]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[CHCHD3]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RBM19]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RAB33B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises RAB33B's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-15.9, -30.2); signed map (-13.3, 2.4). **Vector** length 94.5, 20.2% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.2 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.2 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -5.0 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.8 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB33B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:139,453,232-139,476,609 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434G099 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 7 pathways, smallest: Intra-Golgi traffic; TBC/RABGAPs; RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H082](https://www.uniprot.org/uniprotkb/Q9H082) (Ras-related protein Rab-33B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB33B acts, in coordination with RAB6A, to regulate intra-Golgi retrograde trafficking. Participates in autophagosome …

**Summary**, from NCBI Gene [83452](https://www.ncbi.nlm.nih.gov/gene/83452):

> This gene encodes a small GTP-binding protein of the Rab GTPase family, whose members function in vesicle transport during protein secretion and endocytosis. Rab GTPases are active, membrane-associated proteins that recruit effector proteins in the GTP-bound state and inactive cytosolic proteins when in a GDP-bound state. The protein encoded by this gene is ubiquitously expressed and has been implicated in Golgi to endoplasmic reticulum cycling of Golgi enzymes. In addition, this protein …

**Accessions** — [HGNC:16075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16075) · Entrez [83452](https://www.ncbi.nlm.nih.gov/gene/83452) · UniProt [Q9H082](https://www.uniprot.org/uniprotkb/Q9H082) · Ensembl [ENSG00000172007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172007)

## Data

Gene col 10197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10197); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10197]; `tensor/DDL_lfc|DDL_z.npy` [10197]; `embed/gene_vectors.npy` [10197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10197 or target_col == 10197). Every well: [[RAB33B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB33B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
