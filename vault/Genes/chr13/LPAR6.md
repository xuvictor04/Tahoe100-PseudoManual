---
symbol: "LPAR6"
type: "gene"
col: 6333
ensembl_id: "ENSG00000139679"
name: "lysophosphatidic acid receptor 6"
location: "13q14.2"
module: 80
arm: "+"
pooled_cpm: 5.39
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# LPAR6

*lysophosphatidic acid receptor 6* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.11× (z +12.7, q 3e-34, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.864× (z -6.4, q 7e-08, down in 22 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Budesonide (drug)]] 5 µM: 0.736× (z -3.7, q 0.062, down in 12 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Celecoxib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0620×); [[Panobinostat (drug)]] 5 µM in 1 line (C32 0.163×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lopinavir (drug)]] 5 µM in 1 line (NCI-H2030 0.0642×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0919×).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LPXN]] (+0.62, fdr 8e-05), [[ANGPT2]] (+0.59, fdr 5e-05), [[EYS]] (+0.59, fdr 8e-05); moves opposite to [[TBC1D24]] (-0.56, fdr 3e-04), [[CAMSAP1]] (-0.55, fdr 1e-04), [[STX2]] (-0.55, fdr 6e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPHA4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +12.7 | 3e-34 | 27/38 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.05×** | +12.2 | 7e-32 | 23/37 (HOP62, LOX-IMVI, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.56×** | +11.3 | 2e-27 | 26/36 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +9.6 | 8e-20 | 20/26 (NCI-H1573, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +8.6 | 6e-16 | 6/11 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +8.3 | 1e-14 | 5/16 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +7.2 | 6e-11 | 18/29 (Hs 766T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 3e-05 | 17/45 (NCI-H1573, SW 900, …) | two highest doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.9 | 5e-05 | 15/43 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.45×** | +4.5 | 5e-04 | 7/21 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.4 | 5e-04 | 8/35 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.41×** | +4.1 | 0.002 | 6/35 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.003 | 11/37 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.008 | 7/44 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.6 | 0.014 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.026 | 1/43 (HT-29) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.074 | 2/42 (NCI-H2347, C32) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6333.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Celecoxib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0620×); [[Panobinostat (drug)]] 5 µM in 1 line (C32 0.163×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lopinavir (drug)]] 5 µM in 1 line (NCI-H2030 0.0642×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0919×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.864× | -6.4 | 7e-08 | 22/48 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.736×** | -3.7 | 0.062 | 12/46 (J82, SW 900, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.821× | -3.3 | 0.20 | 8/45 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.776× | -3.1 | 0.32 | 8/46 (KATO III, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 3.98 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +14.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 21.7× (z +11.4) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0919× (z -8.8) |
| [[HOP62 (line)]] | alt | 3.65 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +16.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 17.0× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 5.40 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +10.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Celecoxib (drug)]] 0.05 µM 0.0620× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 7.53 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 15.7× (z +9.1) | — |
| [[SW480 (line)]] | alt | 9.66 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 13.7× (z +11.1) | — |
| [[A-172 (line)]] | wt | 5.29 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 4.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.5× (z +14.3) | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 4.66 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 3.06 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.1× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 2.57 | 0 | 1 | — | [[Lopinavir (drug)]] 5 µM 0.0642× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 4.30 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 13.1× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -8.7) |
| [[SW 900 (line)]] | alt | 3.59 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 21.4× (z +8.5) | — |
| [[SW48 (line)]] | wt | 5.08 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.2× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPXN]] | +0.62 | +0.58 / +0.37 | both halves | 8e-05 |  |
| [[ANGPT2]] | +0.59 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[EYS]] | +0.59 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[DPY19L2P2]] | +0.58 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[NEK8]] | +0.58 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[GRM8]] | +0.57 | +0.45 / +0.37 | both halves | 8e-05 | pathway: GPCR ligand binding |
| [[HAS2-AS1]] | +0.57 | +0.40 / +0.36 | both halves | 1e-04 |  |
| [[ZNF341-AS1]] | +0.57 | +0.47 / +0.32 | both halves | 2e-04 |  |
| [[ZSWIM5]] | +0.57 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[CD96]] | +0.57 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[DKK2]] | +0.56 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[BFSP1]] | +0.56 | +0.47 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D24]] | -0.56 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[CAMSAP1]] | -0.55 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[STX2]] | -0.55 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[ANKRD27]] | -0.54 | -0.53 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[STK25]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[WDR5]] | -0.53 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[DIP2A]] | -0.53 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[FANCE]] | -0.53 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[CRAT]] | -0.52 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[CDC42BPB]] | -0.51 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[ZDHHC8]] | -0.51 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[GTPBP3]] | -0.51 | -0.44 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[INPP4A]] | -0.51 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[KIF1C]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA4]] | B | EPHA4 activity strengthens LPAR6's drug response | lines that do not express EPHA4 (19) vs lines expressing it (29) | the lines without EPHA4 respond 0.41× as strongly (z diff +1.61); strongest at Homoharringtonine 5 µM: 1.11x vs 3.60x (z diff +5.2) | 0.081 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 16.7); signed map (27.1, 3.2). **Vector** length 53.3, 6.65% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.6 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +12.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.8 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidic acid receptor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:48,389,567-48,444,704 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P2Y5; previously P2RY5 |
| Gene groups (HGNC) | Lysophosphatidic acid receptors |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 7 pathways, smallest: P2Y receptors; Nucleotide-like (purinergic) receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P43657](https://www.uniprot.org/uniprotkb/P43657) (Lysophosphatidic acid receptor 6):

> Binds to oleoyl-L-alpha-lysophosphatidic acid (LPA). Intracellular cAMP is involved in the receptor activation. Important for the maintenance of hair growth and texture.

**Summary**, from NCBI Gene [10161](https://www.ncbi.nlm.nih.gov/gene/10161):

> The protein encoded by this gene belongs to the family of G-protein coupled receptors, that are preferentially activated by adenosine and uridine nucleotides. This gene aligns with an internal intron of the retinoblastoma susceptibility gene in the reverse orientation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2009]

**Accessions** — [HGNC:15520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15520) · Entrez [10161](https://www.ncbi.nlm.nih.gov/gene/10161) · UniProt [P43657](https://www.uniprot.org/uniprotkb/P43657) · Ensembl [ENSG00000139679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139679)

## Data

Gene col 6333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6333); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6333]; `tensor/DDL_lfc|DDL_z.npy` [6333]; `embed/gene_vectors.npy` [6333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6333 or target_col == 6333). Every well: [[LPAR6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPAR6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
