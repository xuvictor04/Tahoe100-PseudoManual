---
symbol: "DCLRE1C"
type: "gene"
col: 7631
ensembl_id: "ENSG00000152457"
name: "DNA cross-link repair 1C"
location: "10p13"
module: 7
arm: "+"
pooled_cpm: 28.71
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DCLRE1C

*DNA cross-link repair 1C* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.76× (z +6.4, q 7e-08, up in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 2.27×; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.674× (z -8.6, q 5e-15, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOE1]] (+0.57, fdr 1e-05), [[ZNF107]] (+0.57, fdr 1e-05), [[TMEM62]] (+0.54, fdr 1e-05); moves opposite to [[OLFML2A]] (-0.51, fdr 3e-05), [[CHRDL1]] (-0.49, fdr 1e-04), [[TTC3]] (-0.49, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7631.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 2.27×; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.76×** | +6.4 | 7e-08 | 26/47 (J82, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.27×** | +4.8 | 4e-04 | 18/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +4.4 | 0.002 | 16/47 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.15× | +4.2 | 0.003 | 13/47 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.22×** | +4.1 | 0.003 | 13/48 (A498, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.21×** | +4.1 | 0.003 | 15/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.21×** | +4.1 | 0.003 | 14/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.20× | +4.0 | 0.005 | 14/47 (RKO, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.023 | 11/44 (SW 900, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.034 | 8/47 (A-172, J82, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.062 | 6/48 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.062 | 8/48 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7631.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.674×** | -8.6 | 5e-15 | 32/48 (SNU-423, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.710×** | -7.4 | 3e-11 | 27/46 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -7.4 | 3e-11 | 26/47 (HepG2/C3A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -7.0 | 3e-10 | 24/48 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.809×** | -6.5 | 9e-09 | 22/47 (SNU-423, COLO 205, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.747×** | -6.3 | 2e-08 | 23/47 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.776×** | -5.1 | 3e-05 | 19/47 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[palbociclib (drug)]] 0.5 µM |  | **0.783×** | -3.8 | 0.011 | 11/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.856× | -3.4 | 0.047 | 10/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.749×** | -3.3 | 0.058 | 14/46 (MIA PaCa-2, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.864× | -3.2 | 0.079 | 11/48 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.862× | -3.1 | 0.093 | 12/47 (HCT15, NCI-H2347, …) | all doses, flat |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.10 | 8/48 (CHP-212, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 31.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 34.7 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0938× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 50.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -9.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0835× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 35.8 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.111× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0689× (z -14.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0648× (z -14.2) ⚠ toxic |
| [[LoVo (line)]] | wt | 14.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.231× (z -13.3) ⚠ toxic |
| [[RKO (line)]] | wt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 29.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -9.9) |
| [[SW48 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOE1]] | +0.57 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZNF107]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TMEM62]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[HAUS8]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[WDR53]] | +0.51 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ZNF200]] | +0.50 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[AATF]] | +0.49 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[BFAR]] | +0.49 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[PALB2]] | +0.49 | +0.43 / +0.51 | both halves | 3e-05 | pathway: DNA Double-Strand Break Repair; STRING 640 |
| [[TTI1]] | +0.48 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[PHF5A]] | +0.48 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[ZNF100]] | +0.48 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLFML2A]] | -0.51 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[CHRDL1]] | -0.49 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TTC3]] | -0.49 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[POSTN]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[NPTXR]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[MXRA8]] | -0.44 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[LSMEM1]] | -0.43 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[MORF4L2]] | -0.43 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[CXADR]] | -0.42 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[SEPTIN2]] | -0.42 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[HDLBP]] | -0.42 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[COL3A1]] | -0.42 | -0.32 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DCLRE1C's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF100]] | B | ZNF100 activity raises DCLRE1C's level | lines that do not express ZNF100 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without ZNF100 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF66, ENSG00000269237, SORT1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-43.7, -48.9); signed map (-39.7, -37.3). **Vector** length 86.4, 17.1% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.0 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.8 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +0.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | +6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.6 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -6.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.4 | -7.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | DNA cross-link repair 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:14,897,359-14,954,432 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARTEMIS, FLJ11360, SNM1C, A-SCID; previously SCIDA |
| Gene groups (HGNC) | DNA cross-link repair family |
| Reactome | 3 pathways, smallest: Nonhomologous End-Joining (NHEJ); DNA Double-Strand Break Repair; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SD1](https://www.uniprot.org/uniprotkb/Q96SD1) (Protein artemis):

> Nuclease involved in DNA non-homologous end joining (NHEJ); required for double-strand break repair and V(D)J recombination. Required for V(D)J recombination, the process by which exons encoding the antigen-binding domains of immunoglobulins and T-cell receptor proteins are assembled from individual V, (D), and J gene segments. V(D)J recombination is initiated by the lymphoid specific RAG endonuclease complex, which generates site specific DNA double strand breaks (DSBs). These DSBs present two …

**Summary**, from NCBI Gene [64421](https://www.ncbi.nlm.nih.gov/gene/64421):

> This gene encodes a nuclear protein that is involved in V(D)J recombination and DNA repair. The encoded protein has single-strand-specific 5'-3' exonuclease activity; it also exhibits endonuclease activity on 5' and 3' overhangs and hairpins. The protein also functions in the regulation of the cell cycle in response to DNA damage. Mutations in this gene can cause Athabascan-type severe combined immunodeficiency (SCIDA) and Omenn syndrome. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:17642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17642) · Entrez [64421](https://www.ncbi.nlm.nih.gov/gene/64421) · UniProt [Q96SD1](https://www.uniprot.org/uniprotkb/Q96SD1) · Ensembl [ENSG00000152457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152457)

## Data

Gene col 7631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7631); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7631]; `tensor/DDL_lfc|DDL_z.npy` [7631]; `embed/gene_vectors.npy` [7631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7631 or target_col == 7631). Every well: [[DCLRE1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCLRE1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
