---
symbol: "GSPT1"
type: "gene"
col: 2355
ensembl_id: "ENSG00000103342"
name: "G1 to S phase transition 1"
location: "16p13.13"
module: 4
arm: "+"
pooled_cpm: 155.8
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GSPT1

*G1 to S phase transition 1* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +18.5, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.37× (z +7.7, q 1e-12, up in 35 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.254×; ⚠ cell-cycle shift, explains ~24% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (SW 1088 0.0929×; ⚠ toxic); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.340×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM120A]] (+0.71, fdr 1e-05), [[EIF4G1]] (+0.68, fdr 7e-06), [[IPO5]] (+0.68, fdr 7e-06); moves opposite to [[NDUFB4]] (-0.64, fdr 2e-05), [[IFI27L2]] (-0.64, fdr 1e-05), [[ZFAND2A-DT]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 28 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.12×** | +18.5 | 0e+00 | 48/49 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.14×** | +18.1 | 0e+00 | 42/44 (A549, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.75×** | +12.8 | 5e-35 | 40/45 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +12.2 | 4e-32 | 45/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.40×** | +11.8 | 3e-30 | 35/48 (A549, A498, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.57×** | +11.1 | 8e-27 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.43×** | +8.9 | 6e-17 | 35/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.41×** | +8.5 | 1e-15 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +7.7 | 1e-12 | 35/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.35×** | +7.4 | 7e-12 | 39/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +6.9 | 3e-10 | 28/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +6.5 | 3e-09 | 31/48 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.31×** | +6.4 | 7e-09 | 28/48 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +5.9 | 2e-07 | 28/48 (SNU-423, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +5.8 | 2e-07 | 28/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 7e-05 | 25/48 (PANC-1, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.6 | 1e-04 | 10/49 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +4.2 | 7e-04 | 22/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +4.0 | 0.001 | 14/48 (Hs 766T, SW1417, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +4.0 | 0.001 | 22/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.002 | 26/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.008 | 19/48 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.027 | 19/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.034 | 14/47 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.14× | +3.1 | 0.034 | 11/48 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.048 | 12/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 1.13× | +2.9 | 0.053 | 6/48 (J82, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2355.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.254×; ⚠ cell-cycle shift, explains ~24% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (SW 1088 0.0929×; ⚠ toxic); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.340×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 0.895× | -3.8 | 0.070 | 6/48 (SW 1088, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.876× | -3.4 | 0.090 | 13/50 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.869× | -3.4 | 0.090 | 17/47 (LoVo, C-33 A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.907× | -3.3 | 0.090 | 5/49 (NCI-H23, Panc 03.27, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.871× | -3.3 | 0.090 | 15/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.911× | -3.3 | 0.090 | 11/48 (RKO, J82, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.14 | 20/48 (SNU-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Minodronic acid (drug)]] 0.05 µM |  | 0.878× | -3.0 | 0.14 | 6/48 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.885× | -3.0 | 0.14 | 10/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.844× | -3.0 | 0.14 | 14/48 (A498, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 122 | 12 (12 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.99× (z +14.8) ⚠ toxic | — |
| [[SW480 (line)]] | alt | 211 | 10 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 101 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +16.1) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 2.59× (z +10.1) | — |
| [[A549 (line)]] | wt | 154 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +17.6) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[LoVo (line)]] | wt | 164 | 7 (7 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.35× (z +12.7) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 176 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.86× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 103 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 154 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.3) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[CFPAC-1 (line)]] | alt | 101 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Hs 766T (line)]] | wt | 146 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 162 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 162 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.16× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 120 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[A498 (line)]] | wt | 206 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +17.1) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[H4 (line)]] | wt | 117 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +11.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2347 (line)]] | alt | 104 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 103 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 138 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.49× (z +10.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HS-578T (line)]] | alt | 112 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[J82 (line)]] | alt | 191 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 171 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.02× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 123 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SW1417 (line)]] | alt | 156 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HCT15 (line)]] | alt | 213 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 159 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -16.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[BT-474 (line)]] | alt | 222 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.5) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[C32 (line)]] | wt | 132 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.4) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[CHP-212 (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.340× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 232 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.12× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 268 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 226 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RPMI-7951 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 174 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0929× (z -11.3) ⚠ toxic |
| [[SW48 (line)]] | wt | 188 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 194 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 165 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM120A]] | +0.71 | +0.57 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[EIF4G1]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); STRING 667 |
| [[IPO5]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[PAK2]] | +0.66 | +0.57 / +0.67 | both halves | 9e-06 | pathway: Signaling by ROBO receptors |
| [[IPO7]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PRKDC]] | +0.63 | +0.60 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[NOLC1]] | +0.62 | +0.57 / +0.64 | both halves | 9e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[SYNCRIP]] | +0.62 | +0.49 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[SMARCC1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[LRPPRC]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[AGPAT3]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[BTBD1]] | +0.60 | +0.57 / +0.60 | both halves | 8e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFB4]] | -0.64 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[IFI27L2]] | -0.64 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[ZFAND2A-DT]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ZNF8-DT]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[CCS]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SAT2]] | -0.56 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[RNF114]] | -0.56 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[APBA3]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[VPS37D]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[CCDC127]] | -0.56 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[BSDC1]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.2, -30.7); signed map (-7.5, -44.0). **Vector** length 95.9, 30.3% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.6 | +18.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.3 | +18.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +5.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.9 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +2.1 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.1 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.8 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -3.1 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | -3.6 | -1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.6 | -2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.4 | -1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.0 | -2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | G1 to S phase transition 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:11,868,128-11,916,082 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GST1, ETF3A, eRF3a |
| Gene groups (HGNC) | SURF complex; Translational GTPases |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 10 pathways, smallest: Eukaryotic Translation Termination; Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC); Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P15170](https://www.uniprot.org/uniprotkb/P15170) (Eukaryotic peptide chain release factor GTP-binding subunit ERF3A):

> GTPase component of the eRF1-eRF3-GTP ternary complex, a ternary complex that mediates translation termination in response to the termination codons UAA, UAG and UGA. GSPT1/ERF3A mediates ETF1/ERF1 delivery to stop codons: The eRF1-eRF3-GTP complex binds to a stop codon in the ribosomal A-site. GTP hydrolysis by GSPT1/ERF3A induces a conformational change that leads to its dissociation, permitting ETF1/ERF1 to accommodate fully in the A-site. Component of the transient SURF complex which …

**Summary**, from NCBI Gene [2935](https://www.ncbi.nlm.nih.gov/gene/2935):

> Enables GTPase activity and translation release factor activity. Involved in regulation of translational termination and translational termination. Acts upstream of or within protein methylation. Part of translation release factor complex. Is active in cytosolic ribosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4621) · Entrez [2935](https://www.ncbi.nlm.nih.gov/gene/2935) · UniProt [P15170](https://www.uniprot.org/uniprotkb/P15170) · Ensembl [ENSG00000103342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103342)

## Data

Gene col 2355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2355); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2355]; `tensor/DDL_lfc|DDL_z.npy` [2355]; `embed/gene_vectors.npy` [2355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2355 or target_col == 2355). Every well: [[GSPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
