---
symbol: "CYBC1"
type: "gene"
col: 10975
ensembl_id: "ENSG00000178927"
name: "cytochrome b-245 chaperone 1"
location: "17q25.3"
module: 7
arm: "+"
pooled_cpm: 12.48
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CYBC1

*cytochrome b-245 chaperone 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.59× (z +5.4, q 3e-05, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.270× (z -21.5, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM127]] (+0.53, fdr 4e-05), [[ARSA]] (+0.53, fdr 5e-05), [[MPI]] (+0.53, fdr 1e-05); moves opposite to [[GRK7]] (-0.50, fdr 8e-05), [[TBCE-1]] (-0.50, fdr 1e-04), [[LINC01030]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +5.4 | 3e-05 | 25/47 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +4.8 | 4e-04 | 22/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +4.3 | 0.004 | 20/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.006 | 20/47 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.032 | 12/44 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.032 | 18/47 (SNU-423, HOP62, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.033 | 15/46 (CFPAC-1, PANC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.074 | 15/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.30× | +3.1 | 0.13 | 11/41 (HOP62, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.270×** | -21.5 | 0e+00 | 44/47 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.357×** | -11.9 | 2e-30 | 43/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.365×** | -11.7 | 3e-29 | 40/45 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.392×** | -10.9 | 3e-25 | 39/45 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.406×** | -10.4 | 2e-23 | 39/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.454×** | -9.2 | 5e-18 | 35/47 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.446×** | -9.0 | 2e-17 | 40/46 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.230×** | -8.9 | 4e-17 | 38/43 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.256×** | -8.2 | 1e-14 | 37/47 (PANC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.542×** | -6.8 | 5e-10 | 29/41 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.575×** | -6.4 | 8e-09 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -5.4 | 4e-06 | 25/47 (RKO, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -4.8 | 8e-05 | 24/47 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.671×** | -4.6 | 2e-04 | 20/46 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.695×** | -4.0 | 0.003 | 17/46 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.004 | 15/47 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.742×** | -3.4 | 0.016 | 11/47 (RKO, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 16.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0420× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 11.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -16.3) |
| [[PANC-1 (line)]] | alt | 20.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -16.6) |
| [[LoVo (line)]] | wt | 9.89 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0381× (z -18.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.197× (z -13.2) |
| [[SW480 (line)]] | alt | 13.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.156× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 5.41 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -11.1) |
| [[A-427 (line)]] | wt | 22.9 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0733× (z -9.5) |
| [[KATO III (line)]] | alt | 23.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -17.2) |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0369× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 9.78 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -8.9) |
| [[SW 900 (line)]] | alt | 9.60 | 0 | 3 | — | [[Digitoxin (drug)]] 0.05 µM 0.0446× (z -12.3) |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -9.4) |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -10.3) |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0978× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Bendamustine (drug)]] 5 µM 0.0946× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.126× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 9.92 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.153× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -9.0) |
| [[RKO (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0719× (z -11.1) |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 23.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -17.2) |
| [[A-172 (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.2) |
| [[A549 (line)]] | wt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 7.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0867× (z -9.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 9.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -13.4) |
| [[H4 (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -8.7) |
| [[HOP62 (line)]] | alt | 7.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -10.0) |
| [[HS-578T (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.129× (z -9.4) ⚠ transcription drop |
| [[J82 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.1) |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0666× (z -10.4) |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -9.9) |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.9) |
| [[SW48 (line)]] | wt | 8.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0724× (z -11.3) |
| [[A498 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM127]] | +0.53 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[ARSA]] | +0.53 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[MPI]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[C6orf47]] | +0.52 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[LRRC14]] | +0.52 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[KCTD17]] | +0.52 | +0.58 / +0.31 | both halves | 2e-04 |  |
| [[RIC8A]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[SIPA1]] | +0.52 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[EIF4A3]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[MEA1]] | +0.51 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[CTXN1]] | +0.51 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[BORCS8]] | +0.51 | +0.36 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK7]] | -0.50 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[TBCE-1]] | -0.50 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[LINC01030]] | -0.49 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[LINC00486]] | -0.48 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[FAM184B]] | -0.48 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[PIWIL2]] | -0.46 | -0.40 / -0.29 | both halves | 3e-04 |  |
| [[FBXO4]] | -0.46 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[CDKL1]] | -0.46 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[NDUFS1]] | -0.46 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[LRRC66]] | -0.46 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[CC2D2A]] | -0.45 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[TRMT13]] | -0.45 | -0.33 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CYBC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.183). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (13.5, -12.4); signed map (-37.0, 16.7). **Vector** length 63.6, 11.5% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.6 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.3 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | -2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -21.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | -1.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b-245 chaperone 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,440,912-82,450,829 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4368, FLJ90469, Eros; previously C17orf62 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQA9](https://www.uniprot.org/uniprotkb/Q9BQA9) (Cytochrome b-245 chaperone 1):

> Functions as a chaperone necessary for a stable expression of the CYBA and CYBB subunits of the cytochrome b-245 heterodimer. Controls the phagocyte respiratory burst and is essential for innate immunity (By similarity).

**Summary**, from NCBI Gene [79415](https://www.ncbi.nlm.nih.gov/gene/79415):

> Involved in innate immune response and respiratory burst after phagocytosis. Located in endoplasmic reticulum. Implicated in autosomal recessive chronic granulomatous disease 5. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28672) · Entrez [79415](https://www.ncbi.nlm.nih.gov/gene/79415) · UniProt [Q9BQA9](https://www.uniprot.org/uniprotkb/Q9BQA9) · Ensembl [ENSG00000178927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178927)

## Data

Gene col 10975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10975); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10975]; `tensor/DDL_lfc|DDL_z.npy` [10975]; `embed/gene_vectors.npy` [10975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10975 or target_col == 10975). Every well: [[CYBC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYBC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
