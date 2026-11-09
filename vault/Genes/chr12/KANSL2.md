---
symbol: "KANSL2"
type: "gene"
col: 6321
ensembl_id: "ENSG00000139620"
name: "KAT8 regulatory NSL complex subunit 2"
location: "12q13.11"
module: 107
arm: "+"
pooled_cpm: 36.58
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# KANSL2

*KAT8 regulatory NSL complex subunit 2* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +16.0, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.501× (z -11.6, q 2e-28, down in 28 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.865× (z -3.6, q 0.037, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (A-427 0.124×, RPMI-7951 0.112×, HCT15 0.156×, SW480 0.389×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW1417 0.226×, RKO 0.217×, A549 0.221×, NCI-H2347 0.366×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.106×, SW48 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.236×); [[Saquinavir (drug)]] 0.5 µM in 1 line (Hs 766T 0.239×); [[Tofacitinib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0865×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX11B]] (+0.62, fdr 1e-05), [[PANK2]] (+0.62, fdr 7e-06), [[ZNF708]] (+0.61, fdr 1e-05); moves opposite to [[CREB5]] (-0.59, fdr 2e-05), [[SPAG9]] (-0.57, fdr 2e-05), [[PICALM]] (-0.53, fdr 6e-05).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +16.0 | 0e+00 | 42/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.09×** | +14.8 | 0e+00 | 47/49 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.97×** | +11.8 | 5e-30 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +10.1 | 1e-21 | 38/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +9.8 | 1e-20 | 37/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.69×** | +9.1 | 7e-18 | 36/48 (SW480, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +8.8 | 1e-16 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.65×** | +8.4 | 3e-15 | 38/47 (HT-29, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.3 | 8e-15 | 34/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +7.2 | 4e-11 | 34/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.50×** | +7.1 | 7e-11 | 32/48 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.49×** | +6.9 | 2e-10 | 32/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +6.7 | 8e-10 | 28/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +6.7 | 8e-10 | 32/48 (HEC-1-A, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.46×** | +6.6 | 2e-09 | 31/47 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 5e-04 | 19/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.002 | 17/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.002 | 20/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.003 | 19/48 (A549, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.024 | 21/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.027 | 8/48 (PANC-1, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6321.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (A-427 0.124×, RPMI-7951 0.112×, HCT15 0.156×, SW480 0.389×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW1417 0.226×, RKO 0.217×, A549 0.221×, NCI-H2347 0.366×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.106×, SW48 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.236×); [[Saquinavir (drug)]] 0.5 µM in 1 line (Hs 766T 0.239×); [[Tofacitinib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0865×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.501×** | -11.6 | 2e-28 | 28/39 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.564×** | -10.0 | 4e-21 | 33/45 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -5.3 | 3e-05 | 2/48 (Hs 766T, NCI-H661) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.776×** | -4.4 | 0.001 | 23/48 (SW480, KATO III, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -3.6 | 0.037 | 19/48 (SW480, SW 1271, …) | two highest doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.825×** | -3.4 | 0.073 | 17/47 (HepG2/C3A, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.829× | -3.2 | 0.13 | 13/47 (HOP62, SW 1271, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.781× | -3.1 | 0.14 | 11/48 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 66.0 | 7 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.60× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 24.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.7) | — |
| [[KATO III (line)]] | alt | 39.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 44.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.8 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 32.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.6) | — |
| [[A-427 (line)]] | wt | 75.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.09× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -20.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 39.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 26.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.2) | — |
| [[LoVo (line)]] | wt | 42.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 26.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 50.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 47.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 45.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -12.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -9.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.125× (z -9.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[COLO 205 (line)]] | alt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -12.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 35.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.236× (z -9.5) |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.239× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 49.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +8.7) | — |
| [[NCI-H661 (line)]] | alt | 55.5 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0865× (z -9.2) |
| [[RKO (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -12.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -13.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 50.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX11B]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[PANK2]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 | same gene group |
| [[ZNF708]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[NDUFS3]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.59 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[DBR1]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF738]] | +0.59 | +0.36 / +0.66 | both halves | 1e-04 |  |
| [[SPRYD4]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SMPD4BP]] | +0.58 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[NGDN]] | +0.56 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[PTCD1]] | +0.55 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[ZNF266]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREB5]] | -0.59 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SPAG9]] | -0.57 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[PICALM]] | -0.53 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[JUN]] | -0.52 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[VPS13A]] | -0.52 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[NCAM1]] | -0.52 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[NR6A1]] | -0.51 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[KTN1]] | -0.51 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[CAST]] | -0.50 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[NBEAL1]] | -0.48 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[ATXN1]] | -0.48 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[DNAJB5]] | -0.48 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-51.3, 4.8); signed map (-10.8, -13.9). **Vector** length 68.8, 14.0% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +6.7 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +2.5 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.2 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +7.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.7 | +0.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.2 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.1 | -10.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | KAT8 regulatory NSL complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:48,653,211-48,682,238 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20436, NSL2; previously C12orf41 |
| Gene groups (HGNC) | NSL histone acetyltransferase complex; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9L4](https://www.uniprot.org/uniprotkb/Q9H9L4) (KAT8 regulatory NSL complex subunit 2):

> Non-catalytic component of the NSL histone acetyltransferase complex, a multiprotein complex that mediates histone H4 acetylation at 'Lys-5'- and 'Lys-8' (H4K5ac and H4K8ac) at transcription start sites and promotes transcription initiation. Required for NSL complex stability and for transcription of intraciliary transport genes in both ciliated and non-ciliated cells by regulating histone H4 acetylation at 'Lys-5'- and 'Lys-12' (H4K5ac and H4K12ac) (By similarity). This is necessary for cilium …

**Summary**, from NCBI Gene [54934](https://www.ncbi.nlm.nih.gov/gene/54934):

> Predicted to be involved in positive regulation of DNA-templated transcription. Located in cytosol; nucleoplasm; and plasma membrane. Part of histone acetyltransferase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26024) · Entrez [54934](https://www.ncbi.nlm.nih.gov/gene/54934) · UniProt [Q9H9L4](https://www.uniprot.org/uniprotkb/Q9H9L4) · Ensembl [ENSG00000139620](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139620)

## Data

Gene col 6321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6321); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6321]; `tensor/DDL_lfc|DDL_z.npy` [6321]; `embed/gene_vectors.npy` [6321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6321 or target_col == 6321). Every well: [[KANSL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KANSL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
