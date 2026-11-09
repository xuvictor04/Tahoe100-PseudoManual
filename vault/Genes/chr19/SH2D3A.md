---
symbol: "SH2D3A"
type: "gene"
col: 4649
ensembl_id: "ENSG00000125731"
name: "SH2 domain containing 3A"
location: "19p13.3"
module: 141
arm: "+"
pooled_cpm: 23.49
n_lines_expressing: 26
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 70
direction_downstream: 89
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# SH2D3A

*SH2 domain containing 3A* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.91× (z +7.8, q 3e-12, up in 4 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +6.3, q 1e-07, up in 12 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.895× (z -5.1, q 2e-04, down in 3 of 25 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.682× (z -4.5, q 0.002, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA2-AS1]] (+0.75, fdr 7e-06), [[MST1R]] (+0.70, fdr 7e-06), [[GJB3]] (+0.68, fdr 7e-06); moves opposite to [[CSDE1]] (-0.51, fdr 5e-05), [[METTL4]] (-0.49, fdr 1e-04).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 70 arrows point to it, the strongest [[EPS8L1]] → it (grade B ⚠); 89 go from it, the strongest it → [[PTK2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.8 | 3e-12 | 4/19 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +6.3 | 1e-07 | 12/24 (A498, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.4 | 2e-05 | 3/22 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +5.2 | 3e-05 | 11/24 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +4.6 | 6e-04 | 7/24 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +4.3 | 0.002 | 4/19 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.0 | 0.006 | 8/24 (A498, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.009 | 6/24 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.022 | 6/24 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.022 | 9/24 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.049 | 2/25 (SW480, HCT15) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.1 | 0.088 | 6/23 (KATO III, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -5.1 | 2e-04 | 3/25 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.682×** | -4.5 | 0.002 | 14/24 (SW480, HCT15, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.695×** | -4.4 | 0.002 | 15/24 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -4.4 | 0.002 | 15/24 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.708×** | -4.4 | 0.002 | 16/25 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.719×** | -4.0 | 0.006 | 16/24 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.776×** | -4.0 | 0.006 | 18/24 (SW480, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.733×** | -3.9 | 0.006 | 15/25 (NCI-H1573, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.798×** | -3.9 | 0.006 | 11/24 (SW480, HCT15, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.748×** | -3.7 | 0.015 | 13/24 (SW480, HCT15, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.018 | 19/24 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.023 | 14/24 (HCT15, HT-29, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.750×** | -3.3 | 0.036 | 6/24 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.629×** | -3.1 | 0.089 | 2/24 (COLO 205, SK-MEL-2) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -3.0 | 0.089 | 16/23 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 39.5 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 72.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.3) |
| [[COLO 205 (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.127× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -23.8) |
| [[HT-29 (line)]] | alt | 64.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -17.3) |
| [[LoVo (line)]] | wt | 52.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 54.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -11.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.5) |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 7.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 48.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -13.2) |
| [[SW48 (line)]] | wt | 38.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -15.2) |
| [[A-172 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA2-AS1]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GJB3]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[TMC6]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.67 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.67 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[LINC00659]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[TNS4]] | +0.66 | +0.60 / +0.70 | both halves | 7e-06 | same gene group |
| [[RDH13]] | +0.65 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SDR16C5]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[CBLC]] | +0.63 | +0.45 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | -0.51 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[METTL4]] | -0.49 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*70 arrows, 70 of them with an alert ⚠; grade A 0, B 18, C 52. Shown: the 12 strongest; 58 more arrows (58 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | EPS8L1 activity raises SH2D3A's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.53× lower at baseline in the lines without EPS8L1 | 0.007 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[CCDC120]] | B | CCDC120 activity raises SH2D3A's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 3.96× lower at baseline in the lines without CCDC120 | 0.017 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[PRAG1]] | B | PRAG1 activity raises SH2D3A's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 3.30× lower at baseline in the lines without PRAG1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[PDE9A]] | B | PDE9A activity raises SH2D3A's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 3.58× lower at baseline in the lines without PDE9A | 0.024 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[LINC02320]] | B | LINC02320 activity raises SH2D3A's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 3.34× lower at baseline in the lines without LINC02320 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[SEMA3B]] | B | SEMA3B activity raises SH2D3A's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without SEMA3B | 0.039 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[UNC13D]] | B | UNC13D activity raises SH2D3A's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.60× lower at baseline in the lines without UNC13D | 0.042 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises SH2D3A's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.19× lower at baseline in the lines without TJP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises SH2D3A's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.20× lower at baseline in the lines without GPRC5A | 0.045 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[ITGA6]] | B | ITGA6 activity raises SH2D3A's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 3.21× lower at baseline in the lines without ITGA6 | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PTK2B]] | B | PTK2B activity raises SH2D3A's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.22× lower at baseline in the lines without PTK2B | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PPL]] | B | PPL activity raises SH2D3A's level | lines that do not express PPL (19) vs lines expressing it (31) | 3.65× lower at baseline in the lines without PPL | 0.053 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |

### Downstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 45, C 44. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTK2B]] | B | SH2D3A activity raises PTK2B's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.32× lower at baseline in the lines without SH2D3A | 5e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[EPS8L1]] | B | SH2D3A activity raises EPS8L1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.67× lower at baseline in the lines without SH2D3A | 6e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[KRT8]] | B | SH2D3A activity raises KRT8's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 4.13× lower at baseline in the lines without SH2D3A | 1e-03 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[PARD6B]] | B | SH2D3A activity raises PARD6B's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.27× lower at baseline in the lines without SH2D3A | 1e-03 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[CCDC120]] | B | SH2D3A activity raises CCDC120's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.67× lower at baseline in the lines without SH2D3A | 0.001 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[TMC6]] | B | SH2D3A activity raises TMC6's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.88× lower at baseline in the lines without SH2D3A | 0.001 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[TICAM1]] | B | SH2D3A activity raises TICAM1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without SH2D3A | 0.002 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[ACOT11]] | B | SH2D3A activity raises ACOT11's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.67× lower at baseline in the lines without SH2D3A | 0.003 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[BAIAP2L1]] | B | SH2D3A activity raises BAIAP2L1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.18× lower at baseline in the lines without SH2D3A | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[EZR]] | B | SH2D3A activity raises EZR's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without SH2D3A | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[ITGA6]] | B | SH2D3A activity raises ITGA6's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.75× lower at baseline in the lines without SH2D3A | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[BAIAP2L2]] | B | SH2D3A activity raises BAIAP2L2's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.63× lower at baseline in the lines without SH2D3A | 0.005 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.4, 51.2); signed map (4.3, 38.0). **Vector** length 87.2, 29.3% of its response variance represented; |z| ≥ 3 in 557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.9 | +3.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.6 | -4.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.5 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | SH2 domain containing 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,752,160-6,767,463 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NSP1 |
| Gene groups (HGNC) | SH2 domain containing; NSP adaptor proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRG2](https://www.uniprot.org/uniprotkb/Q9BRG2) (SH2 domain-containing protein 3A):

> May play a role in JNK activation.

**Summary**, from NCBI Gene [10045](https://www.ncbi.nlm.nih.gov/gene/10045):

> Predicted to enable guanyl-nucleotide exchange factor activity and phosphotyrosine residue binding activity. Predicted to be involved in JNK cascade. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16885) · Entrez [10045](https://www.ncbi.nlm.nih.gov/gene/10045) · UniProt [Q9BRG2](https://www.uniprot.org/uniprotkb/Q9BRG2) · Ensembl [ENSG00000125731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125731)

## Data

Gene col 4649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4649); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4649]; `tensor/DDL_lfc|DDL_z.npy` [4649]; `embed/gene_vectors.npy` [4649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4649 or target_col == 4649). Every well: [[SH2D3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH2D3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
