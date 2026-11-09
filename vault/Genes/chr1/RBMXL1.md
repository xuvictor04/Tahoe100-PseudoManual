---
symbol: "RBMXL1"
type: "gene"
col: 13109
ensembl_id: "ENSG00000213516"
name: "RBMX like 1"
location: "1p22.2"
module: 219
arm: "+"
pooled_cpm: 12.96
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# RBMXL1

*RBMX like 1* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +14.8, q 0e+00, up in 41 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (PANC-1 3.57×, J82 3.46×, NCI-H460 3.26×, HOP62 3.50×, …).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.669× (z -5.7, q 8e-06, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TANK]] (+0.65, fdr 1e-05), [[ZNF274]] (+0.63, fdr 1e-05), [[KYAT3]] (+0.60, fdr 4e-05, ⚠ same locus), [[CAAP1]] (+0.58, fdr 2e-05); moves opposite to [[ARHGEF7]] (-0.61, fdr 1e-05), [[NAP1L4]] (-0.59, fdr 1e-05), [[PDK1]] (-0.58, fdr 1e-05).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAGEA4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13109.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (PANC-1 3.57×, J82 3.46×, NCI-H460 3.26×, HOP62 3.50×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +14.8 | 0e+00 | 41/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.54×** | +6.1 | 3e-07 | 24/46 (SK-MEL-2, PANC-1, …) | top dose only | composition shift |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.24× | +3.2 | 0.20 | 9/44 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.24× | +3.2 | 0.20 | 13/46 (A-172, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.22 | 18/48 (HS-578T, NCI-H460, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13109.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -5.7 | 8e-06 | 24/45 (A-427, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -5.5 | 1e-05 | 22/47 (SHP-77, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.512×** | -5.1 | 5e-05 | 19/48 (SK-MEL-2, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -4.8 | 2e-04 | 21/46 (HepG2/C3A, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.539×** | -4.7 | 2e-04 | 22/44 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.834× | -3.8 | 0.017 | 13/48 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.788×** | -3.5 | 0.039 | 14/47 (SNU-423, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -3.5 | 0.039 | 9/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.783×** | -3.3 | 0.057 | 9/47 (NCI-H23, LoVo, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.065 | 11/48 (RPMI-7951, C-33 A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -3.2 | 0.065 | 7/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.808×** | -3.1 | 0.084 | 13/45 (SW48, C-33 A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.813× | -3.0 | 0.11 | 14/47 (NCI-H23, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +9.8) | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0894× (z -13.3) |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0808× (z -9.9) |
| [[HOP62 (line)]] | alt | 8.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.2) | — |
| [[J82 (line)]] | alt | 18.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0858× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.103× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 8.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.6) | — |
| [[A498 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANK]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[ZNF274]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[KYAT3]] | +0.60 | +0.42 / +0.71 | both halves | 4e-05 | STRING 443; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CAAP1]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ZNF140]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TMEM265]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CD163L1]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SOCS3]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[BCL10]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[STK16]] | +0.55 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[SLC31A2]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[HDX]] | +0.55 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ZNF641]] | +0.55 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF7]] | -0.61 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[PDK1]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.58 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[TTC13]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.57 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.56 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[TMED10]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PDIA6]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[RNF4]] | -0.56 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[NDC1]] | -0.56 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[WHAMMP1]] | -0.55 | -0.59 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGEA4]] | B | MAGEA4 activity raises RBMXL1's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.15× lower at baseline in the lines without MAGEA4 | 0.034 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[TOP2A]] | B | TOP2A activity raises RBMXL1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.8, 17.4); signed map (8.7, 24.6). **Vector** length 75.6, 13.3% of its response variance represented; |z| ≥ 3 in 774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.0 | +14.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.3 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.0 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +1.5 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.1 | +1.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RBMX like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:88,979,456-88,992,960 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KAT3 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E39](https://www.uniprot.org/uniprotkb/Q96E39) (RNA binding motif protein, X-linked-like-1):

> RNA-binding protein which may be involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [494115](https://www.ncbi.nlm.nih.gov/gene/494115):

> This gene represents a retrogene of RNA binding motif protein, X-linked (RBMX), which is located on chromosome X. While all introns in the coding sequence have been processed out compared to the RBMX locus, the ORF is intact and there is specific evidence for transcription at this location. The preservation of the ORF by purifying selection in all Old World monkeys carrying it suggests that this locus is likely to be functional, possibly during male meiosis when X chromosomal genes are silenced …

**Accessions** — [HGNC:25073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25073) · Entrez [494115](https://www.ncbi.nlm.nih.gov/gene/494115) · UniProt [Q96E39](https://www.uniprot.org/uniprotkb/Q96E39) · Ensembl [ENSG00000213516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213516)

## Data

Gene col 13109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13109); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13109]; `tensor/DDL_lfc|DDL_z.npy` [13109]; `embed/gene_vectors.npy` [13109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13109 or target_col == 13109). Every well: [[RBMXL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBMXL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
