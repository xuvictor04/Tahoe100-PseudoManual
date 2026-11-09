---
symbol: "MRPL49"
type: "gene"
col: 7409
ensembl_id: "ENSG00000149792"
name: "mitochondrial ribosomal protein L49"
location: "11q13.1"
module: 7
arm: "+"
pooled_cpm: 14.03
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MRPL49

*mitochondrial ribosomal protein L49* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.97× (z +12.0, q 3e-30, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.835× (z -4.5, q 0.004, down in 14 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERAL1]] (+0.66, fdr 1e-05), [[RBM22]] (+0.63, fdr 1e-05), [[PRKAB1]] (+0.62, fdr 1e-05); moves opposite to [[NME2]] (-0.52, fdr 2e-05), [[TOMM20]] (-0.51, fdr 3e-05), [[LRRC75A]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.97×** | +12.0 | 3e-30 | 40/46 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +11.4 | 9e-28 | 33/46 (LS 180, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +11.3 | 3e-27 | 33/40 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +9.5 | 4e-19 | 29/46 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.69×** | +9.3 | 3e-18 | 33/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.62×** | +8.5 | 1e-15 | 21/36 (J82, PANC-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +7.4 | 8e-12 | 29/46 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +7.4 | 1e-11 | 23/47 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +7.0 | 1e-10 | 26/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.49×** | +6.8 | 8e-10 | 14/25 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 1e-08 | 23/47 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.43×** | +5.9 | 2e-07 | 15/29 (Hs 766T, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +5.6 | 1e-06 | 23/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +4.9 | 3e-05 | 16/45 (A498, A549, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.8 | 8e-05 | 16/48 (LOX-IMVI, RKO, …) | rises with dose | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +3.9 | 0.002 | 15/48 (A549, PANC-1, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.015 | 10/41 (NCI-H23, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.019 | 3/45 (KATO III, BT-474, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.032 | 7/43 (PANC-1, A498, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.068 | 4/44 (HS-578T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -4.5 | 0.004 | 14/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.777×** | -4.3 | 0.005 | 14/46 (J82, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.796×** | -4.0 | 0.011 | 19/47 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.820×** | -3.5 | 0.064 | 17/47 (NCI-H2030, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.828×** | -3.3 | 0.092 | 6/48 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 0.833× | -3.2 | 0.11 | 13/43 (LoVo, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.837× | -3.2 | 0.13 | 22/46 (SHP-77, SW 900, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 13.8 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0901× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 6.86 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0539× (z -9.7) |
| [[LoVo (line)]] | wt | 8.96 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 9.41 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0646× (z -11.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW480 (line)]] | alt | 14.4 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.67× (z +8.8) | — |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERAL1]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 | pathway: Mitochondrial ribosome-associated quality control |
| [[RBM22]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[PRKAB1]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[PPIE]] | +0.62 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[C8orf33]] | +0.62 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[PARP3]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ACTR8]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[PEF1]] | +0.61 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[AUP1]] | +0.61 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[CCDC90B]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ZNF564]] | +0.60 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[MDM2]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME2]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TOMM20]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[LRRC75A]] | -0.49 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[UQCRH]] | -0.49 | -0.55 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MRPL49's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-34.6, 15.5); signed map (4.7, -30.4). **Vector** length 83.1, 15.4% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +11.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.7 | +6.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +5.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.5 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.4 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L49 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,122,183-65,127,371 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NOF, NOF1, L49mt, mL49; previously C11orf4 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q13405](https://www.uniprot.org/uniprotkb/Q13405) carries no function annotation.

**Summary**, from NCBI Gene [740](https://www.ncbi.nlm.nih.gov/gene/740):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:1176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1176) · Entrez [740](https://www.ncbi.nlm.nih.gov/gene/740) · UniProt [Q13405](https://www.uniprot.org/uniprotkb/Q13405) · Ensembl [ENSG00000149792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149792)

## Data

Gene col 7409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7409); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7409]; `tensor/DDL_lfc|DDL_z.npy` [7409]; `embed/gene_vectors.npy` [7409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7409 or target_col == 7409). Every well: [[MRPL49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
