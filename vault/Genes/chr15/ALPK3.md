---
symbol: "ALPK3"
type: "gene"
col: 5860
ensembl_id: "ENSG00000136383"
name: "alpha kinase 3"
location: "15q25.3"
module: 47
arm: "+"
pooled_cpm: 20.35
n_lines_expressing: 45
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# ALPK3

*alpha kinase 3* — 15q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +6.8, q 7e-09, up in 16 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.52×, NCI-H23 5.05×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 6.24×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.519× (z -7.5, q 3e-11, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PILRA]] (+0.77, fdr 7e-06), [[LINC02133]] (+0.75, fdr 7e-06), [[PITRM1-AS1]] (+0.75, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SCUBE2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5860.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.52×, NCI-H23 5.05×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 6.24×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +6.8 | 7e-09 | 16/40 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.0 | 1e-04 | 4/23 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +4.8 | 3e-04 | 8/25 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.49×** | +4.6 | 6e-04 | 14/43 (LoVo, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.5 | 7e-04 | 6/43 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.5 | 7e-04 | 8/30 (LoVo, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5860.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -7.5 | 3e-11 | 28/42 (H4, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.552×** | -6.8 | 3e-09 | 25/42 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.605×** | -5.8 | 2e-06 | 26/38 (J82, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.652×** | -4.9 | 1e-04 | 24/41 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.462×** | -4.6 | 4e-04 | 17/36 (LS 180, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.673×** | -4.5 | 6e-04 | 19/41 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -4.3 | 0.001 | 19/35 (NCI-H2030, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.770×** | -4.2 | 0.002 | 17/43 (RKO, LOX-IMVI, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.704×** | -3.8 | 0.009 | 14/39 (SNU-423, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.718×** | -3.8 | 0.009 | 16/42 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.719×** | -3.8 | 0.009 | 19/43 (H4, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.726×** | -3.6 | 0.015 | 19/41 (A549, A498, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.740×** | -3.4 | 0.025 | 6/42 (LoVo, HT-29, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.592×** | -3.1 | 0.068 | 9/37 (NCI-H460, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.593×** | -3.1 | 0.068 | 8/42 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -11.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 60.5 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -12.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[H4 (line)]] | wt | 15.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0441× (z -12.4) |
| [[HT-29 (line)]] | alt | 166 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -16.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0722× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 97.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -11.1) |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 2 (2 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.128× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 11.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0547× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 15.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 29.9 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -13.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 5.18 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0610× (z -10.0) |
| [[A549 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0942× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0900× (z -8.6) |
| [[KATO III (line)]] | alt | 7.61 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0768× (z -10.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H23 (line)]] | alt | 8.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -8.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.97 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRA]] | +0.77 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[LINC02133]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[OIT3]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.75 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[C19orf38]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[SH2D4B]] | +0.74 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[TMEM25]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCUBE2]] | B | SCUBE2 activity lowers ALPK3's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 2.56× higher at baseline in the lines without SCUBE2 | 0.019 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[FBXW10B]] | B | FBXW10B activity raises ALPK3's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without FBXW10B | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[SRMS]] | B | SRMS activity raises ALPK3's level | lines that do not express SRMS (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without SRMS | 0.097 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[MMP25]] | C | MMP25 activity lowers ALPK3's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 3.53× higher at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent; its own permutation p |
| [[MPP4]] | C | MPP4 activity lowers ALPK3's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 3.36× higher at baseline in the lines without MPP4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, -14.2); signed map (18.3, 10.9). **Vector** length 88.5, 17.6% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.6 | -6.8 |
|  | [[NG25 (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.4 | -4.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -3.1 | -5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.9 | -3.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | alpha kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.3 — chr15:84,817,356-84,873,479 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAK, KIAA1330, Midori |
| Gene groups (HGNC) | I-set domain containing; Alpha kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96L96](https://www.uniprot.org/uniprotkb/Q96L96) (Alpha-protein kinase 3):

> Involved in cardiomyocyte differentiation.

**Summary**, from NCBI Gene [57538](https://www.ncbi.nlm.nih.gov/gene/57538):

> Predicted to enable ATP binding activity; protein serine kinase activity; and protein serine/threonine kinase activity. Predicted to be involved in cardiac muscle cell development. Predicted to be active in nucleus. Implicated in hypertrophic cardiomyopathy 27. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17574) · Entrez [57538](https://www.ncbi.nlm.nih.gov/gene/57538) · UniProt [Q96L96](https://www.uniprot.org/uniprotkb/Q96L96) · Ensembl [ENSG00000136383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136383)

## Data

Gene col 5860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5860); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5860]; `tensor/DDL_lfc|DDL_z.npy` [5860]; `embed/gene_vectors.npy` [5860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5860 or target_col == 5860). Every well: [[ALPK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALPK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
