---
symbol: "COX7B"
type: "gene"
col: 5182
ensembl_id: "ENSG00000131174"
name: "cytochrome c oxidase subunit 7B"
location: "Xq21.1"
module: 48
arm: "+"
pooled_cpm: 66.29
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# COX7B

*cytochrome c oxidase subunit 7B* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.12× (z +8.3, q 4e-14, up in 41 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +3.9, q 0.009, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HOP62 6.09×, C32 6.38×, A498 4.24×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 3.54×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 3.79×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA1]] (+0.75, fdr 7e-06), [[SERF2]] (+0.73, fdr 7e-06), [[ATP5MG]] (+0.72, fdr 7e-06); moves opposite to [[LAS1L]] (-0.61, fdr 1e-05), [[LSG1]] (-0.59, fdr 3e-05), [[EIF4G1]] (-0.59, fdr 7e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5182.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HOP62 6.09×, C32 6.38×, A498 4.24×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 3.54×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 3.79×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.12×** | +8.3 | 4e-14 | 41/42 (HOP62, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.89×** | +7.4 | 3e-11 | 47/48 (A549, HOP62, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.34×** | +5.8 | 1e-06 | 40/45 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.10×** | +5.7 | 2e-06 | 45/47 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.92×** | +5.0 | 7e-05 | 40/47 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.68×** | +4.0 | 0.006 | 39/48 (LoVo, SW480, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.009 | 32/48 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.57×** | +3.3 | 0.055 | 37/48 (SNU-423, HS-578T, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.57×** | +3.3 | 0.055 | 30/47 (C32, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.51×** | +3.1 | 0.094 | 30/48 (LoVo, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.53×** | +3.1 | 0.094 | 28/48 (NCI-H1573, SNU-423, …) | rises with dose | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.650× | -3.3 | 0.45 | 36/48 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.418× | -3.1 | 0.45 | 37/49 (HEC-1-A, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.653× | -3.0 | 0.45 | 30/48 (HEC-1-A, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 67.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.24× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[C32 (line)]] | wt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.38× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HOP62 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LoVo (line)]] | wt | 89.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.79× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H1792 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 117 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 82.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 15 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA1]] | +0.75 | +0.60 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 983 |
| [[SERF2]] | +0.73 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[ATP5MG]] | +0.72 | +0.64 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 786 |
| [[DPM3]] | +0.70 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[COX7A2]] ⚠ | +0.70 | +0.59 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 991; ⚠ in the vector space only through flagged drug-doses |
| [[MIF]] | +0.69 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[COX5A]] ⚠ | +0.69 | +0.63 / +0.68 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 995; ⚠ in the vector space only through flagged drug-doses |
| [[COX8A]] | +0.68 | +0.62 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 997 |
| [[FAU]] | +0.67 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[COX4I1]] ⚠ | +0.67 | +0.56 / +0.65 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1E]] | +0.67 | +0.57 / +0.69 | both halves | 9e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 669 |
| [[NDUFB11]] ⚠ | +0.67 | +0.56 / +0.63 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 959; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA3]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 930 |
| [[ROMO1]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[MIEN1]] | +0.65 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[RPS29]] | +0.65 | +0.46 / +0.68 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAS1L]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[LSG1]] | -0.59 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.59 | -0.38 / -0.61 | both halves | 7e-05 |  |
| [[ABCF2]] | -0.58 | -0.34 / -0.63 | both halves | 1e-04 | pathway: Cellular response to chemical stress |
| [[NPEPL1]] | -0.55 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[CCT2]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[RNPS1]] | -0.55 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[ANKRD40]] | -0.55 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[NOM1]] | -0.55 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[MAK16]] | -0.55 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[BRD9]] | -0.54 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[ZFP41]] | -0.54 | -0.28 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.2, -23.5); signed map (-35.0, 10.7). **Vector** length 58.3, 20.8% of its response variance represented; |z| ≥ 3 in 537 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.58 to 7); *Complex I biogenesis* (reactome, mean cos +0.51 to 9); *Cristae formation* (reactome, mean cos +0.58 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +2.9 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +2.6 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +2.5 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | -0.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -3.8 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -3.0 | +8.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -2.6 | +7.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | +0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:77,899,440-77,907,376 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P24311](https://www.uniprot.org/uniprotkb/P24311) (Cytochrome c oxidase subunit 7B, mitochondrial):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [1349](https://www.ncbi.nlm.nih.gov/gene/1349):

> Cytochrome c oxidase (COX), the terminal component of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. This component is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, and the nuclear-encoded subunits may function in the regulation and assembly of the complex. This nuclear …

**Accessions** — [HGNC:2291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2291) · Entrez [1349](https://www.ncbi.nlm.nih.gov/gene/1349) · UniProt [P24311](https://www.uniprot.org/uniprotkb/P24311) · Ensembl [ENSG00000131174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131174)

## Data

Gene col 5182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5182); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5182]; `tensor/DDL_lfc|DDL_z.npy` [5182]; `embed/gene_vectors.npy` [5182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5182 or target_col == 5182). Every well: [[COX7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
