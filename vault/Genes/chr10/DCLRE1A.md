---
symbol: "DCLRE1A"
type: "gene"
col: 12740
ensembl_id: "ENSG00000198924"
name: "DNA cross-link repair 1A"
location: "10q25.3"
module: 16
arm: "+"
pooled_cpm: 6.32
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# DCLRE1A

*DNA cross-link repair 1A* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +9.0, q 1e-16, up in 31 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.445× (z -8.0, q 4e-13, down in 30 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.446× (z -8.0, q 4e-13, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIF1]] (+0.78, fdr 7e-06), [[ZNF678]] (+0.76, fdr 7e-06), [[ZNF681]] (+0.75, fdr 7e-06); moves opposite to [[CBFA2T2]] (-0.71, fdr 7e-06), [[RPLP2]] (-0.71, fdr 7e-06), [[TPT1]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02649]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +9.0 | 1e-16 | 31/38 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +8.1 | 2e-13 | 30/43 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +6.8 | 3e-09 | 9/11 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +6.3 | 4e-08 | 24/38 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +5.4 | 1e-05 | 25/45 (HT-29, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.77×** | +5.3 | 1e-05 | 20/39 (C32, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +4.9 | 8e-05 | 17/43 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +4.7 | 2e-04 | 17/46 (PANC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.2 | 0.001 | 5/15 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.008 | 8/45 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | 1.35× | +3.0 | 0.14 | 8/26 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -8.0 | 4e-13 | 30/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.446×** | -8.0 | 4e-13 | 32/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.498×** | -6.9 | 1e-09 | 27/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.531×** | -6.2 | 6e-08 | 28/44 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.596×** | -5.1 | 4e-05 | 21/43 (NCI-H23, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.644×** | -4.3 | 0.001 | 15/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.775×** | -3.5 | 0.034 | 16/43 (PANC-1, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -3.4 | 0.040 | 13/39 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.710×** | -3.4 | 0.048 | 15/43 (SNU-423, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.65 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -10.3) |
| [[LS 180 (line)]] | wt | 5.64 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0552× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 9.12 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0950× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 7.36 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -10.3) |
| [[SW480 (line)]] | alt | 9.02 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -9.3) |
| [[A-427 (line)]] | wt | 12.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -10.2) |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0992× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 6.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0662× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 5.69 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0960× (z -8.9) |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -10.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 6.57 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.115× (z -8.5) |
| [[A-172 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIF1]] | +0.78 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[ZNF678]] | +0.76 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[ZNF681]] | +0.75 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[DDX20]] | +0.74 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[CEP41]] | +0.74 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[FAM111A]] | +0.70 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[ZNF724]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[ZNF816]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[C9orf64]] | +0.70 | +0.79 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.71 | -0.79 / -0.61 | both halves | 7e-06 |  |
| [[RPLP2]] | -0.71 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[TPT1]] | -0.70 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[RPL28]] | -0.68 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[RPS21]] | -0.68 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.68 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[CD81]] | -0.67 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | -0.67 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[RPS11]] | -0.67 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.67 | -0.73 / -0.51 | both halves | 1e-05 |  |
| [[UBL5]] | -0.67 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[RPS29]] | -0.67 | -0.66 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02649]] | C | LINC02649 activity lowers DCLRE1A's level | lines that do not express LINC02649 (3) vs lines expressing it (47) | 1.80× higher at baseline in the lines without LINC02649 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAP3K8, LINC02656, B4GALT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.759). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.4, 13.0); signed map (4.2, -35.2). **Vector** length 83.8, 16.0% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +5.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | DNA cross-link repair 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:113,834,725-113,854,383 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNM1, PSO2, KIAA0086, hSNM1 |
| Gene groups (HGNC) | DNA cross-link repair family; Zinc fingers UBZ4 CCHC-type |
| Reactome | 2 pathways, smallest: Fanconi Anemia Pathway; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PJP8](https://www.uniprot.org/uniprotkb/Q6PJP8) (DNA cross-link repair 1A protein):

> May be required for DNA interstrand cross-link repair. Also required for checkpoint mediated cell cycle arrest in early prophase in response to mitotic spindle poisons. Possesses beta-lactamase activity, catalyzing the hydrolysis of penicillin G and nitrocefin. Exhibits no activity towards other beta-lactam antibiotic classes including cephalosporins (cefotaxime) and carbapenems (imipenem).

**Summary**, from NCBI Gene [9937](https://www.ncbi.nlm.nih.gov/gene/9937):

> This gene encodes a conserved protein that is involved in the repair of DNA interstrand cross-links. DNA cross-links suppress transcription, replication, and DNA segregation. The encoded protein is a regulator of the mitotic cell cycle checkpoint. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:17660](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17660) · Entrez [9937](https://www.ncbi.nlm.nih.gov/gene/9937) · UniProt [Q6PJP8](https://www.uniprot.org/uniprotkb/Q6PJP8) · Ensembl [ENSG00000198924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198924)

## Data

Gene col 12740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12740); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12740]; `tensor/DDL_lfc|DDL_z.npy` [12740]; `embed/gene_vectors.npy` [12740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12740 or target_col == 12740). Every well: [[DCLRE1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCLRE1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
