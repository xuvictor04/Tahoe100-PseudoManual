---
symbol: "ITGB3"
type: "gene"
col: 15178
ensembl_id: "ENSG00000259207"
name: "integrin subunit beta 3"
location: "17q21.32"
module: 13
arm: "+"
pooled_cpm: 42.88
n_lines_expressing: 25
n_dd_up: 6
n_dd_down: 47
n_dd_up_clean: 3
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 37
direction_downstream: 47
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ITGB3

*integrin subunit beta 3* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +6.7, q 8e-09, up in 5 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.36× (z +4.3, q 0.002, up in 9 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.260× (z -18.7, q 0e+00, down in 23 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB13]] (+0.80, fdr 7e-06, ⚠ same locus), [[COL13A1]] (+0.66, fdr 7e-06), [[HTR7]] (+0.66, fdr 7e-06), [[LOXL2]] (+0.63, fdr 7e-06); moves opposite to [[DLEU1]] (-0.44, fdr 1e-04), [[PEG10]] (-0.44, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[COL13A1]] → it (grade B ⚠); 47 go from it, the strongest it → [[SSH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +6.7 | 8e-09 | 5/19 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.7 | 8e-09 | 6/21 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +5.4 | 1e-05 | 4/19 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.3 | 0.002 | 9/23 (Panc 03.27, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 0.002 | 9/22 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.041 | 13/22 (SNU-423, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.20 | 11/23 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15178.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.260×** | -18.7 | 0e+00 | 23/23 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.229×** | -14.5 | 4e-45 | 23/23 (RPMI-7951, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.259×** | -12.8 | 5e-35 | 22/23 (SK-MEL-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.323×** | -11.1 | 2e-26 | 21/23 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.392×** | -9.2 | 4e-18 | 23/23 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.400×** | -8.9 | 6e-17 | 19/23 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.436×** | -8.1 | 3e-14 | 20/23 (J82, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.460×** | -7.6 | 2e-12 | 19/23 (hTERT-HPNE, HS-578T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.506×** | -6.6 | 3e-09 | 20/23 (CFPAC-1, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.635×** | -6.3 | 2e-08 | 18/23 (HEC-1-A, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.539×** | -6.0 | 8e-08 | 21/23 (NCI-H1792, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.541×** | -5.8 | 3e-07 | 19/20 (NCI-H1792, J82, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.589×** | -5.2 | 1e-05 | 15/23 (J82, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.567×** | -5.1 | 1e-05 | 9/23 (SK-MEL-2, C32, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.590×** | -5.0 | 3e-05 | 14/22 (SK-MEL-2, C32, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.385×** | -4.9 | 3e-05 | 18/20 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.609×** | -4.8 | 4e-05 | 14/23 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.706×** | -4.8 | 5e-05 | 20/23 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.616×** | -4.7 | 6e-05 | 17/23 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.662×** | -4.4 | 3e-04 | 12/23 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 398 | 0 | 22 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0607× (z -27.3) |
| [[SK-MEL-2 (line)]] | alt | 210 | 0 | 22 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0668× (z -27.3) |
| [[HS-578T (line)]] | alt | 133 | 0 | 21 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 147 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0414× (z -25.8) |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0161× (z -35.4) |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 13 (2 ⚠) | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.0210× (z -12.7) |
| [[J82 (line)]] | alt | 76.8 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0435× (z -26.9) |
| [[Hs 766T (line)]] | wt | 69.9 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0485× (z -24.6) |
| [[hTERT-HPNE (line)]] | wt | 191 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0655× (z -19.7) |
| [[SW 900 (line)]] | alt | 65.1 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0777× (z -19.1) |
| [[HEC-1-A (line)]] | alt | 64.4 | 1 (1 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.07× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -17.3) |
| [[Panc 03.27 (line)]] | alt | 30.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -14.7) |
| [[SNU-423 (line)]] | alt | 119 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0452× (z -25.9) |
| [[HOP62 (line)]] | alt | 29.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -17.9) |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0955× (z -19.9) |
| [[RPMI-7951 (line)]] | alt | 72.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0731× (z -20.9) |
| [[SW 1088 (line)]] | alt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0697× (z -11.8) |
| [[A549 (line)]] | wt | 12.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0832× (z -14.3) |
| [[H4 (line)]] | wt | 11.9 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0620× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 27.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -16.2) |
| [[A498 (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.77 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB13]] | +0.80 | +0.79 / +0.83 | both halves | 7e-06 | ⚠ same locus (9.5 kb, same strand: neighbours can correlate without regulation) |
| [[COL13A1]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[HTR7]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[LOXL2]] | +0.63 | +0.68 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[MTSS1]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[FAM20C]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[LTBP3]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 | pathway: Elastic fibre formation; STRING 552 |
| [[ADAM12]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[NAV1]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PLAT]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |
| [[ITGA3]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 979 |
| [[TGM2]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[RGS17]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU1]] | -0.44 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[PEG10]] | -0.44 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 6, C 31. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | COL13A1 activity raises ITGB3's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 4.58× lower at baseline in the lines without COL13A1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[CYGB]] | B | CYGB activity raises ITGB3's level | lines that do not express CYGB (20) vs lines expressing it (30) | 3.34× lower at baseline in the lines without CYGB | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[LINC02454]] | B | LINC02454 activity raises ITGB3's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 4.64× lower at baseline in the lines without LINC02454 | 0.067 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[RGS17]] | B | RGS17 activity raises ITGB3's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 4.12× lower at baseline in the lines without RGS17 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[RAI14]] | B | RAI14 activity raises ITGB3's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 4.93× lower at baseline in the lines without RAI14 | 0.086 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[ITGA3]] | B | ITGA3 activity raises ITGB3's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 4.31× lower at baseline in the lines without ITGA3 | 0.096 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[FRMD4A]] | C | FRMD4A activity raises ITGB3's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 6.74× lower at baseline in the lines without FRMD4A | 6e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[LINC02813]] | C | LINC02813 activity raises ITGB3's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 4.30× lower at baseline in the lines without LINC02813 | 0.005 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN; co-absent with the target |
| [[ADAMTS9-AS2]] | C | ADAMTS9-AS2 activity raises ITGB3's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 6.08× lower at baseline in the lines without ADAMTS9-AS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2; co-absent with the target |
| [[EFCAB13]] | C | EFCAB13 activity raises ITGB3's level | lines that do not express EFCAB13 (14) vs lines expressing it (36) | 5.89× lower at baseline in the lines without EFCAB13 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNS3, TRIM6, GPR176; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises ITGB3's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 6.48× lower at baseline in the lines without AEBP1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[LRAT]] | C | LRAT activity raises ITGB3's level | lines that do not express LRAT (30) vs lines expressing it (20) | 5.70× lower at baseline in the lines without LRAT | 0.012 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 20, C 27. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSH1]] | B | ITGB3 activity raises SSH1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without ITGB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[SMOX]] | B | ITGB3 activity raises SMOX's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.54× lower at baseline in the lines without ITGB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[ITPR1]] | B | ITGB3 activity raises ITPR1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.75× lower at baseline in the lines without ITGB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[COL13A1]] | B | ITGB3 activity raises COL13A1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.40× lower at baseline in the lines without ITGB3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[RGS17]] | B | ITGB3 activity raises RGS17's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.80× lower at baseline in the lines without ITGB3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[MLPH]] | B | ITGB3 activity raises MLPH's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.74× lower at baseline in the lines without ITGB3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[ITGA3]] | B | ITGB3 activity raises ITGA3's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.07× lower at baseline in the lines without ITGB3 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[WIPF1]] | B | ITGB3 activity raises WIPF1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.43× lower at baseline in the lines without ITGB3 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[EFCAB13-DT]] | B | ITGB3 activity raises EFCAB13-DT's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 1.35× lower at baseline in the lines without ITGB3 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[ITPR1]] | B | ITGB3 activity weakens ITPR1's drug response | lines that do not express ITGB3 (13) vs lines expressing it (21) | the lines without ITGB3 respond 1.27× as strongly (z diff -0.70); strongest at Panobinostat 0.5 µM: 2.32x vs 1.42x (z diff -3.6) | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; target measured in part of the lines; both ways; artifact flags |
| [[PPFIBP1]] | B | ITGB3 activity raises PPFIBP1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without ITGB3 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[PHC2]] | B | ITGB3 activity raises PHC2's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 1.47× lower at baseline in the lines without ITGB3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 7.0); signed map (6.3, 50.9). **Vector** length 117, 41.8% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.5 µM |  | +1.6 | +2.6 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -7.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -4.4 |
|  | [[NG25 (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,253,827-47,313,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD61, GPIIIa; previously GP3A |
| Gene groups (HGNC) | CD molecules; Integrin beta subunits; Human platelet antigens |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, COAGULATION, INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 47 pathways, smallest: Fibrin formation; PECAM1 interactions; GRB2:SOS provides linkage to MAPK signaling for Integrins |
| Matched by | ensembl_id |

**Function**, from UniProt [P05106](https://www.uniprot.org/uniprotkb/P05106) (Integrin beta-3):

> Integrin alpha-V/beta-3 (ITGAV:ITGB3) is a receptor for cytotactin, fibronectin, laminin, matrix metalloproteinase-2, osteopontin, osteomodulin, prothrombin, thrombospondin, vitronectin and von Willebrand factor (VWF). Integrin alpha-IIb/beta-3 (ITGA2B:ITGB3) is a receptor for fibronectin, fibrinogen, plasminogen, prothrombin, thrombospondin and vitronectin. Integrins alpha-IIb/beta-3 and alpha-V/beta-3 recognize the sequence R-G-D in a wide array of ligands. Integrin alpha-IIb/beta-3 …

**Summary**, from NCBI Gene [3690](https://www.ncbi.nlm.nih.gov/gene/3690):

> The ITGB3 protein product is the integrin beta chain beta 3. Integrins are integral cell-surface proteins composed of an alpha chain and a beta chain. A given chain may combine with multiple partners resulting in different integrins. Integrin beta 3 is found along with the alpha IIb chain in platelets. Integrins are known to participate in cell adhesion as well as cell-surface mediated signalling. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6156) · Entrez [3690](https://www.ncbi.nlm.nih.gov/gene/3690) · UniProt [P05106](https://www.uniprot.org/uniprotkb/P05106) · Ensembl [ENSG00000259207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259207)

## Data

Gene col 15178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15178); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15178]; `tensor/DDL_lfc|DDL_z.npy` [15178]; `embed/gene_vectors.npy` [15178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15178 or target_col == 15178). Every well: [[ITGB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
