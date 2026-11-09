---
symbol: "CLDN16"
type: "gene"
col: 3512
ensembl_id: "ENSG00000113946"
name: "claudin 16"
location: "3q28"
module: 19
arm: "+"
pooled_cpm: 5.68
n_lines_expressing: 23
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CLDN16

*claudin 16* — 3q28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 5.97× (z +15.9, q 0e+00, up in 4 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.75× (z +13.7, q 3e-40, up in 8 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.656× (z -3.8, q 0.069, down in 9 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.151×, KATO III 0.131×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0572×, NCI-H460 0.103×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (A-427 0.286×, Hs 766T 0.119×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1QTNF1-AS1]] (+0.65, fdr 4e-05), [[QPCT]] (+0.63, fdr 3e-05), [[LINC01010]] (+0.61, fdr 2e-05); moves opposite to [[HAUS3]] (-0.52, fdr 1e-04), [[SELENOO]] (-0.51, fdr 2e-04), [[CLTCL1]] (-0.50, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[YBX3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.97×** | +15.9 | 0e+00 | 4/7 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +13.7 | 3e-40 | 8/18 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.04×** | +13.4 | 1e-38 | 7/12 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.00×** | +12.8 | 2e-35 | 5/7 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +7.2 | 5e-11 | 7/18 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.04×** | +6.8 | 8e-10 | 9/20 (LOX-IMVI, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.1 | 7e-08 | 8/20 (HEC-1-A, SNU-423, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +5.7 | 9e-07 | 2/15 (HEC-1-A, A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +5.7 | 9e-07 | 7/19 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.6 | 1e-06 | 2/18 (HEC-1-A, HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.86×** | +5.3 | 7e-06 | 1/6 (HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.0 | 2e-05 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.0 | 2e-05 | 6/20 (HOP62, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.00×** | +4.7 | 9e-05 | 1/11 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.007 | 4/20 (NCI-H2030, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.038 | 0/19 | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.078 | 4/19 (A-427, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.56×** | +3.0 | 0.078 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.083 | 0/15 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3512.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.151×, KATO III 0.131×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0572×, NCI-H460 0.103×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (A-427 0.286×, Hs 766T 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.656×** | -3.8 | 0.069 | 9/19 (A498, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.704× | -3.4 | 0.20 | 7/20 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.731× | -3.0 | 0.48 | 8/20 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 76.4 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.171× (z -13.8) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.204× (z -12.5) |
| [[KATO III (line)]] | alt | 7.46 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 44.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.54× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 9.80 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.2) |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.119× (z -9.1) |
| [[J82 (line)]] | alt | 1.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 7.11 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -8.9) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW480 (line)]] | alt | 2.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0873× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.835 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.907 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.817 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QTNF1-AS1]] | +0.65 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[QPCT]] | +0.63 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[LINC01010]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[CLDN1]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 | same gene group; pathway: Cell junction organization; STRING 831; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[MIR1915HG]] | +0.60 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[ABCC9]] | +0.58 | +0.40 / +0.46 | both halves | 4e-05 |  |
| [[LINC02605]] | +0.58 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[OLR1]] | +0.57 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[LMNTD1]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[DLGAP1]] | +0.57 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[TNFRSF11B]] | +0.56 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[PSG4]] | +0.56 | +0.32 / +0.46 | both halves | 1e-04 |  |
| [[TM4SF1-AS1]] | +0.56 | +0.39 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAUS3]] | -0.52 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[SELENOO]] | -0.51 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[CLTCL1]] | -0.50 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[SLC25A42]] | -0.50 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[PKD1P6]] | -0.50 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[MLXIP]] | -0.49 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[PCYT1A]] | -0.48 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[PKD1]] | -0.47 | -0.44 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLDN16's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02605]] | B | LINC02605 activity lowers CLDN16's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 2.00× higher at baseline in the lines without LINC02605 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[CLDN1]] | C | CLDN1 activity raises CLDN16's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 2.40× lower at baseline in the lines without CLDN1 | 0.053 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YBX3]] | B | CLDN16 activity raises YBX3's level | lines that do not express CLDN16 (27) vs lines expressing it (23) | 1.85× lower at baseline in the lines without CLDN16 | 0.067 | ⚠ within organs, on part of the lines; also absent: DAW1, ENSG00000257869, ENSG00000255029 |
| [[LINC02068]] | B | CLDN16 activity raises LINC02068's level | lines that do not express CLDN16 (27) vs lines expressing it (23) | 1.37× lower at baseline in the lines without CLDN16 | 0.091 | ⚠ within organs, on part of the lines; also absent: DAW1, ENSG00000257869, ENSG00000255029 |
| [[CLDN1]] | C | CLDN16 activity raises CLDN1's level | lines that do not express CLDN16 (27) vs lines expressing it (23) | 6.37× lower at baseline in the lines without CLDN16 | 2e-04 | ⚠ within organs, on part of the lines; also absent: DAW1, ENSG00000257869, ENSG00000255029; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.9, 26.6); signed map (42.9, 16.5). **Vector** length 40.6, 7.67% of its response variance represented; |z| ≥ 3 in 509 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +15.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +2.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -1.6 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | claudin 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q28 — chr3:190,322,541-190,412,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCLN1, HOMG3 |
| Gene groups (HGNC) | Claudins |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5I7](https://www.uniprot.org/uniprotkb/Q9Y5I7) (Claudin-16):

> Forms paracellular channels: coassembles with CLDN19 into tight junction strands with cation-selective channels through the strands, conveying epithelial permeability in a process known as paracellular tight junction permeability. Involved in the maintenance of ion gradients along the nephron. In the thick ascending limb (TAL) of Henle's loop, facilitates sodium paracellular permeability from the interstitial compartment to the lumen, contributing to the lumen-positive transepithelial potential …

**Summary**, from NCBI Gene [10686](https://www.ncbi.nlm.nih.gov/gene/10686):

> Tight junctions represent one mode of cell-to-cell adhesion in epithelial or endothelial cell sheets, forming continuous seals around cells and serving as a physical barrier to prevent solutes and water from passing freely through the paracellular space. These junctions are comprised of sets of continuous networking strands in the outwardly facing cytoplasmic leaflet, with complementary grooves in the inwardly facing extracytoplasmic leaflet. The protein encoded by this gene, a member of the …

**Accessions** — [HGNC:2037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2037) · Entrez [10686](https://www.ncbi.nlm.nih.gov/gene/10686) · UniProt [Q9Y5I7](https://www.uniprot.org/uniprotkb/Q9Y5I7) · Ensembl [ENSG00000113946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113946)

## Data

Gene col 3512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3512); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3512]; `tensor/DDL_lfc|DDL_z.npy` [3512]; `embed/gene_vectors.npy` [3512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3512 or target_col == 3512). Every well: [[CLDN16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
