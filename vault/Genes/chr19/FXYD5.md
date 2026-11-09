---
symbol: "FXYD5"
type: "gene"
col: 1584
ensembl_id: "ENSG00000089327"
name: "FXYD domain containing ion transport regulator 5"
location: "19q13.12"
module: 110
arm: "+"
pooled_cpm: 39.56
n_lines_expressing: 45
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 23
direction_downstream: 1
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# FXYD5

*FXYD domain containing ion transport regulator 5* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.36× (z +9.6, q 6e-19, up in 36 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 3.81×, LOX-IMVI 2.78×, KATO III 3.17×, A498 2.73×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 4.35×, KATO III 3.60×, LOX-IMVI 2.94×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.242× (z -22.3, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO2B]] (+0.73, fdr 7e-06), [[ABTB3]] (+0.71, fdr 1e-05), [[ATP13A2]] (+0.70, fdr 1e-05); moves opposite to [[CEBPD]] (-0.63, fdr 3e-05), [[FOSL2]] (-0.60, fdr 1e-05), [[ZNF608]] (-0.59, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[COL13A1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NT5E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1584.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 3.81×, LOX-IMVI 2.78×, KATO III 3.17×, A498 2.73×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 4.35×, KATO III 3.60×, LOX-IMVI 2.94×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +9.6 | 6e-19 | 36/37 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +9.1 | 3e-17 | 30/33 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.7 | 5e-04 | 28/35 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.242×** | -22.3 | 0e+00 | 42/43 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.364×** | -11.2 | 7e-27 | 37/42 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.494×** | -7.8 | 9e-13 | 38/43 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.541×** | -6.8 | 1e-09 | 36/43 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.538×** | -6.6 | 4e-09 | 32/43 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.546×** | -6.2 | 5e-08 | 38/43 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.587×** | -5.7 | 1e-06 | 30/41 (A-172, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.614×** | -5.4 | 4e-06 | 32/43 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.663×** | -4.2 | 0.002 | 29/43 (MIA PaCa-2, RKO, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.773×** | -4.0 | 0.003 | 27/43 (RKO, A-172, …) | rises with dose | low cells (technical?) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.503×** | -3.8 | 0.008 | 25/42 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.783×** | -3.7 | 0.008 | 25/43 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.721×** | -3.6 | 0.014 | 23/43 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.523×** | -3.6 | 0.015 | 28/42 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.721×** | -3.5 | 0.018 | 24/42 (A-172, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.734×** | -3.4 | 0.022 | 24/43 (Hs 766T, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 74.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -16.2) |
| [[HOP62 (line)]] | alt | 70.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -27.5) |
| [[LOX-IMVI (line)]] | wt | 69.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0838× (z -24.6) |
| [[RKO (line)]] | wt | 91.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0698× (z -31.6) |
| [[A498 (line)]] | wt | 44.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -13.8) |
| [[A549 (line)]] | wt | 50.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -18.0) |
| [[HS-578T (line)]] | alt | 55.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.3) |
| [[KATO III (line)]] | alt | 46.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -22.1) |
| [[H4 (line)]] | wt | 92.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0150× (z -29.3) |
| [[Hs 766T (line)]] | wt | 141 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 50.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.4) |
| [[LoVo (line)]] | wt | 32.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -16.9) |
| [[LS 180 (line)]] | wt | 36.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.2) |
| [[NCI-H1792 (line)]] | alt | 31.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.35× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 32.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 70.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -22.4) |
| [[SK-MEL-2 (line)]] | alt | 73.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.1) |
| [[SW 900 (line)]] | alt | 45.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -16.2) |
| [[SW480 (line)]] | alt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 52.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.3) |
| [[C32 (line)]] | wt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 34.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.5) |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.7) |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -15.9) |
| [[J82 (line)]] | alt | 41.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 53.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.7) |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 30.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.1) |
| [[PANC-1 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -17.7) |
| [[SW1417 (line)]] | alt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.8) |
| [[SW48 (line)]] | wt | 37.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.4) |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO2B]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[ABTB3]] | +0.71 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.70 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[S100A16]] | +0.69 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[MMP1]] | +0.69 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[KCNC4]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PNP]] | +0.66 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[PROCR]] | +0.63 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[AP3M2]] | +0.62 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[KIF21B]] | +0.61 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[CSNK1E]] | +0.61 | +0.69 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPD]] | -0.63 | -0.73 / -0.46 | both halves | 3e-05 |  |
| [[FOSL2]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.59 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[RNF115]] | -0.58 | -0.71 / -0.41 | both halves | 4e-05 |  |
| [[REPIN1]] | -0.58 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[HNRNPH2]] | -0.57 | -0.63 / -0.43 | both halves | 4e-05 |  |
| [[CPEB2]] | -0.56 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PPP4R2]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[RBM7]] | -0.55 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[WTAP]] | -0.55 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[NFYB]] | -0.55 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[SREK1]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 20, C 3. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | COL13A1 activity raises FXYD5's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without COL13A1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[CTSL]] | B | CTSL activity raises FXYD5's level | lines that do not express CTSL (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without CTSL | 0.004 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[S100A16]] | B | S100A16 activity raises FXYD5's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.60× lower at baseline in the lines without S100A16 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[ALPK1]] | B | ALPK1 activity raises FXYD5's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 3.39× lower at baseline in the lines without ALPK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[ITGA5]] | B | ITGA5 activity raises FXYD5's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without ITGA5 | 0.013 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[CD44]] | B | CD44 activity raises FXYD5's level | lines that do not express CD44 (15) vs lines expressing it (35) | 3.11× lower at baseline in the lines without CD44 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[UBASH3B]] | B | UBASH3B activity raises FXYD5's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.52× lower at baseline in the lines without UBASH3B | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[AMOTL1]] | B | AMOTL1 activity raises FXYD5's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.54× lower at baseline in the lines without AMOTL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[IL13RA2]] | B | IL13RA2 activity raises FXYD5's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.20× lower at baseline in the lines without IL13RA2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[NLRP3]] | B | NLRP3 activity raises FXYD5's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without NLRP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[MMP1]] | B | MMP1 activity raises FXYD5's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without MMP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[PROCR]] | B | PROCR activity raises FXYD5's level | lines that do not express PROCR (8) vs lines expressing it (42) | 2.80× lower at baseline in the lines without PROCR | 0.059 | ⚠ within organs, on part of the lines; also absent: ATP2B4, RNF135, LAMB1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5E]] | B | FXYD5 activity raises NT5E's level | lines that do not express FXYD5 (5) vs lines expressing it (45) | 6.63× lower at baseline in the lines without FXYD5 | 0.081 | ⚠ within organs, on part of the lines; also absent: ACCS, LGI4, CAV2; its own permutation p |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.1, 3.5); signed map (2.8, 48.1). **Vector** length 86.4, 25.1% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.6 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -22.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -11.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -6.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | FXYD domain containing ion transport regulator 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,154,730-35,169,881 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OIT2 |
| Gene groups (HGNC) | FXYD domain containing ion transport regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DB9](https://www.uniprot.org/uniprotkb/Q96DB9) (FXYD domain-containing ion transport regulator 5):

> Associates with and regulates the activity of the sodium/potassium-transporting ATPase (NKA) which catalyzes the hydrolysis of ATP coupled with the exchange of Na(+) and K(+) ions across the plasma membrane (By similarity). May increase NKA activity by increasing the apparent affinity for Na(+). Involved in down-regulation of E-cadherin which results in reduced cell adhesion. Promotes metastasis.

**Summary**, from NCBI Gene [53827](https://www.ncbi.nlm.nih.gov/gene/53827):

> This gene encodes a member of a family of small membrane proteins that share a 35-amino acid signature sequence domain, beginning with the sequence PFXYD and containing 7 invariant and 6 highly conserved amino acids. The approved human gene nomenclature for the family is FXYD-domain containing ion transport regulator. Mouse FXYD5 has been termed RIC (Related to Ion Channel). FXYD2, also known as the gamma subunit of the Na,K-ATPase, regulates the properties of that enzyme. FXYD1 …

**Accessions** — [HGNC:4029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4029) · Entrez [53827](https://www.ncbi.nlm.nih.gov/gene/53827) · UniProt [Q96DB9](https://www.uniprot.org/uniprotkb/Q96DB9) · Ensembl [ENSG00000089327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089327)

## Data

Gene col 1584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1584); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1584]; `tensor/DDL_lfc|DDL_z.npy` [1584]; `embed/gene_vectors.npy` [1584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1584 or target_col == 1584). Every well: [[FXYD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FXYD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
