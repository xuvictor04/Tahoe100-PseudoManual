---
symbol: "CAMSAP1-DT"
type: "gene"
col: 14166
ensembl_id: "ENSG00000238058"
name: "CAMSAP1 divergent transcript"
location: "9q34.3"
module: 38
arm: "+"
pooled_cpm: 8.38
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CAMSAP1-DT

*CAMSAP1 divergent transcript* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.38× (z +10.3, q 4e-22, up in 8 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Abiraterone acetate (drug)]] 0.05 µM: 1.35× (z +3.7, q 0.027, up in 8 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.467× (z -9.4, q 3e-18, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Simotinib (drug)]] 0.05 µM: 0.732× (z -3.6, q 0.023, down in 18 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC22A20P]] (+0.57, fdr 1e-05), [[KCTD13]] (+0.57, fdr 1e-05), [[LINC02614]] (+0.56, fdr 2e-05); moves opposite to [[PIK3R1]] (-0.49, fdr 5e-05), [[PRELID2]] (-0.49, fdr 3e-05), [[CEP295]] (-0.48, fdr 4e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +10.3 | 4e-22 | 8/15 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.7 | 3e-06 | 17/29 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.25×** | +4.0 | 0.013 | 9/47 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.027 | 8/47 (NCI-H460, J82, …) | inconsistent across doses | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.027 | 5/48 (SW1417, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.046 | 6/48 (SHP-77, NCI-H2347, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.049 | 12/46 (SW480, SNU-1, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.19× | +3.1 | 0.14 | 10/44 (RPMI-7951, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14166.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.467×** | -9.4 | 3e-18 | 36/47 (J82, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.595×** | -9.1 | 3e-17 | 33/45 (SK-MEL-2, HS-578T, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.591×** | -6.3 | 7e-08 | 22/46 (HEC-1-A, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.620×** | -5.9 | 5e-07 | 25/44 (NCI-H23, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.663×** | -5.1 | 4e-05 | 21/47 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.694×** | -4.5 | 6e-04 | 20/47 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.709×** | -4.3 | 0.002 | 18/47 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.727×** | -3.9 | 0.006 | 12/43 (HEC-1-A, A498, …) | rises with dose |  |
| [[Simotinib (drug)]] 0.05 µM |  | **0.732×** | -3.6 | 0.023 | 18/44 (PANC-1, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.765×** | -3.3 | 0.054 | 9/44 (BT-474, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.607×** | -3.2 | 0.060 | 11/36 (SHP-77, A549, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.773×** | -3.2 | 0.060 | 14/46 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.761×** | -3.2 | 0.060 | 12/46 (A-172, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.773×** | -3.2 | 0.060 | 4/48 (SW 1088, KATO III, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.782×** | -3.0 | 0.089 | 12/41 (HS-578T, SNU-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 8.88 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -10.3) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.118× (z -9.7) |
| [[A-172 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[AsPC-1 (line)]] | alt | 8.30 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0989× (z -9.7) |
| [[C-33 A (line)]] | alt | 9.38 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0919× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.7) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HS-578T (line)]] | alt | 5.55 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -11.0) ⚠ cell-cycle shift, explains ~65% of this change |
| [[LOX-IMVI (line)]] | wt | 9.76 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.0) ⚠ cell-cycle shift, explains ~65% of this change |
| [[LS 180 (line)]] | wt | 4.53 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.106× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 4.55 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0929× (z -10.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0658× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 9.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.5) ⚠ cell-cycle shift, explains ~65% of this change |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[SW480 (line)]] | alt | 7.25 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0600× (z -9.1) |
| [[A-427 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC22A20P]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[KCTD13]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LINC02614]] | +0.56 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[GATD1-DT]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 | same gene group |
| [[QRICH2]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[TECPR2]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[SLC23A3]] | +0.53 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[LINC00205]] | +0.52 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CROCCP3-1]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[GHRLOS]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[GNB1]] | +0.50 | +0.37 / +0.49 | both halves | 7e-05 |  |
| [[ZNF514]] | +0.50 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3R1]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[PRELID2]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CEP295]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[HOXA13]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[NFIA]] | -0.46 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[ALDH9A1]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ZNF608]] | -0.46 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[PIK3C2B]] | -0.45 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[FSBP]] | -0.45 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[CYC1]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[CXXC5]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[MEF2C]] | -0.43 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.295). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, 1.4); signed map (2.7, 8.7). **Vector** length 56.4, 7.29% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.5 | -9.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.1 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.0 | -6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | CAMSAP1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q34.3 — chr9:135,907,812-135,916,126 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55648) · Entrez [107987141](https://www.ncbi.nlm.nih.gov/gene/107987141) · Ensembl [ENSG00000238058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238058)

## Data

Gene col 14166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14166); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14166]; `tensor/DDL_lfc|DDL_z.npy` [14166]; `embed/gene_vectors.npy` [14166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14166 or target_col == 14166). Every well: [[CAMSAP1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMSAP1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
