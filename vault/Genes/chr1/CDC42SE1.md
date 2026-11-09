---
symbol: "CDC42SE1"
type: "gene"
col: 12434
ensembl_id: "ENSG00000197622"
name: "CDC42 small effector 1"
location: "1q21.3"
module: 57
arm: "-"
pooled_cpm: 38.0
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# CDC42SE1

*CDC42 small effector 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.96× (z +11.1, q 1e-25, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.683× (z -6.3, q 1e-07, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC9B]] (+0.50, fdr 4e-05), [[VHL]] (+0.49, fdr 6e-05), [[IRGQ]] (+0.48, fdr 3e-05); moves opposite to [[IFT172]] (-0.50, fdr 3e-05), [[POT1]] (-0.47, fdr 5e-05), [[MIGA1]] (-0.47, fdr 3e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +11.1 | 1e-25 | 38/47 (SW480, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +8.6 | 2e-15 | 37/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +7.7 | 4e-12 | 34/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.58×** | +7.5 | 1e-11 | 28/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.53×** | +6.7 | 3e-09 | 26/39 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.9 | 4e-07 | 30/47 (SW1417, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +5.3 | 1e-05 | 27/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.35×** | +5.0 | 5e-05 | 28/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.34×** | +4.7 | 2e-04 | 24/47 (A-172, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.38×** | +4.5 | 4e-04 | 20/42 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 4e-04 | 26/48 (NCI-H2030, CFPAC-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.33×** | +4.4 | 4e-04 | 24/47 (NCI-H2030, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +4.3 | 7e-04 | 22/48 (HepG2/C3A, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.28×** | +4.0 | 0.002 | 19/48 (A498, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.26×** | +3.8 | 0.005 | 20/46 (HEC-1-A, A549, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.024 | 16/46 (C32, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.024 | 12/48 (A549, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.024 | 20/47 (HEC-1-A, SW 900, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.026 | 13/48 (SW480, HEC-1-A, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.033 | 13/47 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.033 | 8/46 (NCI-H2030, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +2.8 | 0.096 | 10/47 (SW 900, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12434.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.683×** | -6.3 | 1e-07 | 28/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.771×** | -4.3 | 0.004 | 22/48 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.619×** | -3.5 | 0.082 | 20/46 (C32, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.781× | -3.4 | 0.10 | 18/48 (NCI-H1573, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -3.2 | 0.15 | 21/47 (RKO, NCI-H460, …) | top dose only | composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.829× | -3.2 | 0.15 | 12/48 (SW480, A-427, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.829× | -3.0 | 0.18 | 15/47 (NCI-H1573, SW 1271, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.807× | -3.0 | 0.18 | 14/48 (NCI-H1573, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 78.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.51× (z +8.8) | — |
| [[A498 (line)]] | wt | 63.3 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 27.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 64.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.307× (z -10.9) |
| [[SW480 (line)]] | alt | 30.0 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.13× (z +11.7) | — |
| [[A-427 (line)]] | wt | 60.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 45.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.40× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.148× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 62.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.75× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 33.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.199× (z -9.0) |
| [[SW 900 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC9B]] | +0.50 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[VHL]] | +0.49 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[IRGQ]] | +0.48 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[GABBR1]] | +0.48 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[ARRDC1-AS1]] | +0.47 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[RBPMS2]] | +0.47 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[CD2BP2]] | +0.46 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[AP5B1]] | +0.46 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[SLC36A1]] | +0.46 | +0.41 / +0.38 | both halves | 6e-05 |  |
| [[ARFRP1]] | +0.46 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[CDKN1A]] | +0.45 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[PVR]] | +0.45 | +0.47 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[POT1]] | -0.47 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[MIGA1]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[COPB1]] | -0.46 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[EIF2AK1]] | -0.45 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[USP48]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PDXDC2P]] | -0.44 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[PRPF3]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[MNS1]] | -0.42 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[HEATR5B]] | -0.42 | -0.45 / -0.20 | both halves | 7e-04 |  |
| [[ANAPC5]] | -0.42 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[GUSBP1]] | -0.42 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.347). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.8, 9.7); signed map (2.9, 3.3). **Vector** length 88.1, 20.7% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +11.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.8 | +3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.5 | +5.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.4 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.0 | +2.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.7 | -6.3 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -3.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 small effector 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,050,971-151,070,325 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCIP1, SPEC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRR8](https://www.uniprot.org/uniprotkb/Q9NRR8) (CDC42 small effector protein 1):

> Probably involved in the organization of the actin cytoskeleton by acting downstream of CDC42, inducing actin filament assembly. Alters CDC42-induced cell shape changes. In activated T-cells, may play a role in CDC42-mediated F-actin accumulation at the immunological synapse. May play a role in early contractile events in phagocytosis in macrophages.

**Summary**, from NCBI Gene [56882](https://www.ncbi.nlm.nih.gov/gene/56882):

> Predicted to enable GTPase inhibitor activity. Predicted to be involved in signal transduction. Located in cell junction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17719) · Entrez [56882](https://www.ncbi.nlm.nih.gov/gene/56882) · UniProt [Q9NRR8](https://www.uniprot.org/uniprotkb/Q9NRR8) · Ensembl [ENSG00000197622](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197622)

## Data

Gene col 12434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12434); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12434]; `tensor/DDL_lfc|DDL_z.npy` [12434]; `embed/gene_vectors.npy` [12434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12434 or target_col == 12434). Every well: [[CDC42SE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42SE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
