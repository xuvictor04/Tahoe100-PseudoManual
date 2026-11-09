---
symbol: "USP10"
type: "gene"
col: 2332
ensembl_id: "ENSG00000103194"
name: "ubiquitin specific peptidase 10"
location: "16q24.1"
module: 33
arm: "+"
pooled_cpm: 144.78
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# USP10

*ubiquitin specific peptidase 10* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.14× (z +15.4, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.514× (z -12.0, q 1e-30, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SNU-1 0.0503×, RKO 0.144×, NCI-H23 0.233×, SK-MEL-2 0.244×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (SK-MEL-2 0.0808×, A-427 0.206×, C-33 A 0.215×, MIA PaCa-2 0.262×, …; ⚠ toxic; transcription drop); [[Menadione (drug)]] 0.05 µM in 1 line (SW 1088 0.0733×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR43]] (+0.70, fdr 7e-06), [[WDR36]] (+0.69, fdr 7e-06), [[NME1]] (+0.68, fdr 7e-06); moves opposite to [[TP53INP2]] (-0.54, fdr 1e-05), [[TOM1]] (-0.52, fdr 2e-05), [[ATP6V0C]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM78B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.14×** | +15.4 | 0e+00 | 49/49 (SW480, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.55×** | +11.9 | 2e-30 | 48/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +8.9 | 1e-16 | 44/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +7.2 | 1e-10 | 41/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +7.1 | 2e-10 | 34/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +6.6 | 4e-09 | 38/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 1e-05 | 34/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 1e-05 | 30/48 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +5.2 | 1e-05 | 35/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.8 | 1e-04 | 31/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **1.29×** | +4.5 | 3e-04 | 32/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.9 | 0.004 | 26/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +3.6 | 0.016 | 24/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.4 | 0.025 | 19/38 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.20× | +3.2 | 0.048 | 21/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.048 | 21/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.077 | 12/49 (H4, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2332.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SNU-1 0.0503×, RKO 0.144×, NCI-H23 0.233×, SK-MEL-2 0.244×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (SK-MEL-2 0.0808×, A-427 0.206×, C-33 A 0.215×, MIA PaCa-2 0.262×, …; ⚠ toxic; transcription drop); [[Menadione (drug)]] 0.05 µM in 1 line (SW 1088 0.0733×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.514×** | -12.0 | 1e-30 | 45/49 (SNU-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.502×** | -12.0 | 1e-30 | 39/44 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.571×** | -9.4 | 1e-18 | 39/45 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.834× | -3.2 | 0.22 | 22/47 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Alpelisib (drug)]] 5 µM |  | 0.727× | -3.0 | 0.26 | 20/47 (HCT15, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 186 | 4 | 5 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 5.91× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 143 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.39× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -19.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 174 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.63× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -12.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 230 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.26× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 265 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.57× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 116 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -12.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 196 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.62× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -11.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 166 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 116 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 138 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 5.88× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 76.9 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.42× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -9.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 220 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.36× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -22.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 180 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.27× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0503× (z -30.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 180 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.68× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 142 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.10× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.532× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 134 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.90× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 178 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -17.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 89.4 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.55× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -11.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 101 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.11× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 143 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.94× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -10.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 170 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.36× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -14.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -11.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 133 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.81× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 109 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.98× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -12.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 144 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.25× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0808× (z -29.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 92.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.07× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.73× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 154 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.460× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 145 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 186 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.23× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -20.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 95.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.44× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 94.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 142 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.92× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -11.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 96.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.48× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 194 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.19× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 133 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.05× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 141 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.98× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 92.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.25× (z +14.2) | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0733× (z -10.9) |
| [[A-172 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 196 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 211 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR43]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[WDR36]] | +0.69 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[NME1]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[ALDH1B1]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[WDR3]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PHB1]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[NSUN2]] | +0.62 | +0.77 / +0.47 | both halves | 2e-05 |  |
| [[NARS2]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[MRPL24]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HMBS]] | +0.61 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[STARD7]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53INP2]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TOM1]] | -0.52 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ATP6V0C]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | FAM78B activity raises USP10's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without FAM78B | 0.089 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.3, -39.5); signed map (-6.9, -50.5). **Vector** length 79.9, 24.9% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.51 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +11.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.8 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | -0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | -0.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | +8.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | +5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | -2.9 | +4.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | +0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:84,699,986-84,779,922 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBPO, KIAA0190 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 6 pathways, smallest: Termination of translesion DNA synthesis; Translesion synthesis by Y family DNA polymerases bypasses lesions on DNA template; DNA Damage Bypass |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14694](https://www.uniprot.org/uniprotkb/Q14694) (Ubiquitin carboxyl-terminal hydrolase 10):

> Hydrolase that can remove conjugated ubiquitin from target proteins such as p53/TP53, RPS2/us5, RPS3/us3, RPS10/eS10, BECN1, SNX3 and CFTR. Acts as an essential regulator of p53/TP53 stability: in unstressed cells, specifically deubiquitinates p53/TP53 in the cytoplasm, leading to counteract MDM2 action and stabilize p53/TP53. Following DNA damage, translocates to the nucleus and deubiquitinates p53/TP53, leading to regulate the p53/TP53-dependent DNA damage response. Component of a regulatory …

**Summary**, from NCBI Gene [9100](https://www.ncbi.nlm.nih.gov/gene/9100):

> Ubiquitin is a highly conserved protein that is covalently linked to other proteins to regulate their function and degradation. This gene encodes a member of the ubiquitin-specific protease family of cysteine proteases. The enzyme specifically cleaves ubiquitin from ubiquitin-conjugated protein substrates. The protein is found in the nucleus and cytoplasm. It functions as a co-factor of the DNA-bound androgen receptor complex, and is inhibited by a protein in the Ras-GTPase pathway. The human …

**Accessions** — [HGNC:12608](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12608) · Entrez [9100](https://www.ncbi.nlm.nih.gov/gene/9100) · UniProt [Q14694](https://www.uniprot.org/uniprotkb/Q14694) · Ensembl [ENSG00000103194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103194)

## Data

Gene col 2332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2332); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2332]; `tensor/DDL_lfc|DDL_z.npy` [2332]; `embed/gene_vectors.npy` [2332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2332 or target_col == 2332). Every well: [[USP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
