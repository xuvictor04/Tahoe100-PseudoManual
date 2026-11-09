---
symbol: "YOD1"
type: "gene"
col: 11122
ensembl_id: "ENSG00000180667"
name: "YOD1 deubiquitinase"
location: "1q32.1"
module: 34
arm: "+"
pooled_cpm: 42.41
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 12
n_dd_up_clean: 21
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 17
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# YOD1

*YOD1 deubiquitinase* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +15.2, q 0e+00, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.683× (z -5.6, q 1e-05, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PFKFB2]] (+0.56, fdr 2e-05, ⚠ same locus), [[KLHL21]] (+0.56, fdr 3e-05), [[TMC7]] (+0.54, fdr 1e-05), [[DHRS9]] (+0.52, fdr 1e-05); moves opposite to [[WDPCP]] (-0.55, fdr 4e-05), [[ATF2]] (-0.44, fdr 2e-04), [[PACSIN2]] (-0.44, fdr 2e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[SERPINB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +15.2 | 0e+00 | 37/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +13.8 | 1e-40 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +10.9 | 2e-25 | 35/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +9.9 | 5e-21 | 38/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.96×** | +9.8 | 1e-20 | 42/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.92×** | +9.5 | 2e-19 | 41/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +8.3 | 1e-14 | 28/38 (AsPC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +8.1 | 3e-14 | 37/46 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +7.8 | 3e-13 | 41/47 (NCI-H1573, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +7.6 | 1e-12 | 33/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +7.4 | 9e-12 | 33/46 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +6.9 | 3e-10 | 31/46 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +6.6 | 2e-09 | 34/48 (AsPC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +6.2 | 2e-08 | 29/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.14×** | +5.8 | 2e-07 | 28/45 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.4 | 2e-06 | 32/46 (MIA PaCa-2, AN3 CA, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 2e-05 | 23/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.46×** | +4.9 | 2e-05 | 23/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11122.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.683×** | -5.6 | 1e-05 | 27/46 (Hs 766T, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.741×** | -4.3 | 0.006 | 22/46 (SW48, SW480, …) | all doses, stronger at high dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.748×** | -4.1 | 0.007 | 20/46 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Brimonidine (drug)]] 5 µM |  | **0.773×** | -3.8 | 0.019 | 16/47 (SW480, HT-29, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.824×** | -3.7 | 0.021 | 13/48 (SW48, SW480, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -3.6 | 0.030 | 17/46 (Hs 766T, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.787×** | -3.6 | 0.030 | 18/47 (Hs 766T, AsPC-1, …) | two highest doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.041 | 13/46 (J82, C32, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.800×** | -3.2 | 0.085 | 12/48 (SW48, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.811×** | -3.1 | 0.094 | 20/46 (AsPC-1, RKO, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.811×** | -3.1 | 0.094 | 12/47 (SW48, RKO, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.813×** | -3.1 | 0.097 | 13/46 (SW48, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 174 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -13.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.214× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 69.5 | 7 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.23× (z +12.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 93.9 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.00× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.232× (z -12.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -9.6) |
| [[PANC-1 (line)]] | alt | 21.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.9) | — |
| [[SW48 (line)]] | wt | 159 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0333× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.162× (z -9.3) |
| [[KATO III (line)]] | alt | 35.3 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +9.8) | — |
| [[A498 (line)]] | wt | 49.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +19.5) | — |
| [[A549 (line)]] | wt | 27.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 18.0 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 42.0 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.05× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 56.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -9.3) |
| [[HS-578T (line)]] | alt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 44.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.6) | — |
| [[LoVo (line)]] | wt | 88.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +11.3) | — |
| [[RKO (line)]] | wt | 42.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.79× (z +9.2) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 53.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 60.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -9.2) |
| [[SW480 (line)]] | alt | 48.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +11.5) | — |
| [[A-172 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFKFB2]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[KLHL21]] | +0.56 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[TMC7]] | +0.54 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[DHRS9]] | +0.52 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[HTR1D]] | +0.51 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[DSC2]] | +0.50 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SLC14A1]] | +0.49 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FST]] | +0.49 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[RHOF]] | +0.49 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TBILA]] | +0.49 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[C6orf141]] | +0.49 | +0.43 / +0.40 | both halves | 4e-05 |  |
| [[LINC01589]] | +0.49 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[IGDCC4]] | +0.48 | +0.36 / +0.46 | both halves | 9e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDPCP]] | -0.55 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ATF2]] | -0.44 | -0.45 / -0.31 | both halves | 2e-04 | same gene group |
| [[PACSIN2]] | -0.44 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[ZMYND8]] | -0.44 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[PIK3R1]] | -0.44 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[IMMT]] | -0.43 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[SSBP2]] | -0.43 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[ANGPTL4]] | -0.43 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[RBM6]] | -0.43 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[WWOX]] | -0.42 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[TTLL5]] | -0.42 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[SPATA6]] | -0.42 | -0.40 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB5]] | B | SERPINB5 activity raises YOD1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.40× lower at baseline in the lines without SERPINB5 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[LAMC2]] | B | LAMC2 activity raises YOD1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.94× lower at baseline in the lines without LAMC2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[PKP1]] | B | PKP1 activity raises YOD1's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 1.88× lower at baseline in the lines without PKP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[DSC2]] | B | DSC2 activity raises YOD1's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 1.85× lower at baseline in the lines without DSC2 | 0.025 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[LINC02582]] | B | LINC02582 activity raises YOD1's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.20× lower at baseline in the lines without LINC02582 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[LINC00520]] | B | LINC00520 activity raises YOD1's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 1.46× lower at baseline in the lines without LINC00520 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930 |
| [[KCNK1]] | B | KCNK1 activity raises YOD1's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.95× lower at baseline in the lines without KCNK1 | 0.042 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[SLC6A20]] | B | SLC6A20 activity raises YOD1's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 2.22× lower at baseline in the lines without SLC6A20 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[C4BPB]] | B | C4BPB activity raises YOD1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.01× lower at baseline in the lines without C4BPB | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[COL17A1]] | B | COL17A1 activity raises YOD1's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without COL17A1 | 0.051 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[MAP2K1]] | B | MAP2K1 activity raises YOD1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01589]] | B | LINC01589 activity raises YOD1's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 1.78× lower at baseline in the lines without LINC01589 | 0.058 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.0, 55.2); signed map (3.8, 34.0). **Vector** length 81.1, 19.2% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | +4.3 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +4.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.0 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | +6.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +5.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | YOD1 deubiquitinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:207,043,849-207,052,980 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp451J1719, OTUD2, DUBA8 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; OTU domain containing |
| Reactome | 2 pathways, smallest: Ovarian tumor domain proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VVQ6](https://www.uniprot.org/uniprotkb/Q5VVQ6) (Ubiquitin thioesterase OTU1):

> Hydrolase that can remove conjugated ubiquitin from proteins and participates in endoplasmic reticulum-associated degradation (ERAD) for misfolded lumenal proteins. May act by triming the ubiquitin chain on the associated substrate to facilitate their threading through the VCP/p97 pore. Ubiquitin moieties on substrates may present a steric impediment to the threading process when the substrate is transferred to the VCP pore and threaded through VCP's axial channel. Mediates deubiquitination of …

**Summary**, from NCBI Gene [55432](https://www.ncbi.nlm.nih.gov/gene/55432):

> Protein ubiquitination controls many intracellular processes, including cell cycle progression, transcriptional activation, and signal transduction. This dynamic process, involving ubiquitin conjugating enzymes and deubiquitinating enzymes, adds and removes ubiquitin. Deubiquitinating enzymes are cysteine proteases that specifically cleave ubiquitin from ubiquitin-conjugated protein substrates. The protein encoded by this gene belongs to a DUB subfamily characterized by an ovarian tumor (OTU) …

**Accessions** — [HGNC:25035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25035) · Entrez [55432](https://www.ncbi.nlm.nih.gov/gene/55432) · UniProt [Q5VVQ6](https://www.uniprot.org/uniprotkb/Q5VVQ6) · Ensembl [ENSG00000180667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180667)

## Data

Gene col 11122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11122); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11122]; `tensor/DDL_lfc|DDL_z.npy` [11122]; `embed/gene_vectors.npy` [11122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11122 or target_col == 11122). Every well: [[YOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
