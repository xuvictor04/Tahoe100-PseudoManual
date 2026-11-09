---
symbol: "MIGA1"
type: "gene"
col: 11111
ensembl_id: "ENSG00000180488"
name: "mitoguardin 1"
location: "1p31.1"
module: 57
arm: "+"
pooled_cpm: 66.61
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# MIGA1

*mitoguardin 1* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 1.14× (z +4.9, q 5e-04, up in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~93% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 1.30× (z +3.5, q 0.082, up in 11 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.435× (z -21.3, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LONP2]] (+0.73, fdr 7e-06), [[EXD2]] (+0.69, fdr 7e-06), [[PARL]] (+0.67, fdr 7e-06); moves opposite to [[PKNOX1]] (-0.56, fdr 1e-05), [[PMEPA1]] (-0.55, fdr 1e-05), [[ERF]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | 1.14× | +4.9 | 5e-04 | 22/48 (LS 180, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +3.9 | 0.027 | 15/48 (LS 180, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.082 | 11/49 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.28× | +3.3 | 0.15 | 7/50 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | 1.27× | +3.2 | 0.15 | 10/47 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.13× | +3.0 | 0.24 | 8/50 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.435×** | -21.3 | 0e+00 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -20.6 | 0e+00 | 45/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.567×** | -20.5 | 0e+00 | 41/48 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.562×** | -14.7 | 0e+00 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.581×** | -13.8 | 2e-41 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.583×** | -13.2 | 5e-38 | 37/48 (J82, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -11.0 | 4e-26 | 41/48 (SW480, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.683×** | -9.7 | 2e-20 | 30/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.690×** | -9.1 | 5e-18 | 32/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.690×** | -8.3 | 4e-15 | 28/45 (H4, HCT15, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -7.7 | 5e-13 | 29/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.817×** | -7.3 | 2e-11 | 24/48 (A498, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.825×** | -6.9 | 2e-10 | 26/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.801×** | -5.6 | 7e-07 | 27/48 (Hs 766T, HCT15, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.829×** | -4.8 | 8e-05 | 22/48 (HCT15, H4, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.853× | -4.0 | 0.002 | 18/48 (CFPAC-1, HT-29, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.813×** | -3.7 | 0.005 | 19/48 (C32, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.863× | -3.7 | 0.005 | 16/48 (H4, SW48, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.823×** | -3.5 | 0.010 | 17/48 (PANC-1, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.879× | -3.3 | 0.024 | 12/47 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.880× | -3.2 | 0.025 | 12/48 (HEC-1-A, RPMI-7951, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.053 | 14/48 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.923× | -2.8 | 0.086 | 2/48 (Hs 766T, NCI-H1792) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 56.4 | 0 | 12 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.292× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 88.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -22.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -16.7) |
| [[PANC-1 (line)]] | alt | 70.9 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.380× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -15.9) |
| [[SNU-423 (line)]] | alt | 63.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -20.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -10.3) |
| [[Hs 766T (line)]] | wt | 90.9 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -15.1) |
| [[HS-578T (line)]] | alt | 104 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.455× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 60.8 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -11.7) |
| [[SW480 (line)]] | alt | 63.7 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -21.4) |
| [[AsPC-1 (line)]] | alt | 51.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -20.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -15.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.484× (z -9.5) |
| [[H4 (line)]] | wt | 68.4 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -10.1) |
| [[HOP62 (line)]] | alt | 59.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.353× (z -11.9) |
| [[LoVo (line)]] | wt | 54.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.358× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -12.3) |
| [[LS 180 (line)]] | wt | 56.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 86.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -11.3) |
| [[SW 900 (line)]] | alt | 76.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -17.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.331× (z -11.6) |
| [[A498 (line)]] | wt | 76.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -15.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.501× (z -9.7) |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.246× (z -11.6) |
| [[C32 (line)]] | wt | 70.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -18.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -10.5) |
| [[HCT15 (line)]] | alt | 121 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.396× (z -8.8) |
| [[J82 (line)]] | alt | 61.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -16.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.433× (z -10.3) |
| [[A-172 (line)]] | wt | 26.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 65.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.391× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 79.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -22.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.491× (z -8.9) |
| [[AN3 CA (line)]] | alt | 75.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 44.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -10.4) |
| [[HT-29 (line)]] | alt | 45.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 73.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -8.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H23 (line)]] | alt | 89.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 80.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 1271 (line)]] | alt | 67.7 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0520× (z -11.5) |
| [[A-427 (line)]] | wt | 63.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.478× (z -8.5) |
| [[C-33 A (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -14.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 72.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.495× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 83.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 61.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.405× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 83.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 76.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 128 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0625× (z -11.2) |
| [[A549 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LONP2]] | +0.73 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[EXD2]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[PARL]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.66 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[SAMM50]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[RNF20]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[VPS35]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ZNF133]] | +0.63 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[IARS2]] | +0.63 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[EIF2A]] | +0.63 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[ACP1]] | +0.62 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[CDC40]] | +0.61 | +0.72 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKNOX1]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[PMEPA1]] | -0.55 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ERF]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[SKIL]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[MIDN]] | -0.53 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[KDM6B]] | -0.52 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ARHGAP26]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.0, -11.2); signed map (-31.3, -15.1). **Vector** length 90.2, 22.4% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +6.5 | +4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +3.9 |
|  | [[NG25 (drug)]] 5 µM |  | +4.1 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | -4.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -20.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -11.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.3 | -13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.6 | -20.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | mitoguardin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:77,779,624-77,879,540 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35093; previously FAM73A |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NAN2](https://www.uniprot.org/uniprotkb/Q8NAN2) (Mitoguardin 1):

> Regulator of mitochondrial fusion: acts by forming homo- and heterodimers at the mitochondrial outer membrane and facilitating the formation of PLD6/MitoPLD dimers. May act by regulating phospholipid metabolism via PLD6/MitoPLD.

**Summary**, from NCBI Gene [374986](https://www.ncbi.nlm.nih.gov/gene/374986):

> Enables protein heterodimerization activity and protein homodimerization activity. Involved in mitochondrial fusion. Located in mitochondrion and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24741) · Entrez [374986](https://www.ncbi.nlm.nih.gov/gene/374986) · UniProt [Q8NAN2](https://www.uniprot.org/uniprotkb/Q8NAN2) · Ensembl [ENSG00000180488](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180488)

## Data

Gene col 11111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11111); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11111]; `tensor/DDL_lfc|DDL_z.npy` [11111]; `embed/gene_vectors.npy` [11111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11111 or target_col == 11111). Every well: [[MIGA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIGA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
