---
symbol: "POLR3E"
type: "gene"
col: 663
ensembl_id: "ENSG00000058600"
name: "RNA polymerase III subunit E"
location: "16p12.2"
module: 18
arm: "+"
pooled_cpm: 24.61
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# POLR3E

*RNA polymerase III subunit E* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.00× (z +17.6, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.700× (z -12.9, q 3e-35, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LETM1]] (+0.72, fdr 7e-06), [[WDR4]] (+0.69, fdr 7e-06), [[LYRM4]] (+0.69, fdr 7e-06); moves opposite to [[KMT2E]] (-0.61, fdr 1e-05), [[MARCKS]] (-0.56, fdr 1e-05), [[RYBP]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CHGB]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ATR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 663.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.00×** | +17.6 | 0e+00 | 42/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.06×** | +17.3 | 0e+00 | 41/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.94×** | +16.8 | 0e+00 | 38/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +8.1 | 1e-13 | 18/40 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +7.1 | 2e-10 | 22/47 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +6.8 | 1e-09 | 17/48 (PANC-1, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +6.1 | 8e-08 | 22/46 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +5.7 | 7e-07 | 15/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +5.4 | 5e-06 | 18/47 (CFPAC-1, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.8 | 1e-04 | 16/34 (SW 900, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 4e-04 | 16/47 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.39×** | +4.4 | 6e-04 | 7/45 (J82, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +4.3 | 6e-04 | 7/47 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.12× | +3.9 | 0.003 | 3/48 (SNU-1, LoVo, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.10× | +3.4 | 0.022 | 6/48 (SHP-77, H4, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.032 | 6/46 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.037 | 6/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.042 | 5/45 (NCI-H460, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.13× | +3.0 | 0.081 | 2/48 (Hs 766T, NCI-H1573) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.700×** | -12.9 | 3e-35 | 27/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.725×** | -11.7 | 5e-29 | 30/48 (J82, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.649×** | -10.6 | 4e-24 | 26/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.753×** | -7.3 | 5e-11 | 23/47 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.754×** | -7.3 | 5e-11 | 25/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.762×** | -7.0 | 3e-10 | 21/48 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -6.1 | 9e-08 | 20/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.790×** | -6.1 | 9e-08 | 18/47 (A498, SW48, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.802×** | -5.7 | 9e-07 | 14/47 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.837× | -4.6 | 2e-04 | 9/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -4.4 | 5e-04 | 17/48 (LS 180, J82, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.857× | -4.0 | 0.003 | 13/47 (A-427, RKO, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 0.852× | -4.0 | 0.003 | 14/46 (HepG2/C3A, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -3.8 | 0.005 | 6/48 (Hs 766T, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.862× | -3.8 | 0.005 | 9/48 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.859× | -3.8 | 0.006 | 9/48 (CHP-212, NCI-H2030, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.815×** | -3.8 | 0.006 | 9/47 (HS-578T, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.862× | -3.6 | 0.012 | 7/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.870× | -3.5 | 0.017 | 12/45 (SW1417, C32, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.878× | -3.2 | 0.033 | 11/47 (MIA PaCa-2, BT-474, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.4 | 2 | 3 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.67× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.8) |
| [[J82 (line)]] | alt | 24.9 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.340× (z -13.4) |
| [[A498 (line)]] | wt | 41.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 24.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.87× (z +10.7) | — |
| [[RKO (line)]] | wt | 38.4 | 0 | 3 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0818× (z -10.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.475× (z -8.5) |
| [[A-427 (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.313× (z -9.7) |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 2 | — | [[Methotrexate (drug)]] 0.5 µM 0.0561× (z -11.6) |
| [[A549 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -14.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[CHP-212 (line)]] | wt | 24.5 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0879× (z -8.5) |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0844× (z -11.2) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 36.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 29.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.483× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.240× (z -10.0) |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SW48 (line)]] | wt | 37.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -10.4) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SW480 (line)]] | alt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -9.4) |
| [[A-172 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LETM1]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[WDR4]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[LYRM4]] | +0.69 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[URB1]] | +0.68 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.67 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[DDX54]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[NAA25]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[TWNK]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[GART]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[POMT2]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PUS1]] | +0.65 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[LIG3]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2E]] | -0.61 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[MARCKS]] | -0.56 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[RYBP]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[MEF2A]] | -0.56 | -0.44 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHGB]] | B | CHGB activity raises POLR3E's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.28× lower at baseline in the lines without CHGB | 0.053 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[KCTD15]] | B | KCTD15 activity raises POLR3E's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without KCTD15 | 0.084 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATR]] | C | POLR3E's natural level weakens ATR's drug response | POLR3E's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.36; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.4, -33.3); signed map (-1.1, -51.4). **Vector** length 104, 23.7% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.9 | +17.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.6 | +17.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +16.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +7.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.9 | +8.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +6.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -12.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.5 | -11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.5 | -6.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:22,297,375-22,335,101 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPC5, SIN, FLJ10509, C37 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVU0](https://www.uniprot.org/uniprotkb/Q9NVU0) (DNA-directed RNA polymerase III subunit RPC5):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Specific peripheric component of RNA polymerase III (Pol III) which synthesizes small non-coding RNAs including 5S rRNA, snRNAs, tRNAs and miRNAs from at least 500 distinct genomic loci. Assembles with POLR3D/RPC4 forming a subcomplex that binds the Pol III core. Enables recruitment of Pol III at transcription initiation site and drives transcription initiation …

**Summary**, from NCBI Gene [55718](https://www.ncbi.nlm.nih.gov/gene/55718):

> Involved in termination of RNA polymerase III transcription and transcription initiation at RNA polymerase III promoter. Located in nucleoplasm. Part of RNA polymerase III complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30347) · Entrez [55718](https://www.ncbi.nlm.nih.gov/gene/55718) · UniProt [Q9NVU0](https://www.uniprot.org/uniprotkb/Q9NVU0) · Ensembl [ENSG00000058600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058600)

## Data

Gene col 663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 663); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 663]; `tensor/DDL_lfc|DDL_z.npy` [663]; `embed/gene_vectors.npy` [663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 663 or target_col == 663). Every well: [[POLR3E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
