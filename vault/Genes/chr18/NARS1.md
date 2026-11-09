---
symbol: "NARS1"
type: "gene"
col: 5560
ensembl_id: "ENSG00000134440"
name: "asparaginyl-tRNA synthetase 1"
location: "18q21.31"
module: 63
arm: "+"
pooled_cpm: 108.5
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# NARS1

*asparaginyl-tRNA synthetase 1* — 18q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.49× (z +16.4, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.82× (z +7.9, q 5e-13, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (PANC-1 0.410×, RKO 0.430×, A-427 0.543×, SW1417 0.557×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 0.417×, KATO III 0.432×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.406×, PANC-1 0.428×; ⚠ cell-cycle shift, explains ~23% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW 1271 0.0897×); [[Cabozantinib (S-malate) (drug)]] 5 µM in 1 line (SW 1088 0.0772×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TARS1]] (+0.85, fdr 7e-06), [[XPOT]] (+0.84, fdr 7e-06), [[IARS1]] (+0.83, fdr 7e-06); moves opposite to [[POLR2L]] (-0.61, fdr 1e-05), [[H2AJ]] (-0.50, fdr 2e-04), [[DCAF15]] (-0.47, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PSAT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +16.4 | 0e+00 | 48/48 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +15.4 | 0e+00 | 43/43 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +10.5 | 2e-23 | 40/44 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +7.9 | 5e-13 | 44/47 (LoVo, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +7.4 | 2e-11 | 38/46 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +6.6 | 4e-09 | 44/47 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.17×** | +5.3 | 9e-06 | 45/47 (LOX-IMVI, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 34/47 (C-33 A, LOX-IMVI, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.85×** | +4.2 | 0.002 | 38/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.004 | 28/47 (NCI-H2030, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.007 | 33/46 (LOX-IMVI, NCI-H23, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.35×** | +3.8 | 0.007 | 23/49 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.007 | 29/47 (NCI-H2030, RPMI-7951, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.007 | 35/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.33×** | +3.6 | 0.010 | 28/46 (CFPAC-1, LOX-IMVI, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.69×** | +3.6 | 0.010 | 32/47 (A549, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.011 | 24/47 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.012 | 26/47 (NCI-H23, LOX-IMVI, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.016 | 21/47 (SW48, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.051 | 26/47 (NCI-H1573, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.064 | 16/48 (LOX-IMVI, NCI-H23, …) | two highest doses |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.081 | 21/47 (RKO, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5560.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (PANC-1 0.410×, RKO 0.430×, A-427 0.543×, SW1417 0.557×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 0.417×, KATO III 0.432×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.406×, PANC-1 0.428×; ⚠ cell-cycle shift, explains ~23% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW 1271 0.0897×); [[Cabozantinib (S-malate) (drug)]] 5 µM in 1 line (SW 1088 0.0772×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.842× | -3.2 | 0.79 | 20/47 (SW 1271, HT-29, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 144 | 2 (2 ⚠) | 6 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.417× (z -10.8) |
| [[A-427 (line)]] | wt | 242 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -10.7) ⚠ cell-cycle shift, explains ~23% of this change |
| [[C32 (line)]] | wt | 69.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.84× (z +8.5) | — |
| [[A498 (line)]] | wt | 106 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +15.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 99.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +15.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 120 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.00× (z +16.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 75.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +11.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 208 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.41× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.432× (z -8.9) |
| [[LoVo (line)]] | wt | 176 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.32× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 88.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.42× (z +15.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 180 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 56.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 121 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 133 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 63.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +15.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 55.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 64.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.50× (z +15.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 42.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 195 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 41.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 96.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +10.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 92.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +14.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 165 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 82.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 84.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +15.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 59.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 158 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.11× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 61.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 49.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 108 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 164 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 66.1 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 5 µM 0.0772× (z -8.5) |
| [[SW 1271 (line)]] | alt | 82.0 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0897× (z -8.8) |
| [[BT-474 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 196 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARS1]] | +0.85 | +0.83 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 924 |
| [[XPOT]] | +0.84 | +0.77 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[IARS1]] | +0.83 | +0.74 / +0.82 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 965 |
| [[HSPA9]] | +0.82 | +0.75 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TCEA1]] | +0.81 | +0.74 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[YARS1]] | +0.81 | +0.77 / +0.80 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 966 |
| [[MTHFD2]] | +0.80 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[AARS1]] | +0.80 | +0.76 / +0.79 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 947 |
| [[PSAT1]] | +0.80 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[EPRS1]] | +0.78 | +0.74 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 998 |
| [[CEBPG]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[MARS1]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 886 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2L]] | -0.61 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[H2AJ]] | -0.50 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[DCAF15]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[SMAD3]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[CYP2U1-AS1]] | -0.46 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSAT1]] | B | PSAT1 activity raises NARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without PSAT1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[CHAC1]] | B | CHAC1 activity raises NARS1's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.53× lower at baseline in the lines without CHAC1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity raises NARS1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.33× lower at baseline in the lines without ANK2 | 0.086 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[SLC38A1]] | C | SLC38A1 activity raises NARS1's level | lines that do not express SLC38A1 (3) vs lines expressing it (47) | 1.49× lower at baseline in the lines without SLC38A1 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ALPK3, TRIB3, SAMHD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, 47.3); signed map (-13.9, 24.0). **Vector** length 107, 37.4% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.65 to 16); *mTORC1 signaling* (hallmark, mean cos +0.62 to 20); *unfolded protein response* (hallmark, mean cos +0.72 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.8 | +4.6 |
|  | [[Artesunate (drug)]] 5 µM |  | +5.5 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +4.9 | +4.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.6 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.5 | +5.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.4 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +3.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.0 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.1 | +0.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.0 | -0.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.8 | +1.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.3 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | asparaginyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.31 — chr18:57,600,656-57,622,213 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AsnRS; previously NARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 3 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [O43776](https://www.uniprot.org/uniprotkb/O43776) (Asparagine--tRNA ligase, cytoplasmic):

> Catalyzes the attachment of asparagine to tRNA(Asn) in a two-step reaction: asparagine is first activated by ATP to form Asn-AMP and then transferred to the acceptor end of tRNA(Asn). In addition to its essential role in protein synthesis, acts as a signaling molecule that induced migration of CCR3-expressing cells. Has an essential role in the development of the cerebral cortex, being required for proper proliferation of radial glial cells.

**Summary**, from NCBI Gene [4677](https://www.ncbi.nlm.nih.gov/gene/4677):

> Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Asparaginyl-tRNA synthetase is localized to the cytoplasm and belongs to the class II family of tRNA synthetases. The N-terminal domain represents the signature sequence for the eukaryotic asparaginyl-tRNA synthetases. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7643) · Entrez [4677](https://www.ncbi.nlm.nih.gov/gene/4677) · UniProt [O43776](https://www.uniprot.org/uniprotkb/O43776) · Ensembl [ENSG00000134440](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134440)

## Data

Gene col 5560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5560); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5560]; `tensor/DDL_lfc|DDL_z.npy` [5560]; `embed/gene_vectors.npy` [5560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5560 or target_col == 5560). Every well: [[NARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
