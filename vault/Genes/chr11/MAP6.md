---
symbol: "MAP6"
type: "gene"
col: 10128
ensembl_id: "ENSG00000171533"
name: "microtubule associated protein 6"
location: "11q13.5"
module: 82
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 28
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# MAP6

*microtubule associated protein 6* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.13× (z +14.0, q 1e-41, up in 19 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.511× (z -5.8, q 2e-06, down in 15 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB6B]] (+0.66, fdr 7e-06), [[MCF2L2]] (+0.65, fdr 1e-05), [[LPAR3]] (+0.65, fdr 1e-05); moves opposite to [[ELP4]] (-0.50, fdr 1e-04), [[RFX3]] (-0.50, fdr 8e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CCDC33]] → it (grade B ⚠); 8 go from it, the strongest it → [[ESYT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.13×** | +14.0 | 1e-41 | 19/22 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +12.8 | 2e-35 | 7/18 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.16×** | +11.9 | 3e-30 | 1/2 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +9.2 | 3e-18 | 2/6 (SW 900, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.78×** | +8.9 | 9e-17 | 16/19 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +7.8 | 7e-13 | 4/11 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +6.4 | 1e-08 | 14/23 (NCI-H1573, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +6.2 | 4e-08 | 3/18 (NCI-H2347, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +6.0 | 1e-07 | 11/18 (NCI-H1573, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +5.7 | 6e-07 | 14/22 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.37×** | +5.3 | 5e-06 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +4.3 | 8e-04 | 9/19 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.32×** | +3.8 | 0.006 | 1/5 (SW480) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +3.6 | 0.012 | 8/20 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.035 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.035 | 0/15 | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.41×** | +3.0 | 0.080 | 8/21 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.080 | 1/20 (NCI-H460) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +2.9 | 0.085 | 0/17 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10128.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -5.8 | 2e-06 | 15/23 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.512×** | -5.8 | 2e-06 | 14/19 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.611×** | -4.3 | 0.003 | 10/24 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.617×** | -4.1 | 0.007 | 8/20 (A-172, NCI-H23, …) | top dose only | composition shift |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.667×** | -3.3 | 0.095 | 2/21 (HOP62, PANC-1) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.600× | -3.2 | 0.14 | 3/23 (SW 900, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -3.1 | 0.15 | 6/24 (SW 900, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 33.1 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0985× (z -23.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 5.92 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0732× (z -8.6) |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0791× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 4.06 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.49× (z +9.4) | — |
| [[A-427 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.750 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.759 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.671 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.364 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6B]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[MCF2L2]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[LPAR3]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SULT4A1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[KIF5A]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[FAM124A]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[KIF5C]] | +0.64 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[BRSK2]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NOVA2]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PDZD4]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[DPYSL5]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[HAGLR]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP4]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[RFX3]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC33]] | B | CCDC33 activity raises MAP6's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without CCDC33 | 0.034 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[DOC2A]] | B | DOC2A activity raises MAP6's level | lines that do not express DOC2A (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without DOC2A | 0.039 | ⚠ within organs, on part of the lines; also absent: C12orf56, ENSG00000267405; maybe low, not absent |
| [[SLC45A1]] | B | SLC45A1 activity raises MAP6's level | lines that do not express SLC45A1 (19) vs lines expressing it (31) | 2.01× lower at baseline in the lines without SLC45A1 | 0.078 | ⚠ within organs, on part of the lines; also absent: LRRC34, PNMA2, SSTR2 |
| [[CHD5]] | B | CHD5 activity raises MAP6's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without CHD5 | 0.092 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[ZFP28]] | C | ZFP28 activity raises MAP6's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 2.48× lower at baseline in the lines without ZFP28 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6; co-absent with the target |
| [[SLC66A1L]] | C | SLC66A1L activity raises MAP6's level | lines that do not express SLC66A1L (25) vs lines expressing it (25) | 1.86× lower at baseline in the lines without SLC66A1L | 0.015 | ⚠ within organs, on part of the lines; also absent: MIR137HG, ADAMTS12, SLC8A1; co-absent with the target |
| [[RASSF2]] | C | RASSF2 activity raises MAP6's level | lines that do not express RASSF2 (16) vs lines expressing it (34) | 2.24× lower at baseline in the lines without RASSF2 | 0.020 | ⚠ within organs, on part of the lines; also absent: HDGFL3, MARK1, RFPL1S; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises MAP6's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.30× lower at baseline in the lines without KIF1A | 0.023 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[ZNF71]] | C | ZNF71 activity raises MAP6's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.15× lower at baseline in the lines without ZNF71 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESYT3]] | B | MAP6 activity raises ESYT3's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without MAP6 | 0.050 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91 |
| [[ZIM2-AS1]] | B | MAP6 activity raises ZIM2-AS1's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 2.36× lower at baseline in the lines without MAP6 | 0.051 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91 |
| [[GRB14]] | B | MAP6 activity lowers GRB14's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 1.35× higher at baseline in the lines without MAP6 | 0.054 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91 |
| [[CDH23]] | B | MAP6 activity strengthens CDH23's drug response | lines that do not express MAP6 (22) vs lines expressing it (24) | the lines without MAP6 respond 0.60× as strongly (z diff +0.97); strongest at Panobinostat 0.05 µM: 1.30x vs 2.35x (z diff +2.2) | 0.068 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91; target measured in part of the lines; artifact flags |
| [[SLC66A1L]] | C | MAP6 activity raises SLC66A1L's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 1.52× lower at baseline in the lines without MAP6 | 0.030 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91; co-absent with the target |
| [[ZFP28]] | C | MAP6 activity raises ZFP28's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 4.26× lower at baseline in the lines without MAP6 | 0.048 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91; co-absent with the target |
| [[ZNF71]] | C | MAP6 activity raises ZNF71's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 2.87× lower at baseline in the lines without MAP6 | 0.049 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91; co-absent with the target |
| [[CACNG4]] | C | MAP6 activity raises CACNG4's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 2.39× lower at baseline in the lines without MAP6 | 0.078 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.0, 40.1); signed map (26.2, 29.0). **Vector** length 43.3, 8.68% of its response variance represented; |z| ≥ 3 in 575 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +14.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.0 | -4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.9 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:75,586,918-75,669,038 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1878, STOP, FLJ41346, MAP6-N |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JE9](https://www.uniprot.org/uniprotkb/Q96JE9) (Microtubule-associated protein 6):

> Involved in microtubule stabilization in many cell types, including neuronal cells (By similarity). Specifically has microtubule cold stabilizing activity (By similarity). Involved in dendrite morphogenesis and maintenance by regulating lysosomal trafficking via its interaction with TMEM106B. Regulates KIF5A-mediated axonal cargo transport (By similarity). Regulates axonal growth during neuron polarization (By similarity).

**Summary**, from NCBI Gene [4135](https://www.ncbi.nlm.nih.gov/gene/4135):

> This gene encodes a microtubule-associated protein. The encoded protein is a calmodulin-binding and calmodulin-regulated protein that is involved in microtubule stabilization. Two transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6868) · Entrez [4135](https://www.ncbi.nlm.nih.gov/gene/4135) · UniProt [Q96JE9](https://www.uniprot.org/uniprotkb/Q96JE9) · Ensembl [ENSG00000171533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171533)

## Data

Gene col 10128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10128); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10128]; `tensor/DDL_lfc|DDL_z.npy` [10128]; `embed/gene_vectors.npy` [10128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10128 or target_col == 10128). Every well: [[MAP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
