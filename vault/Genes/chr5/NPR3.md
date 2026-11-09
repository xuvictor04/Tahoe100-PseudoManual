---
symbol: "NPR3"
type: "gene"
col: 3459
ensembl_id: "ENSG00000113389"
name: "natriuretic peptide receptor 3"
location: "5p13.3"
module: 104
arm: "+"
pooled_cpm: 11.42
n_lines_expressing: 43
n_dd_up: 51
n_dd_down: 0
n_dd_up_clean: 42
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# NPR3

*natriuretic peptide receptor 3* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.60× (z +28.7, q 0e+00, up in 33 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.372×, HS-578T 0.342×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGC4859]] (+0.65, fdr 1e-05), [[SAMSN1]] (+0.63, fdr 1e-05), [[DCN]] (+0.62, fdr 1e-05); moves opposite to [[CSF2]] (-0.53, fdr 2e-05), [[LINC00973]] (-0.50, fdr 3e-05), [[ARMC9]] (-0.49, fdr 3e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MIR583HG]] → it (grade B ⚠); 4 go from it, the strongest it → [[LEPR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.60×** | +28.7 | 0e+00 | 33/37 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.32×** | +18.7 | 0e+00 | 27/35 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.93×** | +17.5 | 0e+00 | 28/34 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.07×** | +14.9 | 0e+00 | 26/40 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.97×** | +14.5 | 1e-45 | 32/41 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.90×** | +14.1 | 2e-43 | 27/41 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **6.17×** | +12.7 | 7e-35 | 31/37 (A498, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.91×** | +12.1 | 7e-32 | 22/41 (HOP62, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +11.2 | 3e-27 | 30/41 (SW480, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +11.0 | 3e-26 | 16/36 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.07×** | +9.6 | 3e-20 | 23/39 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +8.9 | 3e-17 | 17/34 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +8.8 | 7e-17 | 23/41 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.19×** | +8.1 | 3e-14 | 26/39 (J82, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.08×** | +7.8 | 2e-13 | 20/36 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +7.2 | 3e-11 | 24/41 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3459.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.372×, HS-578T 0.342×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.791× | -3.2 | 0.66 | 8/41 (SW48, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.83 | 18 | 0 | [[Triamcinolone (drug)]] 5 µM 6.53× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 72.1 | 10 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +10.2) ⚠ position not correctable · without an alert: [[Triamcinolone (drug)]] 5 µM 2.59× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.9) |
| [[SW480 (line)]] | alt | 3.43 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 22.3× (z +12.2) | — |
| [[LoVo (line)]] | wt | 3.71 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 30.4× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.89 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +10.7) | — |
| [[A498 (line)]] | wt | 15.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +10.7) | — |
| [[C32 (line)]] | wt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 6.66 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.30× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.92× (z +9.1) | — |
| [[A-172 (line)]] | wt | 5.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 4.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.64× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 2.90 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 63.7× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 3.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.1× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.8) |
| [[J82 (line)]] | alt | 5.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.63× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 3.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 22.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +8.8) | — |
| [[A-427 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGC4859]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SAMSN1]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DCN]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[LVRN]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LINC00607]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ANKRD7]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LEPR]] | +0.58 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[C12orf60]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[MAP7D2]] | +0.55 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[LINC01950]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[IRAK3]] | +0.54 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[STXBP5-AS1]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF2]] | -0.53 | -0.49 / -0.56 | both halves | 2e-05 |  |
| [[LINC00973]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ARMC9]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[EFL1]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PKIA]] | -0.45 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[GALNT6]] | -0.44 | -0.49 / -0.22 | both halves | 6e-04 |  |
| [[CXCL8]] | -0.44 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[SLAMF7]] | -0.44 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[IQCH]] | -0.44 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[MIR155HG]] | -0.44 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[BRD7]] | -0.43 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[CD274]] | -0.42 | -0.43 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR583HG]] | B | MIR583HG activity raises NPR3's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.95× lower at baseline in the lines without MIR583HG | 0.045 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[MGC4859]] | B | MGC4859 activity raises NPR3's level | lines that do not express MGC4859 (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without MGC4859 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC00922, LINC01811, LINC00276; maybe low, not absent |
| [[GALNT6]] | B | GALNT6 activity lowers NPR3's level | lines that do not express GALNT6 (14) vs lines expressing it (36) | 1.70× higher at baseline in the lines without GALNT6 | 0.081 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, ACOT11, TNFRSF10A-DT |
| [[TBXAS1]] | B | TBXAS1 activity raises NPR3's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.74× lower at baseline in the lines without TBXAS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEPR]] | B | NPR3 activity raises LEPR's level | lines that do not express NPR3 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without NPR3 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[WDR49]] | B | NPR3 activity raises WDR49's level | lines that do not express NPR3 (7) vs lines expressing it (43) | 2.39× lower at baseline in the lines without NPR3 | 0.071 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Selinexor (drug)]] 0.5 µM | B | NPR3 activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express NPR3 (7) vs lines expressing it (41) | the lines without NPR3: 0.90× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SNX31]] | B | NPR3 activity raises SNX31's level | lines that do not express NPR3 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without NPR3 | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.5, 19.5); signed map (20.4, 30.7). **Vector** length 101, 23.2% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +28.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +18.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +17.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +12.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.9 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.9 | +4.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | +3.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -0.1 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | natriuretic peptide receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:32,689,070-32,791,724 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GUCY2B, FLJ14054; previously NPRC, ANPRC, C5orf23 |
| Gene groups (HGNC) | DENN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17342](https://www.uniprot.org/uniprotkb/P17342) (Atrial natriuretic peptide receptor 3):

> Receptor for the natriuretic peptide hormones, binding with similar affinities atrial natriuretic peptide NPPA/ANP, brain natriuretic peptide NPPB/BNP, and C-type natriuretic peptide NPPC/CNP. May function as a clearance receptor for NPPA, NPPB and NPPC, regulating their local concentrations and effects. Acts as a regulator of osteoblast differentiation and bone growth by binding to its ligand osteocrin, thereby preventing binding between NPR3/NPR-C and natriuretic peptides, leading to increase …

**Summary**, from NCBI Gene [4883](https://www.ncbi.nlm.nih.gov/gene/4883):

> This gene encodes one of three natriuretic peptide receptors. Natriutetic peptides are small peptides which regulate blood volume and pressure, pulmonary hypertension, and cardiac function as well as some metabolic and growth processes. The product of this gene encodes a natriuretic peptide receptor responsible for clearing circulating and extracellular natriuretic peptides through endocytosis of the receptor. Multiple transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:7945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7945) · Entrez [4883](https://www.ncbi.nlm.nih.gov/gene/4883) · UniProt [P17342](https://www.uniprot.org/uniprotkb/P17342) · Ensembl [ENSG00000113389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113389)

## Data

Gene col 3459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3459); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3459]; `tensor/DDL_lfc|DDL_z.npy` [3459]; `embed/gene_vectors.npy` [3459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3459 or target_col == 3459). Every well: [[NPR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
