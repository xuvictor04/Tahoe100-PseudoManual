---
symbol: "GPR37"
type: "gene"
col: 10001
ensembl_id: "ENSG00000170775"
name: "G protein-coupled receptor 37"
location: "7q31.33"
module: 167
arm: "+"
pooled_cpm: 2.28
n_lines_expressing: 31
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# GPR37

*G protein-coupled receptor 37* — 7q31.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.47× (z +10.9, q 6e-25, up in 19 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.543× (z -5.0, q 4e-04, down in 9 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.151×, NCI-H2030 0.327×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (HT-29 0.0996×, NCI-H1573 0.108×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.118×; ⚠ toxic; transcription drop); [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0635×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.295×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGCG]] (+0.60, fdr 2e-05), [[FLRT3]] (+0.57, fdr 2e-05), [[KLF5]] (+0.57, fdr 2e-05); moves opposite to [[GPALPP1]] (-0.52, fdr 2e-04), [[FAM156A]] (-0.51, fdr 1e-04), [[APTX]] (-0.50, fdr 1e-04).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 5 go from it, the strongest it → [[PRKAR2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.47×** | +10.9 | 6e-25 | 19/23 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +8.5 | 4e-15 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.44×** | +7.6 | 6e-12 | 14/19 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.11×** | +6.4 | 3e-08 | 10/24 (C32, A-427, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +6.1 | 1e-07 | 1/11 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +5.6 | 2e-06 | 3/9 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +5.4 | 5e-06 | 5/19 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +5.3 | 7e-06 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +5.2 | 1e-05 | 3/24 (C32, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +4.5 | 3e-04 | 3/18 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.73×** | +4.5 | 3e-04 | 6/16 (HT-29, A-427, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.05×** | +4.4 | 6e-04 | 2/11 (A-427, A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.015 | 8/24 (NCI-H23, LoVo, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.5 | 0.021 | 0/13 | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.10 | 7/24 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10001.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.151×, NCI-H2030 0.327×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (HT-29 0.0996×, NCI-H1573 0.108×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.118×; ⚠ toxic; transcription drop); [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0635×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.295×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.543×** | -5.0 | 4e-04 | 9/19 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.605×** | -4.2 | 0.006 | 12/21 (A498, NCI-H2030, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.769× | -3.2 | 0.22 | 8/22 (NCI-H1792, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.702× | -3.1 | 0.30 | 11/24 (HT-29, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 6.75 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.0635× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 18.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.0) |
| [[HT-29 (line)]] | alt | 7.34 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0996× (z -9.8) |
| [[A-172 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.704 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.796 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.624 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.152 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.621 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.938 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.159 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.656 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.188 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.855 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.217 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGCG]] | +0.60 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[FLRT3]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[KLF5]] | +0.57 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[AHR]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[BIRC3]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[TCIM]] | +0.55 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[LINC00540]] | +0.54 | +0.29 / +0.53 | both halves | 2e-04 |  |
| [[CYP2J2]] | +0.53 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[ELOVL4]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[XDH]] | +0.53 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[PLSCR4]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[S100A9]] | +0.51 | +0.36 / +0.54 | both halves | 9e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPALPP1]] | -0.52 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[FAM156A]] | -0.51 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[APTX]] | -0.50 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[PMS2P4-1]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SLC30A6]] | -0.49 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ACO2]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[GLE1]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TTC28-AS1]] | -0.47 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[UNKL]] | -0.47 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[BABAM1]] | -0.47 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[VIPAS39]] | -0.47 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[SPG7]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises GPR37's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RHOV]] | B | RHOV activity raises GPR37's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.28× lower at baseline in the lines without RHOV | 0.077 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[TARID]] | B | TARID activity raises GPR37's level | lines that do not express TARID (29) vs lines expressing it (21) | 1.53× lower at baseline in the lines without TARID | 0.089 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[PON3]] | B | PON3 activity raises GPR37's level | lines that do not express PON3 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without PON3 | 0.098 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKAR2B]] | B | GPR37 activity raises PRKAR2B's level | lines that do not express GPR37 (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without GPR37 | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ECHDC3, L3MBTL4 |
| [[IL15]] | B | GPR37 activity raises IL15's level | lines that do not express GPR37 (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without GPR37 | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ECHDC3, L3MBTL4 |
| [[AHR]] | B | GPR37 activity raises AHR's level | lines that do not express GPR37 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without GPR37 | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ECHDC3, L3MBTL4 |
| [[PLSCR4]] | C | GPR37 activity raises PLSCR4's level | lines that do not express GPR37 (19) vs lines expressing it (31) | 3.04× lower at baseline in the lines without GPR37 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ECHDC3, L3MBTL4; co-absent with the target |
| [[CFH]] | C | GPR37 activity raises CFH's level | lines that do not express GPR37 (19) vs lines expressing it (31) | 2.90× lower at baseline in the lines without GPR37 | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ECHDC3, L3MBTL4; co-absent with the target |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 48.0); signed map (52.2, 23.7). **Vector** length 41.7, 7.56% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.3 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.4 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +0.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.4 | -5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.8 | -2.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.33 — chr7:124,743,885-124,765,792 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EDNRBL, hET(B)R-LP, PAELR |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [O15354](https://www.uniprot.org/uniprotkb/O15354) (Prosaposin receptor GPR37):

> G protein-coupled receptor that plays a role in several physiological pathways such as resolution of inflammatory pain and oligodendrocyte differentiation (By similarity). Acts as a receptor for several ligands including prosaposin, osteocalcin or neuroprotectin D1. Ligand binding induces endocytosis, followed by an ERK phosphorylation cascade. Acts as a receptor for osteocalcin (OCN) to regulate oligodendrocyte differentiation and central nervous system myelination. Mechanistically, plays a …

**Summary**, from NCBI Gene [2861](https://www.ncbi.nlm.nih.gov/gene/2861):

> This gene is a member of the G protein-coupled receptor family. The encoded protein contains seven transmembrane domains and is found in cell and endoplasmic reticulum membranes. G protein-coupled receptors are involved in translating outside signals into G protein mediated intracellular effects. This gene product interacts with Parkin and is involved in juvenile Parkinson disease. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:4494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4494) · Entrez [2861](https://www.ncbi.nlm.nih.gov/gene/2861) · UniProt [O15354](https://www.uniprot.org/uniprotkb/O15354) · Ensembl [ENSG00000170775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170775)

## Data

Gene col 10001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10001); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10001]; `tensor/DDL_lfc|DDL_z.npy` [10001]; `embed/gene_vectors.npy` [10001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10001 or target_col == 10001). Every well: [[GPR37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
