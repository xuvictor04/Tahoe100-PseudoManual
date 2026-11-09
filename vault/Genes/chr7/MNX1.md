---
symbol: "MNX1"
type: "gene"
col: 5095
ensembl_id: "ENSG00000130675"
name: "motor neuron and pancreas homeobox 1"
location: "7q36.3"
module: 54
arm: "+"
pooled_cpm: 12.84
n_lines_expressing: 39
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MNX1

*motor neuron and pancreas homeobox 1* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +8.6, q 4e-15, up in 26 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.451× (z -9.3, q 3e-18, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR2F6]] (+0.62, fdr 4e-05), [[SIVA1]] (+0.59, fdr 9e-05), [[SAC3D1]] (+0.58, fdr 1e-04); moves opposite to [[NCOA4]] (-0.63, fdr 5e-05), [[FLII]] (-0.58, fdr 3e-05), [[SBDS]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 6 go from it, the strongest it → [[RNF6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +8.6 | 4e-15 | 26/37 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.79×** | +6.8 | 2e-09 | 22/37 (PANC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.56×** | +5.2 | 4e-05 | 20/37 (PANC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.6 | 6e-04 | 19/37 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.011 | 10/35 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.32× | +3.2 | 0.10 | 10/37 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.32× | +3.2 | 0.10 | 11/36 (A549, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.21× | +3.2 | 0.10 | 10/37 (PANC-1, J82, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.21× | +3.1 | 0.12 | 9/37 (NCI-H460, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.451×** | -9.3 | 3e-18 | 25/33 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.570×** | -9.3 | 3e-18 | 23/35 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.484×** | -8.2 | 6e-14 | 24/36 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.546×** | -7.1 | 2e-10 | 22/37 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.595×** | -6.1 | 1e-07 | 25/37 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -4.3 | 0.002 | 15/37 (HT-29, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.481×** | -4.1 | 0.003 | 15/36 (MIA PaCa-2, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.707×** | -4.1 | 0.003 | 16/37 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -3.9 | 0.005 | 15/36 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -3.7 | 0.011 | 13/35 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -3.6 | 0.019 | 4/37 (SHP-77, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.740×** | -3.5 | 0.020 | 17/36 (Hs 766T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -3.5 | 0.021 | 16/36 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.755×** | -3.2 | 0.064 | 9/37 (A498, SW 900, …) | rises with dose | plate-row cell shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.767×** | -3.1 | 0.072 | 9/37 (KATO III, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.772×** | -3.0 | 0.086 | 15/37 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.773×** | -3.0 | 0.086 | 5/37 (A-172, SNU-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -3.0 | 0.098 | 8/34 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.07 | 1 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.84× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.0957× (z -13.6) |
| [[SW480 (line)]] | alt | 28.8 | 3 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.38× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -18.8) |
| [[KATO III (line)]] | alt | 40.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -11.8) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0892× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 40.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 9.21 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 6.00 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0576× (z -10.3) |
| [[SW48 (line)]] | wt | 33.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +14.0) | — |
| [[A-172 (line)]] | wt | 6.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0251× (z -15.6) |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -8.6) |
| [[LoVo (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -8.8) |
| [[A498 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2F6]] | +0.62 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[SIVA1]] | +0.59 | +0.37 / +0.55 | both halves | 9e-05 |  |
| [[SAC3D1]] | +0.58 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[DLL3]] | +0.57 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[TNNI3]] | +0.56 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[SH2B2]] | +0.55 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[KIAA1958]] | +0.55 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[NUDT1]] | +0.55 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[ANKRD13D]] | +0.55 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[METRN]] | +0.54 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[PTMAP2]] ⚠ | +0.54 | +0.36 / +0.48 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM243]] | +0.54 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[ANAPC11]] | +0.54 | +0.28 / +0.57 | both halves | 3e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA4]] | -0.63 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[FLII]] | -0.58 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[SBDS]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[PARP3]] | -0.57 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ZSCAN30]] | -0.56 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[ZMPSTE24]] | -0.55 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[TMEM43]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[CAPNS1]] | -0.53 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[LIN7C]] | -0.53 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[RNF6]] | -0.53 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[TAF9]] | -0.52 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[CHM]] | -0.52 | -0.33 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MNX1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SBK1]] | B | SBK1 activity raises MNX1's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without SBK1 | 0.053 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[SLC29A4]] | B | SLC29A4 activity raises MNX1's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.07× lower at baseline in the lines without SLC29A4 | 0.068 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF6]] | B | MNX1 activity raises RNF6's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without MNX1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |
| [[ANKRD9]] | B | MNX1 activity raises ANKRD9's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without MNX1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |
| [[TMEM160]] | B | MNX1 activity raises TMEM160's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without MNX1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |
| [[NR2F6]] | B | MNX1 activity raises NR2F6's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without MNX1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |
| [[ZNRF2]] | B | MNX1 activity raises ZNRF2's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without MNX1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |
| [[TAF9]] | B | MNX1 activity raises TAF9's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without MNX1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.0, -4.1); signed map (-35.9, 4.6). **Vector** length 69.7, 14.7% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.9 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +8.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.3 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.0 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -9.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.5 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | motor neuron and pancreas homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:156,994,051-157,010,663 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HB9, HOXHB9, SCRA1; previously HLXB9 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P50219](https://www.uniprot.org/uniprotkb/P50219) (Motor neuron and pancreas homeobox protein 1):

> Transcription factor (By similarity). Recognizes and binds to the regulatory elements of target genes, such as visual system homeobox CHX10, negatively modulating transcription (By similarity). Plays a role in establishing motor neuron identity, in concert with LIM domain transcription factor LMO4 (By similarity). Involved in negatively modulating transcription of interneuron genes in motor neurons, acting, at least in part, by blocking regulatory sequence interactions of the ISL1-LHX3 complex …

**Summary**, from NCBI Gene [3110](https://www.ncbi.nlm.nih.gov/gene/3110):

> This gene encodes a nuclear protein, which contains a homeobox domain and is a transcription factor. Mutations in this gene result in Currarino syndrome, an autosomic dominant congenital malformation. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:4979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4979) · Entrez [3110](https://www.ncbi.nlm.nih.gov/gene/3110) · UniProt [P50219](https://www.uniprot.org/uniprotkb/P50219) · Ensembl [ENSG00000130675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130675)

## Data

Gene col 5095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5095); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5095]; `tensor/DDL_lfc|DDL_z.npy` [5095]; `embed/gene_vectors.npy` [5095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5095 or target_col == 5095). Every well: [[MNX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MNX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
