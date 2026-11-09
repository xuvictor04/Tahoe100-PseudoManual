---
symbol: "SHROOM2"
type: "gene"
col: 7135
ensembl_id: "ENSG00000146950"
name: "shroom family member 2"
location: "Xp22.2"
module: 97
arm: "+"
pooled_cpm: 11.23
n_lines_expressing: 35
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# SHROOM2

*shroom family member 2* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.92× (z +13.2, q 4e-37, up in 19 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.651× (z -6.2, q 4e-07, down in 18 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGFBR2]] (+0.59, fdr 1e-05), [[SCAP]] (+0.58, fdr 1e-05), [[TBC1D2B]] (+0.58, fdr 3e-05); moves opposite to [[NEK11]] (-0.53, fdr 9e-05), [[CYP27C1]] (-0.53, fdr 4e-05), [[DUSP28]] (-0.53, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 3 go from it, the strongest it → [[CCNJL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, none with an alert; shown: the 15 strongest. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +13.2 | 4e-37 | 19/32 (NCI-H460, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +11.0 | 1e-25 | 25/32 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +10.5 | 2e-23 | 25/32 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +10.1 | 1e-21 | 25/32 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +9.4 | 5e-19 | 19/32 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.88×** | +9.0 | 2e-17 | 19/28 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.48×** | +6.8 | 8e-10 | 21/31 (NCI-H460, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 4e-06 | 14/32 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.46×** | +5.4 | 4e-06 | 11/32 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.49×** | +5.2 | 9e-06 | 10/30 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.42×** | +5.0 | 2e-05 | 13/32 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.37×** | +4.5 | 4e-04 | 10/32 (HOP62, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 4e-04 | 9/30 (A549, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 6e-04 | 10/30 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 9e-04 | 10/32 (Hs 766T, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7135.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.651×** | -6.2 | 4e-07 | 18/31 (SW480, Panc 03.27, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -5.4 | 2e-05 | 5/33 (HOP62, SNU-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -4.8 | 3e-04 | 10/32 (SW480, SW 1271, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.726×** | -4.6 | 6e-04 | 12/32 (LoVo, A549, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.728×** | -4.6 | 6e-04 | 16/31 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -4.4 | 9e-04 | 10/29 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.726×** | -4.2 | 0.002 | 9/30 (RKO, SK-MEL-2, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.827×** | -3.9 | 0.008 | 14/29 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.753×** | -3.8 | 0.010 | 13/17 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.735×** | -3.2 | 0.088 | 8/29 (A549, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.790× | -3.1 | 0.10 | 10/29 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.312× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 3.21 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.45× (z +10.9) | — |
| [[A-427 (line)]] | wt | 19.6 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0796× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 27.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0945× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 46.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0903× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0874× (z -8.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[A-172 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFBR2]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SCAP]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D2B]] | +0.58 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[DAB2IP]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MT1A]] | +0.57 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[RHOBTB2]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[PDE9A]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[TGFBR3]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FGD4]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ASB13]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CCND3]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MT2A]] | +0.54 | +0.40 / +0.41 | both halves | 5e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK11]] | -0.53 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[CYP27C1]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[DUSP28]] | -0.53 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ALG13]] | -0.52 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[TM9SF5P]] | -0.51 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[LINC01004]] | -0.51 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[BHLHE40-AS1]] | -0.50 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[LINC00310]] | -0.50 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[RNF217-AS1]] | -0.49 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[LINC00944]] | -0.48 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[ATXN1L]] | -0.48 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[RNPC3-DT]] | -0.48 | -0.26 / -0.37 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises SHROOM2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[ETNK2]] | B | ETNK2 activity raises SHROOM2's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 2.50× lower at baseline in the lines without ETNK2 | 0.051 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[RAPGEF5]] | B | RAPGEF5 activity raises SHROOM2's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without RAPGEF5 | 0.094 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCNJL]] | B | SHROOM2 activity raises CCNJL's level | lines that do not express SHROOM2 (15) vs lines expressing it (35) | 1.95× lower at baseline in the lines without SHROOM2 | 0.012 | ⚠ within organs, on part of the lines; also absent: GPR143, RASGEF1C |
| [[PXDNL]] | B | SHROOM2 activity lowers PXDNL's level | lines that do not express SHROOM2 (15) vs lines expressing it (35) | 1.33× higher at baseline in the lines without SHROOM2 | 0.044 | ⚠ within organs, on part of the lines; also absent: GPR143, RASGEF1C |
| [[MERTK]] | B | SHROOM2 activity raises MERTK's level | lines that do not express SHROOM2 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without SHROOM2 | 0.092 | ⚠ within organs, on part of the lines; also absent: GPR143, RASGEF1C |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.7, 11.7); signed map (14.1, 32.6). **Vector** length 63.7, 12.8% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +13.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +9.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +6.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +4.4 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | shroom family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:9,786,429-9,949,443 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously APXL |
| Gene groups (HGNC) | PDZ domain containing; Shroom family |
| Hallmark sets | APICAL_SURFACE, APICAL_JUNCTION, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13796](https://www.uniprot.org/uniprotkb/Q13796) (Protein Shroom2):

> May be involved in endothelial cell morphology changes during cell spreading. In the retinal pigment epithelium, may regulate the biogenesis of melanosomes and promote their association with the apical cell surface by inducing gamma-tubulin redistribution (By similarity).

**Summary**, from NCBI Gene [357](https://www.ncbi.nlm.nih.gov/gene/357):

> This gene represents the human homolog of Xenopus laevis apical protein (APX) gene, which is implicated in amiloride-sensitive sodium channel activity. It is expressed in endothelial cells and facilitates the formation of a contractile network within endothelial cells. Depletion of this gene results in an increase in endothelial sprouting, migration, and angiogenesis. This gene is highly expressed in the retina, and is a strong candidate for ocular albinism type 1 syndrome. Alternatively …

**Accessions** — [HGNC:630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:630) · Entrez [357](https://www.ncbi.nlm.nih.gov/gene/357) · UniProt [Q13796](https://www.uniprot.org/uniprotkb/Q13796) · Ensembl [ENSG00000146950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146950)

## Data

Gene col 7135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7135); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7135]; `tensor/DDL_lfc|DDL_z.npy` [7135]; `embed/gene_vectors.npy` [7135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7135 or target_col == 7135). Every well: [[SHROOM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHROOM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
