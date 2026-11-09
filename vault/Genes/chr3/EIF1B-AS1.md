---
symbol: "EIF1B-AS1"
type: "gene"
col: 15965
ensembl_id: "ENSG00000280739"
name: ""
location: ""
module: 10
arm: "+"
pooled_cpm: 8.75
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 30
n_dd_up_clean: 21
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 13
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# EIF1B-AS1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +6.7, q 1e-08, up in 29 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.242× (z -11.8, q 2e-29, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUCLG2-DT]] (+0.82, fdr 7e-06), [[DPH6-DT]] (+0.81, fdr 7e-06), [[AGA-DT]] (+0.79, fdr 9e-06); moves opposite to [[TMEM120B]] (-0.65, fdr 6e-05), [[GRAMD4]] (-0.64, fdr 1e-04), [[TMEM184B]] (-0.64, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[KIAA0825]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +6.7 | 1e-08 | 29/42 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.84×** | +5.1 | 9e-05 | 26/46 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.49×** | +4.8 | 3e-04 | 21/45 (LS 180, A-427, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.65×** | +4.3 | 0.003 | 20/43 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +4.2 | 0.003 | 21/44 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.63×** | +4.2 | 0.003 | 20/44 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.003 | 15/45 (SK-MEL-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.003 | 18/46 (SK-MEL-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +3.7 | 0.015 | 17/46 (SK-MEL-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.017 | 16/44 (NCI-H23, A498, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.017 | 19/46 (NCI-H23, A549, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.018 | 15/46 (NCI-H1792, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.018 | 18/44 (SK-MEL-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.032 | 7/45 (A498, KATO III, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.035 | 9/44 (SK-MEL-2, A-427, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.51×** | +3.3 | 0.035 | 13/45 (NCI-H2030, SK-MEL-2, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.035 | 17/43 (H4, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.242×** | -11.8 | 2e-29 | 39/46 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.354×** | -8.8 | 5e-16 | 34/45 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.362×** | -8.6 | 1e-15 | 33/45 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.404×** | -7.6 | 6e-12 | 27/40 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.455×** | -6.5 | 7e-09 | 28/45 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.584×** | -6.4 | 1e-08 | 30/46 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.505×** | -5.8 | 6e-07 | 24/40 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.493×** | -5.7 | 6e-07 | 22/35 (COLO 205, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.526×** | -5.3 | 6e-06 | 25/45 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.546×** | -5.1 | 2e-05 | 26/45 (LS 180, LOX-IMVI, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.558×** | -4.9 | 4e-05 | 25/45 (NCI-H23, CHP-212, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.332×** | -4.9 | 5e-05 | 23/45 (SK-MEL-2, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.561×** | -4.9 | 5e-05 | 25/46 (NCI-H2030, AN3 CA, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.611×** | -4.2 | 0.001 | 19/45 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -4.1 | 0.001 | 18/41 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.540×** | -3.7 | 0.007 | 11/46 (SW 1088, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.439×** | -3.6 | 0.009 | 14/35 (HOP62, C32, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.446×** | -3.6 | 0.010 | 17/40 (A-427, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.643×** | -3.5 | 0.012 | 18/44 (Panc 03.27, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.473×** | -3.3 | 0.023 | 14/43 (CFPAC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.6 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.132× (z -10.2) |
| [[LS 180 (line)]] | wt | 15.0 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0670× (z -13.4) |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0743× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0833× (z -11.1) |
| [[PANC-1 (line)]] | alt | 8.02 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0848× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0543× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0617× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.120× (z -8.8) |
| [[A498 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 7.85 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0377× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 7.78 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.101× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 7.24 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0769× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 7.68 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0843× (z -8.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[Panc 03.27 (line)]] | alt | 7.29 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0649× (z -10.0) |
| [[SW480 (line)]] | alt | 3.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +9.1) | — |
| [[A-172 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUCLG2-DT]] | +0.82 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[DPH6-DT]] | +0.81 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[AGA-DT]] | +0.79 | +0.79 / +0.57 | both halves | 9e-06 |  |
| [[CFAP418-AS1]] | +0.78 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[ZRANB2-DT]] | +0.78 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.76 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.76 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.73 | +0.72 / +0.42 | both halves | 4e-05 |  |
| [[MAD2L1-DT]] | +0.73 | +0.73 / +0.38 | both halves | 6e-05 |  |
| [[BCLAF1]] | +0.72 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[LINC00240]] | +0.72 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[STPG2]] | +0.71 | +0.67 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | -0.65 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[GRAMD4]] | -0.64 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[TMEM184B]] | -0.64 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[TPST2]] | -0.62 | -0.65 / -0.39 | both halves | 6e-05 |  |
| [[MPG]] | -0.62 | -0.72 / -0.26 | both halves | 4e-04 |  |
| [[LCMT1]] | -0.62 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[ANKRD27]] | -0.61 | -0.59 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA0825]] | B | KIAA0825 activity raises EIF1B-AS1's level | lines that do not express KIAA0825 (9) vs lines expressing it (41) | 2.46× lower at baseline in the lines without KIAA0825 | 0.020 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, SPART, CCDC102B; maybe low, not absent |
| [[LINC00466]] | B | LINC00466 activity raises EIF1B-AS1's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without LINC00466 | 0.038 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[CTSO]] | B | CTSO activity strengthens EIF1B-AS1's drug response | lines that do not express CTSO (8) vs lines expressing it (38) | the lines without CTSO respond 0.53× as strongly (z diff +1.85); strongest at Digitoxin 5 µM: 0.74x vs 0.33x (z diff +3.9) | 0.060 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT; target measured in part of the lines; artifact flags |
| [[DPY19L2]] | B | DPY19L2 activity raises EIF1B-AS1's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without DPY19L2 | 0.065 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ |
| [[MAP2K1]] | B | MAP2K1 activity lowers EIF1B-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CTSO]] | B | CTSO activity raises EIF1B-AS1's level | lines that do not express CTSO (8) vs lines expressing it (42) | 2.02× lower at baseline in the lines without CTSO | 0.088 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[ANKRD18B]] | B | ANKRD18B activity raises EIF1B-AS1's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without ANKRD18B | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[CCDC7]] | C | CCDC7's natural level strengthens EIF1B-AS1's drug response | CCDC7's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.45; direction not clear | 0.055 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises EIF1B-AS1's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.02× lower at baseline in the lines without WARS2-AS1 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent |
| [[DPH6-DT]] | C | DPH6-DT activity raises EIF1B-AS1's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.24× lower at baseline in the lines without DPH6-DT | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |
| [[CCDC171]], [[DUSP19]], [[RFX3-DT]] | C | CCDC171, DUSP19, RFX3-DT activity raises EIF1B-AS1's level | lines that do not express CCDC171, DUSP19, RFX3-DT (3) vs lines expressing them (47) | 2.62× lower at baseline in the lines without CCDC171, DUSP19, RFX3-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p; co-absent genes |
| [[LRRIQ3]] | C | LRRIQ3 activity raises EIF1B-AS1's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.45× lower at baseline in the lines without LRRIQ3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.6, 16.5); signed map (30.1, -9.9). **Vector** length 78.4, 16.4% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.9 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.4 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -3.2 |

## What is on record

> [!warning] No registry record
> EIF1B-AS1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15965); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15965]; `tensor/DDL_lfc|DDL_z.npy` [15965]; `embed/gene_vectors.npy` [15965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15965 or target_col == 15965). Every well: [[EIF1B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF1B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
