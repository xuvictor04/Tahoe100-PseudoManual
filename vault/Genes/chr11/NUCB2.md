---
symbol: "NUCB2"
type: "gene"
col: 938
ensembl_id: "ENSG00000070081"
name: "nucleobindin 2"
location: "11p15.1"
module: 42
arm: "+"
pooled_cpm: 131.45
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# NUCB2

*nucleobindin 2* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.91× (z +11.3, q 3e-27, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +4.3, q 0.003, up in 28 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.89×, NCI-H23 5.91×, HOP62 4.09×, HEC-1-A 3.84×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SK-MEL-2 5.54×, A-427 4.34×, PANC-1 3.92×, AsPC-1 5.92×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.35×, NCI-H2347 1.85×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.432× (z -13.5, q 5e-39, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90B1]] (+0.74, fdr 7e-06), [[DNAJC3]] (+0.74, fdr 7e-06), [[KDELR1]] (+0.74, fdr 7e-06); moves opposite to [[NIP7]] (-0.74, fdr 7e-06), [[TRMT61A]] (-0.64, fdr 7e-06), [[GPATCH4]] (-0.64, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.89×, NCI-H23 5.91×, HOP62 4.09×, HEC-1-A 3.84×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SK-MEL-2 5.54×, A-427 4.34×, PANC-1 3.92×, AsPC-1 5.92×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.35×, NCI-H2347 1.85×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +11.3 | 3e-27 | 48/49 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +11.3 | 3e-27 | 42/44 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +7.1 | 2e-10 | 40/45 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.003 | 28/49 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | 1.32× | +3.2 | 0.16 | 31/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 938.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.432×** | -13.5 | 5e-39 | 45/48 (A498, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.405×** | -10.3 | 2e-22 | 43/48 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.503×** | -7.5 | 9e-12 | 42/48 (SW 900, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.560×** | -6.1 | 1e-07 | 39/48 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.633×** | -5.2 | 2e-05 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -5.2 | 2e-05 | 35/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.676×** | -4.5 | 6e-04 | 34/48 (HT-29, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.701×** | -4.1 | 0.003 | 28/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.702×** | -4.0 | 0.003 | 38/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.734×** | -3.5 | 0.024 | 27/48 (HCT15, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.734×** | -3.3 | 0.047 | 28/48 (H4, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.749×** | -3.3 | 0.047 | 26/48 (KATO III, SW 1088, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.738×** | -3.2 | 0.051 | 28/47 (Panc 03.27, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 148 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -17.4) |
| [[HOP62 (line)]] | alt | 139 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 201 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 101 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.2) |
| [[PANC-1 (line)]] | alt | 124 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.6) |
| [[A549 (line)]] | wt | 82.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 59.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.7) |
| [[H4 (line)]] | wt | 238 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -18.1) |
| [[HEC-1-A (line)]] | alt | 88.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -11.1) |
| [[KATO III (line)]] | alt | 129 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 123 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.6) |
| [[A-172 (line)]] | wt | 231 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 110 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +14.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 105 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -9.8) |
| [[HT-29 (line)]] | alt | 133 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 109 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 100 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -12.6) |
| [[SHP-77 (line)]] | alt | 94.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 105 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -11.1) |
| [[SNU-423 (line)]] | alt | 144 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -8.7) |
| [[A498 (line)]] | wt | 292 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -20.5) |
| [[AsPC-1 (line)]] | alt | 36.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 83.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 205 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.6) |
| [[HS-578T (line)]] | alt | 241 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -14.1) |
| [[J82 (line)]] | alt | 183 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -10.0) |
| [[LS 180 (line)]] | wt | 172 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 51.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 168 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 84.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 164 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.9) |
| [[SNU-1 (line)]] | wt | 120 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.9) |
| [[SW 1088 (line)]] | alt | 203 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -10.2) |
| [[SW1417 (line)]] | alt | 79.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 69.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 164 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 160 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 79.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +12.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 63.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.7) | — |
| [[SW480 (line)]] | alt | 140 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.8) |
| [[AN3 CA (line)]] | alt | 144 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90B1]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[DNAJC3]] | +0.74 | +0.76 / +0.72 | both halves | 7e-06 | STRING 411 |
| [[KDELR1]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[LMAN1]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[SEC63]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[TTC3]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[CALR]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[SUCO]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.70 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[COPA]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.69 | +0.73 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIP7]] | -0.74 | -0.70 / -0.71 | both halves | 7e-06 |  |
| [[TRMT61A]] | -0.64 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.64 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[FAM83H]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[COA7]] | -0.62 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[TMEM185B]] | -0.61 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[TRMT5]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[UTP20]] | -0.59 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[NOL11]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[NDUFAF4]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[NOP56]] | -0.57 | -0.59 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, -31.5); signed map (-53.6, 9.2). **Vector** length 124, 49.5% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.65 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.60 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.59 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.5 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.9 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -10.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.2 | -0.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | nucleobindin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:17,208,153-17,349,980 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NEFA |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P80303](https://www.uniprot.org/uniprotkb/P80303) (Nucleobindin-2):

> Calcium-binding protein which may have a role in calcium homeostasis (By similarity). Acts as a non-receptor guanine nucleotide exchange factor which binds to and activates guanine nucleotide-binding protein (G protein) alpha subunit GNAI3 (By similarity).; [Nesfatin-1]: Anorexigenic peptide, seems to play an important role in hypothalamic pathways regulating food intake and energy homeostasis, acting in a leptin-independent manner. May also exert hypertensive roles and modulate blood pressure …

**Summary**, from NCBI Gene [4925](https://www.ncbi.nlm.nih.gov/gene/4925):

> This gene encodes a protein with a suggested role in calcium level maintenance, eating regulation in the hypothalamus, and release of tumor necrosis factor from vascular endothelial cells. This protein binds calcium and has EF-folding domains. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:8044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8044) · Entrez [4925](https://www.ncbi.nlm.nih.gov/gene/4925) · UniProt [P80303](https://www.uniprot.org/uniprotkb/P80303) · Ensembl [ENSG00000070081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070081)

## Data

Gene col 938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 938); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 938]; `tensor/DDL_lfc|DDL_z.npy` [938]; `embed/gene_vectors.npy` [938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 938 or target_col == 938). Every well: [[NUCB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUCB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
