---
symbol: "UBTD2"
type: "gene"
col: 9616
ensembl_id: "ENSG00000168246"
name: "ubiquitin domain containing 2"
location: "5q35.1"
module: 154
arm: "+"
pooled_cpm: 88.95
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# UBTD2

*ubiquitin domain containing 2* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.68× (z +14.5, q 7e-45, up in 42 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 13 lines (NCI-H1573 29.0×, SK-MEL-2 8.71×, HS-578T 15.1×, SNU-423 11.4×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 2.50×, A-172 3.02×; ⚠ cell-cycle shift, explains ~57% of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (C32 8.18×, NCI-H2030 5.02×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.422× (z -17.7, q 0e+00, down in 39 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.763× (z -5.8, q 8e-07, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SBK1]] (+0.58, fdr 4e-05), [[RALA]] (+0.57, fdr 1e-05), [[ZNRF1]] (+0.56, fdr 1e-05); moves opposite to [[EIF2B5]] (-0.50, fdr 1e-04), [[SF3B1]] (-0.49, fdr 6e-05), [[USP21]] (-0.48, fdr 5e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ROR1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9616.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 13 lines (NCI-H1573 29.0×, SK-MEL-2 8.71×, HS-578T 15.1×, SNU-423 11.4×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 2.50×, A-172 3.02×; ⚠ cell-cycle shift, explains ~57% of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (C32 8.18×, NCI-H2030 5.02×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.68×** | +14.5 | 7e-45 | 42/49 (NCI-H1573, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +5.4 | 2e-05 | 25/48 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.5 | 0.001 | 17/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.3 | 0.003 | 22/48 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.20×** | +3.8 | 0.018 | 19/47 (SW 900, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +3.5 | 0.048 | 18/49 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.12 | 11/48 (NCI-H1792, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.422×** | -17.7 | 0e+00 | 39/42 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.497×** | -14.9 | 0e+00 | 44/49 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.538×** | -12.2 | 4e-32 | 40/45 (A-427, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.815×** | -6.2 | 9e-08 | 25/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.763×** | -5.8 | 8e-07 | 30/48 (AN3 CA, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.774×** | -5.3 | 1e-05 | 26/48 (SNU-423, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.802×** | -4.7 | 2e-04 | 23/48 (SW 1088, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -4.3 | 0.001 | 22/48 (BT-474, A-427, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.819×** | -4.1 | 0.003 | 23/50 (A-172, BT-474, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.828×** | -4.0 | 0.003 | 16/48 (HOP62, SNU-423, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.876× | -4.0 | 0.003 | 6/48 (SW48, CFPAC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.736×** | -3.4 | 0.029 | 19/47 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.2 | 0.061 | 11/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.902× | -3.1 | 0.072 | 10/48 (NCI-H1792, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 130 | 3 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -17.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 66.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -14.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.452× (z -9.6) |
| [[SNU-423 (line)]] | alt | 112 | 3 (2 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 11.4× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 199 | 3 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.71× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -15.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 98.5 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +14.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -14.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 182 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0649× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -11.1) |
| [[BT-474 (line)]] | alt | 105 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.75× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.365× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 94.1 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.58× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -18.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 110 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -18.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CFPAC-1 (line)]] | alt | 94.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.15× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -14.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 163 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -13.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 86.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.498× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 77.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.52× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 195 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.87× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -16.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 85.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -20.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 97.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -13.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 86.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.8× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 74.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 13.4× (z +12.5) | — |
| [[HEC-1-A (line)]] | alt | 91.6 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.153× (z -12.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 83.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -12.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 127 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 15.1× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 67.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.99× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 80.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.79× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 82.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 29.0× (z +21.3) | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.75× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -9.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 83.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.1× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -10.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 64.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -12.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 99.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -18.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 90.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -10.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 64.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 66.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.2× (z +11.6) | — |
| [[KATO III (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0797× (z -24.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H460 (line)]] | wt | 66.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.456× (z -9.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 89.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -22.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 58.9 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.72× (z +8.5) | — |
| [[SW480 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -10.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBK1]] | +0.58 | +0.48 / +0.43 | both halves | 4e-05 |  |
| [[RALA]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZNRF1]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[UBE2R2]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[KCNK13]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SPSB1]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[MFHAS1]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PELO]] | +0.53 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[KHDRBS3]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[RHOG]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[RPLP0P2]] | +0.52 | +0.29 / +0.52 | both halves | 3e-04 |  |
| [[SLC35E4]] | +0.51 | +0.37 / +0.48 | both halves | 7e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B5]] | -0.50 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[SF3B1]] | -0.49 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[USP21]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ZNF280D]] | -0.48 | -0.62 / -0.28 | both halves | 3e-04 |  |
| [[PPWD1]] | -0.47 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ARFGAP2]] | -0.45 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.45 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[NDUFS1]] | -0.45 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[TIA1]] | -0.44 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[SCRN1]] | -0.44 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[PRR4]] | -0.43 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[SAFB]] | -0.42 | -0.35 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROR1-AS1]] | B | ROR1-AS1 activity raises UBTD2's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 1.46× lower at baseline in the lines without ROR1-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.0, 36.1); signed map (-12.8, 46.7). **Vector** length 105, 29.2% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +14.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +5.3 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | +0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.3 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -5.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.3 | -3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.8 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:172,209,646-172,283,764 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DC-UbP, MGC30022 |
| Matched by | ensembl_id |

UniProt [Q8WUN7](https://www.uniprot.org/uniprotkb/Q8WUN7) carries no function annotation.

**Summary**, from NCBI Gene [92181](https://www.ncbi.nlm.nih.gov/gene/92181):

> Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24463) · Entrez [92181](https://www.ncbi.nlm.nih.gov/gene/92181) · UniProt [Q8WUN7](https://www.uniprot.org/uniprotkb/Q8WUN7) · Ensembl [ENSG00000168246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168246)

## Data

Gene col 9616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9616); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9616]; `tensor/DDL_lfc|DDL_z.npy` [9616]; `embed/gene_vectors.npy` [9616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9616 or target_col == 9616). Every well: [[UBTD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBTD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
