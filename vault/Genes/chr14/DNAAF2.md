---
symbol: "DNAAF2"
type: "gene"
col: 9134
ensembl_id: "ENSG00000165506"
name: "dynein axonemal assembly factor 2"
location: "14q21.3"
module: 1
arm: "+"
pooled_cpm: 9.83
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DNAAF2

*dynein axonemal assembly factor 2* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.22× (z +8.6, q 7e-15, up in 26 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +5.7, q 2e-06, up in 22 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.151×, SK-MEL-2 0.140×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (A498 0.191×; ⚠ cell-cycle shift, explains ~63% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (SW48 0.0943×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LS 180 0.173×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADO]] (+0.74, fdr 7e-06), [[RPP38]] (+0.70, fdr 7e-06), [[ZBTB2]] (+0.65, fdr 1e-05); moves opposite to [[F11R]] (-0.62, fdr 1e-05), [[QSOX1]] (-0.59, fdr 1e-05), [[SAR1A]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PPP1R9A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +8.6 | 7e-15 | 26/34 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.6 | 2e-08 | 9/17 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.7 | 2e-06 | 22/44 (A549, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +5.6 | 4e-06 | 28/46 (SW480, A549, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +5.3 | 1e-05 | 17/27 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.1 | 2e-05 | 21/37 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.68×** | +5.0 | 4e-05 | 24/45 (A549, SW480, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.56×** | +4.7 | 1e-04 | 24/45 (CFPAC-1, NCI-H1792, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.4 | 6e-04 | 17/47 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.002 | 17/47 (A-172, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.44×** | +3.9 | 0.005 | 13/39 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.7 | 0.011 | 15/47 (NCI-H460, A549, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.6 | 0.012 | 4/48 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.42×** | +3.4 | 0.028 | 15/40 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.3 | 0.037 | 16/45 (CFPAC-1, A549, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.080 | 16/46 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.098 | 7/46 (A498, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9134.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.151×, SK-MEL-2 0.140×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (A498 0.191×; ⚠ cell-cycle shift, explains ~63% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (SW48 0.0943×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LS 180 0.173×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.722× | -3.2 | 0.39 | 13/45 (KATO III, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.746× | -3.2 | 0.39 | 16/47 (PANC-1, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.03 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.191× (z -9.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[CFPAC-1 (line)]] | alt | 7.21 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.173× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 7.81 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.67× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 17.9 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0943× (z -8.7) |
| [[A-172 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADO]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[RPP38]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZBTB2]] | +0.65 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[NUDT19]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[RRS1]] | +0.65 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.64 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[AASDHPPT]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[COA7]] | +0.63 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[E2F5]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SRSF8]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.63 | +0.58 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F11R]] | -0.62 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SAR1A]] | -0.56 | -0.63 / -0.49 | both halves | 1e-05 | STRING 403 |
| [[MAGT1]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R9A]] | B | PPP1R9A activity raises DNAAF2's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without PPP1R9A | 0.048 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[MEX3A]] | B | MEX3A activity raises DNAAF2's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without MEX3A | 0.057 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-35.2, 14.1); signed map (3.0, -38.7). **Vector** length 69.6, 12.8% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.5 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.1 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | -2.1 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -1.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal assembly factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,625,174-49,635,244 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10563, KTU, pf13, CILD10; previously C14orf104 |
| Gene groups (HGNC) | Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVR5](https://www.uniprot.org/uniprotkb/Q9NVR5) (Protein kintoun):

> Required for cytoplasmic pre-assembly of axonemal dyneins, thereby playing a central role in motility in cilia and flagella. Involved in pre-assembly of dynein arm complexes in the cytoplasm before intraflagellar transport loads them for the ciliary compartment.

**Summary**, from NCBI Gene [55172](https://www.ncbi.nlm.nih.gov/gene/55172):

> This gene encodes a highly conserved protein involved in the preassembly of dynein arm complexes which power cilia. These complexes are found in some cilia and are assembled in the cytoplasm prior to transport for cilia formation. Mutations in this gene have been associated with primary ciliary dyskinesia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:20188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20188) · Entrez [55172](https://www.ncbi.nlm.nih.gov/gene/55172) · UniProt [Q9NVR5](https://www.uniprot.org/uniprotkb/Q9NVR5) · Ensembl [ENSG00000165506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165506)

## Data

Gene col 9134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9134); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9134]; `tensor/DDL_lfc|DDL_z.npy` [9134]; `embed/gene_vectors.npy` [9134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9134 or target_col == 9134). Every well: [[DNAAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
