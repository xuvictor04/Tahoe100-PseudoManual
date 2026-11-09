---
symbol: "IRAK4"
type: "gene"
col: 12510
ensembl_id: "ENSG00000198001"
name: "interleukin 1 receptor associated kinase 4"
location: "12q12"
module: 85
arm: "-"
pooled_cpm: 19.96
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# IRAK4

*interleukin 1 receptor associated kinase 4* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +15.3, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.412× (z -13.5, q 1e-38, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DECR1]] (+0.70, fdr 1e-05), [[FAM120AOS]] (+0.67, fdr 1e-05), [[PSME3IP1]] (+0.67, fdr 2e-05); moves opposite to [[VPS37C]] (-0.61, fdr 1e-05), [[MAST3]] (-0.61, fdr 2e-04), [[TNFAIP8L1]] (-0.61, fdr 2e-05).
> It sits in the **-** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +15.3 | 0e+00 | 43/46 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +12.2 | 1e-31 | 35/41 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +10.9 | 2e-25 | 24/32 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +8.7 | 4e-16 | 37/46 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +8.2 | 3e-14 | 23/35 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.6 | 3e-12 | 33/48 (LS 180, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +6.8 | 7e-10 | 31/46 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.6 | 2e-06 | 21/48 (A-427, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 7e-05 | 17/48 (NCI-H23, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.36×** | +4.5 | 4e-04 | 17/44 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 16/48 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.001 | 17/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +4.2 | 0.001 | 18/47 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 18/47 (NCI-H23, A549, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.007 | 18/48 (Hs 766T, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.008 | 18/48 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.009 | 17/47 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.015 | 9/47 (NCI-H23, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.039 | 9/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.039 | 12/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.412×** | -13.5 | 1e-38 | 41/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -12.7 | 2e-34 | 37/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.471×** | -11.5 | 4e-28 | 39/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.474×** | -11.3 | 1e-27 | 40/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -4.9 | 1e-04 | 25/44 (C-33 A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.744×** | -4.1 | 0.004 | 16/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.8 | 0.013 | 2/48 (HepG2/C3A, SNU-1) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.014 | 20/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.647×** | -3.5 | 0.034 | 14/46 (RKO, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.869× | -3.0 | 0.14 | 10/48 (AN3 CA, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.685× | -3.0 | 0.14 | 20/48 (NCI-H460, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.7 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 34.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0656× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.119× (z -16.7) |
| [[PANC-1 (line)]] | alt | 24.6 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +12.7) | [[Digitoxin (drug)]] 5 µM 0.237× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.274× (z -12.2) |
| [[LoVo (line)]] | wt | 31.9 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.385× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 15.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +11.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 37.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -9.6) |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 12.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 24.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 19.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.2) | [[Lonafarnib (drug)]] 5 µM 0.0887× (z -8.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +10.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.25× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 7.24 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -11.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 8.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | +0.70 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[FAM120AOS]] | +0.67 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[PSME3IP1]] | +0.67 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PDIA3P1]] | +0.63 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[PHYH]] | +0.63 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[GANC]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[RWDD2B]] | +0.62 | +0.75 / +0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[FAM174B]] | +0.61 | +0.63 / +0.27 | both halves | 3e-04 |  |
| [[HFE]] | +0.61 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ZMPSTE24]] | +0.61 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ZMYND11]] | +0.60 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[IL13RA1]] | +0.60 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[NCOA4]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37C]] | -0.61 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[MAST3]] | -0.61 | -0.62 / -0.32 | both halves | 2e-04 |  |
| [[TNFAIP8L1]] | -0.61 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[FCHO1]] | -0.60 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[KYAT1]] | -0.59 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[CKLF]] | -0.59 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[MAP1S]] | -0.58 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[FBXL16]] | -0.57 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.57 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[BAIAP3]] | -0.57 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[ANAPC11]] | -0.56 | -0.58 / -0.22 | both halves | 6e-04 |  |
| [[SH2B2]] | -0.56 | -0.55 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IRAK4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers IRAK4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **-** arm (projection on the module's main direction -0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-1.7, 11.9); signed map (26.0, -21.2). **Vector** length 79.2, 16.4% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +12.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +6.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -12.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.5 | -0.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.4 | -0.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor associated kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:43,758,944-43,798,307 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-64 |
| Gene groups (HGNC) | Interleukin 1 receptor associated kinase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 26 pathways, smallest: TRAF6 mediated IRF7 activation in TLR7/8 or 9 signaling; IRAK4 deficiency (TLR2/4); Diseases associated with the TLR signaling cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWZ3](https://www.uniprot.org/uniprotkb/Q9NWZ3) (Interleukin-1 receptor-associated kinase 4):

> Serine/threonine-protein kinase that plays a critical role in initiating innate immune response against foreign pathogens. Involved in Toll-like receptor (TLR) and IL-1R signaling pathways. Is rapidly recruited by MYD88 to the receptor-signaling complex upon TLR activation to form the Myddosome together with IRAK2. Phosphorylates initially IRAK1, thus stimulating the kinase activity and intensive autophosphorylation of IRAK1. Phosphorylates E3 ubiquitin ligases Pellino proteins (PELI1, PELI2 …

**Summary**, from NCBI Gene [51135](https://www.ncbi.nlm.nih.gov/gene/51135):

> This gene encodes a kinase that activates NF-kappaB in both the Toll-like receptor (TLR) and T-cell receptor (TCR) signaling pathways. The protein is essential for most innate immune responses. Mutations in this gene result in IRAK4 deficiency and recurrent invasive pneumococcal disease. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:17967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17967) · Entrez [51135](https://www.ncbi.nlm.nih.gov/gene/51135) · UniProt [Q9NWZ3](https://www.uniprot.org/uniprotkb/Q9NWZ3) · Ensembl [ENSG00000198001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198001)

## Data

Gene col 12510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12510); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12510]; `tensor/DDL_lfc|DDL_z.npy` [12510]; `embed/gene_vectors.npy` [12510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12510 or target_col == 12510). Every well: [[IRAK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRAK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
