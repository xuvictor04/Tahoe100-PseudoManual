---
symbol: "TIMM50"
type: "gene"
col: 2559
ensembl_id: "ENSG00000105197"
name: "translocase of inner mitochondrial membrane 50"
location: "19q13.2"
module: 33
arm: "+"
pooled_cpm: 26.58
n_lines_expressing: 49
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TIMM50

*translocase of inner mitochondrial membrane 50* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +11.0, q 2e-25, up in 33 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.81× (z +7.2, q 4e-11, up in 35 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0745×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPOUT1]] (+0.63, fdr 9e-06), [[RRP1]] (+0.61, fdr 2e-05), [[HSPBP1]] (+0.61, fdr 7e-06); moves opposite to [[GNAS]] (-0.55, fdr 3e-05), [[SMIM14]] (-0.50, fdr 3e-04), [[YBX1]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.98×** | +11.0 | 2e-25 | 33/38 (NCI-H460, SW480, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.14×** | +9.3 | 4e-18 | 41/46 (SW480, HT-29, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.04×** | +8.7 | 6e-16 | 40/46 (SW480, HT-29, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.04×** | +8.7 | 6e-16 | 35/45 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.97×** | +8.2 | 2e-14 | 32/46 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.38×** | +7.7 | 1e-12 | 19/27 (KATO III, LoVo, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.94×** | +7.4 | 1e-11 | 28/31 (PANC-1, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.81×** | +7.2 | 4e-11 | 38/46 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +7.2 | 4e-11 | 35/46 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +6.5 | 5e-09 | 28/45 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +6.2 | 2e-08 | 37/46 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +5.9 | 1e-07 | 30/46 (PANC-1, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.6 | 1e-06 | 24/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +5.5 | 1e-06 | 24/42 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.56×** | +5.4 | 2e-06 | 28/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +4.2 | 9e-04 | 18/45 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.004 | 16/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.00×** | +3.7 | 0.005 | 12/45 (PANC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.006 | 17/45 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.58×** | +3.3 | 0.020 | 12/45 (NCI-H460, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.74×** | +3.0 | 0.055 | 7/44 (PANC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.72×** | +2.9 | 0.065 | 7/43 (PANC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.72×** | +2.9 | 0.065 | 4/45 (PANC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.48×** | +2.9 | 0.074 | 5/45 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +2.8 | 0.092 | 14/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2559.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0745×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 0.814× | -3.3 | 0.25 | 13/47 (hTERT-HPNE, A-427, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.762× | -3.3 | 0.25 | 14/45 (KATO III, SW480, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 5 µM |  | 0.838× | -3.1 | 0.33 | 15/47 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -3.0 | 0.33 | 15/47 (NCI-H2347, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 237 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0745× (z -9.4) |
| [[HS-578T (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOUT1]] | +0.63 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[RRP1]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[HSPBP1]] | +0.61 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[MRPL4]] | +0.60 | +0.37 / +0.68 | both halves | 7e-05 |  |
| [[TRMT61A]] | +0.59 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CLUH]] | +0.58 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[MCAT]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[TIMM8A]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 | pathway: Mitochondrial protein import; STRING 784 |
| [[SMG5]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[NOC4L]] | +0.57 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[E2F4]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[POLR1A]] | +0.56 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SMIM14]] | -0.50 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[YBX1]] | -0.47 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[TXNDC16]] | -0.47 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[LNX2]] | -0.47 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[CLK1]] | -0.46 | -0.49 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.9, -40.3); signed map (1.4, -46.7). **Vector** length 47.5, 7.93% of its response variance represented; |z| ≥ 3 in 707 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +2.7 | +7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.4 | +8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.3 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +2.3 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +5.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.6 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 50 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,480,412-39,493,785 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIM50L, TIM50 |
| Gene groups (HGNC) | CTD family phosphatases |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3ZCQ8](https://www.uniprot.org/uniprotkb/Q3ZCQ8) (Mitochondrial import inner membrane translocase subunit TIM50):

> Essential component of the TIM23 complex, a complex that mediates the translocation of transit peptide-containing proteins across the mitochondrial inner membrane. Has some phosphatase activity in vitro; however such activity may not be relevant in vivo.; [Isoform 2]: May participate in the release of snRNPs and SMN from the Cajal body.

**Summary**, from NCBI Gene [92609](https://www.ncbi.nlm.nih.gov/gene/92609):

> This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of this gene in human cells results in the release of cytochrome c and apoptosis. [provided by RefSeq, …

**Accessions** — [HGNC:23656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23656) · Entrez [92609](https://www.ncbi.nlm.nih.gov/gene/92609) · UniProt [Q3ZCQ8](https://www.uniprot.org/uniprotkb/Q3ZCQ8) · Ensembl [ENSG00000105197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105197)

## Data

Gene col 2559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2559); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2559]; `tensor/DDL_lfc|DDL_z.npy` [2559]; `embed/gene_vectors.npy` [2559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2559 or target_col == 2559). Every well: [[TIMM50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
