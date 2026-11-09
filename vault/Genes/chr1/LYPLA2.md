---
symbol: "LYPLA2"
type: "gene"
col: 219
ensembl_id: "ENSG00000011009"
name: "lysophospholipase 2"
location: "1p36.11"
module: 17
arm: "-"
pooled_cpm: 10.5
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# LYPLA2

*lysophospholipase 2* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +10.9, q 4e-25, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.712× (z -4.1, q 0.026, down in 15 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Menadione (drug)]] 5 µM in 1 line (C32 0.0629×); [[Silodosin (drug)]] 5 µM in 1 line (H4 0.0871×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1CA]] (+0.59, fdr 1e-05), [[FURIN]] (+0.53, fdr 2e-05), [[DHRS11]] (+0.53, fdr 9e-05); moves opposite to [[MAP4K5]] (-0.51, fdr 1e-04), [[RAD23A]] (-0.50, fdr 3e-04), [[GTF2H2C]] (-0.50, fdr 3e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +10.9 | 4e-25 | 40/43 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.28×** | +10.3 | 2e-22 | 28/35 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.08×** | +8.8 | 2e-16 | 17/21 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.3 | 3e-08 | 26/48 (HOP62, LOX-IMVI, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.63×** | +5.9 | 5e-07 | 32/45 (LS 180, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.59×** | +5.6 | 2e-06 | 25/45 (RKO, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.53×** | +4.9 | 7e-05 | 17/28 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.47×** | +4.9 | 8e-05 | 22/45 (PANC-1, HCT15, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.8 | 9e-05 | 17/47 (CFPAC-1, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.49×** | +4.8 | 9e-05 | 18/39 (PANC-1, A549, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.40×** | +4.2 | 0.001 | 16/42 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.41×** | +4.2 | 0.002 | 18/41 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.004 | 17/46 (SW480, SW48, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.4 | 0.023 | 9/27 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.3 | 0.033 | 1/20 (NCI-H2347) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.039 | 9/42 (SK-MEL-2, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.29×** | +2.9 | 0.097 | 6/43 (HEC-1-A, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 219.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Menadione (drug)]] 5 µM in 1 line (C32 0.0629×); [[Silodosin (drug)]] 5 µM in 1 line (H4 0.0871×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.712×** | -4.1 | 0.026 | 15/44 (C32, NCI-H23, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM |  | 0.757× | -3.4 | 0.19 | 14/45 (SW1417, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.761× | -3.3 | 0.19 | 8/48 (SW480, SW 1088, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.615× | -3.2 | 0.20 | 13/42 (SW480, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Thymopentin (drug)]] 5 µM |  | 0.771× | -3.1 | 0.20 | 7/46 (H4, HS-578T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.775× | -3.1 | 0.20 | 15/45 (C-33 A, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 7.04 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0629× (z -10.4) |
| [[H4 (line)]] | wt | 9.87 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0871× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 7.27 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.33× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1573 (line)]] | alt | 8.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 6.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.1) | — |
| [[A-172 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1CA]] | +0.59 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[FURIN]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[DHRS11]] | +0.53 | +0.37 / +0.47 | both halves | 9e-05 |  |
| [[PCGF2]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[GPAA1]] | +0.52 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[IRGQ]] | +0.52 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[DMWD]] | +0.49 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[LRP10]] | +0.48 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[GSK3A]] | +0.48 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[UROD]] | +0.48 | +0.21 / +0.55 | both halves | 6e-04 |  |
| [[CDIPT]] | +0.47 | +0.24 / +0.47 | both halves | 4e-04 |  |
| [[ZFYVE27]] | +0.47 | +0.45 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP4K5]] | -0.51 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[RAD23A]] | -0.50 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[GTF2H2C]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TTBK2]] | -0.49 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[ESD]] | -0.49 | -0.49 / -0.35 | both halves | 1e-04 | same gene group |
| [[SUGT1P4-STRA6LP-CCDC180]] | -0.48 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[PARP2]] | -0.47 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[HNRNPDL]] | -0.47 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[MRPS31P4]] | -0.46 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[STRA6LP]] | -0.46 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[SUGT1P4-STRA6LP]] | -0.46 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[THAP8]] | -0.46 | -0.58 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LYPLA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[STRA6LP]], [[SUGT1P4-STRA6LP]], [[SUGT1P4-STRA6LP-CCDC180]] | B | STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 activity lowers LYPLA2's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 1.15× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 0.093 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.1, -6.5); signed map (2.3, 3.3). **Vector** length 62.6, 10.2% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.4 | +5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.7 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.4 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | lysophospholipase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:23,791,110-23,795,539 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APT-2, APT2 |
| Gene groups (HGNC) | Depalmitoylases; Thioester hydrolases |
| Reactome | 3 pathways, smallest: L1CAM interactions; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [O95372](https://www.uniprot.org/uniprotkb/O95372) (Acyl-protein thioesterase 2):

> Acts as an acyl-protein thioesterase hydrolyzing fatty acids from S-acylated cysteine residues in proteins such as trimeric G alpha proteins, GSDMD, GAP43, ZDHHC6 or HRAS. Deacylates GAP43. Mediates depalmitoylation of ZDHHC6. Has lysophospholipase activity. Hydrolyzes prostaglandin glycerol esters (PG-Gs) in the following order prostaglandin D2-glycerol ester (PGD2-G) > prostaglandin E2 glycerol ester (PGE2-G) > prostaglandin F2-alpha-glycerol ester (PGF2-alpha-G). Hydrolyzes …

**Summary**, from NCBI Gene [11313](https://www.ncbi.nlm.nih.gov/gene/11313):

> Lysophospholipases are enzymes that act on biological membranes to regulate the multifunctional lysophospholipids. There are alternatively spliced transcript variants described for this gene but the full length nature is not known yet. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6738) · Entrez [11313](https://www.ncbi.nlm.nih.gov/gene/11313) · UniProt [O95372](https://www.uniprot.org/uniprotkb/O95372) · Ensembl [ENSG00000011009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011009)

## Data

Gene col 219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 219); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 219]; `tensor/DDL_lfc|DDL_z.npy` [219]; `embed/gene_vectors.npy` [219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 219 or target_col == 219). Every well: [[LYPLA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPLA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
