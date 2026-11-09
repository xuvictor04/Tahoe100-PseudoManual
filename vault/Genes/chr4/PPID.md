---
symbol: "PPID"
type: "gene"
col: 10122
ensembl_id: "ENSG00000171497"
name: "peptidylprolyl isomerase D"
location: "4q32.1"
module: 64
arm: "+"
pooled_cpm: 45.15
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PPID

*peptidylprolyl isomerase D* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.44× (z +28.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.774× (z -4.1, q 0.022, down in 22 of 48 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.631× (z -3.9, q 0.032, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.247×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.301×; ⚠ cell-cycle shift, explains ~56% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYW3]] (+0.74, fdr 7e-06), [[UBXN4]] (+0.72, fdr 1e-05), [[MTIF2]] (+0.71, fdr 7e-06); moves opposite to [[DHPS]] (-0.63, fdr 1e-05), [[SMARCD2]] (-0.61, fdr 2e-05), [[KMT5C]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNMB3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.44×** | +28.1 | 0e+00 | 46/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.09×** | +18.1 | 0e+00 | 48/48 (HEC-1-A, C32, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.97×** | +16.8 | 0e+00 | 46/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +13.8 | 6e-41 | 44/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +10.4 | 3e-23 | 43/48 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.92×** | +10.1 | 4e-22 | 35/42 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +10.1 | 4e-22 | 44/48 (A498, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.87×** | +10.1 | 6e-22 | 38/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.83×** | +9.2 | 2e-18 | 41/48 (NCI-H2347, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +8.3 | 5e-15 | 38/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +6.5 | 4e-09 | 36/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.9 | 2e-07 | 35/43 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.88×** | +5.3 | 5e-06 | 31/47 (LoVo, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.9 | 3e-05 | 27/47 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[EX229 (drug)]] 5 µM |  | **1.78×** | +4.9 | 4e-05 | 31/48 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.8 | 5e-05 | 24/48 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.9 | 0.003 | 19/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.003 | 19/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.003 | 21/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.009 | 17/48 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.009 | 20/48 (HEC-1-A, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10122.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.247×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.301×; ⚠ cell-cycle shift, explains ~56% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.774×** | -4.1 | 0.022 | 22/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.631×** | -3.9 | 0.032 | 19/48 (C-33 A, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.849× | -3.7 | 0.043 | 18/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -3.6 | 0.053 | 3/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.816× | -3.2 | 0.13 | 23/48 (COLO 205, PANC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.820× | -3.0 | 0.22 | 15/47 (MIA PaCa-2, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.3 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +19.9) | — |
| [[A-172 (line)]] | wt | 45.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +23.2) | — |
| [[NCI-H2347 (line)]] | alt | 47.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +18.4) | — |
| [[NCI-H460 (line)]] | wt | 37.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +21.6) | — |
| [[PANC-1 (line)]] | alt | 49.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +28.5) | — |
| [[A549 (line)]] | wt | 37.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +17.9) | — |
| [[HEC-1-A (line)]] | alt | 47.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +18.8) | — |
| [[HOP62 (line)]] | alt | 33.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +22.7) | — |
| [[LoVo (line)]] | wt | 51.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +18.5) | — |
| [[NCI-H1573 (line)]] | alt | 50.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +25.5) | — |
| [[NCI-H1792 (line)]] | alt | 34.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +22.2) | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +21.5) | — |
| [[HS-578T (line)]] | alt | 43.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +17.0) | — |
| [[RPMI-7951 (line)]] | alt | 45.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +14.2) | — |
| [[SNU-1 (line)]] | wt | 49.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 34.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +17.6) | — |
| [[SW48 (line)]] | wt | 78.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +15.5) | — |
| [[C32 (line)]] | wt | 37.8 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.83× (z +15.0) | — |
| [[hTERT-HPNE (line)]] | wt | 38.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +16.9) | — |
| [[KATO III (line)]] | alt | 41.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.12× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 53.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.74× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 37.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.1) | — |
| [[SK-MEL-2 (line)]] | alt | 63.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 26.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +14.5) | — |
| [[C-33 A (line)]] | alt | 66.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.47× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 29.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +13.4) | — |
| [[HT-29 (line)]] | alt | 33.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 35.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +13.5) | — |
| [[RKO (line)]] | wt | 74.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.78× (z +10.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -8.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SHP-77 (line)]] | alt | 35.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.63× (z +9.2) | — |
| [[SW480 (line)]] | alt | 69.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.61× (z +12.5) | — |
| [[BT-474 (line)]] | alt | 30.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.12× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[HCT15 (line)]] | alt | 49.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 44.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 39.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +13.8) | — |
| [[J82 (line)]] | alt | 47.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +15.0) | — |
| [[LOX-IMVI (line)]] | wt | 33.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.31× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 42.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 42.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.66× (z +9.1) | — |
| [[A-427 (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW3]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[UBXN4]] | +0.72 | +0.80 / +0.56 | both halves | 1e-05 |  |
| [[MTIF2]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[RNF6]] | +0.67 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[NUDT9]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.63 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.63 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[PSMD6]] | +0.63 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[HSPB8]] | +0.61 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[GLRX2]] | +0.61 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[BMS1]] | +0.60 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[RPF1]] | +0.60 | +0.67 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHPS]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.61 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[KMT5C]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SUMF2]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[CD81]] | -0.57 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[POLR2F]] | -0.56 | -0.62 / -0.33 | both halves | 1e-04 | pathway: ESR-mediated signaling |
| [[ATP6AP2]] | -0.55 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[PHPT1]] | -0.55 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[CA5BP1]] | -0.55 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[PRDX4]] | -0.55 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[FUCA1]] | -0.54 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[KIAA2013]] | -0.54 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB3]] | B | KCNMB3 activity lowers PPID's level | lines that do not express KCNMB3 (7) vs lines expressing it (43) | 1.41× higher at baseline in the lines without KCNMB3 | 0.034 | ⚠ within organs, on part of the lines; also absent: IQCD, MLF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-20.0, 8.9); signed map (8.0, -30.2). **Vector** length 92.8, 25.1% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +18.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +28.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +13.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.2 | +10.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +1.7 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.4 | +3.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.4 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:158,709,127-158,723,396 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CYP-40, CypD |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Cyclophilin peptidylprolyl isomerases |
| Reactome | 2 pathways, smallest: ESR-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08752](https://www.uniprot.org/uniprotkb/Q08752) (Peptidyl-prolyl cis-trans isomerase D):

> PPIase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding. Proposed to act as a co-chaperone in HSP90 complexes such as in unligated steroid receptors heterocomplexes. Different co-chaperones seem to compete for association with HSP90 thus establishing distinct HSP90-co-chaperone-receptor complexes with the potential to exert tissue-specific receptor activity control. May have a preference for estrogen receptor …

**Summary**, from NCBI Gene [5481](https://www.ncbi.nlm.nih.gov/gene/5481):

> The protein encoded by this gene is a member of the peptidyl-prolyl cis-trans isomerase (PPIase) family. PPIases catalyze the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and accelerate the folding of proteins. This protein has been shown to possess PPIase activity and, similar to other family members, can bind to the immunosuppressant cyclosporin A. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9257) · Entrez [5481](https://www.ncbi.nlm.nih.gov/gene/5481) · UniProt [Q08752](https://www.uniprot.org/uniprotkb/Q08752) · Ensembl [ENSG00000171497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171497)

## Data

Gene col 10122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10122); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10122]; `tensor/DDL_lfc|DDL_z.npy` [10122]; `embed/gene_vectors.npy` [10122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10122 or target_col == 10122). Every well: [[PPID — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPID.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
