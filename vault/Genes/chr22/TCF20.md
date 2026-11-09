---
symbol: "TCF20"
type: "gene"
col: 1889
ensembl_id: "ENSG00000100207"
name: "transcription factor 20"
location: "22q13.2"
module: 18
arm: "+"
pooled_cpm: 134.61
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TCF20

*transcription factor 20* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 1.99× (z +9.5, q 1e-18, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.596× (z -13.7, q 6e-40, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.432×, NCI-H23 0.511×, LOX-IMVI 0.489×, RKO 0.529×, …; ⚠ cell-cycle shift, explains ~57% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.252×, SK-MEL-2 0.279×, HCT15 0.301×, NCI-H1792 0.340×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 0.239×, SK-MEL-2 0.310×, AsPC-1 0.306×, LS 180 0.381×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW 900 0.513×, SK-MEL-2 0.561×); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.164×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H661 0.193×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHD7]] (+0.63, fdr 1e-05), [[TRAPPC10]] (+0.59, fdr 2e-05), [[UCK2]] (+0.59, fdr 9e-06); moves opposite to [[LYSMD3]] (-0.63, fdr 7e-06), [[UFSP2]] (-0.59, fdr 1e-05), [[ARMCX3]] (-0.57, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +9.5 | 1e-18 | 39/48 (C32, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +7.2 | 2e-10 | 31/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +7.1 | 3e-10 | 31/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +7.0 | 5e-10 | 33/49 (BT-474, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +5.1 | 3e-05 | 26/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.20×** | +4.8 | 1e-04 | 21/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.003 | 21/48 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.17× | +4.1 | 0.003 | 19/48 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.0 | 0.003 | 19/45 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.15× | +3.5 | 0.026 | 14/48 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.5 | 0.026 | 12/47 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.13× | +3.1 | 0.081 | 17/47 (Hs 766T, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.081 | 16/47 (SW48, C32, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.096 | 7/48 (HS-578T, RKO, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1889.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.432×, NCI-H23 0.511×, LOX-IMVI 0.489×, RKO 0.529×, …; ⚠ cell-cycle shift, explains ~57% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.252×, SK-MEL-2 0.279×, HCT15 0.301×, NCI-H1792 0.340×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 0.239×, SK-MEL-2 0.310×, AsPC-1 0.306×, LS 180 0.381×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW 900 0.513×, SK-MEL-2 0.561×); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.164×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H661 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.596×** | -13.7 | 6e-40 | 43/49 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -13.2 | 3e-37 | 39/44 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.732×** | -7.6 | 4e-12 | 31/45 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.786×** | -6.4 | 3e-08 | 28/48 (RKO, C32, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.820×** | -5.1 | 5e-05 | 26/47 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.833× | -4.8 | 1e-04 | 24/48 (SW 900, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.884× | -4.6 | 3e-04 | 21/48 (MIA PaCa-2, NCI-H23, …) | two highest doses | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.769×** | -3.6 | 0.019 | 19/47 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.797× | -3.1 | 0.11 | 12/48 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.891× | -3.1 | 0.11 | 10/48 (NCI-H1573, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.888× | -3.0 | 0.11 | 13/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.904× | -3.0 | 0.11 | 12/49 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | 0.805× | -3.0 | 0.11 | 17/48 (LoVo, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 155 | 1 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 4.22× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -13.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[LS 180 (line)]] | wt | 188 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.15× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 155 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -13.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 130 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 178 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -21.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 139 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 350 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.561× (z -8.5) |
| [[SW480 (line)]] | alt | 168 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 2.43× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.651× (z -11.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 142 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -11.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 131 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -14.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 118 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -14.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[MIA PaCa-2 (line)]] | alt | 137 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -15.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H2030 (line)]] | alt | 196 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -12.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 204 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.00× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -15.1) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SW48 (line)]] | wt | 166 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.50× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -11.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 125 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.65× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 200 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -12.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +8.7) | — |
| [[A549 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.531× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -12.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 90.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -8.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -14.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 92.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.5) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.164× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.193× (z -8.6) |
| [[SHP-77 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.517× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 93.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.513× (z -8.6) |
| [[A-172 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 88.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 189 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 163 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD7]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TRAPPC10]] | +0.59 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[UCK2]] | +0.59 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[SFMBT1]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SLC41A3]] | +0.56 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[FOXK2]] | +0.56 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[RANBP17]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[POU2F1]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[BORCS5]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MACROD1]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[DOCK9]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TMTC4]] | +0.54 | +0.62 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYSMD3]] | -0.63 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[UFSP2]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ARMCX3]] | -0.57 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[UFL1]] | -0.56 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[RAB3GAP2]] | -0.53 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.52 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[NDUFA5]] | -0.52 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[AIMP1]] | -0.51 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[TMEM167B]] | -0.50 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SLC25A46]] | -0.50 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[MAP3K13]] | -0.49 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[MPV17]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (11.3, -39.5); signed map (-47.2, -20.5). **Vector** length 111, 31.3% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.7 | +1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -8.0 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -7.2 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.2 | -3.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,160,013-42,343,616 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AR1, SPBP |
| Gene groups (HGNC) | PHD finger proteins; TCF20 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGU0](https://www.uniprot.org/uniprotkb/Q9UGU0) (Transcription factor 20):

> Transcriptional activator that binds to the regulatory region of MMP3 and thereby controls stromelysin expression. It stimulates the activity of various transcriptional activators such as JUN, SP1, PAX6 and ETS1, suggesting a function as a coactivator.

**Summary**, from NCBI Gene [6942](https://www.ncbi.nlm.nih.gov/gene/6942):

> This gene encodes a transcription factor that recognizes the platelet-derived growth factor-responsive element in the matrix metalloproteinase 3 promoter. The encoded protein is thought to be a transcriptional coactivator, enhancing the activity of transcription factors such as JUN and SP1. Mutations in this gene are associated with autism spectrum disorders. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:11631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11631) · Entrez [6942](https://www.ncbi.nlm.nih.gov/gene/6942) · UniProt [Q9UGU0](https://www.uniprot.org/uniprotkb/Q9UGU0) · Ensembl [ENSG00000100207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100207)

## Data

Gene col 1889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1889); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1889]; `tensor/DDL_lfc|DDL_z.npy` [1889]; `embed/gene_vectors.npy` [1889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1889 or target_col == 1889). Every well: [[TCF20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCF20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
