---
symbol: "KDM4A-AS1"
type: "gene"
col: 14065
ensembl_id: "ENSG00000236200"
name: "KDM4A antisense RNA 1"
location: "1p34.2-p34.1"
module: 105
arm: "+"
pooled_cpm: 4.29
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# KDM4A-AS1

*KDM4A antisense RNA 1* — 1p34.2-p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.97× (z +18.1, q 0e+00, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.149×, SK-MEL-2 0.222×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0492×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.106×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.167×); [[Flutamide (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0583×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (KATO III 0.0799×).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POM121]] (+0.56, fdr 3e-04), [[MAP2K1]] (+0.56, fdr 5e-04), [[FAM86DP]] (+0.55, fdr 3e-05); moves opposite to [[SMARCE1]] (-0.54, fdr 1e-04), [[ABCC2]] (-0.50, fdr 8e-04, ⚠ not reproduced), [[SYNE1]] (-0.50, fdr 5e-04), [[COPS5]] (-0.50, fdr 9e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.97×** | +18.1 | 0e+00 | 44/47 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +17.5 | 0e+00 | 35/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.78×** | +17.4 | 0e+00 | 43/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.46×** | +16.3 | 0e+00 | 42/47 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +11.9 | 1e-30 | 24/36 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +10.1 | 7e-22 | 25/39 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +9.5 | 2e-19 | 15/22 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +9.2 | 3e-18 | 28/47 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.82×** | +7.9 | 2e-13 | 7/17 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.86×** | +7.8 | 3e-13 | 1/8 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +6.9 | 2e-10 | 18/39 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.6 | 3e-09 | 13/46 (HOP62, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +5.2 | 1e-05 | 8/46 (J82, SHP-77, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +5.2 | 1e-05 | 11/42 (HOP62, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.0 | 2e-05 | 8/45 (A498, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.3 | 4e-04 | 13/43 (SW480, HOP62, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.010 | 5/34 (HEC-1-A, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14065.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.149×, SK-MEL-2 0.222×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0492×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.106×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.167×); [[Flutamide (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0583×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (KATO III 0.0799×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -5.3 | 8e-05 | 16/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.627× | -3.2 | 0.31 | 3/44 (SW480, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.843× | -3.1 | 0.31 | 8/46 (SHP-77, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.04 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 6.75 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +10.5) | [[Cobimetinib (drug)]] 0.05 µM 0.167× (z -10.0) |
| [[A498 (line)]] | wt | 5.46 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 6.35 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.42× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 8.48 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0492× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 3.65 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 7.64 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 3.70 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0799× (z -8.9) |
| [[RKO (line)]] | wt | 4.98 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0814× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 5.70 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0583× (z -9.3) |
| [[A-172 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POM121]] | +0.56 | +0.28 / +0.47 | both halves | 3e-04 |  |
| [[MAP2K1]] | +0.56 | +0.24 / +0.52 | both halves | 5e-04 |  |
| [[FAM86DP]] | +0.55 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[LINC03009-1]] | +0.54 | +0.33 / +0.40 | both halves | 1e-04 |  |
| [[FAM89A]] | +0.54 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[C9orf40]] | +0.54 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[BRI3BP]] | +0.52 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[CKLF]] | +0.51 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[RASA2]] | +0.51 | +0.19 / +0.45 | ⚠ not reproduced | 8e-04 |  |
| [[RFWD3]] | +0.50 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PIGF]] | +0.50 | +0.25 / +0.49 | both halves | 4e-04 |  |
| [[ZNF215]] | +0.50 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[CSNK1E]] | +0.49 | +0.22 / +0.47 | both halves | 6e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCE1]] | -0.54 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[ABCC2]] | -0.50 | -0.19 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[SYNE1]] | -0.50 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[COPS5]] | -0.50 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[GNGT1]] | -0.49 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[TRIML2]] | -0.49 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[GDAP1]] | -0.49 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[ACIN1]] | -0.49 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[ANXA7]] | -0.49 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[SPDYA]] | -0.49 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[LGALS3]] | -0.48 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[ZMYM4]] | -0.48 | -0.24 / -0.44 | both halves | 4e-04 |  |
| [[CLUAP1]] | -0.48 | -0.28 / -0.42 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KDM4A-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IL1RAP]] | B | IL1RAP activity lowers KDM4A-AS1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.44× higher at baseline in the lines without IL1RAP | 0.040 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[C1QL1]] | B | C1QL1 activity raises KDM4A-AS1's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.34× lower at baseline in the lines without C1QL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[TRPC6]] | B | TRPC6 activity lowers KDM4A-AS1's level | lines that do not express TRPC6 (14) vs lines expressing it (36) | 1.31× higher at baseline in the lines without TRPC6 | 0.060 | ⚠ within organs, on part of the lines; also absent: UNC80, ARHGAP30, ENSG00000236283; maybe low, not absent |
| [[TRIML2]] | B | TRIML2 activity raises KDM4A-AS1's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without TRIML2 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032 |
| [[CTXN1]] | B | CTXN1 activity raises KDM4A-AS1's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without CTXN1 | 0.098 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[CFL2]] | C | CFL2 activity raises KDM4A-AS1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.67× lower at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.9, 3.8); signed map (-42.7, 22.8). **Vector** length 44.4, 4.74% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +17.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +11.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +10.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.6 | +16.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.5 | +18.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +4.3 |
|  | [[vincristine (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | -0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | +2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | KDM4A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p34.2-p34.1 — chr1:43,685,123-43,708,138 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40528) · Entrez [100132774](https://www.ncbi.nlm.nih.gov/gene/100132774) · Ensembl [ENSG00000236200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236200)

## Data

Gene col 14065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14065); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14065]; `tensor/DDL_lfc|DDL_z.npy` [14065]; `embed/gene_vectors.npy` [14065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14065 or target_col == 14065). Every well: [[KDM4A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM4A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
