---
symbol: "RAD52"
type: "gene"
col: 17
ensembl_id: "ENSG00000002016"
name: "RAD52 DNA repair protein"
location: "12p13.33"
module: 28
arm: "+"
pooled_cpm: 20.61
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# RAD52

*RAD52 DNA repair protein* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +18.4, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.585× (z -10.0, q 7e-21, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLK4]] (+0.74, fdr 7e-06), [[TRMT10B]] (+0.73, fdr 7e-06), [[GIN1]] (+0.71, fdr 2e-05); moves opposite to [[TPST2]] (-0.64, fdr 3e-05), [[BRI3BP]] (-0.62, fdr 4e-05), [[MAPKAPK2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 17.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +18.4 | 0e+00 | 41/47 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +10.0 | 3e-21 | 34/47 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +9.0 | 5e-17 | 31/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +7.0 | 3e-10 | 31/48 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +6.7 | 2e-09 | 28/48 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 3e-05 | 22/48 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.6 | 4e-04 | 15/48 (LoVo, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 4e-04 | 21/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.19× | +4.5 | 5e-04 | 18/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 8e-04 | 14/48 (KATO III, A-427, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +4.3 | 9e-04 | 15/48 (SW480, C32, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.3 | 1e-03 | 13/47 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.002 | 12/47 (NCI-H1573, A-172, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 10/47 (A498, SW 900, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +3.9 | 0.004 | 12/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.009 | 12/48 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.19× | +3.4 | 0.017 | 8/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.019 | 10/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 17.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.585×** | -10.0 | 7e-21 | 33/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.647×** | -8.2 | 1e-13 | 29/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.689×** | -7.0 | 5e-10 | 26/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.734×** | -5.8 | 1e-06 | 23/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -5.1 | 3e-05 | 22/47 (SW480, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.755×** | -5.1 | 4e-05 | 22/46 (A-172, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.774×** | -4.8 | 1e-04 | 15/48 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.795×** | -4.1 | 0.002 | 14/29 (KATO III, A-427, …) | rises with dose | composition shift |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.812×** | -3.9 | 0.006 | 12/48 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.682×** | -3.6 | 0.016 | 11/45 (SW48, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Rimonabant (drug)]] 5 µM |  | 0.887× | -3.2 | 0.075 | 6/48 (NCI-H1792, NCI-H661, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.0 | 0.13 | 11/47 (MIA PaCa-2, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 17. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.9 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.4) | [[Digitoxin (drug)]] 0.5 µM 0.356× (z -10.6) |
| [[A-427 (line)]] | wt | 75.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 14.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 17.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.412× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 35.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.7) | — |
| [[A-172 (line)]] | wt | 9.83 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.8) | — |
| [[KATO III (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LoVo (line)]] | wt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 58.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.5) | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 17), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK4]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.73 | +0.87 / +0.67 | both halves | 7e-06 |  |
| [[GIN1]] | +0.71 | +0.80 / +0.47 | both halves | 2e-05 |  |
| [[KCTD18]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[PEX12]] | +0.71 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[COQ5]] | +0.70 | +0.77 / +0.49 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.69 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[ZSCAN21]] | +0.69 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.69 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ZNF585A]] | +0.69 | +0.80 / +0.34 | both halves | 1e-04 |  |
| [[ARL14EP]] | +0.69 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[TCEANC]] | +0.69 | +0.74 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.64 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[BRI3BP]] | -0.62 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[MAPKAPK2]] | -0.62 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[FARP2]] | -0.61 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.61 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[GRK6]] | -0.60 | -0.63 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.836). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.9, 6.5); signed map (7.1, -22.8). **Vector** length 82.7, 15.7% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +18.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -10.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Rimonabant (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | RAD52 DNA repair protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:911,736-990,053 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | DNA_REPAIR |
| Reactome | 9 pathways, smallest: HDR through MMEJ (alt-NHEJ); HDR through Single Strand Annealing (SSA); SUMOylation of DNA damage response and repair proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P43351](https://www.uniprot.org/uniprotkb/P43351) (DNA repair protein RAD52 homolog):

> Involved in double-stranded break repair. Plays a central role in genetic recombination and DNA repair by promoting the annealing of complementary single-stranded DNA and by stimulation of the RAD51 recombinase.

**Summary**, from NCBI Gene [5893](https://www.ncbi.nlm.nih.gov/gene/5893):

> The protein encoded by this gene shares similarity with Saccharomyces cerevisiae Rad52, a protein important for DNA double-strand break repair and homologous recombination. This gene product was shown to bind single-stranded DNA ends, and mediate the DNA-DNA interaction necessary for the annealing of complementary DNA strands. It was also found to interact with DNA recombination protein RAD51, which suggested its role in RAD51 related DNA recombination and repair. A pseudogene of this gene is …

**Accessions** — [HGNC:9824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9824) · Entrez [5893](https://www.ncbi.nlm.nih.gov/gene/5893) · UniProt [P43351](https://www.uniprot.org/uniprotkb/P43351) · Ensembl [ENSG00000002016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000002016)

## Data

Gene col 17: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 17); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 17, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 17]; `tensor/DDL_lfc|DDL_z.npy` [17]; `embed/gene_vectors.npy` [17]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 17 or target_col == 17). Every well: [[RAD52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
