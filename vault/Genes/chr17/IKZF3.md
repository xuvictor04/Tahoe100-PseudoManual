---
symbol: "IKZF3"
type: "gene"
col: 8432
ensembl_id: "ENSG00000161405"
name: "IKAROS family zinc finger 3"
location: "17q12-q21.1"
module: 1
arm: "+"
pooled_cpm: 8.73
n_lines_expressing: 19
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 14
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# IKZF3

*IKAROS family zinc finger 3* — 17q12-q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.4× (z +39.1, q 0e+00, up in 15 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.291×, SNU-1 0.347×); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.207×, SNU-1 0.159×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35F2]] (+0.56, fdr 1e-05), [[PAK1IP1]] (+0.56, fdr 1e-05), [[P2RY1]] (+0.53, fdr 2e-05); moves opposite to [[GHITM]] (-0.50, fdr 5e-05), [[ATF6B]] (-0.50, fdr 3e-05), [[ADIPOR1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[KCNQ4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.4×** | +39.1 | 0e+00 | 15/15 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.94×** | +24.8 | 0e+00 | 8/14 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.29×** | +16.0 | 0e+00 | 11/12 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.73×** | +15.8 | 0e+00 | 16/17 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +10.9 | 8e-26 | 11/16 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.47×** | +9.2 | 3e-18 | 8/13 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.16×** | +8.5 | 2e-15 | 9/17 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.26×** | +8.3 | 8e-15 | 1/6 (CFPAC-1) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.11×** | +8.2 | 1e-14 | 5/17 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.21×** | +8.0 | 5e-14 | 1/10 (CFPAC-1) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +7.9 | 2e-13 | 11/15 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.97×** | +7.4 | 5e-12 | 0/10 | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +6.7 | 7e-10 | 15/17 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +5.5 | 1e-06 | 3/16 (LoVo, BT-474, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.42×** | +5.4 | 2e-06 | 7/17 (A-427, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.4 | 3e-06 | 3/17 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +5.2 | 8e-06 | 4/17 (NCI-H2030, SNU-1, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +4.9 | 3e-05 | 5/17 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +4.5 | 2e-04 | 8/17 (NCI-H2347, SNU-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.003 | 0/17 | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.012 | 0/15 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8432.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.291×, SNU-1 0.347×); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.207×, SNU-1 0.159×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | 0.716× | -3.7 | 0.13 | 1/17 (NCI-H2347) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.722× | -3.3 | 0.25 | 1/17 (KATO III) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 60.3 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -8.9) |
| [[PANC-1 (line)]] | alt | 8.02 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +20.4) | — |
| [[RKO (line)]] | wt | 51.7 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +27.5) | — |
| [[A-427 (line)]] | wt | 9.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +11.0) | — |
| [[A498 (line)]] | wt | 3.49 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +14.0) | — |
| [[KATO III (line)]] | alt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.375× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[CFPAC-1 (line)]] | alt | 4.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +14.1) | — |
| [[LoVo (line)]] | wt | 3.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.80× (z +18.9) | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[Panc 03.27 (line)]] | alt | 3.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +10.2) | — |
| [[A-172 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35F2]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PAK1IP1]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[P2RY1]] | +0.53 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[TSPAN2]] | +0.53 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[EPOP]] | +0.52 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[BRIX1]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ZNF485]] | +0.51 | +0.51 / +0.48 | both halves | 2e-05 | same gene group |
| [[ZNF620]] | +0.51 | +0.49 / +0.52 | both halves | 1e-05 | same gene group |
| [[NOC3L]] | +0.51 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[C12orf29]] | +0.51 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[RASGRF1]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[LRRC8B]] | +0.50 | +0.41 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GHITM]] | -0.50 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[ATF6B]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ADIPOR1]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MCFD2]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CTSD]] | -0.48 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[DCAF11]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PBXIP1]] | -0.47 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[PCYOX1]] | -0.47 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[GNPTG]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[UFD1]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SEL1L]] | -0.46 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[OS9]] | -0.46 | -0.34 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IKZF3's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNK5]] | C | KCNK5 activity raises IKZF3's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 2.64× lower at baseline in the lines without KCNK5 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNQ4]] | B | IKZF3 activity raises KCNQ4's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without IKZF3 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[TNFRSF10A-DT]] | B | IKZF3 activity raises TNFRSF10A-DT's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without IKZF3 | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| cells under [[AZD2858 (drug)]] 0.5 µM | B | IKZF3 activity lowers the cells' numbers under AZD2858 0.5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.24× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[SLC16A9]] | B | IKZF3 activity raises SLC16A9's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.49× lower at baseline in the lines without IKZF3 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[PPIL1]] | B | IKZF3 activity raises PPIL1's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.27× lower at baseline in the lines without IKZF3 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| cells under [[crizotinib (drug)]] 5 µM | B | IKZF3 activity lowers the cells' numbers under crizotinib 5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.16× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| cells under [[Harringtonine (drug)]] 5 µM | B | IKZF3 activity lowers the cells' numbers under Harringtonine 5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.78× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| cells under [[Adagrasib (drug)]] 5 µM | B | IKZF3 activity lowers the cells' numbers under Adagrasib 5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.15× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[EPOP]] | B | IKZF3 activity raises EPOP's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.43× lower at baseline in the lines without IKZF3 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| cells under [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.5 µM | B | IKZF3 activity lowers the cells' numbers under Methyl aminolevulinate (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.16× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| cells under [[Busulfan (drug)]] 5 µM | B | IKZF3 activity lowers the cells' numbers under Busulfan 5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.09× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| cells under [[Pimitespib (drug)]] 5 µM | B | IKZF3 activity raises the cells' numbers under Pimitespib 5 µM (protects the cells) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 0.82× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-2.3, 3.8); signed map (-0.6, -41.9). **Vector** length 47.9, 12.4% of its response variance represented; |z| ≥ 3 in 409 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.5 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.1 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +39.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.2 | +3.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +0.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | IKAROS family zinc finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12-q21.1 — chr17:39,757,718-39,864,312 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Aiolos; previously ZNFN1A3 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 6 pathways, smallest: Interaction of NuRD complexes with transcription factors; NuRD complex assembly; CHD3, CHD4, CHD5 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKT9](https://www.uniprot.org/uniprotkb/Q9UKT9) (Zinc finger protein Aiolos):

> Transcription factor that plays an important role in the regulation of lymphocyte differentiation. Plays an essential role in regulation of B-cell differentiation, proliferation and maturation to an effector state. Involved in regulating BCL2 expression and controlling apoptosis in T-cells in an IL2-dependent manner.

**Summary**, from NCBI Gene [22806](https://www.ncbi.nlm.nih.gov/gene/22806):

> This gene encodes a member of the Ikaros family of zinc-finger proteins. Three members of this protein family (Ikaros, Aiolos and Helios) are hematopoietic-specific transcription factors involved in the regulation of lymphocyte development. This gene product is a transcription factor that is important in the regulation of B lymphocyte proliferation and differentiation. Both Ikaros and Aiolos can participate in chromatin remodeling. Regulation of gene expression in B lymphocytes by Aiolos is …

**Accessions** — [HGNC:13178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13178) · Entrez [22806](https://www.ncbi.nlm.nih.gov/gene/22806) · UniProt [Q9UKT9](https://www.uniprot.org/uniprotkb/Q9UKT9) · Ensembl [ENSG00000161405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161405)

## Data

Gene col 8432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8432); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8432]; `tensor/DDL_lfc|DDL_z.npy` [8432]; `embed/gene_vectors.npy` [8432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8432 or target_col == 8432). Every well: [[IKZF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IKZF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
