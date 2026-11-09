---
symbol: "SKIC8"
type: "gene"
col: 6401
ensembl_id: "ENSG00000140395"
name: "SKI8 subunit of superkiller complex"
location: "15q25.1"
module: 49
arm: "+"
pooled_cpm: 28.9
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SKIC8

*SKI8 subunit of superkiller complex* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.83× (z +10.7, q 3e-24, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.721× (z -5.8, q 3e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL2]] (+0.64, fdr 1e-05), [[RARS1]] (+0.62, fdr 1e-05), [[ZCCHC17]] (+0.62, fdr 1e-05); moves opposite to [[KAT6A]] (-0.54, fdr 2e-05), [[TBL1XR1]] (-0.52, fdr 5e-05), [[GALNT7]] (-0.52, fdr 1e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +10.7 | 3e-24 | 37/48 (LoVo, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.83×** | +10.7 | 3e-24 | 42/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.80×** | +10.4 | 4e-23 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.68×** | +9.2 | 5e-18 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.56×** | +7.9 | 4e-13 | 32/44 (NCI-H23, SW480, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.40×** | +5.7 | 1e-06 | 28/46 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.40×** | +5.5 | 3e-06 | 22/41 (KATO III, A498, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.4 | 4e-06 | 23/48 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.37×** | +5.4 | 4e-06 | 19/36 (SHP-77, NCI-H460, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.4 | 5e-04 | 19/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.001 | 18/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +4.1 | 0.002 | 24/47 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.22×** | +3.5 | 0.016 | 19/45 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +3.5 | 0.016 | 17/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.037 | 12/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.051 | 5/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.721×** | -5.8 | 3e-06 | 31/48 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.805×** | -5.4 | 2e-05 | 21/48 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.522×** | -5.2 | 3e-05 | 26/48 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.555×** | -4.7 | 3e-04 | 27/48 (LOX-IMVI, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.799×** | -4.0 | 0.008 | 18/48 (H4, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.625×** | -3.8 | 0.014 | 15/47 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.834× | -3.1 | 0.14 | 10/47 (SK-MEL-2, hTERT-HPNE, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.681× | -3.1 | 0.14 | 8/48 (AN3 CA, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | 0.886× | -3.1 | 0.14 | 14/48 (HS-578T, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.52× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 24.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0679× (z -9.0) |
| [[A498 (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 42.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0977× (z -10.1) |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0661× (z -10.1) |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.405× (z -9.6) ⚠ cell-cycle shift, explains ~93% of this change |
| [[LoVo (line)]] | wt | 36.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +8.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0429× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 51.2 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0646× (z -9.9) |
| [[A-172 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL2]] | +0.64 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[RARS1]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZCCHC17]] | +0.62 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SLC30A6]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SEC13]] | +0.60 | +0.36 / +0.56 | both halves | 9e-05 | same gene group |
| [[MED8]] | +0.59 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[PSMD13]] | +0.59 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[NPRL2]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[GPR180]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ANKS3]] | +0.58 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[LTN1]] | +0.57 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[OXNAD1]] | +0.56 | +0.36 / +0.54 | both halves | 9e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT6A]] | -0.54 | -0.49 / -0.50 | both halves | 2e-05 |  |
| [[TBL1XR1]] | -0.52 | -0.40 / -0.55 | both halves | 5e-05 | same gene group |
| [[GALNT7]] | -0.52 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[RNF103]] | -0.52 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[PRRC2B]] | -0.51 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[FZD4-DT]] | -0.50 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[SIAH1]] | -0.50 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[BMPR1B]] | -0.50 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[ARAP2]] | -0.50 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[CAPN3]] | -0.49 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[DSC3]] | -0.49 | -0.20 / -0.43 | ⚠ not reproduced | 8e-04 |  |
| [[PSPC1]] | -0.48 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[HNRNPK-AS1]] | -0.48 | -0.41 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.1, -33.1); signed map (-45.1, 4.5). **Vector** length 81.3, 17.2% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | +10.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.6 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.4 | +10.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.3 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.1 | +10.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +4.2 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +1.6 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.4 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -4.6 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | SKI8 subunit of superkiller complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,277,835-78,299,703 (-) |
| Ensembl biotype | protein_coding |
| Also known as | REC14, SKI8; previously WDR61 |
| Gene groups (HGNC) | WD repeat domain containing; Paf1/RNA polymerase II complex ; SKI complex subunits |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Dengue virus activates/modulates innate and adaptive immune responses; E3 ubiquitin ligases ubiquitinate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZS3](https://www.uniprot.org/uniprotkb/Q9GZS3) (Superkiller complex protein 8):

> Component of the PAF1 complex (PAF1C) which has multiple functions during transcription by RNA polymerase II and is implicated in regulation of development and maintenance of embryonic stem cell pluripotency. PAF1C associates with RNA polymerase II through interaction with POLR2A CTD non-phosphorylated and 'Ser-2'- and 'Ser-5'-phosphorylated forms and is involved in transcriptional elongation, acting both independently and synergistically with TCEA1 and in cooperation with the DSIF complex and …

**Summary**, from NCBI Gene [80349](https://www.ncbi.nlm.nih.gov/gene/80349):

> WDR61 is a subunit of the human PAF and SKI complexes, which function in transcriptional regulation and are involved in events downstream of RNA synthesis, such as RNA surveillance (Zhu et al., 2005 [PubMed 16024656]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30300) · Entrez [80349](https://www.ncbi.nlm.nih.gov/gene/80349) · UniProt [Q9GZS3](https://www.uniprot.org/uniprotkb/Q9GZS3) · Ensembl [ENSG00000140395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140395)

## Data

Gene col 6401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6401); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6401]; `tensor/DDL_lfc|DDL_z.npy` [6401]; `embed/gene_vectors.npy` [6401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6401 or target_col == 6401). Every well: [[SKIC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKIC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
