---
symbol: "ELOVL6"
type: "gene"
col: 9968
ensembl_id: "ENSG00000170522"
name: "ELOVL fatty acid elongase 6"
location: "4q25"
module: 74
arm: "+"
pooled_cpm: 41.59
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 25
n_dd_up_clean: 8
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# ELOVL6

*ELOVL fatty acid elongase 6* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.19× (z +18.4, q 0e+00, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.463× (z -18.1, q 0e+00, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMPS]] (+0.59, fdr 1e-05), [[BEND3]] (+0.59, fdr 1e-05), [[TBXAS1]] (+0.59, fdr 3e-05); moves opposite to [[PRMT2]] (-0.57, fdr 3e-05), [[RANBP10]] (-0.56, fdr 3e-05), [[CRBN]] (-0.56, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADAMTS9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +18.4 | 0e+00 | 38/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.39×** | +7.7 | 4e-12 | 29/47 (HEC-1-A, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.37×** | +5.0 | 9e-05 | 23/45 (A-172, RPMI-7951, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.24×** | +4.9 | 1e-04 | 20/48 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.30×** | +4.3 | 0.002 | 21/44 (A-172, SNU-423, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +3.9 | 0.011 | 17/45 (LoVo, A-172, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.7 | 0.017 | 19/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.26×** | +3.6 | 0.020 | 18/40 (A-172, H4, …) | two highest doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.25×** | +3.6 | 0.023 | 19/46 (A-172, C32, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.037 | 16/46 (NCI-H2347, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.039 | 13/46 (NCI-H2347, A549, …) | all doses, flat |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.039 | 13/46 (HEC-1-A, A498, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.063 | 12/46 (A549, CFPAC-1, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.063 | 16/46 (A498, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9968.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.463×** | -18.1 | 0e+00 | 36/46 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.516×** | -11.0 | 1e-25 | 40/47 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -10.8 | 6e-25 | 35/45 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -10.7 | 2e-24 | 35/47 (RKO, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.574×** | -9.2 | 3e-18 | 34/47 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.583×** | -9.0 | 2e-17 | 31/46 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.618×** | -8.0 | 9e-14 | 28/47 (RKO, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.633×** | -7.2 | 4e-11 | 35/46 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -6.7 | 1e-09 | 26/45 (HepG2/C3A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -6.3 | 2e-08 | 30/47 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -5.8 | 3e-07 | 24/45 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.534×** | -5.5 | 2e-06 | 26/44 (SW480, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.740×** | -4.9 | 3e-05 | 24/47 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -4.7 | 1e-04 | 21/45 (NCI-H1573, SW 900, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.787×** | -4.6 | 2e-04 | 22/47 (SK-MEL-2, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.686×** | -4.5 | 3e-04 | 24/46 (CFPAC-1, LoVo, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.781×** | -4.1 | 0.001 | 23/46 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.807×** | -3.6 | 0.010 | 16/45 (J82, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 39.4 | 8 | 1 | [[Dexamethasone (drug)]] 0.05 µM 3.39× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.9) |
| [[RKO (line)]] | wt | 130 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0785× (z -22.3) |
| [[A-172 (line)]] | wt | 31.5 | 6 (4 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 32.1 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -19.6) |
| [[A498 (line)]] | wt | 70.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -18.7) |
| [[COLO 205 (line)]] | alt | 55.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -18.8) |
| [[J82 (line)]] | alt | 66.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -12.1) |
| [[KATO III (line)]] | alt | 61.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -10.7) |
| [[LoVo (line)]] | wt | 17.8 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 39.3 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 40.6 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +15.3) | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 73.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -13.8) |
| [[SW480 (line)]] | alt | 32.9 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -13.9) |
| [[BT-474 (line)]] | alt | 41.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.224× (z -9.2) ⚠ cell-cycle shift, explains ~10% of this change |
| [[HEC-1-A (line)]] | alt | 73.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 84.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -16.1) |
| [[SHP-77 (line)]] | alt | 60.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.211× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -20.1) |
| [[SW1417 (line)]] | alt | 18.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 26.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 39.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 43.4 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.13× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.282× (z -10.3) |
| [[SNU-1 (line)]] | wt | 91.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.297× (z -8.8) |
| [[SW48 (line)]] | wt | 48.5 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.239× (z -8.9) |
| [[A-427 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -11.2) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 39.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 47.8 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0942× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 33.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 64.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -10.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 35.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.193× (z -9.1) |
| [[HS-578T (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0581× (z -26.8) |
| [[HT-29 (line)]] | alt | 40.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 37.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 54.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMPS]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[BEND3]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[TBXAS1]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 | pathway: Fatty acid metabolism |
| [[PTPRG]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SUV39H2]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[FADS2]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 703 |
| [[LAMB1]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[NME1]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ADCY3]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TMEM181]] | +0.55 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[PPIA]] | +0.53 | +0.37 / +0.51 | both halves | 7e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ATP1A1]] | +0.53 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT2]] | -0.57 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[RANBP10]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[CRBN]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TBC1D17]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[UBXN1]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[UBE2B]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[DENND6B]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[DNAL4]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[CCDC127]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZSCAN16]] | -0.52 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[ASB8]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS9]] | B | ADAMTS9 activity raises ELOVL6's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without ADAMTS9 | 0.031 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[TOP2A]] | B | TOP2A activity lowers ELOVL6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction -0.532). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.8, -49.5); signed map (0.7, 14.2). **Vector** length 117, 32.7% of its response variance represented; |z| ≥ 3 in 1,466 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +18.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.9 | +5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.1 | +7.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.8 | +3.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.5 | +4.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -18.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -4.4 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -4.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -3.5 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ELOVL fatty acid elongase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:110,045,846-110,199,199 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23378, MGC5487, LCE |
| Gene groups (HGNC) | ELOVL fatty acid elongase family |
| Hallmark sets | ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5J4](https://www.uniprot.org/uniprotkb/Q9H5J4) (Very long chain fatty acid elongase 6):

> Catalyzes the first and rate-limiting reaction of the four reactions that constitute the long-chain fatty acids elongation cycle. This endoplasmic reticulum-bound enzymatic process allows the addition of 2 carbons to the chain of long- and very long-chain fatty acids (VLCFAs) per cycle. Condensing enzyme that elongates fatty acids with 12, 14 and 16 carbons with higher activity toward C16:0 acyl-CoAs. Catalyzes the synthesis of unsaturated C16 long chain fatty acids and, to a lesser extent, …

**Summary**, from NCBI Gene [79071](https://www.ncbi.nlm.nih.gov/gene/79071):

> Fatty acid elongases (EC 6.2.1.3), such as ELOVL6, use malonyl-CoA as a 2-carbon donor in the first and rate-limiting step of fatty acid elongation (Moon et al., 2001 [PubMed 11567032]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:15829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15829) · Entrez [79071](https://www.ncbi.nlm.nih.gov/gene/79071) · UniProt [Q9H5J4](https://www.uniprot.org/uniprotkb/Q9H5J4) · Ensembl [ENSG00000170522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170522)

## Data

Gene col 9968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9968); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9968]; `tensor/DDL_lfc|DDL_z.npy` [9968]; `embed/gene_vectors.npy` [9968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9968 or target_col == 9968). Every well: [[ELOVL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOVL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
