---
symbol: "ZNF567-DT"
type: "gene"
col: 13502
ensembl_id: "ENSG00000225975"
name: "ZNF567 divergent transcript"
location: "19q13.12"
module: 30
arm: "+"
pooled_cpm: 2.74
n_lines_expressing: 44
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 18
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ZNF567-DT

*ZNF567 divergent transcript* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.74× (z +9.4, q 3e-18, up in 34 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.646× (z -5.7, q 4e-06, down in 14 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.0889×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0543×; ⚠ cell-cycle shift, explains ~26% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0942×); [[Malotilate (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0731×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF461]] (+0.63, fdr 1e-05, ⚠ same locus), [[OSBPL7]] (+0.59, fdr 3e-05), [[ZNF527]] (+0.58, fdr 1e-05), [[GDPD3]] (+0.57, fdr 4e-05); moves opposite to [[E2F3]] (-0.51, fdr 3e-04), [[DGKH]] (-0.50, fdr 3e-04), [[CLOCK]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZIM2-AS1]] → it (grade B ⚠); 18 go from it, the strongest it → [[ZNF875]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.74×** | +9.4 | 3e-18 | 34/40 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +8.5 | 5e-15 | 26/39 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +7.3 | 4e-11 | 13/31 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +7.2 | 8e-11 | 20/39 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +7.0 | 3e-10 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.58×** | +6.1 | 1e-07 | 5/39 (J82, A549, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.2 | 2e-05 | 13/39 (PANC-1, A498, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.80×** | +5.2 | 2e-05 | 17/36 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +4.7 | 1e-04 | 11/38 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +4.6 | 2e-04 | 10/33 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +4.5 | 4e-04 | 11/40 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 9e-04 | 10/37 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +3.6 | 0.012 | 1/5 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +3.6 | 0.014 | 3/15 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.018 | 4/39 (PANC-1, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.054 | 3/39 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.054 | 7/37 (HEC-1-A, SNU-423, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13502.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.0889×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.0543×; ⚠ cell-cycle shift, explains ~26% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0942×); [[Malotilate (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0731×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -5.7 | 4e-06 | 14/30 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.544×** | -5.7 | 4e-06 | 15/40 (H4, Hs 766T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.600×** | -4.8 | 4e-04 | 16/39 (NCI-H1792, SNU-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.677×** | -3.6 | 0.040 | 12/39 (A-172, A549, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.2 | 0.16 | 8/42 (SW1417, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 2.18 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0889× (z -12.0) |
| [[A-172 (line)]] | wt | 4.01 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0543× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.91 | 0 | 1 | — | [[Brivudine (drug)]] 0.05 µM 0.0718× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 3.26 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0942× (z -10.1) |
| [[SW480 (line)]] | alt | 4.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +11.0) | — |
| [[A-427 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.293 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF461]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 | ⚠ same locus (15.8 kb, same strand: neighbours can correlate without regulation) |
| [[OSBPL7]] | +0.59 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[ZNF527]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[GDPD3]] | +0.57 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[KCTD21]] | +0.57 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[USP35]] | +0.57 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[ZNF875]] | +0.56 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[LINC00888]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ZNF540]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[IQSEC2]] | +0.55 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[DYNC2LI1]] | +0.54 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[DUSP12]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[CYB5R1]] | +0.54 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F3]] | -0.51 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[DGKH]] | -0.50 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[CLOCK]] | -0.49 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[HIVEP1]] | -0.49 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[IGF2BP3]] | -0.48 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[ARID1A]] | -0.47 | -0.24 / -0.48 | both halves | 4e-04 |  |
| [[CENPP]] | -0.47 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[SNRPB]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[IRF2]] | -0.47 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[BAZ1A]] | -0.47 | -0.17 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[GLI3]] | -0.46 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[GEN1]] | -0.46 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[ATP11C]] | -0.46 | -0.29 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZIM2-AS1]] | B | ZIM2-AS1 activity raises ZNF567-DT's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without ZIM2-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ZNF71]] | B | ZNF71 activity raises ZNF567-DT's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without ZNF71 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZNF177]] | B | ZNF177 activity raises ZNF567-DT's level | lines that do not express ZNF177 (8) vs lines expressing it (42) | 1.95× lower at baseline in the lines without ZNF177 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF559-ZNF177, ZNF559, HYDIN |
| [[ZNF471]] | B | ZNF471 activity raises ZNF567-DT's level | lines that do not express ZNF471 (28) vs lines expressing it (22) | 1.40× lower at baseline in the lines without ZNF471 | 0.080 | ⚠ within organs, on part of the lines; also absent: TRIML2, ZNF667, ZNF667-AS1 |
| [[ZNF420]] | C | ZNF420 activity raises ZNF567-DT's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 2.58× lower at baseline in the lines without ZNF420 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540; co-absent with the target |
| [[ZNF527]] | C | ZNF527 activity raises ZNF567-DT's level | lines that do not express ZNF527 (3) vs lines expressing it (47) | 3.03× lower at baseline in the lines without ZNF527 | 0.004 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221; co-absent with the target |
| [[ZNF540]] | C | ZNF540 activity raises ZNF567-DT's level | lines that do not express ZNF540 (5) vs lines expressing it (45) | 2.96× lower at baseline in the lines without ZNF540 | 0.010 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZFP14, ZNF573; maybe low, not absent; co-absent with the target |
| [[ZNF461]] | C | ZNF461 activity raises ZNF567-DT's level | lines that do not express ZNF461 (7) vs lines expressing it (43) | 2.50× lower at baseline in the lines without ZNF461 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF567, ZNF529-AS1, ZNF571; co-absent with the target |
| [[ZFP14]] | C | ZFP14 activity raises ZNF567-DT's level | lines that do not express ZFP14 (4) vs lines expressing it (46) | 2.98× lower at baseline in the lines without ZFP14 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ZNF540, ZNF566, ZNF567; co-absent with the target; its own permutation p |
| [[CENPP]] | C | CENPP activity raises ZNF567-DT's level | lines that do not express CENPP (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without CENPP | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 13, C 5. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF875]] | B | ZNF567-DT activity raises ZNF875's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 3.27× lower at baseline in the lines without ZNF567-DT | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[ZNF383]] | B | ZNF567-DT, [[ZNF571]] activity raises ZNF383's level | lines that do not express ZNF567-DT, ZNF571 (6) vs lines expressing them (44) | 2.84× lower at baseline in the lines without ZNF567-DT, ZNF571 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF420, ZNF850, ZNF540; co-absent genes |
| [[ZNF112]] | B | ZNF567-DT, [[ZNF571]] activity raises ZNF112's level | lines that do not express ZNF567-DT, ZNF571 (6) vs lines expressing them (44) | 2.27× lower at baseline in the lines without ZNF567-DT, ZNF571 | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF420, ZNF850, ZNF540; co-absent genes |
| [[ZNF283]] | B | ZNF567-DT activity raises ZNF283's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without ZNF567-DT | 0.042 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[NPHP1]] | B | ZNF567-DT activity raises NPHP1's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without ZNF567-DT | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[ZNF71]] | B | ZNF567-DT activity raises ZNF71's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 4.27× lower at baseline in the lines without ZNF567-DT | 0.065 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[ZNF177]] | B | ZNF567-DT, [[ZNF571]] activity raises ZNF177's level | lines that do not express ZNF567-DT, ZNF571 (6) vs lines expressing them (44) | 2.39× lower at baseline in the lines without ZNF567-DT, ZNF571 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF420, ZNF850, ZNF540; co-absent genes |
| [[LINC00888]] | B | ZNF567-DT, [[ZNF571]] activity raises LINC00888's level | lines that do not express ZNF567-DT, ZNF571 (6) vs lines expressing them (44) | 2.04× lower at baseline in the lines without ZNF567-DT, ZNF571 | 0.070 | ⚠ within organs, on part of the lines; also absent: ZNF420, ZNF850, ZNF540; co-absent genes |
| [[RNF20]] | B | ZNF567-DT, [[ZNF571]] activity raises RNF20's level | lines that do not express ZNF567-DT, ZNF571 (6) vs lines expressing them (44) | 1.35× lower at baseline in the lines without ZNF567-DT, ZNF571 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF420, ZNF850, ZNF540; co-absent genes |
| [[ZNF559-ZNF177]] | B | ZNF567-DT activity raises ZNF559-ZNF177's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 2.40× lower at baseline in the lines without ZNF567-DT | 0.084 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[LINC00888-1]] | B | ZNF567-DT, [[ZNF571]] activity raises LINC00888-1's level | lines that do not express ZNF567-DT, ZNF571 (6) vs lines expressing them (44) | 2.71× lower at baseline in the lines without ZNF567-DT, ZNF571 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF420, ZNF850, ZNF540; co-absent genes |
| [[ZIM2-AS1]] | B | ZNF567-DT activity raises ZIM2-AS1's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 3.07× lower at baseline in the lines without ZNF567-DT | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (4.5, -5.9); signed map (-31.3, -1.3). **Vector** length 43.6, 5.16% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.1 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +2.0 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.1 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.6 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ZNF567 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.12 — chr19:36,682,636-36,687,468 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC01534 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51281) · Entrez [101927621](https://www.ncbi.nlm.nih.gov/gene/101927621) · Ensembl [ENSG00000225975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225975)

## Data

Gene col 13502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13502); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13502]; `tensor/DDL_lfc|DDL_z.npy` [13502]; `embed/gene_vectors.npy` [13502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13502 or target_col == 13502). Every well: [[ZNF567-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF567-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
