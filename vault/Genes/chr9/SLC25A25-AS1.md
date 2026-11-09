---
symbol: "SLC25A25-AS1"
type: "gene"
col: 13983
ensembl_id: "ENSG00000234771"
name: "SLC25A25 antisense RNA 1"
location: "9q34.11"
module: 27
arm: "+"
pooled_cpm: 5.12
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SLC25A25-AS1

*SLC25A25 antisense RNA 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.41× (z +9.1, q 3e-17, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 1.39× (z +3.6, q 0.044, up in 4 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 3 lines (LS 180 6.47×, KATO III 3.30×, HT-29 3.17×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.648× (z -5.0, q 3e-04, down in 15 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.672× (z -4.6, q 9e-04, down in 13 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNE3]] (+0.57, fdr 1e-05), [[BCAR3-AS1]] (+0.56, fdr 3e-05), [[STEAP2-AS1]] (+0.56, fdr 2e-05); moves opposite to [[LGALS1]] (-0.45, fdr 3e-04), [[KATNAL1]] (-0.45, fdr 1e-04), [[CDKL5]] (-0.45, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOX3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13983.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 3 lines (LS 180 6.47×, KATO III 3.30×, HT-29 3.17×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +9.1 | 3e-17 | 1/7 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +8.9 | 1e-16 | 4/10 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.3 | 3e-14 | 11/22 (LS 180, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +3.6 | 0.044 | 4/44 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.21× | +3.1 | 0.19 | 7/46 (KATO III, HT-29, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.35× | +3.1 | 0.19 | 5/24 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.35× | +3.0 | 0.20 | 5/46 (A549, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.648×** | -5.0 | 3e-04 | 15/47 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.655×** | -4.9 | 3e-04 | 15/34 (LoVo, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -4.6 | 9e-04 | 13/45 (RKO, SW480, …) | two highest doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.689×** | -3.9 | 0.015 | 12/44 (COLO 205, RKO, …) | two highest doses | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.723×** | -3.7 | 0.020 | 12/44 (SW480, SNU-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.727×** | -3.7 | 0.020 | 5/47 (Hs 766T, SHP-77, …) | two highest doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.697×** | -3.7 | 0.020 | 8/45 (SNU-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Sinomenine (drug)]] 0.5 µM |  | **0.736×** | -3.5 | 0.029 | 9/44 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.742×** | -3.4 | 0.037 | 11/44 (J82, COLO 205, …) | all doses, stronger at high dose |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.090 | 7/43 (SW480, A498, …) | top dose only | position effect removed |
| [[Bexarotene (drug)]] 5 µM |  | **0.764×** | -3.1 | 0.097 | 5/47 (SW 1271, NCI-H460, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.747× | -3.0 | 0.12 | 4/45 (CFPAC-1, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 52.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -14.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 3.49 | 0 | 2 (2 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0615× (z -9.2) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.17× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.30× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 8.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 5.94 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 6.47× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 6.96 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNE3]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[BCAR3-AS1]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 | same gene group |
| [[STEAP2-AS1]] | +0.56 | +0.62 / +0.47 | both halves | 2e-05 | same gene group |
| [[SPTBN2]] | +0.56 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[FGD3]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[FAAH]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[TMEM184A]] | +0.54 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[BCL2L15]] | +0.54 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SPATA6L]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[B3GAT1-DT]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[PSD4]] | +0.54 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[SP2-AS1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS1]] | -0.45 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[KATNAL1]] | -0.45 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[CDKL5]] | -0.45 | -0.32 / -0.39 | both halves | 1e-04 |  |
| [[WDR44]] | -0.44 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[WDR54]] | -0.43 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[PRKRA]] | -0.43 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOX3]] | B | TOX3 activity raises SLC25A25-AS1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without TOX3 | 0.010 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[PROM1]] | B | PROM1 activity raises SLC25A25-AS1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.15× lower at baseline in the lines without PROM1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[ARHGEF38]] | B | ARHGEF38 activity raises SLC25A25-AS1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 2.12× lower at baseline in the lines without ARHGEF38 | 0.014 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises SLC25A25-AS1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without HNF1A-AS1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[MUC5B]] | B | MUC5B activity raises SLC25A25-AS1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.64× lower at baseline in the lines without MUC5B | 0.067 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[LINC02331]] | B | LINC02331 activity raises SLC25A25-AS1's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 1.98× lower at baseline in the lines without LINC02331 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 46.9); signed map (67.6, -0.4). **Vector** length 52.7, 6.62% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | -2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.2 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -3.7 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -1.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Cloxacillin (sodium) (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SLC25A25 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q34.11 — chr9:128,108,581-128,118,693 (-) |
| Ensembl biotype | lncRNA |
| Also known as | HRCEG |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27844) · Entrez [100289019](https://www.ncbi.nlm.nih.gov/gene/100289019) · Ensembl [ENSG00000234771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234771)

## Data

Gene col 13983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13983); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13983]; `tensor/DDL_lfc|DDL_z.npy` [13983]; `embed/gene_vectors.npy` [13983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13983 or target_col == 13983). Every well: [[SLC25A25-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC25A25-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
