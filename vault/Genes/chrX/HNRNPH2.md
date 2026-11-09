---
symbol: "HNRNPH2"
type: "gene"
col: 4780
ensembl_id: "ENSG00000126945"
name: "heterogeneous nuclear ribonucleoprotein H2"
location: "Xq22.1"
module: 16
arm: "+"
pooled_cpm: 31.12
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# HNRNPH2

*heterogeneous nuclear ribonucleoprotein H2* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.49× (z +20.5, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.93× (z +11.4, q 1e-27, up in 39 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (A-427 0.0595×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.114×; ⚠ cell-cycle shift, explains ~23% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (AN3 CA 0.143×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.216×); [[Allantoin (drug)]] 0.5 µM in 1 line (CHP-212 0.108×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF776]] (+0.80, fdr 7e-06), [[ZNF268]] (+0.75, fdr 7e-06), [[FOSL2]] (+0.75, fdr 7e-06); moves opposite to [[COG5]] (-0.67, fdr 9e-06), [[RASA2]] (-0.66, fdr 1e-05), [[SRD5A1]] (-0.66, fdr 8e-06).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.49×** | +20.5 | 0e+00 | 44/48 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.34×** | +13.0 | 4e-36 | 41/48 (NCI-H1573, A498, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.93×** | +11.4 | 1e-27 | 39/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +10.8 | 6e-25 | 40/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +9.3 | 2e-18 | 35/44 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +8.6 | 7e-16 | 39/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +8.3 | 1e-14 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +7.9 | 3e-13 | 33/42 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +7.6 | 2e-12 | 26/37 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +7.5 | 3e-12 | 37/48 (HT-29, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +6.4 | 8e-09 | 31/46 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.49×** | +6.3 | 1e-08 | 32/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.47×** | +6.1 | 4e-08 | 30/46 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.44×** | +5.8 | 3e-07 | 28/46 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +5.4 | 3e-06 | 28/47 (SW480, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.0 | 2e-05 | 22/48 (SK-MEL-2, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.001 | 23/45 (J82, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.030 | 7/48 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.15× | +3.1 | 0.043 | 13/48 (MIA PaCa-2, KATO III, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.073 | 10/48 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.076 | 19/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4780.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (A-427 0.0595×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.114×; ⚠ cell-cycle shift, explains ~23% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (AN3 CA 0.143×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.216×); [[Allantoin (drug)]] 0.5 µM in 1 line (CHP-212 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | 0.798× | -3.6 | 0.15 | 18/48 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.799× | -3.5 | 0.15 | 20/46 (AN3 CA, H4, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.822× | -3.1 | 0.32 | 12/48 (HT-29, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.4 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 40.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +10.4) | — |
| [[J82 (line)]] | alt | 30.9 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +17.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 31.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +19.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +11.7) | — |
| [[A498 (line)]] | wt | 21.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +18.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.48× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 50.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +16.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.52× (z +8.5) | — |
| [[A-427 (line)]] | wt | 34.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.83× (z +8.7) | [[Bortezomib (drug)]] 5 µM 0.0595× (z -12.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 13.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +14.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 58.0 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -10.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Pemetrexed (drug)]] 5 µM 0.143× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 33.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +15.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[COLO 205 (line)]] | alt | 37.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +13.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HT-29 (line)]] | alt | 41.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.60× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.5) ⚠ cell-cycle shift, explains ~34% of this change | [[Imiquimod (maleate) (drug)]] 5 µM 0.216× (z -8.5) |
| [[A549 (line)]] | wt | 19.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[C32 (line)]] | wt | 22.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +11.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[CFPAC-1 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.108× (z -8.5) |
| [[H4 (line)]] | wt | 24.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HOP62 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[Hs 766T (line)]] | wt | 37.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +14.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 56.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LoVo (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +14.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LS 180 (line)]] | wt | 29.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +14.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW 900 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW1417 (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 47.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.34× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF776]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.75 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[FOSL2]] | +0.75 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[UBQLN2]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[MED12]] | +0.73 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[LYRM2]] | +0.72 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[ZNF24]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[REPIN1]] | +0.70 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[LIG4]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.68 | +0.74 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG5]] | -0.67 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[RASA2]] | -0.66 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[SRD5A1]] | -0.66 | -0.68 / -0.58 | both halves | 8e-06 |  |
| [[SMG1P5]] | -0.64 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[RGS10]] | -0.64 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[CORO7]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[SCAI]] | -0.62 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[NTAQ1]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | -0.61 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PALS2]] | -0.60 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[SLC37A3]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.7, 11.7); signed map (3.4, -28.5). **Vector** length 94.6, 22.6% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +8.4 | +20.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +10.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +11.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.1 | +13.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +5.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.4 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +2.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.1 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -0.7 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein H2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,408,222-101,414,133 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hnRNPH', FTP3, HNRPH'; previously HNRPH2 |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P55795](https://www.uniprot.org/uniprotkb/P55795) (Heterogeneous nuclear ribonucleoprotein H2):

> This protein is a component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complexes which provide the substrate for the processing events that pre-mRNAs undergo before becoming functional, translatable mRNAs in the cytoplasm. Binds poly(RG).

**Summary**, from NCBI Gene [3188](https://www.ncbi.nlm.nih.gov/gene/3188):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins have …

**Accessions** — [HGNC:5042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5042) · Entrez [3188](https://www.ncbi.nlm.nih.gov/gene/3188) · UniProt [P55795](https://www.uniprot.org/uniprotkb/P55795) · Ensembl [ENSG00000126945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126945)

## Data

Gene col 4780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4780); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4780]; `tensor/DDL_lfc|DDL_z.npy` [4780]; `embed/gene_vectors.npy` [4780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4780 or target_col == 4780). Every well: [[HNRNPH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
