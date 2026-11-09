---
symbol: "KMT2E"
type: "gene"
col: 84
ensembl_id: "ENSG00000005483"
name: "lysine methyltransferase 2E (inactive)"
location: "7q22.3"
module: 59
arm: "+"
pooled_cpm: 522.49
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 19
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# KMT2E

*lysine methyltransferase 2E (inactive)* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +23.5, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.380× (z -21.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP1-DT]] (+0.73, fdr 8e-06), [[ZNF292]] (+0.73, fdr 7e-06), [[DBP]] (+0.70, fdr 7e-06); moves opposite to [[ZNF731P]] (-0.68, fdr 1e-05), [[TTL]] (-0.65, fdr 7e-06), [[ABCF2]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 84.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +23.5 | 0e+00 | 45/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.23×** | +16.5 | 0e+00 | 48/49 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +11.9 | 3e-30 | 40/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +9.8 | 2e-20 | 45/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +9.6 | 8e-20 | 42/48 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.2 | 4e-18 | 40/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +8.6 | 9e-16 | 33/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.0 | 2e-10 | 30/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.29×** | +5.6 | 1e-06 | 26/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.23×** | +4.3 | 7e-04 | 26/49 (NCI-H460, SNU-423, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | **1.22×** | +4.3 | 1e-03 | 27/49 (RPMI-7951, COLO 205, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.19× | +3.8 | 0.006 | 23/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.009 | 28/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.12× | +3.6 | 0.013 | 6/48 (LoVo, KATO III, …) | top dose only | position effect removed |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.018 | 19/49 (BT-474, A549, …) | rises with dose | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.018 | 14/48 (AsPC-1, SW1417, …) | rises with dose | low cells (technical?) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.080 | 21/48 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 1.15× | +3.0 | 0.081 | 10/48 (RPMI-7951, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 84.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.380×** | -21.2 | 0e+00 | 48/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.404×** | -19.8 | 0e+00 | 48/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -16.1 | 0e+00 | 42/44 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.493×** | -15.5 | 0e+00 | 47/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.512×** | -14.7 | 0e+00 | 47/48 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.646×** | -9.2 | 3e-18 | 39/50 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -8.5 | 2e-15 | 2/50 (MIA PaCa-2, NCI-H1792) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.673×** | -8.3 | 6e-15 | 41/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.696×** | -7.9 | 1e-13 | 34/48 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.780×** | -7.7 | 9e-13 | 36/48 (AN3 CA, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.717×** | -7.3 | 2e-11 | 41/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.719×** | -6.9 | 2e-10 | 37/48 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.733×** | -6.8 | 5e-10 | 42/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.722×** | -6.6 | 2e-09 | 30/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.810×** | -6.5 | 3e-09 | 26/49 (NCI-H1792, AN3 CA, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.818×** | -4.4 | 3e-04 | 28/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.829×** | -4.1 | 0.001 | 24/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.848× | -3.6 | 0.008 | 17/49 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.731×** | -3.6 | 0.008 | 26/49 (AsPC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.862× | -3.3 | 0.028 | 19/48 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.863× | -3.2 | 0.029 | 20/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.905× | -3.1 | 0.045 | 1/48 (NCI-H661) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.869× | -3.1 | 0.045 | 13/49 (KATO III, NCI-H1573, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.873× | -3.0 | 0.060 | 12/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.830×** | -2.9 | 0.070 | 19/48 (H4, HOP62, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 84. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 545 | 13 (6 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +22.3) | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 667 | 3 | 13 (10 ⚠) | [[TAK-901 (drug)]] 5 µM 3.54× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -22.2) |
| [[KATO III (line)]] | alt | 477 | 8 (1 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +22.4) | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 732 | 2 | 12 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.375× (z -14.4) |
| [[LoVo (line)]] | wt | 416 | 10 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +30.6) | [[Panobinostat (drug)]] 5 µM 0.379× (z -17.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.396× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 774 | 2 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +21.4) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.295× (z -18.0) |
| [[Hs 766T (line)]] | wt | 705 | 2 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.0) | [[Panobinostat (drug)]] 5 µM 0.252× (z -21.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.294× (z -19.4) |
| [[HT-29 (line)]] | alt | 473 | 4 (1 ⚠) | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +19.5) | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -20.3) |
| [[LS 180 (line)]] | wt | 472 | 5 (1 ⚠) | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +17.3) | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 508 | 6 (1 ⚠) | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.70× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.223× (z -22.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.226× (z -22.5) |
| [[hTERT-HPNE (line)]] | wt | 497 | 5 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.249× (z -19.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.258× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 476 | 6 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +18.4) | [[Panobinostat (drug)]] 5 µM 0.339× (z -16.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.375× (z -14.5) |
| [[NCI-H23 (line)]] | alt | 361 | 7 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +27.0) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.444× (z -12.1) |
| [[PANC-1 (line)]] | alt | 371 | 8 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +41.5) | [[Panobinostat (drug)]] 5 µM 0.406× (z -17.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.407× (z -17.4) |
| [[SW 900 (line)]] | alt | 657 | 1 | 10 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 3.85× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -20.9) |
| [[SNU-423 (line)]] | alt | 584 | 2 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.356× (z -16.7) |
| [[SW48 (line)]] | wt | 434 | 7 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +20.1) | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -10.3) |
| [[SW480 (line)]] | alt | 532 | 5 (1 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.42× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -15.9) |
| [[A-427 (line)]] | wt | 331 | 5 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.459× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 550 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +22.7) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -26.3) |
| [[COLO 205 (line)]] | alt | 506 | 4 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.97× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.322× (z -18.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.351× (z -16.9) |
| [[HS-578T (line)]] | alt | 552 | 4 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.302× (z -17.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.347× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 892 | 1 | 8 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.07× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 507 | 4 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +26.0) | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -17.5) |
| [[SW1417 (line)]] | alt | 692 | 3 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.376× (z -14.5) |
| [[AN3 CA (line)]] | alt | 782 | 0 | 8 (6 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.483× (z -13.3) |
| [[C32 (line)]] | wt | 1,231 | 4 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.393× (z -12.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.404× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 408 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.283× (z -17.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.349× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 677 | 4 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.309× (z -13.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.314× (z -13.3) |
| [[RKO (line)]] | wt | 597 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +20.5) | [[Panobinostat (drug)]] 0.5 µM 0.508× (z -9.8) |
| [[A-172 (line)]] | wt | 370 | 3 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +25.0) | [[Panobinostat (drug)]] 5 µM 0.429× (z -12.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.452× (z -11.7) |
| [[HCT15 (line)]] | alt | 507 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.425× (z -12.4) |
| [[HOP62 (line)]] | alt | 527 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.90× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -17.7) |
| [[A498 (line)]] | wt | 460 | 4 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +34.4) | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 392 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.420× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 484 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -12.2) |
| [[A549 (line)]] | wt | 369 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +20.3) | [[Panobinostat (drug)]] 0.5 µM 0.410× (z -11.3) |
| [[BT-474 (line)]] | alt | 518 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.32× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 418 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.412× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -10.2) |
| [[J82 (line)]] | alt | 314 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.7) | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -8.6) |
| [[C-33 A (line)]] | alt | 427 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.458× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.461× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 387 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.414× (z -8.9) |
| [[SNU-1 (line)]] | wt | 542 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 483 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.286× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -8.7) |
| [[CHP-212 (line)]] | wt | 481 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -9.7) |
| [[NCI-H661 (line)]] | alt | 674 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 249 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 1088 (line)]] | alt | 738 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -9.7) |
| [[NCI-H2122 (line)]] | alt | 617 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 639 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 84), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP1-DT]] | +0.73 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ZNF292]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 | STRING 525 |
| [[DBP]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[IST1]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[TRA2A]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ABCA5]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | +0.66 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[RAB9A]] | +0.66 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CA11]] | +0.66 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[ZNF821]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZNF428]] | +0.65 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[VAMP2]] | +0.65 | +0.57 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.68 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[TTL]] | -0.65 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.64 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[PSME3]] | -0.63 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[NIPA2]] | -0.63 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[EIF2S1]] | -0.63 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[LETM1]] | -0.61 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[MACROH2A1]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[POLR3E]] | -0.61 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.61 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[E2F4]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KMT2E's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00408]] | B | LINC00408 activity raises KMT2E's level | lines that do not express LINC00408 (38) vs lines expressing it (12) | 1.23× lower at baseline in the lines without LINC00408 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000287861, ANKRD20A9P, PHF2P2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (12.9, -21.4); signed map (-8.5, 3.5). **Vector** length 114, 50.7% of its response variance represented; |z| ≥ 3 in 1,774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.7 | +23.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +7.3 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +6.6 | -6.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.0 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +4.1 | +1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.1 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.4 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -7.3 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.5 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | +1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.1 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.1 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -3.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | lysine methyltransferase 2E (inactive) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:104,940,943-105,115,019 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HDCMC04P, SETD5B; previously MLL5 |
| Gene groups (HGNC) | PHD finger proteins; SET domain containing; Putative lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZD2](https://www.uniprot.org/uniprotkb/Q8IZD2) (Histone reader KMT2E):

> Associates with chromatin regions downstream of transcriptional start sites of active genes and thus regulates gene transcription. Chromatin interaction is mediated via the binding to tri-methylated histone H3 at 'Lys-4' (H3K4me3). Key regulator of hematopoiesis involved in terminal myeloid differentiation and in the regulation of hematopoietic stem cell (HSCs) self-renewal by a mechanism that involves DNA methylation (By similarity). Also acts as an important cell cycle regulator, …

**Summary**, from NCBI Gene [55904](https://www.ncbi.nlm.nih.gov/gene/55904):

> This gene is a member of the myeloid/lymphoid or mixed-lineage leukemia (MLL) family and encodes a protein with an N-terminal PHD zinc finger and a central SET domain. Overexpression of the protein inhibits cell cycle progression. Alternate transcriptional splice variants have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18541) · Entrez [55904](https://www.ncbi.nlm.nih.gov/gene/55904) · UniProt [Q8IZD2](https://www.uniprot.org/uniprotkb/Q8IZD2) · Ensembl [ENSG00000005483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005483)

## Data

Gene col 84: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 84); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 84, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 84]; `tensor/DDL_lfc|DDL_z.npy` [84]; `embed/gene_vectors.npy` [84]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 84 or target_col == 84). Every well: [[KMT2E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMT2E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
