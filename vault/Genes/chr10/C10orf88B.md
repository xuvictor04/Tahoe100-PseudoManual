---
symbol: "C10orf88B"
type: "gene"
col: 14950
ensembl_id: "ENSG00000255624"
name: "C10orf88B (pseudogene)"
location: "10q26.13"
module: 91
arm: "+"
pooled_cpm: 7.43
n_lines_expressing: 39
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# C10orf88B

*C10orf88B (pseudogene)* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.73× (z +15.8, q 0e+00, up in 29 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.469× (z -8.0, q 9e-13, down in 24 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEN1]] (+0.71, fdr 7e-06), [[C5]] (+0.69, fdr 1e-05), [[ZNF681]] (+0.65, fdr 3e-05); moves opposite to [[PLD3]] (-0.58, fdr 3e-04), [[ZNF235]] (-0.57, fdr 4e-05), [[PLCD1]] (-0.57, fdr 5e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +15.8 | 0e+00 | 29/35 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.84×** | +15.0 | 0e+00 | 23/24 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +14.7 | 0e+00 | 10/11 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.48×** | +13.4 | 1e-38 | 29/33 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +11.5 | 2e-28 | 12/16 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +9.4 | 6e-19 | 24/35 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.4 | 5e-15 | 20/36 (SW480, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.80×** | +6.3 | 2e-08 | 15/25 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.71×** | +6.0 | 1e-07 | 15/36 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.68×** | +5.8 | 4e-07 | 19/36 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +5.5 | 3e-06 | 14/35 (NCI-H2030, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.004 | 8/36 (NCI-H460, A-427, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.006 | 7/36 (HOP62, NCI-H23, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.26×** | +3.7 | 0.011 | 5/36 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.016 | 4/36 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.027 | 3/36 (KATO III, SNU-423, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.051 | 7/36 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.052 | 4/33 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.054 | 5/36 (HEC-1-A, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.054 | 6/36 (NCI-H460, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.469×** | -8.0 | 9e-13 | 24/36 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.351×** | -6.1 | 3e-07 | 17/36 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.590×** | -5.9 | 7e-07 | 18/36 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -5.5 | 7e-06 | 13/29 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.629×** | -5.2 | 3e-05 | 20/36 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.430×** | -4.9 | 8e-05 | 12/28 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -4.8 | 1e-04 | 18/36 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -4.6 | 3e-04 | 17/31 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.676×** | -4.4 | 8e-04 | 12/36 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.697×** | -4.0 | 0.003 | 14/36 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.711×** | -3.8 | 0.007 | 13/35 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[palbociclib (drug)]] 0.5 µM |  | **0.629×** | -3.7 | 0.010 | 11/37 (A498, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.737×** | -3.4 | 0.028 | 8/36 (A-427, SHP-77, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.663×** | -3.3 | 0.042 | 6/36 (PANC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.738×** | -3.3 | 0.042 | 6/36 (SW 1271, HepG2/C3A, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.0 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.153× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 30.3 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +9.5) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.243× (z -10.8) |
| [[SW480 (line)]] | alt | 7.67 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +13.3) | — |
| [[A549 (line)]] | wt | 5.81 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.47× (z +9.9) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0977× (z -8.7) |
| [[C-33 A (line)]] | alt | 9.69 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0738× (z -9.2) |
| [[SNU-423 (line)]] | alt | 5.53 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +9.2) | [[Thymol (drug)]] 0.5 µM 0.0662× (z -10.3) |
| [[A-427 (line)]] | wt | 32.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.317× (z -8.9) |
| [[KATO III (line)]] | alt | 5.86 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0737× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 8.03 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.3× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 7.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 1 | — | [[Artesunate (drug)]] 0.5 µM 0.138× (z -8.7) |
| [[A-172 (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.690 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.662 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEN1]] | +0.71 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[C5]] | +0.69 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[ZNF681]] | +0.65 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[LMNB1-DT]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ZNF726]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[XRCC2]] | +0.62 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[CENPH]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[DARS2]] | +0.62 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[FBXO43]] | +0.61 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[ADAT1]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[LRR1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[BRCA2]] | +0.60 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLD3]] | -0.58 | -0.62 / -0.28 | both halves | 3e-04 |  |
| [[ZNF235]] | -0.57 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[PLCD1]] | -0.57 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ATP5MJ]] | -0.57 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[TUBG2]] | -0.57 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[BLVRB]] | -0.56 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[IFT52]] | -0.56 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[MGST3]] | -0.56 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[TBC1D17]] | -0.55 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[SEZ6L2]] | -0.55 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[MRPL43]] | -0.55 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[CYB5R1]] | -0.55 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C10orf88B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.4, -45.7); signed map (30.9, -30.6). **Vector** length 73.2, 15.2% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.54 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.55 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +15.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +15.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +8.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +3.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -8.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +2.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | C10orf88B (pseudogene) |
| Locus type | pseudogene |
| Location | 10q26.13 — chr10:122,879,851-122,898,024 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | C10orf88BP |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44080) · Entrez [399815](https://www.ncbi.nlm.nih.gov/gene/399815) · Ensembl [ENSG00000255624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255624)

## Data

Gene col 14950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14950); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14950]; `tensor/DDL_lfc|DDL_z.npy` [14950]; `embed/gene_vectors.npy` [14950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14950 or target_col == 14950). Every well: [[C10orf88B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C10orf88B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
