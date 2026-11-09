---
symbol: "BAHD1"
type: "gene"
col: 6390
ensembl_id: "ENSG00000140320"
name: "bromo adjacent homology domain containing 1"
location: "15q15.1"
module: 3
arm: "+"
pooled_cpm: 22.35
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# BAHD1

*bromo adjacent homology domain containing 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +17.8, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.453× (z -13.4, q 3e-38, down in 33 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.811× (z -3.6, q 0.038, down in 14 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL8A]] (+0.78, fdr 7e-06), [[IL17RA]] (+0.76, fdr 7e-06), [[MARK4]] (+0.69, fdr 1e-05); moves opposite to [[HNRNPK]] (-0.67, fdr 2e-05), [[CPNE1]] (-0.66, fdr 1e-05), [[MBTPS2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAT1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +17.8 | 0e+00 | 42/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +12.7 | 2e-34 | 40/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.03×** | +12.0 | 5e-31 | 42/47 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +11.6 | 9e-29 | 42/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +11.3 | 1e-27 | 38/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +10.0 | 1e-21 | 37/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +9.7 | 2e-20 | 41/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +8.2 | 2e-14 | 34/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +6.6 | 2e-09 | 33/48 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +5.8 | 4e-07 | 26/48 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +5.3 | 6e-06 | 27/47 (HOP62, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.1 | 1e-05 | 24/45 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.005 | 14/46 (LS 180, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.007 | 18/48 (SK-MEL-2, HepG2/C3A, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.7 | 0.008 | 16/41 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.012 | 9/48 (NCI-H1792, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.017 | 12/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.029 | 7/45 (H4, SW1417, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6390.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.453×** | -13.4 | 3e-38 | 33/42 (NCI-H2347, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -12.6 | 4e-34 | 27/33 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.622×** | -7.4 | 2e-11 | 25/38 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -4.9 | 1e-04 | 1/48 (SW 1271) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.811×** | -3.6 | 0.038 | 14/48 (A-172, HCT15, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.811×** | -3.5 | 0.038 | 13/48 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.817×** | -3.4 | 0.051 | 8/48 (NCI-H2347, C32, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.815×** | -3.2 | 0.095 | 14/46 (SW 900, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 32.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +10.4) | — |
| [[SW480 (line)]] | alt | 25.7 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 22.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 17.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.33× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 38.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -15.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 18.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -11.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0939× (z -12.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 31.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -14.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 19.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.70× (z +8.9) | — |
| [[NCI-H661 (line)]] | alt | 38.4 | 0 | 2 | — | [[Erdafitinib (drug)]] 0.05 µM 0.0631× (z -9.4) |
| [[PANC-1 (line)]] | alt | 23.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +10.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.4) | — |
| [[A549 (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0822× (z -13.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0727× (z -14.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +12.2) | — |
| [[RKO (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL8A]] | +0.78 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[IL17RA]] | +0.76 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[MARK4]] | +0.69 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[MACO1]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RAB11FIP5]] | +0.68 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[UBE2D2]] | +0.67 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.67 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[CARD19]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[MIR4458HG]] | +0.66 | +0.37 / +0.72 | both halves | 8e-05 |  |
| [[TRIM62]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[ZFAND2A]] | +0.66 | +0.57 / +0.60 | both halves | 9e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.67 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[CPNE1]] | -0.66 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[MBTPS2]] | -0.66 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[CBX5]] | -0.66 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.63 | -0.41 / -0.71 | both halves | 4e-05 |  |
| [[CHRAC1]] | -0.63 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[YWHAE]] | -0.63 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[ERLIN2]] | -0.63 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[NEK9]] | -0.62 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[PTGR2]] | -0.62 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[BCLAF1]] | -0.62 | -0.39 / -0.67 | both halves | 5e-05 |  |
| [[ZC3H11A]] | -0.62 | -0.47 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAT1]] | C | FAT1 activity lowers BAHD1's level | lines that do not express FAT1 (3) vs lines expressing it (47) | 1.72× higher at baseline in the lines without FAT1 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARHGAP15, CDKN1A, CYP2E1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.6, -4.3); signed map (-25.9, 7.5). **Vector** length 102, 24.1% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.9 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +17.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +9.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.8 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.3 | +3.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.8 | -13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.9 | -7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -3.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | bromo adjacent homology domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,439,721-40,468,236 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0945 |
| Gene groups (HGNC) | MIER complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBE0](https://www.uniprot.org/uniprotkb/Q8TBE0) (Bromo adjacent homology domain-containing 1 protein):

> Heterochromatin protein that acts as a transcription repressor and has the ability to promote the formation of large heterochromatic domains. May act by recruiting heterochromatin proteins such as CBX5 (HP1 alpha), HDAC5 and MBD1. Represses IGF2 expression by binding to its CpG-rich P3 promoter and recruiting heterochromatin proteins. At specific stages of Listeria infection, in complex with TRIM28, corepresses interferon-stimulated genes, including IFNL1, IFNL2 and IFNL3.

**Summary**, from NCBI Gene [22893](https://www.ncbi.nlm.nih.gov/gene/22893):

> Enables chromatin binding activity. Involved in heterochromatin formation and negative regulation of DNA-templated transcription. Located in nucleoplasm. Part of chromatin silencing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29153) · Entrez [22893](https://www.ncbi.nlm.nih.gov/gene/22893) · UniProt [Q8TBE0](https://www.uniprot.org/uniprotkb/Q8TBE0) · Ensembl [ENSG00000140320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140320)

## Data

Gene col 6390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6390); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6390]; `tensor/DDL_lfc|DDL_z.npy` [6390]; `embed/gene_vectors.npy` [6390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6390 or target_col == 6390). Every well: [[BAHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
