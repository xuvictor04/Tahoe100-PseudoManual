---
symbol: "MARK1"
type: "gene"
col: 3767
ensembl_id: "ENSG00000116141"
name: "microtubule affinity regulating kinase 1"
location: "1q41"
module: 124
arm: "+"
pooled_cpm: 15.03
n_lines_expressing: 26
n_dd_up: 38
n_dd_down: 5
n_dd_up_clean: 29
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# MARK1

*microtubule affinity regulating kinase 1* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +15.9, q 0e+00, up in 16 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.560× (z -10.2, q 2e-21, down in 16 of 23 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP46]] (+0.64, fdr 1e-05), [[KIF21A]] (+0.59, fdr 4e-05), [[POU6F1]] (+0.58, fdr 1e-04); moves opposite to [[PRPF3]] (-0.52, fdr 3e-04), [[ALDH6A1]] (-0.50, fdr 9e-05), [[CHPF]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRKG1]] → it (grade C ⚠); 3 go from it, the strongest it → [[HDGFL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +15.9 | 0e+00 | 16/22 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +15.5 | 0e+00 | 9/23 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.23×** | +14.0 | 2e-42 | 22/23 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.08×** | +12.1 | 1e-31 | 22/23 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +12.0 | 5e-31 | 11/23 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.95×** | +11.6 | 2e-29 | 21/23 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +10.1 | 6e-22 | 10/23 (NCI-H460, A-427, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +9.4 | 6e-19 | 13/22 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.8 | 6e-17 | 12/23 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +8.1 | 3e-14 | 14/22 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.4 | 6e-12 | 12/22 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.3 | 1e-11 | 1/20 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +7.2 | 3e-11 | 12/23 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +6.9 | 3e-10 | 10/22 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +6.7 | 8e-10 | 16/23 (BT-474, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.64×** | +6.2 | 2e-08 | 8/23 (HOP62, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +6.1 | 2e-08 | 15/23 (BT-474, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 1e-06 | 16/23 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 2e-05 | 14/23 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3767.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.560×** | -10.2 | 2e-21 | 16/23 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.647×** | -7.6 | 7e-12 | 18/23 (SHP-77, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.809×** | -3.6 | 0.064 | 9/23 (C-33 A, J82, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.814×** | -3.5 | 0.070 | 2/23 (J82, NCI-H2030) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -3.3 | 0.082 | 1/24 (HOP62) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.827×** | -3.3 | 0.082 | 4/23 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Rosiglitazone (drug)]] 0.05 µM |  | 0.820× | -3.2 | 0.11 | 3/23 (BT-474, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 50.6 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.176× (z -16.4) |
| [[NCI-H460 (line)]] | wt | 8.29 | 7 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.31× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 105 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.196× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 63.1 | 2 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.82× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0988× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.360× (z -9.0) |
| [[A498 (line)]] | wt | 7.14 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.56× (z +17.2) | — |
| [[H4 (line)]] | wt | 26.9 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 8.12× (z +10.1) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0720× (z -11.7) |
| [[SHP-77 (line)]] | alt | 181 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -25.3) |
| [[LOX-IMVI (line)]] | wt | 39.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -16.9) |
| [[SW480 (line)]] | alt | 11.6 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.240× (z -10.5) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.250× (z -10.2) |
| [[BT-474 (line)]] | alt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 9.75 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.53× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 28.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.99× (z +10.5) | — |
| [[A-427 (line)]] | wt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.36× (z +12.0) | — |
| [[CHP-212 (line)]] | wt | 52.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0980× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 9.09 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0782× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +9.9) | — |
| [[A-172 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.16 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP46]] | +0.64 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[KIF21A]] | +0.59 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[POU6F1]] | +0.58 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[HDGFL3]] | +0.57 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[BEND7]] | +0.57 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[ADAM23]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RUFY3]] | +0.56 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[PYGO1]] | +0.56 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[MIER3]] | +0.55 | +0.47 / +0.27 | both halves | 3e-04 |  |
| [[UST]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[PLEKHA5]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[FBXO30]] | +0.54 | +0.54 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF3]] | -0.52 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[ALDH6A1]] | -0.50 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[CHPF]] | -0.49 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[MMUT]] | -0.49 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[IFT172]] | -0.49 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[RAB3A]] | -0.49 | -0.41 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[UTP6]] | -0.47 | -0.49 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[HPCAL1]] | -0.46 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[FAM234A]] | -0.46 | -0.38 / -0.29 | both halves | 3e-04 |  |
| [[MARF1]] | -0.46 | -0.43 / -0.29 | both halves | 3e-04 |  |
| [[CREB3L2]] | -0.45 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[SENP2]] | -0.45 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[KIAA0319L]] | -0.44 | -0.31 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKG1]] | C | PRKG1 activity raises MARK1's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without PRKG1 | 0.066 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDGFL3]] | B | MARK1 activity raises HDGFL3's level | lines that do not express MARK1 (24) vs lines expressing it (26) | 2.91× lower at baseline in the lines without MARK1 | 0.018 | ⚠ within organs, on part of the lines; also absent: FXYD6, COL4A4, ENSG00000283982 |
| [[NUTM2B-AS1]] | B | MARK1 activity raises NUTM2B-AS1's level | lines that do not express MARK1 (24) vs lines expressing it (26) | 1.24× lower at baseline in the lines without MARK1 | 0.047 | ⚠ within organs, on part of the lines; also absent: FXYD6, COL4A4, ENSG00000283982 |
| [[MACROH2A2]] | B | MARK1 activity raises MACROH2A2's level | lines that do not express MARK1 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without MARK1 | 0.085 | ⚠ within organs, on part of the lines; also absent: FXYD6, COL4A4, ENSG00000283982 |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-14.4, 12.0); signed map (11.4, -6.3). **Vector** length 65.9, 16.2% of its response variance represented; |z| ≥ 3 in 586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +6.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -10.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -2.2 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | +0.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | microtubule affinity regulating kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:220,528,136-220,664,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MARK, PAR-1C |
| Gene groups (HGNC) | Microtubule affinity regulating kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0L2](https://www.uniprot.org/uniprotkb/Q9P0L2) (Serine/threonine-protein kinase MARK1):

> Serine/threonine-protein kinase. Involved in cell polarity and microtubule dynamics regulation. Phosphorylates DCX, MAP2 and MAP4. Phosphorylates the microtubule-associated protein MAPT/TAU. Involved in cell polarity by phosphorylating the microtubule-associated proteins MAP2, MAP4 and MAPT/TAU at KXGS motifs, causing detachment from microtubules, and their disassembly. Involved in the regulation of neuronal migration through its dual activities in regulating cellular polarity and microtubule …

**Summary**, from NCBI Gene [4139](https://www.ncbi.nlm.nih.gov/gene/4139):

> Enables anion binding activity; magnesium ion binding activity; and tau-protein kinase activity. Involved in intracellular signal transduction; negative regulation of epithelial to mesenchymal transition; and protein phosphorylation. Located in cytoplasm; dendrite; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6896) · Entrez [4139](https://www.ncbi.nlm.nih.gov/gene/4139) · UniProt [Q9P0L2](https://www.uniprot.org/uniprotkb/Q9P0L2) · Ensembl [ENSG00000116141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116141)

## Data

Gene col 3767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3767); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3767]; `tensor/DDL_lfc|DDL_z.npy` [3767]; `embed/gene_vectors.npy` [3767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3767 or target_col == 3767). Every well: [[MARK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
