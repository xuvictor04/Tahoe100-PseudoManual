---
symbol: "TRIM39"
type: "gene"
col: 12897
ensembl_id: "ENSG00000204599"
name: "tripartite motif containing 39"
location: "6p22.1"
module: 38
arm: "+"
pooled_cpm: 19.72
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# TRIM39

*tripartite motif containing 39* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +13.1, q 1e-36, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.569× (z -10.7, q 9e-24, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RECQL5]] (+0.75, fdr 7e-06), [[LRRC41]] (+0.69, fdr 3e-05), [[SLC9A5]] (+0.69, fdr 1e-05); moves opposite to [[SOAT1]] (-0.63, fdr 1e-05), [[STX7]] (-0.60, fdr 5e-05), [[METAP1]] (-0.60, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +13.1 | 1e-36 | 35/46 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.007 | 12/48 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.013 | 12/45 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.3 | 0.12 | 6/47 (J82, NCI-H460, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.18 | 2/47 (CFPAC-1, BT-474) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12897.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -10.7 | 9e-24 | 38/47 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -10.0 | 3e-21 | 29/46 (C32, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.589×** | -10.0 | 3e-21 | 37/48 (J82, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.693×** | -9.8 | 2e-20 | 40/48 (J82, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.609×** | -9.4 | 9e-19 | 36/48 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.644×** | -8.3 | 8e-15 | 32/48 (J82, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.748×** | -5.5 | 4e-06 | 23/47 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.768×** | -5.0 | 5e-05 | 17/46 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.771×** | -4.9 | 6e-05 | 22/47 (NCI-H2347, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.771×** | -4.5 | 3e-04 | 16/38 (A549, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.805×** | -4.1 | 0.002 | 20/43 (A-427, COLO 205, …) | inconsistent across doses | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.868× | -3.8 | 0.008 | 13/48 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.820×** | -3.7 | 0.008 | 16/47 (RPMI-7951, SW48, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.696×** | -3.6 | 0.014 | 12/48 (NCI-H23, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.821×** | -3.4 | 0.022 | 6/47 (NCI-H1573, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.838× | -3.3 | 0.030 | 8/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.065 | 11/46 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.850× | -2.9 | 0.088 | 15/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 36.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -11.2) |
| [[A-427 (line)]] | wt | 23.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[A549 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0861× (z -9.2) |
| [[C32 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.168× (z -9.0) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 9.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 1 | — | [[PH-797804 (drug)]] 0.05 µM 0.153× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H1573 (line)]] | alt | 39.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[NCI-H460 (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.257× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.3) | — |
| [[A498 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL5]] | +0.75 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[LRRC41]] | +0.69 | +0.44 / +0.71 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SLC9A5]] | +0.69 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | +0.66 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[STK19]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ACAD9]] | +0.66 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[ZNF432]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[ARMC5]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ZKSCAN5]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 | STRING 429 |
| [[SPAG7]] | +0.62 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[ZNF335]] | +0.62 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[C6orf62]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOAT1]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[STX7]] | -0.60 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[METAP1]] | -0.60 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[PPP1CC]] | -0.58 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SLC23A2]] | -0.58 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[HMGN3]] | -0.58 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[MNAT1]] | -0.57 | -0.31 / -0.59 | both halves | 2e-04 | same gene group |
| [[KDM1A]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ATP5F1C]] | -0.56 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[BTBD3]] | -0.56 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ATP8A1]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[RAB4A]] | -0.56 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.2, 18.6); signed map (6.8, 0.7). **Vector** length 86.2, 16.5% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.5 | +13.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +0.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.2 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -9.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -10.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:30,326,479-30,343,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RNF23 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCM9](https://www.uniprot.org/uniprotkb/Q9HCM9) (E3 ubiquitin-protein ligase TRIM39):

> [Isoform 1]: E3 ubiquitin-protein ligase. May facilitate apoptosis by inhibiting APC/C-Cdh1-mediated poly-ubiquitination and subsequent proteasome-mediated degradation of the pro-apoptotic protein MOAP1. Regulates the G1/S transition of the cell cycle and DNA damage-induced G2 arrest by stabilizing CDKN1A/p21. Positively regulates CDKN1A/p21 stability by competing with DTL for CDKN1A/p21 binding, therefore disrupting DCX(DTL) E3 ubiquitin ligase complex-mediated CDKN1A/p21 ubiquitination and …

**Summary**, from NCBI Gene [56658](https://www.ncbi.nlm.nih.gov/gene/56658):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The function of this protein has not been identified. This gene lies within the major histocompatibility complex class I region on chromosome 6. Alternate splicing results in two transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10065) · Entrez [56658](https://www.ncbi.nlm.nih.gov/gene/56658) · UniProt [Q9HCM9](https://www.uniprot.org/uniprotkb/Q9HCM9) · Ensembl [ENSG00000204599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204599)

## Data

Gene col 12897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12897); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12897]; `tensor/DDL_lfc|DDL_z.npy` [12897]; `embed/gene_vectors.npy` [12897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12897 or target_col == 12897). Every well: [[TRIM39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
