---
symbol: "CARD19"
type: "gene"
col: 9090
ensembl_id: "ENSG00000165233"
name: "caspase recruitment domain family member 19"
location: "9q22.31"
module: 3
arm: "+"
pooled_cpm: 21.45
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CARD19

*caspase recruitment domain family member 19* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.82× (z +6.2, q 3e-07, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.359× (z -5.6, q 2e-05, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAPC2]] (+0.75, fdr 7e-06), [[MGST3]] (+0.74, fdr 7e-06), [[MPST]] (+0.74, fdr 7e-06); moves opposite to [[ZNF507]] (-0.71, fdr 7e-06), [[ZMYND11]] (-0.70, fdr 1e-05), [[UTP20]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NDRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +6.2 | 3e-07 | 33/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +4.8 | 3e-04 | 26/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +4.8 | 3e-04 | 28/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +4.1 | 0.007 | 22/46 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.36× | +3.2 | 0.15 | 17/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.77× | +3.1 | 0.17 | 13/35 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | 1.36× | +3.1 | 0.17 | 19/43 (LoVo, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.359×** | -5.6 | 2e-05 | 34/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.691×** | -5.4 | 2e-05 | 27/45 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.605×** | -5.2 | 4e-05 | 26/44 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.613×** | -4.9 | 1e-04 | 24/47 (HS-578T, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.675×** | -3.8 | 0.017 | 24/47 (SW 900, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.502×** | -3.7 | 0.017 | 20/45 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -3.6 | 0.024 | 22/48 (AsPC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.696×** | -3.5 | 0.034 | 22/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -3.4 | 0.036 | 23/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.725×** | -3.3 | 0.051 | 17/48 (SNU-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.802×** | -3.2 | 0.065 | 18/48 (NCI-H23, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -3.1 | 0.089 | 21/41 (SW 900, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 77.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0874× (z -20.5) |
| [[NCI-H23 (line)]] | alt | 9.29 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -12.2) |
| [[A-172 (line)]] | wt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.4) |
| [[A498 (line)]] | wt | 45.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 38.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.4) |
| [[J82 (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.2) |
| [[KATO III (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 16.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.9) ⚠ cell-cycle shift, explains ~8% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0354× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 16.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.2) ⚠ cell-cycle shift, explains ~8% of this change | — |
| [[RKO (line)]] | wt | 14.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +8.9) ⚠ cell-cycle shift, explains ~8% of this change | — |
| [[A-427 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC2]] | +0.75 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[MGST3]] | +0.74 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[MPST]] | +0.74 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[FAM89B]] | +0.72 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.72 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[MPG]] | +0.72 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[RRAS]] | +0.71 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MACO1]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CARHSP1]] | +0.71 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[PLA2G15]] | +0.71 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[STK32C]] | +0.71 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.71 | +0.49 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF507]] | -0.71 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[ZMYND11]] | -0.70 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[UTP20]] | -0.69 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[TRIM44]] | -0.68 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.67 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[MRRF]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[MED12]] | -0.66 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.65 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[MTHFSD]] | -0.65 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.65 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.65 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[RGS5]] | -0.65 | -0.63 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | NDRG1 activity raises CARD19's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without NDRG1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[HDAC6]] | B | HDAC6 activity lowers CARD19's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[THBS1]] | B | THBS1 activity raises CARD19's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 1.37× lower at baseline in the lines without THBS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.0, -1.5); signed map (-29.5, 17.1). **Vector** length 108, 29.2% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.5 | +6.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.7 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +4.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.2 | -0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.7 | -0.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | caspase recruitment domain family member 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:93,096,217-93,113,283 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11115, bA370F5.1, BinCARD; previously C9orf89 |
| Gene groups (HGNC) | Caspase recruitment domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LW7](https://www.uniprot.org/uniprotkb/Q96LW7) (Caspase recruitment domain-containing protein 19):

> Plays a role in inhibiting the effects of BCL10-induced activation of NF-kappa-B. May inhibit the phosphorylation of BCL10 in a CARD-dependent manner.

**Summary**, from NCBI Gene [84270](https://www.ncbi.nlm.nih.gov/gene/84270):

> Predicted to enable CARD domain binding activity. Predicted to be involved in negative regulation of canonical NF-kappaB signal transduction. Predicted to act upstream of or within obsolete positive regulation of NF-kappaB transcription factor activity; positive regulation of canonical NF-kappaB signal transduction; and protein catabolic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28148) · Entrez [84270](https://www.ncbi.nlm.nih.gov/gene/84270) · UniProt [Q96LW7](https://www.uniprot.org/uniprotkb/Q96LW7) · Ensembl [ENSG00000165233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165233)

## Data

Gene col 9090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9090); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9090]; `tensor/DDL_lfc|DDL_z.npy` [9090]; `embed/gene_vectors.npy` [9090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9090 or target_col == 9090). Every well: [[CARD19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARD19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
