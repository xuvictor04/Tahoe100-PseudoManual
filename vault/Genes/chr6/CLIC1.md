---
symbol: "CLIC1"
type: "gene"
col: 13130
ensembl_id: "ENSG00000213719"
name: "CLIC family member 1"
location: "6p21.33"
module: 78
arm: "+"
pooled_cpm: 105.96
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# CLIC1

*CLIC family member 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.77× (z +12.0, q 1e-30, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.34× (z +3.4, q 0.056, up in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (C-33 A 10.6×, KATO III 4.02×, J82 3.39×, LoVo 3.76×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 3.98×, KATO III 4.69×, LoVo 3.55×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.29×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.657× (z -7.0, q 1e-09, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGDIA]] (+0.68, fdr 7e-06), [[PLEC]] (+0.60, fdr 1e-05), [[CSRP1]] (+0.59, fdr 3e-05); moves opposite to [[SULT1A1]] (-0.56, fdr 2e-05), [[PAXBP1]] (-0.56, fdr 3e-05), [[SLC2A11]] (-0.53, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLEC]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13130.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (C-33 A 10.6×, KATO III 4.02×, J82 3.39×, LoVo 3.76×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 3.98×, KATO III 4.69×, LoVo 3.55×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.29×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +12.0 | 1e-30 | 49/49 (C-33 A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +11.1 | 5e-26 | 41/43 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +6.3 | 4e-08 | 36/45 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.56×** | +5.3 | 2e-05 | 37/48 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.9 | 1e-04 | 0/50 | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.42×** | +4.1 | 0.003 | 36/47 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +3.7 | 0.019 | 31/48 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.056 | 26/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.16 | 22/47 (NCI-H460, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -7.0 | 1e-09 | 42/49 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.574×** | -6.6 | 1e-08 | 41/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.585×** | -6.3 | 4e-08 | 42/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.732×** | -5.2 | 2e-05 | 37/48 (RPMI-7951, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.646×** | -5.2 | 3e-05 | 37/48 (COLO 205, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -4.3 | 0.002 | 31/48 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.792×** | -3.9 | 0.008 | 25/48 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.713×** | -3.7 | 0.017 | 34/50 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.725×** | -3.6 | 0.019 | 29/48 (A-172, RKO, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.739×** | -3.6 | 0.019 | 31/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.577×** | -3.4 | 0.034 | 26/45 (H4, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.750×** | -3.3 | 0.048 | 28/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.592×** | -3.2 | 0.051 | 29/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.774×** | -3.0 | 0.096 | 25/49 (SW 900, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 86.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.9) | — |
| [[KATO III (line)]] | alt | 133 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -11.1) |
| [[PANC-1 (line)]] | alt | 90.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 148 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.450× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 156 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 227 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -11.5) |
| [[Hs 766T (line)]] | wt | 95.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.5) |
| [[J82 (line)]] | alt | 147 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +13.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 90.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +11.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 99.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.4) |
| [[SW480 (line)]] | alt | 97.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.2) |
| [[A498 (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +10.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 89.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 89.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 99.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 135 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 103 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 52.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +11.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 79.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.0) |
| [[C-33 A (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.6× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 108 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 64.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 62.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 150 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.0) |
| [[SHP-77 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.45× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.6) |
| [[SW 900 (line)]] | alt | 83.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 166 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 112 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGDIA]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PLEC]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CSRP1]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PPP1CA]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[F2RL1]] | +0.58 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[RP2]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CAPNS1]] | +0.56 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[GALE]] | +0.56 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[TAGLN2]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ARF6]] | +0.55 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[CDC42EP2]] | +0.55 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[YWHAZ]] | +0.55 | +0.59 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SULT1A1]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PAXBP1]] | -0.56 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[SLC2A11]] | -0.53 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[SNHG25]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[NAP1L1]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ATP6V0D1-DT]] | -0.51 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[HINT1]] | -0.51 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TIAL1]] | -0.50 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[NDUFAF7]] | -0.50 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[PNISR]] | -0.50 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[GLMN]] | -0.50 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[SLC18B1]] | -0.49 | -0.39 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEC]] | C | PLEC activity raises CLIC1's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without PLEC | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.6, -4.4); signed map (-7.4, 32.5). **Vector** length 85.3, 28.4% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.5 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.3 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +11.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | -0.8 |
| fall | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | -2.7 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | -2.6 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.3 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | CLIC family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,730,581-31,739,763 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NCC27, p64CLCP, G6, CLCNL1 |
| Gene groups (HGNC) | CLIC family |
| Matched by | ensembl_id |

**Function**, from UniProt [O00299](https://www.uniprot.org/uniprotkb/O00299) (Chloride intracellular channel protein 1):

> In the soluble state, catalyzes glutaredoxin-like thiol disulfide exchange reactions with reduced glutathione as electron donor. Reduces selenite and dehydroascorbate and may act as an antioxidant during oxidative stress response. Can insert into membranes and form voltage-dependent multi-ion conductive channels. Membrane insertion seems to be redox-regulated and may occur only under oxidizing conditions. Involved in regulation of the cell cycle.

**Summary**, from NCBI Gene [1192](https://www.ncbi.nlm.nih.gov/gene/1192):

> Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. Chloride intracellular channel 1 is a member of the p64 family; the protein localizes principally to the cell nucleus and exhibits both nuclear and plasma membrane chloride ion channel activity. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2062) · Entrez [1192](https://www.ncbi.nlm.nih.gov/gene/1192) · UniProt [O00299](https://www.uniprot.org/uniprotkb/O00299) · Ensembl [ENSG00000213719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213719)

## Data

Gene col 13130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13130); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13130]; `tensor/DDL_lfc|DDL_z.npy` [13130]; `embed/gene_vectors.npy` [13130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13130 or target_col == 13130). Every well: [[CLIC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLIC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
