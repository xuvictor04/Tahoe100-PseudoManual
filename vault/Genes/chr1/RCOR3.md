---
symbol: "RCOR3"
type: "gene"
col: 3935
ensembl_id: "ENSG00000117625"
name: "REST corepressor 3"
location: "1q32.2-q32.3"
module: 45
arm: "+"
pooled_cpm: 87.48
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# RCOR3

*REST corepressor 3* — 1q32.2-q32.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 2.25×, KATO III 1.99×, SW48 2.32×; ⚠ cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.31×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.467× (z -12.2, q 2e-31, down in 42 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.544× (z -9.7, q 3e-20, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP33]] (+0.73, fdr 7e-06), [[MBIP]] (+0.69, fdr 7e-06), [[FBXO9]] (+0.68, fdr 7e-06); moves opposite to [[RNF32-AS1]] (-0.66, fdr 7e-06), [[TBILA]] (-0.64, fdr 7e-06), [[DNAH1]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3935.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 2.25×, KATO III 1.99×, SW48 2.32×; ⚠ cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.31×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.24× | +3.2 | 0.31 | 22/50 (C32, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.15× | +3.1 | 0.31 | 4/48 (SK-MEL-2, COLO 205, …) | rises with dose | position effect removed |
| [[Tomivosertib (drug)]] 5 µM |  | 1.44× | +3.1 | 0.31 | 13/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.21× | +3.1 | 0.31 | 18/49 (PANC-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3935.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.467×** | -12.2 | 2e-31 | 42/49 (NCI-H1573, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.458×** | -12.0 | 6e-31 | 40/44 (SW1417, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.470×** | -11.2 | 1e-26 | 38/45 (NCI-H23, RKO, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.544×** | -9.7 | 3e-20 | 45/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.665×** | -6.5 | 8e-09 | 43/48 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.666×** | -6.5 | 8e-09 | 30/48 (NCI-H1573, C32, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.670×** | -6.4 | 1e-08 | 43/48 (SNU-423, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -6.0 | 2e-07 | 34/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.726×** | -5.1 | 2e-05 | 35/48 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -4.3 | 9e-04 | 27/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.771×** | -4.1 | 0.002 | 27/48 (CHP-212, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.779×** | -4.0 | 0.003 | 26/48 (CFPAC-1, A-172, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.654×** | -3.5 | 0.017 | 29/48 (BT-474, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.659×** | -3.5 | 0.020 | 24/48 (MIA PaCa-2, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.806×** | -3.4 | 0.022 | 25/48 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.022 | 21/48 (CFPAC-1, A549, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.808×** | -3.4 | 0.022 | 22/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.670×** | -3.3 | 0.023 | 20/47 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.673×** | -3.3 | 0.025 | 22/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.693×** | -3.2 | 0.038 | 21/48 (RPMI-7951, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.038 | 20/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.822×** | -3.0 | 0.060 | 21/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.707×** | -2.9 | 0.078 | 17/48 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 90.3 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -14.0) |
| [[C32 (line)]] | wt | 84.3 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.204× (z -14.9) |
| [[CFPAC-1 (line)]] | alt | 92.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 119 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.492× (z -8.7) |
| [[SNU-423 (line)]] | alt | 108 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.326× (z -12.0) |
| [[A-172 (line)]] | wt | 101 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.415× (z -9.6) |
| [[HT-29 (line)]] | alt | 87.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.354× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 74.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -12.1) |
| [[LS 180 (line)]] | wt | 96.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 60.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 90.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.507× (z -8.7) |
| [[SW1417 (line)]] | alt | 89.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 87.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[CHP-212 (line)]] | wt | 185 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HCT15 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.301× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 75.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -9.3) |
| [[HS-578T (line)]] | alt | 63.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.278× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 70.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 79.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.269× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[AN3 CA (line)]] | alt | 87.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[AsPC-1 (line)]] | alt | 73.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 80.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 89.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 84.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 73.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.313× (z -11.3) |
| [[SW 900 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 91.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.449× (z -8.5) |
| [[BT-474 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 101 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP33]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[MBIP]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[FBXO9]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[KBTBD3]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ELF2]] | +0.66 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[TXNDC16]] | +0.66 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[SNX2]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.64 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[KCTD3]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ZNF224]] | +0.63 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[MLLT10]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[DENND4C]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF32-AS1]] | -0.66 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[TBILA]] | -0.64 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[DNAH1]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[BLZF2P]] | -0.63 | -0.57 / -0.62 | both halves | 8e-06 |  |
| [[BACH1]] | -0.62 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[SPTBN5]] | -0.62 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[CHRNA10]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[UTP11]] | -0.61 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[NABP1]] | -0.60 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[GHRLOS]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[GTPBP4]] | -0.60 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[LINC01204]] | -0.60 | -0.61 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.2, -24.6); signed map (-24.3, -7.6). **Vector** length 101, 30.7% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.0 | +2.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.9 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -4.6 | -11.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.0 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | REST corepressor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2-q32.3 — chr1:211,258,377-211,316,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10876 |
| Gene groups (HGNC) | Myb/SANT domain containing; CoREST complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2K3](https://www.uniprot.org/uniprotkb/Q9P2K3) (REST corepressor 3):

> May act as a component of a corepressor complex that represses transcription.

**Summary**, from NCBI Gene [55758](https://www.ncbi.nlm.nih.gov/gene/55758):

> Predicted to enable enzyme binding activity and transcription corepressor activity. Predicted to be involved in negative regulation of DNA-templated transcription and regulation of transcription by RNA polymerase II. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25594) · Entrez [55758](https://www.ncbi.nlm.nih.gov/gene/55758) · UniProt [Q9P2K3](https://www.uniprot.org/uniprotkb/Q9P2K3) · Ensembl [ENSG00000117625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117625)

## Data

Gene col 3935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3935); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3935]; `tensor/DDL_lfc|DDL_z.npy` [3935]; `embed/gene_vectors.npy` [3935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3935 or target_col == 3935). Every well: [[RCOR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCOR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
