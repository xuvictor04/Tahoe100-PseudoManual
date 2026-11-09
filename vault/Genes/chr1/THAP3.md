---
symbol: "THAP3"
type: "gene"
col: 480
ensembl_id: "ENSG00000041988"
name: "THAP domain containing 3"
location: "1p36.31"
module: 12
arm: "+"
pooled_cpm: 7.59
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# THAP3

*THAP domain containing 3* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.34× (z +10.6, q 1e-23, up in 29 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.17× (z +9.7, q 1e-19, up in 34 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 0.110×, A498 0.133×; ⚠ toxic; transcription drop); [[Furosemide (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0630×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.209×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SW 900 0.0959×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPF2]] (+0.70, fdr 7e-06), [[DSTYK]] (+0.69, fdr 7e-06), [[RWDD3]] (+0.66, fdr 1e-05); moves opposite to [[IPO7]] (-0.67, fdr 1e-05), [[ITGB1]] (-0.66, fdr 7e-06), [[FAM91A1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +10.6 | 1e-23 | 29/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +9.7 | 1e-19 | 34/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.70×** | +9.4 | 1e-18 | 30/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +8.5 | 2e-15 | 33/41 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +7.3 | 4e-11 | 30/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.9 | 4e-10 | 24/38 (LOX-IMVI, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +6.5 | 6e-09 | 27/47 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +6.3 | 2e-08 | 23/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.69×** | +6.3 | 2e-08 | 24/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +6.2 | 4e-08 | 25/47 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.61×** | +6.0 | 1e-07 | 15/37 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +5.6 | 1e-06 | 21/45 (CFPAC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +5.5 | 1e-06 | 22/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.0 | 3e-05 | 18/39 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.5 | 3e-04 | 15/44 (A-172, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +4.4 | 4e-04 | 12/48 (RKO, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 5e-04 | 20/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.006 | 10/46 (C-33 A, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.021 | 6/46 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.021 | 0/47 | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.075 | 6/41 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 480.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 0.110×, A498 0.133×; ⚠ toxic; transcription drop); [[Furosemide (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0630×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.209×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SW 900 0.0959×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.8 | 0.095 | 5/48 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.762× | -3.2 | 0.25 | 6/48 (COLO 205, J82, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -3.1 | 0.25 | 10/48 (SW480, NCI-H2347, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.837× | -3.1 | 0.25 | 8/48 (CHP-212, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +14.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +8.9) | — |
| [[SW480 (line)]] | alt | 7.48 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.87× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -14.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 6.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -11.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 6.63 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0630× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 6.02 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.209× (z -8.6) |
| [[SNU-423 (line)]] | alt | 7.40 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 6.11 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0959× (z -8.6) |
| [[A-172 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPF2]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[DSTYK]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[RWDD3]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[COIL]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SAT2]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[NELFA]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[GFER]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[WHAMM]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ZNNT1]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TERF2IP]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[EAPP]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[LRRC37B]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO7]] | -0.67 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[ITGB1]] | -0.66 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[FAM91A1]] | -0.62 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.61 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[TPM3]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SEPTIN10]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.60 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.60 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ACTN1]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[LRPPRC]] | -0.59 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[GALNT1]] | -0.58 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[UGGT1]] | -0.58 | -0.36 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | C | THAP3's natural level lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (makes them more sensitive) | THAP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.71 | 0.250 over the table, 0.009 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.4, -17.3); signed map (-9.4, -0.7). **Vector** length 56.9, 8.31% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.6 | +9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | -0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.0 | -2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.5 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.3 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | +0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,624,868-6,635,586 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTV1](https://www.uniprot.org/uniprotkb/Q8WTV1) (THAP domain-containing protein 3):

> Component of a THAP1/THAP3-HCFC1-OGT complex that is required for the regulation of the transcriptional activity of RRM1.

**Summary**, from NCBI Gene [90326](https://www.ncbi.nlm.nih.gov/gene/90326):

> Predicted to enable DNA binding activity and zinc ion binding activity. Involved in positive regulation of transcription by RNA polymerase II. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20855) · Entrez [90326](https://www.ncbi.nlm.nih.gov/gene/90326) · UniProt [Q8WTV1](https://www.uniprot.org/uniprotkb/Q8WTV1) · Ensembl [ENSG00000041988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000041988)

## Data

Gene col 480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 480); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 480]; `tensor/DDL_lfc|DDL_z.npy` [480]; `embed/gene_vectors.npy` [480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 480 or target_col == 480). Every well: [[THAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
