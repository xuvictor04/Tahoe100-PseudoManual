---
symbol: "CREB3L1"
type: "gene"
col: 8089
ensembl_id: "ENSG00000157613"
name: "cAMP responsive element binding protein 3 like 1"
location: "11p11.2"
module: 44
arm: "+"
pooled_cpm: 20.24
n_lines_expressing: 26
n_dd_up: 18
n_dd_down: 21
n_dd_up_clean: 16
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 18
direction_downstream: 27
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CREB3L1

*cAMP responsive element binding protein 3 like 1* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +10.9, q 4e-25, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.398× (z -12.7, q 3e-34, down in 21 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGT1A6]] (+0.57, fdr 7e-06), [[NXPH4]] (+0.53, fdr 3e-05), [[UGT1A1]] (+0.53, fdr 2e-05); moves opposite to [[JPX]] (-0.51, fdr 3e-05), [[CMTM3]] (-0.44, fdr 1e-04), [[ZC3H12C]] (-0.44, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[SPARC]] → it (grade B ⚠); 27 go from it, the strongest it → [[SLC6A8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +10.9 | 4e-25 | 15/23 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.3 | 8e-11 | 9/24 (Panc 03.27, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.2 | 1e-07 | 4/22 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.0 | 2e-07 | 2/17 (SNU-423, HOP62) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 2e-05 | 10/24 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.0 | 5e-05 | 9/24 (Panc 03.27, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.9 | 8e-05 | 13/23 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +4.8 | 1e-04 | 10/24 (Panc 03.27, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 2e-04 | 11/24 (HOP62, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 2e-04 | 9/24 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.002 | 12/23 (HOP62, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.002 | 6/24 (Panc 03.27, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.002 | 8/24 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.005 | 11/24 (HOP62, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.019 | 10/24 (HOP62, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.045 | 3/24 (Panc 03.27, SNU-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.045 | 4/24 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8089.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.398×** | -12.7 | 3e-34 | 21/24 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.493×** | -10.2 | 8e-22 | 21/24 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.511×** | -9.6 | 1e-19 | 16/22 (A-172, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.538×** | -8.9 | 8e-17 | 20/24 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.549×** | -8.6 | 8e-16 | 18/24 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.625×** | -6.7 | 2e-09 | 18/24 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.647×** | -6.3 | 3e-08 | 13/23 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -6.1 | 8e-08 | 19/24 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.685×** | -5.4 | 3e-06 | 16/24 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -5.2 | 1e-05 | 17/24 (LS 180, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.704×** | -4.8 | 1e-04 | 14/24 (HT-29, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.576×** | -4.1 | 0.002 | 13/24 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.754×** | -4.1 | 0.002 | 7/24 (SNU-423, SHP-77, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.760×** | -3.9 | 0.003 | 13/24 (A-172, HS-578T, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.764×** | -3.9 | 0.004 | 10/24 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.760×** | -3.8 | 0.005 | 1/23 (COLO 205) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 42.6 | 9 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.60× (z +13.7) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 4.23× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 50.8 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -12.7) |
| [[Hs 766T (line)]] | wt | 52.6 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0922× (z -15.4) |
| [[HT-29 (line)]] | alt | 159 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -11.0) |
| [[A-172 (line)]] | wt | 78.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -20.8) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -16.4) |
| [[HS-578T (line)]] | alt | 50.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 27.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.0) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0852× (z -8.6) |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0851× (z -10.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.37 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.103× (z -8.6) |
| [[SNU-423 (line)]] | alt | 64.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.6) | — |
| [[A-427 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGT1A6]] | +0.57 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[NXPH4]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[UGT1A1]] | +0.53 | +0.57 / +0.49 | both halves | 2e-05 |  |
| [[SEMA5A]] | +0.52 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[SNHG18]] | +0.52 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[COL1A1]] | +0.52 | +0.38 / +0.51 | both halves | 6e-05 | STRING 587 |
| [[LRP1]] | +0.51 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[NID2]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SLC6A8]] | +0.51 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[UGT1A9]] | +0.51 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[NR3C2]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPX]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CMTM3]] | -0.44 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[ZC3H12C]] | -0.44 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[MTHFD2L]] | -0.44 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[ZBTB38]] | -0.44 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[HMGA2]] | -0.43 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ATXN7L1]] | -0.43 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[ADAMTS9]] | -0.42 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[ZFPM2-AS1]] | -0.42 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[TANGO6]] | -0.42 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[TPK1]] | -0.41 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[ZNF839]] | -0.41 | -0.29 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 6, C 12. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPARC]] | B | SPARC activity raises CREB3L1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.17× lower at baseline in the lines without SPARC | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CREB3L1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[CASZ1]] | B | CASZ1 activity lowers CREB3L1's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 3.09× higher at baseline in the lines without CASZ1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[DKK3]] | B | DKK3 activity raises CREB3L1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.57× lower at baseline in the lines without DKK3 | 0.058 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[CPPED1]] | B | CPPED1 activity lowers CREB3L1's level | lines that do not express CPPED1 (5) vs lines expressing it (45) | 4.61× higher at baseline in the lines without CPPED1 | 0.068 | ⚠ within organs, on part of the lines; also absent: CCDC144CP |
| [[CXXC5]] | B | CXXC5 activity raises CREB3L1's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 3.14× lower at baseline in the lines without CXXC5 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[COL1A1]] | C | COL1A1 activity raises CREB3L1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 3.87× lower at baseline in the lines without COL1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises CREB3L1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 5.27× lower at baseline in the lines without COL1A2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[UGT1A8]], [[UGT1A9]] | C | UGT1A8, UGT1A9 activity raises CREB3L1's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 4.35× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.014 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[UGT1A6]] | C | UGT1A6 activity raises CREB3L1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 4.23× lower at baseline in the lines without UGT1A6 | 0.014 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises CREB3L1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.39× lower at baseline in the lines without COL5A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[FGFR2]] | C | FGFR2 activity raises CREB3L1's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 3.94× lower at baseline in the lines without FGFR2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 18, C 9. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC6A8]] | B | CREB3L1 activity weakens SLC6A8's drug response | lines that do not express CREB3L1 (23) vs lines expressing it (21) | the lines without CREB3L1 respond 1.13× as strongly (z diff -0.21); strongest at Idarubicin (hydrochloride) 5 µM: 1.92x vs 1.14x (z diff -3.9) | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; target measured in part of the lines; both ways; artifact flags |
| [[SPARC]] | B | CREB3L1 activity raises SPARC's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without CREB3L1 | 0.012 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[DNM2]] | B | CREB3L1 activity raises DNM2's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.27× lower at baseline in the lines without CREB3L1 | 0.028 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[ABHD12]] | B | CREB3L1 activity raises ABHD12's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.48× lower at baseline in the lines without CREB3L1 | 0.032 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[ZNF710-AS1]] | B | CREB3L1 activity raises ZNF710-AS1's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.43× lower at baseline in the lines without CREB3L1 | 0.032 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[ABHD12]] | B | CREB3L1 activity weakens ABHD12's drug response | lines that do not express CREB3L1 (24) vs lines expressing it (25) | the lines without CREB3L1 respond 1.39× as strongly (z diff -0.89); strongest at Idarubicin (hydrochloride) 5 µM: 1.38x vs 1.05x (z diff -3.1) | 0.036 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; target measured in part of the lines; artifact flags |
| [[PDXDC2P]] | B | CREB3L1 activity raises PDXDC2P's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without CREB3L1 | 0.048 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[LRIG1]] | B | CREB3L1 activity raises LRIG1's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 2.27× lower at baseline in the lines without CREB3L1 | 0.050 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[PRR15L]] | B | CREB3L1 activity raises PRR15L's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without CREB3L1 | 0.051 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[ZBTB7C]] | B | CREB3L1 activity raises ZBTB7C's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.91× lower at baseline in the lines without CREB3L1 | 0.058 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[PDXDC2P]] | B | CREB3L1 activity strengthens PDXDC2P's drug response | lines that do not express CREB3L1 (24) vs lines expressing it (25) | the lines without CREB3L1 respond 0.74× as strongly (z diff +1.90); strongest at Homoharringtonine 0.5 µM: 0.53x vs 0.34x (z diff +3.4) | 0.059 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; target measured in part of the lines; artifact flags |
| [[CAPN5]] | B | CREB3L1 activity raises CAPN5's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.77× lower at baseline in the lines without CREB3L1 | 0.062 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (60.2, 21.9); signed map (67.5, -3.0). **Vector** length 74.2, 19.3% of its response variance represented; |z| ≥ 3 in 707 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.52 to 4); *Aspirin ADME* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +10.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.2 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -6.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cAMP responsive element binding protein 3 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,277,662-46,321,409 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OASIS |
| Gene groups (HGNC) | CREB3 transcription factor family |
| Reactome | 4 pathways, smallest: CREB3 factors activate genes; Unfolded Protein Response (UPR); Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BA8](https://www.uniprot.org/uniprotkb/Q96BA8) (Cyclic AMP-responsive element-binding protein 3-like protein 1):

> [Cyclic AMP-responsive element-binding protein 3-like protein 1]: Precursor of the transcription factor form (Processed cyclic AMP-responsive element-binding protein 3-like protein 1), which is embedded in the endoplasmic reticulum membrane with N-terminal DNA-binding and transcription activation domains oriented toward the cytosolic face of the membrane. In response to ER stress or DNA damage, transported to the Golgi, where it is cleaved in a site-specific manner by resident proteases …

**Summary**, from NCBI Gene [90993](https://www.ncbi.nlm.nih.gov/gene/90993):

> The protein encoded by this gene is normally found in the membrane of the endoplasmic reticulum (ER). However, upon stress to the ER, the encoded protein is cleaved and the released cytoplasmic transcription factor domain translocates to the nucleus. There it activates the transcription of target genes by binding to box-B elements. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:18856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18856) · Entrez [90993](https://www.ncbi.nlm.nih.gov/gene/90993) · UniProt [Q96BA8](https://www.uniprot.org/uniprotkb/Q96BA8) · Ensembl [ENSG00000157613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157613)

## Data

Gene col 8089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8089); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8089]; `tensor/DDL_lfc|DDL_z.npy` [8089]; `embed/gene_vectors.npy` [8089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8089 or target_col == 8089). Every well: [[CREB3L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREB3L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
