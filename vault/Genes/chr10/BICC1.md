---
symbol: "BICC1"
type: "gene"
col: 4381
ensembl_id: "ENSG00000122870"
name: "BicC family RNA binding protein 1"
location: "10q21.1"
module: 167
arm: "+"
pooled_cpm: 92.81
n_lines_expressing: 22
n_dd_up: 20
n_dd_down: 16
n_dd_up_clean: 17
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 23
direction_downstream: 36
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# BICC1

*BicC family RNA binding protein 1* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.78× (z +10.5, q 3e-23, up in 13 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.583× (z -7.0, q 2e-09, down in 19 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEX41]] (+0.68, fdr 7e-06), [[CD38]] (+0.66, fdr 7e-06), [[LINC02015]] (+0.64, fdr 7e-06); moves opposite to [[NGEF]] (-0.41, fdr 5e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[SVEP1]] → it (grade B ⚠); 36 go from it, the strongest it → [[HIF1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4381.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +10.5 | 3e-23 | 13/20 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.9 | 1e-16 | 1/18 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +7.8 | 1e-12 | 3/20 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.7 | 2e-06 | 9/20 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.5 | 4e-06 | 2/20 (HOP62, H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.2 | 2e-05 | 3/18 (CHP-212, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.4 | 0.001 | 15/19 (HOP62, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 0.002 | 10/20 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.003 | 9/20 (Panc 03.27, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.004 | 12/20 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.009 | 3/20 (NCI-H1792, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.012 | 12/20 (HOP62, SW 900, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.017 | 9/20 (HOP62, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.017 | 5/20 (H4, CHP-212, …) | two highest doses |  |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.056 | 1/20 (hTERT-HPNE) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.074 | 6/20 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.074 | 15/19 (HOP62, A549, …) | rises with dose |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.098 | 8/20 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4381.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -7.0 | 2e-09 | 19/20 (hTERT-HPNE, HEC-1-A, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.661×** | -5.3 | 3e-05 | 17/20 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.672×** | -5.1 | 5e-05 | 14/20 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -5.0 | 1e-04 | 18/20 (hTERT-HPNE, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.683×** | -4.9 | 1e-04 | 7/19 (CHP-212, HOP62, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.702×** | -4.6 | 5e-04 | 15/20 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.710×** | -4.4 | 7e-04 | 10/20 (SW 900, NCI-H2030, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **0.785×** | -4.4 | 7e-04 | 10/20 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -4.1 | 0.002 | 16/19 (NCI-H2030, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Neratinib (drug)]] 5 µM |  | **0.766×** | -3.4 | 0.029 | 13/20 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.029 | 9/20 (SW 900, SNU-423, …) | top dose only | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.759×** | -3.4 | 0.030 | 1/20 (HOP62) | top dose only | plate-row cell shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.3 | 0.033 | 1/21 (SW 1088) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.773×** | -3.3 | 0.033 | 13/20 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.766×** | -3.3 | 0.033 | 9/19 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.033 | 17/20 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.792×** | -3.0 | 0.088 | 14/20 (NCI-H2030, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 62.7 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 647 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -16.8) |
| [[SW 900 (line)]] | alt | 170 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.217× (z -9.9) |
| [[C32 (line)]] | wt | 79.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 365 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.185× (z -8.8) |
| [[A549 (line)]] | wt | 280 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 258 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.277× (z -8.9) |
| [[HOP62 (line)]] | alt | 31.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.75× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.232× (z -9.6) |
| [[SNU-423 (line)]] | alt | 696 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -10.0) |
| [[SW480 (line)]] | alt | 88.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 22.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 21.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.88 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.37 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.41 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.68 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.77 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX41]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CD38]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LINC02015]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[CSGALNACT1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[SLC16A7]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 | **novel candidate** |
| [[CP]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PTGFR]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TGFB2]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TNS3]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[HTRA3]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 | **novel candidate** |
| [[PHLDB2]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PLD1]] | +0.53 | +0.40 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGEF]] | -0.41 | -0.39 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 4, C 19. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SVEP1]] | B | SVEP1 activity raises BICC1's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 3.00× lower at baseline in the lines without SVEP1 | 0.038 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[MEIS1]] | B | MEIS1 activity raises BICC1's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 5.00× lower at baseline in the lines without MEIS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[MAP2K1]] | B | MAP2K1 activity lowers BICC1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[RBPMS]] | B | RBPMS activity raises BICC1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 3.26× lower at baseline in the lines without RBPMS | 0.089 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[EYA4]] | C | EYA4 activity raises BICC1's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 5.14× lower at baseline in the lines without EYA4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA; co-absent with the target |
| [[TGFBI]] | C | TGFBI activity raises BICC1's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 4.12× lower at baseline in the lines without TGFBI | 0.013 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |
| [[ADAMTS9-AS2]] | C | ADAMTS9-AS2 activity raises BICC1's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 5.01× lower at baseline in the lines without ADAMTS9-AS2 | 0.019 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2; co-absent with the target |
| [[COL4A2]] | C | COL4A2 activity raises BICC1's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 4.70× lower at baseline in the lines without COL4A2 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |
| [[RHCG]] | C | RHCG activity raises BICC1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 3.74× lower at baseline in the lines without RHCG | 0.026 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises BICC1's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 4.47× lower at baseline in the lines without ADAM12 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[GLIS3]] | C | GLIS3 activity raises BICC1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 4.16× lower at baseline in the lines without GLIS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO; co-absent with the target |
| [[CNTNAP3]] | C | CNTNAP3 activity raises BICC1's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 3.24× lower at baseline in the lines without CNTNAP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 12, C 24. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HIF1A]] | B | BICC1 activity raises HIF1A's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without BICC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[RUNX2]] | B | BICC1 activity raises RUNX2's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.56× lower at baseline in the lines without BICC1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[SPTLC3]] | B | BICC1 activity raises SPTLC3's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without BICC1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[MEIS1]] | B | BICC1 activity raises MEIS1's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 3.02× lower at baseline in the lines without BICC1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[STARD13]] | B | BICC1 activity raises STARD13's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without BICC1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[LPAR1]] | B | BICC1 activity raises LPAR1's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 3.51× lower at baseline in the lines without BICC1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[GRIK2]] | B | BICC1 activity raises GRIK2's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.53× lower at baseline in the lines without BICC1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[RBPMS]] | B | BICC1 activity raises RBPMS's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without BICC1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[THBS1]] | B | BICC1 activity raises THBS1's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 3.67× lower at baseline in the lines without BICC1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[TNS3]] | B | BICC1 activity raises TNS3's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without BICC1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[SVEP1]] | B | BICC1 activity raises SVEP1's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.19× lower at baseline in the lines without BICC1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[FNDC3B]] | B | BICC1 activity raises FNDC3B's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 1.72× lower at baseline in the lines without BICC1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 21.5); signed map (50.6, 25.4). **Vector** length 85.0, 33.9% of its response variance represented; |z| ≥ 3 in 592 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +8.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -4.4 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.8 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | BicC family RNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:58,512,872-58,831,435 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H694](https://www.uniprot.org/uniprotkb/Q9H694) (Protein bicaudal C homolog 1):

> Putative RNA-binding protein. Acts as a negative regulator of Wnt signaling. May be involved in regulating gene expression during embryonic development.

**Summary**, from NCBI Gene [80114](https://www.ncbi.nlm.nih.gov/gene/80114):

> This gene encodes an RNA-binding protein that is active in regulating gene expression by modulating protein translation during embryonic development. Mouse studies identified the corresponding protein to be under strict control during cell differentiation and to be a maternally provided gene product. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:19351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19351) · Entrez [80114](https://www.ncbi.nlm.nih.gov/gene/80114) · UniProt [Q9H694](https://www.uniprot.org/uniprotkb/Q9H694) · Ensembl [ENSG00000122870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122870)

## Data

Gene col 4381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4381); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4381]; `tensor/DDL_lfc|DDL_z.npy` [4381]; `embed/gene_vectors.npy` [4381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4381 or target_col == 4381). Every well: [[BICC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BICC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
