---
symbol: "JPT2"
type: "gene"
col: 13029
ensembl_id: "ENSG00000206053"
name: "Jupiter microtubule associated homolog 2"
location: "16p13.3"
module: 24
arm: "-"
pooled_cpm: 67.6
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# JPT2

*Jupiter microtubule associated homolog 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.98× (z +16.2, q 0e+00, up in 39 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.27× (z +5.8, q 7e-07, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A498 3.34×, NCI-H23 3.64×, NCI-H460 3.43×, LS 180 3.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (A498 4.25×, LoVo 3.94×, KATO III 3.34×, LS 180 3.29×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 2.61×, NCI-H460 3.15×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (HOP62 2.04×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HEC-1-A 0.276×, PANC-1 0.401×, SW480 0.461×, HCT15 0.417×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (HEC-1-A 0.515×, PANC-1 0.559×, NCI-H2347 0.528×, J82 0.604×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.436×, HEC-1-A 0.415×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cepharanthine (drug)]] 0.5 µM in 1 line (CHP-212 0.0960×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO5]] (+0.61, fdr 1e-05), [[LMNB2]] (+0.60, fdr 2e-05), [[PRKDC]] (+0.59, fdr 1e-05); moves opposite to [[SMIM26]] (-0.63, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[ODR4]] (-0.61, fdr 1e-05), [[SMIM27]] (-0.59, fdr 9e-05), [[DCTN6-DT]] (-0.58, fdr 5e-05).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13029.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A498 3.34×, NCI-H23 3.64×, NCI-H460 3.43×, LS 180 3.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (A498 4.25×, LoVo 3.94×, KATO III 3.34×, LS 180 3.29×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 2.61×, NCI-H460 3.15×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (HOP62 2.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +16.2 | 0e+00 | 39/41 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +15.9 | 0e+00 | 42/49 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +13.0 | 4e-36 | 7/49 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +8.8 | 2e-16 | 30/42 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +5.8 | 7e-07 | 20/48 (HOP62, A498, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.20×** | +4.6 | 5e-04 | 21/47 (NCI-H460, NCI-H1573, …) | two highest doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +4.3 | 0.001 | 11/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +4.0 | 0.004 | 17/48 (NCI-H1573, HT-29, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | 1.17× | +3.9 | 0.005 | 19/48 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.015 | 10/48 (A549, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.033 | 12/48 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +3.4 | 0.033 | 16/49 (A498, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.033 | 15/47 (NCI-H1573, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.14× | +3.2 | 0.058 | 6/48 (NCI-H2347, AN3 CA, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.058 | 8/49 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.14× | +3.1 | 0.058 | 13/47 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.058 | 10/48 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.068 | 7/47 (A549, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 1.13× | +3.0 | 0.077 | 6/48 (NCI-H2347, HT-29, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.077 | 4/48 (A498, H4, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.13× | +2.9 | 0.086 | 7/48 (A498, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13029.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HEC-1-A 0.276×, PANC-1 0.401×, SW480 0.461×, HCT15 0.417×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (HEC-1-A 0.515×, PANC-1 0.559×, NCI-H2347 0.528×, J82 0.604×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.436×, HEC-1-A 0.415×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cepharanthine (drug)]] 0.5 µM in 1 line (CHP-212 0.0960×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 5 µM |  | 0.846× | -5.9 | 2e-06 | 19/49 (NCI-H2347, SHP-77, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -5.8 | 2e-06 | 20/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -4.7 | 5e-04 | 12/48 (CFPAC-1, KATO III, …) | rises with dose | position effect removed |
| [[Baicalin (drug)]] 5 µM |  | 0.879× | -4.6 | 6e-04 | 8/49 (NCI-H2030, SW1417, …) | top dose only | position effect removed |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.859× | -3.7 | 0.028 | 9/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.909× | -3.4 | 0.059 | 9/48 (KATO III, RKO, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.878× | -3.3 | 0.088 | 13/48 (LS 180, CFPAC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 157 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -22.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 163 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -18.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 76.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +18.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 31.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +12.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 41.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 27.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +12.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 55.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 50.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 87.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 41.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 59.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 71.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 89.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 58.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +10.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 33.0 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0960× (z -9.2) |
| [[H4 (line)]] | wt | 40.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 89.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 59.2 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.04× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 65.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.604× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +12.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 84.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.141× (z -15.1) ⚠ toxic; cell-cycle shift, explains ~6% of this change |
| [[RPMI-7951 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[LMNB2]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PRKDC]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TARDBP]] | +0.59 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[EIF2S1]] | +0.58 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[ATL3]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TFDP1]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[NUP155]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[DARS2]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SLC25A24]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[SCRIB]] | +0.56 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[CAD]] | +0.56 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.63 | -0.54 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ODR4]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SMIM27]] | -0.59 | -0.37 / -0.59 | both halves | 9e-05 |  |
| [[DCTN6-DT]] | -0.58 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[TCEAL9]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[TCEAL8]] | -0.58 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TRIM52-AS1]] | -0.57 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[SNHG9]] | -0.57 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[SAT2]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | -0.57 | -0.46 / -0.64 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | -0.57 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[SCAND1]] | -0.57 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[CHCHD5]] | -0.56 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[NKAP]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.6, -34.1); signed map (-31.8, -48.3). **Vector** length 99.0, 21.5% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +16.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.5 | +4.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.4 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.5 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -1.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.6 | -1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.5 | +0.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.4 | -2.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | Jupiter microtubule associated homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,678,256-1,702,280 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13092, L11, KIAA1426; previously C16orf34, HN1L |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H910](https://www.uniprot.org/uniprotkb/Q9H910) (Jupiter microtubule associated homolog 2):

> Nicotinic acid adenine dinucleotide phosphate (NAADP) binding protein required for NAADP-evoked intracellular calcium release. Confers NAADP-sensitivity to the two pore channels (TPCs) complex. Enables NAADP to activate Ca(2+) release from the endoplasmic reticulum through ryanodine receptors.; (Microbial infection) Involved in the endolysosomal trafficking of human coronavirus SARS-CoV-2.

**Summary**, from NCBI Gene [90861](https://www.ncbi.nlm.nih.gov/gene/90861):

> Involved in endocytosis involved in viral entry into host cell and regulation of calcium-mediated signaling. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14137) · Entrez [90861](https://www.ncbi.nlm.nih.gov/gene/90861) · UniProt [Q9H910](https://www.uniprot.org/uniprotkb/Q9H910) · Ensembl [ENSG00000206053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206053)

## Data

Gene col 13029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13029); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13029]; `tensor/DDL_lfc|DDL_z.npy` [13029]; `embed/gene_vectors.npy` [13029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13029 or target_col == 13029). Every well: [[JPT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JPT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
