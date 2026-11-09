---
symbol: "TNFRSF10A"
type: "gene"
col: 2483
ensembl_id: "ENSG00000104689"
name: "TNF receptor superfamily member 10a"
location: "8p21.3"
module: 110
arm: "+"
pooled_cpm: 41.14
n_lines_expressing: 40
n_dd_up: 17
n_dd_down: 26
n_dd_up_clean: 13
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# TNFRSF10A

*TNF receptor superfamily member 10a* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.94× (z +11.7, q 7e-29, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.600× (z -9.1, q 5e-17, down in 33 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM89A]] (+0.63, fdr 1e-05), [[UBASH3B]] (+0.61, fdr 7e-06), [[INSYN2A]] (+0.59, fdr 4e-05); moves opposite to [[EHMT2]] (-0.50, fdr 2e-05), [[ALDH1A1]] (-0.50, fdr 5e-05), [[CDC73]] (-0.50, fdr 5e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EPHA2]] → it (grade B ⚠); 7 go from it, the strongest it → [[EPHA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +11.7 | 7e-29 | 35/38 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +9.8 | 5e-20 | 33/38 (KATO III, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +9.5 | 4e-19 | 33/38 (KATO III, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.4 | 1e-18 | 22/37 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.8 | 1e-09 | 26/37 (Panc 03.27, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.7 | 2e-09 | 25/38 (COLO 205, A549, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.5 | 6e-09 | 22/38 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +6.2 | 5e-08 | 23/38 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.8 | 5e-07 | 22/38 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +5.4 | 3e-06 | 21/38 (A549, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 4e-04 | 13/38 (LoVo, A549, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.29×** | +4.3 | 8e-04 | 16/36 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.1 | 0.001 | 12/25 (A549, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 17/38 (HOP62, HS-578T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.9 | 0.004 | 14/38 (NCI-H460, RKO, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.015 | 16/38 (SW480, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.024 | 18/38 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.054 | 12/38 (MIA PaCa-2, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.600×** | -9.1 | 5e-17 | 33/38 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.641×** | -7.8 | 2e-12 | 22/38 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.736×** | -7.3 | 5e-11 | 27/38 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.678×** | -6.8 | 1e-09 | 27/38 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.700×** | -6.8 | 1e-09 | 25/38 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.730×** | -6.6 | 3e-09 | 27/38 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.687×** | -6.3 | 2e-08 | 25/38 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.694×** | -6.2 | 5e-08 | 25/38 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.702×** | -6.0 | 1e-07 | 21/33 (HCT15, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.695×** | -5.9 | 2e-07 | 24/38 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.722×** | -5.7 | 6e-07 | 24/39 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.738×** | -5.3 | 5e-06 | 20/38 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.770×** | -5.2 | 9e-06 | 22/38 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.728×** | -5.2 | 1e-05 | 19/35 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.760×** | -4.8 | 6e-05 | 18/38 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.820×** | -4.7 | 1e-04 | 16/38 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.612×** | -4.5 | 2e-04 | 18/37 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 54.2 | 3 | 8 | [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +9.7) | [[Trametinib (drug)]] 5 µM 0.442× (z -10.9) |
| [[A498 (line)]] | wt | 65.2 | 6 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 47.8 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +19.2) | — |
| [[RKO (line)]] | wt | 101 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +17.3) | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 104 | 5 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +14.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 77.2 | 1 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +8.5) | [[Adagrasib (drug)]] 0.05 µM 0.566× (z -20.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.428× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 60.4 | 0 | 5 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.624× (z -14.8) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.333× (z -10.4) |
| [[KATO III (line)]] | alt | 53.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.97× (z +10.6) | — |
| [[LoVo (line)]] | wt | 51.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +19.1) | — |
| [[LS 180 (line)]] | wt | 62.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +15.8) | — |
| [[BT-474 (line)]] | alt | 50.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -9.2) |
| [[HCT15 (line)]] | alt | 91.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -11.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 57.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +12.5) | — |
| [[A-427 (line)]] | wt | 62.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.405× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 71.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 66.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.400× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.63× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.34 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89A]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[UBASH3B]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[INSYN2A]] | +0.59 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[SPRY4-AS1]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ACER2]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[S100A11]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PNP]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ANKRD13B]] | +0.52 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ZNF562]] | +0.52 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[GSTO1]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[IL17RA]] | +0.51 | +0.43 / +0.56 | both halves | 3e-05 | same gene group |
| [[SFN]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 | pathway: Apoptosis |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHMT2]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ALDH1A1]] | -0.50 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[CDC73]] | -0.50 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[ZMYM3]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[MPP7]] | -0.49 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[HINT3]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[TPM1]] | -0.48 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[BACE1-AS]] | -0.48 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[ALDH3B1]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[HTATSF1]] | -0.47 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[C4orf33]] | -0.46 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[SCRN3]] | -0.46 | -0.39 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | EPHA2 activity raises TNFRSF10A's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 3.75× lower at baseline in the lines without EPHA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[UPP1]] | B | UPP1 activity raises TNFRSF10A's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.96× lower at baseline in the lines without UPP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[GALNT14]] | B | GALNT14 activity raises TNFRSF10A's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 2.10× lower at baseline in the lines without GALNT14 | 0.070 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[MAP2K1]] | B | MAP2K1 activity raises TNFRSF10A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ITGA2]] | B | ITGA2 activity raises TNFRSF10A's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without ITGA2 | 0.082 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[CDCP1]] | C | CDCP1 activity raises TNFRSF10A's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 4.39× lower at baseline in the lines without CDCP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | TNFRSF10A activity raises EPHA2's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 3.88× lower at baseline in the lines without TNFRSF10A | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1 |
| [[S100A11]] | B | TNFRSF10A activity raises S100A11's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 1.86× lower at baseline in the lines without TNFRSF10A | 0.011 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1 |
| [[UPP1]] | B | TNFRSF10A activity raises UPP1's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without TNFRSF10A | 0.036 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1 |
| [[NTSR1]] | B | TNFRSF10A activity raises NTSR1's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without TNFRSF10A | 0.045 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1 |
| [[ASAP2]] | B | TNFRSF10A activity raises ASAP2's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without TNFRSF10A | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1 |
| [[CDCP1]] | C | TNFRSF10A activity raises CDCP1's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 6.99× lower at baseline in the lines without TNFRSF10A | 0.004 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1; co-absent with the target |
| [[TNFRSF10D]] | C | TNFRSF10A activity raises TNFRSF10D's level | lines that do not express TNFRSF10A (10) vs lines expressing it (40) | 4.38× lower at baseline in the lines without TNFRSF10A | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, SLC16A5, CDCP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.3, 5.9); signed map (-3.6, 40.7). **Vector** length 123, 35.4% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.1 | +9.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.9 | +11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +2.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.6 | -9.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.7 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.7 | -6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.6 | -6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.4 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 10a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:23,190,452-23,225,102 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DR4, Apo2, TRAILR-1, CD261, TRAILR1 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Reactome | 17 pathways, smallest: TRAIL  signaling; CASP8 activity is inhibited; Dimerization of procaspase-8 |
| Matched by | ensembl_id |

