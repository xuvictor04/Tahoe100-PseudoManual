---
symbol: "ADGRL2"
type: "gene"
col: 3873
ensembl_id: "ENSG00000117114"
name: "adhesion G protein-coupled receptor L2"
location: "1p31.1"
module: 9
arm: "+"
pooled_cpm: 66.53
n_lines_expressing: 31
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ADGRL2

*adhesion G protein-coupled receptor L2* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +11.3, q 6e-27, up in 15 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.602× (z -9.1, q 3e-17, down in 21 of 29 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS3ST5]] (+0.58, fdr 1e-05), [[BHMT2]] (+0.54, fdr 2e-04), [[RMST]] (+0.51, fdr 3e-05); moves opposite to [[LSM14B]] (-0.48, fdr 1e-04), [[SNAP29]] (-0.45, fdr 1e-04), [[PKN1]] (-0.44, fdr 7e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[BMP5]] → it (grade B ⚠); 2 go from it, the strongest it → [[BMP5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +11.3 | 6e-27 | 15/30 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +6.1 | 3e-07 | 13/29 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.4 | 1e-05 | 12/24 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.008 | 10/30 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.008 | 10/29 (HS-578T, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +3.7 | 0.021 | 10/29 (C32, Panc 03.27, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.11 | 5/29 (Panc 03.27, SHP-77, …) | all doses, flat | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.11 | 7/27 (hTERT-HPNE, NCI-H460, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +3.1 | 0.11 | 6/28 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.11 | 10/28 (NCI-H460, C32, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.12 | 9/29 (SW480, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3873.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.602×** | -9.1 | 3e-17 | 21/29 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.631×** | -8.3 | 3e-14 | 18/29 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -7.9 | 4e-13 | 21/28 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.664×** | -7.4 | 2e-11 | 21/29 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.726×** | -5.8 | 1e-06 | 17/29 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.747×** | -5.2 | 1e-05 | 17/29 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.847× | -4.2 | 0.002 | 16/29 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.792×** | -4.2 | 0.002 | 16/28 (A498, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.809×** | -3.8 | 0.009 | 13/29 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.814×** | -3.6 | 0.021 | 14/28 (SHP-77, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.762×** | -3.5 | 0.024 | 14/28 (HEC-1-A, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.832×** | -3.3 | 0.044 | 13/28 (CHP-212, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.834× | -3.3 | 0.049 | 7/29 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -3.2 | 0.049 | 8/29 (SW480, SHP-77, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.837× | -3.2 | 0.053 | 8/29 (SW480, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.883× | -3.1 | 0.055 | 14/30 (SW480, SHP-77, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.717×** | -3.1 | 0.055 | 9/28 (SW480, J82, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.841× | -3.1 | 0.055 | 10/29 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.720×** | -3.1 | 0.056 | 8/29 (LOX-IMVI, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 0.849× | -2.9 | 0.086 | 6/29 (Hs 766T, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 403 | 0 | 15 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -15.7) |
| [[SW480 (line)]] | alt | 308 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0702× (z -18.7) |
| [[HOP62 (line)]] | alt | 27.2 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.03× (z +10.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.97× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H23 (line)]] | alt | 89.7 | 0 | 4 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.626× (z -10.6) ⚠ position not correctable · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -8.5) |
| [[A498 (line)]] | wt | 66.4 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 209 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 86.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -10.4) |
| [[Hs 766T (line)]] | wt | 181 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -10.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Panc 03.27 (line)]] | alt | 48.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[A549 (line)]] | wt | 69.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[C32 (line)]] | wt | 34.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[J82 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H1573 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H2347 (line)]] | alt | 18.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.35× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 28.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +17.1) | — |
| [[NCI-H661 (line)]] | alt | 1,383 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -10.3) |
| [[PANC-1 (line)]] | alt | 77.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.414× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.97 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS3ST5]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[BHMT2]] | +0.54 | +0.48 / +0.31 | both halves | 2e-04 |  |
| [[RMST]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[RUNX1T1]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[SYT4]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[CSRNP3]] | +0.51 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[ROBO2]] | +0.50 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[ZNF804A]] | +0.50 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[KCND2]] | +0.49 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[GRIK1]] | +0.49 | +0.45 / +0.39 | both halves | 6e-05 |  |
| [[SLCO6A1]] | +0.49 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[RIT2]] | +0.48 | +0.46 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM14B]] | -0.48 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SNAP29]] | -0.45 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[PKN1]] | -0.44 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[BRI3]] | -0.44 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[RNF187]] | -0.44 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[CABLES2]] | -0.43 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[WIPF2]] | -0.43 | -0.43 / -0.29 | both halves | 3e-04 |  |
| [[MIGA2]] | -0.43 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[TOLLIP]] | -0.42 | -0.38 / -0.37 | both halves | 7e-05 |  |
| [[RASSF1]] | -0.42 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[PLXNA3]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[KLHL26]] | -0.41 | -0.35 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP5]] | B | BMP5 activity raises ADGRL2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 4.01× lower at baseline in the lines without BMP5 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3 |
| [[NELL2]] | B | NELL2 activity raises ADGRL2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.68× lower at baseline in the lines without NELL2 | 0.025 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[ADAMTS19]] | B | ADAMTS19 activity raises ADGRL2's level | lines that do not express ADAMTS19 (11) vs lines expressing it (39) | 3.02× lower at baseline in the lines without ADAMTS19 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000287943, FAM13C, ABCA12; maybe low, not absent |
| [[RMST]] | B | RMST activity raises ADGRL2's level | lines that do not express RMST (35) vs lines expressing it (15) | 2.99× lower at baseline in the lines without RMST | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent |
| [[DACH1]] | B | DACH1 activity raises ADGRL2's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 2.37× lower at baseline in the lines without DACH1 | 0.070 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7 |
| [[GRIK1]] | B | GRIK1 activity raises ADGRL2's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.65× lower at baseline in the lines without GRIK1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent |
| [[RUNX1T1]] | B | RUNX1T1 activity raises ADGRL2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.44× lower at baseline in the lines without RUNX1T1 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[HS3ST5]] | C | HS3ST5 activity raises ADGRL2's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 3.38× lower at baseline in the lines without HS3ST5 | 0.077 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP5]] | B | ADGRL2 activity raises BMP5's level | lines that do not express ADGRL2 (19) vs lines expressing it (31) | 2.40× lower at baseline in the lines without ADGRL2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAM23, SCN9A, WDR17 |
| [[ROBO1]] | B | ADGRL2 activity raises ROBO1's level | lines that do not express ADGRL2 (19) vs lines expressing it (31) | 2.54× lower at baseline in the lines without ADGRL2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAM23, SCN9A, WDR17 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.0, 38.7); signed map (45.9, 32.8). **Vector** length 89.0, 24.0% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +11.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | -0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | +5.0 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | -9.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -7.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -5.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -0.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor L2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:81,306,147-81,993,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0786, LEC1, CIRL2; previously LPHH1, LPHN2 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily L; Olfactomedin domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [O95490](https://www.uniprot.org/uniprotkb/O95490) (Adhesion G protein-coupled receptor L2):

> Orphan adhesion G protein-coupled receptor (aGPCR), which mediates synapse specificity (By similarity). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors (By similarity). Following G protein-coupled receptor activation, associates with cell adhesion molecules that are expressed at the surface of adjacent cells to direct synapse specificity. Specifically mediates the …

**Summary**, from NCBI Gene [23266](https://www.ncbi.nlm.nih.gov/gene/23266):

> This gene encodes a member of the latrophilin subfamily of G-protein coupled receptors. The encoded protein participates in the regulation of exocytosis. The proprotein is thought to be further cleaved within a cysteine-rich G-protein-coupled receptor proteolysis site into two chains that are non-covalently bound at the cell membrane. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:18582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18582) · Entrez [23266](https://www.ncbi.nlm.nih.gov/gene/23266) · UniProt [O95490](https://www.uniprot.org/uniprotkb/O95490) · Ensembl [ENSG00000117114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117114)

## Data

Gene col 3873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3873); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3873]; `tensor/DDL_lfc|DDL_z.npy` [3873]; `embed/gene_vectors.npy` [3873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3873 or target_col == 3873). Every well: [[ADGRL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
