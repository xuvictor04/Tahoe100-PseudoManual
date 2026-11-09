---
symbol: "OTULINL"
type: "gene"
col: 7005
ensembl_id: "ENSG00000145569"
name: "OTU deubiquitinase with linear linkage specificity like"
location: "5p15.2"
module: 176
arm: "+"
pooled_cpm: 6.23
n_lines_expressing: 43
n_dd_up: 36
n_dd_down: 8
n_dd_up_clean: 29
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# OTULINL

*OTU deubiquitinase with linear linkage specificity like* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.62× (z +24.2, q 0e+00, up in 38 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.648× (z -5.6, q 1e-05, down in 12 of 40 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AIF1L]] (+0.58, fdr 8e-05), [[KCNS3]] (+0.58, fdr 6e-05), [[MMP15]] (+0.55, fdr 5e-05); moves opposite to [[ASH1L]] (-0.54, fdr 5e-05), [[ANKHD1-EIF4EBP3]] (-0.51, fdr 3e-04), [[CREBBP]] (-0.50, fdr 1e-04).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SCD5]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[AZD-8055 (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.62×** | +24.2 | 0e+00 | 38/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.05×** | +23.0 | 0e+00 | 38/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.28×** | +18.6 | 0e+00 | 37/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.08×** | +18.0 | 0e+00 | 38/39 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.65×** | +17.5 | 0e+00 | 37/39 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.62×** | +16.4 | 0e+00 | 18/24 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +14.5 | 1e-45 | 24/36 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.07×** | +14.3 | 1e-44 | 29/36 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.26×** | +14.0 | 2e-42 | 10/16 (LoVo, SHP-77, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.07×** | +13.8 | 1e-41 | 9/13 (LoVo, HOP62, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.90×** | +13.6 | 2e-40 | 27/33 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +10.8 | 2e-25 | 23/37 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +9.7 | 1e-20 | 19/37 (C32, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **4.22×** | +9.6 | 3e-20 | 23/38 (A498, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.0 | 1e-10 | 15/40 (A549, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.56×** | +5.6 | 6e-07 | 12/39 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.49×** | +4.9 | 4e-05 | 8/38 (SHP-77, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.45×** | +4.8 | 6e-05 | 10/39 (SHP-77, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7005.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -5.6 | 1e-05 | 12/40 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.692×** | -4.8 | 6e-04 | 9/30 (BT-474, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -4.3 | 0.003 | 15/31 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.731×** | -4.0 | 0.008 | 14/39 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.738×** | -3.7 | 0.025 | 9/39 (SW 1271, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.755×** | -3.6 | 0.027 | 14/38 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.749×** | -3.6 | 0.027 | 11/36 (J82, CHP-212, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.768×** | -3.4 | 0.046 | 13/39 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.786× | -3.1 | 0.11 | 7/36 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 38.9 | 15 | 0 | [[Dexamethasone (drug)]] 5 µM 7.23× (z +11.8) | — |
| [[SW480 (line)]] | alt | 3.34 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 29.7× (z +14.4) | — |
| [[LoVo (line)]] | wt | 14.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.88× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 1.77 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +12.4) | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -8.9) |
| [[A498 (line)]] | wt | 8.79 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 2.87 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 18.7× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.83× (z +9.3) | — |
| [[A-172 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIF1L]] | +0.58 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[KCNS3]] | +0.58 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[MMP15]] | +0.55 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[RAB39A]] | +0.55 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[TOX2]] | +0.55 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[PTPRU]] | +0.55 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[C1orf21]] | +0.54 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[MBOAT2]] | +0.54 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[ATP1A3]] | +0.54 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[SEMA4D]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.53 | +0.24 / +0.62 | both halves | 4e-04 |  |
| [[PPP1R14C]] | +0.53 | +0.31 / +0.65 | both halves | 2e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASH1L]] | -0.54 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ANKHD1-EIF4EBP3]] | -0.51 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[CREBBP]] | -0.50 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[HERC4]] | -0.50 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[GTF2IRD2B]] | -0.49 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[CKMT2-AS1]] | -0.48 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[ELP4]] | -0.48 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[SON]] | -0.46 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[N4BP2L2]] | -0.46 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[MAU2]] | -0.46 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[LINC02100]] | -0.46 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[MED13]] | -0.45 | -0.30 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCD5]] | B | SCD5 activity lowers OTULINL's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without SCD5 | 0.060 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[NR3C1]] | B | NR3C1 activity raises OTULINL's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[DAB2IP]] | C | DAB2IP activity raises OTULINL's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without DAB2IP | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[AZD-8055 (drug)]] 5 µM | B | OTULINL activity raises the cells' numbers under AZD-8055 5 µM (protects the cells) | lines that do not express OTULINL (7) vs lines expressing it (41) | the lines without OTULINL: 0.76× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: PLP2, LRFN4, C12orf75; maybe low, not absent |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.0, 40.4); signed map (-23.5, 35.0). **Vector** length 68.9, 11.7% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +17.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +6.6 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +6.6 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +6.4 | +14.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +9.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +9.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.7 | +4.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -4.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase with linear linkage specificity like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:14,581,792-14,616,180 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11127, NET20; previously FAM105A |
| Gene groups (HGNC) | OTU domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUU6](https://www.uniprot.org/uniprotkb/Q9NUU6) (Inactive ubiquitin thioesterase OTULINL):

> Lacks deubiquitinase activity.

**Summary**, from NCBI Gene [54491](https://www.ncbi.nlm.nih.gov/gene/54491):

> Located in cytoplasmic side of endoplasmic reticulum membrane and nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25629) · Entrez [54491](https://www.ncbi.nlm.nih.gov/gene/54491) · UniProt [Q9NUU6](https://www.uniprot.org/uniprotkb/Q9NUU6) · Ensembl [ENSG00000145569](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145569)

## Data

Gene col 7005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7005); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7005]; `tensor/DDL_lfc|DDL_z.npy` [7005]; `embed/gene_vectors.npy` [7005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7005 or target_col == 7005). Every well: [[OTULINL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTULINL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
