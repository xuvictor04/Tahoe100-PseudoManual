---
symbol: "NHSL2"
type: "gene"
col: 12817
ensembl_id: "ENSG00000204131"
name: "NHS like 2"
location: "Xq13.1"
module: 61
arm: "+"
pooled_cpm: 5.59
n_lines_expressing: 26
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# NHSL2

*NHS like 2* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.04× (z +18.6, q 0e+00, up in 15 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 0.320×; ⚠ position not correctable); [[Binimetinib (drug)]] 0.5 µM in 1 line (HOP62 0.161×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HOP62 0.109×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (HOP62 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COLEC12]] (+0.66, fdr 7e-06), [[KCNN3]] (+0.65, fdr 7e-06), [[IL1RAPL1]] (+0.59, fdr 1e-05); moves opposite to [[ZDHHC7]] (-0.45, fdr 5e-05), [[ZNF449]] (-0.45, fdr 3e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[ZFPM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.04×** | +18.6 | 0e+00 | 15/17 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +14.4 | 1e-44 | 7/17 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +13.7 | 2e-40 | 5/11 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +12.5 | 2e-33 | 14/21 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.60×** | +11.3 | 2e-27 | 14/16 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +10.8 | 4e-25 | 2/8 (PANC-1, HS-578T) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.52×** | +10.2 | 3e-22 | 2/7 (SNU-423, HS-578T) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +9.4 | 3e-19 | 9/15 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +8.1 | 5e-14 | 13/19 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +6.6 | 2e-09 | 5/17 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.7 | 6e-07 | 8/18 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.60×** | +5.5 | 2e-06 | 9/22 (HOP62, BT-474, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.59×** | +5.5 | 2e-06 | 11/22 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.63×** | +5.3 | 4e-06 | 4/16 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.60×** | +5.2 | 9e-06 | 3/14 (SW 900, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +5.1 | 1e-05 | 8/21 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.3 | 6e-04 | 2/17 (NCI-H460, HOP62) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 1e-03 | 11/19 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.003 | 3/22 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.039 | 6/20 (BT-474, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.039 | 1/22 (PANC-1) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +2.8 | 0.087 | 1/19 (BT-474) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12817.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 0.320×; ⚠ position not correctable); [[Binimetinib (drug)]] 0.5 µM in 1 line (HOP62 0.161×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HOP62 0.109×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (HOP62 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | 0.741× | -3.6 | 0.19 | 6/22 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.765× | -3.2 | 0.37 | 0/20 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 35.1 | 5 (2 ⚠) | 21 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +15.9) | [[Adagrasib (drug)]] 0.05 µM 0.320× (z -22.2) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.161× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 2.58 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +12.4) | [[Pemetrexed (drug)]] 5 µM 0.0748× (z -8.9) |
| [[BT-474 (line)]] | alt | 39.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 3.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 41.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +16.9) | — |
| [[PANC-1 (line)]] | alt | 5.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +9.6) | — |
| [[A-427 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 6.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 25.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -8.9) |
| [[SW 900 (line)]] | alt | 6.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +12.0) | — |
| [[A-172 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLEC12]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[KCNN3]] | +0.65 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[IL1RAPL1]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PCSK2]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ADAMTSL1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[LRFN5]] | +0.58 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[OLFM2]] | +0.57 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[IL11]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SLCO2B1]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[COL22A1]] | +0.56 | +0.36 / +0.65 | both halves | 1e-04 |  |
| [[CYB5R2]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[LINC00973]] | +0.53 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC7]] | -0.45 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ZNF449]] | -0.45 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NHSL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[S1PR3]] | C | S1PR3 activity raises NHSL2's level | lines that do not express S1PR3 (21) vs lines expressing it (29) | 2.72× lower at baseline in the lines without S1PR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: BASP1, VEGFC, SPANXA2-OT1; co-absent with the target |
| [[COLEC12]] | C | COLEC12 activity raises NHSL2's level | lines that do not express COLEC12 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without COLEC12 | 0.063 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, PIEZO2, SLC22A17; maybe low, not absent; co-absent with the target |
| [[EML1]] | C | EML1 activity raises NHSL2's level | lines that do not express EML1 (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without EML1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1; co-absent with the target |
| [[GAS7]] | C | GAS7 activity raises NHSL2's level | lines that do not express GAS7 (24) vs lines expressing it (26) | 1.59× lower at baseline in the lines without GAS7 | 0.082 | ⚠ within organs, on part of the lines; also absent: COLEC12, ADCY1, MAPK4; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFPM2]] | B | NHSL2 activity raises ZFPM2's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 2.16× lower at baseline in the lines without NHSL2 | 0.069 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent |
| [[RHBDL3]] | B | NHSL2 activity raises RHBDL3's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without NHSL2 | 0.083 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent |
| [[FMNL3]] | B | NHSL2 activity raises FMNL3's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without NHSL2 | 0.092 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent |
| [[EML1]] | C | NHSL2 activity raises EML1's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 4.12× lower at baseline in the lines without NHSL2 | 0.008 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent; co-absent with the target |
| [[S1PR3]] | C | NHSL2 activity raises S1PR3's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 3.50× lower at baseline in the lines without NHSL2 | 0.014 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent; co-absent with the target |
| [[COLEC12]] | C | NHSL2 activity raises COLEC12's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 2.87× lower at baseline in the lines without NHSL2 | 0.025 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent; co-absent with the target |
| [[AFF3]] | C | NHSL2 activity raises AFF3's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 4.16× lower at baseline in the lines without NHSL2 | 0.089 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, 33.0); signed map (32.3, 25.4). **Vector** length 61.8, 16.5% of its response variance represented; |z| ≥ 3 in 586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.7 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +4.3 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.7 | +0.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.6 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | NHS like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,910,845-72,161,750 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NHS family |
| Matched by | ensembl_id |

UniProt [Q5HYW2](https://www.uniprot.org/uniprotkb/Q5HYW2) carries no function annotation.

**Summary**, from NCBI Gene [340527](https://www.ncbi.nlm.nih.gov/gene/340527):

> Predicted to enable calcium ion binding activity. Predicted to be involved in cell differentiation. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33737](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33737) · Entrez [340527](https://www.ncbi.nlm.nih.gov/gene/340527) · UniProt [Q5HYW2](https://www.uniprot.org/uniprotkb/Q5HYW2) · Ensembl [ENSG00000204131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204131)

## Data

Gene col 12817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12817); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12817]; `tensor/DDL_lfc|DDL_z.npy` [12817]; `embed/gene_vectors.npy` [12817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12817 or target_col == 12817). Every well: [[NHSL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NHSL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
