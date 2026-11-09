---
symbol: "SCML2"
type: "gene"
col: 2213
ensembl_id: "ENSG00000102098"
name: "Scm polycomb group protein like 2"
location: "Xp22.13"
module: 67
arm: "+"
pooled_cpm: 22.87
n_lines_expressing: 43
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# SCML2

*Scm polycomb group protein like 2* — Xp22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.11× (z +12.4, q 2e-32, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.562× (z -9.6, q 4e-19, down in 27 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.725× (z -7.6, q 5e-12, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP85]] (+0.73, fdr 7e-06), [[NEIL3]] (+0.70, fdr 7e-06), [[UBE2T]] (+0.69, fdr 7e-06); moves opposite to [[LINC00571]] (-0.62, fdr 1e-05), [[ZNF621]] (-0.61, fdr 1e-05), [[ATXN1L]] (-0.61, fdr 1e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[UGT8]] → it (grade B ⚠); 5 go from it, the strongest it → [[CEP192]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.11×** | +12.4 | 2e-32 | 33/41 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.93×** | +10.9 | 3e-25 | 31/39 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +10.3 | 2e-22 | 35/41 (SW1417, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +8.6 | 2e-15 | 28/40 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +7.9 | 3e-13 | 27/40 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.58×** | +7.6 | 3e-12 | 26/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.56×** | +7.4 | 1e-11 | 26/41 (SW1417, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +7.1 | 6e-11 | 25/40 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.54×** | +7.1 | 6e-11 | 24/41 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.56×** | +7.1 | 1e-10 | 21/40 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.53×** | +7.0 | 1e-10 | 25/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.47×** | +6.4 | 6e-09 | 20/40 (SW1417, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +6.3 | 1e-08 | 21/41 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +5.3 | 4e-06 | 13/41 (SW1417, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.5 | 3e-04 | 13/40 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.001 | 11/41 (Panc 03.27, SW1417, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.004 | 11/39 (A498, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.023 | 12/40 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.562×** | -9.6 | 4e-19 | 27/39 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.574×** | -8.6 | 2e-15 | 21/36 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -7.6 | 5e-12 | 26/40 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.657×** | -6.8 | 2e-09 | 16/33 (NCI-H2030, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -5.4 | 6e-06 | 22/40 (HEC-1-A, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.826×** | -4.5 | 5e-04 | 14/41 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.797×** | -3.8 | 0.012 | 18/41 (A-427, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.812×** | -3.5 | 0.033 | 14/39 (NCI-H661, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.814×** | -3.5 | 0.034 | 9/41 (Hs 766T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.822×** | -3.3 | 0.057 | 11/40 (NCI-H2030, SW480, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.765×** | -3.1 | 0.085 | 11/40 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.835× | -3.0 | 0.11 | 11/40 (SW48, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 42.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 61.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0584× (z -26.4) |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 47.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -16.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 64.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -14.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 39.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 28.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +10.1) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -11.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 7.62 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.89× (z +9.6) | — |
| [[A-172 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP85]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[NEIL3]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[UBE2T]] | +0.69 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CCDC150]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[NEURL1B]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NMU]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[BARD1]] | +0.65 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[MPHOSPH9]] | +0.65 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[BLM]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[BTBD3]] | +0.64 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CEP57L1]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[NCAPH]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00571]] | -0.62 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[ZNF621]] | -0.61 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ATXN1L]] | -0.61 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[FAM120AOS]] | -0.58 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[METTL6]] | -0.56 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[ZFHX2-AS1]] | -0.56 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CELF6]] | -0.56 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ERVK13-1]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[CCT6B]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SLC6A13]] | -0.54 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[CDKL3]] | -0.54 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT8]] | B | UGT8 activity lowers SCML2's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 2.21× higher at baseline in the lines without UGT8 | 0.009 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |
| [[NMU]] | B | NMU activity lowers SCML2's level | lines that do not express NMU (18) vs lines expressing it (32) | 2.02× higher at baseline in the lines without NMU | 0.088 | ⚠ within organs, on part of the lines; also absent: S100A2, ANK3, FAM83F; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEP192]] | B | SCML2 activity raises CEP192's level | lines that do not express SCML2 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without SCML2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ASAP3, ENSG00000267131, LAG3 |
| [[ZYG11A]] | B | SCML2 activity raises ZYG11A's level | lines that do not express SCML2 (7) vs lines expressing it (43) | 3.11× lower at baseline in the lines without SCML2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ASAP3, ENSG00000267131, LAG3 |
| [[ERVK13-1]] | B | SCML2 activity lowers ERVK13-1's level | lines that do not express SCML2 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without SCML2 | 0.086 | ⚠ within organs, on part of the lines; also absent: ASAP3, ENSG00000267131, LAG3 |
| [[TMEM131L]] | B | SCML2 activity raises TMEM131L's level | lines that do not express SCML2 (7) vs lines expressing it (43) | 2.19× lower at baseline in the lines without SCML2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ASAP3, ENSG00000267131, LAG3 |
| [[UGT8]] | B | SCML2 activity lowers UGT8's level | lines that do not express SCML2 (7) vs lines expressing it (43) | 4.94× higher at baseline in the lines without SCML2 | 0.096 | ⚠ within organs, on part of the lines; also absent: ASAP3, ENSG00000267131, LAG3 |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.4, -52.8); signed map (-45.3, -40.1). **Vector** length 88.7, 20.3% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.58 to 12); *G2/M checkpoint* (hallmark, mean cos +0.56 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.3 | +3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +2.6 | +10.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -3.2 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Scm polycomb group protein like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.13 — chrX:18,239,313-18,354,688 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sterile alpha motif domain containing; MBT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQR0](https://www.uniprot.org/uniprotkb/Q9UQR0) (Sex comb on midleg-like protein 2):

> Putative Polycomb group (PcG) protein. PcG proteins act by forming multiprotein complexes, which are required to maintain the transcriptionally repressive state of homeotic genes throughout development (By similarity).

**Summary**, from NCBI Gene [10389](https://www.ncbi.nlm.nih.gov/gene/10389):

> This gene encodes a member of the Polycomb group proteins. These proteins form the Polycomb repressive complexes which are involved in transcriptional repression. The encoded protein binds histone peptides that are monomethylated at lysine residues and may be involved in regulating homeotic gene expression during development. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:10581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10581) · Entrez [10389](https://www.ncbi.nlm.nih.gov/gene/10389) · UniProt [Q9UQR0](https://www.uniprot.org/uniprotkb/Q9UQR0) · Ensembl [ENSG00000102098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102098)

## Data

Gene col 2213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2213); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2213]; `tensor/DDL_lfc|DDL_z.npy` [2213]; `embed/gene_vectors.npy` [2213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2213 or target_col == 2213). Every well: [[SCML2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCML2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
