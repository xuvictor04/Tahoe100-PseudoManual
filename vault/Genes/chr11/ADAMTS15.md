---
symbol: "ADAMTS15"
type: "gene"
col: 9236
ensembl_id: "ENSG00000166106"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 15"
location: "11q24.3"
module: 196
arm: "+"
pooled_cpm: 2.52
n_lines_expressing: 32
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# ADAMTS15

*ADAM metallopeptidase with thrombospondin type 1 motif 15* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 5.25× (z +12.3, q 3e-32, up in 19 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.502× (z -5.2, q 1e-04, down in 10 of 24 measured lines).
> Its strongest partners by |cos| (74 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP3C]] (+0.52, fdr 1e-04), [[SEMA3F]] (+0.52, fdr 7e-05), [[TLE3]] (+0.50, fdr 6e-05); moves opposite to [[CLCC1]] (-0.46, fdr 2e-04), [[RNF14]] (-0.45, fdr 2e-04), [[LINC02641]] (-0.42, fdr 4e-04).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AFF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **5.25×** | +12.3 | 3e-32 | 19/24 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.63×** | +11.4 | 1e-27 | 17/26 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.43×** | +10.2 | 3e-22 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.32×** | +8.9 | 6e-17 | 17/25 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.16×** | +8.1 | 6e-14 | 8/23 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +7.9 | 2e-13 | 8/20 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.72×** | +7.4 | 8e-12 | 15/25 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.63×** | +7.2 | 5e-11 | 0/12 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +5.9 | 3e-07 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +5.2 | 1e-05 | 2/11 (HEC-1-A, SW480) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.1 | 1e-05 | 3/20 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.82×** | +4.4 | 4e-04 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +4.3 | 6e-04 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.69×** | +3.8 | 0.005 | 4/23 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +3.6 | 0.011 | 6/16 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.017 | 2/21 (HEC-1-A, SW480) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +3.1 | 0.054 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.502×** | -5.2 | 1e-04 | 10/24 (SHP-77, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.606×** | -3.8 | 0.049 | 7/25 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.714×** | -3.6 | 0.062 | 8/26 (SHP-77, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.631×** | -3.5 | 0.077 | 8/21 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.641×** | -3.3 | 0.078 | 5/23 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.535×** | -3.3 | 0.078 | 3/24 (PANC-1, NCI-H661, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **0.646×** | -3.3 | 0.083 | 7/24 (RPMI-7951, A549, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.448× | -3.1 | 0.12 | 6/20 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0850× (z -11.2) |
| [[PANC-1 (line)]] | alt | 7.34 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -10.2) |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0963× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 1.58 | 0 | 1 | — | [[Radotinib (drug)]] 5 µM 0.0755× (z -9.0) |
| [[Hs 766T (line)]] | wt | 4.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -8.9) |
| [[J82 (line)]] | alt | 6.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0937× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H1792 (line)]] | alt | 3.82 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0350× (z -9.8) |
| [[SW480 (line)]] | alt | 3.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.762 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.632 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.222 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.700 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.918 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.738 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.361 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.643 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP3C]] | +0.52 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[SEMA3F]] | +0.52 | +0.51 / +0.37 | both halves | 7e-05 |  |
| [[TLE3]] | +0.50 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[ANKRD20A4P]] | +0.49 | +0.36 / +0.35 | both halves | 1e-04 |  |
| [[LMCD1]] | +0.48 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[NR4A1]] | +0.47 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[MAN1C1]] | +0.46 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[DGKD]] | +0.44 | +0.26 / +0.34 | both halves | 4e-04 |  |
| [[SAPCD1]] | +0.43 | +0.25 / +0.34 | both halves | 4e-04 |  |
| [[DOC2B]] | +0.43 | +0.40 / +0.32 | both halves | 1e-04 |  |
| [[ANKRD20A1]] | +0.43 | +0.36 / +0.22 | both halves | 6e-04 |  |
| [[ADSS1]] | +0.42 | +0.31 / +0.38 | both halves | 2e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCC1]] | -0.46 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[RNF14]] | -0.45 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[LINC02641]] | -0.42 | -0.32 / -0.26 | both halves | 4e-04 |  |
| [[TCAIM]] | -0.42 | -0.30 / -0.26 | both halves | 4e-04 |  |
| [[URM1]] | -0.42 | -0.27 / -0.31 | both halves | 3e-04 |  |
| [[SMARCAL1]] | -0.41 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[PTPDC1]] | -0.41 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[YARS2]] | -0.40 | -0.11 / -0.23 | ⚠ not reproduced | 0.002 |  |
| [[PLPBP]] | -0.40 | -0.14 / -0.24 | ⚠ not reproduced | 0.002 |  |
| [[METTL6]] | -0.40 | -0.09 / -0.37 | ⚠ not reproduced | 0.003 |  |
| [[FAM149B1]] | -0.40 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[PTPN9]] | -0.39 | -0.22 / -0.32 | both halves | 6e-04 |  |
| [[SLC35E3]] | -0.38 | -0.25 / -0.27 | both halves | 4e-04 |  |
| [[LVRN]] | -0.38 | -0.24 / -0.34 | both halves | 4e-04 |  |
| [[RMDN1]] | -0.37 | -0.28 / -0.33 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFF2]] | B | AFF2 activity raises ADAMTS15's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without AFF2 | 0.053 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.7, 32.3); signed map (-15.0, 34.6). **Vector** length 50.9, 10.3% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +11.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.9 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:130,448,645-130,476,645 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE58](https://www.uniprot.org/uniprotkb/Q8TE58) (A disintegrin and metalloproteinase with thrombospondin motifs 15):

> Metalloprotease which has proteolytic activity against the proteoglycan VCAN, cleaving it at the 'Glu-1428-|-1429-Ala' site. Cleaves VCAN in the pericellular matrix surrounding myoblasts, facilitating myoblast contact and fusion which is required for skeletal muscle development and regeneration.

**Summary**, from NCBI Gene [170689](https://www.ncbi.nlm.nih.gov/gene/170689):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. ADAMTS family members share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The encoded preproprotein is proteolytically processed to generate …

**Accessions** — [HGNC:16305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16305) · Entrez [170689](https://www.ncbi.nlm.nih.gov/gene/170689) · UniProt [Q8TE58](https://www.uniprot.org/uniprotkb/Q8TE58) · Ensembl [ENSG00000166106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166106)

## Data

Gene col 9236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9236); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9236]; `tensor/DDL_lfc|DDL_z.npy` [9236]; `embed/gene_vectors.npy` [9236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9236 or target_col == 9236). Every well: [[ADAMTS15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
