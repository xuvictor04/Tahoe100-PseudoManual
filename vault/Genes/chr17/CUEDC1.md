---
symbol: "CUEDC1"
type: "gene"
col: 11143
ensembl_id: "ENSG00000180891"
name: "CUE domain containing 1"
location: "17q22"
module: 41
arm: "-"
pooled_cpm: 48.44
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# CUEDC1

*CUE domain containing 1* — 17q22

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 2.47×; ⚠ cell-cycle shift, explains ~63% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.246× (z -23.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUTM2B-AS1]] (+0.65, fdr 9e-06), [[SH3RF1]] (+0.61, fdr 1e-05), [[ANAPC7]] (+0.58, fdr 1e-05); moves opposite to [[PJA2]] (-0.61, fdr 1e-05), [[NPRL2]] (-0.61, fdr 3e-05), [[SUCO]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11143.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 2.47×; ⚠ cell-cycle shift, explains ~63% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.9 | 0.060 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.246×** | -23.0 | 0e+00 | 48/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.254×** | -22.5 | 0e+00 | 46/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.328×** | -18.3 | 0e+00 | 45/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -11.8 | 3e-30 | 39/48 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -7.9 | 2e-13 | 34/49 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.629×** | -7.6 | 3e-12 | 37/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.638×** | -7.4 | 1e-11 | 34/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.638×** | -7.1 | 8e-11 | 31/48 (COLO 205, LoVo, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.652×** | -6.8 | 8e-10 | 30/48 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.513×** | -5.7 | 5e-07 | 26/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.801×** | -5.2 | 1e-05 | 22/47 (A-427, SW1417, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.755×** | -4.4 | 4e-04 | 25/48 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.756×** | -4.4 | 4e-04 | 25/47 (C-33 A, LoVo, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.856× | -3.6 | 0.012 | 16/48 (A498, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.678×** | -3.3 | 0.031 | 17/48 (HS-578T, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.697×** | -3.1 | 0.059 | 18/47 (RPMI-7951, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.829×** | -3.0 | 0.081 | 9/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.882× | -2.9 | 0.092 | 9/48 (HS-578T, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 106 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -22.9) |
| [[KATO III (line)]] | alt | 57.1 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 80.4 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -17.7) |
| [[SNU-1 (line)]] | wt | 74.0 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -14.8) |
| [[SW1417 (line)]] | alt | 75.3 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -16.0) |
| [[HT-29 (line)]] | alt | 67.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 69.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -15.1) |
| [[A-172 (line)]] | wt | 37.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -14.0) |
| [[BT-474 (line)]] | alt | 91.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 75.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -15.1) |
| [[COLO 205 (line)]] | alt | 51.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.6) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -9.9) |
| [[HS-578T (line)]] | alt | 46.0 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.9) ⚠ cell-cycle shift, explains ~63% of this change | [[Panobinostat (drug)]] 5 µM 0.166× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 41.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.0) |
| [[RKO (line)]] | wt | 36.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.5) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.284× (z -9.2) |
| [[SW48 (line)]] | wt | 47.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0890× (z -13.6) |
| [[A498 (line)]] | wt | 55.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -13.2) |
| [[A549 (line)]] | wt | 57.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.214× (z -13.1) |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.125× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.239× (z -9.1) |
| [[C32 (line)]] | wt | 40.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -11.4) |
| [[HOP62 (line)]] | alt | 43.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -12.6) |
| [[J82 (line)]] | alt | 38.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -14.0) |
| [[LoVo (line)]] | wt | 29.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 52.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 44.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 40.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -15.4) |
| [[PANC-1 (line)]] | alt | 54.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -18.9) |
| [[SW480 (line)]] | alt | 50.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -19.8) |
| [[A-427 (line)]] | wt | 41.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -16.3) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H2030 (line)]] | alt | 53.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -13.3) |
| [[SHP-77 (line)]] | alt | 39.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -10.0) |
| [[SNU-423 (line)]] | alt | 54.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -10.1) |
| [[SW 900 (line)]] | alt | 46.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -10.2) |
| [[H4 (line)]] | wt | 34.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -8.6) |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -9.2) |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -11.0) |
| [[AN3 CA (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTM2B-AS1]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[SH3RF1]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[NUTM2A-AS1]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[FKRP]] | +0.57 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[FGF2]] | +0.56 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[WDR82]] | +0.56 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[EXOSC6]] | +0.54 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[ARSB]] | +0.54 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[DLG5]] | +0.54 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[RUFY3]] | +0.53 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[PPP6R2]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | -0.61 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[NPRL2]] | -0.61 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[SUCO]] | -0.60 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.60 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[MMUT]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[HELZ]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[GNAI3]] | -0.56 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[USP37]] | -0.55 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MXI1]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[APAF1]] | -0.55 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SMAP2]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RAB3A]] | -0.55 | -0.40 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.8, -16.7); signed map (20.9, -27.4). **Vector** length 94.5, 24.0% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.9 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +3.9 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.4 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -7.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.9 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -18.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -22.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -5.7 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | -2.3 | -2.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | CUE domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:57,861,243-57,955,412 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CUE domain containing |
| Matched by | ensembl_id |

UniProt [Q9NWM3](https://www.uniprot.org/uniprotkb/Q9NWM3) carries no function annotation.

**Summary**, from NCBI Gene [404093](https://www.ncbi.nlm.nih.gov/gene/404093):

> Predicted to enable ubiquitin binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31350) · Entrez [404093](https://www.ncbi.nlm.nih.gov/gene/404093) · UniProt [Q9NWM3](https://www.uniprot.org/uniprotkb/Q9NWM3) · Ensembl [ENSG00000180891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180891)

## Data

Gene col 11143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11143); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11143]; `tensor/DDL_lfc|DDL_z.npy` [11143]; `embed/gene_vectors.npy` [11143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11143 or target_col == 11143). Every well: [[CUEDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUEDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
