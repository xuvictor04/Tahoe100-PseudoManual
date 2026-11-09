---
symbol: "CHROMR"
type: "gene"
col: 13372
ensembl_id: "ENSG00000223960"
name: "cholesterol induced regulator of metabolism RNA"
location: "2q31.2"
module: 32
arm: "+"
pooled_cpm: 14.72
n_lines_expressing: 38
n_dd_up: 10
n_dd_down: 30
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CHROMR

*cholesterol induced regulator of metabolism RNA* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.72× (z +9.7, q 2e-19, up in 25 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.52× (z +3.9, q 0.013, up in 17 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.464× (z -10.5, q 5e-23, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD9L]] (+0.62, fdr 1e-05), [[SAMD9]] (+0.62, fdr 8e-06), [[HERC6]] (+0.59, fdr 2e-05); moves opposite to [[MPG]] (-0.50, fdr 6e-05), [[ELMO3]] (-0.50, fdr 1e-04), [[FAM83E]] (-0.49, fdr 6e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ANTXR1]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Mifepristone (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +9.7 | 2e-19 | 25/32 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.7 | 1e-15 | 20/21 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +6.1 | 1e-07 | 16/29 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.013 | 17/35 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.028 | 12/34 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.035 | 11/35 (NCI-H2030, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.089 | 11/35 (SNU-423, A549, …) | rises with dose | position effect removed |
| [[Megestrol (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.089 | 12/36 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.089 | 11/36 (A498, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.089 | 9/36 (C-33 A, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.11 | 14/36 (A549, C-33 A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.464×** | -10.5 | 5e-23 | 28/35 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.368×** | -9.7 | 1e-19 | 29/35 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.440×** | -7.9 | 4e-13 | 29/36 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.445×** | -7.8 | 8e-13 | 28/36 (J82, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.470×** | -7.3 | 4e-11 | 30/35 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.473×** | -7.2 | 4e-11 | 26/36 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -7.2 | 4e-11 | 25/34 (LoVo, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.483×** | -7.0 | 2e-10 | 26/35 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.541×** | -5.9 | 2e-07 | 25/35 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.327×** | -5.6 | 1e-06 | 22/36 (H4, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.570×** | -5.4 | 3e-06 | 21/35 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.388×** | -4.8 | 8e-05 | 20/33 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.631×** | -4.4 | 4e-04 | 21/34 (AsPC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.738×** | -4.1 | 0.001 | 19/36 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.636×** | -4.1 | 0.001 | 21/36 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.742×** | -4.1 | 0.002 | 17/36 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.657×** | -3.9 | 0.003 | 18/36 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.689×** | -3.6 | 0.009 | 17/34 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 34.5 | 0 | 7 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0547× (z -16.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.196× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 36.8 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.164× (z -9.7) |
| [[H4 (line)]] | wt | 22.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.8) |
| [[Hs 766T (line)]] | wt | 9.42 | 0 | 2 | — | [[Allantoin (drug)]] 0.5 µM 0.0916× (z -10.2) |
| [[PANC-1 (line)]] | alt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.8) |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -13.0) |
| [[SW480 (line)]] | alt | 16.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -8.8) |
| [[A-172 (line)]] | wt | 32.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -12.1) |
| [[A-427 (line)]] | wt | 12.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.203× (z -8.5) |
| [[A498 (line)]] | wt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.0) |
| [[A549 (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 7.53 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0860× (z -8.8) |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0495× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0502× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 10.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD9L]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SAMD9]] | +0.62 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[HERC6]] | +0.59 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[XAF1]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LINC01116]] | +0.59 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[DDX60L]] | +0.58 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[DTX3L]] | +0.58 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[EIF2AK2]] | +0.57 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[PARP14]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SAMHD1]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[IFIT5]] | +0.57 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[IFIT2]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.50 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[ELMO3]] | -0.50 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[FAM83E]] | -0.49 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[SOCS7]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SNX14]] | -0.47 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[UQCRH]] | -0.47 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[KCNK6]] | -0.46 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[RPL18]] ⚠ | -0.46 | -0.33 / -0.42 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANTXR1]] | B | ANTXR1 activity raises CHROMR's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 2.82× lower at baseline in the lines without ANTXR1 | 0.014 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[LINC00648]] | B | LINC00648 activity strengthens CHROMR's drug response | lines that do not express LINC00648 (24) vs lines expressing it (12) | the lines without LINC00648 respond 0.74× as strongly (z diff +1.49); strongest at Panobinostat 5 µM: 0.53x vs 0.31x (z diff +2.6) | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; target measured in part of the lines; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers CHROMR's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[ADAMTS10]] | B | ADAMTS10 activity raises CHROMR's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without ADAMTS10 | 0.032 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| [[APOBEC3G]] | B | APOBEC3G activity raises CHROMR's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without APOBEC3G | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |
| [[MAP2K2]] | B | MAP2K2 activity lowers CHROMR's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Mifepristone (drug)]] 0.5 µM | B | CHROMR activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express CHROMR (12) vs lines expressing it (36) | the lines without CHROMR: 0.82× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: CCDC88A, LARP6, DLK2; maybe low, not absent |
| [[ADAMTS10]] | B | CHROMR activity raises ADAMTS10's level | lines that do not express CHROMR (12) vs lines expressing it (38) | 2.58× lower at baseline in the lines without CHROMR | 0.091 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: CCDC88A, LARP6, DLK2; maybe low, not absent |
| [[PHF11]] | C | CHROMR's natural level strengthens PHF11's drug response | CHROMR's natural level across 34 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.54; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.0, 54.8); signed map (63.1, 33.1). **Vector** length 87.3, 24.1% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IFIT antiviral response* (reactome, mean cos +0.53 to 9); *Viral strategies to evade IFIT action* (reactome, mean cos +0.54 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -0.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.9 | +3.1 |
| fall | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.3 | -2.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | cholesterol induced regulator of metabolism RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q31.2 — chr2:178,413,635-178,440,243 (+) |
| Ensembl biotype | lncRNA |
| Also known as | CHROME; previously PRKRA-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54059) · Entrez [101927027](https://www.ncbi.nlm.nih.gov/gene/101927027) · Ensembl [ENSG00000223960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223960)

## Data

Gene col 13372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13372); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13372]; `tensor/DDL_lfc|DDL_z.npy` [13372]; `embed/gene_vectors.npy` [13372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13372 or target_col == 13372). Every well: [[CHROMR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHROMR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
