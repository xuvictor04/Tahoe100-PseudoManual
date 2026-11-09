---
symbol: "ELAVL2"
type: "gene"
col: 2826
ensembl_id: "ENSG00000107105"
name: "ELAV like RNA binding protein 2"
location: "9p21.3"
module: 61
arm: "+"
pooled_cpm: 11.34
n_lines_expressing: 16
n_dd_up: 41
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ELAVL2

*ELAV like RNA binding protein 2* — 9p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.87× (z +18.4, q 0e+00, up in 11 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.628× (z -5.8, q 5e-06, down in 3 of 14 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHST8]] (+0.65, fdr 1e-05), [[SH3GL2]] (+0.62, fdr 9e-06), [[CDH18]] (+0.62, fdr 1e-05); moves opposite to [[XPNPEP3]] (-0.51, fdr 6e-05), [[CEP104]] (-0.45, fdr 7e-04), [[DNAJC16]] (-0.44, fdr 8e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PLCE1]] → it (grade B ⚠); 7 go from it, the strongest it → [[CCDC85A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.87×** | +18.4 | 0e+00 | 11/13 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +15.3 | 0e+00 | 13/14 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +15.2 | 0e+00 | 4/12 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.61×** | +11.4 | 5e-28 | 0/6 | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.44×** | +11.0 | 3e-26 | 4/11 (SW 900, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.14×** | +9.4 | 4e-19 | 7/13 (NCI-H460, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.14×** | +9.4 | 4e-19 | 13/14 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.96×** | +8.3 | 5e-15 | 12/14 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.94×** | +8.2 | 2e-14 | 11/14 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +8.1 | 5e-14 | 9/12 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.91×** | +7.4 | 6e-12 | 2/7 (NCI-H460, A498) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.71×** | +6.6 | 2e-09 | 8/14 (J82, NCI-H460, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.5 | 3e-09 | 7/14 (A498, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +5.4 | 3e-06 | 11/14 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.56×** | +5.3 | 5e-06 | 8/13 (J82, A498, …) | rises with dose | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.48×** | +4.8 | 4e-05 | 0/14 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +4.8 | 5e-05 | 2/14 (NCI-H460, SW 900) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.003 | 1/14 (NCI-H460) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.006 | 1/11 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.016 | 7/14 (A498, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.027 | 4/14 (NCI-H460, A-172, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.040 | 0/13 | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.29×** | +2.9 | 0.055 | 1/14 (H4) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.628×** | -5.8 | 5e-06 | 3/14 (SW 900, C-33 A, …) | two highest doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.715×** | -3.8 | 0.034 | 2/14 (A-172, CHP-212) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.742×** | -3.4 | 0.067 | 0/14 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.761×** | -3.4 | 0.067 | 2/14 (A-172, A498) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.762×** | -3.4 | 0.067 | 2/14 (SW 900, A-172) | inconsistent across doses |  |
| [[Quinestrol (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.067 | 1/14 (C-33 A) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.685×** | -3.3 | 0.067 | 0/14 | inconsistent across doses | noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.753×** | -3.2 | 0.082 | 0/14 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.759×** | -3.2 | 0.099 | 0/14 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.0 | 0.13 | 1/14 (C-33 A) | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | 0.776× | -3.0 | 0.13 | 1/14 (H4) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +17.7) | — |
| [[A-172 (line)]] | wt | 8.34 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +14.0) | — |
| [[J82 (line)]] | alt | 84.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +19.3) | — |
| [[NCI-H460 (line)]] | wt | 3.66 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.66× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 180 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.1) |
| [[SW 900 (line)]] | alt | 3.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +10.4) | — |
| [[A-427 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHST8]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SH3GL2]] | +0.62 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[CDH18]] | +0.62 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[FMN2]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CA8]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ANOS2P]] | +0.59 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[LHX2]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[CAMK4]] | +0.58 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[RGS7]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 | STRING 432 |
| [[CHRM3]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[CCDC85A]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[CDH12]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPNPEP3]] | -0.51 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[CEP104]] | -0.45 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[DNAJC16]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCE1]] | B | PLCE1 activity lowers ELAVL2's level | lines that do not express PLCE1 (16) vs lines expressing it (34) | 1.87× higher at baseline in the lines without PLCE1 | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC46A3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ELAVL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PGBD5]] | C | PGBD5 activity raises ELAVL2's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without PGBD5 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2; co-absent with the target |
| [[RAB39A]] | C | RAB39A activity raises ELAVL2's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without RAB39A | 0.089 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; co-absent with the target |
| [[POU3F2]] | C | POU3F2 activity raises ELAVL2's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 2.60× lower at baseline in the lines without POU3F2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC85A]] | B | ELAVL2 activity raises CCDC85A's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.69× lower at baseline in the lines without ELAVL2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10 |
| [[ERC2]] | B | ELAVL2 activity raises ERC2's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 3.07× lower at baseline in the lines without ELAVL2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10 |
| [[SPTB]] | B | ELAVL2 activity raises SPTB's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without ELAVL2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10 |
| [[RGS7]] | C | ELAVL2 activity raises RGS7's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 3.36× lower at baseline in the lines without ELAVL2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10; co-absent with the target |
| [[CELF4]] | C | ELAVL2 activity raises CELF4's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.00× lower at baseline in the lines without ELAVL2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10; co-absent with the target |
| [[STXBP5L]] | C | ELAVL2 activity raises STXBP5L's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without ELAVL2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10; co-absent with the target |
| [[PGBD5]] | C | ELAVL2 activity raises PGBD5's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.74× lower at baseline in the lines without ELAVL2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, 32.6); signed map (33.3, 26.0). **Vector** length 42.2, 11.0% of its response variance represented; |z| ≥ 3 in 373 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.0 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +3.7 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.4 | +11.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +4.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -3.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -5.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ELAV like RNA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.3 — chr9:23,690,104-23,826,337 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HuB, HEL-N1 |
| Gene groups (HGNC) | RNA binding motif containing; ELAV like RNA binding protein family |
| Reactome | 3 pathways, smallest: Dengue Virus-Host Interactions; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12926](https://www.uniprot.org/uniprotkb/Q12926) (ELAV-like protein 2):

> RNA-binding protein that binds to the 3' untranslated region (3'UTR) of target mRNAs (By similarity). Seems to recognize a GAAA motif (By similarity). Can bind to its own 3'UTR, the FOS 3'UTR and the ID 3'UTR (By similarity).

**Summary**, from NCBI Gene [1993](https://www.ncbi.nlm.nih.gov/gene/1993):

> In humans, the ELAV like RNA binding protein gene family has four members (ELAVL1-4). ELAVL RNA binding proteins recognize AU-rich elements in the 3' UTRs of gene transcripts and thereby regulate gene expression post-transcriptionally. The protein encoded by this gene binds to several 3' UTRs, including its own and also that of FOS, ID, and POU5F1. This gene encodes ELAVL2 and, like ELAVL3 and ELAVL4, is expressed specifically in neurons and primarily localizes to the cytoplasm. This protein …

**Accessions** — [HGNC:3313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3313) · Entrez [1993](https://www.ncbi.nlm.nih.gov/gene/1993) · UniProt [Q12926](https://www.uniprot.org/uniprotkb/Q12926) · Ensembl [ENSG00000107105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107105)

## Data

Gene col 2826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2826); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2826]; `tensor/DDL_lfc|DDL_z.npy` [2826]; `embed/gene_vectors.npy` [2826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2826 or target_col == 2826). Every well: [[ELAVL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELAVL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
