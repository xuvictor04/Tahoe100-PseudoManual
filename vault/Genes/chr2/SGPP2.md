---
symbol: "SGPP2"
type: "gene"
col: 8629
ensembl_id: "ENSG00000163082"
name: "sphingosine-1-phosphate phosphatase 2"
location: "2q36.1"
module: 106
arm: "+"
pooled_cpm: 45.08
n_lines_expressing: 18
n_dd_up: 34
n_dd_down: 12
n_dd_up_clean: 28
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 46
direction_downstream: 89
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# SGPP2

*sphingosine-1-phosphate phosphatase 2* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.21× (z +27.0, q 0e+00, up in 9 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 5 µM: 0.614× (z -4.2, q 0.012, down in 1 of 16 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3TC1]] (+0.67, fdr 1e-05), [[TRIM29]] (+0.66, fdr 1e-05), [[FOXQ1]] (+0.63, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[SPATA6L]] → it (grade B ⚠); 89 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.21×** | +27.0 | 0e+00 | 9/16 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.65×** | +15.3 | 0e+00 | 11/16 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +14.5 | 4e-45 | 13/16 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +11.6 | 5e-29 | 0/16 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +9.6 | 9e-20 | 6/16 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +9.0 | 2e-17 | 11/16 (HT-29, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +8.1 | 3e-14 | 1/15 (A549) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +8.1 | 3e-14 | 11/17 (BT-474, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.67×** | +8.0 | 6e-14 | 7/16 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.61×** | +7.8 | 3e-13 | 7/16 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.58×** | +7.5 | 3e-12 | 6/16 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.56×** | +7.3 | 1e-11 | 6/16 (AsPC-1, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.49×** | +6.5 | 3e-09 | 8/16 (AsPC-1, A549, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +6.4 | 5e-09 | 5/16 (AsPC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +6.4 | 6e-09 | 1/16 (BT-474) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.2 | 2e-08 | 0/16 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.7 | 3e-07 | 6/16 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8629.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 5 µM |  | **0.614×** | -4.2 | 0.012 | 1/16 (SW480) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.779×** | -4.1 | 0.012 | 11/16 (HT-29, COLO 205, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.789×** | -3.9 | 0.020 | 11/16 (LoVo, AsPC-1, …) | two highest doses |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.041 | 0/16 | top dose only |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.062 | 1/16 (BT-474) | rises with dose |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.079 | 0/16 | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 5 µM |  | **0.680×** | -3.3 | 0.079 | 0/16 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.796×** | -3.2 | 0.087 | 0/16 | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.823×** | -3.2 | 0.087 | 0/16 | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.799×** | -3.2 | 0.087 | 1/16 (HCT15) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.801×** | -3.1 | 0.090 | 1/16 (SW480) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.822×** | -3.1 | 0.099 | 4/16 (NCI-H1573, CFPAC-1, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | 0.701× | -3.0 | 0.11 | 11/16 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 345 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -21.2) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -10.6) |
| [[LoVo (line)]] | wt | 201 | 1 | 8 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 6.72× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -20.4) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.348× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 81.9 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 113 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.7) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H1573 (line)]] | alt | 29.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 19.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 143 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.98× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -14.4) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 176 | 1 | 4 (4 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.83× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -13.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 136 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -10.0) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 36.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +17.6) | — |
| [[SW48 (line)]] | wt | 363 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0795× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.202× (z -9.5) |
| [[A549 (line)]] | wt | 13.1 | 3 | 0 | [[Clobetasol propionate (drug)]] 5 µM 6.73× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -12.7) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HCT15 (line)]] | alt | 73.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0799× (z -17.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 20.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.65× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~5% of this change |
| [[KATO III (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -12.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.57 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3TC1]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[TRIM29]] | +0.66 | +0.72 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[FOXQ1]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[GAREM1]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[PLEKHA7]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[GCNT3]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SCNN1A]] | +0.60 | +0.47 / +0.68 | both halves | 2e-05 | **novel candidate** |
| [[PLEKHG6]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[EPS8]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[DNAJC15]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[KRT6A]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[FGD4]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 7, C 39. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATA6L]] | B | SPATA6L activity raises SGPP2's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 4.14× lower at baseline in the lines without SPATA6L | 0.025 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[GRAMD2B]] | B | GRAMD2B activity raises SGPP2's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 3.51× lower at baseline in the lines without GRAMD2B | 0.026 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[EPS8L1]] | B | EPS8L1 activity raises SGPP2's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.68× lower at baseline in the lines without EPS8L1 | 0.026 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[LINC00511]] | B | LINC00511 activity raises SGPP2's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 2.95× lower at baseline in the lines without LINC00511 | 0.037 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[SDCBP2]] | B | SDCBP2 activity raises SGPP2's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 4.07× lower at baseline in the lines without SDCBP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[MT1F]] | B | MT1F activity raises SGPP2's level | lines that do not express MT1F (17) vs lines expressing it (33) | 3.06× lower at baseline in the lines without MT1F | 0.046 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[EFNB2]] | B | EFNB2 activity raises SGPP2's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.67× lower at baseline in the lines without EFNB2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[INAVA]] | C | INAVA activity raises SGPP2's level | lines that do not express INAVA (29) vs lines expressing it (21) | 8.05× lower at baseline in the lines without INAVA | 6e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |
| [[TC2N]] | C | TC2N activity raises SGPP2's level | lines that do not express TC2N (28) vs lines expressing it (22) | 8.69× lower at baseline in the lines without TC2N | 2e-04 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14; co-absent with the target |
| [[FAM83B]] | C | FAM83B activity raises SGPP2's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 8.83× lower at baseline in the lines without FAM83B | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises SGPP2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 9.33× lower at baseline in the lines without SLC44A4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises SGPP2's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 7.90× lower at baseline in the lines without TRIM29 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |

### Downstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 44, C 45. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | SGPP2 activity raises EPS8L1's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 4.59× lower at baseline in the lines without SGPP2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[ITPKC]] | B | SGPP2 activity raises ITPKC's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.47× lower at baseline in the lines without SGPP2 | 1e-03 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[FGD4]] | B | SGPP2 activity raises FGD4's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.90× lower at baseline in the lines without SGPP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[PLEKHA7]] | B | SGPP2 activity raises PLEKHA7's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.30× lower at baseline in the lines without SGPP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[SDCBP2]] | B | SGPP2 activity raises SDCBP2's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 4.82× lower at baseline in the lines without SGPP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[KIF13B]] | B | SGPP2 activity raises KIF13B's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.50× lower at baseline in the lines without SGPP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[ARHGEF16]] | B | SGPP2 activity raises ARHGEF16's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.30× lower at baseline in the lines without SGPP2 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[GRAMD2B]] | B | SGPP2 activity raises GRAMD2B's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.15× lower at baseline in the lines without SGPP2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[AMN]] | B | SGPP2 activity raises AMN's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.19× lower at baseline in the lines without SGPP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[ACOT11]] | B | SGPP2 activity raises ACOT11's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.93× lower at baseline in the lines without SGPP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[GSKIP]] | B | SGPP2 activity raises GSKIP's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 1.67× lower at baseline in the lines without SGPP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[NOSTRIN]] | B | SGPP2 activity raises NOSTRIN's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.22× lower at baseline in the lines without SGPP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.0, 44.3); signed map (52.5, 11.3). **Vector** length 79.4, 25.6% of its response variance represented; |z| ≥ 3 in 620 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +14.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +27.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +6.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.7 | +7.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.5 | +7.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.4 | +7.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -4.1 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | sphingosine-1-phosphate phosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:222,424,543-222,562,621 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPP2, FLJ39004 |
| Gene groups (HGNC) | Sphingosine-1-phosphate phosphatases |
| Reactome | 3 pathways, smallest: Sphingolipid catabolism; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWX5](https://www.uniprot.org/uniprotkb/Q8IWX5) (Sphingosine-1-phosphate phosphatase 2):

> Has specific phosphohydrolase activity towards sphingoid base 1-phosphates. Has high phosphohydrolase activity against dihydrosphingosine-1-phosphate and sphingosine-1-phosphate (S1P) in vitro. Sphingosine-1-phosphate phosphatase activity is needed for efficient recycling of sphingosine into the sphingolipid synthesis pathway (By similarity). May play a role in attenuating intracellular sphingosine 1-phosphate (S1P) signaling. May play a role in pro-inflammatory signaling. Plays a role in the …

**Summary**, from NCBI Gene [130367](https://www.ncbi.nlm.nih.gov/gene/130367):

> The protein encoded by this gene is a transmembrane protein that degrades the bioactive signaling molecule sphingosine 1-phosphate. The encoded protein is induced during inflammatory responses and has been shown to be downregulated by the microRNA-31 tumor suppressor. Alternative splice variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:19953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19953) · Entrez [130367](https://www.ncbi.nlm.nih.gov/gene/130367) · UniProt [Q8IWX5](https://www.uniprot.org/uniprotkb/Q8IWX5) · Ensembl [ENSG00000163082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163082)

## Data

Gene col 8629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8629); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8629]; `tensor/DDL_lfc|DDL_z.npy` [8629]; `embed/gene_vectors.npy` [8629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8629 or target_col == 8629). Every well: [[SGPP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGPP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
