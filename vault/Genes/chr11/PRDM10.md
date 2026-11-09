---
symbol: "PRDM10"
type: "gene"
col: 9936
ensembl_id: "ENSG00000170325"
name: "PR/SET domain 10"
location: "11q24.3"
module: 15
arm: "+"
pooled_cpm: 39.93
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PRDM10

*PR/SET domain 10* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.40× (z +19.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.313× (z -18.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM15]] (+0.78, fdr 7e-06), [[HCFC1]] (+0.74, fdr 7e-06), [[TMEM11-DT]] (+0.70, fdr 1e-05); moves opposite to [[RP9]] (-0.71, fdr 7e-06), [[ZNF205]] (-0.68, fdr 1e-05), [[SNAPIN]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARL4D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +19.6 | 0e+00 | 48/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.24×** | +12.8 | 8e-35 | 47/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.04×** | +11.3 | 2e-27 | 46/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.00×** | +11.0 | 5e-26 | 45/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +10.6 | 3e-24 | 41/47 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.54×** | +6.8 | 8e-10 | 34/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.44×** | +5.8 | 5e-07 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +4.9 | 7e-05 | 25/47 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.6 | 3e-04 | 26/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +4.5 | 5e-04 | 23/48 (SW1417, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +4.2 | 0.001 | 22/48 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.001 | 21/48 (SW1417, Hs 766T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.25×** | +3.3 | 0.044 | 17/48 (C32, SNU-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.2 | 0.051 | 15/48 (NCI-H2030, HT-29, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.096 | 18/48 (NCI-H1573, A549, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.096 | 19/48 (LoVo, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.313×** | -18.4 | 0e+00 | 47/48 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.440×** | -18.4 | 0e+00 | 39/47 (SW 900, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.321×** | -18.0 | 0e+00 | 47/48 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.354×** | -16.4 | 0e+00 | 47/48 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.419×** | -12.9 | 5e-36 | 45/48 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.479×** | -11.6 | 3e-29 | 47/48 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -11.1 | 7e-27 | 37/47 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.546×** | -9.6 | 8e-20 | 43/48 (C-33 A, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.570×** | -8.9 | 4e-17 | 38/48 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.631×** | -6.8 | 5e-10 | 26/40 (Hs 766T, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.739×** | -6.8 | 7e-10 | 35/48 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.657×** | -6.6 | 1e-09 | 29/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.469×** | -6.1 | 4e-08 | 37/48 (AN3 CA, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -5.8 | 2e-07 | 31/48 (hTERT-HPNE, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.695×** | -5.7 | 3e-07 | 33/48 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.634×** | -3.7 | 0.007 | 19/48 (NCI-H23, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.856× | -3.4 | 0.017 | 20/48 (RKO, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 34.9 | 8 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.463× (z -8.8) |
| [[PANC-1 (line)]] | alt | 54.5 | 3 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -14.7) |
| [[LoVo (line)]] | wt | 43.5 | 5 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.375× (z -9.8) |
| [[A-427 (line)]] | wt | 31.5 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.7) |
| [[HT-29 (line)]] | alt | 38.8 | 3 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 78.8 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -17.2) |
| [[SW 900 (line)]] | alt | 36.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -19.9) |
| [[A-172 (line)]] | wt | 26.0 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.269× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 42.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.5) |
| [[KATO III (line)]] | alt | 57.5 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.299× (z -10.1) |
| [[LS 180 (line)]] | wt | 53.0 | 5 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.74× (z +18.6) | [[Belinostat (drug)]] 5 µM 0.349× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 31.6 | 2 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -13.2) |
| [[RKO (line)]] | wt | 77.0 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 27.3 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.5) |
| [[C-33 A (line)]] | alt | 53.3 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.161× (z -12.5) |
| [[C32 (line)]] | wt | 42.9 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +11.1) | [[Belinostat (drug)]] 5 µM 0.167× (z -14.2) |
| [[COLO 205 (line)]] | alt | 30.1 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.44× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.9 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 105 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.168× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 36.2 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.176× (z -12.8) |
| [[H4 (line)]] | wt | 39.0 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.1) |
| [[HOP62 (line)]] | alt | 29.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.342× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 46.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.302× (z -9.8) |
| [[SHP-77 (line)]] | alt | 31.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.92× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.70× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 30.3 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +16.9) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -11.7) |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -11.0) |
| [[SNU-1 (line)]] | wt | 66.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -12.0) |
| [[A498 (line)]] | wt | 26.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.307× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 21.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 30.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.0) | [[Belinostat (drug)]] 5 µM 0.363× (z -8.8) |
| [[Hs 766T (line)]] | wt | 40.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0666× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 26.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 29.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +16.5) | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 31.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0907× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.1) |
| [[SW48 (line)]] | wt | 57.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.1) |
| [[A549 (line)]] | wt | 26.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -8.9) |
| [[AN3 CA (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.120× (z -9.2) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 51.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -16.4) |
| [[HCT15 (line)]] | alt | 51.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.2) |
| [[J82 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.1) |
| [[SNU-423 (line)]] | alt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +13.7) | — |
| [[NCI-H2122 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM15]] | +0.78 | +0.73 / +0.64 | both halves | 7e-06 | same gene group |
| [[HCFC1]] | +0.74 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[TMEM11-DT]] | +0.70 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SLC25A53]] | +0.67 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[NR2C2]] | +0.67 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[METTL4]] | +0.66 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CDK2AP1]] | +0.64 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[WDR20]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.64 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[ZNF460-AS1]] | +0.63 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[MSL1]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[LEMD3]] | +0.61 | +0.51 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RP9]] | -0.71 | -0.81 / -0.58 | both halves | 7e-06 |  |
| [[ZNF205]] | -0.68 | -0.66 / -0.51 | both halves | 1e-05 | same gene group |
| [[SNAPIN]] | -0.67 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[MRPS31P4]] | -0.66 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[IFTAP]] | -0.65 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[CREB3]] | -0.62 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[GORAB]] | -0.62 | -0.78 / -0.62 | both halves | 7e-06 |  |
| [[ZNF45]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 | same gene group |
| [[NUDT12]] | -0.61 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[RIOK2]] | -0.61 | -0.72 / -0.53 | both halves | 1e-05 |  |
| [[POLM]] | -0.61 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[DHRS2]] | -0.60 | -0.40 / -0.59 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL4D]] | B | ARL4D activity lowers PRDM10's level | lines that do not express ARL4D (5) vs lines expressing it (45) | 1.85× higher at baseline in the lines without ARL4D | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, SOGA1, ELOVL5 |
| [[TOP2A]] | B | TOP2A activity lowers PRDM10's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NET1]] | C | NET1 activity lowers PRDM10's level | lines that do not express NET1 (4) vs lines expressing it (46) | 1.48× higher at baseline in the lines without NET1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NPEPPSP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.0, 19.9); signed map (5.8, -1.4). **Vector** length 119, 37.0% of its response variance represented; |z| ≥ 3 in 1,380 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +19.5 | +19.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.8 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +10.2 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.8 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +8.0 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +3.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.7 | -12.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -18.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -8.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -9.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:129,899,706-130,002,835 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1231, PFM7, MGC131802 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Putative lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQV6](https://www.uniprot.org/uniprotkb/Q9NQV6) (PR domain zinc finger protein 10):

> Transcriptional activator, essential for early embryonic development and survival of embryonic stem cells (ESCs) (By similarity). Supports cell growth and survival during early development by transcriptionally activating the expression of the translation initiation factor EIF3B, to sustain global translation (By similarity). Activates the transcription of FLNC.

**Summary**, from NCBI Gene [56980](https://www.ncbi.nlm.nih.gov/gene/56980):

> The protein encoded by this gene is a transcription factor that contains C2H2-type zinc-fingers. It also contains a positive regulatory domain, which has been found in several other zinc-finger transcription factors including those involved in B cell differentiation and tumor suppression. Studies of the mouse counterpart suggest that this protein may be involved in the development of the central nerve system (CNS), as well as in the pathogenesis of neuronal storage disease. Multiple …

**Accessions** — [HGNC:13995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13995) · Entrez [56980](https://www.ncbi.nlm.nih.gov/gene/56980) · UniProt [Q9NQV6](https://www.uniprot.org/uniprotkb/Q9NQV6) · Ensembl [ENSG00000170325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170325)

## Data

Gene col 9936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9936); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9936]; `tensor/DDL_lfc|DDL_z.npy` [9936]; `embed/gene_vectors.npy` [9936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9936 or target_col == 9936). Every well: [[PRDM10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
