---
symbol: "DUOX2"
type: "gene"
col: 6383
ensembl_id: "ENSG00000140279"
name: "dual oxidase 2"
location: "15q21.1"
module: 70
arm: "+"
pooled_cpm: 5.58
n_lines_expressing: 18
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 19
direction_downstream: 52
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# DUOX2

*dual oxidase 2* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.26× (z +8.8, q 5e-16, up in 12 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.545× (z -4.6, q 0.002, down in 10 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0165×, NCI-H1792 0.0597×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (CFPAC-1 0.0172×, NCI-H1792 0.0490×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.0536×, CFPAC-1 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.111×, CFPAC-1 0.302×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0138×, NCI-H1792 0.0795×); [[Auranofin (drug)]] 5 µM in 2 lines (AsPC-1 0.0242×, CFPAC-1 0.164×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASP10]] (+0.68, fdr 7e-06), [[CFB]] (+0.65, fdr 1e-05), [[SLC34A2]] (+0.63, fdr 3e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[LINC01285]] → it (grade B ⚠); 52 go from it, the strongest it → [[CARD14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +8.8 | 5e-16 | 12/15 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +7.9 | 1e-12 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +5.7 | 2e-06 | 6/13 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +5.0 | 9e-05 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.45×** | +4.9 | 1e-04 | 6/12 (AsPC-1, CFPAC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.91×** | +4.8 | 2e-04 | 8/14 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.6 | 4e-04 | 2/14 (LoVo, A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +4.3 | 1e-03 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.005 | 7/15 (COLO 205, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.45×** | +3.6 | 0.018 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.026 | 4/14 (A549, COLO 205, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.036 | 1/15 (LoVo) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.036 | 0/13 | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.23×** | +3.2 | 0.050 | 4/13 (AsPC-1, CFPAC-1, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.089 | 5/13 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6383.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0165×, NCI-H1792 0.0597×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (CFPAC-1 0.0172×, NCI-H1792 0.0490×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.0536×, CFPAC-1 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.111×, CFPAC-1 0.302×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0138×, NCI-H1792 0.0795×); [[Auranofin (drug)]] 5 µM in 2 lines (AsPC-1 0.0242×, CFPAC-1 0.164×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.545×** | -4.6 | 0.002 | 10/15 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.635× | -3.4 | 0.13 | 6/15 (NCI-H1792, CFPAC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | 0.727× | -3.4 | 0.13 | 8/15 (HepG2/C3A, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.645× | -3.2 | 0.20 | 5/14 (CFPAC-1, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 45.6 | 0 | 21 (13 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0104× (z -21.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0165× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.164× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0242× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0138× (z -14.1) |
| [[A-172 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.600 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP10]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[CFB]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[SLC34A2]] | +0.63 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ODF3B]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GBP2]] | +0.59 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[PTPRR]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[THEMIS2]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[TNFSF10]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[MUC4]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[VNN1]] | +0.56 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ADAM28]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 5, C 14. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01285]] | B | LINC01285 activity raises DUOX2's level | lines that do not express LINC01285 (21) vs lines expressing it (29) | 2.06× lower at baseline in the lines without LINC01285 | 0.048 | ⚠ within organs, on part of the lines; also absent: HNF1A, SLC22A3, LINC01819; maybe low, not absent |
| [[RBM47]] | B | RBM47 activity raises DUOX2's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without RBM47 | 0.067 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[TOP2A]] | B | TOP2A activity lowers DUOX2's level | compounds that target TOP2A: 3 of 5 raise it (Amsacrine, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BST2]] | B | BST2 activity raises DUOX2's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.85× lower at baseline in the lines without BST2 | 0.073 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[CDKN2A]] | B | CDKN2A activity raises DUOX2's level | lines that do not express CDKN2A (22) vs lines expressing it (28) | 1.66× lower at baseline in the lines without CDKN2A | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE |
| [[VNN1]] | C | VNN1 activity raises DUOX2's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.42× lower at baseline in the lines without VNN1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises DUOX2's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 3.67× lower at baseline in the lines without IGFBP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[APOL1]] | C | APOL1 activity raises DUOX2's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without APOL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises DUOX2's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 3.23× lower at baseline in the lines without ITIH2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[TMPRSS3]] | C | TMPRSS3 activity raises DUOX2's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.28× lower at baseline in the lines without TMPRSS3 | 0.021 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2; co-absent with the target |
| [[SMIM2-AS1]] | C | SMIM2-AS1 activity raises DUOX2's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.05× lower at baseline in the lines without SMIM2-AS1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent; co-absent with the target |
| [[CP]] | C | CP activity raises DUOX2's level | lines that do not express CP (39) vs lines expressing it (11) | 2.72× lower at baseline in the lines without CP | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB; co-absent with the target |

### Downstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 32, C 20. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD14]] | B | DUOX2 activity raises CARD14's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.98× lower at baseline in the lines without DUOX2 | 1e-03 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[FMO5]] | B | DUOX2 activity raises FMO5's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.32× lower at baseline in the lines without DUOX2 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[TMEM140]] | B | DUOX2 activity raises TMEM140's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.25× lower at baseline in the lines without DUOX2 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[RBM47]] | B | DUOX2 activity raises RBM47's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without DUOX2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[RND1]] | B | DUOX2 activity raises RND1's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.18× lower at baseline in the lines without DUOX2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[CASP10]] | B | DUOX2 activity raises CASP10's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without DUOX2 | 0.011 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[NT5C3A]] | B | DUOX2 activity raises NT5C3A's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.58× lower at baseline in the lines without DUOX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[GABRE]] | B | DUOX2 activity raises GABRE's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 3.42× lower at baseline in the lines without DUOX2 | 0.015 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[GBP2]] | B | DUOX2 activity raises GBP2's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.81× lower at baseline in the lines without DUOX2 | 0.017 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[UBE2H]] | B | DUOX2 activity raises UBE2H's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.60× lower at baseline in the lines without DUOX2 | 0.020 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[UBE2H]] | B | DUOX2 activity weakens UBE2H's drug response | lines that do not express DUOX2 (32) vs lines expressing it (17) | the lines without DUOX2 respond 1.27× as strongly (z diff -0.84); strongest at Ouabain (Octahydrate) 5 µM: 1.87x vs 1.32x (z diff -4.0) | 0.033 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB; target measured in part of the lines; both ways; artifact flags |
| [[ETV7]] | B | DUOX2 activity raises ETV7's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.70× lower at baseline in the lines without DUOX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.5, 49.7); signed map (60.8, 27.5). **Vector** length 51.1, 14.5% of its response variance represented; |z| ≥ 3 in 489 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +3.9 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -3.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | dual oxidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:45,092,650-45,114,172 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P138-TOX, P138(TOX), THOX2, LNOX2 |
| Gene groups (HGNC) | EF-hand domain containing; Flavoproteins; NADH oxidase family; Dual oxidase family |
| Reactome | 3 pathways, smallest: Metabolism of amine-derived hormones; Thyroxine biosynthesis; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRD8](https://www.uniprot.org/uniprotkb/Q9NRD8) (Dual oxidase 2):

> Generates hydrogen peroxide which is required for the activity of thyroid peroxidase/TPO and lactoperoxidase/LPO. Plays a role in thyroid hormone synthesis. Also required for lactoperoxidase-mediated antimicrobial defense at the surface of mucosa. Synthesizes NAADP from its reduced NAADPH form which promotes Ca(2+) signaling during T cell activation. May have its own peroxidase activity through its N-terminal peroxidase-like domain.

**Summary**, from NCBI Gene [50506](https://www.ncbi.nlm.nih.gov/gene/50506):

> The protein encoded by this gene is a glycoprotein and a member of the NADPH oxidase family. The synthesis of thyroid hormone is catalyzed by a protein complex located at the apical membrane of thyroid follicular cells. This complex contains an iodide transporter, thyroperoxidase, and a peroxide generating system that includes this encoded protein and DUOX1. This protein is known as dual oxidase because it has both a peroxidase homology domain and a gp91phox domain. [provided by RefSeq, Jul …

**Accessions** — [HGNC:13273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13273) · Entrez [50506](https://www.ncbi.nlm.nih.gov/gene/50506) · UniProt [Q9NRD8](https://www.uniprot.org/uniprotkb/Q9NRD8) · Ensembl [ENSG00000140279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140279)

## Data

Gene col 6383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6383); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6383]; `tensor/DDL_lfc|DDL_z.npy` [6383]; `embed/gene_vectors.npy` [6383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6383 or target_col == 6383). Every well: [[DUOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
