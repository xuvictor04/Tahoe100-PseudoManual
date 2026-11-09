---
symbol: "PKD2L2-DT"
type: "gene"
col: 14670
ensembl_id: "ENSG00000250159"
name: "PKD2L2 divergent transcript"
location: "5q31.2"
module: 10
arm: "+"
pooled_cpm: 9.49
n_lines_expressing: 29
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PKD2L2-DT

*PKD2L2 divergent transcript* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +15.9, q 0e+00, up in 10 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.406× (z -10.6, q 2e-23, down in 24 of 27 measured lines).
> Its strongest partners by |cos| (58 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 42 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF528]] (+0.63, fdr 1e-04), [[DPY19L2P2]] (+0.62, fdr 8e-04, ⚠ one half only (not replicated)), [[EIF1B-AS1]] (+0.61, fdr 7e-06), [[ZNF793]] (+0.59, fdr 1e-04); moves opposite to [[RALGPS1]] (-0.49, fdr 2e-04), [[GNA12]] (-0.47, fdr 0.004, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLBD1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +15.9 | 0e+00 | 10/26 (SK-MEL-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +12.4 | 6e-33 | 14/26 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +6.7 | 4e-09 | 2/13 (NCI-H2347, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.7 | 5e-04 | 6/27 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +4.5 | 7e-04 | 12/26 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 7e-04 | 8/27 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.001 | 15/26 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 0.001 | 10/26 (A-172, A549, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.44×** | +4.3 | 0.001 | 5/26 (A-427, Panc 03.27, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.004 | 9/27 (MIA PaCa-2, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.006 | 8/26 (SNU-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.008 | 14/26 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.015 | 3/27 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.23×** | +3.5 | 0.018 | 10/26 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.029 | 15/27 (NCI-H23, J82, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.086 | 6/27 (J82, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.406×** | -10.6 | 2e-23 | 24/27 (LOX-IMVI, A-427, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.410×** | -10.5 | 3e-23 | 21/27 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.436×** | -9.8 | 3e-20 | 21/27 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.579×** | -6.2 | 9e-08 | 19/27 (Panc 03.27, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -4.9 | 9e-05 | 15/26 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.672×** | -4.7 | 3e-04 | 18/27 (PANC-1, MIA PaCa-2, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.676×** | -4.6 | 3e-04 | 14/27 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.688×** | -4.4 | 7e-04 | 14/27 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **0.691×** | -4.4 | 8e-04 | 13/20 (A-172, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.709×** | -4.1 | 0.003 | 18/27 (MIA PaCa-2, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.710×** | -4.0 | 0.003 | 10/26 (RPMI-7951, MIA PaCa-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.714×** | -4.0 | 0.003 | 20/25 (Hs 766T, NCI-H23, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.736×** | -3.4 | 0.029 | 15/26 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.747×** | -3.3 | 0.039 | 7/27 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.046 | 10/27 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.830×** | -3.1 | 0.063 | 5/27 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 31.2 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.111× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 37.3 | 0 | 7 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -13.5) |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -13.0) |
| [[A-427 (line)]] | wt | 58.1 | 0 | 6 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0293× (z -17.4) |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.9) |
| [[A549 (line)]] | wt | 6.65 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 18.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.112× (z -12.5) |
| [[C32 (line)]] | wt | 25.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0771× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -8.8) |
| [[H4 (line)]] | wt | 13.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0413× (z -12.5) |
| [[HOP62 (line)]] | alt | 9.93 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0992× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.170× (z -8.5) |
| [[J82 (line)]] | alt | 13.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -8.8) |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0271× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H1792 (line)]] | alt | 21.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 8.54 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0660× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 6.40 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.128× (z -8.8) |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.858 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 41 of them with an alert (⚠; 41 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF528]] | +0.63 | +0.68 / +0.34 | both halves | 1e-04 |  |
| [[DPY19L2P2]] | +0.62 | +0.67 / +0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[EIF1B-AS1]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ZNF793]] | +0.59 | +0.62 / +0.36 | both halves | 1e-04 |  |
| [[DPY19L2]] | +0.58 | +0.66 / +0.31 | both halves | 2e-04 |  |
| [[AGA-DT]] | +0.58 | +0.58 / +0.34 | both halves | 1e-04 | same gene group |
| [[KATNAL2]] | +0.58 | +0.67 / +0.34 | both halves | 1e-04 |  |
| [[LINC00663]] | +0.56 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[SUCLG2-DT]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 | same gene group |
| [[DPY19L2P2-1]] | +0.56 | +0.60 / +0.30 | both halves | 2e-04 |  |
| [[DPH6-DT]] | +0.56 | +0.60 / +0.37 | both halves | 7e-05 | same gene group |
| [[SEPTIN7-DT]] | +0.56 | +0.63 / +0.14 | ⚠ one half (not replicated) | 0.002 | same gene group |
| [[PJVK]] | +0.55 | +0.58 / +0.22 | both halves | 6e-04 |  |
| [[LINC00466]] | +0.55 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGPS1]] | -0.49 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[GNA12]] | -0.47 | -0.57 / -0.06 | ⚠ one half (not replicated) | 0.004 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLBD1-AS1]] | B | PLBD1-AS1 activity raises PKD2L2-DT's level | lines that do not express PLBD1-AS1 (21) vs lines expressing it (29) | 1.74× lower at baseline in the lines without PLBD1-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PLBD1, LINC01357, ANO1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (18.0, 16.9); signed map (32.9, -9.4). **Vector** length 56.2, 11.9% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +15.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.0 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.0 | +3.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.3 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -10.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | PKD2L2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q31.2 — chr5:137,809,780-137,889,394 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55557) · Entrez [101928005](https://www.ncbi.nlm.nih.gov/gene/101928005) · Ensembl [ENSG00000250159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250159)

## Data

Gene col 14670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14670); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14670]; `tensor/DDL_lfc|DDL_z.npy` [14670]; `embed/gene_vectors.npy` [14670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14670 or target_col == 14670). Every well: [[PKD2L2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKD2L2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
