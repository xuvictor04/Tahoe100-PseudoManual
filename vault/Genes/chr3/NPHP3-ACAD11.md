---
symbol: "NPHP3-ACAD11"
type: "gene"
col: 15830
ensembl_id: "ENSG00000274810"
name: "NPHP3-ACAD11 readthrough (NMD candidate)"
location: "3q22.1"
module: 37
arm: "+"
pooled_cpm: 7.64
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# NPHP3-ACAD11

*NPHP3-ACAD11 readthrough (NMD candidate)* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +10.9, q 4e-25, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.675× (z -5.3, q 4e-05, down in 18 of 46 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Omeprazole (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0539×); [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.147×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (C32 0.0668×; ⚠ cell-cycle shift, explains ~20% of this change); [[Sunitinib (drug)]] 0.05 µM in 1 line (A-172 0.111×); [[Ferulic acid (drug)]] 0.5 µM in 1 line (AsPC-1 0.0668×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC62]] (+0.75, fdr 7e-06), [[PRC1-AS1]] (+0.74, fdr 7e-06), [[ZNF451-AS1]] (+0.72, fdr 7e-06); moves opposite to [[THEM6]] (-0.61, fdr 3e-05), [[DAGLA]] (-0.58, fdr 7e-05), [[NAA40]] (-0.56, fdr 5e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +10.9 | 4e-25 | 31/43 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +10.4 | 6e-23 | 11/15 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.56×** | +6.3 | 6e-08 | 25/48 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.7 | 1e-06 | 21/42 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.5 | 4e-06 | 14/33 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.4 | 7e-06 | 18/43 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.31×** | +5.3 | 9e-06 | 19/48 (AsPC-1, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +3.6 | 0.022 | 4/23 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +3.1 | 0.11 | 5/47 (A-427, LS 180, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15830.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Omeprazole (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0539×); [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.147×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (C32 0.0668×; ⚠ cell-cycle shift, explains ~20% of this change); [[Sunitinib (drug)]] 0.05 µM in 1 line (A-172 0.111×); [[Ferulic acid (drug)]] 0.5 µM in 1 line (AsPC-1 0.0668×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.675×** | -5.3 | 4e-05 | 18/46 (SNU-423, H4, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.678×** | -5.3 | 4e-05 | 15/37 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.695×** | -5.1 | 6e-05 | 19/47 (MIA PaCa-2, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.724×** | -4.5 | 8e-04 | 15/46 (AN3 CA, HOP62, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.729×** | -4.4 | 0.001 | 17/43 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.742×** | -4.2 | 0.003 | 13/45 (BT-474, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.579×** | -4.0 | 0.005 | 12/46 (SK-MEL-2, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.617×** | -3.5 | 0.028 | 10/37 (Hs 766T, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 0.848× | -3.3 | 0.063 | 6/48 (HOP62, SW48, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.794×** | -3.2 | 0.068 | 8/42 (C32, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.795×** | -3.1 | 0.090 | 15/43 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 5 µM |  | 0.798× | -3.1 | 0.11 | 8/46 (SW1417, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 4.36 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.28× (z +8.8) | [[Ferulic acid (drug)]] 0.5 µM 0.0668× (z -10.1) |
| [[A-172 (line)]] | wt | 11.2 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.111× (z -10.7) |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0724× (z -9.9) |
| [[C32 (line)]] | wt | 9.67 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0668× (z -10.8) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[Panc 03.27 (line)]] | alt | 7.42 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0802× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0539× (z -14.7) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC62]] | +0.75 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[PRC1-AS1]] | +0.74 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ZNF451-AS1]] | +0.72 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.71 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.71 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PLD5P1]] | +0.70 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[PXDNL]] | +0.70 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[OOEP]] | +0.70 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[MFSD2B]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.67 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[NUP210L]] | +0.67 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.61 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[DAGLA]] | -0.58 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[NAA40]] | -0.56 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[MAGEF1]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NPHP3-ACAD11's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.2, -15.1); signed map (15.3, 4.1). **Vector** length 61.4, 8.48% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +10.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +2.7 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.2 | -4.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -2.2 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | +0.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | NPHP3-ACAD11 readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 3q22.1 — chr3:132,558,142-132,722,459 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100532724](https://www.ncbi.nlm.nih.gov/gene/100532724):

> This locus represents naturally occurring read-through transcription between the neighboring NPHP3 (nephronophthisis 3, adolescent) and ACAD11 (acyl-CoA dehydrogenase family, member 11) genes on chromosome 3. The read-through transcript is a candidate for nonsense-mediated mRNA decay (NMD), and is thus unlikely to produce a protein product. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:48351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48351) · Entrez [100532724](https://www.ncbi.nlm.nih.gov/gene/100532724) · Ensembl [ENSG00000274810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274810)

## Data

Gene col 15830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15830); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15830]; `tensor/DDL_lfc|DDL_z.npy` [15830]; `embed/gene_vectors.npy` [15830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15830 or target_col == 15830). Every well: [[NPHP3-ACAD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPHP3-ACAD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
