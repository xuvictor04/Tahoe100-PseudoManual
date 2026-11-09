---
symbol: "CEBPZ"
type: "gene"
col: 3722
ensembl_id: "ENSG00000115816"
name: "CCAAT enhancer binding protein zeta"
location: "2p22.2"
module: 11
arm: "+"
pooled_cpm: 114.06
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CEBPZ

*CCAAT enhancer binding protein zeta* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.17× (z +15.3, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.88× (z +14.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.674× (z -5.3, q 6e-05, down in 29 of 44 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.280×, A-427 0.316×, SK-MEL-2 0.331×, CHP-212 0.274×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.408×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (AN3 CA 0.256×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF6]] (+0.85, fdr 7e-06), [[ESF1]] (+0.84, fdr 7e-06), [[MRPS18B]] (+0.81, fdr 7e-06); moves opposite to [[SEC61A2]] (-0.66, fdr 7e-06), [[TWSG1]] (-0.66, fdr 7e-06), [[RPL10]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.17×** | +15.3 | 0e+00 | 46/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.88×** | +14.8 | 0e+00 | 48/48 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.58×** | +12.8 | 5e-35 | 48/48 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.05×** | +10.1 | 1e-21 | 48/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.19×** | +8.5 | 3e-15 | 43/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +6.6 | 3e-09 | 44/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.59×** | +6.4 | 9e-09 | 38/48 (LoVo, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.45×** | +5.2 | 2e-05 | 33/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +5.2 | 2e-05 | 35/48 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.1 | 2e-05 | 31/47 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.41×** | +4.8 | 1e-04 | 34/48 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.7 | 1e-04 | 35/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.19× | +3.4 | 0.028 | 19/48 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~80% of this change | **1.25×** | +3.0 | 0.097 | 24/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.24×** | +3.0 | 0.099 | 24/48 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3722.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.280×, A-427 0.316×, SK-MEL-2 0.331×, CHP-212 0.274×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.408×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (AN3 CA 0.256×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.674×** | -5.3 | 6e-05 | 29/44 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.844× | -3.4 | 0.14 | 17/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.846× | -3.3 | 0.14 | 17/48 (PANC-1, SW1417, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -3.3 | 0.14 | 19/49 (A498, CHP-212, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.796× | -3.2 | 0.16 | 24/48 (CFPAC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.785× | -3.1 | 0.16 | 25/48 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 98.1 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 123 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.40× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 127 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +16.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.01× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 87.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.92× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 76.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +17.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.50× (z +14.9) | — |
| [[NCI-H1573 (line)]] | alt | 77.9 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +17.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 134 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +14.3) | — |
| [[A-172 (line)]] | wt | 85.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.46× (z +11.9) | — |
| [[RKO (line)]] | wt | 118 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -12.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 129 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +15.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +12.6) | — |
| [[C32 (line)]] | wt | 67.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.03× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 99.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +15.8) | — |
| [[HS-578T (line)]] | alt | 72.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.10× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 66.5 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.86× (z +14.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.06× (z +13.5) | — |
| [[NCI-H2347 (line)]] | alt | 63.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.45× (z +12.6) | — |
| [[SW 900 (line)]] | alt | 94.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 108 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 95.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.3× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 96.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.37× (z +13.6) | — |
| [[hTERT-HPNE (line)]] | wt | 84.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +12.3) | — |
| [[J82 (line)]] | alt | 75.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 180 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 152 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 136 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -9.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 102 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +9.4) | — |
| [[KATO III (line)]] | alt | 148 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 109 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 184 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 90.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +10.1) | — |
| [[A-427 (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 105 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.256× (z -8.8) |
| [[BT-474 (line)]] | alt | 71.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.3) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[CHP-212 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 129 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.3) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 69.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[Panc 03.27 (line)]] | alt | 144 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 90.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +9.8) | — |
| [[SW480 (line)]] | alt | 154 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.57× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF6]] | +0.85 | +0.83 / +0.87 | both halves | 7e-06 | STRING 902 |
| [[ESF1]] | +0.84 | +0.88 / +0.80 | both halves | 7e-06 | STRING 928 |
| [[MRPS18B]] | +0.81 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[NIFK]] | +0.81 | +0.78 / +0.85 | both halves | 7e-06 | STRING 951 |
| [[ZNF146]] | +0.81 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[CWC22]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 | STRING 462 |
| [[PRPF38B]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.76 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.76 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[REXO4]] | +0.76 | +0.78 / +0.80 | both halves | 7e-06 | STRING 703 |
| [[TRMT10C]] | +0.75 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 | STRING 954 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | -0.66 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[TWSG1]] | -0.66 | -0.61 / -0.71 | both halves | 7e-06 |  |
| [[RPL10]] | -0.64 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[ERMP1]] | -0.63 | -0.46 / -0.68 | both halves | 2e-05 |  |
| [[HFM1]] | -0.63 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[CTSZ]] | -0.63 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[RNPEP]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.62 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[RPN1]] | -0.62 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.61 | -0.51 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.807). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.3, 1.2); signed map (-1.5, -20.5). **Vector** length 128, 48.8% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +14.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.3 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.8 | +12.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.4 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +5.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.6 | +1.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.9 | -3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -2.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | CCAAT enhancer binding protein zeta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:37,201,612-37,231,596 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CBF2, CTF2, HSP-CBF |
| Gene groups (HGNC) | CCAAT/enhancer binding proteins; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03701](https://www.uniprot.org/uniprotkb/Q03701) (CCAAT/enhancer-binding protein zeta):

> Stimulates transcription from the HSP70 promoter.

**Summary**, from NCBI Gene [10153](https://www.ncbi.nlm.nih.gov/gene/10153):

> This gene belongs to the CBF/Mak21 family. The encoded protein plays a role in cellular response to environmental stimuli through a transcriptional process that involves heat shock factors, conserved DNA elements (heat shock elements or HSEs) and CCAAT boxes. The protein acts as a DNA-binding transcriptional activator and regulates the heat-shock protein 70 (HSP70) promoter in a CCAAT-dependent manner. The protein is also involved in cell growth and differentiation, particularly, hematopoietic …

**Accessions** — [HGNC:24218](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24218) · Entrez [10153](https://www.ncbi.nlm.nih.gov/gene/10153) · UniProt [Q03701](https://www.uniprot.org/uniprotkb/Q03701) · Ensembl [ENSG00000115816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115816)

## Data

Gene col 3722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3722); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3722]; `tensor/DDL_lfc|DDL_z.npy` [3722]; `embed/gene_vectors.npy` [3722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3722 or target_col == 3722). Every well: [[CEBPZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEBPZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
