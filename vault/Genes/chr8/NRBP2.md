---
symbol: "NRBP2"
type: "gene"
col: 11637
ensembl_id: "ENSG00000185189"
name: "nuclear receptor binding protein 2"
location: "8q24.3"
module: 2
arm: "+"
pooled_cpm: 8.35
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# NRBP2

*nuclear receptor binding protein 2* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.41× (z +9.5, q 9e-19, up in 13 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.42× (z +4.0, q 0.008, up in 16 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.396× (z -10.0, q 5e-21, down in 36 of 44 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.481× (z -8.2, q 5e-14, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LENG8]] (+0.68, fdr 7e-06), [[CAPN1]] (+0.67, fdr 1e-05), [[KLHL17]] (+0.64, fdr 7e-06); moves opposite to [[PIGBOS1]] (-0.53, fdr 2e-05), [[SUMO4]] (-0.51, fdr 9e-05), [[TCEAL8]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +9.5 | 9e-19 | 13/18 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +8.7 | 1e-15 | 22/29 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.52×** | +6.7 | 5e-09 | 23/46 (A-427, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +6.5 | 1e-08 | 18/23 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.008 | 16/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.44×** | +3.9 | 0.011 | 11/47 (A498, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.013 | 15/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.013 | 9/45 (NCI-H460, RKO, …) | two highest doses | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.072 | 9/41 (A498, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.32× | +3.0 | 0.15 | 9/44 (HOP62, RPMI-7951, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.396×** | -10.0 | 5e-21 | 36/44 (SW480, A-172, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -8.2 | 5e-14 | 32/40 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.545×** | -6.8 | 2e-09 | 26/45 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.553×** | -6.3 | 4e-08 | 26/43 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.751×** | -4.6 | 6e-04 | 22/42 (SNU-423, RKO, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -4.4 | 1e-03 | 22/46 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.480×** | -4.3 | 0.001 | 19/43 (NCI-H1573, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -4.1 | 0.002 | 23/44 (C32, HOP62, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -3.7 | 0.015 | 18/40 (KATO III, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.015 | 17/45 (NCI-H1792, NCI-H661, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.732×** | -3.5 | 0.022 | 20/41 (HOP62, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.747×** | -3.3 | 0.048 | 16/47 (BT-474, SNU-1, …) | rises with dose | composition shift |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.743×** | -3.2 | 0.069 | 12/42 (NCI-H1792, A549, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.684×** | -3.1 | 0.091 | 9/45 (KATO III, H4, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 9.99 | 0 | 2 | — | [[Idoxuridine (drug)]] 0.5 µM 0.0618× (z -10.1) |
| [[A-172 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.210× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.190× (z -9.1) |
| [[HOP62 (line)]] | alt | 6.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[hTERT-HPNE (line)]] | wt | 6.91 | 0 | 1 (1 ⚠) | — | [[Edoxaban (tosylate monohydrate) (drug)]] 0.5 µM 0.0562× (z -9.6) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 3.43 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.134× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0849× (z -9.0) |
| [[SNU-423 (line)]] | alt | 5.76 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 4.89 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LENG8]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CAPN1]] | +0.67 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[PLCB3]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SBF1]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[AKT1]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[DLST]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[PGGHG]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[CCDC61]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SH3GLB2]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TUBGCP6]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGBOS1]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SUMO4]] | -0.51 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[TCEAL8]] | -0.49 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises NRBP2's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without SLC4A3 | 0.082 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.5, -22.6); signed map (-46.4, -10.5). **Vector** length 78.5, 14.0% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.7 | +6.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +3.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.8 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.3 | -10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -8.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | +0.3 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,833,583-143,840,973 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434P086 |
| Gene groups (HGNC) | Pseudokinases; MicroRNA protein coding host genes; Nuclear receptor binding protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSY0](https://www.uniprot.org/uniprotkb/Q9NSY0) (Nuclear receptor-binding protein 2):

> May regulate apoptosis of neural progenitor cells during their differentiation.

**Summary**, from NCBI Gene [340371](https://www.ncbi.nlm.nih.gov/gene/340371):

> Predicted to enable protein serine/threonine kinase activity. Involved in negative regulation of macroautophagy. Predicted to be located in cytoplasm. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19339) · Entrez [340371](https://www.ncbi.nlm.nih.gov/gene/340371) · UniProt [Q9NSY0](https://www.uniprot.org/uniprotkb/Q9NSY0) · Ensembl [ENSG00000185189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185189)

## Data

Gene col 11637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11637); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11637]; `tensor/DDL_lfc|DDL_z.npy` [11637]; `embed/gene_vectors.npy` [11637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11637 or target_col == 11637). Every well: [[NRBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
