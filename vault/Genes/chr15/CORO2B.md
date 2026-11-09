---
symbol: "CORO2B"
type: "gene"
col: 2388
ensembl_id: "ENSG00000103647"
name: "coronin 2B"
location: "15q23"
module: 110
arm: "+"
pooled_cpm: 8.52
n_lines_expressing: 37
n_dd_up: 25
n_dd_down: 41
n_dd_up_clean: 20
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# CORO2B

*coronin 2B* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 2.75× (z +10.5, q 4e-23, up in 26 of 34 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 2.78× (z +10.2, q 5e-22, up in 24 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.528× (z -9.4, q 3e-18, down in 21 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PXN]] (+0.74, fdr 7e-06), [[TOMM34]] (+0.74, fdr 7e-06), [[ACP7]] (+0.73, fdr 7e-06); moves opposite to [[MBNL2]] (-0.59, fdr 1e-05), [[TNS3]] (-0.58, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[BCL2A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **2.75×** | +10.5 | 4e-23 | 26/34 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **2.78×** | +10.2 | 5e-22 | 24/34 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.92×** | +9.6 | 2e-19 | 21/34 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +8.1 | 9e-14 | 6/13 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **2.10×** | +7.5 | 5e-12 | 20/34 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **2.05×** | +7.5 | 8e-12 | 20/34 (PANC-1, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **2.00×** | +7.2 | 5e-11 | 15/31 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +6.6 | 2e-09 | 17/33 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +6.5 | 4e-09 | 15/34 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +6.2 | 4e-08 | 6/17 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.3 | 6e-06 | 10/30 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.60×** | +4.9 | 5e-05 | 14/34 (CFPAC-1, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.3 | 7e-04 | 12/34 (SW1417, A549, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.79×** | +4.3 | 7e-04 | 8/31 (PANC-1, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.004 | 13/34 (CFPAC-1, HepG2/C3A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.004 | 12/34 (RKO, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.008 | 5/34 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.009 | 9/34 (LoVo, SW480, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.010 | 8/34 (RKO, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 1 with an alert ⚠; shown: the 15 strongest. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2388.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.528×** | -9.4 | 3e-18 | 21/30 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.473×** | -8.8 | 3e-16 | 25/33 (HOP62, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.437×** | -8.5 | 2e-15 | 25/34 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.420×** | -8.3 | 1e-14 | 24/34 (HOP62, RKO, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.457×** | -8.2 | 4e-14 | 23/34 (HOP62, HepG2/C3A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.581×** | -7.8 | 6e-13 | 19/34 (HOP62, HepG2/C3A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.481×** | -7.4 | 1e-11 | 23/34 (HOP62, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.609×** | -7.3 | 2e-11 | 21/33 (RKO, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.578×** | -6.9 | 4e-10 | 21/33 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.527×** | -6.3 | 2e-08 | 20/33 (HOP62, RKO, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.556×** | -6.1 | 5e-08 | 20/34 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.664×** | -6.0 | 9e-08 | 19/34 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.571×** | -5.8 | 2e-07 | 19/33 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.678×** | -5.7 | 4e-07 | 17/34 (RKO, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.569×** | -5.6 | 6e-07 | 14/33 (HepG2/C3A, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 44.5 | 0 | 37 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.200× (z -29.0) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0202× (z -19.2) |
| [[RKO (line)]] | wt | 67.7 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -20.9) |
| [[HepG2_C3A (line)]] | wt | 58.6 | 0 | 14 (2 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0192× (z -19.9) |
| [[A549 (line)]] | wt | 14.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 5.42 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.254× (z -15.2) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.0966× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.418× (z -11.6) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0698× (z -9.6) |
| [[A-172 (line)]] | wt | 8.15 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.250× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 7.36 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0709× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.0) |
| [[SNU-423 (line)]] | alt | 8.27 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.0324× (z -13.0) |
| [[SW480 (line)]] | alt | 8.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.6) |
| [[A-427 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXN]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[TOMM34]] | +0.74 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[ACP7]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[FXYD5]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[SLC4A7]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[PNP]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[S100A16]] | +0.71 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[ELK3]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ARHGAP22]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL2]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TNS3]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2A1]] | B | BCL2A1 activity raises CORO2B's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.04× lower at baseline in the lines without BCL2A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[RAB3B]] | B | RAB3B activity raises CORO2B's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 2.72× lower at baseline in the lines without RAB3B | 0.011 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[ROBO4]] | B | ROBO4 activity raises CORO2B's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without ROBO4 | 0.042 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[BICDL1]] | B | BICDL1 activity lowers CORO2B's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 2.12× higher at baseline in the lines without BICDL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | B | TM4SF19, TM4SF19-DYNLT2B activity strengthens CORO2B's drug response | lines that do not express TM4SF19, TM4SF19-DYNLT2B (11) vs lines expressing them (23) | the lines without TM4SF19, TM4SF19-DYNLT2B respond 0.55× as strongly (z diff +1.63); strongest at Homoharringtonine 5 µM: 0.72x vs 0.37x (z diff +3.6) | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; target measured in part of the lines; artifact flags; co-absent genes |
| [[IL11]] | B | IL11 activity raises CORO2B's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.21× lower at baseline in the lines without IL11 | 0.075 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[LINC01812]] | B | LINC01812 activity raises CORO2B's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 1.51× lower at baseline in the lines without LINC01812 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |
| [[NR3C1]] | B | NR3C1 activity lowers CORO2B's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[LINC01629]] | B | LINC01629 activity raises CORO2B's level | lines that do not express LINC01629 (30) vs lines expressing it (20) | 1.87× lower at baseline in the lines without LINC01629 | 0.092 | ⚠ within organs, on part of the lines; also absent: XIST, ENSG00000262198, RHEX |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.909). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.0, 3.8); signed map (4.8, 46.9). **Vector** length 109, 27.7% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +6.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.1 | +10.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +10.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +9.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +7.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.0 | -8.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -6.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.8 | -8.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.7 | -7.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -8.2 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -4.0 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | coronin 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:68,578,993-68,727,806 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ClipinC, KIAA0925 |
| Gene groups (HGNC) | WD repeat domain containing; Coronins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ03](https://www.uniprot.org/uniprotkb/Q9UQ03) (Coronin-2B):

> May play a role in the reorganization of neuronal actin structure.

**Summary**, from NCBI Gene [10391](https://www.ncbi.nlm.nih.gov/gene/10391):

> Enables talin binding activity and vinculin binding activity. Acts upstream of or within several processes, including negative regulation of cell-substrate adhesion; regulation of actin cytoskeleton organization; and regulation of establishment of protein localization. Located in focal adhesion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2256) · Entrez [10391](https://www.ncbi.nlm.nih.gov/gene/10391) · UniProt [Q9UQ03](https://www.uniprot.org/uniprotkb/Q9UQ03) · Ensembl [ENSG00000103647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103647)

## Data

Gene col 2388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2388); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2388]; `tensor/DDL_lfc|DDL_z.npy` [2388]; `embed/gene_vectors.npy` [2388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2388 or target_col == 2388). Every well: [[CORO2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CORO2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
