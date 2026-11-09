---
symbol: "ETFA"
type: "gene"
col: 6396
ensembl_id: "ENSG00000140374"
name: "electron transfer flavoprotein subunit alpha"
location: "15q24.2-q24.3"
module: 24
arm: "-"
pooled_cpm: 134.03
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ETFA

*electron transfer flavoprotein subunit alpha* — 15q24.2-q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.75× (z +15.8, q 0e+00, up in 44 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.80× (z +8.7, q 4e-16, up in 36 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (AsPC-1 0.459×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (SW 1088 0.0876×; ⚠ toxic); [[Sunitinib (drug)]] 5 µM in 1 line (SW 1088 0.120×; ⚠ toxic).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPZA1]] (+0.45, fdr 1e-04), [[RAB10]] (+0.42, fdr 9e-04, ⚠ not reproduced), [[PCSK7]] (+0.41, fdr 2e-04), [[ANKRD13C]] (+0.41, fdr 7e-05); moves opposite to [[EIF4A3]] (-0.51, fdr 2e-05), [[BRD2]] (-0.43, fdr 7e-05), [[NCKIPSD]] (-0.42, fdr 4e-05).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.75×** | +15.8 | 0e+00 | 44/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +14.8 | 0e+00 | 32/48 (A549, J82, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.70×** | +14.4 | 2e-44 | 38/44 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.51×** | +10.7 | 2e-24 | 34/45 (A549, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.47×** | +10.5 | 1e-23 | 34/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +9.3 | 1e-18 | 28/49 (MIA PaCa-2, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.38×** | +9.0 | 2e-17 | 39/48 (HT-29, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +8.7 | 4e-16 | 36/49 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +8.5 | 1e-15 | 38/48 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.31×** | +7.5 | 3e-12 | 32/48 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.20×** | +4.9 | 4e-05 | 25/50 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.18× | +4.5 | 3e-04 | 22/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.5 | 4e-04 | 17/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.17× | +4.4 | 4e-04 | 21/48 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.4 | 4e-04 | 20/48 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Rosiglitazone (drug)]] 5 µM |  | 1.17× | +4.3 | 7e-04 | 17/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Mifepristone (drug)]] 5 µM |  | 1.16× | +4.1 | 0.001 | 15/48 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 1.14× | +3.7 | 0.005 | 13/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.09× | +3.6 | 0.008 | 4/49 (LoVo, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.4 | 0.015 | 4/49 (LOX-IMVI, SW 900, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.025 | 10/49 (NCI-H23, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.025 | 12/46 (SK-MEL-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.044 | 12/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bexarotene (drug)]] 5 µM |  | 1.11× | +2.9 | 0.070 | 7/48 (SW480, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6396.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (AsPC-1 0.459×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (SW 1088 0.0876×; ⚠ toxic); [[Sunitinib (drug)]] 5 µM in 1 line (SW 1088 0.120×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adenine (drug)]] 5 µM |  | 0.919× | -3.4 | 0.21 | 2/48 (HS-578T, CHP-212) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.889× | -3.4 | 0.21 | 22/48 (NCI-H23, RKO, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.803× | -3.3 | 0.21 | 14/48 (BT-474, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.811× | -3.1 | 0.25 | 11/49 (A-427, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 192 | 8 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +19.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 156 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 100 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[PANC-1 (line)]] | alt | 130 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +15.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Rosiglitazone (drug)]] 5 µM 1.64× (z +8.5) | — |
| [[A-172 (line)]] | wt | 98.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +17.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 135 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +17.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.87× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 114 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[KATO III (line)]] | alt | 178 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 145 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 146 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H460 (line)]] | wt | 140 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 73.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C-33 A (line)]] | alt | 89.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 92.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[J82 (line)]] | alt | 121 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +18.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 294 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.75× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 1088 (line)]] | alt | 99.8 | 0 | 2 (2 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0876× (z -9.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 93.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.459× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[BT-474 (line)]] | alt | 211 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HepG2_C3A (line)]] | wt | 161 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 57.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 66.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 213 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.84× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 79.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 98.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.27× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.20× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 81.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +10.2) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[A498 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 153 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 86.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 189 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 147 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPZA1]] | +0.45 | +0.33 / +0.37 | both halves | 1e-04 |  |
| [[RAB10]] | +0.42 | +0.19 / +0.47 | ⚠ not reproduced | 9e-04 |  |
| [[PCSK7]] | +0.41 | +0.56 / +0.29 | both halves | 2e-04 |  |
| [[ANKRD13C]] | +0.41 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[HIGD1A]] | +0.40 | +0.33 / +0.40 | both halves | 1e-04 | pathway: Aerobic respiration and respiratory electron transport |
| [[CAPZB]] | +0.40 | +0.15 / +0.39 | ⚠ not reproduced | 0.001 |  |
| [[NDUFB3]] | +0.40 | +0.57 / +0.24 | both halves | 5e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[ATAD1]] | +0.39 | +0.46 / +0.39 | both halves | 6e-05 |  |
| [[SDHC]] | +0.39 | +0.47 / +0.30 | both halves | 2e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 641 |
| [[BTBD10]] | +0.39 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[ATP5MG]] | +0.39 | +0.40 / +0.32 | both halves | 2e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[GNB1]] | +0.38 | +0.10 / +0.39 | ⚠ not reproduced | 0.003 |  |
| [[SELENOF]] | +0.38 | +0.32 / +0.42 | both halves | 2e-04 |  |
| [[SUCLG1]] | +0.38 | +0.40 / +0.43 | both halves | 5e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 956 |
| [[SMN2]] | +0.38 | +0.43 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4A3]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[BRD2]] | -0.43 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[NCKIPSD]] | -0.42 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[RBM14]] | -0.42 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[USP21]] | -0.41 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[SRP14-DT]] | -0.39 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[MRM3]] | -0.38 | -0.09 / -0.46 | ⚠ not reproduced | 0.003 |  |
| [[CCSAP]] | -0.37 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[NXF1]] | -0.37 | -0.36 / -0.32 | both halves | 1e-04 |  |
| [[MYLIP]] | -0.37 | -0.37 / -0.22 | both halves | 6e-04 |  |
| [[FBXL14]] | -0.37 | -0.05 / -0.46 | ⚠ not reproduced | 0.005 |  |
| [[FEM1C]] | -0.37 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[PPP1R3E]] | -0.37 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[DNAJA1]] | -0.36 | -0.23 / -0.36 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.0111). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.6, -17.2); signed map (-47.9, -24.9). **Vector** length 82.0, 18.3% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.4 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.9 | +15.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.4 | +14.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | +1.8 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +3.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.0 | -3.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -4.1 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | +1.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | electron transfer flavoprotein subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2-q24.3 — chr15:76,188,555-76,311,730 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GA2, EMA, MADD |
| Gene groups (HGNC) | Flavoproteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P13804](https://www.uniprot.org/uniprotkb/P13804) (Electron transfer flavoprotein subunit alpha, mitochondrial):

> Heterodimeric electron transfer flavoprotein that accepts electrons from several mitochondrial dehydrogenases, including acyl-CoA dehydrogenases, glutaryl-CoA and sarcosine dehydrogenase. It transfers the electrons to the main mitochondrial respiratory chain via ETF-ubiquinone oxidoreductase (ETF dehydrogenase). Required for normal mitochondrial fatty acid oxidation and normal amino acid metabolism.

**Summary**, from NCBI Gene [2108](https://www.ncbi.nlm.nih.gov/gene/2108):

> ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in large excretion of glutaric, lactic, ethylmalonic, butyric, isobutyric, 2-methyl-butyric, and …

**Accessions** — [HGNC:3481](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3481) · Entrez [2108](https://www.ncbi.nlm.nih.gov/gene/2108) · UniProt [P13804](https://www.uniprot.org/uniprotkb/P13804) · Ensembl [ENSG00000140374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140374)

## Data

Gene col 6396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6396); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6396]; `tensor/DDL_lfc|DDL_z.npy` [6396]; `embed/gene_vectors.npy` [6396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6396 or target_col == 6396). Every well: [[ETFA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETFA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
