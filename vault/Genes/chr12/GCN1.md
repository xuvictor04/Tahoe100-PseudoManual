---
symbol: "GCN1"
type: "gene"
col: 1572
ensembl_id: "ENSG00000089154"
name: "GCN1 activator of EIF2AK4"
location: "12q24.23"
module: 33
arm: "+"
pooled_cpm: 80.0
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# GCN1

*GCN1 activator of EIF2AK4* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.74× (z +7.7, q 6e-12, up in 43 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 2.23×, LOX-IMVI 1.83×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 2.50×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.722× (z -6.8, q 6e-09, down in 30 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF587B]] (+0.80, fdr 7e-06), [[LRRC59]] (+0.73, fdr 7e-06), [[PCNX3]] (+0.72, fdr 7e-06); moves opposite to [[CERT1]] (-0.67, fdr 1e-05), [[RAB9A]] (-0.65, fdr 8e-06), [[ANKRD12]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01273]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1572.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 2.23×, LOX-IMVI 1.83×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 2.50×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +7.7 | 6e-12 | 43/49 (MIA PaCa-2, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.32×** | +6.5 | 3e-08 | 38/48 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +6.2 | 8e-08 | 41/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.26× | +3.2 | 0.19 | 23/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 1.50× | +3.1 | 0.19 | 16/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.23× | +3.0 | 0.19 | 22/48 (NCI-H1573, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.722×** | -6.8 | 6e-09 | 30/49 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.673×** | -5.6 | 6e-06 | 35/48 (J82, C-33 A, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -4.7 | 4e-04 | 28/47 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.756×** | -4.1 | 0.005 | 26/48 (SHP-77, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.769×** | -3.9 | 0.012 | 26/48 (SW 900, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.776×** | -3.7 | 0.017 | 28/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.793×** | -3.4 | 0.043 | 22/48 (A-172, LS 180, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.793×** | -3.4 | 0.043 | 26/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.4 | 0.046 | 18/48 (HS-578T, AN3 CA, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.790×** | -3.3 | 0.046 | 24/48 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.796×** | -3.2 | 0.061 | 19/47 (LoVo, C-33 A, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.863× | -3.1 | 0.091 | 13/48 (SW480, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 78.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -10.2) |
| [[J82 (line)]] | alt | 87.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.366× (z -10.1) |
| [[SHP-77 (line)]] | alt | 106 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.405× (z -9.0) |
| [[A498 (line)]] | wt | 96.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -8.6) |
| [[C32 (line)]] | wt | 46.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 57.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 60.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 65.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.129× (z -8.9) |
| [[PANC-1 (line)]] | alt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -8.6) |
| [[SW 1271 (line)]] | alt | 72.6 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0884× (z -9.2) |
| [[SW 900 (line)]] | alt | 70.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -8.6) |
| [[SW480 (line)]] | alt | 74.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.470× (z -8.5) |
| [[A-172 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 146 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 102 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF587B]] | +0.80 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[LRRC59]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.72 | +0.64 / +0.80 | both halves | 7e-06 | same gene group |
| [[MFN2]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[NSUN2]] | +0.70 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.69 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[NCBP1]] | +0.69 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[RPSA]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 | pathway: Cellular response to starvation; STRING 900 |
| [[TXNDC5]] | +0.68 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[TRAP1]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[URB1]] | +0.66 | +0.58 / +0.71 | both halves | 7e-06 | STRING 468 |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERT1]] | -0.67 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.65 | -0.58 / -0.68 | both halves | 8e-06 |  |
| [[ANKRD12]] | -0.65 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[BTG1]] | -0.64 | -0.48 / -0.74 | both halves | 2e-05 |  |
| [[PNRC1]] | -0.63 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[RRAGC]] | -0.63 | -0.59 / -0.64 | both halves | 7e-06 | pathway: Cellular response to starvation |
| [[EIF1B]] | -0.63 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[CCDC24]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[KMT2E]] | -0.60 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[KMT2A]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[NCOA1]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[MARCKS]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01273]] | B | LINC01273 activity lowers GCN1's level | lines that do not express LINC01273 (12) vs lines expressing it (38) | 1.05× higher at baseline in the lines without LINC01273 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000287263, A4GALT, TRIM7; maybe low, not absent; its own permutation p |
| [[HDAC6]] | B | HDAC6 activity raises GCN1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.7, -28.0); signed map (-23.1, -44.0). **Vector** length 118, 35.9% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.3 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.5 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.7 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +6.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -5.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.0 | -3.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | GCN1 activator of EIF2AK4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:120,127,202-120,194,715 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0219, GCN1L; previously GCN1L1 |
| Gene groups (HGNC) | TOG domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Response of EIF2AK4 (GCN2) to amino acid deficiency; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92616](https://www.uniprot.org/uniprotkb/Q92616) (Stalled ribosome sensor GCN1):

> Ribosome collision sensor that plays a key role in the RNF14-RNF25 translation quality control pathway, a pathway that takes place when a ribosome has stalled during translation, and which promotes ubiquitination and degradation of translation factors on stalled ribosomes. Directly binds to the ribosome and acts as a sentinel for colliding ribosomes: activated following ribosome stalling and promotes recruitment of RNF14, which directly ubiquitinates EEF1A1/eEF1A, leading to its degradation. In …

**Summary**, from NCBI Gene [10985](https://www.ncbi.nlm.nih.gov/gene/10985):

> Enables molecular adaptor activity and stalled ribosome sensor activity. Involved in protein-RNA covalent cross-linking repair. Located in cytosol. Is active in cytosolic ribosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4199) · Entrez [10985](https://www.ncbi.nlm.nih.gov/gene/10985) · UniProt [Q92616](https://www.uniprot.org/uniprotkb/Q92616) · Ensembl [ENSG00000089154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089154)

## Data

Gene col 1572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1572); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1572]; `tensor/DDL_lfc|DDL_z.npy` [1572]; `embed/gene_vectors.npy` [1572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1572 or target_col == 1572). Every well: [[GCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
