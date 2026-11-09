---
symbol: "C5orf63"
type: "gene"
col: 8909
ensembl_id: "ENSG00000164241"
name: "chromosome 5 open reading frame 63"
location: "5q23.2"
module: 1
arm: "+"
pooled_cpm: 4.77
n_lines_expressing: 39
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# C5orf63

*chromosome 5 open reading frame 63* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.65× (z +5.1, q 2e-04, up in 12 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.477× (z -10.7, q 4e-24, down in 25 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[N6AMT1]] (+0.70, fdr 7e-06), [[RBM45]] (+0.62, fdr 7e-06), [[PDCD2]] (+0.60, fdr 1e-05); moves opposite to [[IFT140]] (-0.56, fdr 5e-05), [[STX5]] (-0.55, fdr 1e-05), [[TSEN34]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[PRPSAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +5.1 | 2e-04 | 12/33 (PANC-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.8 | 4e-04 | 6/15 (LS 180, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.0 | 0.011 | 7/20 (AsPC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +3.9 | 0.011 | 4/9 (HT-29, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.022 | 11/34 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.043 | 9/34 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.048 | 8/36 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.051 | 4/35 (CFPAC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.26×** | +3.3 | 0.052 | 9/36 (KATO III, HT-29, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.060 | 10/36 (SW480, CFPAC-1, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.070 | 5/34 (SW480, HT-29, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8909.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.477×** | -10.7 | 4e-24 | 25/31 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.403×** | -9.3 | 3e-18 | 24/35 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.430×** | -8.7 | 9e-16 | 23/30 (SW480, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.536×** | -6.4 | 2e-08 | 17/34 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.561×** | -5.9 | 4e-07 | 19/34 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.687×** | -5.4 | 5e-06 | 16/32 (PANC-1, A549, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.592×** | -5.4 | 6e-06 | 17/36 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.391×** | -5.0 | 3e-05 | 17/33 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -4.9 | 6e-05 | 12/31 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -4.8 | 1e-04 | 12/31 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.625×** | -4.6 | 3e-04 | 17/33 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -4.5 | 4e-04 | 14/30 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.697×** | -3.7 | 0.009 | 14/34 (PANC-1, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.713×** | -3.3 | 0.034 | 12/35 (PANC-1, A549, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.731×** | -3.2 | 0.048 | 7/35 (PANC-1, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -14.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -13.8) |
| [[SW480 (line)]] | alt | 7.43 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0274× (z -11.5) |
| [[LS 180 (line)]] | wt | 8.63 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0795× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 6.56 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.6) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A549 (line)]] | wt | 7.00 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -9.9) ⚠ cell-cycle shift, explains ~86% of this change |
| [[CFPAC-1 (line)]] | alt | 4.18 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0639× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -9.0) |
| [[J82 (line)]] | alt | 4.32 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0422× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 7.48 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.101× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 8.34 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -8.6) |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0679× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N6AMT1]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[RBM45]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PDCD2]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TMEM209]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ZDHHC21]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[SPIN3]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[RRP15]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ZNF485]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TMEM177]] | +0.57 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TSEN15]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ABHD13]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[TMBIM4]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT140]] | -0.56 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[STX5]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TSEN34]] | -0.55 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[TPI1]] | -0.52 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[INTS6L]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[NARF]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[FANK1]] | -0.50 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[KDM2A]] | -0.50 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[RNF122]] | -0.50 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[NLGN2]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[GTF2B]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[FNBP1]] | -0.49 | -0.42 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises C5orf63's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRPSAP1]] | B | C5orf63 activity lowers PRPSAP1's level | lines that do not express C5orf63 (11) vs lines expressing it (39) | 1.57× higher at baseline in the lines without C5orf63 | 0.018 | ⚠ within organs, on part of the lines; also absent: TSPAN15, TNFRSF10A, ABCC3 |
| [[STX5-DT]] | B | C5orf63 activity raises STX5-DT's level | lines that do not express C5orf63 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without C5orf63 | 0.087 | ⚠ within organs, on part of the lines; also absent: TSPAN15, TNFRSF10A, ABCC3 |
| cells under [[Tolcapone (drug)]] 5 µM | B | C5orf63 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express C5orf63 (11) vs lines expressing it (37) | the lines without C5orf63: 0.91× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TSPAN15, TNFRSF10A, ABCC3 |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.7, 0.9); signed map (-2.5, -38.5). **Vector** length 53.2, 8.63% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | +3.3 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -10.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.6 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 5 open reading frame 63 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:127,045,235-127,073,506 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YDR286C, FLJ44606 |
| Matched by | ensembl_id |

UniProt [A6NC05](https://www.uniprot.org/uniprotkb/A6NC05) carries no function annotation.

**Summary**, from NCBI Gene [401207](https://www.ncbi.nlm.nih.gov/gene/401207):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:40051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40051) · Entrez [401207](https://www.ncbi.nlm.nih.gov/gene/401207) · UniProt [A6NC05](https://www.uniprot.org/uniprotkb/A6NC05) · Ensembl [ENSG00000164241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164241)

## Data

Gene col 8909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8909); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8909]; `tensor/DDL_lfc|DDL_z.npy` [8909]; `embed/gene_vectors.npy` [8909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8909 or target_col == 8909). Every well: [[C5orf63 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C5orf63.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
