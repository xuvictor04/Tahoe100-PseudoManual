---
symbol: "SLC35G1"
type: "gene"
col: 10703
ensembl_id: "ENSG00000176273"
name: "solute carrier family 35 member G1"
location: "10q23.33"
module: 18
arm: "+"
pooled_cpm: 11.58
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SLC35G1

*solute carrier family 35 member G1* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (15 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.03× (z +16.9, q 0e+00, up in 37 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +13.9, q 2e-41, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.403× (z -7.6, q 2e-11, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAQR3]] (+0.68, fdr 7e-06), [[HDDC2]] (+0.67, fdr 4e-05), [[USP46]] (+0.67, fdr 1e-05); moves opposite to [[ZNF324]] (-0.57, fdr 8e-05), [[KIAA0319L]] (-0.53, fdr 3e-05), [[NBEAL1]] (-0.53, fdr 3e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.03×** | +16.9 | 0e+00 | 37/40 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +13.9 | 2e-41 | 34/45 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +11.8 | 1e-29 | 26/34 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +11.7 | 2e-29 | 32/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +10.9 | 8e-26 | 16/18 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +9.6 | 9e-20 | 28/46 (PANC-1, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.77×** | +9.1 | 1e-17 | 32/46 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +8.9 | 5e-17 | 16/26 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.72×** | +8.3 | 9e-15 | 28/44 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.56×** | +7.1 | 8e-11 | 22/46 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +7.0 | 2e-10 | 26/47 (HEC-1-A, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +6.6 | 2e-09 | 19/46 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +6.4 | 7e-09 | 21/46 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +6.0 | 8e-08 | 20/46 (J82, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.43×** | +5.7 | 5e-07 | 17/46 (A498, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 2e-06 | 20/46 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.1 | 1e-05 | 13/46 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.3 | 4e-04 | 13/46 (SNU-423, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.002 | 10/46 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.18× | +3.8 | 0.004 | 12/47 (HOP62, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.008 | 16/45 (A-172, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.018 | 7/47 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.030 | 8/47 (LS 180, H4, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -7.6 | 2e-11 | 23/46 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.657×** | -6.7 | 6e-09 | 22/46 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -5.8 | 1e-06 | 18/45 (HT-29, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.502×** | -5.7 | 1e-06 | 21/43 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.733×** | -4.8 | 2e-04 | 16/45 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -3.8 | 0.012 | 16/46 (SW48, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.812×** | -3.3 | 0.070 | 13/46 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.076 | 5/46 (HepG2/C3A, HS-578T, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.07 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 12.3× (z +11.1) | [[Tadalafil (drug)]] 5 µM 0.126× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 25.8 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -19.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -10.1) |
| [[SNU-423 (line)]] | alt | 5.87 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 9.89× (z +8.9) | [[Fluvoxamine (drug)]] 0.5 µM 0.0972× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 13.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.91× (z +8.6) ⚠ toxic | [[Digitoxin (drug)]] 5 µM 0.200× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 20.1 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 11.0 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.29× (z +10.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 8.57 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 10.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.09× (z +9.3) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 6.39 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0929× (z -9.9) |
| [[SW48 (line)]] | wt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0833× (z -11.2) |
| [[A-427 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR3]] | +0.68 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[HDDC2]] | +0.67 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[USP46]] | +0.67 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[KLHL23]] | +0.67 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[NAE1]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TMEM64]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[RAB11FIP2]] | +0.63 | +0.60 / +0.37 | both halves | 7e-05 |  |
| [[RAVER2]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[RNASEH2B]] | +0.60 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[ZC3HAV1L]] | +0.60 | +0.44 / +0.33 | both halves | 1e-04 |  |
| [[FAM136A]] | +0.59 | +0.40 / +0.36 | both halves | 1e-04 |  |
| [[FAIM]] | +0.58 | +0.62 / +0.21 | both halves | 6e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF324]] | -0.57 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[KIAA0319L]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[NBEAL1]] | -0.53 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[CHMP1A]] | -0.52 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[ATG4B]] | -0.52 | -0.54 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[PDPK1]] | -0.52 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[PMM1]] | -0.52 | -0.46 / -0.32 | both halves | 1e-04 |  |
| [[VRK3]] | -0.51 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[PPARA]] | -0.51 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[MAPK8IP3]] | -0.51 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[AP1G1]] | -0.50 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[DEPP1]] | -0.49 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[TBC1D22A]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC35G1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HENMT1]] | B | HENMT1 activity lowers SLC35G1's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 1.30× higher at baseline in the lines without HENMT1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[DEPP1]] | B | DEPP1 activity lowers SLC35G1's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.71× higher at baseline in the lines without DEPP1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[ADCY3]] | B | ADCY3 activity raises SLC35G1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without ADCY3 | 0.088 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[HMGCR]] | B | HMGCR activity raises SLC35G1's level | compounds that target HMGCR: 2 of 2 lower it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.7, 12.5); signed map (-13.1, -40.9). **Vector** length 73.6, 12.9% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.0 | +16.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.2 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +3.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.4 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.4 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -2.7 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member G1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:93,893,973-93,956,062 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33990, C10orf60, POST; previously TMEM20 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2M3R5](https://www.uniprot.org/uniprotkb/Q2M3R5) (Solute carrier family 35 member G1):

> Chloride-sensitive citrate transporter localized on the basolateral membrane of enterocytes that mediates efflux of citrate into the bloodstream. May also play a role in intracellular calcium sensing and homeostasis by acting as a negative regulator of plasma membrane calcium-transporting ATPases, thereby preventing calcium efflux from the cell.

**Summary**, from NCBI Gene [159371](https://www.ncbi.nlm.nih.gov/gene/159371):

> This gene encodes a transmembrane protein which is a member of the drug/metabolite transporter protein superfamily. The encoded protein may play a role in the regulation of calcium levels inside the cell. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:26607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26607) · Entrez [159371](https://www.ncbi.nlm.nih.gov/gene/159371) · UniProt [Q2M3R5](https://www.uniprot.org/uniprotkb/Q2M3R5) · Ensembl [ENSG00000176273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176273)

## Data

Gene col 10703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10703); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10703]; `tensor/DDL_lfc|DDL_z.npy` [10703]; `embed/gene_vectors.npy` [10703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10703 or target_col == 10703). Every well: [[SLC35G1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35G1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
