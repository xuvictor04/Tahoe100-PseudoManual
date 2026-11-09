---
symbol: "TRMT10B"
type: "gene"
col: 9099
ensembl_id: "ENSG00000165275"
name: "tRNA methyltransferase 10B"
location: "9p13.2"
module: 28
arm: "+"
pooled_cpm: 20.39
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TRMT10B

*tRNA methyltransferase 10B* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +10.0, q 6e-21, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.608× (z -11.8, q 2e-29, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD52]] (+0.73, fdr 7e-06), [[SNHG11]] (+0.71, fdr 7e-06), [[MRPL58]] (+0.71, fdr 7e-06); moves opposite to [[MLEC]] (-0.63, fdr 7e-06), [[TMED4]] (-0.63, fdr 7e-06), [[TMBIM6]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +10.0 | 6e-21 | 30/45 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +9.8 | 3e-20 | 36/45 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +8.4 | 1e-14 | 30/45 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 5e-06 | 22/45 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +5.2 | 3e-05 | 20/46 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.004 | 10/45 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.15× | +3.4 | 0.062 | 7/46 (J82, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.076 | 12/45 (J82, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9099.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -11.8 | 2e-29 | 36/46 (SNU-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.541×** | -10.3 | 2e-22 | 30/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.579×** | -9.2 | 8e-18 | 33/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -9.0 | 5e-17 | 36/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -7.2 | 7e-11 | 27/46 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -6.9 | 4e-10 | 27/43 (SK-MEL-2, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -5.9 | 4e-07 | 24/43 (PANC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.683×** | -5.7 | 9e-07 | 22/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.729×** | -5.1 | 2e-05 | 18/44 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.743×** | -5.0 | 4e-05 | 24/45 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.752×** | -4.3 | 0.001 | 12/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.790×** | -3.9 | 0.004 | 13/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.870× | -3.3 | 0.041 | 6/46 (Hs 766T, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.808×** | -3.2 | 0.058 | 13/45 (J82, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -3.1 | 0.083 | 0/46 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 42.3 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -17.5) |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -10.4) |
| [[SW480 (line)]] | alt | 29.5 | 2 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.70× (z +9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.189× (z -14.7) |
| [[KATO III (line)]] | alt | 33.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.209× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 44.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.3) | [[TAK-901 (drug)]] 5 µM 0.0985× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 22.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +16.6) | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +15.9) | — |
| [[NCI-H460 (line)]] | wt | 18.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -8.9) |
| [[A-172 (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0642× (z -12.4) |
| [[Hs 766T (line)]] | wt | 34.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -8.7) |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.225× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.184× (z -8.5) ⚠ toxic |
| [[J82 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.474× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0842× (z -19.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 8.80 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.95× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 24.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.5) |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD52]] | +0.73 | +0.87 / +0.67 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.71 | +0.81 / +0.58 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[TMEM42]] | +0.71 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[LIPT1]] | +0.70 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.70 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[CHURC1]] | +0.69 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.69 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[SPG11]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[MKS1]] | +0.69 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[CLK4]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 | STRING 807 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLEC]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[TMED4]] | -0.63 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[TMBIM6]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.60 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.60 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[CDK2]] | -0.59 | -0.70 / -0.45 | both halves | 3e-05 |  |
| [[BCAP31]] | -0.59 | -0.65 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-29.4, 5.6); signed map (5.4, -22.1). **Vector** length 94.9, 20.9% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -11.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -9.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.3 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.8 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 10B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:37,753,803-37,778,972 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31455, bA3J10.9; previously RG9MTD3 |
| Gene groups (HGNC) | SPOUT methyltransferase domain containing; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PF06](https://www.uniprot.org/uniprotkb/Q6PF06) (tRNA methyltransferase 10 homolog B):

> S-adenosyl-L-methionine-dependent guanine N(1)-methyltransferase that catalyzes the formation of N(1)-methylguanine at position 9 (m1G9) in tRNAs. Probably not able to catalyze formation of N(1)-methyladenine at position 9 (m1A9) in tRNAs.

**Summary**, from NCBI Gene [158234](https://www.ncbi.nlm.nih.gov/gene/158234):

> Enables tRNA (guanosine(9)-N1)-methyltransferase activity. Involved in protein insertion into mitochondrial inner membrane. Located in cytosol and mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26454) · Entrez [158234](https://www.ncbi.nlm.nih.gov/gene/158234) · UniProt [Q6PF06](https://www.uniprot.org/uniprotkb/Q6PF06) · Ensembl [ENSG00000165275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165275)

## Data

Gene col 9099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9099); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9099]; `tensor/DDL_lfc|DDL_z.npy` [9099]; `embed/gene_vectors.npy` [9099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9099 or target_col == 9099). Every well: [[TRMT10B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT10B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
