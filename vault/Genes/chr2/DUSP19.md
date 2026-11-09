---
symbol: "DUSP19"
type: "gene"
col: 8614
ensembl_id: "ENSG00000162999"
name: "dual specificity phosphatase 19"
location: "2q32.1"
module: 16
arm: "+"
pooled_cpm: 2.75
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 17
n_dd_up_clean: 17
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# DUSP19

*dual specificity phosphatase 19* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.97× (z +8.7, q 2e-15, up in 7 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.06× (z +8.4, q 1e-14, up in 24 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.358× (z -8.4, q 2e-14, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC30A]] (+0.73, fdr 7e-06), [[OSGEPL1]] (+0.62, fdr 1e-05), [[BDH2]] (+0.61, fdr 7e-06); moves opposite to [[LMBR1]] (-0.57, fdr 3e-05), [[C19orf25]] (-0.57, fdr 1e-05), [[CORO7]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FBXO15]] → it (grade B ⚠); 4 go from it, the strongest it → [[PRDX6-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +8.7 | 2e-15 | 7/9 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.06×** | +8.4 | 1e-14 | 24/41 (RKO, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +7.3 | 6e-11 | 2/4 (NCI-H2030, LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +6.4 | 3e-08 | 2/3 (NCI-H2030, PANC-1) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.12×** | +6.2 | 7e-08 | 23/42 (PANC-1, A-172, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.2 | 2e-05 | 13/30 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +4.6 | 4e-04 | 12/40 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.77×** | +4.6 | 4e-04 | 9/30 (A498, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.72×** | +4.4 | 8e-04 | 11/38 (NCI-H2030, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.002 | 9/39 (A498, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.61×** | +3.9 | 0.005 | 10/39 (HEC-1-A, PANC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.015 | 7/42 (A498, HEC-1-A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.016 | 4/35 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.52×** | +3.5 | 0.021 | 6/36 (PANC-1, LoVo, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.032 | 4/36 (A-172, NCI-H1792, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.054 | 5/38 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.054 | 8/41 (SW480, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.058 | 6/37 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.086 | 4/39 (A-427, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8614.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.358×** | -8.4 | 2e-14 | 26/36 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.364×** | -8.3 | 3e-14 | 28/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.397×** | -7.6 | 6e-12 | 27/38 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -6.8 | 2e-09 | 19/22 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.519×** | -5.4 | 8e-06 | 15/37 (LoVo, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.521×** | -5.3 | 8e-06 | 16/35 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -5.3 | 1e-05 | 19/41 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.552×** | -4.9 | 8e-05 | 16/41 (J82, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.581×** | -4.4 | 5e-04 | 13/42 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.576×** | -4.3 | 0.001 | 11/36 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.607×** | -4.1 | 0.002 | 16/43 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.710×** | -4.0 | 0.004 | 19/39 (Panc 03.27, SHP-77, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.628×** | -3.8 | 0.006 | 9/37 (SW 900, CHP-212, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.638×** | -3.7 | 0.010 | 11/42 (H4, SW 1271, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.640×** | -3.6 | 0.010 | 13/37 (RPMI-7951, PANC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.676×** | -3.1 | 0.071 | 7/39 (HT-29, SNU-1, …) | two highest doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.688×** | -3.1 | 0.076 | 11/30 (Hs 766T, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 7.93 | 0 | 4 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.134× (z -8.7) |
| [[A-427 (line)]] | wt | 5.63 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0923× (z -9.7) |
| [[Hs 766T (line)]] | wt | 3.38 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0276× (z -10.6) |
| [[PANC-1 (line)]] | alt | 3.53 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0474× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0892× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 6.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 6.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0994× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.89 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0520× (z -10.5) |
| [[SHP-77 (line)]] | alt | 9.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0945× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 4.13 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0497× (z -8.5) |
| [[A-172 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.840 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC30A]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[OSGEPL1]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[BDH2]] | +0.61 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[DPY19L2P2-1]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[LRRIQ3]] | +0.60 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CRISPLD1]] | +0.60 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[NUDT6]] | +0.59 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ID2-AS1]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[RBM7]] | +0.57 | +0.46 / +0.46 | both halves | 2e-05 |  |
| [[C2orf74-DT]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[AMACR]] | +0.56 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[BBS10]] | +0.56 | +0.67 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[C19orf25]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CORO7]] | -0.56 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NFATC2IP]] | -0.56 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[MUC20-OT1]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[RSKR]] | -0.55 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[MROH1]] | -0.55 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[DAP3]] | -0.55 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ZNF778]] | -0.55 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[TPTEP2-CSNK1E]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GAN]] | -0.53 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ATP6V0A2]] | -0.53 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO15]] | B | FBXO15 activity raises DUSP19's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without FBXO15 | 0.017 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[CALCRL]] | B | CALCRL activity raises DUSP19's level | lines that do not express CALCRL (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without CALCRL | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000259363, NRG1, SPOCK3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers DUSP19's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[KATNAL2]] | B | KATNAL2 activity raises DUSP19's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without KATNAL2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises DUSP19's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without SYT9-AS1 | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LRRIQ3]] | C | LRRIQ3 activity raises DUSP19's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDX6-AS1]] | C | DUSP19 activity raises PRDX6-AS1's level | lines that do not express DUSP19 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without DUSP19 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[LRRIQ3]] | C | DUSP19 activity raises LRRIQ3's level | lines that do not express DUSP19 (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without DUSP19 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[ATRAID]] | C | DUSP19 activity raises ATRAID's level | lines that do not express DUSP19 (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without DUSP19 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |
| [[EIF1B-AS1]] | C | [[CCDC171]], DUSP19, [[RFX3-DT]] activity raises EIF1B-AS1's level | lines that do not express CCDC171, DUSP19, RFX3-DT (3) vs lines expressing them (47) | 2.62× lower at baseline in the lines without CCDC171, DUSP19, RFX3-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.1, 20.4); signed map (10.0, -40.0). **Vector** length 51.0, 7.40% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -5.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -5.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.9 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:183,078,559-183,100,008 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SKRP1, DUSP17 |
| Gene groups (HGNC) | Atypical dual specificity phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTR2](https://www.uniprot.org/uniprotkb/Q8WTR2) (Dual specificity protein phosphatase 19):

> Has a dual specificity toward Ser/Thr and Tyr-containing proteins.

**Summary**, from NCBI Gene [142679](https://www.ncbi.nlm.nih.gov/gene/142679):

> Dual-specificity phosphatases (DUSPs) constitute a large heterogeneous subgroup of the type I cysteine-based protein-tyrosine phosphatase superfamily. DUSPs are characterized by their ability to dephosphorylate both tyrosine and serine/threonine residues. They have been implicated as major modulators of critical signaling pathways. DUSP19 contains a variation of the consensus DUSP C-terminal catalytic domain, with the last serine residue replaced by alanine, and lacks the N-terminal CH2 domain …

**Accessions** — [HGNC:18894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18894) · Entrez [142679](https://www.ncbi.nlm.nih.gov/gene/142679) · UniProt [Q8WTR2](https://www.uniprot.org/uniprotkb/Q8WTR2) · Ensembl [ENSG00000162999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162999)

## Data

Gene col 8614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8614); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8614]; `tensor/DDL_lfc|DDL_z.npy` [8614]; `embed/gene_vectors.npy` [8614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8614 or target_col == 8614). Every well: [[DUSP19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
