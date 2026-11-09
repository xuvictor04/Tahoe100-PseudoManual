---
symbol: "LZTR1"
type: "gene"
col: 1833
ensembl_id: "ENSG00000099949"
name: "leucine zipper like post translational regulator 1"
location: "22q11.21"
module: 2
arm: "+"
pooled_cpm: 7.25
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# LZTR1

*leucine zipper like post translational regulator 1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.42× (z +4.6, q 0.003, up in 5 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.45× (z +3.8, q 0.041, up in 10 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.636× (z -6.5, q 5e-08, down in 21 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.810× (z -4.3, q 0.003, down in 16 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.114×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 0.0692×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.172×; ⚠ cell-cycle shift, explains ~82% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.209×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (C32 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIPOR1]] (+0.68, fdr 1e-05), [[ARFRP1]] (+0.64, fdr 7e-06), [[ZNF783]] (+0.63, fdr 9e-06, ⚠ ZNF783 in the vector space only through flagged drug-doses), [[IPO13]] (+0.61, fdr 1e-05); moves opposite to [[BCL2L14]] (-0.56, fdr 3e-05), [[A2MP1]] (-0.54, fdr 3e-05), [[TESK2]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF391]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.6 | 0.003 | 5/15 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.041 | 10/35 (A498, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.29×** | +3.6 | 0.047 | 7/48 (SW1417, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.20× | +3.6 | 0.047 | 8/48 (C-33 A, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.082 | 5/37 (HEC-1-A, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.3 | 0.082 | 5/47 (LoVo, SW1417, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 1.18× | +3.3 | 0.086 | 2/48 (RPMI-7951, J82) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.27× | +3.2 | 0.10 | 4/21 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.52× | +3.1 | 0.12 | 0/19 | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.27× | +3.1 | 0.12 | 5/45 (LoVo, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.27× | +3.0 | 0.12 | 5/45 (MIA PaCa-2, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1833.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.114×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 0.0692×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.172×; ⚠ cell-cycle shift, explains ~82% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.209×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (C32 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.636×** | -6.5 | 5e-08 | 21/43 (NCI-H1792, HOP62, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.721×** | -4.7 | 8e-04 | 15/46 (PANC-1, A-172, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -4.3 | 0.003 | 16/41 (Hs 766T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.568×** | -4.2 | 0.003 | 16/47 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.818×** | -4.1 | 0.005 | 19/43 (LOX-IMVI, J82, …) | top dose only | composition shift |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.857× | -3.1 | 0.16 | 11/47 (C-33 A, SW 1088, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 8.81 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.136× (z -8.5) |
| [[Hs 766T (line)]] | wt | 7.22 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 6.88 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -10.7) ⚠ cell-cycle shift, explains ~82% of this change |
| [[NCI-H1792 (line)]] | alt | 6.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0692× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPOR1]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ARFRP1]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ZNF783]] ⚠ | +0.63 | +0.58 / +0.57 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[IPO13]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC4A3]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[RPS6KA4]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TRIM68]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SGSH]] | +0.58 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ELAC2]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ACTR8]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[PARP3]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CEP170B]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L14]] | -0.56 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[A2MP1]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[TESK2]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[GLCCI1]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[COX8A]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[LINC01019]] | -0.52 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[NDUFA2]] | -0.50 | -0.56 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF391]] | B | ZNF391 activity raises LZTR1's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without ZNF391 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.474). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.1, -26.2); signed map (-8.7, -31.4). **Vector** length 55.7, 7.10% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.8 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.9 | -4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -1.9 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.2 | +0.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | leucine zipper like post translational regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,982,269-20,999,032 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LZTR-1, BTBD29 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N653](https://www.uniprot.org/uniprotkb/Q8N653) (Leucine-zipper-like transcriptional regulator 1):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex that mediates ubiquitination of Ras GTPases (M-Ras/MRAS, K-Ras/KRAS, N-Ras/NRAS and H-Ras/HRAS) and Ras-like protein RIT1. Acts as a negative regulator of RAS-MAPK signaling by controlling Ras levels and decreasing Ras association with membranes.

**Summary**, from NCBI Gene [8216](https://www.ncbi.nlm.nih.gov/gene/8216):

> This gene encodes a member of the BTB-kelch superfamily. Initially described as a putative transcriptional regulator based on weak homology to members of the basic leucine zipper-like family, the encoded protein subsequently has been shown to localize exclusively to the Golgi network where it may help stabilize the Gogli complex. Deletion of this gene may be associated with DiGeorge syndrome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6742) · Entrez [8216](https://www.ncbi.nlm.nih.gov/gene/8216) · UniProt [Q8N653](https://www.uniprot.org/uniprotkb/Q8N653) · Ensembl [ENSG00000099949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099949)

## Data

Gene col 1833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1833); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1833]; `tensor/DDL_lfc|DDL_z.npy` [1833]; `embed/gene_vectors.npy` [1833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1833 or target_col == 1833). Every well: [[LZTR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LZTR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