**Function**, from UniProt [O00220](https://www.uniprot.org/uniprotkb/O00220) (Tumor necrosis factor receptor superfamily member 10A):

> Receptor for the cytotoxic ligand TNFSF10/TRAIL. The adapter molecule FADD recruits caspase-8 to the activated receptor. The resulting death-inducing signaling complex (DISC) performs caspase-8 proteolytic activation which initiates the subsequent cascade of caspases (aspartate-specific cysteine proteases) mediating apoptosis. Promotes the activation of NF-kappa-B.

**Summary**, from NCBI Gene [8797](https://www.ncbi.nlm.nih.gov/gene/8797):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptor is activated by tumor necrosis factor-related apoptosis inducing ligand (TNFSF10/TRAIL), and thus transduces cell death signal and induces cell apoptosis. Studies with FADD-deficient mice suggested that FADD, a death domain containing adaptor protein, is required for the apoptosis mediated by this protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11904) · Entrez [8797](https://www.ncbi.nlm.nih.gov/gene/8797) · UniProt [O00220](https://www.uniprot.org/uniprotkb/O00220) · Ensembl [ENSG00000104689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104689)

## Data

Gene col 2483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2483); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2483]; `tensor/DDL_lfc|DDL_z.npy` [2483]; `embed/gene_vectors.npy` [2483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2483 or target_col == 2483). Every well: [[TNFRSF10A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF10A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
