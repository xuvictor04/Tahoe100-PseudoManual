---
symbol: "LRIG2"
type: "gene"
col: 12683
ensembl_id: "ENSG00000198799"
name: "leucine rich repeats and immunoglobulin like domains 2"
location: "1p13.2"
module: 65
arm: "+"
pooled_cpm: 50.97
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# LRIG2

*leucine rich repeats and immunoglobulin like domains 2* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 2.57× (z +6.5, q 5e-08, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.300× (z -17.4, q 0e+00, down in 42 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.478× (z -10.6, q 3e-24, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG9]] (+0.74, fdr 7e-06), [[ANAPC4]] (+0.72, fdr 7e-06), [[DUSP11]] (+0.71, fdr 7e-06); moves opposite to [[CHD4]] (-0.63, fdr 1e-05), [[LINC01934]] (-0.60, fdr 1e-05), [[CCDC144CP]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +6.5 | 5e-08 | 37/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +4.9 | 3e-04 | 30/49 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | 1.24× | +3.1 | 0.36 | 19/48 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12683.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.300×** | -17.4 | 0e+00 | 42/46 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.326×** | -14.9 | 0e+00 | 39/42 (Hs 766T, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.353×** | -14.4 | 6e-45 | 39/41 (Hs 766T, A498, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.478×** | -10.6 | 3e-24 | 46/48 (SNU-423, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -5.2 | 2e-05 | 30/48 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.814×** | -4.2 | 0.002 | 25/48 (AsPC-1, A498, …) | top dose only | composition shift |
| [[Thymol (drug)]] 5 µM |  | **0.815×** | -4.2 | 0.002 | 26/48 (LOX-IMVI, Hs 766T, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.786×** | -3.2 | 0.093 | 16/48 (NCI-H1792, MIA PaCa-2, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.861× | -3.1 | 0.14 | 12/48 (LS 180, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 67.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -9.1) |
| [[A-172 (line)]] | wt | 47.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0836× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.407× (z -10.5) |
| [[A498 (line)]] | wt | 59.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0704× (z -22.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 42.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -8.9) |
| [[HS-578T (line)]] | alt | 73.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.3) ⚠ cell-cycle shift, explains ~88% of this change |
| [[NCI-H2347 (line)]] | alt | 51.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -9.1) |
| [[PANC-1 (line)]] | alt | 39.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -14.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 45.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -17.6) ⚠ cell-cycle shift, explains ~88% of this change |
| [[HCT15 (line)]] | alt | 93.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -13.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 72.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -15.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 64.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0467× (z -25.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 43.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.1) ⚠ cell-cycle shift, explains ~88% of this change |
| [[J82 (line)]] | alt | 41.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -14.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 46.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 57.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -16.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 82.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 48.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.7) ⚠ cell-cycle shift, explains ~88% of this change |
| [[NCI-H2030 (line)]] | alt | 59.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -14.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 44.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -10.5) |
| [[C-33 A (line)]] | alt | 65.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -11.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 37.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.325× (z -8.8) |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 2 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.101× (z -8.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Berbamine (drug)]] 0.5 µM 0.102× (z -8.7) |
| [[HT-29 (line)]] | alt | 37.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.281× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 48.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 49.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 42.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -9.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 61.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -10.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 72.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -8.6) |
| [[SNU-423 (line)]] | alt | 40.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.214× (z -12.0) |
| [[SW48 (line)]] | wt | 48.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -9.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -18.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 77.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0723× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -13.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 94.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0663× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG9]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ANAPC4]] | +0.72 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[DUSP11]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[MTX2]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[C12orf76]] | +0.70 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[PRMT9]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NDUFB7]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[MMS19]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[MED23]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TADA1]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD4]] | -0.63 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[LINC01934]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CCDC144CP]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[DDX5]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PARD6G-AS1]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.57 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[GNG4]] | -0.57 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[THOC6]] | -0.57 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[LARGE1]] | -0.57 | -0.63 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.788). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.7, -10.6); signed map (-30.6, -12.1). **Vector** length 93.5, 24.7% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.6 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -7.3 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and immunoglobulin like domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:113,073,198-113,132,260 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0806 |
| Gene groups (HGNC) | I-set domain containing |
| Matched by | ensembl_id |

UniProt [O94898](https://www.uniprot.org/uniprotkb/O94898) carries no function annotation.

**Summary**, from NCBI Gene [9860](https://www.ncbi.nlm.nih.gov/gene/9860):

> This gene encodes a transmembrane protein containing leucine-rich repeats and immunoglobulin-like domains. The encoded protein promotes epidermal growth factor signalling, resulting in increased proliferation. Its expression in the cytoplasm of glioma cells is correlated with poor survival. Mutations in this gene can cause urofacial syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:20889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20889) · Entrez [9860](https://www.ncbi.nlm.nih.gov/gene/9860) · UniProt [O94898](https://www.uniprot.org/uniprotkb/O94898) · Ensembl [ENSG00000198799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198799)

## Data

Gene col 12683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12683); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12683]; `tensor/DDL_lfc|DDL_z.npy` [12683]; `embed/gene_vectors.npy` [12683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12683 or target_col == 12683). Every well: [[LRIG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRIG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
