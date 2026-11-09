---
symbol: "FCHSD1"
type: "gene"
col: 12494
ensembl_id: "ENSG00000197948"
name: "FCH and double SH3 domains 1"
location: "5q31.3"
module: 2
arm: "+"
pooled_cpm: 13.31
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# FCHSD1

*FCH and double SH3 domains 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.37× (z +10.2, q 2e-21, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.452× (z -13.2, q 5e-37, down in 39 of 43 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.562× (z -9.6, q 2e-19, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP35]] (+0.78, fdr 7e-06), [[TCIRG1]] (+0.75, fdr 7e-06), [[ABHD17A]] (+0.72, fdr 1e-05); moves opposite to [[MCTS1]] (-0.63, fdr 5e-05), [[FBXL17]] (-0.63, fdr 1e-05), [[CLOCK]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KIF3C]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Tomivosertib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +10.2 | 2e-21 | 40/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +8.7 | 6e-16 | 35/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +5.6 | 4e-06 | 29/45 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.40×** | +5.5 | 4e-06 | 24/45 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.9 | 1e-04 | 24/44 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.002 | 20/42 (CFPAC-1, C32, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.004 | 19/43 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.015 | 15/42 (HS-578T, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.32×** | +3.3 | 0.067 | 11/45 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.452×** | -13.2 | 5e-37 | 39/43 (LoVo, A-172, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.348×** | -11.9 | 2e-30 | 37/44 (NCI-H1792, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -9.6 | 2e-19 | 32/42 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -7.1 | 2e-10 | 29/42 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.649×** | -4.8 | 2e-04 | 22/44 (A-172, HS-578T, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -4.7 | 2e-04 | 22/41 (SNU-423, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.673×** | -4.7 | 3e-04 | 20/44 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -4.6 | 3e-04 | 25/43 (J82, SW 1088, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.528×** | -3.9 | 0.005 | 21/44 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.808×** | -3.5 | 0.022 | 17/44 (NCI-H1792, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.742×** | -3.5 | 0.023 | 18/44 (KATO III, HOP62, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.028 | 13/44 (PANC-1, HCT15, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.748×** | -3.4 | 0.028 | 16/45 (SW 900, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | **0.746×** | -3.3 | 0.037 | 15/43 (KATO III, AsPC-1, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.754×** | -3.2 | 0.055 | 11/43 (KATO III, SW 1271, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 0.05 µM |  | **0.749×** | -3.1 | 0.060 | 10/43 (SW48, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -11.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -9.6) |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 10.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.8) |
| [[A549 (line)]] | wt | 11.9 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0738× (z -12.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0638× (z -15.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 25.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -11.9) |
| [[A-427 (line)]] | wt | 4.13 | 0 | 1 | — | [[Tomivosertib (drug)]] 0.05 µM 0.0829× (z -8.5) |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -11.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -12.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.2) ⚠ cell-cycle shift, explains ~41% of this change |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -9.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SNU-423 (line)]] | alt | 8.01 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0989× (z -9.7) |
| [[SW480 (line)]] | alt | 17.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.47× (z +8.8) | — |
| [[A498 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP35]] | +0.78 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[TCIRG1]] | +0.75 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[ABHD17A]] | +0.72 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[GDI1]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PLD2]] | +0.69 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[SEMA6C]] | +0.69 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.68 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MAST3]] | +0.68 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[KLC3]] | +0.67 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[F11R]] | +0.66 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[LTBP4]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[BMP8B]] | +0.65 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTS1]] | -0.63 | -0.70 / -0.40 | both halves | 5e-05 |  |
| [[FBXL17]] | -0.63 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[CLOCK]] | -0.62 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[CPSF2]] | -0.62 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ASH1L]] | -0.61 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MZF1-AS1]] | -0.61 | -0.65 / -0.24 | both halves | 5e-04 |  |
| [[POGLUT1]] | -0.60 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[GALNT7-DT]] | -0.60 | -0.60 / -0.24 | both halves | 4e-04 |  |
| [[ATAD2B]] | -0.60 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ZNF827]] | -0.60 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ZFX]] | -0.60 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ZNF337-AS1]] | -0.59 | -0.62 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF3C]] | B | KIF3C activity raises FCHSD1's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 1.95× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FCHSD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers FCHSD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SFXN3]] | C | SFXN3 activity raises FCHSD1's level | lines that do not express SFXN3 (3) vs lines expressing it (47) | 3.77× lower at baseline in the lines without SFXN3 | 9e-04 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tomivosertib (drug)]] 5 µM | C | FCHSD1 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express FCHSD1 (3) vs lines expressing it (45) | the lines without FCHSD1: 0.68× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PLS3, CDK6, SH2B3 |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | FCHSD1 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express FCHSD1 (3) vs lines expressing it (45) | the lines without FCHSD1: 0.33× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PLS3, CDK6, SH2B3 |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | FCHSD1 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express FCHSD1 (3) vs lines expressing it (45) | the lines without FCHSD1: 0.73× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PLS3, CDK6, SH2B3 |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | FCHSD1 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express FCHSD1 (3) vs lines expressing it (45) | the lines without FCHSD1: 0.78× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PLS3, CDK6, SH2B3 |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | FCHSD1 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express FCHSD1 (3) vs lines expressing it (45) | the lines without FCHSD1: 0.75× the cells of the other lines | 0.092 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PLS3, CDK6, SH2B3 |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (5.1, -4.8); signed map (-30.1, 0.2). **Vector** length 97.5, 22.0% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.1 | +10.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +4.3 | +5.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | -0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -8.2 | -13.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.2 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | FCH and double SH3 domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,639,302-141,651,418 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00007 |
| Gene groups (HGNC) | F-BAR domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WN1](https://www.uniprot.org/uniprotkb/Q86WN1) (F-BAR and double SH3 domains protein 1):

> Promotes actin polymerization mediated by SNX9 and WASL.

**Summary**, from NCBI Gene [89848](https://www.ncbi.nlm.nih.gov/gene/89848):

> Predicted to enable lipid binding activity. Predicted to be involved in neuromuscular synaptic transmission and positive regulation of actin filament polymerization. Predicted to act upstream of or within several processes, including import into nucleus; inflammatory response; and response to hydrogen peroxide. Predicted to be located in cuticular plate. Predicted to be part of protein-containing complex. Predicted to be active in neuromuscular junction and recycling endosome. [provided by …

**Accessions** — [HGNC:25463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25463) · Entrez [89848](https://www.ncbi.nlm.nih.gov/gene/89848) · UniProt [Q86WN1](https://www.uniprot.org/uniprotkb/Q86WN1) · Ensembl [ENSG00000197948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197948)

## Data

Gene col 12494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12494); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12494]; `tensor/DDL_lfc|DDL_z.npy` [12494]; `embed/gene_vectors.npy` [12494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12494 or target_col == 12494). Every well: [[FCHSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FCHSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
