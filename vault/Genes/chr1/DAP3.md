---
symbol: "DAP3"
type: "gene"
col: 5358
ensembl_id: "ENSG00000132676"
name: "death associated protein 3"
location: "1q22"
module: 36
arm: "+"
pooled_cpm: 118.17
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# DAP3

*death associated protein 3* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 3.33× (z +22.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.838× (z -4.7, q 0.001, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 0.680× (z -3.6, q 0.031, down in 24 of 50 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (MIA PaCa-2 0.765×, NCI-H23 0.764×, NCI-H2030 0.798×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.517×; ⚠ cell-cycle shift, explains ~0% of this change); [[Voriconazole (drug)]] 0.05 µM in 1 line (SW 1088 0.0807×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TANGO2]] (+0.65, fdr 1e-05), [[HERC2P2]] (+0.65, fdr 1e-05), [[PWWP3A]] (+0.65, fdr 1e-05); moves opposite to [[RBM7]] (-0.63, fdr 1e-05), [[DYRK1A]] (-0.62, fdr 1e-05), [[FBXL3]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.33×** | +22.7 | 0e+00 | 48/48 (HOP62, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.17×** | +21.8 | 0e+00 | 48/48 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.90×** | +19.0 | 0e+00 | 48/48 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.92×** | +12.4 | 5e-33 | 44/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.83×** | +11.4 | 3e-28 | 45/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.80×** | +11.1 | 8e-27 | 42/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +10.4 | 3e-23 | 45/48 (C32, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.80×** | +9.8 | 1e-20 | 43/49 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.64×** | +8.9 | 2e-17 | 36/44 (Hs 766T, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +7.5 | 4e-12 | 40/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.83×** | +7.4 | 9e-12 | 41/49 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +7.4 | 9e-12 | 38/48 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +5.8 | 3e-07 | 30/45 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.38×** | +5.6 | 9e-07 | 27/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +5.5 | 1e-06 | 28/48 (MIA PaCa-2, NCI-H1573, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.003 | 24/48 (SW 900, A-172, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.039 | 18/49 (A-172, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.065 | 13/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.069 | 15/48 (Hs 766T, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +2.9 | 0.072 | 7/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +2.8 | 0.090 | 14/48 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.16× | +2.8 | 0.090 | 15/48 (CFPAC-1, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5358.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (MIA PaCa-2 0.765×, NCI-H23 0.764×, NCI-H2030 0.798×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.517×; ⚠ cell-cycle shift, explains ~0% of this change); [[Voriconazole (drug)]] 0.05 µM in 1 line (SW 1088 0.0807×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.838× | -4.7 | 0.001 | 24/48 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.799×** | -4.2 | 0.007 | 28/50 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -4.0 | 0.012 | 3/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.820×** | -3.7 | 0.026 | 26/48 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.680×** | -3.6 | 0.031 | 24/50 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.872× | -3.6 | 0.031 | 13/48 (SW480, A-427, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.834× | -3.4 | 0.049 | 21/48 (SW48, RKO, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.881× | -3.4 | 0.049 | 2/48 (PANC-1, NCI-H1792) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.049 | 22/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.864× | -3.3 | 0.059 | 15/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.862× | -3.2 | 0.060 | 16/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.843× | -3.2 | 0.064 | 19/49 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.848× | -3.1 | 0.081 | 14/48 (KATO III, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 0.848× | -3.1 | 0.081 | 19/48 (H4, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 61.5 | 12 (8 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.02× (z +13.3) | — |
| [[Hs 766T (line)]] | wt | 82.3 | 10 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.45× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 75.9 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.60× (z +13.7) | — |
| [[COLO 205 (line)]] | alt | 78.4 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.8× (z +18.8) | — |
| [[Panc 03.27 (line)]] | alt | 85.7 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 68.4 | 8 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.07× (z +13.8) | — |
| [[A-172 (line)]] | wt | 194 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.40× (z +17.4) | — |
| [[HOP62 (line)]] | alt | 103 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.60× (z +19.1) | — |
| [[KATO III (line)]] | alt | 87.9 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.01× (z +15.3) | — |
| [[LoVo (line)]] | wt | 87.9 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.33× (z +14.7) | — |
| [[RPMI-7951 (line)]] | alt | 78.3 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.35× (z +11.8) | — |
| [[SW480 (line)]] | alt | 103 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.01× (z +16.2) | — |
| [[LS 180 (line)]] | wt | 108 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.74× (z +15.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 137 | 5 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.46× (z +14.6) | [[Selinexor (drug)]] 5 µM 0.602× (z -8.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H2347 (line)]] | alt | 117 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.14× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 89.9 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.51× (z +16.0) | — |
| [[HT-29 (line)]] | alt | 88.2 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.87× (z +15.3) | — |
| [[SW 900 (line)]] | alt | 151 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.70× (z +15.4) | — |
| [[A-427 (line)]] | wt | 184 | 2 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.30× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.98× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.513× (z -9.0) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A498 (line)]] | wt | 124 | 4 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.87× (z +14.0) | — |
| [[C32 (line)]] | wt | 78.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.47× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 94.4 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.74× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 93.7 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.05× (z +16.8) | — |
| [[SHP-77 (line)]] | alt | 193 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 90.6 | 4 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.95× (z +12.3) | — |
| [[A549 (line)]] | wt | 114 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.16× (z +12.9) | — |
| [[H4 (line)]] | wt | 87.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.05× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 75.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.10× (z +15.2) | — |
| [[LOX-IMVI (line)]] | wt | 87.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.55× (z +13.5) | — |
| [[NCI-H1573 (line)]] | alt | 114 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.34× (z +18.8) | — |
| [[NCI-H23 (line)]] | alt | 285 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 168 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.43× (z +17.9) | — |
| [[PANC-1 (line)]] | alt | 176 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.51× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 121 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.25× (z +13.7) | — |
| [[SNU-1 (line)]] | wt | 91.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.33× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 108 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 85.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.37× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 175 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.74× (z +11.9) | — |
| [[SW48 (line)]] | wt | 115 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.92× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 77.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.75× (z +9.8) | — |
| [[RKO (line)]] | wt | 152 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.16× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 89.9 | 0 | 1 | — | [[Voriconazole (drug)]] 0.05 µM 0.0807× (z -9.3) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANGO2]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[HERC2P2]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PWWP3A]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[HERC2P9]] | +0.64 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.64 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ZNF496]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[EIF3K]] | +0.63 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PSMB3]] | +0.63 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[RNF216]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ZNF544]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[METTL2B]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[EPS15L1]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM7]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[DYRK1A]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[FBXL3]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[CHASERR]] | -0.61 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.61 | -0.50 / -0.55 | both halves | 1e-05 | STRING 639 |
| [[FMR1]] | -0.61 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[CFAP20]] | -0.60 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[PLEKHF2]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ZBED5-AS1]] | -0.58 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[BDH2]] | -0.58 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ZBED8]] | -0.58 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[REL]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-5.4, -31.2); signed map (-16.0, -53.0). **Vector** length 117, 41.2% of its response variance represented; |z| ≥ 3 in 1,246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +12.0 | +19.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.4 | +21.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.5 | +22.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.4 | +7.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.8 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +10.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +1.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -10.2 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.6 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | +0.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -6.5 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | -5.8 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | death associated protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,687,960-155,739,010 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRPS29, DAP-3, MRP-S29, bMRP-10, MGC126058, MGC126059, DKFZp686G12159, mS29 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins |
| Hallmark sets | APOPTOSIS |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P51398](https://www.uniprot.org/uniprotkb/P51398) (Small ribosomal subunit protein mS29):

> As a component of the mitochondrial small ribosomal subunit, it plays a role in the translation of mitochondrial mRNAs. Involved in mediating interferon-gamma-induced cell death. Displays GTPase activity in vitro.

**Summary**, from NCBI Gene [7818](https://www.ncbi.nlm.nih.gov/gene/7818):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:2673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2673) · Entrez [7818](https://www.ncbi.nlm.nih.gov/gene/7818) · UniProt [P51398](https://www.uniprot.org/uniprotkb/P51398) · Ensembl [ENSG00000132676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132676)

## Data

Gene col 5358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5358); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5358]; `tensor/DDL_lfc|DDL_z.npy` [5358]; `embed/gene_vectors.npy` [5358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5358 or target_col == 5358). Every well: [[DAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
