---
symbol: "CLPTM1L"
type: "gene"
col: 554
ensembl_id: "ENSG00000049656"
name: "CLPTM1 like"
location: "5p15.33"
module: 138
arm: "+"
pooled_cpm: 43.17
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# CLPTM1L

*CLPTM1 like* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.71× (z +13.7, q 1e-39, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +7.2, q 3e-11, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.712× (z -4.7, q 0.001, down in 29 of 48 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTBP1]] (+0.67, fdr 7e-06), [[CCNL2]] (+0.61, fdr 1e-05), [[WIZ]] (+0.57, fdr 1e-05); moves opposite to [[CMAS]] (-0.54, fdr 5e-05), [[LDAF1]] (-0.53, fdr 2e-05), [[CAMLG]] (-0.51, fdr 3e-05).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 20 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.71×** | +13.7 | 1e-39 | 44/45 (A498, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.99×** | +13.3 | 7e-38 | 42/48 (PANC-1, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.72×** | +13.2 | 2e-37 | 35/38 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.21×** | +9.6 | 8e-20 | 37/41 (CFPAC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.98×** | +9.3 | 1e-18 | 40/48 (SW480, NCI-H1792, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.89×** | +8.4 | 6e-15 | 32/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.77×** | +7.8 | 4e-13 | 38/48 (SW480, NCI-H1792, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.71×** | +7.3 | 1e-11 | 39/47 (SW480, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.2 | 3e-11 | 33/47 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.53×** | +5.8 | 3e-07 | 32/46 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.6 | 1e-06 | 33/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.52×** | +5.5 | 2e-06 | 30/47 (SHP-77, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.3 | 6e-06 | 31/48 (SW480, LOX-IMVI, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.2 | 7e-06 | 25/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.41×** | +4.7 | 1e-04 | 28/48 (SW480, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +4.6 | 2e-04 | 32/47 (COLO 205, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.003 | 23/48 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.016 | 18/47 (Panc 03.27, Hs 766T, …) | two highest doses | position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.021 | 19/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.029 | 16/47 (HOP62, HS-578T, …) | two highest doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.031 | 17/45 (A-427, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.033 | 12/47 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.035 | 16/48 (A-172, BT-474, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.042 | 14/48 (RKO, SW480, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +3.0 | 0.045 | 16/48 (MIA PaCa-2, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.045 | 19/48 (NCI-H1792, PANC-1, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.045 | 12/48 (SW480, LoVo, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.712×** | -4.7 | 0.001 | 29/48 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.753×** | -3.8 | 0.045 | 21/47 (J82, A-427, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.781× | -3.4 | 0.11 | 20/47 (NCI-H2030, SNU-423, …) | rises with dose | low cells (technical?); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.792× | -3.2 | 0.17 | 16/48 (HCT15, KATO III, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.798× | -3.0 | 0.29 | 17/48 (LOX-IMVI, NCI-H2030, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 51.0 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +28.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.55× (z +14.0) | — |
| [[A549 (line)]] | wt | 29.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +17.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 51.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 4.27× (z +10.1) | — |
| [[SW480 (line)]] | alt | 49.4 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 58.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 24.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 39.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 28.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 29.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 38.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +18.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 67.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +13.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SNU-423 (line)]] | alt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.00× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 39.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[BT-474 (line)]] | alt | 44.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.23× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[COLO 205 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.53× (z +9.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1792 (line)]] | alt | 27.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +13.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2347 (line)]] | alt | 49.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.8) | — |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW1417 (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTBP1]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CCNL2]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[WIZ]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SRF]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[CHTOP]] | +0.54 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PLXNB1]] | +0.53 | +0.32 / +0.52 | both halves | 2e-04 |  |
| [[ATP13A1]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TAF1C]] | +0.52 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[TAOK2]] | +0.52 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[USP19]] | +0.52 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[RMRP]] | +0.51 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[OPLAH]] ⚠ | +0.51 | +0.51 / +0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GET4]] | +0.51 | +0.40 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMAS]] | -0.54 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[LDAF1]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CAMLG]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[MORC3]] | -0.50 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[RPL39]] | -0.49 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[ATP6V0D2]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ISCA1]] | -0.47 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[ACTR6]] | -0.47 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[KLHL7]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[CCDC82]] | -0.45 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[ABHD3]] | -0.45 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ECI2]] | -0.45 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, -25.1); signed map (4.2, -5.6). **Vector** length 67.9, 13.6% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +6.3 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.0 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.1 | +13.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +1.0 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | CLPTM1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:1,317,752-1,345,099 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14400, CRR9 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KA5](https://www.uniprot.org/uniprotkb/Q96KA5) (Lipid scramblase CLPTM1L):

> Scramblase that mediates the translocation of glucosaminylphosphatidylinositol (alpha-D-GlcN-(1-6)-(1,2-diacyl-sn-glycero-3-phospho)-1D-myo-inositol, GlcN-PI) across the endoplasmic reticulum (ER) membrane, from the cytosolic leaflet to the luminal leaflet of the ER membrane, where it participates in the biosynthesis of glycosylphosphatidylinositol (GPI). GPI is a lipid glycoconjugate involved in post-translational modification of proteins. Can also translocate …

**Summary**, from NCBI Gene [81037](https://www.ncbi.nlm.nih.gov/gene/81037):

> The protein encoded by this gene is a membrane protein whose overexpression in cisplatin-sensitive cells causes apoptosis. Polymorphisms in this gene have been reported to increase susceptibility to several cancers, including lung, pancreatic, and breast cancers. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:24308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24308) · Entrez [81037](https://www.ncbi.nlm.nih.gov/gene/81037) · UniProt [Q96KA5](https://www.uniprot.org/uniprotkb/Q96KA5) · Ensembl [ENSG00000049656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049656)

## Data

Gene col 554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 554); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 554]; `tensor/DDL_lfc|DDL_z.npy` [554]; `embed/gene_vectors.npy` [554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 554 or target_col == 554). Every well: [[CLPTM1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLPTM1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
