---
symbol: "STARD7-AS1"
type: "gene"
col: 12914
ensembl_id: "ENSG00000204685"
name: "STARD7 antisense RNA 1"
location: "2q11.2"
module: 15
arm: "+"
pooled_cpm: 9.59
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# STARD7-AS1

*STARD7 antisense RNA 1* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +6.8, q 5e-09, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.406× (z -12.3, q 3e-32, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF785]] (+0.72, fdr 1e-05), [[SPRYD4]] (+0.71, fdr 1e-05), [[DHX35]] (+0.69, fdr 1e-05); moves opposite to [[SPAG9]] (-0.63, fdr 2e-05), [[GDE1]] (-0.63, fdr 3e-05), [[CAST]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TMEM92]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +6.8 | 5e-09 | 24/45 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.5 | 1e-05 | 19/40 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.0 | 1e-04 | 22/45 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 8e-04 | 9/46 (A-172, NCI-H460, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.011 | 9/47 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.5 | 0.050 | 13/48 (HT-29, HS-578T, …) | top dose only | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.072 | 5/47 (SW 900, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.406×** | -12.3 | 3e-32 | 36/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.443×** | -11.1 | 2e-26 | 41/47 (SNU-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.455×** | -10.8 | 7e-25 | 36/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.470×** | -9.9 | 4e-21 | 29/46 (A-427, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.669×** | -7.8 | 9e-13 | 29/47 (PANC-1, A498, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.642×** | -6.1 | 1e-07 | 22/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.654×** | -5.8 | 5e-07 | 20/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.694×** | -5.0 | 4e-05 | 18/44 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.685×** | -5.0 | 4e-05 | 19/39 (NCI-H23, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -4.5 | 3e-04 | 15/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.721×** | -4.5 | 4e-04 | 8/48 (AN3 CA, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.550×** | -4.3 | 9e-04 | 15/48 (PANC-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.582×** | -3.9 | 0.005 | 12/44 (NCI-H23, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.610×** | -3.5 | 0.016 | 9/42 (RKO, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.782×** | -3.3 | 0.031 | 6/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.640×** | -3.2 | 0.048 | 6/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.085 | 10/46 (SW480, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.805×** | -3.0 | 0.085 | 12/46 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Uridine (drug)]] 5 µM |  | **0.807×** | -2.9 | 0.090 | 4/48 (BT-474, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 8.86 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0635× (z -12.7) |
| [[A498 (line)]] | wt | 14.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -13.6) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.293× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 33.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 6.05 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.6) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A-172 (line)]] | wt | 7.63 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0680× (z -12.0) |
| [[BT-474 (line)]] | alt | 5.75 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0833× (z -8.8) ⚠ toxic |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.121× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -8.9) |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0713× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 7.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 9.56 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.176× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 9.03 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.229× (z -9.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[RPMI-7951 (line)]] | alt | 9.19 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0775× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0612× (z -10.5) |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -8.8) |
| [[SW480 (line)]] | alt | 13.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -10.6) |
| [[A549 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF785]] | +0.72 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[SPRYD4]] | +0.71 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[DHX35]] | +0.69 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TMEM267]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[GTF3C2-AS2]] | +0.69 | +0.62 / +0.55 | both halves | 1e-05 | same gene group |
| [[TRAPPC13]] | +0.68 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MTG2]] | +0.67 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ZBTB8A]] | +0.66 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PSKH1]] | +0.65 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[DDX59]] | +0.65 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[GABPB1]] | +0.65 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[PIGC]] | +0.65 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.63 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[GDE1]] | -0.63 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CAST]] | -0.60 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[USP9X]] | -0.59 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[MAPRE2]] | -0.59 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[NBEAL1]] | -0.58 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[SKAP2]] | -0.58 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ATP1A3]] | -0.58 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[ALAS1]] | -0.55 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[ATP7A]] | -0.55 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[KRT19]] | -0.55 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92]] | B | TMEM92 activity lowers STARD7-AS1's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.27× higher at baseline in the lines without TMEM92 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[CCDC88A]] | B | CCDC88A activity raises STARD7-AS1's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.33× lower at baseline in the lines without CCDC88A | 0.084 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[SLC9B2]] | C | SLC9B2 activity raises STARD7-AS1's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.40× lower at baseline in the lines without SLC9B2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.7, 18.6); signed map (28.4, -19.3). **Vector** length 78.5, 14.0% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -12.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -10.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -11.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.8 | -4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | STARD7 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q11.2 — chr2:96,208,389-96,243,353 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40827) · Entrez [285033](https://www.ncbi.nlm.nih.gov/gene/285033) · Ensembl [ENSG00000204685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204685)

## Data

Gene col 12914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12914); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12914]; `tensor/DDL_lfc|DDL_z.npy` [12914]; `embed/gene_vectors.npy` [12914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12914 or target_col == 12914). Every well: [[STARD7-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD7-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
