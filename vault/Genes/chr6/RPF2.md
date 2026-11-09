---
symbol: "RPF2"
type: "gene"
col: 12408
ensembl_id: "ENSG00000197498"
name: "ribosome production factor 2 homolog"
location: "6q21"
module: 1
arm: "+"
pooled_cpm: 70.48
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RPF2

*ribosome production factor 2 homolog* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +13.3, q 1e-37, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.52× (z +12.7, q 9e-35, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 0.5 µM: 0.757× (z -3.8, q 0.071, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.451×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX18]] (+0.70, fdr 7e-06), [[UTP14A]] (+0.68, fdr 7e-06), [[ESF1]] (+0.66, fdr 7e-06); moves opposite to [[NAGA]] (-0.51, fdr 1e-04), [[PPM1A]] (-0.50, fdr 3e-05), [[MYL6]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.98×** | +13.3 | 1e-37 | 40/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.52×** | +12.7 | 9e-35 | 44/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.24×** | +10.4 | 3e-23 | 45/49 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.01×** | +9.4 | 5e-19 | 42/49 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.86×** | +8.5 | 1e-15 | 46/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.79×** | +7.8 | 8e-13 | 35/44 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.75×** | +7.7 | 1e-12 | 41/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.63×** | +6.5 | 6e-09 | 37/48 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.59×** | +6.4 | 1e-08 | 37/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.0 | 1e-07 | 36/48 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.28×** | +6.0 | 1e-07 | 44/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +5.5 | 2e-06 | 32/48 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.2 | 7e-06 | 35/48 (C-33 A, SK-MEL-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.00×** | +5.0 | 2e-05 | 41/48 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.98×** | +4.9 | 3e-05 | 39/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.68×** | +4.8 | 6e-05 | 38/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.5 | 3e-04 | 28/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.62×** | +4.4 | 3e-04 | 42/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.83×** | +4.4 | 4e-04 | 33/48 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +4.2 | 6e-04 | 32/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.75×** | +4.0 | 0.001 | 30/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.026 | 20/48 (NCI-H2347, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12408.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.451×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.757×** | -3.8 | 0.071 | 28/47 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.740×** | -3.7 | 0.071 | 27/50 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.777× | -3.4 | 0.11 | 23/47 (SW480, H4, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.630× | -3.3 | 0.11 | 22/50 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.844× | -3.3 | 0.13 | 20/48 (SW480, A-427, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | 0.656× | -3.1 | 0.22 | 17/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 36.1 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +17.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.52× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 49.8 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +17.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.74× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 207 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +12.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +11.4) | — |
| [[A549 (line)]] | wt | 44.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 60.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 58.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.03× (z +12.1) | — |
| [[LoVo (line)]] | wt | 61.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 54.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.59× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 79.2 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.45× (z +11.1) | — |
| [[A-172 (line)]] | wt | 40.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +13.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.70× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 32.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 33.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 14.4× (z +9.0) | — |
| [[H4 (line)]] | wt | 52.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 36.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.77× (z +11.6) | — |
| [[J82 (line)]] | alt | 61.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[RKO (line)]] | wt | 88.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 101 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 91.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 93.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 71.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A498 (line)]] | wt | 57.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[Hs 766T (line)]] | wt | 46.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 61.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 87.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 60.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2030 (line)]] | alt | 83.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +8.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2347 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.4) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[Panc 03.27 (line)]] | alt | 40.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +9.0) | — |
| [[A-427 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 134 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX18]] | +0.70 | +0.75 / +0.60 | both halves | 7e-06 | STRING 992 |
| [[UTP14A]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 | STRING 890 |
| [[ESF1]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 | STRING 932 |
| [[MDM4]] | +0.64 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[RSL1D1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 | STRING 996 |
| [[EIF3M]] | +0.63 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[SDAD1]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 | STRING 967 |
| [[PDCD11]] | +0.60 | +0.56 / +0.66 | both halves | 1e-05 | STRING 976 |
| [[NIFK]] | +0.60 | +0.73 / +0.49 | both halves | 1e-05 | STRING 999 |
| [[PAK1IP1]] | +0.59 | +0.69 / +0.50 | both halves | 1e-05 | STRING 973 |
| [[NOL8]] | +0.59 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[RAD50]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGA]] | -0.51 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[PPM1A]] | -0.50 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MYL6]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CMTM6]] | -0.49 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[ITM2B]] | -0.49 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[RNF38]] | -0.48 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[CALM3]] | -0.48 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[TSPAN17]] | -0.48 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[ITM2C]] | -0.48 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[SDHA]] | -0.48 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[ATG9A]] | -0.48 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RPF2's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.537). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.7, -41.5); signed map (0.6, -44.7). **Vector** length 86.3, 27.5% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +12.7 |
|  | [[EX229 (drug)]] 5 µM |  | +5.8 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.7 | +9.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[EX229 (drug)]] 0.5 µM |  | +3.5 | +4.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -3.9 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.8 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +0.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -2.4 | +6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosome production factor 2 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:110,982,015-111,028,263 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21087, bA397G5.4; previously BXDC1 |
| Gene groups (HGNC) | Brix domain containing; Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7B2](https://www.uniprot.org/uniprotkb/Q9H7B2) (Ribosome production factor 2 homolog):

> Involved in ribosomal large subunit assembly. May regulate the localization of the 5S RNP/5S ribonucleoprotein particle to the nucleolus.

**Summary**, from NCBI Gene [84154](https://www.ncbi.nlm.nih.gov/gene/84154):

> Enables 5S rRNA binding activity. Involved in protein localization to nucleolus; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20870) · Entrez [84154](https://www.ncbi.nlm.nih.gov/gene/84154) · UniProt [Q9H7B2](https://www.uniprot.org/uniprotkb/Q9H7B2) · Ensembl [ENSG00000197498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197498)

## Data

Gene col 12408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12408); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12408]; `tensor/DDL_lfc|DDL_z.npy` [12408]; `embed/gene_vectors.npy` [12408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12408 or target_col == 12408). Every well: [[RPF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
