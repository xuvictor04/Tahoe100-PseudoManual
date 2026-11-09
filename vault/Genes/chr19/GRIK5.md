---
symbol: "GRIK5"
type: "gene"
col: 2658
ensembl_id: "ENSG00000105737"
name: "glutamate ionotropic receptor kainate type subunit 5"
location: "19q13.2"
module: 53
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# GRIK5

*glutamate ionotropic receptor kainate type subunit 5* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.8× (z +28.7, q 0e+00, up in 28 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (NCI-H23 0.0733×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FNDC7]] (+0.82, fdr 7e-06), [[PKD1L1]] (+0.80, fdr 7e-06), [[MMP25]] (+0.80, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.8×** | +28.7 | 0e+00 | 28/29 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.51×** | +16.9 | 0e+00 | 30/32 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.48×** | +13.5 | 3e-39 | 23/28 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +10.7 | 2e-24 | 2/2 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.74×** | +10.5 | 1e-23 | 24/37 (A-172, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +9.1 | 5e-18 | 5/11 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.28×** | +9.1 | 9e-18 | 26/39 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +7.7 | 9e-13 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +6.6 | 3e-09 | 6/11 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.0 | 1e-07 | 7/42 (PANC-1, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.02×** | +5.6 | 1e-06 | 15/43 (A498, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +4.9 | 4e-05 | 14/41 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[EX229 (drug)]] 5 µM |  | **3.25×** | +4.9 | 4e-05 | 6/24 (PANC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +4.5 | 3e-04 | 9/43 (HT-29, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +4.4 | 5e-04 | 7/41 (PANC-1, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.003 | 10/40 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.003 | 11/44 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +3.6 | 0.010 | 13/39 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.015 | 4/21 (HCT15, A549, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.2 | 0.037 | 4/18 (C-33 A, HCT15, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2658.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (NCI-H23 0.0733×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.683× | -3.0 | 0.52 | 4/42 (LoVo, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 5.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 1.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.6× (z +16.8) | — |
| [[A-172 (line)]] | wt | 1.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +9.5) | — |
| [[A498 (line)]] | wt | 1.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +8.7) | — |
| [[C32 (line)]] | wt | 2.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.6× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 1.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 4.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 4.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 1.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.7× (z +13.8) | — |
| [[LoVo (line)]] | wt | 3.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.4× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 2.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.7× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 0.708 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.1× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 3.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 4.97 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0733× (z -9.0) |
| [[PANC-1 (line)]] | alt | 2.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +13.3) | — |
| [[SW48 (line)]] | wt | 6.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +8.7) | — |
| [[SW480 (line)]] | alt | 2.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +12.4) | — |
| [[A-427 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.762 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.699 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNDC7]] | +0.82 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.80 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[MMP25]] | +0.80 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[USP50]] | +0.80 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.79 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.79 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[DPYS]] | +0.78 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[LINC02901]] | +0.77 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[UBE2D3-AS1]] | +0.77 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.76 | +0.78 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises GRIK5's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.57× lower at baseline in the lines without ASGR1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises GRIK5's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without LINC00334 | 0.092 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[SH2D4B]] | C | SH2D4B activity lowers GRIK5's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.26× higher at baseline in the lines without SH2D4B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, -13.2); signed map (20.4, 10.8). **Vector** length 65.3, 10.3% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +28.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor kainate type subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,998,321-42,070,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GluK5, KA2; previously GRIK2 |
| Gene groups (HGNC) | Glutamate ionotropic receptor kainate type subunits |
| Reactome | 6 pathways, smallest: Activation of Ca-permeable Kainate Receptor; Ionotropic activity of kainate receptors; Activation of kainate receptors upon glutamate binding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16478](https://www.uniprot.org/uniprotkb/Q16478) (Glutamate receptor ionotropic, kainate 5):

> Ionotropic glutamate receptor that functions as a cation-permeable ligand-gated ion channel, gated by L-glutamate and the glutamatergic agonist kainic acid. Cannot form functional channels on its own and produces channel activity only in heteromeric assembly with GRIK1 and GRIK2 subunits. Can form functional heteromeric receptors with GRIK3 (By similarity).

**Summary**, from NCBI Gene [2901](https://www.ncbi.nlm.nih.gov/gene/2901):

> This gene encodes a protein that belongs to the glutamate-gated ionic channel family. Glutamate functions as the major excitatory neurotransmitter in the central nervous system through activation of ligand-gated ion channels and G protein-coupled membrane receptors. The protein encoded by this gene forms functional heteromeric kainate-preferring ionic channels with the subunits encoded by related gene family members. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:4583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4583) · Entrez [2901](https://www.ncbi.nlm.nih.gov/gene/2901) · UniProt [Q16478](https://www.uniprot.org/uniprotkb/Q16478) · Ensembl [ENSG00000105737](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105737)

## Data

Gene col 2658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2658); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2658]; `tensor/DDL_lfc|DDL_z.npy` [2658]; `embed/gene_vectors.npy` [2658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2658 or target_col == 2658). Every well: [[GRIK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
