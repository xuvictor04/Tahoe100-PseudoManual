---
symbol: "SNRPA1"
type: "gene"
col: 5255
ensembl_id: "ENSG00000131876"
name: "small nuclear ribonucleoprotein polypeptide A'"
location: "15q26.3"
module: 182
arm: "+"
pooled_cpm: 41.75
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# SNRPA1

*small nuclear ribonucleoprotein polypeptide A'* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.95× (z +8.7, q 1e-15, up in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.24× (z +8.1, q 2e-13, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Temsirolimus (drug)]] 0.05 µM: 0.755× (z -3.7, q 0.067, down in 16 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM1A]] (+0.76, fdr 7e-06), [[NDC1]] (+0.72, fdr 7e-06), [[PMS2P3]] (+0.72, fdr 7e-06); moves opposite to [[TUT7]] (-0.66, fdr 7e-06), [[ZNF674]] (-0.62, fdr 1e-05), [[GGPS1]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 182]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.7 | 1e-15 | 40/47 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +8.1 | 2e-13 | 45/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +7.2 | 8e-11 | 38/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.66×** | +6.7 | 3e-09 | 38/48 (KATO III, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +6.6 | 4e-09 | 35/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.45×** | +6.2 | 7e-08 | 27/35 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +5.1 | 3e-05 | 30/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +4.3 | 0.001 | 26/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +4.2 | 0.001 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.38×** | +4.2 | 0.001 | 24/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.013 | 20/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.020 | 21/48 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.020 | 20/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.30×** | +3.4 | 0.025 | 21/48 (NCI-H1792, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.035 | 19/49 (PANC-1, A-172, …) | top dose only | plate-row cell shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.041 | 16/49 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.045 | 15/48 (PANC-1, CHP-212, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.755×** | -3.7 | 0.067 | 16/48 (Panc 03.27, HOP62, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.759×** | -3.6 | 0.067 | 22/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.761×** | -3.6 | 0.067 | 20/48 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.769×** | -3.4 | 0.082 | 13/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -3.4 | 0.082 | 19/39 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.775× | -3.2 | 0.12 | 19/49 (NCI-H1792, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Entrectinib (drug)]] 5 µM |  | 0.792× | -3.1 | 0.18 | 11/48 (SNU-423, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.8 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.95× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +13.3) | — |
| [[LoVo (line)]] | wt | 59.9 | 3 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.83× (z +11.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -14.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 43.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 29.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.16× (z +9.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.207× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 53.9 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.12× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 58.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.103× (z -10.5) |
| [[KATO III (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 42.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | +0.76 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[NDC1]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[PMS2P3]] | +0.72 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.70 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[ALG9]] | +0.70 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[SNX4]] | +0.70 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[NUP54]] | +0.68 | +0.73 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SKP2]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[FOXJ3]] | +0.68 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[GCSH]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[TRIT1]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[RNF145]] | +0.65 | +0.76 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | -0.66 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[ZNF674]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[GGPS1]] | -0.61 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[SKIL]] | -0.61 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[C6orf62]] | -0.61 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[KDM6B]] | -0.61 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SP2]] | -0.60 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ZNF274]] | -0.59 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TFE3]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[BCL10]] | -0.59 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[SON]] | -0.59 | -0.65 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.7, -13.3); signed map (-34.5, -10.3). **Vector** length 91.8, 23.5% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.1 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.5 | +7.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +6.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.0 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.9 | +1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein polypeptide A' |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:101,281,510-101,295,282 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Lea1, U2A' |
| Gene groups (HGNC) | U2 small nuclear ribonucleoprotein |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 18 pathways, smallest: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P09661](https://www.uniprot.org/uniprotkb/P09661) (U2 small nuclear ribonucleoprotein A'):

> Involved in pre-mRNA splicing as component of the spliceosome. Associated with sn-RNP U2, where it contributes to the binding of stem loop IV of U2 snRNA.

**Summary**, from NCBI Gene [6627](https://www.ncbi.nlm.nih.gov/gene/6627):

> Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11152) · Entrez [6627](https://www.ncbi.nlm.nih.gov/gene/6627) · UniProt [P09661](https://www.uniprot.org/uniprotkb/P09661) · Ensembl [ENSG00000131876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131876)

## Data

Gene col 5255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5255); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5255]; `tensor/DDL_lfc|DDL_z.npy` [5255]; `embed/gene_vectors.npy` [5255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5255 or target_col == 5255). Every well: [[SNRPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
