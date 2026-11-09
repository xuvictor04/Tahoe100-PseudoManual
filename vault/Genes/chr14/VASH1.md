---
symbol: "VASH1"
type: "gene"
col: 982
ensembl_id: "ENSG00000071246"
name: "vasohibin 1"
location: "14q24.3"
module: 82
arm: "+"
pooled_cpm: 4.11
n_lines_expressing: 34
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 4
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 20
direction_downstream: 22
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# VASH1

*vasohibin 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +5.5, q 2e-05, up in 15 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.323× (z -14.1, q 1e-42, down in 25 of 28 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.217× (z -13.5, q 2e-39, down in 27 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZD4]] (+0.71, fdr 1e-05), [[SEPTIN3]] (+0.67, fdr 7e-06), [[SEPTIN5]] (+0.66, fdr 7e-06); moves opposite to [[N4BP2L2]] (-0.48, fdr 7e-05), [[COPZ1]] (-0.45, fdr 4e-05), [[FAM177B]] (-0.45, fdr 9e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); 22 go from it, the strongest it → [[F2R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 982.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +5.5 | 2e-05 | 15/31 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +4.6 | 7e-04 | 12/31 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +4.6 | 7e-04 | 3/7 (A-172, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.008 | 11/28 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.008 | 6/27 (A549, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 982.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.323×** | -14.1 | 1e-42 | 25/28 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.217×** | -13.5 | 2e-39 | 27/31 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.240×** | -12.6 | 3e-34 | 22/27 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.241×** | -12.6 | 3e-34 | 29/31 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.254×** | -12.1 | 7e-32 | 24/27 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.293×** | -10.1 | 7e-22 | 25/30 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.317×** | -9.8 | 9e-21 | 22/29 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.358×** | -9.1 | 7e-18 | 21/31 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.376×** | -8.7 | 3e-16 | 23/30 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.414×** | -7.8 | 3e-13 | 22/31 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.416×** | -7.8 | 4e-13 | 19/30 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.423×** | -7.6 | 1e-12 | 23/30 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.484×** | -6.2 | 3e-08 | 13/22 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.545×** | -5.1 | 2e-05 | 17/29 (MIA PaCa-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.351×** | -4.8 | 5e-05 | 10/30 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -4.6 | 2e-04 | 16/28 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.600×** | -4.5 | 2e-04 | 14/29 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.385×** | -4.4 | 3e-04 | 13/24 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 7.09 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0710× (z -19.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0309× (z -17.6) |
| [[A-427 (line)]] | wt | 18.5 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0164× (z -21.3) |
| [[MIA PaCa-2 (line)]] | alt | 9.39 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0263× (z -15.6) |
| [[NCI-H2030 (line)]] | alt | 6.35 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0952× (z -9.4) |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0277× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 5.53 | 0 | 3 (1 ⚠) | — | [[Bendamustine (drug)]] 5 µM 0.0759× (z -11.0) |
| [[HOP62 (line)]] | alt | 7.55 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -9.8) |
| [[C-33 A (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -10.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 2.20 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0367× (z -14.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0627× (z -8.8) |
| [[A-172 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -12.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 3.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0447× (z -10.1) |
| [[J82 (line)]] | alt | 3.12 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0659× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 3.13 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0362× (z -10.0) |
| [[SW480 (line)]] | alt | 3.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -9.4) |
| [[A498 (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.500 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZD4]] | +0.71 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[SEPTIN3]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SEPTIN5]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ADCY1]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[KIF26A]] | +0.64 | +0.70 / +0.37 | both halves | 8e-05 |  |
| [[GNAO1]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[JAKMIP1]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[GNAZ]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[FHL1]] | +0.59 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[EHD3]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[FSD1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ADAM22]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP2L2]] | -0.48 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[COPZ1]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[FAM177B]] | -0.45 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[GTF2IRD2]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[GTF2IRD2B]] | -0.43 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[SYNRG]] | -0.43 | -0.38 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 11, C 9. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises VASH1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without MCOLN2 | 0.025 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[DPYSL5]] | B | DPYSL5 activity raises VASH1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.21× lower at baseline in the lines without DPYSL5 | 0.030 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[ADD2]] | B | ADD2 activity raises VASH1's level | lines that do not express ADD2 (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without ADD2 | 0.040 | ⚠ within organs, on part of the lines; also absent: NEFL, CHST8, UCHL1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers VASH1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers VASH1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TERT]] | B | TERT activity raises VASH1's level | lines that do not express TERT (13) vs lines expressing it (37) | 2.48× lower at baseline in the lines without TERT | 0.069 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[GNAZ]] | B | GNAZ activity raises VASH1's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without GNAZ | 0.072 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[WT1-AS]] | B | WT1-AS activity raises VASH1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.84× lower at baseline in the lines without WT1-AS | 0.081 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises VASH1's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.92× lower at baseline in the lines without KDM2B-DT | 0.082 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[KIF26A]] | B | KIF26A activity raises VASH1's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.06× lower at baseline in the lines without KIF26A | 0.088 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[SEMA6B]] | B | SEMA6B activity raises VASH1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.91× lower at baseline in the lines without SEMA6B | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[RET]] | C | RET activity raises VASH1's level | lines that do not express RET (28) vs lines expressing it (22) | 3.23× lower at baseline in the lines without RET | 0.002 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 11, C 11. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2R]] | B | VASH1 activity raises F2R's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without VASH1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[SDC3]] | B | VASH1 activity raises SDC3's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without VASH1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[SLC4A3]] | B | VASH1 activity strengthens SLC4A3's drug response | lines that do not express VASH1 (11) vs lines expressing it (28) | the lines without VASH1 respond 0.55× as strongly (z diff +1.48); strongest at Idarubicin (hydrochloride) 5 µM: 0.64x vs 0.38x (z diff +2.9) | 0.037 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; target measured in part of the lines; artifact flags |
| [[SEPTIN5]] | B | VASH1 activity raises SEPTIN5's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without VASH1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[ANXA6]] | B | VASH1 activity raises ANXA6's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without VASH1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[KIF26A]] | B | VASH1 activity raises KIF26A's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.03× lower at baseline in the lines without VASH1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[CHST14]] | B | VASH1 activity raises CHST14's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without VASH1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[SMARCD3]] | B | VASH1 activity raises SMARCD3's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without VASH1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[ADD2]] | B | VASH1 activity raises ADD2's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 3.14× lower at baseline in the lines without VASH1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[TATDN2]] | B | VASH1 activity raises TATDN2's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 1.48× lower at baseline in the lines without VASH1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[TERT]] | B | VASH1 activity raises TERT's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without VASH1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[KHDC1-AS1]] | C | VASH1 activity raises KHDC1-AS1's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 3.38× lower at baseline in the lines without VASH1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.1, 39.7); signed map (26.2, 27.5). **Vector** length 59.3, 11.5% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.3 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +4.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.0 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.8 | -0.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +0.8 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -12.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.1 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -8.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | +0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | vasohibin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:76,761,468-76,783,015 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1036 |
| Gene groups (HGNC) | Vasohibin family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L8A9](https://www.uniprot.org/uniprotkb/Q7L8A9) (Tubulinyl-Tyr carboxypeptidase 1):

> Tyrosine carboxypeptidase that removes the C-terminal tyrosine residue of alpha-tubulin, thereby regulating microtubule dynamics and function. Critical for spindle function and accurate chromosome segregation during mitosis since microtubule detyrosination regulates mitotic spindle length and postioning. Acts as an angiogenesis inhibitor: inhibits migration, proliferation and network formation by endothelial cells as well as angiogenesis. This inhibitory effect is selective to endothelial cells …

**Summary**, from NCBI Gene [22846](https://www.ncbi.nlm.nih.gov/gene/22846):

> Enables actin binding activity and metallocarboxypeptidase activity. Involved in negative regulation of angiogenesis; negative regulation of blood vessel endothelial cell migration; and proteolysis. Acts upstream of or within several processes, including negative regulation of endothelial cell proliferation; negative regulation of lymphangiogenesis; and regulation of cellular senescence. Located in several cellular components, including apical part of cell; endoplasmic reticulum; and obsolete …

**Accessions** — [HGNC:19964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19964) · Entrez [22846](https://www.ncbi.nlm.nih.gov/gene/22846) · UniProt [Q7L8A9](https://www.uniprot.org/uniprotkb/Q7L8A9) · Ensembl [ENSG00000071246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071246)

## Data

Gene col 982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 982); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 982]; `tensor/DDL_lfc|DDL_z.npy` [982]; `embed/gene_vectors.npy` [982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 982 or target_col == 982). Every well: [[VASH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VASH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
