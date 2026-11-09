---
symbol: "RBM27"
type: "gene"
col: 1648
ensembl_id: "ENSG00000091009"
name: "RNA binding motif protein 27"
location: "5q32"
module: 169
arm: "+"
pooled_cpm: 169.43
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# RBM27

*RNA binding motif protein 27* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.77× (z +11.3, q 1e-26, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.739× (z -5.8, q 5e-06, down in 27 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.813× (z -4.1, q 0.011, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.171×, AN3 CA 0.189×, A-427 0.396×, NCI-H460 0.406×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (BT-474 0.607×, LoVo 0.670×, A-172 0.657×, RKO 0.598×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (SW 1088 0.0646×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H15]] (+0.71, fdr 7e-06), [[RWDD1]] (+0.65, fdr 7e-06), [[NOL7]] (+0.63, fdr 1e-05, ⚠ NOL7 in the vector space only through flagged drug-doses), [[FAM133B]] (+0.63, fdr 1e-05); moves opposite to [[EIF4EBP2]] (-0.63, fdr 2e-05), [[NEMP1]] (-0.60, fdr 1e-05), [[RSC1A1]] (-0.57, fdr 4e-05).
> It is in [[Module 169]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1648.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +11.3 | 1e-26 | 44/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +11.0 | 1e-25 | 46/49 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +10.3 | 2e-22 | 43/48 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.44×** | +10.1 | 5e-22 | 34/48 (A549, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +9.2 | 4e-18 | 44/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.57×** | +8.9 | 6e-17 | 45/48 (LoVo, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.7 | 4e-16 | 42/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +8.1 | 6e-14 | 42/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +7.0 | 1e-10 | 40/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.42×** | +6.7 | 1e-09 | 34/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.38×** | +6.4 | 1e-08 | 34/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.35×** | +5.9 | 2e-07 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +5.9 | 2e-07 | 41/45 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.33×** | +5.4 | 3e-06 | 30/48 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 3e-06 | 42/49 (PANC-1, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.006 | 31/48 (PANC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.015 | 11/49 (CFPAC-1, A549, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.016 | 20/48 (KATO III, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.024 | 17/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.039 | 4/49 (HT-29, SW 900, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.044 | 23/48 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.044 | 15/47 (NCI-H23, CFPAC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.058 | 16/48 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1648.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.171×, AN3 CA 0.189×, A-427 0.396×, NCI-H460 0.406×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (BT-474 0.607×, LoVo 0.670×, A-172 0.657×, RKO 0.598×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (SW 1088 0.0646×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.739×** | -5.8 | 5e-06 | 27/44 (SHP-77, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.813×** | -4.1 | 0.011 | 25/48 (J82, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.845× | -3.3 | 0.18 | 22/49 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.18 | 17/47 (SK-MEL-2, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.897× | -3.1 | 0.25 | 7/48 (NCI-H661, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1648. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 182 | 10 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +15.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.93× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 147 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.45× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 128 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.80× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 168 | 5 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +12.3) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.406× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 144 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 135 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 178 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.06× (z +12.1) | — |
| [[A-427 (line)]] | wt | 246 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.77× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -14.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 181 | 4 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.59× (z +14.8) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.73× (z +8.8) | — |
| [[A549 (line)]] | wt | 146 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +16.4) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 154 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.3) ⚠ cell-cycle shift, explains ~60% of this change | [[Dinaciclib (drug)]] 5 µM 0.414× (z -10.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 170 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +10.4) ⚠ cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 150 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.1) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.54× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 141 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.06× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 225 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.56× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 123 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.40× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 99.2 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.46× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.99× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 149 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 197 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.96× (z +9.8) | — |
| [[RKO (line)]] | wt | 187 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 312 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.76× (z +9.3) | — |
| [[A-172 (line)]] | wt | 227 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 145 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.2) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[AN3 CA (line)]] | alt | 252 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 135 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.63× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 133 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.33× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 147 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.08× (z +8.5) | — |
| [[KATO III (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +13.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 193 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 184 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.5) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[RPMI-7951 (line)]] | alt | 115 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.59× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -22.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 192 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.8) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0646× (z -12.8) |
| [[SW 900 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.2) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[SW48 (line)]] | wt | 177 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.38× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 214 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 262 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1648), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 7 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H15]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 | same gene group |
| [[RWDD1]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[NOL7]] ⚠ | +0.63 | +0.54 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FAM133B]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[MRPL21]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MRPS26]] | +0.62 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.62 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[LEO1]] | +0.61 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[TXNL1]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MARCHF5]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[CWC15]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[DHX29]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4EBP2]] | -0.63 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[NEMP1]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RSC1A1]] | -0.57 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[ELK4]] | -0.55 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[PRKAR1A]] | -0.55 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[BAG6]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[GPAA1]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ARL5B]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[CD164]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZNF799]] | -0.51 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[NID1]] | -0.51 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[BTBD19]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.6, -10.5); signed map (-20.4, -8.4). **Vector** length 88.5, 30.1% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +11.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +8.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | -0.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +9.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -6.0 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -4.2 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:146,203,605-146,289,223 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1311, ARRS1, Psc1, ZC3H20 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; RNA binding motif containing |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2N5](https://www.uniprot.org/uniprotkb/Q9P2N5) (RNA-binding protein 27):

> May be involved in the turnover of nuclear polyadenylated (pA+) RNA.

**Summary**, from NCBI Gene [54439](https://www.ncbi.nlm.nih.gov/gene/54439):

> Enables RNA binding activity. Predicted to be involved in RNA catabolic process. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29243) · Entrez [54439](https://www.ncbi.nlm.nih.gov/gene/54439) · UniProt [Q9P2N5](https://www.uniprot.org/uniprotkb/Q9P2N5) · Ensembl [ENSG00000091009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091009)

## Data

Gene col 1648: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1648); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1648, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1648]; `tensor/DDL_lfc|DDL_z.npy` [1648]; `embed/gene_vectors.npy` [1648]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1648 or target_col == 1648). Every well: [[RBM27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
