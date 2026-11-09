---
symbol: "RELCH"
type: "gene"
col: 5561
ensembl_id: "ENSG00000134444"
name: "RAB11 binding and LisH domain, coiled-coil and HEAT repeat containing"
location: "18q21.33"
module: 169
arm: "+"
pooled_cpm: 83.56
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# RELCH

*RAB11 binding and LisH domain, coiled-coil and HEAT repeat containing* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.47× (z +17.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.426× (z -16.8, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.805× (z -4.3, q 0.003, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB7]] (+0.74, fdr 7e-06), [[TENT2]] (+0.71, fdr 7e-06), [[VDAC3]] (+0.71, fdr 7e-06); moves opposite to [[FKRP]] (-0.69, fdr 7e-06), [[ZNF121]] (-0.66, fdr 7e-06), [[THOC6]] (-0.65, fdr 1e-05).
> It is in [[Module 169]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +17.9 | 0e+00 | 48/48 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +15.8 | 0e+00 | 48/48 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.10×** | +14.6 | 0e+00 | 47/48 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.41×** | +12.7 | 1e-34 | 47/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +10.6 | 3e-24 | 32/49 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +10.3 | 6e-23 | 43/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +9.8 | 7e-21 | 44/48 (NCI-H23, SW48, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +9.5 | 2e-19 | 38/50 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +9.4 | 4e-19 | 39/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +8.4 | 3e-15 | 39/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +7.3 | 1e-11 | 37/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +7.2 | 4e-11 | 39/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.9 | 2e-10 | 36/48 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.8 | 4e-10 | 37/48 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +5.6 | 9e-07 | 39/49 (LoVo, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +5.3 | 4e-06 | 23/48 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5561.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.426×** | -16.8 | 0e+00 | 47/49 (SHP-77, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.427×** | -16.2 | 0e+00 | 41/44 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.557×** | -10.7 | 3e-24 | 35/45 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -4.3 | 0.003 | 26/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.815×** | -4.0 | 0.006 | 22/48 (A549, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -4.0 | 0.007 | 0/50 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.823×** | -3.9 | 0.009 | 24/49 (HEC-1-A, SHP-77, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.827×** | -3.8 | 0.012 | 20/47 (BT-474, NCI-H23, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.822×** | -3.7 | 0.012 | 20/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.830×** | -3.7 | 0.014 | 17/48 (LS 180, HOP62, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.3 | 0.046 | 18/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.794×** | -3.2 | 0.056 | 18/48 (NCI-H460, NCI-H1573, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.084 | 8/48 (SW48, HOP62, …) | all doses, flat |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -3.1 | 0.086 | 19/45 (Panc 03.27, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 105 | 10 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +14.6) | — |
| [[C-33 A (line)]] | alt | 87.8 | 9 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.22× (z +13.4) | — |
| [[HEC-1-A (line)]] | alt | 122 | 5 (1 ⚠) | 4 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -17.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 53.5 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 63.7 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.28× (z +12.0) | — |
| [[A-427 (line)]] | wt | 55.7 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -19.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 110 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.13× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -10.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 211 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -19.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 128 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -19.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 97.4 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 53.8 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.64× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 96.7 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -16.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 59.6 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.15× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 96.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 112 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.91× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -17.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 86.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -21.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 54.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 51.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.86× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 108 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.51× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -23.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 98.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 70.3 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.10× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 62.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.494× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 117 | 3 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 81.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -12.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -14.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 32.2 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.84× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 130 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 83.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -17.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 74.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -15.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 105 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -18.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 35.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -14.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 128 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.27× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 70.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -20.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -16.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 70.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 78.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 89.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -15.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -15.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 57.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 67.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 92.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[TENT2]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PPP2R5E]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 | same gene group; STRING 473 |
| [[PEX3]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[KIAA2013]] | +0.67 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[BMT2]] | +0.67 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R12B]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[DCAF5]] | +0.66 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TTC9C]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SPATA7]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKRP]] | -0.69 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[ZNF121]] | -0.66 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[THOC6]] | -0.65 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.63 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[SKIL]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[SRSF6]] | -0.61 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.60 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.60 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[COA7]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ZYX]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[REXO1]] | -0.59 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[MGA]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.1, -13.0); signed map (-34.5, -6.7). **Vector** length 109, 36.2% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +9.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +9.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.2 | +4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +12.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +7.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.7 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.4 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.6 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | RAB11 binding and LisH domain, coiled-coil and HEAT repeat containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:62,187,255-62,310,249 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT885, HsT3308, FLJ33841; previously KIAA1468 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P260](https://www.uniprot.org/uniprotkb/Q9P260) (RAB11-binding protein RELCH):

> Regulates intracellular cholesterol distribution from recycling endosomes to the trans-Golgi network through interactions with RAB11 and OSBP. Functions in membrane tethering and promotes OSBP-mediated cholesterol transfer between RAB11-bound recycling endosomes and OSBP-bound Golgi-like membranes.

**Summary**, from NCBI Gene [57614](https://www.ncbi.nlm.nih.gov/gene/57614):

> Involved in intracellular cholesterol transport. Located in recycling endosome and trans-Golgi network. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29289) · Entrez [57614](https://www.ncbi.nlm.nih.gov/gene/57614) · UniProt [Q9P260](https://www.uniprot.org/uniprotkb/Q9P260) · Ensembl [ENSG00000134444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134444)

## Data

Gene col 5561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5561); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5561]; `tensor/DDL_lfc|DDL_z.npy` [5561]; `embed/gene_vectors.npy` [5561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5561 or target_col == 5561). Every well: [[RELCH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RELCH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
