---
symbol: "TMEM164"
type: "gene"
col: 8087
ensembl_id: "ENSG00000157600"
name: "transmembrane protein 164"
location: "Xq23"
module: 97
arm: "+"
pooled_cpm: 67.02
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# TMEM164

*transmembrane protein 164* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Budesonide (drug)]] 5 µM: 1.28× (z +4.3, q 0.012, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.357× (z -25.1, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP1A1]] (+0.65, fdr 7e-06), [[TBC1D8]] (+0.62, fdr 7e-06), [[TBXAS1]] (+0.62, fdr 2e-05); moves opposite to [[SLC41A2]] (-0.61, fdr 7e-06), [[ZNF624]] (-0.53, fdr 2e-05), [[ADAMTS16]] (-0.53, fdr 2e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.012 | 24/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.066 | 20/48 (HS-578T, H4, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.075 | 21/48 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.20× | +3.2 | 0.18 | 19/48 (HS-578T, H4, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.357×** | -25.1 | 0e+00 | 45/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -14.4 | 3e-44 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.423×** | -14.2 | 9e-44 | 42/48 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -10.0 | 2e-21 | 43/49 (AN3 CA, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.551×** | -9.9 | 6e-21 | 33/41 (NCI-H23, LS 180, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.550×** | -9.8 | 1e-20 | 36/48 (NCI-H23, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.548×** | -9.6 | 8e-20 | 35/43 (hTERT-HPNE, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -9.2 | 2e-18 | 39/48 (LOX-IMVI, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.614×** | -8.4 | 3e-15 | 39/48 (AsPC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.642×** | -7.6 | 1e-12 | 36/48 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.642×** | -7.3 | 2e-11 | 32/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.731×** | -5.4 | 3e-06 | 30/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -5.1 | 2e-05 | 24/49 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.746×** | -5.0 | 2e-05 | 28/48 (SK-MEL-2, SW48, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.757×** | -4.8 | 6e-05 | 24/48 (SW48, KATO III, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.788×** | -4.1 | 0.001 | 25/49 (SW1417, HOP62, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.793×** | -4.0 | 0.002 | 23/48 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.793×** | -3.8 | 0.004 | 19/47 (H4, NCI-H23, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.674×** | -3.6 | 0.010 | 21/48 (LS 180, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 40.9 | 16 | 1 (1 ⚠) | [[Budesonide (drug)]] 5 µM 4.51× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 78.9 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -35.2) |
| [[LOX-IMVI (line)]] | wt | 87.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 249 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -20.8) |
| [[SW480 (line)]] | alt | 58.7 | 1 (1 ⚠) | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -19.8) |
| [[LS 180 (line)]] | wt | 91.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -22.8) |
| [[NCI-H23 (line)]] | alt | 80.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -24.4) |
| [[NCI-H460 (line)]] | wt | 78.5 | 1 (1 ⚠) | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -24.3) |
| [[C32 (line)]] | wt | 55.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -18.1) |
| [[KATO III (line)]] | alt | 73.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -19.3) |
| [[LoVo (line)]] | wt | 94.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0766× (z -22.1) |
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.5) |
| [[NCI-H1573 (line)]] | alt | 77.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0936× (z -27.8) |
| [[NCI-H2030 (line)]] | alt | 78.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -18.5) |
| [[RKO (line)]] | wt | 44.7 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0933× (z -28.9) |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -11.5) |
| [[SW1417 (line)]] | alt | 85.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -11.3) |
| [[SW48 (line)]] | wt | 62.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -18.0) |
| [[H4 (line)]] | wt | 63.7 | 0 | 3 (1 ⚠) | — | [[OTS514 (drug)]] 5 µM 0.0682× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 29.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 32.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 40.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 32.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -12.5) |
| [[A-427 (line)]] | wt | 35.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 106 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.0305× (z -11.0) |
| [[C-33 A (line)]] | alt | 41.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.100× (z -15.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.8) |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.0937× (z -9.3) |
| [[COLO 205 (line)]] | alt | 55.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -21.0) |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.1) |
| [[HOP62 (line)]] | alt | 52.7 | 1 | 1 | [[Dexamethasone (drug)]] 0.5 µM 2.48× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -9.9) |
| [[Hs 766T (line)]] | wt | 90.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.1) |
| [[SNU-423 (line)]] | alt | 90.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.6) |
| [[A-172 (line)]] | wt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.2) |
| [[A549 (line)]] | wt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -14.7) |
| [[BT-474 (line)]] | alt | 42.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.8) |
| [[HT-29 (line)]] | alt | 64.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 38.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 71.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -9.4) |
| [[SHP-77 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 43.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.0) |
| [[SW 900 (line)]] | alt | 46.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.5) |
| [[A498 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1A1]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TBC1D8]] | +0.62 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[TBXAS1]] | +0.62 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[LDLRAD3]] | +0.61 | +0.67 / +0.58 | both halves | 7e-06 | same gene group |
| [[FAM135A]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PXYLP1]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PHKA1]] | +0.59 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[LAMB1]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[FKBP5]] | +0.56 | +0.48 / +0.49 | both halves | 2e-05 | same gene group; pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[TOP1]] | +0.56 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[MAP3K6]] | +0.55 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[B3GNT5]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC41A2]] | -0.61 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[ZNF624]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ADAMTS16]] | -0.53 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[HMGN2P46]] | -0.53 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[PER3]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SYTL2]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[TEF]] | -0.51 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MARCKS]] | -0.51 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[TP53BP1]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[GORAB]] | -0.50 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[MSANTD3]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[KIAA1217]] | -0.49 | -0.53 / -0.43 | both halves | 3e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises TMEM164's level | compounds that target NR3C1: 2 of 3 raise it (Budesonide, Dexamethasone) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds |
| [[KIAA1217]] | B | KIAA1217 activity raises TMEM164's level | lines that do not express KIAA1217 (10) vs lines expressing it (40) | 1.41× lower at baseline in the lines without KIAA1217 | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM107B, MET, S100A16 |
| [[IL18R1]] | B | IL18R1 activity raises TMEM164's level | lines that do not express IL18R1 (15) vs lines expressing it (35) | 1.25× lower at baseline in the lines without IL18R1 | 0.083 | ⚠ within organs, on part of the lines; also absent: JCAD |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.3, 13.7); signed map (16.7, 34.3). **Vector** length 113, 33.4% of its response variance represented; |z| ≥ 3 in 1,391 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dexamethasone (drug)]] 0.5 µM |  | +5.3 | +3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +5.2 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +5.1 | +3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +5.0 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.8 | -25.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.4 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -9.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 164 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:110,002,631-110,182,734 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22679, RP13-360B22.2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5U3C3](https://www.uniprot.org/uniprotkb/Q5U3C3) (Transmembrane protein 164):

> Positive regulator of ferroptosis. Involved in the acylation of ether lysophospholipids with the arachidonoyl chain (5Z,8Z,11Z,14Z-eicosatetraenoyl; C20:4) of diacylglycerophospholipids, generating C20:4 ether glycerophospholipids (ePEs) such as 1-(1Z-octadecenyl)-2-(5Z,8Z,11Z,14Z-eicosatetraenoyl)-sn-glycero-3-phosphoethanolamine (PE (P-18:0/20:4)), which promotes ferroptosis. Selectively mediates ATG5-dependent autophagosome formation during ferroptosis, rather than during starvation, and …

**Summary**, from NCBI Gene [84187](https://www.ncbi.nlm.nih.gov/gene/84187):

> Involved in positive regulation of ferroptosis. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26217) · Entrez [84187](https://www.ncbi.nlm.nih.gov/gene/84187) · UniProt [Q5U3C3](https://www.uniprot.org/uniprotkb/Q5U3C3) · Ensembl [ENSG00000157600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157600)

## Data

Gene col 8087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8087); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8087]; `tensor/DDL_lfc|DDL_z.npy` [8087]; `embed/gene_vectors.npy` [8087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8087 or target_col == 8087). Every well: [[TMEM164 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM164.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
