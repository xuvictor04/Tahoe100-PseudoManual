---
symbol: "STOX1"
type: "gene"
col: 9176
ensembl_id: "ENSG00000165730"
name: "storkhead box 1"
location: "10q22.1"
module: 10
arm: "+"
pooled_cpm: 6.31
n_lines_expressing: 41
n_dd_up: 31
n_dd_down: 19
n_dd_up_clean: 22
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# STOX1

*storkhead box 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.99× (z +16.8, q 0e+00, up in 29 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.511× (z -7.2, q 2e-10, down in 21 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.537× (z -6.7, q 5e-09, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (49 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 51 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLBD1-AS1]] (+0.62, fdr 0.001, ⚠ one half only (not replicated)), [[DHRS4L2]] (+0.61, fdr 1e-05), [[F8]] (+0.60, fdr 2e-04), [[C5]] (+0.59, fdr 3e-05); moves opposite to [[GET1]] (-0.56, fdr 9e-04, ⚠ one half only (not replicated)), [[LINC02935]] (-0.54, fdr 3e-05), [[ANKRD27]] (-0.53, fdr 0.004, ⚠ one half only (not replicated)), [[TUSC2]] (-0.51, fdr 7e-04), [[VRK3]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[SNX5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +16.8 | 0e+00 | 29/31 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +15.6 | 0e+00 | 24/32 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +9.6 | 1e-19 | 23/37 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.06×** | +7.8 | 9e-13 | 25/36 (SW480, PANC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +7.6 | 5e-12 | 18/37 (Panc 03.27, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.88×** | +6.6 | 4e-09 | 10/22 (SW480, HOP62, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.87×** | +6.5 | 6e-09 | 16/32 (SW480, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.79×** | +6.3 | 2e-08 | 16/38 (PANC-1, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +6.2 | 3e-08 | 17/34 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.69×** | +5.4 | 3e-06 | 1/7 (HOP62) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +5.3 | 6e-06 | 13/31 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.56×** | +4.8 | 7e-05 | 3/23 (A498, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +4.8 | 8e-05 | 12/37 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.7 | 9e-05 | 7/37 (A498, J82, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.55×** | +4.7 | 9e-05 | 13/37 (SW480, PANC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.51×** | +4.5 | 3e-04 | 11/35 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.001 | 9/35 (SW480, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.001 | 8/35 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Afatinib (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.005 | 8/37 (LoVo, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.012 | 10/34 (NCI-H1573, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.014 | 9/34 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -7.2 | 2e-10 | 21/33 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.537×** | -6.7 | 5e-09 | 23/38 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.563×** | -6.2 | 1e-07 | 20/36 (A-427, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.565×** | -6.2 | 1e-07 | 17/36 (PANC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.678×** | -5.9 | 4e-07 | 18/35 (Panc 03.27, C-33 A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.634×** | -4.9 | 8e-05 | 18/35 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -4.8 | 1e-04 | 16/34 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.642×** | -4.8 | 1e-04 | 19/32 (SW480, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.651×** | -4.6 | 2e-04 | 17/36 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.659×** | -4.5 | 4e-04 | 13/36 (AN3 CA, RKO, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.472×** | -4.2 | 0.001 | 15/32 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.664×** | -4.2 | 0.001 | 14/33 (LS 180, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.682×** | -4.1 | 0.002 | 15/35 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.723×** | -3.5 | 0.018 | 7/38 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.724×** | -3.5 | 0.018 | 7/36 (RKO, C-33 A, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.727×** | -3.4 | 0.021 | 10/36 (HT-29, SK-MEL-2, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.737×** | -3.2 | 0.050 | 9/35 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.4 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -13.0) |
| [[A-427 (line)]] | wt | 14.4 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.141× (z -10.9) |
| [[PANC-1 (line)]] | alt | 7.53 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.143× (z -10.4) |
| [[SW48 (line)]] | wt | 20.9 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.0534× (z -11.0) |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0541× (z -9.5) |
| [[C-33 A (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -9.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 2.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 5.36 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0861× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 6.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +10.8) | — |
| [[RKO (line)]] | wt | 12.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.113× (z -9.6) |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0524× (z -9.5) |
| [[A-172 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 46 of them with an alert (⚠; 46 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLBD1-AS1]] | +0.62 | +0.70 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[DHRS4L2]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[F8]] | +0.60 | +0.68 / +0.29 | both halves | 2e-04 |  |
| [[C5]] | +0.59 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[GTF3C6]] | +0.59 | +0.64 / -0.02 | ⚠ one half (not replicated) | 1.00 |  |
| [[SLC25A21]] | +0.59 | +0.62 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[LACTB2]] | +0.58 | +0.70 / +0.22 | both halves | 6e-04 |  |
| [[ALDH16A1]] | +0.58 | +0.58 / +0.28 | both halves | 3e-04 |  |
| [[RBM26-AS1]] | +0.58 | +0.66 / +0.26 | both halves | 3e-04 |  |
| [[RAD9B]] | +0.57 | +0.61 / +0.22 | both halves | 6e-04 |  |
| [[POGLUT1]] | +0.57 | +0.66 / +0.26 | both halves | 4e-04 |  |
| [[ACAD9-DT]] | +0.57 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[RCBTB2]] | +0.57 | +0.50 / +0.21 | both halves | 6e-04 |  |
| [[BANK1]] | +0.57 | +0.56 / +0.23 | both halves | 5e-04 |  |
| [[GPLD1]] | +0.56 | +0.65 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GET1]] | -0.56 | -0.65 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[LINC02935]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD27]] | -0.53 | -0.61 / -0.06 | ⚠ one half (not replicated) | 0.004 |  |
| [[TUSC2]] | -0.51 | -0.56 / -0.20 | both halves | 7e-04 |  |
| [[VRK3]] | -0.51 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[PCMT1]] | -0.51 | -0.66 / +0.12 | ⚠ one half (not replicated) | 1.00 |  |
| [[YIF1B]] | -0.51 | -0.56 / +0.11 | ⚠ one half (not replicated) | 1.00 |  |
| [[SBF2]] | -0.50 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[YIPF1]] | -0.50 | -0.52 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STOX1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[EMID1]] | B | EMID1 activity raises STOX1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without EMID1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[FAXC]] | B | FAXC activity raises STOX1's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without FAXC | 0.077 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[FAM169A]] | C | FAM169A activity raises STOX1's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 2.48× lower at baseline in the lines without FAM169A | 0.056 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX5]] | B | STOX1 activity raises SNX5's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without STOX1 | 0.053 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent |
| [[FAM174B]] | B | STOX1 activity raises FAM174B's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 1.64× lower at baseline in the lines without STOX1 | 0.064 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent |
| [[WNT3]] | B | STOX1 activity raises WNT3's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 1.80× lower at baseline in the lines without STOX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent |
| [[ZNF644]] | B | STOX1 activity raises ZNF644's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 1.24× lower at baseline in the lines without STOX1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent |
| [[FAIM]] | B | STOX1 activity raises FAIM's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 1.53× lower at baseline in the lines without STOX1 | 0.094 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent |
| [[FAM169A]] | C | STOX1 activity raises FAM169A's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 5.05× lower at baseline in the lines without STOX1 | 0.082 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.3, 32.3); signed map (31.0, -29.4). **Vector** length 69.8, 13.2% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +15.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.1 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +2.9 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.5 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -6.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | storkhead box 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:68,827,531-68,895,432 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25162; previously C10orf24 |
| Gene groups (HGNC) | Storkhead boxes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZVD7](https://www.uniprot.org/uniprotkb/Q6ZVD7) (Storkhead-box protein 1):

> Involved in regulating the levels of reactive oxidative species and reactive nitrogen species and in mitochondrial homeostasis in the placenta. Required for regulation of inner ear epithelial cell proliferation via the AKT signaling pathway (By similarity).; [Isoform A]: Involved in cell cycle regulation by binding to the CCNB1 promoter, up-regulating its expression and promoting mitotic entry. Induces phosphorylation of MAPT/tau.

**Summary**, from NCBI Gene [219736](https://www.ncbi.nlm.nih.gov/gene/219736):

> Enables RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Involved in several processes, including positive regulation of mitotic cell cycle phase transition; positive regulation of protein phosphorylation; and regulation of gene expression. Located in centrosome; cytosol; and nuclear lumen. Implicated in pre-eclampsia. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23508) · Entrez [219736](https://www.ncbi.nlm.nih.gov/gene/219736) · UniProt [Q6ZVD7](https://www.uniprot.org/uniprotkb/Q6ZVD7) · Ensembl [ENSG00000165730](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165730)

## Data

Gene col 9176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9176); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9176]; `tensor/DDL_lfc|DDL_z.npy` [9176]; `embed/gene_vectors.npy` [9176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9176 or target_col == 9176). Every well: [[STOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
