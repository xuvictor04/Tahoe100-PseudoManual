---
symbol: "MPC2"
type: "gene"
col: 6687
ensembl_id: "ENSG00000143158"
name: "mitochondrial pyruvate carrier 2"
location: "1q24.2"
module: 5
arm: "-"
pooled_cpm: 20.65
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MPC2

*mitochondrial pyruvate carrier 2* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.40× (z +9.5, q 9e-19, up in 37 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +7.5, q 1e-11, up in 37 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H23 0.0640×); [[Rapamycin (drug)]] 0.5 µM in 1 line (H4 0.0867×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF6]] (+0.62, fdr 1e-05, ⚠ same locus), [[ADD3]] (+0.60, fdr 2e-05), [[RNASE4]] (+0.59, fdr 1e-05), [[OXR1]] (+0.59, fdr 3e-05); moves opposite to [[ZNF195]] (-0.68, fdr 1e-05), [[MAK16]] (-0.68, fdr 7e-06), [[ZNF239]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLAG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 13 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.40×** | +9.5 | 9e-19 | 37/41 (A549, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.5 | 1e-11 | 37/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.95×** | +7.0 | 6e-10 | 25/31 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.89×** | +6.9 | 7e-10 | 33/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.81×** | +6.5 | 1e-08 | 35/47 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.77×** | +6.2 | 5e-08 | 34/46 (PANC-1, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.60×** | +5.1 | 2e-05 | 30/48 (PANC-1, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 3e-04 | 25/46 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.61×** | +4.4 | 6e-04 | 19/36 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.45×** | +3.9 | 0.006 | 21/47 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.39×** | +3.6 | 0.017 | 19/48 (SW1417, PANC-1, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.38×** | +3.5 | 0.019 | 22/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~71% of this change | **1.38×** | +3.3 | 0.035 | 16/44 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.35×** | +3.3 | 0.045 | 19/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.33×** | +3.1 | 0.066 | 16/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.59×** | +3.0 | 0.094 | 8/47 (Hs 766T, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6687.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H23 0.0640×); [[Rapamycin (drug)]] 0.5 µM in 1 line (H4 0.0867×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.747× | -3.0 | 0.70 | 15/47 (NCI-H2347, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[A549 (line)]] | wt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0867× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[KATO III (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0640× (z -14.0) |
| [[SW480 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[A-172 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*28 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF6]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ADD3]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[RNASE4]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[OXR1]] | +0.59 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ARL3]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[RFX2]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PCSK1N]] | +0.57 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[PPP2R5A]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ANG]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[CUTA]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TMEM59]] | +0.56 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SLC25A1]] | +0.56 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[MAP3K2]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*72 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF195]] | -0.68 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[MAK16]] | -0.68 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ZNF239]] | -0.67 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.67 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[DDX21]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ZNF202]] | -0.65 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[DDX31]] | -0.65 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.64 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[WDR4]] | -0.64 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[GNL3L]] | -0.63 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[BYSL]] | -0.63 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[PUS1]] | -0.63 | -0.58 / -0.61 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAG1]] | B | PLAG1 activity lowers MPC2's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.48× higher at baseline in the lines without PLAG1 | 0.068 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.2, -35.8); signed map (-24.9, 17.0). **Vector** length 70.8, 15.9% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.9 | +6.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +2.9 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +7.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.1 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.9 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial pyruvate carrier 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:167,916,675-167,937,072 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564B167, SLC54A2; previously BRP44 |
| Gene groups (HGNC) | Solute carrier family 54, mitochondrial pyruvate carriers |
| Hallmark sets | DNA_REPAIR |
| Reactome | 2 pathways, smallest: Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95563](https://www.uniprot.org/uniprotkb/O95563) (Mitochondrial pyruvate carrier 2):

> Mediates the uptake of pyruvate into mitochondria to maintain the balance between glycolysis and oxidative phosphorylation. Plays an essential role in cellular metabolism.

**Summary**, from NCBI Gene [25874](https://www.ncbi.nlm.nih.gov/gene/25874):

> Enables identical protein binding activity. Involved in pyruvate import into mitochondria. Located in mitochondrial inner membrane. Part of mitochondrial pyruvate carrier complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24515) · Entrez [25874](https://www.ncbi.nlm.nih.gov/gene/25874) · UniProt [O95563](https://www.uniprot.org/uniprotkb/O95563) · Ensembl [ENSG00000143158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143158)

## Data

Gene col 6687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6687); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6687]; `tensor/DDL_lfc|DDL_z.npy` [6687]; `embed/gene_vectors.npy` [6687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6687 or target_col == 6687). Every well: [[MPC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
