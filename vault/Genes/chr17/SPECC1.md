---
symbol: "SPECC1"
type: "gene"
col: 4884
ensembl_id: "ENSG00000128487"
name: "sperm antigen with calponin homology and coiled-coil domains 1"
location: "17p11.2"
module: 210
arm: "+"
pooled_cpm: 101.07
n_lines_expressing: 44
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# SPECC1

*sperm antigen with calponin homology and coiled-coil domains 1* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.12× (z +45.1, q 0e+00, up in 40 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.252×, BT-474 0.179×, A-427 0.392×, SHP-77 0.459×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.173×, NCI-H23 0.453×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.0747×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND5B]] (+0.56, fdr 3e-05), [[ARHGAP10]] (+0.53, fdr 5e-05), [[SLCO3A1]] (+0.52, fdr 1e-05); moves opposite to [[WDR37]] (-0.51, fdr 1e-05), [[ACOX3]] (-0.49, fdr 7e-05), [[DDX49]] (-0.49, fdr 3e-05).
> It is in [[Module 210]], a single-armed module (tRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCDC144CP]] → it (grade B ⚠); 3 go from it, the strongest it → [[CCDC144CP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 69 in all, 29 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.12×** | +45.1 | 0e+00 | 40/41 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.43×** | +24.0 | 0e+00 | 41/42 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.33×** | +23.7 | 0e+00 | 40/42 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +22.0 | 0e+00 | 37/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.16×** | +21.6 | 0e+00 | 39/42 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.09×** | +20.6 | 0e+00 | 38/42 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +18.4 | 0e+00 | 35/41 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +16.5 | 0e+00 | 33/42 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +14.1 | 3e-43 | 31/42 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +12.4 | 2e-33 | 38/42 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +12.0 | 1e-31 | 30/41 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +12.0 | 2e-31 | 29/42 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.54×** | +11.6 | 1e-29 | 31/42 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.52×** | +11.2 | 2e-27 | 33/44 (NCI-H460, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +10.5 | 2e-24 | 32/42 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +9.9 | 1e-21 | 33/43 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +9.0 | 5e-18 | 27/43 (HepG2/C3A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +9.0 | 9e-18 | 28/42 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +8.7 | 1e-16 | 34/43 (SK-MEL-2, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +8.5 | 4e-16 | 20/42 (A549, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +6.5 | 2e-09 | 23/42 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.26×** | +6.5 | 2e-09 | 22/43 (C-33 A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4884.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.252×, BT-474 0.179×, A-427 0.392×, SHP-77 0.459×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.173×, NCI-H23 0.453×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.0747×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.877× | -3.7 | 0.10 | 14/41 (NCI-H23, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.886× | -3.5 | 0.16 | 4/42 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.892× | -3.3 | 0.21 | 10/42 (A-172, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 105 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +28.2) | — |
| [[NCI-H460 (line)]] | wt | 79.3 | 10 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +22.2) | — |
| [[A549 (line)]] | wt | 137 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +17.2) | — |
| [[COLO 205 (line)]] | alt | 42.8 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +17.3) | — |
| [[NCI-H2347 (line)]] | alt | 33.3 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +25.9) | — |
| [[SK-MEL-2 (line)]] | alt | 136 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +17.6) | — |
| [[SW 900 (line)]] | alt | 57.7 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +20.2) | — |
| [[BT-474 (line)]] | alt | 54.1 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[H4 (line)]] | wt | 47.4 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +15.7) | — |
| [[LoVo (line)]] | wt | 122 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +17.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 75.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +23.3) | — |
| [[HepG2_C3A (line)]] | wt | 77.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +18.6) | — |
| [[NCI-H1573 (line)]] | alt | 41.4 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 55.8 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +16.9) | — |
| [[A-172 (line)]] | wt | 98.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +16.4) | — |
| [[KATO III (line)]] | alt | 104 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +25.1) | — |
| [[C32 (line)]] | wt | 84.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.03× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 40.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +25.2) | — |
| [[HEC-1-A (line)]] | alt | 94.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +25.3) | — |
| [[J82 (line)]] | alt | 145 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +20.2) | — |
| [[NCI-H23 (line)]] | alt | 96.0 | 2 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.405× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[SW480 (line)]] | alt | 158 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +18.8) | — |
| [[C-33 A (line)]] | alt | 146 | 1 | 2 (2 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.19× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[HS-578T (line)]] | alt | 89.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +22.1) | — |
| [[RKO (line)]] | wt | 70.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +15.1) | — |
| [[SNU-423 (line)]] | alt | 104 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +19.5) | — |
| [[A-427 (line)]] | wt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[HCT15 (line)]] | alt | 84.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 30.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +16.9) | — |
| [[NCI-H1792 (line)]] | alt | 33.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +17.9) | — |
| [[PANC-1 (line)]] | alt | 164 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +16.1) | — |
| [[SW 1271 (line)]] | alt | 143 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +9.4) | [[Pyridoxine (drug)]] 0.5 µM 0.0747× (z -14.2) |
| [[SW1417 (line)]] | alt | 89.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +16.3) | — |
| [[SHP-77 (line)]] | alt | 249 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.459× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[SW48 (line)]] | wt | 58.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.2) | — |
| [[A498 (line)]] | wt | 344 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.97 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND5B]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ARHGAP10]] | +0.53 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[SLCO3A1]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[DRAM1]] | +0.52 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[SPAG1]] | +0.50 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[GRIP1]] | +0.49 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[FCHSD2]] | +0.49 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[NFIB]] | +0.49 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[SCN8A]] | +0.49 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[NTN1]] | +0.49 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ITGAV]] | +0.49 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[UST]] | +0.48 | +0.56 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR37]] | -0.51 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ACOX3]] | -0.49 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[DDX49]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TRMT44]] | -0.49 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[KRBOX4]] | -0.48 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SLC30A6]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[SNHG21]] | -0.45 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[RER1]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[C1orf52]] | -0.43 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[PDCD6]] | -0.43 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[TPRKB]] | -0.43 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[RBAK-RBAKDN]] | -0.43 | -0.50 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144CP]] | B | CCDC144CP activity raises SPECC1's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 4.67× lower at baseline in the lines without CCDC144CP | 5e-04 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[TOP2A]] | B | TOP2A activity lowers SPECC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144CP]] | B | SPECC1 activity raises CCDC144CP's level | lines that do not express SPECC1 (6) vs lines expressing it (44) | 3.31× lower at baseline in the lines without SPECC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BMP8B, FARP1, KIAA1522 |
| [[SEPTIN11]] | B | SPECC1 activity lowers SEPTIN11's level | lines that do not express SPECC1 (6) vs lines expressing it (44) | 1.62× higher at baseline in the lines without SPECC1 | 0.064 | ⚠ within organs, on part of the lines; also absent: BMP8B, FARP1, KIAA1522 |
| [[FGF2]] | B | SPECC1 activity lowers FGF2's level | lines that do not express SPECC1 (6) vs lines expressing it (44) | 1.59× higher at baseline in the lines without SPECC1 | 0.082 | ⚠ within organs, on part of the lines; also absent: BMP8B, FARP1, KIAA1522 |

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction -0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.5, 39.3); signed map (41.9, -16.9). **Vector** length 90.1, 23.7% of its response variance represented; |z| ≥ 3 in 1,420 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.1 | +10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +24.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.2 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | -4.1 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.2 | +20.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | sperm antigen with calponin homology and coiled-coil domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:20,008,865-20,319,026 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCMOGT-1, FLJ36955, NSP; previously CYTSB |
| Matched by | ensembl_id |

UniProt [Q5M775](https://www.uniprot.org/uniprotkb/Q5M775) carries no function annotation.

**Summary**, from NCBI Gene [92521](https://www.ncbi.nlm.nih.gov/gene/92521):

> The protein encoded by this gene belongs to the cytospin-A family. It is localized in the nucleus, and highly expressed in testis and some cancer cell lines. A chromosomal translocation involving this gene and platelet-derived growth factor receptor, beta gene (PDGFRB) may be a cause of juvenile myelomonocytic leukemia. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:30615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30615) · Entrez [92521](https://www.ncbi.nlm.nih.gov/gene/92521) · UniProt [Q5M775](https://www.uniprot.org/uniprotkb/Q5M775) · Ensembl [ENSG00000128487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128487)

## Data

Gene col 4884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4884); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4884]; `tensor/DDL_lfc|DDL_z.npy` [4884]; `embed/gene_vectors.npy` [4884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4884 or target_col == 4884). Every well: [[SPECC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPECC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
