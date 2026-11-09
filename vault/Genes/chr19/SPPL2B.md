---
symbol: "SPPL2B"
type: "gene"
col: 74
ensembl_id: "ENSG00000005206"
name: "signal peptide peptidase like 2B"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 16.37
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SPPL2B

*signal peptide peptidase like 2B* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.98× (z +13.0, q 1e-35, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.643× (z -8.4, q 2e-14, down in 29 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.466× (z -7.6, q 8e-12, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHTF18]] (+0.60, fdr 1e-04), [[RER1]] (+0.59, fdr 1e-05), [[CDK5RAP3]] (+0.59, fdr 1e-05); moves opposite to [[ABRACL]] (-0.50, fdr 1e-04), [[DPH6-DT]] (-0.45, fdr 0.003, ⚠ not reproduced), [[SUCLG2-DT]] (-0.44, fdr 6e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 74.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +13.0 | 1e-35 | 44/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +11.0 | 7e-26 | 40/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +10.7 | 1e-24 | 34/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.6 | 1e-15 | 12/27 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.3 | 3e-11 | 19/40 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +4.8 | 2e-04 | 18/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.25×** | +4.3 | 0.002 | 15/47 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.002 | 8/44 (LoVo, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.22×** | +3.7 | 0.013 | 9/47 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.013 | 6/43 (PANC-1, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.028 | 7/45 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.4 | 0.028 | 7/33 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.030 | 9/43 (SHP-77, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.1 | 0.067 | 12/47 (NCI-H1792, C32, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.067 | 3/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.067 | 8/46 (A-172, A498, …) | all doses, flat |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.085 | 5/47 (NCI-H2347, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 74.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -8.4 | 2e-14 | 29/46 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -7.6 | 8e-12 | 29/44 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -6.8 | 2e-09 | 24/48 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -5.8 | 1e-06 | 22/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.741×** | -5.7 | 1e-06 | 23/46 (NCI-H2030, A549, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.741×** | -5.7 | 1e-06 | 18/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.825×** | -5.2 | 2e-05 | 16/48 (NCI-H1792, H4, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.761×** | -5.0 | 4e-05 | 17/43 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -4.2 | 0.002 | 15/47 (C32, SHP-77, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.804×** | -4.2 | 0.002 | 18/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.813×** | -3.8 | 0.008 | 18/47 (SW 900, NCI-H2030, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.822×** | -3.5 | 0.020 | 15/47 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.840× | -3.3 | 0.038 | 18/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.891× | -3.1 | 0.073 | 13/48 (LS 180, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 74. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 13.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.134× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 8.56 | 0 | 2 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0941× (z -10.7) ⚠ transcription drop · without an alert: [[Pyridoxine (hydrochloride) (drug)]] 5 µM 0.257× (z -8.7) |
| [[A-427 (line)]] | wt | 19.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0921× (z -9.1) |
| [[HCT15 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0854× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0998× (z -12.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A-172 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 74), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHTF18]] | +0.60 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[RER1]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CDK5RAP3]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[RHPN1]] | +0.58 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[CEP131]] | +0.58 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[UVSSA]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[CDK10]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CPSF1]] | +0.57 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[INTS1]] | +0.55 | +0.26 / +0.48 | both halves | 3e-04 |  |
| [[RHOT2]] | +0.54 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[LRCH4]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MATCAP1]] | +0.53 | +0.27 / +0.47 | both halves | 3e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABRACL]] | -0.50 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[DPH6-DT]] | -0.45 | -0.08 / -0.43 | ⚠ not reproduced | 0.003 |  |
| [[SUCLG2-DT]] | -0.44 | -0.23 / -0.40 | both halves | 6e-04 |  |
| [[SMIM10L1]] | -0.43 | -0.32 / -0.19 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.478). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.6, -25.9); signed map (-50.0, -0.6). **Vector** length 60.8, 8.64% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +13.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +11.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.2 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.1 | +3.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +0.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.9 | -5.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -7.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | signal peptide peptidase like 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,328,615-2,355,095 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IMP4, PSL1, KIAA1532 |
| Gene groups (HGNC) | Signal peptide peptidase like family |
| Reactome | 3 pathways, smallest: Regulation of TNFR1 signaling; TNF signaling; Death Receptor Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCT7](https://www.uniprot.org/uniprotkb/Q8TCT7) (Signal peptide peptidase-like 2B):

> Intramembrane-cleaving aspartic protease (I-CLiP) that cleaves type II membrane signal peptides in the hydrophobic plane of the membrane. Functions in ITM2B and TNF processing. Catalyzes the intramembrane cleavage of the anchored fragment of shed TNF (TNF), which promotes the release of the intracellular domain (ICD) for signaling to the nucleus. May play a role in the regulation of innate and adaptive immunity. Catalyzes the intramembrane cleavage of the simian foamy virus processed leader …

**Summary**, from NCBI Gene [56928](https://www.ncbi.nlm.nih.gov/gene/56928):

> This gene encodes a member of the GXGD family of aspartic proteases. The GXGD proteases are transmembrane proteins with two conserved catalytic motifs localized within the membrane-spanning regions. This enzyme localizes to endosomes, lysosomes, and the plasma membrane. It cleaves the transmembrane domain of tumor necrosis factor alpha to release the intracellular domain, which triggers cytokine expression in the innate and adaptive immunity pathways. Multiple transcript variants encoding …

**Accessions** — [HGNC:30627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30627) · Entrez [56928](https://www.ncbi.nlm.nih.gov/gene/56928) · UniProt [Q8TCT7](https://www.uniprot.org/uniprotkb/Q8TCT7) · Ensembl [ENSG00000005206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005206)

## Data

Gene col 74: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 74); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 74, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 74]; `tensor/DDL_lfc|DDL_z.npy` [74]; `embed/gene_vectors.npy` [74]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 74 or target_col == 74). Every well: [[SPPL2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPPL2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
