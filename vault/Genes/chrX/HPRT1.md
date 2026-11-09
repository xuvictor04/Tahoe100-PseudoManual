---
symbol: "HPRT1"
type: "gene"
col: 9173
ensembl_id: "ENSG00000165704"
name: "hypoxanthine phosphoribosyltransferase 1"
location: "Xq26.2-q26.3"
module: 16
arm: "-"
pooled_cpm: 70.6
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# HPRT1

*hypoxanthine phosphoribosyltransferase 1* — Xq26.2-q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +11.5, q 6e-28, up in 34 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.456×, C32 0.443×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.325×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OLA1]] (+0.59, fdr 7e-06), [[PAQR3]] (+0.59, fdr 1e-05), [[BTAF1]] (+0.56, fdr 3e-05); moves opposite to [[SPOP]] (-0.62, fdr 7e-06), [[TRIM4]] (-0.61, fdr 7e-06), [[MRFAP1L1]] (-0.60, fdr 7e-06).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +11.5 | 6e-28 | 34/47 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.06×** | +11.1 | 3e-26 | 37/48 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +10.2 | 3e-22 | 43/49 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +9.3 | 2e-18 | 42/47 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.75×** | +8.3 | 1e-14 | 33/44 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.65×** | +7.7 | 1e-12 | 37/46 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.65×** | +7.7 | 1e-12 | 38/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +7.3 | 2e-11 | 35/47 (SW480, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +7.1 | 9e-11 | 41/47 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.58×** | +6.5 | 4e-09 | 29/45 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 2e-06 | 34/47 (KATO III, A498, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.2 | 0.001 | 18/36 (SNU-423, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.30×** | +4.0 | 0.003 | 23/47 (A498, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.27×** | +3.7 | 0.010 | 24/47 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.25×** | +3.5 | 0.019 | 22/47 (H4, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.019 | 20/48 (A498, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.037 | 19/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.044 | 20/47 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.044 | 18/47 (MIA PaCa-2, SW 900, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.047 | 20/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.084 | 16/47 (PANC-1, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9173.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.456×, C32 0.443×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.325×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 0.643× | -3.6 | 0.20 | 24/49 (HEC-1-A, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 106 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +12.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.50× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 66.0 | 6 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +12.9) | — |
| [[A498 (line)]] | wt | 51.4 | 4 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 115 | 5 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 69.5 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +12.4) | — |
| [[SW 900 (line)]] | alt | 53.3 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +9.9) | — |
| [[KATO III (line)]] | alt | 38.1 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.21× (z +9.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.62× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 73.4 | 3 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 87.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +11.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.0) | — |
| [[A-427 (line)]] | wt | 89.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 40.2 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +9.2) | — |
| [[LoVo (line)]] | wt | 33.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LS 180 (line)]] | wt | 45.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 118 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 89.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.5) | — |
| [[RKO (line)]] | wt | 103 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 141 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.1) | — |
| [[A-172 (line)]] | wt | 30.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 121 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +11.7) | — |
| [[C32 (line)]] | wt | 65.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 44.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.5) | — |
| [[H4 (line)]] | wt | 40.4 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 59.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HEC-1-A (line)]] | alt | 82.2 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 31.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 51.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +13.1) | — |
| [[SW48 (line)]] | wt | 101 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +8.5) | — |
| [[A549 (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 117 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLA1]] | +0.59 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PAQR3]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[BTAF1]] | +0.56 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[NAE1]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ME2]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[VDAC1]] | +0.56 | +0.58 / +0.46 | both halves | 2e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[DGKE]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SRPK1]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[SERGEF]] | +0.55 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[POLR3G]] | +0.53 | +0.59 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[PLEKHA8]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SEC61A2]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOP]] | -0.62 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[TRIM4]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | -0.60 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[ZNF140]] | -0.59 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[KAT5]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[THRAP3]] | -0.57 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[RNF40]] | -0.56 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PRPF6]] | -0.55 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ZBTB48]] | -0.54 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[RBSN]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PBX2]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CWC22]] | -0.53 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises HPRT1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.63× lower at baseline in the lines without ADCY3 | 0.036 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[POLR3G]] | C | POLR3G activity raises HPRT1's level | lines that do not express POLR3G (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without POLR3G | 0.074 | ⚠ few lines (3 vs 47); across organs; also absent: HMGA1, PALS2, SLC35F2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.407). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.4, -0.6); signed map (-31.8, -18.4). **Vector** length 102, 30.1% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.5 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +4.4 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +7.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.2 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.5 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | hypoxanthine phosphoribosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.2-q26.3 — chrX:134,460,165-134,520,513 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HGPRT; previously HPRT |
| Gene groups (HGNC) | Phosphoribosyltransferases |
| Hallmark sets | DNA_REPAIR, XENOBIOTIC_METABOLISM, ESTROGEN_RESPONSE_LATE, MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: Nucleotide salvage defects; Diseases of nucleotide metabolism; Purine salvage |
| Matched by | ensembl_id |

**Function**, from UniProt [P00492](https://www.uniprot.org/uniprotkb/P00492) (Hypoxanthine-guanine phosphoribosyltransferase):

> Converts guanine to guanosine monophosphate, and hypoxanthine to inosine monophosphate. Transfers the 5-phosphoribosyl group from 5-phosphoribosylpyrophosphate onto the purine. Plays a central role in the generation of purine nucleotides through the purine salvage pathway.

**Summary**, from NCBI Gene [3251](https://www.ncbi.nlm.nih.gov/gene/3251):

> The protein encoded by this gene is a transferase, which catalyzes conversion of hypoxanthine to inosine monophosphate and guanine to guanosine monophosphate via transfer of the 5-phosphoribosyl group from 5-phosphoribosyl 1-pyrophosphate. This enzyme plays a central role in the generation of purine nucleotides through the purine salvage pathway. Mutations in this gene result in Lesch-Nyhan syndrome or gout.[provided by RefSeq, Jun 2009]

**Accessions** — [HGNC:5157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5157) · Entrez [3251](https://www.ncbi.nlm.nih.gov/gene/3251) · UniProt [P00492](https://www.uniprot.org/uniprotkb/P00492) · Ensembl [ENSG00000165704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165704)

## Data

Gene col 9173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9173); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9173]; `tensor/DDL_lfc|DDL_z.npy` [9173]; `embed/gene_vectors.npy` [9173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9173 or target_col == 9173). Every well: [[HPRT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPRT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
