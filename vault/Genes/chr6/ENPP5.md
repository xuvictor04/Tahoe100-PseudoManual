---
symbol: "ENPP5"
type: "gene"
col: 3408
ensembl_id: "ENSG00000112796"
name: "ectonucleotide pyrophosphatase/phosphodiesterase family member 5"
location: "6p21.1"
module: 27
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 23
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 34
direction_downstream: 52
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ENPP5

*ectonucleotide pyrophosphatase/phosphodiesterase family member 5* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.01× (z +12.6, q 9e-34, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 4.26× (z +11.8, q 1e-29, up in 19 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.402× (z -7.4, q 5e-11, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BSPRY]] (+0.71, fdr 1e-05), [[TJP3]] (+0.68, fdr 7e-06), [[LINC01814]] (+0.66, fdr 7e-06); moves opposite to [[SPRY3]] (-0.54, fdr 7e-05), [[UBTF]] (-0.51, fdr 1e-04), [[SETD1B]] (-0.49, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 34 arrows point to it, the strongest [[LMTK3]] → it (grade B ⚠); 52 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.01×** | +12.6 | 9e-34 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **4.26×** | +11.8 | 1e-29 | 19/21 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.64×** | +11.2 | 1e-26 | 17/20 (NCI-H2347, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +10.4 | 4e-23 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.54×** | +10.3 | 8e-23 | 18/20 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.49×** | +9.4 | 4e-19 | 1/6 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.95×** | +8.8 | 1e-16 | 15/20 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.64×** | +7.9 | 2e-13 | 18/20 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.91×** | +7.5 | 5e-12 | 12/20 (LS 180, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.34×** | +6.9 | 2e-10 | 13/19 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.92×** | +6.2 | 3e-08 | 1/8 (NCI-H2347) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +6.0 | 8e-08 | 0/17 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.71×** | +4.3 | 6e-04 | 11/19 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.46×** | +3.8 | 0.005 | 0/8 | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.43×** | +3.8 | 0.006 | 8/20 (SW480, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.52×** | +3.4 | 0.023 | 1/16 (BT-474) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.033 | 2/16 (LoVo, HT-29) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.2 | 0.045 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.084 | 6/19 (C-33 A, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.086 | 5/20 (LS 180, LoVo, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.086 | 1/19 (SW48) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -7.4 | 5e-11 | 18/20 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.476×** | -6.1 | 4e-07 | 17/20 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -3.9 | 0.017 | 9/20 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.628×** | -3.7 | 0.034 | 11/19 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.87 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0785× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 5.34 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0470× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 8.60 | 0 | 2 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0575× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 6.74 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0663× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 2.38 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0481× (z -8.5) |
| [[LS 180 (line)]] | wt | 5.00 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0397× (z -10.9) |
| [[A-172 (line)]] | wt | 0.247 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.788 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.721 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BSPRY]] | +0.71 | +0.75 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[TJP3]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[LINC01814]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[LINC00299]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ENPP4]] | +0.62 | +0.47 / +0.67 | both halves | 2e-05 | same gene group; ⚠ same locus (12.5 kb: neighbours can correlate without regulation) |
| [[ILDR1]] | +0.62 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[TMEM139]] | +0.61 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[RORC]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SYNPR-AS1]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[MAP2K6]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[GALM]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[GPR160]] | +0.58 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[USH1C]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY3]] | -0.54 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[UBTF]] | -0.51 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[SETD1B]] | -0.49 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ANKMY1]] | -0.48 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[MCPH1-AS1]] | -0.48 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[AVEN]] | -0.48 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[ANXA2R-OT1]] | -0.47 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[CDR2]] | -0.47 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[DNAAF10]] | -0.47 | -0.29 / -0.37 | both halves | 3e-04 |  |
| [[PHF2]] | -0.47 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[PCBP1-AS1]] | -0.46 | -0.24 / -0.41 | both halves | 5e-04 |  |
| [[EFCAB2]] | -0.46 | -0.23 / -0.49 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 5, C 29. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | LMTK3 activity raises ENPP5's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without LMTK3 | 0.031 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[NMNAT3]] | B | NMNAT3 activity raises ENPP5's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.92× lower at baseline in the lines without NMNAT3 | 0.037 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[KLHL32]] | B | KLHL32 activity raises ENPP5's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.48× lower at baseline in the lines without KLHL32 | 0.041 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity raises ENPP5's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.36× lower at baseline in the lines without MCF2L | 0.046 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[CYFIP2]] | B | CYFIP2 activity raises ENPP5's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.32× lower at baseline in the lines without CYFIP2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[TMEM125]] | C | TMEM125 activity raises ENPP5's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.86× lower at baseline in the lines without TMEM125 | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises ENPP5's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.55× lower at baseline in the lines without ATP2C2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises ENPP5's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.96× lower at baseline in the lines without BSPRY | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[ERBB3]] | C | ERBB3 activity raises ENPP5's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.15× lower at baseline in the lines without ERBB3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; co-absent with the target |
| [[SMPDL3B]] | C | SMPDL3B activity raises ENPP5's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.88× lower at baseline in the lines without SMPDL3B | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises ENPP5's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 3.36× lower at baseline in the lines without RAB25 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[FAAH2]] | C | FAAH2 activity raises ENPP5's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.60× lower at baseline in the lines without FAAH2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 19, C 33. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | ENPP5 activity raises LMTK3's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without ENPP5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[GPR160]] | B | ENPP5 activity raises GPR160's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.46× lower at baseline in the lines without ENPP5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[TMEM92]] | B | ENPP5 activity raises TMEM92's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.36× lower at baseline in the lines without ENPP5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[SLC7A8]] | B | ENPP5 activity raises SLC7A8's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.59× lower at baseline in the lines without ENPP5 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[CDK18]] | B | ENPP5 activity raises CDK18's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without ENPP5 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[ARRB2]] | B | ENPP5 activity lowers ARRB2's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.20× higher at baseline in the lines without ENPP5 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[CNGA1]] | B | ENPP5 activity raises CNGA1's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.64× lower at baseline in the lines without ENPP5 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[CHST9]] | B | ENPP5 activity raises CHST9's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.31× lower at baseline in the lines without ENPP5 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[MCF2L]] | B | ENPP5 activity raises MCF2L's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without ENPP5 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[SRI]] | B | ENPP5 activity raises SRI's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.35× lower at baseline in the lines without ENPP5 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[YPEL2]] | B | ENPP5 activity raises YPEL2's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.68× lower at baseline in the lines without ENPP5 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[MGAT4A]] | B | ENPP5 activity raises MGAT4A's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without ENPP5 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.406). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 48.3); signed map (55.5, 3.8). **Vector** length 56.3, 15.3% of its response variance represented; |z| ≥ 3 in 542 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +2.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.0 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleotide pyrophosphatase/phosphodiesterase family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:46,159,185-46,170,980 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ectonucleotide pyrophosphatase/phosphodiesterase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJA9](https://www.uniprot.org/uniprotkb/Q9UJA9) (Ectonucleotide pyrophosphatase/phosphodiesterase family member 5):

> Can hydrolyze NAD but cannot hydrolyze nucleotide di- and triphosphates. Lacks lysopholipase D activity. May play a role in neuronal cell communication.

**Summary**, from NCBI Gene [59084](https://www.ncbi.nlm.nih.gov/gene/59084):

> This gene encodes a type-I transmembrane glycoprotein. Studies in rat suggest the encoded protein may play a role in neuronal cell communications. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:13717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13717) · Entrez [59084](https://www.ncbi.nlm.nih.gov/gene/59084) · UniProt [Q9UJA9](https://www.uniprot.org/uniprotkb/Q9UJA9) · Ensembl [ENSG00000112796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112796)

## Data

Gene col 3408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3408); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3408]; `tensor/DDL_lfc|DDL_z.npy` [3408]; `embed/gene_vectors.npy` [3408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3408 or target_col == 3408). Every well: [[ENPP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENPP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
