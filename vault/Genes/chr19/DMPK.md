---
symbol: "DMPK"
type: "gene"
col: 2525
ensembl_id: "ENSG00000104936"
name: "DM1 protein kinase"
location: "19q13.32"
module: 38
arm: "+"
pooled_cpm: 24.86
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# DMPK

*DM1 protein kinase* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +8.2, q 2e-13, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.664× (z -10.6, q 2e-23, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRK]] (+0.67, fdr 7e-06), [[TTLL3]] (+0.66, fdr 7e-06), [[SEC16A]] (+0.64, fdr 1e-05); moves opposite to [[CISD2]] (-0.61, fdr 1e-05), [[TMEM106B]] (-0.58, fdr 1e-05), [[LANCL1]] (-0.57, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +8.2 | 2e-13 | 28/47 (A549, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.53×** | +7.7 | 4e-12 | 29/48 (HEC-1-A, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.39×** | +6.0 | 4e-07 | 27/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +5.3 | 1e-05 | 25/46 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.30×** | +4.6 | 5e-04 | 19/43 (NCI-H2030, C32, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +4.6 | 5e-04 | 21/47 (NCI-H1792, HOP62, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.29×** | +4.4 | 8e-04 | 19/48 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.27×** | +4.4 | 8e-04 | 18/48 (HOP62, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.27×** | +4.4 | 8e-04 | 17/46 (HOP62, SW480, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.18× | +4.2 | 0.001 | 8/48 (J82, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.26×** | +4.2 | 0.001 | 17/47 (HOP62, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.1 | 0.002 | 13/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.24×** | +3.9 | 0.004 | 19/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.004 | 15/45 (A549, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.23×** | +3.8 | 0.007 | 13/47 (SNU-1, HOP62, …) | rises with dose |  |
| [[Lucanthone (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.008 | 11/48 (LoVo, NCI-H2347, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.010 | 6/46 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.014 | 13/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.028 | 9/48 (SK-MEL-2, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.031 | 8/48 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.037 | 9/45 (HCT15, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.664×** | -10.6 | 2e-23 | 38/48 (Hs 766T, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.746×** | -5.4 | 2e-05 | 21/42 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.752×** | -5.0 | 1e-04 | 25/47 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 0.865× | -3.8 | 0.023 | 12/48 (AN3 CA, NCI-H1792, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.818×** | -3.5 | 0.044 | 17/47 (HOP62, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.813×** | -3.4 | 0.069 | 17/37 (SW 900, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.829× | -3.0 | 0.16 | 12/47 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Bexarotene (drug)]] 5 µM |  | 0.848× | -3.0 | 0.16 | 6/48 (hTERT-HPNE, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 33.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 26.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.67× (z +8.6) ⚠ cell-cycle shift, explains ~16% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -13.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.262× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -8.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 19.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.229× (z -11.2) |
| [[KATO III (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 17.6 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.141× (z -8.6) |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0742× (z -15.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRK]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SEC16A]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[FBXL18]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[KCNJ14]] | +0.62 | +0.56 / +0.69 | both halves | 1e-05 | pathway: Cardiac conduction |
| [[ORAI2]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 | pathway: Cardiac conduction |
| [[ATP2A1]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MYOGENESIS; STRING 754 |
| [[UCKL1-AS1]] | +0.60 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[SPRED3]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PHKG2]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CHMP1A]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PILRA]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CISD2]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TMEM106B]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.57 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[FBXO7]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ZNF326]] | -0.56 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[TRUB1]] | -0.56 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[RPP30]] | -0.56 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TRAPPC11]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[MTX2]] | -0.56 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[PYURF]] | -0.55 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[MRS2]] | -0.55 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[MATR3]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.1, -20.7); signed map (11.1, 12.7). **Vector** length 92.9, 18.8% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.6 | +3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.6 | +3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +2.4 | +4.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.6 | -10.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Bexarotene (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | DM1 protein kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,769,709-45,782,552 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DMK, DM1PK, MDPK, MT-PK; previously DM1, DM |
| Gene groups (HGNC) | DMPK kinase family |
| Hallmark sets | MYOGENESIS |
| Reactome | 3 pathways, smallest: Ion homeostasis; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q09013](https://www.uniprot.org/uniprotkb/Q09013) (Myotonin-protein kinase):

> Non-receptor serine/threonine protein kinase which is necessary for the maintenance of skeletal muscle structure and function. May play a role in myocyte differentiation and survival by regulating the integrity of the nuclear envelope and the expression of muscle-specific genes. May also phosphorylate PPP1R12A and inhibit the myosin phosphatase activity to regulate myosin phosphorylation. Also critical to the modulation of cardiac contractility and to the maintenance of proper cardiac …

**Summary**, from NCBI Gene [1760](https://www.ncbi.nlm.nih.gov/gene/1760):

> The protein encoded by this gene is a serine-threonine kinase that is closely related to other kinases that interact with members of the Rho family of small GTPases. Substrates for this enzyme include myogenin, the beta-subunit of the L-type calcium channels, and phospholemman. The 3' untranslated region of this gene contains 5-38 copies of a CTG trinucleotide repeat. Expansion of this unstable motif to 50-5,000 copies causes myotonic dystrophy type I, which increases in severity with …

**Accessions** — [HGNC:2933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2933) · Entrez [1760](https://www.ncbi.nlm.nih.gov/gene/1760) · UniProt [Q09013](https://www.uniprot.org/uniprotkb/Q09013) · Ensembl [ENSG00000104936](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104936)

## Data

Gene col 2525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2525); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2525]; `tensor/DDL_lfc|DDL_z.npy` [2525]; `embed/gene_vectors.npy` [2525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2525 or target_col == 2525). Every well: [[DMPK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMPK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
