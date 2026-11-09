---
symbol: "ECI1"
type: "gene"
col: 9564
ensembl_id: "ENSG00000167969"
name: "enoyl-CoA delta isomerase 1"
location: "16p13.3"
module: 28
arm: "-"
pooled_cpm: 31.24
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ECI1

*enoyl-CoA delta isomerase 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 10.9× (z +28.1, q 0e+00, up in 37 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.8, q 1e-06, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.713× (z -4.1, q 0.022, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.232×, A-427 0.489×, PANC-1 0.513×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.118×; ⚠ toxic; cell-cycle shift, explains ~63% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.271×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H3]] (+0.67, fdr 1e-05), [[STAG3L4-1]] (+0.57, fdr 3e-05), [[NBL1]] (+0.54, fdr 4e-05); moves opposite to [[TRMT1L]] (-0.58, fdr 2e-05), [[MGAT2]] (-0.52, fdr 3e-04), [[CSTF2T]] (-0.50, fdr 3e-04).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.9×** | +28.1 | 0e+00 | 37/37 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.98×** | +26.9 | 0e+00 | 43/43 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.61×** | +19.5 | 0e+00 | 40/42 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.7 | 3e-09 | 35/46 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.8 | 1e-06 | 24/47 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.6 | 3e-04 | 18/32 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.6 | 0.029 | 20/47 (A498, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.33×** | +3.5 | 0.029 | 21/46 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.062 | 17/47 (SK-MEL-2, NCI-H23, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.082 | 16/47 (NCI-H2030, AsPC-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.19× | +3.1 | 0.12 | 12/48 (KATO III, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9564.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.232×, A-427 0.489×, PANC-1 0.513×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.118×; ⚠ toxic; cell-cycle shift, explains ~63% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.271×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -4.1 | 0.022 | 23/47 (A-427, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.757× | -3.4 | 0.20 | 14/48 (A-172, LS 180, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 57.1 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 40.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 22.4× (z +21.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 54.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.6× (z +23.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 32.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.3× (z +20.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 46.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.93× (z +19.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 42.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.6× (z +11.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 44.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.03× (z +11.5) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -14.2) ⚠ toxic; cell-cycle shift, explains ~63% of this change |
| [[CFPAC-1 (line)]] | alt | 21.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 23.1× (z +17.5) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 22.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 21.1× (z +14.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 37.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.14× (z +13.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 14.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 31.0× (z +21.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 27.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 20.2× (z +17.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 19.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +14.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 38.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +11.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.8× (z +12.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 35.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 16.4× (z +22.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 53.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.0× (z +19.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 36.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.2× (z +23.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +15.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 14.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.3× (z +15.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 27.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.14× (z +16.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.39× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 24.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 15.2× (z +19.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 50.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.54× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 17.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.4× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 34.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.0× (z +19.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 18.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.2× (z +14.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 23.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.3× (z +18.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 39.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.7× (z +16.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 29.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.68× (z +20.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.84× (z +15.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.06× (z +10.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 15.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 21.6× (z +15.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 33.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 46.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.42× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +12.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.99× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 47.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.10× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.11× (z +11.2) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H3]] | +0.67 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[STAG3L4-1]] | +0.57 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[NBL1]] | +0.54 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[DANCR]] | +0.53 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[TCEA2]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[RBM14-RBM4]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[NUP42]] | +0.51 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[FUT10]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[SARM1]] | +0.49 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[MTHFD2]] | +0.49 | +0.36 / +0.48 | both halves | 9e-05 |  |
| [[YARS1]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[SMG1P1]] | +0.49 | +0.33 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT1L]] | -0.58 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[MGAT2]] | -0.52 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[CSTF2T]] | -0.50 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[BBS10]] | -0.48 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[TBCC]] | -0.48 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[KLHL9]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[CPT2]] | -0.47 | -0.39 / -0.38 | both halves | 7e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 602 |
| [[MRPL35]] | -0.45 | -0.35 / -0.49 | both halves | 1e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[ABT1]] | -0.45 | -0.29 / -0.46 | both halves | 3e-04 |  |
| [[RAB8A]] | -0.45 | -0.32 / -0.55 | both halves | 1e-04 |  |
| [[ELOF1]] | -0.45 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[H3-3B]] | -0.45 | -0.30 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.273). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.9, 0.7); signed map (2.3, 7.3). **Vector** length 61.0, 11.8% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +19.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +26.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +28.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.9 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.4 | +2.5 |

## What is on record

|  |  |
|---|---|
| Name | enoyl-CoA delta isomerase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,239,402-2,252,300 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DCI |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: mitochondrial fatty acid beta-oxidation of unsaturated fatty acids; Mitochondrial Fatty Acid Beta-Oxidation; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P42126](https://www.uniprot.org/uniprotkb/P42126) (Enoyl-CoA delta isomerase 1, mitochondrial):

> Auxiliary enzyme in the beta-oxidation of mono- and polyunsaturated fatty acids. Together with the 2,4-dienoyl-CoA reductase (DECR) and the Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase (ECH1), they allow the reentrance of the enoyl-CoA into the beta-oxidation cycle. Able to isomerize both 3-cis (3Z) and 3-trans (3E) double bonds into the 2-trans (2E) form in a range of fatty enoyl-CoA species, with a preference for (3Z)-enoyl-CoAs over (3E)-enoyl-CoAs. The catalytic efficiency of this enzyme is …

**Summary**, from NCBI Gene [1632](https://www.ncbi.nlm.nih.gov/gene/1632):

> This gene encodes a member of the hydratase/isomerase superfamily. The protein encoded is a key mitochondrial enzyme involved in beta-oxidation of unsaturated fatty acids. It catalyzes the transformation of 3-cis and 3-trans-enoyl-CoA esters arising during the stepwise degradation of cis-, mono-, and polyunsaturated fatty acids to the 2-trans-enoyl-CoA intermediates. Alternatively spliced transcript variants have been described. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:2703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2703) · Entrez [1632](https://www.ncbi.nlm.nih.gov/gene/1632) · UniProt [P42126](https://www.uniprot.org/uniprotkb/P42126) · Ensembl [ENSG00000167969](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167969)

## Data

Gene col 9564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9564); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9564]; `tensor/DDL_lfc|DDL_z.npy` [9564]; `embed/gene_vectors.npy` [9564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9564 or target_col == 9564). Every well: [[ECI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
