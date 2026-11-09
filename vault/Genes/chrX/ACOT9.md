---
symbol: "ACOT9"
type: "gene"
col: 4404
ensembl_id: "ENSG00000123130"
name: "acyl-CoA thioesterase 9"
location: "Xp22.11"
module: 79
arm: "+"
pooled_cpm: 62.94
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ACOT9

*acyl-CoA thioesterase 9* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.71× (z +13.0, q 4e-36, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.563× (z -19.7, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPN21]] (+0.75, fdr 7e-06), [[RASAL2]] (+0.67, fdr 1e-05), [[SLC25A24]] (+0.59, fdr 2e-05); moves opposite to [[PDK3]] (-0.60, fdr 1e-05), [[FAM13A]] (-0.57, fdr 1e-05), [[SRP54-AS1]] (-0.56, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TXNRD3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4404.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +13.0 | 4e-36 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +11.3 | 6e-27 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.45×** | +9.0 | 6e-17 | 35/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +8.1 | 6e-14 | 28/49 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +7.3 | 2e-11 | 23/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.35×** | +7.3 | 3e-11 | 28/47 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +6.8 | 9e-10 | 30/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +6.4 | 9e-09 | 27/47 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +6.3 | 1e-08 | 29/47 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +6.1 | 5e-08 | 26/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +5.7 | 6e-07 | 22/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +5.7 | 7e-07 | 21/47 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +5.6 | 1e-06 | 23/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +5.5 | 1e-06 | 26/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +5.5 | 2e-06 | 22/48 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +5.2 | 8e-06 | 22/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **1.42×** | +4.5 | 2e-04 | 17/45 (HT-29, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.002 | 16/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -19.7 | 0e+00 | 39/47 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.760×** | -6.7 | 7e-09 | 27/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.794×** | -5.6 | 3e-06 | 24/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -5.6 | 3e-06 | 4/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.796×** | -5.3 | 9e-06 | 21/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.657×** | -5.3 | 9e-06 | 21/47 (SNU-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.805×** | -5.3 | 1e-05 | 22/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.810×** | -5.1 | 2e-05 | 17/48 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -5.0 | 3e-05 | 23/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.815×** | -5.0 | 4e-05 | 20/48 (KATO III, SW 1088, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.822×** | -4.8 | 9e-05 | 20/48 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | 0.889× | -3.4 | 0.027 | 11/49 (SK-MEL-2, SW 1088, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.869× | -3.4 | 0.027 | 20/47 (RPMI-7951, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.871× | -3.4 | 0.029 | 19/48 (A-172, SNU-1, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.871× | -3.4 | 0.029 | 11/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.768×** | -3.4 | 0.029 | 9/48 (SW480, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.878× | -3.2 | 0.051 | 3/48 (KATO III, J82, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.882× | -3.1 | 0.071 | 14/48 (HOP62, CFPAC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 140 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -23.2) |
| [[A-172 (line)]] | wt | 125 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -18.8) |
| [[A549 (line)]] | wt | 113 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 83.4 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -16.9) |
| [[J82 (line)]] | alt | 86.3 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -13.5) |
| [[RKO (line)]] | wt | 66.0 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.4) |
| [[SW480 (line)]] | alt | 97.4 | 2 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 54.5 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 132 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 66.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 93.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -11.0) |
| [[HOP62 (line)]] | alt | 45.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -11.9) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -8.8) |
| [[HS-578T (line)]] | alt | 48.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -13.3) |
| [[LoVo (line)]] | wt | 40.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.7) |
| [[PANC-1 (line)]] | alt | 35.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.6) | — |
| [[SNU-1 (line)]] | wt | 98.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.490× (z -8.8) |
| [[A-427 (line)]] | wt | 68.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.0) | — |
| [[A498 (line)]] | wt | 77.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 53.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.3) |
| [[HCT15 (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 28.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 65.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.0) |
| [[SW 1088 (line)]] | alt | 80.0 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.05 µM 0.0809× (z -8.7) |
| [[SW1417 (line)]] | alt | 66.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.4) |
| [[SW48 (line)]] | wt | 23.6 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.175× (z -9.6) |
| [[AN3 CA (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 93.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN21]] | +0.75 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[RASAL2]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SLC25A24]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ETS1]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RAPH1]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PSORS1C1]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[PIEZO1]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PVR]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[EGFR]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[GGACT]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PARVA]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TMEM185B]] | +0.53 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK3]] | -0.60 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[FAM13A]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[C20orf96]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[COG7]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[SPICE1]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[PIK3C2A]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[BRWD3]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TSHZ1]] | -0.55 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[BMT2]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[KDM3A]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[WDR45B]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXNRD3]] | C | TXNRD3 activity raises ACOT9's level | lines that do not express TXNRD3 (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without TXNRD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FSCN1, ELK3, XG; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction -0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.6, 12.0); signed map (12.1, 39.6). **Vector** length 115, 30.6% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.4 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.3 | +1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.5 | +3.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.3 | +6.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -19.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -0.8 |
|  | [[NG25 (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.6 | -5.1 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA thioesterase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:23,701,055-23,766,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-16, MT-ACT48, ACATE2 |
| Gene groups (HGNC) | Acyl-CoA thioesterases; Thioester hydrolases |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y305](https://www.uniprot.org/uniprotkb/Q9Y305) (Acyl-coenzyme A thioesterase 9, mitochondrial):

> Mitochondrial acyl-CoA thioesterase. Catalyzes the hydrolysis of acyl-CoAs into free fatty acids and coenzyme A (CoA), regulating their respective intracellular levels. Regulates both mitochondrial lipid and amino acid metabolism.

**Summary**, from NCBI Gene [23597](https://www.ncbi.nlm.nih.gov/gene/23597):

> The protein encoded by this gene is a mitochondrial acyl-CoA thioesterase of unknown function. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:17152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17152) · Entrez [23597](https://www.ncbi.nlm.nih.gov/gene/23597) · UniProt [Q9Y305](https://www.uniprot.org/uniprotkb/Q9Y305) · Ensembl [ENSG00000123130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123130)

## Data

Gene col 4404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4404); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4404]; `tensor/DDL_lfc|DDL_z.npy` [4404]; `embed/gene_vectors.npy` [4404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4404 or target_col == 4404). Every well: [[ACOT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
