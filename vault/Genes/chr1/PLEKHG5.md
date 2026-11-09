---
symbol: "PLEKHG5"
type: "gene"
col: 10146
ensembl_id: "ENSG00000171680"
name: "pleckstrin homology and RhoGEF domain containing G5"
location: "1p36.31"
module: 34
arm: "+"
pooled_cpm: 19.8
n_lines_expressing: 45
n_dd_up: 0
n_dd_down: 39
n_dd_up_clean: 0
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PLEKHG5

*pleckstrin homology and RhoGEF domain containing G5* — 1p36.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.460× (z -13.6, q 3e-39, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF25]] (+0.78, fdr 7e-06, ⚠ same locus), [[PLEK2]] (+0.77, fdr 7e-06), [[ARID3B]] (+0.68, fdr 7e-06), [[PLAUR]] (+0.68, fdr 7e-06); moves opposite to [[TNS3]] (-0.62, fdr 1e-05), [[ZNF608]] (-0.58, fdr 8e-06), [[MTUS1-DT]] (-0.57, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[KCNN4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erythromycin (drug)]] 5 µM |  | 1.31× | +3.3 | 0.31 | 6/43 (COLO 205, NCI-H2030, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.66× | +3.2 | 0.31 | 15/39 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.31 | 19/42 (NCI-H460, LOX-IMVI, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.460×** | -13.6 | 3e-39 | 30/41 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.412×** | -11.0 | 1e-25 | 34/43 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -10.0 | 2e-21 | 31/40 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.432×** | -10.0 | 2e-21 | 30/42 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.448×** | -9.9 | 3e-21 | 29/40 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.520×** | -7.8 | 6e-13 | 29/40 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -7.4 | 1e-11 | 31/43 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.604×** | -6.2 | 3e-08 | 26/42 (LoVo, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -5.8 | 3e-07 | 24/43 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -5.8 | 3e-07 | 25/42 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.616×** | -5.8 | 4e-07 | 25/43 (AsPC-1, SW48, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.664×** | -4.9 | 6e-05 | 21/37 (LoVo, NCI-H1573, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.690×** | -4.6 | 2e-04 | 17/35 (NCI-H1573, LoVo, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.695×** | -4.5 | 3e-04 | 16/43 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -4.4 | 3e-04 | 19/40 (Hs 766T, LoVo, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.716×** | -4.1 | 0.001 | 15/43 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.725×** | -4.0 | 0.002 | 16/43 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.732×** | -3.9 | 0.003 | 17/42 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -3.7 | 0.005 | 16/43 (HOP62, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 35.4 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.8) |
| [[LoVo (line)]] | wt | 42.6 | 0 | 15 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0790× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0595× (z -20.7) |
| [[Hs 766T (line)]] | wt | 147 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -18.7) |
| [[NCI-H1573 (line)]] | alt | 31.4 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0553× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.7) |
| [[HOP62 (line)]] | alt | 29.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.152× (z -11.7) |
| [[A-172 (line)]] | wt | 22.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -14.0) |
| [[HS-578T (line)]] | alt | 28.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -10.2) ⚠ cell-cycle shift, explains ~59% of this change |
| [[PANC-1 (line)]] | alt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -8.7) |
| [[SW48 (line)]] | wt | 38.7 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -9.6) |
| [[SW480 (line)]] | alt | 16.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 24.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -8.5) |
| [[H4 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0662× (z -11.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 33.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0870× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 9.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -10.1) |
| [[RKO (line)]] | wt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -14.2) |
| [[SW 1271 (line)]] | alt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0620× (z -8.7) |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF25]] | +0.78 | +0.80 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.9 kb, same strand: neighbours can correlate without regulation) |
| [[PLEK2]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 | same gene group; STRING 681 |
| [[ARID3B]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PLAUR]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[LYPD3]] | +0.67 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[S100A16]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[KCNN4]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[LTBP4]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PAQR5]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[STX1A]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 | STRING 463 |
| [[PLEKHM1P1]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS3]] | -0.62 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.58 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[MTUS1-DT]] | -0.57 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[MTUS1]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[CASD1]] | -0.54 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[RARRES1]] | -0.53 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PLEKHG5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDYL2]] | B | CDYL2 activity raises PLEKHG5's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 1.84× lower at baseline in the lines without CDYL2 | 0.080 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[ROBO3]] | B | ROBO3 activity raises PLEKHG5's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without ROBO3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1 |
| [[NR3C1]] | B | NR3C1 activity lowers PLEKHG5's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[ZNF608]] | B | ZNF608 activity lowers PLEKHG5's level | lines that do not express ZNF608 (12) vs lines expressing it (38) | 1.62× higher at baseline in the lines without ZNF608 | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNN4]] | B | PLEKHG5 activity raises KCNN4's level | lines that do not express PLEKHG5 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without PLEKHG5 | 0.064 | ⚠ within organs, on part of the lines; also absent: TNFRSF25, SLC22A20P, ENSG00000287264; maybe low, not absent; its own permutation p |
| [[NEURL1]] | B | PLEKHG5 activity lowers NEURL1's level | lines that do not express PLEKHG5 (5) vs lines expressing it (45) | 1.43× higher at baseline in the lines without PLEKHG5 | 0.064 | ⚠ within organs, on part of the lines; also absent: TNFRSF25, SLC22A20P, ENSG00000287264; maybe low, not absent; its own permutation p |
| [[SLC16A7]] | B | PLEKHG5 activity lowers SLC16A7's level | lines that do not express PLEKHG5 (5) vs lines expressing it (45) | 2.58× higher at baseline in the lines without PLEKHG5 | 0.099 | ⚠ within organs, on part of the lines; also absent: TNFRSF25, SLC22A20P, ENSG00000287264; maybe low, not absent |
| [[TNFRSF25]] | C | PLEKHG5's natural level strengthens TNFRSF25's drug response | PLEKHG5's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.58; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.767). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.1, 2.4); signed map (-0.2, 45.4). **Vector** length 106, 27.5% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.7 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.3 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +3.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.8 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.6 | -3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.5 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -4.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RhoGEF domain containing G5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,467,122-6,520,074 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0720, Syx, GEF720, Tech, ARHGEF45 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 13 pathways, smallest: RND1 GTPase cycle; RND3 GTPase cycle; NRAGE signals death through JNK |
| Matched by | ensembl_id |

**Function**, from UniProt [O94827](https://www.uniprot.org/uniprotkb/O94827) (Pleckstrin homology domain-containing family G member 5):

> Functions as a guanine exchange factor (GEF) for RAB26 and thus regulates autophagy of synaptic vesicles in axon terminal of motoneurons (By similarity). Involved in the control of neuronal cell differentiation. Plays a role in angiogenesis through regulation of endothelial cells chemotaxis. Also affects the migration, adhesion, and matrix/bone degradation in macrophages and osteoclasts.

**Summary**, from NCBI Gene [57449](https://www.ncbi.nlm.nih.gov/gene/57449):

> This gene encodes a protein that activates the nuclear factor kappa B (NFKB1) signaling pathway. Mutations in this gene are associated with autosomal recessive distal spinal muscular atrophy. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:29105](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29105) · Entrez [57449](https://www.ncbi.nlm.nih.gov/gene/57449) · UniProt [O94827](https://www.uniprot.org/uniprotkb/O94827) · Ensembl [ENSG00000171680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171680)

## Data

Gene col 10146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10146); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10146]; `tensor/DDL_lfc|DDL_z.npy` [10146]; `embed/gene_vectors.npy` [10146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10146 or target_col == 10146). Every well: [[PLEKHG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
