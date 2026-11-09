---
symbol: "RABGEF1P3"
type: "gene"
col: 13392
ensembl_id: "ENSG00000224273"
name: "RABGEF1 pseudogene 3"
location: "7q11.23"
module: 229
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 45
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/229"]
generated_by: "tahoemap"
---

# RABGEF1P3

*RABGEF1 pseudogene 3* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.26× (z +7.5, q 5e-11, up in 25 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.515× (z -6.1, q 7e-07, down in 24 of 40 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.563× (z -5.1, q 7e-05, down in 17 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V0D2]] (+0.68, fdr 7e-06), [[GCKR]] (+0.65, fdr 1e-05), [[NLRP1]] (+0.64, fdr 7e-06); moves opposite to [[ARMC8]] (-0.56, fdr 1e-05), [[MED13L]] (-0.54, fdr 2e-05), [[SORT1]] (-0.53, fdr 3e-05).
> It is in [[Module 229]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[KRT7]] → it (grade B ⚠); 9 go from it, the strongest it → [[ZNF229]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.26×** | +7.5 | 5e-11 | 25/39 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.08×** | +6.4 | 6e-08 | 19/35 (A498, H4, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +6.1 | 2e-07 | 12/34 (C32, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +5.7 | 2e-06 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +5.2 | 2e-05 | 20/38 (C32, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.2 | 2e-05 | 5/17 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +4.4 | 9e-04 | 8/31 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +4.2 | 0.002 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.52×** | +3.8 | 0.009 | 4/29 (J82, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.030 | 10/40 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.050 | 2/26 (SW480, SNU-423) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.515×** | -6.1 | 7e-07 | 24/40 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.557×** | -5.3 | 2e-05 | 19/37 (H4, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.563×** | -5.1 | 7e-05 | 17/40 (SNU-423, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -5.0 | 1e-04 | 16/39 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.574×** | -4.9 | 1e-04 | 17/37 (A549, H4, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.618×** | -4.4 | 0.001 | 13/37 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.717×** | -4.3 | 0.001 | 11/40 (H4, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.635×** | -4.2 | 0.002 | 19/39 (H4, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.625×** | -4.1 | 0.002 | 14/35 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -4.1 | 0.003 | 16/28 (SW 900, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.665×** | -3.7 | 0.010 | 7/40 (SK-MEL-2, HEC-1-A, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.686×** | -3.4 | 0.027 | 14/40 (SNU-423, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.669×** | -3.4 | 0.029 | 4/40 (LS 180, NCI-H23, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.700×** | -3.3 | 0.045 | 4/40 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.695×** | -3.2 | 0.052 | 10/24 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -3.0 | 0.084 | 11/38 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.792×** | -3.0 | 0.084 | 9/39 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -3.0 | 0.092 | 10/28 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 5.92 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0397× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.0697× (z -9.0) |
| [[H4 (line)]] | wt | 11.7 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0322× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 3.30 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0697× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 5.25 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0513× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 3.13 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0879× (z -8.6) |
| [[A-172 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.900 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0D2]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[GCKR]] | +0.65 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[NLRP1]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[LINC01705]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TM4SF19]] | +0.58 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[GGT1]] | +0.56 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[MYH16]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PDE2A]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NRIP3]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SLC51A]] | +0.52 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[C9orf24]] | +0.51 | +0.58 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.56 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[MED13L]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SORT1]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ARHGAP17]] | -0.53 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[STOM]] | -0.52 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[SSBP2]] | -0.51 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[PDLIM1]] | -0.51 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[CAV1]] | -0.50 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[CCND3]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[NFIB]] | -0.49 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[KLF9]] | -0.49 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[MBNL1]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT7]] | B | KRT7 activity raises RABGEF1P3's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.35× lower at baseline in the lines without KRT7 | 0.012 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[GTF2IP7]] | B | GTF2IP7 activity raises RABGEF1P3's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without GTF2IP7 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | B | TM4SF19, TM4SF19-DYNLT2B activity raises RABGEF1P3's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.70× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[ANXA10]] | B | ANXA10 activity raises RABGEF1P3's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.32× lower at baseline in the lines without ANXA10 | 0.062 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[BACE2]] | B | BACE2 activity raises RABGEF1P3's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without BACE2 | 0.067 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[ATP6V0D2]] | B | ATP6V0D2 activity raises RABGEF1P3's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without ATP6V0D2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[CRTAC1]] | B | CRTAC1 activity raises RABGEF1P3's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 1.44× lower at baseline in the lines without CRTAC1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF229]] | B | RABGEF1P3 activity raises ZNF229's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without RABGEF1P3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[SAMD1]] | B | RABGEF1P3 activity lowers SAMD1's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 2.09× higher at baseline in the lines without RABGEF1P3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[SAMD11]] | B | RABGEF1P3 activity lowers SAMD11's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 5.13× higher at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[TM4SF19]] | B | RABGEF1P3 activity raises TM4SF19's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 4.91× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[BACE2]] | B | RABGEF1P3 activity raises BACE2's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 3.88× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[DGKG]] | B | RABGEF1P3 activity raises DGKG's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 2.90× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[TVP23C]] | B | RABGEF1P3 activity raises TVP23C's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[SPAG5-AS1]] | B | RABGEF1P3 activity raises SPAG5-AS1's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 1.26× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[NIPAL1]] | B | RABGEF1P3 activity raises NIPAL1's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 2.67× lower at baseline in the lines without RABGEF1P3 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 229]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.835). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.6, -2.7); signed map (14.2, 53.4). **Vector** length 61.9, 9.97% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.7 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +6.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.9 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.6 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | RABGEF1 pseudogene 3 |
| Locus type | pseudogene |
| Location | 7q11.23 — chr7:76,108,434-76,132,187 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55753) · Entrez [122149305](https://www.ncbi.nlm.nih.gov/gene/122149305) · Ensembl [ENSG00000224273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224273)

## Data

Gene col 13392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13392); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13392]; `tensor/DDL_lfc|DDL_z.npy` [13392]; `embed/gene_vectors.npy` [13392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13392 or target_col == 13392). Every well: [[RABGEF1P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABGEF1P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
