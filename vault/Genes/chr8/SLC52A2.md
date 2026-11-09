---
symbol: "SLC52A2"
type: "gene"
col: 11734
ensembl_id: "ENSG00000185803"
name: "solute carrier family 52 member 2"
location: "8q24.3"
module: 3
arm: "+"
pooled_cpm: 8.55
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SLC52A2

*solute carrier family 52 member 2* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +7.7, q 1e-11, up in 20 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +6.6, q 1e-08, up in 29 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.486× (z -6.8, q 8e-09, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNQ]] (+0.64, fdr 1e-05), [[RIC8A]] (+0.62, fdr 1e-05), [[TUSC2]] (+0.60, fdr 2e-04); moves opposite to [[NHLRC2]] (-0.53, fdr 6e-05), [[RHOBTB3]] (-0.51, fdr 5e-05), [[ITGAV]] (-0.50, fdr 5e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HMGN5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.26×** | +7.7 | 1e-11 | 20/30 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.6 | 1e-08 | 29/40 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.21×** | +6.5 | 2e-08 | 8/13 (SW1417, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.86×** | +5.8 | 8e-07 | 29/47 (AsPC-1, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.7 | 1e-06 | 22/33 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +5.4 | 6e-06 | 29/45 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.77×** | +5.4 | 6e-06 | 30/46 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.9 | 6e-05 | 18/35 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.61×** | +4.5 | 4e-04 | 22/46 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.57×** | +3.7 | 0.011 | 16/36 (A-172, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.51×** | +3.6 | 0.016 | 3/17 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.055 | 10/41 (SW480, A-427, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.067 | 12/41 (hTERT-HPNE, SK-MEL-2, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.39×** | +3.1 | 0.080 | 10/44 (NCI-H460, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.486×** | -6.8 | 8e-09 | 32/46 (SW48, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -5.4 | 2e-05 | 26/45 (A-427, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.727×** | -4.2 | 0.005 | 17/41 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.735×** | -4.1 | 0.006 | 20/45 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.611×** | -4.0 | 0.007 | 23/44 (J82, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.659×** | -3.9 | 0.009 | 17/45 (A498, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -3.6 | 0.021 | 24/45 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -3.6 | 0.022 | 15/43 (AsPC-1, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.704×** | -3.3 | 0.064 | 20/39 (hTERT-HPNE, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.709×** | -3.2 | 0.073 | 9/46 (SNU-423, LoVo, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -3.2 | 0.073 | 16/40 (A-427, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 35.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 4.86 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0712× (z -10.6) ⚠ toxic |
| [[J82 (line)]] | alt | 10.5 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.117× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 8.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 3.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.62× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNQ]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[RIC8A]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TUSC2]] | +0.60 | +0.32 / +0.69 | both halves | 2e-04 |  |
| [[YKT6]] | +0.60 | +0.67 / +0.36 | both halves | 9e-05 |  |
| [[MRPS12]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ZNRD2]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[PUSL1]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NUBP2]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[VPS53]] | +0.58 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[SLC35C1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PCYT1A]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SNAPC2]] | +0.57 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | -0.53 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[RHOBTB3]] | -0.51 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ITGAV]] | -0.50 | -0.24 / -0.56 | both halves | 5e-04 |  |
| [[TAB2]] | -0.50 | -0.25 / -0.56 | both halves | 4e-04 |  |
| [[ZNF608]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[KAT2B]] | -0.50 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[ATRX]] | -0.50 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[ENOSF1]] | -0.49 | -0.43 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN5]] | B | HMGN5 activity lowers SLC52A2's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.47× higher at baseline in the lines without HMGN5 | 0.090 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.412). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-13.1, -7.6); signed map (-41.5, 6.4). **Vector** length 66.4, 12.3% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +6.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +2.6 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | +2.4 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +1.8 |
| fall | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -6.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 52 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,333,957-144,361,286 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11856, PAR1, GPCR41, D15Ertd747e, RFVT2, hRFT3, RFT3, HuPAR-1; previously GPR172A |
| Gene groups (HGNC) | Solute carrier family 52; Flavoproteins |
| Reactome | 3 pathways, smallest: Vitamin B2 (riboflavin) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAB3](https://www.uniprot.org/uniprotkb/Q9HAB3) (Solute carrier family 52, riboflavin transporter, member 2):

> Plasma membrane transporter mediating the uptake by cells of the water soluble vitamin B2/riboflavin that plays a key role in biochemical oxidation-reduction reactions of the carbohydrate, lipid, and amino acid metabolism. Humans are unable to synthesize vitamin B2/riboflavin and must obtain it via intestinal absorption. May also act as a receptor for 4-hydroxybutyrate (Probable).; (Microbial infection) In case of infection by retroviruses, acts as a cell receptor to retroviral envelopes …

**Summary**, from NCBI Gene [79581](https://www.ncbi.nlm.nih.gov/gene/79581):

> This gene encodes a membrane protein which belongs to the riboflavin transporter family. In humans, riboflavin must be obtained by intestinal absorption because it cannot be synthesized by the body. The water-soluble vitamin riboflavin is processed to the coenzymes flavin mononucleotide (FMN) and flavin adenine dinucleotide (FAD) which then act as intermediaries in many cellular metabolic reactions. Paralogous members of the riboflavin transporter gene family are located on chromosomes 17 and …

**Accessions** — [HGNC:30224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30224) · Entrez [79581](https://www.ncbi.nlm.nih.gov/gene/79581) · UniProt [Q9HAB3](https://www.uniprot.org/uniprotkb/Q9HAB3) · Ensembl [ENSG00000185803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185803)

## Data

Gene col 11734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11734); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11734]; `tensor/DDL_lfc|DDL_z.npy` [11734]; `embed/gene_vectors.npy` [11734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11734 or target_col == 11734). Every well: [[SLC52A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC52A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
