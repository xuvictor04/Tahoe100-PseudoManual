---
symbol: "OAF"
type: "gene"
col: 11509
ensembl_id: "ENSG00000184232"
name: "out at first homolog"
location: "11q23.3"
module: 84
arm: "+"
pooled_cpm: 18.09
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 28
n_dd_up_clean: 9
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 5
direction_downstream: 12
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# OAF

*out at first homolog* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.93× (z +7.8, q 4e-12, up in 17 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.69× (z +6.2, q 1e-07, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.477× (z -8.7, q 1e-15, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLI2]] (+0.57, fdr 1e-05), [[MAMLD1]] (+0.54, fdr 1e-05), [[FERMT1]] (+0.53, fdr 1e-05); moves opposite to [[LSM14B]] (-0.53, fdr 1e-05), [[PCM1]] (-0.47, fdr 3e-05), [[HDAC6]] (-0.47, fdr 4e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[S100A16]] → it (grade B ⚠); 12 go from it, the strongest it → [[HMBS]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.93×** | +7.8 | 4e-12 | 17/32 (LOX-IMVI, SW 900, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +6.2 | 1e-07 | 25/44 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +4.8 | 4e-04 | 18/43 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.4 | 0.002 | 17/44 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.005 | 22/44 (HT-29, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.005 | 17/44 (Panc 03.27, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.40×** | +3.8 | 0.011 | 10/25 (SW480, HT-29, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.016 | 17/43 (SW1417, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.7 | 0.016 | 15/36 (HS-578T, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.070 | 9/44 (SW480, SW1417, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.070 | 8/44 (HT-29, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.083 | 6/44 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.477×** | -8.7 | 1e-15 | 29/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.637×** | -7.5 | 2e-11 | 24/42 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.597×** | -5.9 | 6e-07 | 26/44 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.678×** | -4.6 | 5e-04 | 20/44 (HepG2/C3A, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.680×** | -4.5 | 5e-04 | 16/44 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.665×** | -4.5 | 5e-04 | 19/43 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.669×** | -4.4 | 9e-04 | 17/44 (NCI-H1573, SW480, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.693×** | -4.3 | 0.001 | 17/44 (H4, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.775×** | -4.2 | 0.001 | 16/44 (CFPAC-1, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.501×** | -4.0 | 0.003 | 15/42 (A-172, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.746×** | -3.8 | 0.006 | 16/44 (LoVo, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.726×** | -3.8 | 0.008 | 20/44 (HepG2/C3A, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.727×** | -3.8 | 0.008 | 20/43 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.730×** | -3.7 | 0.009 | 18/43 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.554×** | -3.4 | 0.022 | 15/43 (H4, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.029 | 16/44 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.777×** | -3.3 | 0.029 | 21/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 94.8 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -16.3) |
| [[RKO (line)]] | wt | 23.5 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0345× (z -18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.139× (z -15.5) |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0710× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0908× (z -9.6) |
| [[A498 (line)]] | wt | 52.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.8) |
| [[COLO 205 (line)]] | alt | 25.0 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 15.6× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -8.9) |
| [[SW480 (line)]] | alt | 14.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -10.3) |
| [[KATO III (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.4) |
| [[LoVo (line)]] | wt | 25.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.6) |
| [[NCI-H2030 (line)]] | alt | 9.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +9.6) | — |
| [[SW 1088 (line)]] | alt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -9.7) |
| [[A-172 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLI2]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MAMLD1]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[FERMT1]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[PLAUR]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ST3GAL1]] | +0.52 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[KIAA1549]] | +0.52 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[PRR5]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[SH3PXD2A]] | +0.51 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[IGSF9B]] | +0.51 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[SHB]] | +0.51 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[FAM222A-AS1]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM14B]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PCM1]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[HDAC6]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[WASHC3]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LRRC27]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[SPACA9]] | -0.45 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[DNAJC27]] | -0.45 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ENTPD3-AS1]] | -0.45 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[FAM76B]] | -0.45 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[TCAIM]] | -0.45 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[GID8]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[C6orf89]] | -0.44 | -0.49 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A16]] | B | S100A16 activity raises OAF's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without S100A16 | 0.070 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[SH2D2A]] | B | SH2D2A activity raises OAF's level | lines that do not express SH2D2A (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without SH2D2A | 0.089 | ⚠ within organs, on part of the lines; also absent: IL1R2, SLC17A9, MT1G; maybe low, not absent |
| [[PTPRE]] | B | PTPRE activity raises OAF's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.00× lower at baseline in the lines without PTPRE | 0.092 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[MAP2K1]] | B | MAP2K1 activity raises OAF's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FOSL1]] | C | FOSL1 activity raises OAF's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 2.87× lower at baseline in the lines without FOSL1 | 0.091 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMBS]] | C | OAF activity lowers HMBS's level | lines that do not express OAF (4) vs lines expressing it (46) | 1.57× higher at baseline in the lines without OAF | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| [[MAMLD1]] | C | OAF activity raises MAMLD1's level | lines that do not express OAF (4) vs lines expressing it (46) | 3.70× lower at baseline in the lines without OAF | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| [[MLKL]] | C | OAF activity raises MLKL's level | lines that do not express OAF (4) vs lines expressing it (46) | 3.24× lower at baseline in the lines without OAF | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| [[FOSL1]] | C | OAF activity raises FOSL1's level | lines that do not express OAF (4) vs lines expressing it (46) | 3.40× lower at baseline in the lines without OAF | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent; co-absent with the target |
| [[PLAUR]] | C | OAF activity raises PLAUR's level | lines that do not express OAF (4) vs lines expressing it (46) | 4.25× lower at baseline in the lines without OAF | 0.037 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| [[FXYD5]] | C | OAF activity raises FXYD5's level | lines that do not express OAF (4) vs lines expressing it (46) | 3.86× lower at baseline in the lines without OAF | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| [[PREX1]] | C | OAF activity lowers PREX1's level | lines that do not express OAF (4) vs lines expressing it (46) | 5.59× higher at baseline in the lines without OAF | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| [[MED12L]] | C | OAF activity lowers MED12L's level | lines that do not express OAF (4) vs lines expressing it (46) | 4.23× higher at baseline in the lines without OAF | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| [[PTPRE]] | C | OAF activity raises PTPRE's level | lines that do not express OAF (4) vs lines expressing it (46) | 4.35× lower at baseline in the lines without OAF | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| [[EHD1]] | C | OAF activity raises EHD1's level | lines that do not express OAF (4) vs lines expressing it (46) | 1.28× lower at baseline in the lines without OAF | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| cells under [[MK-3903 (drug)]] 0.05 µM | C | OAF activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express OAF (4) vs lines expressing it (44) | the lines without OAF: 0.79× the cells of the other lines | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |
| [[POU2F2]] | C | OAF activity raises POU2F2's level | lines that do not express OAF (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without OAF | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL3, LRP1, ALPK1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.4, -0.4); signed map (0.1, 53.1). **Vector** length 103, 24.3% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.5 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.5 | +3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.4 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -8.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | out at first homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:120,211,032-120,230,334 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC52117 |
| Gene groups (HGNC) | BRICHOS domain containing |
| Matched by | ensembl_id |

UniProt [Q86UD1](https://www.uniprot.org/uniprotkb/Q86UD1) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28752) · Entrez [220323](https://www.ncbi.nlm.nih.gov/gene/220323) · UniProt [Q86UD1](https://www.uniprot.org/uniprotkb/Q86UD1) · Ensembl [ENSG00000184232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184232)

## Data

Gene col 11509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11509); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11509]; `tensor/DDL_lfc|DDL_z.npy` [11509]; `embed/gene_vectors.npy` [11509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11509 or target_col == 11509). Every well: [[OAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
