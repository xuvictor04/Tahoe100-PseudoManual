---
symbol: "ADI1"
type: "gene"
col: 11299
ensembl_id: "ENSG00000182551"
name: "acireductone dioxygenase 1"
location: "2p25.3"
module: 154
arm: "+"
pooled_cpm: 25.7
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# ADI1

*acireductone dioxygenase 1* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.80× (z +26.0, q 0e+00, up in 40 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +8.7, q 5e-16, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.486× (z -12.0, q 2e-30, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB2]] (+0.65, fdr 2e-05), [[NNT]] (+0.63, fdr 3e-05), [[ZMYND11]] (+0.62, fdr 2e-05); moves opposite to [[EPN2]] (-0.64, fdr 3e-05), [[CIB1]] (-0.63, fdr 9e-05), [[UBA6]] (-0.63, fdr 7e-05).
> It is in [[Module 154]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.80×** | +26.0 | 0e+00 | 40/40 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.50×** | +24.0 | 0e+00 | 32/32 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.80×** | +20.5 | 0e+00 | 35/36 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.7 | 5e-16 | 28/47 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +7.9 | 5e-13 | 33/44 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +7.4 | 2e-11 | 29/44 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.2 | 5e-08 | 25/48 (A-172, A549, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.74×** | +4.8 | 1e-04 | 19/45 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.4 | 6e-04 | 19/47 (KATO III, HepG2/C3A, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.003 | 15/47 (NCI-H460, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.27×** | +3.9 | 0.004 | 14/44 (NCI-H2347, C32, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.006 | 9/45 (PANC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.8 | 0.006 | 9/30 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.007 | 17/47 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.008 | 13/48 (PANC-1, SNU-423, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.010 | 6/44 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.032 | 18/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.040 | 12/47 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.059 | 8/48 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.070 | 4/46 (A498, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.40×** | +2.9 | 0.078 | 8/47 (NCI-H460, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.085 | 9/48 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11299.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.486×** | -12.0 | 2e-30 | 35/48 (LS 180, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.527×** | -10.7 | 5e-24 | 37/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.542×** | -10.2 | 4e-22 | 38/46 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.581×** | -9.0 | 2e-17 | 33/48 (LS 180, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.700×** | -8.4 | 6e-15 | 34/48 (LS 180, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.620×** | -7.9 | 2e-13 | 30/48 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.656×** | -7.0 | 2e-10 | 30/46 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -5.6 | 2e-06 | 28/47 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.546×** | -5.3 | 9e-06 | 24/48 (LS 180, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.752×** | -4.8 | 1e-04 | 20/48 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.761×** | -4.6 | 3e-04 | 18/47 (SW480, NCI-H2030, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.638×** | -3.9 | 0.004 | 14/45 (NCI-H460, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.797×** | -3.8 | 0.007 | 18/47 (AsPC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.814×** | -3.4 | 0.024 | 12/48 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 47.4 | 3 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +13.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.213× (z -14.4) |
| [[HT-29 (line)]] | alt | 37.2 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.08× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.286× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 31.3 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +14.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.305× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 50.8 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -9.5) |
| [[SW480 (line)]] | alt | 38.2 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +17.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.275× (z -13.9) |
| [[HCT15 (line)]] | alt | 40.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +10.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.191× (z -10.2) |
| [[KATO III (line)]] | alt | 41.8 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 4.72× (z +12.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.244× (z -12.6) |
| [[A549 (line)]] | wt | 12.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.76× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 35.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 16.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 30.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.79× (z +16.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 15.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +11.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 17.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.78× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 22.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +14.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.99× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 41.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.20× (z +9.7) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 0.5 µM 0.392× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 33.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 14.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.96× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 20.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 40.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 17.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.62× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.10× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 46.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.177× (z -10.0) |
| [[SNU-423 (line)]] | alt | 13.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.48× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 26.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0561× (z -8.9) |
| [[C32 (line)]] | wt | 8.03 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +9.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0592× (z -12.3) |
| [[Hs 766T (line)]] | wt | 24.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +10.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.172× (z -9.0) |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | +0.65 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NNT]] | +0.63 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ZMYND11]] | +0.62 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PSME3IP1]] | +0.62 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[CNOT1]] | +0.61 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[HFE]] | +0.61 | +0.50 / +0.30 | both halves | 2e-04 |  |
| [[VPS52]] | +0.61 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[ZNF362]] | +0.61 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[PMF1]] | +0.60 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[RCN1]] | +0.60 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[IQCH-AS1]] | +0.60 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[ZMPSTE24]] | +0.60 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPN2]] | -0.64 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[CIB1]] | -0.63 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[UBA6]] | -0.63 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[DOCK6]] | -0.62 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[PPIP5K1]] | -0.62 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PLIN3]] | -0.61 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[PFDN2]] | -0.61 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[VPS37C]] | -0.61 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[GPR157]] | -0.60 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ARID3B]] | -0.59 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[STK4]] | -0.59 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[PFKFB3]] | -0.59 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction -0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.3, 2.6); signed map (21.1, -30.2). **Vector** length 98.4, 23.8% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +20.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +26.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +24.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +6.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -12.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -7.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -10.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -4.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | acireductone dioxygenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:3,497,366-3,519,531 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SIPL, MTCBP-1, ARD, APL1, FLJ10913, HMFT1638, mtnD |
| Gene groups (HGNC) | Oxygenases |
| Reactome | 3 pathways, smallest: Methionine salvage pathway; Sulfur amino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV57](https://www.uniprot.org/uniprotkb/Q9BV57) (Acireductone dioxygenase):

> Catalyzes 2 different reactions between oxygen and the acireductone 1,2-dihydroxy-3-keto-5-methylthiopentene (DHK-MTPene) depending upon the metal bound in the active site (By similarity). Fe-containing acireductone dioxygenase (Fe-ARD) produces formate and 2-keto-4-methylthiobutyrate (KMTB), the alpha-ketoacid precursor of methionine in the methionine recycle pathway. Ni-containing acireductone dioxygenase (Ni-ARD) produces methylthiopropionate, carbon monoxide and formate, and does not lie on …

**Summary**, from NCBI Gene [55256](https://www.ncbi.nlm.nih.gov/gene/55256):

> This gene encodes an enzyme that belongs to the aci-reductone dioxygenase family of metal-binding enzymes, which are involved in methionine salvage. This enzyme may regulate mRNA processing in the nucleus, and may carry out different functions depending on its localization. Related pseudogenes have been defined on chromosomes 8 and 20. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:30576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30576) · Entrez [55256](https://www.ncbi.nlm.nih.gov/gene/55256) · UniProt [Q9BV57](https://www.uniprot.org/uniprotkb/Q9BV57) · Ensembl [ENSG00000182551](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182551)

## Data

Gene col 11299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11299); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11299]; `tensor/DDL_lfc|DDL_z.npy` [11299]; `embed/gene_vectors.npy` [11299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11299 or target_col == 11299). Every well: [[ADI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
