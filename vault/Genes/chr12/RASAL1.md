---
symbol: "RASAL1"
type: "gene"
col: 3224
ensembl_id: "ENSG00000111344"
name: "RAS protein activator like 1"
location: "12q24.13"
module: 85
arm: "+"
pooled_cpm: 7.12
n_lines_expressing: 25
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 19
direction_downstream: 20
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# RASAL1

*RAS protein activator like 1* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.86× (z +17.1, q 0e+00, up in 18 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.593× (z -6.0, q 1e-06, down in 14 of 21 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMTK3]] (+0.64, fdr 1e-05), [[FCHO1]] (+0.63, fdr 1e-05), [[CBLC]] (+0.62, fdr 2e-05); moves opposite to [[EFCAB2]] (-0.57, fdr 3e-05), [[KIF27]] (-0.57, fdr 4e-04), [[ASXL2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[MPP7]] → it (grade B ⚠); 20 go from it, the strongest it → [[CCDC120]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.86×** | +17.1 | 0e+00 | 18/21 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.66×** | +11.3 | 5e-27 | 18/21 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +9.7 | 6e-20 | 10/22 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +8.3 | 1e-14 | 16/22 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +6.7 | 2e-09 | 11/21 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.7 | 3e-09 | 0/7 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +6.3 | 2e-08 | 8/21 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +5.9 | 3e-07 | 11/21 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +5.7 | 7e-07 | 0/9 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.30×** | +5.0 | 3e-05 | 7/21 (NCI-H460, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +4.8 | 1e-04 | 1/9 (HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.4 | 4e-04 | 3/21 (NCI-H23, LoVo, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.0 | 0.002 | 3/21 (KATO III, A-427, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.9 | 0.004 | 0/10 | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.9 | 0.004 | 0/12 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.37×** | +3.7 | 0.008 | 8/21 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -6.0 | 1e-06 | 14/21 (CFPAC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.607×** | -5.7 | 3e-06 | 15/22 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.664×** | -4.7 | 5e-04 | 11/21 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.682×** | -4.4 | 0.002 | 13/18 (KATO III, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.684×** | -4.3 | 0.002 | 12/21 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.695×** | -4.2 | 0.003 | 7/21 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.702×** | -4.0 | 0.004 | 8/22 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.791×** | -3.8 | 0.010 | 4/21 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.719×** | -3.8 | 0.010 | 12/21 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.731×** | -3.6 | 0.019 | 9/22 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.737×** | -3.4 | 0.041 | 7/21 (SNU-423, KATO III, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.747×** | -3.3 | 0.041 | 8/21 (SW 900, KATO III, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.761×** | -3.1 | 0.078 | 5/21 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -10.5) |
| [[KATO III (line)]] | alt | 43.3 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0261× (z -20.3) |
| [[HEC-1-A (line)]] | alt | 53.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -18.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0473× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -8.8) |
| [[A498 (line)]] | wt | 7.45 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.138× (z -9.9) |
| [[LoVo (line)]] | wt | 11.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -12.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -9.0) ⚠ cell-cycle shift, explains ~11% of this change |
| [[A-172 (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.833 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK3]] | +0.64 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CBLC]] | +0.62 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TMEM63C]] | +0.62 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SEMA4D]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[EDA]] | +0.61 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[GPR160]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[KCNK15-AS1]] | +0.60 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[CDK18]] | +0.60 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[CRYBG2]] | +0.59 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[USH1C]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[CFD]] | +0.59 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.57 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[KIF27]] | -0.57 | -0.59 / -0.24 | both halves | 4e-04 |  |
| [[ASXL2]] | -0.56 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[MAD2L1-DT]] | -0.56 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[SPRY3]] | -0.56 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[ZMYND11]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[AVEN]] | -0.55 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[UBE3B]] | -0.54 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ST7L]] | -0.54 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[UBTF]] | -0.53 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TRAPPC8]] | -0.53 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[SDCBP2-AS1]] | -0.53 | -0.58 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP7]] | B | MPP7 activity raises RASAL1's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without MPP7 | 0.098 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[ATP2C2]] | C | ATP2C2 activity raises RASAL1's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.07× lower at baseline in the lines without ATP2C2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[NCMAP]] | C | NCMAP activity raises RASAL1's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.77× lower at baseline in the lines without NCMAP | 0.013 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent; co-absent with the target |
| [[EPHA1]] | C | EPHA1 activity raises RASAL1's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.40× lower at baseline in the lines without EPHA1 | 0.015 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[ARHGAP8]] | C | ARHGAP8 activity raises RASAL1's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 2.59× lower at baseline in the lines without ARHGAP8 | 0.018 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises RASAL1's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.84× lower at baseline in the lines without BSPRY | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[TC2N]] | C | TC2N activity raises RASAL1's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without TC2N | 0.023 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14; co-absent with the target |
| [[PADI2]] | C | PADI2 activity raises RASAL1's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without PADI2 | 0.024 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2; co-absent with the target |
| [[SMPDL3B]] | C | SMPDL3B activity raises RASAL1's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.69× lower at baseline in the lines without SMPDL3B | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1; co-absent with the target |
| [[ENPP5]] | C | ENPP5 activity raises RASAL1's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without ENPP5 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004; co-absent with the target |
| [[CRYBG2]] | C | CRYBG2 activity raises RASAL1's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.39× lower at baseline in the lines without CRYBG2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1; co-absent with the target |
| [[SLC5A1]] | C | SLC5A1 activity raises RASAL1's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 2.71× lower at baseline in the lines without SLC5A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 11, C 9. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC120]] | B | RASAL1 activity raises CCDC120's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.01× lower at baseline in the lines without RASAL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[IFNLR1]] | B | RASAL1 activity raises IFNLR1's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.86× lower at baseline in the lines without RASAL1 | 0.034 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[TPD52L1]] | B | RASAL1 activity raises TPD52L1's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without RASAL1 | 0.036 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[ZNF511]] | B | RASAL1 activity raises ZNF511's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without RASAL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[TEC]] | B | RASAL1 activity raises TEC's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without RASAL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[FCHO1]] | B | RASAL1 activity raises FCHO1's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without RASAL1 | 0.076 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[FCHO1]] | B | RASAL1 activity weakens FCHO1's drug response | lines that do not express RASAL1 (22) vs lines expressing it (20) | the lines without RASAL1 respond 1.14× as strongly (z diff -1.02); strongest at Dinaciclib 0.05 µM: 1.41x vs 0.82x (z diff -2.5) | 0.076 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1; target measured in part of the lines; artifact flags |
| [[TSTD2]] | B | RASAL1 activity lowers TSTD2's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 1.27× higher at baseline in the lines without RASAL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[VWDE]] | B | RASAL1 activity raises VWDE's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.84× lower at baseline in the lines without RASAL1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[SLC29A2]] | B | RASAL1 activity raises SLC29A2's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without RASAL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[LMTK3]] | B | RASAL1 activity raises LMTK3's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without RASAL1 | 0.096 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[ARHGAP8]] | C | RASAL1 activity raises ARHGAP8's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 3.38× lower at baseline in the lines without RASAL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (10.0, 1.8); signed map (-22.8, 31.8). **Vector** length 58.9, 14.9% of its response variance represented; |z| ≥ 3 in 530 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +17.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +11.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +8.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | RAS protein activator like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:113,098,819-113,136,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RASAL |
| Gene groups (HGNC) | Pleckstrin homology domain containing; C2 and RasGAP domain containing |
| Reactome | 4 pathways, smallest: Regulation of RAS by GAPs; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O95294](https://www.uniprot.org/uniprotkb/O95294) (RasGAP-activating-like protein 1):

> Probable inhibitory regulator of the Ras-cyclic AMP pathway. Plays a role in dendrite formation by melanocytes.

**Summary**, from NCBI Gene [8437](https://www.ncbi.nlm.nih.gov/gene/8437):

> The protein encoded by this gene is member of the GAP1 family of GTPase-activating proteins. These proteins stimulate the GTPase activity of normal RAS p21 but not its oncogenic counterpart. Acting as a suppressor of RAS function, the protein enhances the weak intrinsic GTPase activity of RAS proteins resulting in the inactive GDP-bound form of RAS, thereby allowing control of cellular proliferation and differentiation. This particular family member contains domains which are characteristic of …

**Accessions** — [HGNC:9873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9873) · Entrez [8437](https://www.ncbi.nlm.nih.gov/gene/8437) · UniProt [O95294](https://www.uniprot.org/uniprotkb/O95294) · Ensembl [ENSG00000111344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111344)

## Data

Gene col 3224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3224); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3224]; `tensor/DDL_lfc|DDL_z.npy` [3224]; `embed/gene_vectors.npy` [3224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3224 or target_col == 3224). Every well: [[RASAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
