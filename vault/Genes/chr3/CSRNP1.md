---
symbol: "CSRNP1"
type: "gene"
col: 6910
ensembl_id: "ENSG00000144655"
name: "cysteine and serine rich nuclear protein 1"
location: "3p22.2"
module: 109
arm: "+"
pooled_cpm: 24.64
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# CSRNP1

*cysteine and serine rich nuclear protein 1* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.91× (z +22.4, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.415× (z -8.5, q 1e-14, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUNB]] (+0.75, fdr 7e-06), [[IER2]] (+0.73, fdr 7e-06), [[IER3]] (+0.71, fdr 7e-06); moves opposite to [[SOS1]] (-0.60, fdr 1e-05), [[BMPR1A]] (-0.60, fdr 1e-05), [[RUFY2]] (-0.60, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RUNX1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SBNO2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.91×** | +22.4 | 0e+00 | 43/45 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **25.8×** | +17.0 | 0e+00 | 48/48 (HEC-1-A, NCI-H1792, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **3.13×** | +10.9 | 1e-25 | 40/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +9.6 | 1e-19 | 37/44 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **6.04×** | +9.4 | 8e-19 | 37/45 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.44×** | +8.9 | 5e-17 | 43/47 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.26×** | +8.1 | 6e-14 | 35/47 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.12×** | +7.5 | 6e-12 | 41/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +7.2 | 4e-11 | 34/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +6.2 | 3e-08 | 31/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +4.9 | 4e-05 | 26/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +3.9 | 0.004 | 17/37 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6910.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.415×** | -8.5 | 1e-14 | 37/46 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -7.9 | 5e-13 | 23/31 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -7.4 | 2e-11 | 33/45 (HT-29, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.510×** | -6.5 | 1e-08 | 35/46 (HT-29, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.585×** | -5.4 | 9e-06 | 34/47 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.587×** | -5.3 | 9e-06 | 25/40 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.735×** | -4.4 | 0.001 | 24/47 (KATO III, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.714×** | -4.0 | 0.004 | 22/46 (SW48, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.674×** | -4.0 | 0.005 | 23/46 (J82, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.686×** | -3.8 | 0.009 | 21/46 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.696×** | -3.6 | 0.015 | 19/45 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.502×** | -3.6 | 0.015 | 20/44 (RKO, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.686×** | -3.6 | 0.015 | 19/46 (C32, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.691×** | -3.6 | 0.015 | 20/46 (SW480, HepG2/C3A, …) | all doses, flat | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.028 | 22/47 (NCI-H23, COLO 205, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.731×** | -3.1 | 0.058 | 19/47 (SK-MEL-2, NCI-H23, …) | all doses, flat | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -3.1 | 0.058 | 18/47 (NCI-H2347, AN3 CA, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.715×** | -3.1 | 0.060 | 15/47 (C32, SW48, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.780×** | -3.0 | 0.078 | 17/47 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.3 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +16.6) | — |
| [[A-172 (line)]] | wt | 26.0 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -9.8) |
| [[HOP62 (line)]] | alt | 38.0 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +16.9) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.237× (z -9.0) |
| [[HS-578T (line)]] | alt | 21.5 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 36.4 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.176× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 56.8 | 3 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.9× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 40.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +18.1) | — |
| [[HEC-1-A (line)]] | alt | 30.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.0721× (z -16.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 34.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -17.4) |
| [[SW480 (line)]] | alt | 17.4 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 30.4× (z +11.2) | — |
| [[A498 (line)]] | wt | 18.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +14.2) | — |
| [[C32 (line)]] | wt | 15.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 26.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +15.3) | — |
| [[HepG2_C3A (line)]] | wt | 33.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +13.4) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.178× (z -8.6) |
| [[LoVo (line)]] | wt | 28.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +14.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.219× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +11.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 42.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +17.9) | — |
| [[NCI-H2347 (line)]] | alt | 36.2 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 23.6× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0686× (z -16.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 33.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0789× (z -12.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 25.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0722× (z -16.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +12.3) | — |
| [[J82 (line)]] | alt | 15.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +15.4) | — |
| [[KATO III (line)]] | alt | 16.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +12.5) | [[Selinexor (drug)]] 5 µM 0.328× (z -8.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 31.0 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 26.5× (z +9.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 16.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 36.9× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +15.5) | — |
| [[SW 1271 (line)]] | alt | 71.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0671× (z -9.5) |
| [[SW 900 (line)]] | alt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +11.6) | — |
| [[A-427 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | +0.75 | +0.77 / +0.74 | both halves | 7e-06 | STRING 660 |
| [[IER2]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 | STRING 567 |
| [[IER3]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[NFKBIE]] | +0.69 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[TRIB1]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 | STRING 465 |
| [[SOCS3]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 | STRING 513 |
| [[EGR1]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 | STRING 542 |
| [[KLF10]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 | STRING 412 |
| [[MAP2K3]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[NR4A1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ETV3]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[EGR3]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOS1]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[BMPR1A]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[RUFY2]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[FHIP2A]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[MFSD8]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CIAO2A]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[UBE4B]] | -0.57 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[CHPT1]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[MRPS5]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[GAPVD1]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[NUP133]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ABCD4]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUNX1]] | B | RUNX1 activity raises CSRNP1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.36× lower at baseline in the lines without RUNX1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[GEM]] | B | GEM activity raises CSRNP1's level | lines that do not express GEM (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without GEM | 0.040 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[CXCL8]] | B | CXCL8 activity raises CSRNP1's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without CXCL8 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[HRH1]] | B | HRH1 activity raises CSRNP1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without HRH1 | 0.050 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[TRIB1]] | B | TRIB1 activity raises CSRNP1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.19× lower at baseline in the lines without TRIB1 | 0.051 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity raises CSRNP1's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without SMAD3 | 0.059 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[SHB]] | B | SHB activity raises CSRNP1's level | lines that do not express SHB (5) vs lines expressing it (45) | 2.37× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[ZC3H12A]] | B | ZC3H12A activity raises CSRNP1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.32× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[DUSP10]] | B | DUSP10 activity strengthens CSRNP1's drug response | lines that do not express DUSP10 (10) vs lines expressing it (38) | the lines without DUSP10 respond 0.68× as strongly (z diff +1.95); strongest at Harringtonine 5 µM: 1.68x vs 3.76x (z diff +3.7) | 0.069 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FHL2]] | C | FHL2 activity raises CSRNP1's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SBNO2]] | C | CSRNP1's natural level strengthens SBNO2's drug response | CSRNP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.21; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.0, 0.2); signed map (8.0, 28.8). **Vector** length 111, 34.7% of its response variance represented; |z| ≥ 3 in 1,270 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.61 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.61 to 9); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.60 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +22.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.9 | -1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -6.5 |
|  | [[NG25 (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +1.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.3 | -2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -5.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cysteine and serine rich nuclear protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:39,141,855-39,154,562 (-) |
| Ensembl biotype | protein_coding |
| Also known as | URAX1, DKFZp566F164, FAM130B, TAIP-3; previously AXUD1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S65](https://www.uniprot.org/uniprotkb/Q96S65) (Cysteine/serine-rich nuclear protein 1):

> Binds to the consensus sequence 5'-AGAGTG-3' and has transcriptional activator activity (By similarity). May have a tumor-suppressor function. May play a role in apoptosis.

**Summary**, from NCBI Gene [64651](https://www.ncbi.nlm.nih.gov/gene/64651):

> This gene encodes a protein that localizes to the nucleus and expression of this gene is induced in response to elevated levels of axin. The Wnt signalling pathway, which is negatively regulated by axin, is important in axis formation in early development and impaired regulation of this signalling pathway is often involved in tumors. A decreased level of expression of this gene in tumors compared to the level of expression in their corresponding normal tissues suggests that this gene product …

**Accessions** — [HGNC:14300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14300) · Entrez [64651](https://www.ncbi.nlm.nih.gov/gene/64651) · UniProt [Q96S65](https://www.uniprot.org/uniprotkb/Q96S65) · Ensembl [ENSG00000144655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144655)

## Data

Gene col 6910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6910); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6910]; `tensor/DDL_lfc|DDL_z.npy` [6910]; `embed/gene_vectors.npy` [6910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6910 or target_col == 6910). Every well: [[CSRNP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSRNP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
