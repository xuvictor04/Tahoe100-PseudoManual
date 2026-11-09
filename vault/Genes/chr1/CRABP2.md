---
symbol: "CRABP2"
type: "gene"
col: 6712
ensembl_id: "ENSG00000143320"
name: "cellular retinoic acid binding protein 2"
location: "1q23.1"
module: 103
arm: "+"
pooled_cpm: 29.89
n_lines_expressing: 26
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# CRABP2

*cellular retinoic acid binding protein 2* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.95× (z +15.0, q 0e+00, up in 22 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.666× (z -4.0, q 0.041, down in 10 of 23 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSRP2]] (+0.60, fdr 6e-05), [[SNAI1]] (+0.59, fdr 5e-05), [[TNFRSF11A]] (+0.56, fdr 1e-05); moves opposite to [[SLC25A13]] (-0.55, fdr 1e-05), [[ZC3H14]] (-0.50, fdr 4e-05), [[HECTD1]] (-0.49, fdr 7e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[SNAI1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.95×** | +15.0 | 0e+00 | 22/24 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.82×** | +13.1 | 8e-37 | 12/20 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +11.1 | 2e-26 | 12/17 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +7.3 | 3e-11 | 9/20 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.6 | 3e-06 | 15/24 (A498, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +5.1 | 3e-05 | 14/23 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.9 | 7e-05 | 13/24 (RKO, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.8 | 1e-04 | 7/23 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +4.4 | 7e-04 | 8/23 (SW480, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.42×** | +3.3 | 0.052 | 6/24 (A498, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | 1.36× | +3.0 | 0.13 | 3/22 (AsPC-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.666×** | -4.0 | 0.041 | 10/23 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.684×** | -3.7 | 0.058 | 16/23 (RPMI-7951, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.491×** | -3.6 | 0.059 | 11/24 (HT-29, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.775×** | -3.5 | 0.063 | 10/24 (BT-474, HCT15, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.711×** | -3.3 | 0.087 | 11/23 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.712×** | -3.3 | 0.087 | 9/23 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.532×** | -3.2 | 0.099 | 16/24 (HOP62, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.707×** | -3.2 | 0.099 | 14/23 (C32, HOP62, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.553× | -3.0 | 0.16 | 10/24 (CHP-212, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 20.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +15.4) | — |
| [[SW480 (line)]] | alt | 28.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 33.6 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 105 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +10.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.274× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 49.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 7.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +9.2) | — |
| [[C32 (line)]] | wt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 9.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +9.2) | — |
| [[A-172 (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP2]] | +0.60 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[SNAI1]] | +0.59 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[TNFRSF11A]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SAMD14]] | +0.55 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[LOXL2]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ADORA1]] | +0.52 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[SPAG4]] | +0.52 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[AMZ1]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LRP1]] | +0.52 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[TMEM145]] | +0.51 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[IDH2]] | +0.51 | +0.49 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_PEROXISOME |
| [[ICAM5]] | +0.51 | +0.34 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A13]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H14]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[HECTD1]] | -0.49 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[MRRF]] | -0.48 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[TXNRD3]] | -0.47 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[JPX]] | -0.47 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[MRPL15]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[YLPM1]] | -0.47 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[ZNF839]] | -0.47 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[NOL8]] | -0.46 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[DNAJC16]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[TSEN2]] | -0.46 | -0.33 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CRABP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PDGFB]] | B | PDGFB activity raises CRABP2's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.71× lower at baseline in the lines without PDGFB | 0.039 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[TOP2B]] | B | TOP2B activity lowers CRABP2's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PLTP]] | C | PLTP activity raises CRABP2's level | lines that do not express PLTP (27) vs lines expressing it (23) | 2.68× lower at baseline in the lines without PLTP | 0.089 | ⚠ within organs, on part of the lines; also absent: SEC14L4, HAS2, PPP1R14A; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNAI1]] | B | CRABP2 activity raises SNAI1's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 1.94× lower at baseline in the lines without CRABP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |
| [[KDM5B]] | B | CRABP2 activity raises KDM5B's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 1.24× lower at baseline in the lines without CRABP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |
| [[NIM1K]] | B | CRABP2 activity raises NIM1K's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without CRABP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |
| [[NOL8]] | B | CRABP2 activity weakens NOL8's drug response | lines that do not express CRABP2 (24) vs lines expressing it (24) | the lines without CRABP2 respond 1.17× as strongly (z diff -0.82); strongest at Homoharringtonine 0.05 µM: 1.76x vs 1.40x (z diff -1.9) | 0.071 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2; target measured in part of the lines; artifact flags |
| [[LSR]] | B | CRABP2 activity raises LSR's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 2.46× lower at baseline in the lines without CRABP2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |
| [[DHDH]] | B | CRABP2 activity raises DHDH's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 1.28× lower at baseline in the lines without CRABP2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.5, -26.5); signed map (1.4, 19.3). **Vector** length 61.6, 16.3% of its response variance represented; |z| ≥ 3 in 558 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +15.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | cellular retinoic acid binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,699,606-156,705,816 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRABP-II |
| Gene groups (HGNC) | Fatty acid binding protein family |
| Hallmark sets | PEROXISOME |
| Reactome | 2 pathways, smallest: Signaling by Retinoic Acid; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P29373](https://www.uniprot.org/uniprotkb/P29373) (Cellular retinoic acid-binding protein 2):

> Transports retinoic acid to the nucleus. Regulates the access of retinoic acid to the nuclear retinoic acid receptors.

**Summary**, from NCBI Gene [1382](https://www.ncbi.nlm.nih.gov/gene/1382):

> This gene encodes a member of the retinoic acid (RA, a form of vitamin A) binding protein family and lipocalin/cytosolic fatty-acid binding protein family. The protein is a cytosol-to-nuclear shuttling protein, which facilitates RA binding to its cognate receptor complex and transfer to the nucleus. It is involved in the retinoid signaling pathway, and is associated with increased circulating low-density lipoprotein cholesterol. Alternatively spliced transcript variants encoding the same …

**Accessions** — [HGNC:2339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2339) · Entrez [1382](https://www.ncbi.nlm.nih.gov/gene/1382) · UniProt [P29373](https://www.uniprot.org/uniprotkb/P29373) · Ensembl [ENSG00000143320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143320)

## Data

Gene col 6712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6712); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6712]; `tensor/DDL_lfc|DDL_z.npy` [6712]; `embed/gene_vectors.npy` [6712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6712 or target_col == 6712). Every well: [[CRABP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRABP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
