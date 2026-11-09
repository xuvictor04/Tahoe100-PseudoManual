---
symbol: "FCGBP"
type: "gene"
col: 15849
ensembl_id: "ENSG00000275395"
name: "Fc gamma binding protein"
location: "19q13.2"
module: 8
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 30
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FCGBP

*Fc gamma binding protein* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.76× (z +10.6, q 3e-23, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +9.6, q 2e-19, up in 9 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.601× (z -4.3, q 0.012, down in 9 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.256×, AsPC-1 0.122×, NCI-H2347 0.250×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0622×, AsPC-1 0.0638×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.0647×, KATO III 0.203×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.254×, KATO III 0.398×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNP]] (+0.59, fdr 1e-05), [[FAM83E]] (+0.57, fdr 2e-05), [[MUC20]] (+0.56, fdr 1e-05); moves opposite to [[STEAP3]] (-0.55, fdr 4e-05), [[LANCL1]] (-0.50, fdr 4e-05), [[CROCCP3-1]] (-0.45, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[CAPN12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +10.6 | 3e-23 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +9.6 | 2e-19 | 9/20 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +9.2 | 6e-18 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +8.4 | 6e-15 | 3/11 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +6.8 | 1e-09 | 6/21 (C32, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +5.6 | 2e-06 | 10/26 (SHP-77, HS-578T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.0 | 6e-05 | 3/26 (A549, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +4.8 | 1e-04 | 5/18 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.003 | 6/24 (NCI-H23, SHP-77, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.004 | 7/19 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +3.9 | 0.005 | 6/20 (CFPAC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.56×** | +3.7 | 0.012 | 2/25 (HEC-1-A, PANC-1) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.5 | 0.018 | 4/19 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.059 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +3.1 | 0.075 | 1/22 (BT-474) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.089 | 4/26 (HT-29, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15849.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.256×, AsPC-1 0.122×, NCI-H2347 0.250×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0622×, AsPC-1 0.0638×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.0647×, KATO III 0.203×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.254×, KATO III 0.398×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.601×** | -4.3 | 0.012 | 9/24 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.646×** | -3.7 | 0.073 | 13/27 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 55.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -14.8) |
| [[PANC-1 (line)]] | alt | 21.5 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0622× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0647× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.9) |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0518× (z -8.5) |
| [[A-172 (line)]] | wt | 0.938 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNP]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[FAM83E]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[MUC20]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[TMC4]] | +0.55 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[PTPRR]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PDE4C]] | +0.54 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[ADGRF1]] | +0.53 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[SPATC1]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[FUT3]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SMBD1P]] | +0.52 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[ARHGAP30]] | +0.52 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[LGALS4]] | +0.52 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STEAP3]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[LANCL1]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CROCCP3-1]] | -0.45 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[PPP5C]] | -0.44 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[ENOPH1]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[BTBD1]] | -0.44 | -0.23 / -0.54 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FCGBP's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[BARX2]] | B | BARX2 activity raises FCGBP's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 1.80× lower at baseline in the lines without BARX2 | 0.066 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[LGALS4]] | B | LGALS4 activity raises FCGBP's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 2.41× lower at baseline in the lines without LGALS4 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[CLDN4]] | B | CLDN4 activity raises FCGBP's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without CLDN4 | 0.081 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[SLC44A4]] | C | SLC44A4 activity raises FCGBP's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 1.96× lower at baseline in the lines without SLC44A4 | 0.074 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAPN12]] | B | FCGBP activity raises CAPN12's level | lines that do not express FCGBP (20) vs lines expressing it (30) | 1.36× lower at baseline in the lines without FCGBP | 0.054 | ⚠ within organs, on part of the lines; also absent: LCN2, NPNT, RNF183; maybe low, not absent |
| [[AOAH]] | B | FCGBP activity raises AOAH's level | lines that do not express FCGBP (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without FCGBP | 0.060 | ⚠ within organs, on part of the lines; also absent: LCN2, NPNT, RNF183; maybe low, not absent |
| [[GAL3ST1]] | B | FCGBP activity raises GAL3ST1's level | lines that do not express FCGBP (20) vs lines expressing it (30) | 1.38× lower at baseline in the lines without FCGBP | 0.082 | ⚠ within organs, on part of the lines; also absent: LCN2, NPNT, RNF183; maybe low, not absent |
| [[HNF1A-AS1]] | C | FCGBP activity raises HNF1A-AS1's level | lines that do not express FCGBP (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without FCGBP | 0.060 | ⚠ within organs, on part of the lines; also absent: LCN2, NPNT, RNF183; maybe low, not absent; co-absent with the target |
| [[SLC44A4]] | C | FCGBP activity raises SLC44A4's level | lines that do not express FCGBP (20) vs lines expressing it (30) | 2.53× lower at baseline in the lines without FCGBP | 0.062 | ⚠ within organs, on part of the lines; also absent: LCN2, NPNT, RNF183; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.9, 56.1); signed map (57.2, 5.7). **Vector** length 37.1, 5.63% of its response variance represented; |z| ≥ 3 in 650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.5 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +5.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.8 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.1 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | Fc gamma binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,863,323-39,934,626 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FC(GAMMA)BP, FcgammaBP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6R7](https://www.uniprot.org/uniprotkb/Q9Y6R7) (IgGFc-binding protein):

> May be involved in the maintenance of the mucosal structure as a gel-like component of the mucosa.

**Summary**, from NCBI Gene [8857](https://www.ncbi.nlm.nih.gov/gene/8857):

> Predicted to be an extracellular matrix structural constituent. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13572) · Entrez [8857](https://www.ncbi.nlm.nih.gov/gene/8857) · UniProt [Q9Y6R7](https://www.uniprot.org/uniprotkb/Q9Y6R7) · Ensembl [ENSG00000275395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275395)

## Data

Gene col 15849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15849); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15849]; `tensor/DDL_lfc|DDL_z.npy` [15849]; `embed/gene_vectors.npy` [15849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15849 or target_col == 15849). Every well: [[FCGBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FCGBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
