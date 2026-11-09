---
symbol: "TMEM141"
type: "gene"
col: 14394
ensembl_id: "ENSG00000244187"
name: "transmembrane protein 141"
location: "9q34.3"
module: 58
arm: "+"
pooled_cpm: 11.42
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# TMEM141

*transmembrane protein 141* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.42× (z +7.9, q 1e-12, up in 29 of 31 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 6.68×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.414× (z -8.6, q 7e-15, down in 32 of 39 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCRN2]] (+0.71, fdr 1e-05), [[NDUFAF3]] (+0.70, fdr 1e-05), [[ANTKMT]] (+0.64, fdr 2e-05); moves opposite to [[KLRA1P]] (-0.56, fdr 9e-05), [[POU6F1]] (-0.52, fdr 2e-04), [[PPP1R3F]] (-0.51, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PCK1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Fluvoxamine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14394.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 6.68×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.42×** | +7.9 | 1e-12 | 29/31 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.20×** | +7.7 | 5e-12 | 14/17 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +6.0 | 4e-07 | 18/23 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +4.3 | 0.002 | 20/47 (HOP62, KATO III, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.83×** | +4.1 | 0.004 | 22/36 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.61× | +3.3 | 0.11 | 15/44 (SW480, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.414×** | -8.6 | 7e-15 | 32/39 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.303×** | -8.2 | 9e-14 | 34/38 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.389×** | -6.5 | 2e-08 | 34/43 (COLO 205, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.394×** | -6.4 | 2e-08 | 36/46 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.422×** | -5.9 | 4e-07 | 29/44 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.464×** | -5.0 | 6e-05 | 29/43 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.487×** | -4.9 | 7e-05 | 29/43 (LoVo, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -4.0 | 0.005 | 24/39 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -3.8 | 0.010 | 20/39 (BT-474, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.584×** | -3.7 | 0.013 | 22/45 (LS 180, A549, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.363× | -3.1 | 0.11 | 23/40 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 40.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0645× (z -12.5) |
| [[LoVo (line)]] | wt | 20.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -10.4) |
| [[HT-29 (line)]] | alt | 36.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -11.2) |
| [[SHP-77 (line)]] | alt | 6.30 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -9.8) |
| [[A549 (line)]] | wt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.68× (z +9.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 36.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -10.6) |
| [[LS 180 (line)]] | wt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 5.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 5.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -9.1) |
| [[PANC-1 (line)]] | alt | 19.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 5.96 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0491× (z -9.5) |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -10.0) |
| [[SW480 (line)]] | alt | 5.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -8.9) |
| [[A-172 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCRN2]] | +0.71 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[NDUFAF3]] | +0.70 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[ANTKMT]] | +0.64 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A11]] | +0.61 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[NDUFB3]] | +0.58 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[TMEM160]] | +0.58 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[MRPL40]] | +0.58 | +0.27 / +0.63 | both halves | 3e-04 |  |
| [[ROGDI]] | +0.56 | +0.39 / +0.43 | both halves | 6e-05 |  |
| [[RAB25]] | +0.56 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[NDUFA3]] | +0.56 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[TMEM256]] | +0.55 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[TRAPPC5]] | +0.54 | +0.34 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRA1P]] | -0.56 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[POU6F1]] | -0.52 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[PPP1R3F]] | -0.51 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[GLIPR1-AS1]] | -0.51 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[LINC01355]] | -0.51 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[EOGT]] | -0.51 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[BORCS7-ASMT]] | -0.51 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[PSMD6-AS1]] | -0.49 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[ANXA2R-OT1]] | -0.49 | -0.30 / -0.28 | both halves | 3e-04 |  |
| [[YJEFN3]] | -0.49 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[CASS4]] | -0.48 | -0.36 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[KCTD15]] | -0.48 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[ZNF460-AS1]] | -0.47 | -0.20 / -0.27 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCK1]] | B | PCK1 activity strengthens TMEM141's drug response | lines that do not express PCK1 (36) vs lines expressing it (10) | the lines without PCK1 respond 0.63× as strongly (z diff +1.61); strongest at Homoharringtonine 5 µM: 0.43x vs 0.23x (z diff +4.2) | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; target measured in part of the lines; artifact flags |
| [[TMEM92]] | B | TMEM92 activity raises TMEM141's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.67× lower at baseline in the lines without TMEM92 | 0.054 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[RAB25]] | B | RAB25 activity raises TMEM141's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.01× lower at baseline in the lines without RAB25 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | TMEM141's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | TMEM141's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.452 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.4, -12.0); signed map (-21.8, -4.6). **Vector** length 68.7, 16.0% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex I biogenesis* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.7 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.9 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 141 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,791,344-136,793,317 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14141 |
| Matched by | ensembl_id |

UniProt [Q96I45](https://www.uniprot.org/uniprotkb/Q96I45) carries no function annotation.

**Summary**, from NCBI Gene [85014](https://www.ncbi.nlm.nih.gov/gene/85014):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28211) · Entrez [85014](https://www.ncbi.nlm.nih.gov/gene/85014) · UniProt [Q96I45](https://www.uniprot.org/uniprotkb/Q96I45) · Ensembl [ENSG00000244187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244187)

## Data

Gene col 14394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14394); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14394]; `tensor/DDL_lfc|DDL_z.npy` [14394]; `embed/gene_vectors.npy` [14394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14394 or target_col == 14394). Every well: [[TMEM141 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM141.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
