---
symbol: "CNEP1R1"
type: "gene"
col: 12978
ensembl_id: "ENSG00000205423"
name: "CTD nuclear envelope phosphatase 1 regulatory subunit 1"
location: "16q12.1"
module: 30
arm: "+"
pooled_cpm: 12.22
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CNEP1R1

*CTD nuclear envelope phosphatase 1 regulatory subunit 1* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.82× (z +7.8, q 1e-12, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.544× (z -7.9, q 1e-12, down in 22 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.675× (z -7.3, q 1e-10, down in 27 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.122×, NCI-H2030 0.218×, MIA PaCa-2 0.144×, A498 0.272×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.125×, LOX-IMVI 0.165×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 0.107×, NCI-H1792 0.125×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0867×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (BT-474 0.0860×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.403×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEATR6]] (+0.69, fdr 1e-05), [[SUGT1P4-STRA6LP]] (+0.68, fdr 7e-06), [[ELP1]] (+0.67, fdr 3e-05); moves opposite to [[CCDC90B-AS1]] (-0.64, fdr 3e-05), [[FBXL19-AS1]] (-0.63, fdr 2e-04), [[ZNF341-AS1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GRIP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +7.8 | 1e-12 | 37/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +7.8 | 1e-12 | 36/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +7.7 | 3e-12 | 36/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.9 | 1e-04 | 15/41 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.21×** | +3.6 | 0.037 | 12/48 (RKO, RPMI-7951, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.049 | 9/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12978.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.122×, NCI-H2030 0.218×, MIA PaCa-2 0.144×, A498 0.272×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.125×, LOX-IMVI 0.165×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 0.107×, NCI-H1792 0.125×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0867×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (BT-474 0.0860×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.403×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.544×** | -7.9 | 1e-12 | 22/35 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -7.3 | 1e-10 | 27/45 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -5.8 | 1e-06 | 15/23 (A498, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.662×** | -5.0 | 9e-05 | 15/28 (J82, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Thymol (drug)]] 5 µM |  | **0.823×** | -3.6 | 0.037 | 13/48 (CHP-212, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.774× | -3.2 | 0.13 | 19/46 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 19.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -14.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -9.4) |
| [[BT-474 (line)]] | alt | 7.25 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0860× (z -9.4) |
| [[C32 (line)]] | wt | 7.64 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0867× (z -10.0) |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.115× (z -9.2) |
| [[HT-29 (line)]] | alt | 6.62 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.109× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 9.15 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.44 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 9.26 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.274× (z -8.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A-172 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR6]] | +0.69 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[SUGT1P4-STRA6LP]] | +0.68 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ELP1]] | +0.67 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[POT1]] | +0.66 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[ANAPC4]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[MRPS31P4]] | +0.66 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ABHD10]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[RAD17]] | +0.65 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[NBPF3]] | +0.65 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[RNF216P1]] | +0.65 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[PRUNE1]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.64 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | -0.64 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[FBXL19-AS1]] | -0.63 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[ZNF341-AS1]] | -0.62 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PTPRK]] | -0.61 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ZHX2]] | -0.61 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[MZF1-AS1]] | -0.60 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[LNCRNA-IUR]] | -0.60 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[HIVEP2-DT]] | -0.60 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[MED13]] | -0.59 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[EYS]] | -0.59 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PPP1R15B-AS1]] | -0.59 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NQO1-DT]] | -0.58 | -0.54 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIP1]] | B | GRIP1 activity lowers CNEP1R1's level | lines that do not express GRIP1 (13) vs lines expressing it (37) | 1.15× higher at baseline in the lines without GRIP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PAX9; maybe low, not absent |
| [[STRA6LP]], [[SUGT1P4-STRA6LP]], [[SUGT1P4-STRA6LP-CCDC180]] | B | STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 activity lowers CNEP1R1's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 1.19× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[HDAC6]] | B | HDAC6 activity lowers CNEP1R1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.0, -8.0); signed map (-29.7, -11.6). **Vector** length 72.1, 12.3% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.3 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.1 | -7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.5 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +0.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.6 | -1.2 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | -1.6 | -1.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | CTD nuclear envelope phosphatase 1 regulatory subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:50,024,410-50,037,088 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38101, NEP1-R1; previously C16orf69, TMEM188 |
| Reactome | 6 pathways, smallest: Depolymerization of the Nuclear Lamina; Nuclear Envelope Breakdown; Mitotic Prophase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9A8](https://www.uniprot.org/uniprotkb/Q8N9A8) (Nuclear envelope phosphatase-regulatory subunit 1):

> Forms with the serine/threonine protein phosphatase CTDNEP1 an active complex which dephosphorylates and may activate LPIN1 and LPIN2. LPIN1 and LPIN2 are phosphatidate phosphatases that catalyze the conversion of phosphatidic acid to diacylglycerol and control the metabolism of fatty acids at different levels. May indirectly modulate the lipid composition of nuclear and/or endoplasmic reticulum membranes and be required for proper nuclear membrane morphology and/or dynamics. May also …

**Summary**, from NCBI Gene [255919](https://www.ncbi.nlm.nih.gov/gene/255919):

> This gene encodes a transmembrane protein that belongs to the Tmemb_18A family. A similar protein in yeast is a component of an endoplasmic reticulum-associated protein phosphatase complex and is thought to play a role in the synthesis of triacylglycerol. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:26759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26759) · Entrez [255919](https://www.ncbi.nlm.nih.gov/gene/255919) · UniProt [Q8N9A8](https://www.uniprot.org/uniprotkb/Q8N9A8) · Ensembl [ENSG00000205423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205423)

## Data

Gene col 12978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12978); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12978]; `tensor/DDL_lfc|DDL_z.npy` [12978]; `embed/gene_vectors.npy` [12978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12978 or target_col == 12978). Every well: [[CNEP1R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNEP1R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
