---
symbol: "AP1S3"
type: "gene"
col: 7586
ensembl_id: "ENSG00000152056"
name: "adaptor related protein complex 1 subunit sigma 3"
location: "2q36.1"
module: 3
arm: "-"
pooled_cpm: 94.55
n_lines_expressing: 46
n_dd_up: 33
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# AP1S3

*adaptor related protein complex 1 subunit sigma 3* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.45× (z +29.8, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.803× (z -7.3, q 1e-10, down in 22 of 44 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.639× (z -5.5, q 1e-05, down in 22 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SHP-77 0.360×, HEC-1-A 0.471×, SW1417 0.481×, HT-29 0.552×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SHP-77 0.235×, NCI-H460 0.240×; ⚠ cell-cycle shift, explains ~60% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.242×, SHP-77 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.236×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.418×); [[Clobetasol propionate (drug)]] 5 µM in 1 line (Hs 766T 0.366×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A6]] (+0.52, fdr 3e-05), [[DHX9]] (+0.51, fdr 1e-04), [[LMNTD1]] (+0.49, fdr 3e-05); moves opposite to [[PMM1]] (-0.54, fdr 7e-05), [[XAB2]] (-0.54, fdr 3e-05), [[GID4]] (-0.53, fdr 4e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[JAG1]] → it (grade B ⚠); 5 go from it, the strongest it → [[QPCTL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.45×** | +29.8 | 0e+00 | 42/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +18.7 | 0e+00 | 39/44 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.02×** | +16.5 | 0e+00 | 35/44 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.01×** | +16.4 | 0e+00 | 37/44 (SW480, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.82×** | +14.1 | 5e-43 | 32/44 (SW480, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +12.8 | 1e-35 | 35/44 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.72×** | +12.8 | 2e-35 | 34/44 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +11.1 | 1e-26 | 29/44 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +10.6 | 2e-24 | 28/44 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.55×** | +9.9 | 2e-21 | 23/40 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.48×** | +8.5 | 7e-16 | 27/40 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +8.4 | 2e-15 | 25/44 (A498, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.42×** | +7.9 | 1e-13 | 20/43 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.5 | 4e-12 | 25/44 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.30×** | +6.2 | 2e-08 | 18/43 (SW480, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.6 | 6e-07 | 20/44 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +5.6 | 7e-07 | 18/44 (PANC-1, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +5.3 | 3e-06 | 18/45 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +5.1 | 7e-06 | 15/45 (A-172, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +5.0 | 1e-05 | 20/45 (NCI-H2347, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +4.8 | 3e-05 | 17/44 (HEC-1-A, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.8 | 3e-05 | 15/44 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 4e-04 | 14/43 (A498, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7586.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SHP-77 0.360×, HEC-1-A 0.471×, SW1417 0.481×, HT-29 0.552×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SHP-77 0.235×, NCI-H460 0.240×; ⚠ cell-cycle shift, explains ~60% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.242×, SHP-77 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.236×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.418×); [[Clobetasol propionate (drug)]] 5 µM in 1 line (Hs 766T 0.366×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.803×** | -7.3 | 1e-10 | 22/44 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.639×** | -5.5 | 1e-05 | 22/43 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.891× | -3.9 | 0.021 | 7/45 (HT-29, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.895× | -3.7 | 0.027 | 18/45 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -3.6 | 0.040 | 1/46 (NCI-H2030) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.858× | -3.5 | 0.045 | 12/43 (RPMI-7951, NCI-H23, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.864× | -3.5 | 0.045 | 13/43 (HEC-1-A, SW 1271, …) | two highest doses |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.090 | 9/43 (LS 180, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.13 | 9/44 (COLO 205, LOX-IMVI, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.879× | -3.0 | 0.13 | 13/44 (SK-MEL-2, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.8 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.9) | — |
| [[A-172 (line)]] | wt | 32.2 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +16.1) | — |
| [[NCI-H460 (line)]] | wt | 318 | 0 | 7 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -13.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A498 (line)]] | wt | 43.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +20.8) | — |
| [[A-427 (line)]] | wt | 36.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 74.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +18.0) | — |
| [[SHP-77 (line)]] | alt | 419 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.6) |
| [[BT-474 (line)]] | alt | 86.0 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.1) | [[Lonafarnib (drug)]] 5 µM 0.148× (z -8.6) ⚠ toxic |
| [[C32 (line)]] | wt | 48.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 131 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 138 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.60× (z +11.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 92.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +17.2) | — |
| [[SW 900 (line)]] | alt | 57.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.4) | — |
| [[A549 (line)]] | wt | 71.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 113 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.8) | — |
| [[HepG2_C3A (line)]] | wt | 48.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +15.6) | — |
| [[HT-29 (line)]] | alt | 90.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 26.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +17.5) | — |
| [[NCI-H2347 (line)]] | alt | 67.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.8) | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.218× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Atazanavir (sulfate) (drug)]] 5 µM 0.236× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 79.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +16.1) | — |
| [[SW48 (line)]] | wt | 150 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.9) | [[Bortezomib (drug)]] 0.05 µM 0.310× (z -8.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.3) | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0883× (z -8.6) |
| [[COLO 205 (line)]] | alt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +14.0) | — |
| [[HCT15 (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 5 µM 0.366× (z -9.5) |
| [[LoVo (line)]] | wt | 76.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +16.3) | — |
| [[LOX-IMVI (line)]] | wt | 38.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H1573 (line)]] | alt | 228 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.27× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[RPMI-7951 (line)]] | alt | 56.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 135 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 211 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 22.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A6]] | +0.52 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[DHX9]] | +0.51 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[LMNTD1]] | +0.49 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[NAB1]] | +0.48 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[SCG2]] | +0.47 | +0.45 / +0.40 | both halves | 4e-05 |  |
| [[GASK1B]] | +0.47 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[SLC9A2]] | +0.47 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[PDE7B]] | +0.47 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[TM4SF18]] | +0.47 | +0.36 / +0.37 | both halves | 9e-05 |  |
| [[ATAD1]] | +0.47 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[GALNT10]] | +0.46 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CAVIN2-AS1]] | +0.46 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMM1]] | -0.54 | -0.37 / -0.64 | both halves | 7e-05 |  |
| [[XAB2]] | -0.54 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[GID4]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[DCAF11]] | -0.50 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[WIPI2]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ZNF394]] | -0.49 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[MKRN1]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ALKBH7]] | -0.49 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[BCKDHA]] | -0.48 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[MPST]] | -0.48 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TTC9C]] | -0.48 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[NARF]] | -0.48 | -0.32 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG1]] | B | JAG1 activity raises AP1S3's level | lines that do not express JAG1 (6) vs lines expressing it (44) | 2.08× lower at baseline in the lines without JAG1 | 0.073 | ⚠ within organs, on part of the lines; also absent: DENND3, SHB, IER3 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QPCTL]] | C | AP1S3 activity lowers QPCTL's level | lines that do not express AP1S3 (4) vs lines expressing it (46) | 1.68× higher at baseline in the lines without AP1S3 | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02842, ENSG00000236283, LRIF1; maybe low, not absent |
| [[TBC1D20]] | C | AP1S3 activity lowers TBC1D20's level | lines that do not express AP1S3 (4) vs lines expressing it (46) | 1.47× higher at baseline in the lines without AP1S3 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02842, ENSG00000236283, LRIF1; maybe low, not absent |
| [[NSD3]] | C | AP1S3 activity strengthens NSD3's drug response | lines that do not express AP1S3 (4) vs lines expressing it (45) | the lines without AP1S3 respond 0.95× as strongly (z diff +0.68); strongest at Belinostat 5 µM: 0.85x vs 0.68x (z diff +3.5) | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02842, ENSG00000236283, LRIF1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FAT1]] | C | AP1S3 activity raises FAT1's level | lines that do not express AP1S3 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without AP1S3 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02842, ENSG00000236283, LRIF1; maybe low, not absent |
| [[RASEF]] | C | AP1S3 activity raises RASEF's level | lines that do not express AP1S3 (4) vs lines expressing it (46) | 5.10× lower at baseline in the lines without AP1S3 | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02842, ENSG00000236283, LRIF1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.412). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-14.2, -15.4); signed map (42.5, 29.6). **Vector** length 100, 24.0% of its response variance represented; |z| ≥ 3 in 1,469 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +7.6 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +7.1 | +14.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +18.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +29.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -3.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.1 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.5 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 1 subunit sigma 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:223,667,680-223,838,027 (-) |
| Ensembl biotype | protein_coding |
| Also known as | sigma1C |
| Gene groups (HGNC) | Adaptor related protein complex 1 |
| Reactome | 13 pathways, smallest: Nef mediated downregulation of MHC class I complex cell surface expression; Nef-mediates down modulation of cell surface receptors by recruiting them to clathrin adapters; The role of Nef in HIV-1 replication and disease pathogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PC3](https://www.uniprot.org/uniprotkb/Q96PC3) (AP-1 complex subunit sigma-3):

> Subunit of clathrin-associated adaptor protein complex 1 that plays a role in protein sorting in the late-Golgi/trans-Golgi network (TGN) and/or endosomes. The AP complexes mediate both the recruitment of clathrin to membranes and the recognition of sorting signals within the cytosolic tails of transmembrane cargo molecules. Involved in TLR3 trafficking.

**Summary**, from NCBI Gene [130340](https://www.ncbi.nlm.nih.gov/gene/130340):

> This gene encodes a member of the adaptor-related protein complex 1, sigma subunit genes. The encoded protein is a component of adaptor protein complex 1 (AP-1), one of the AP complexes involved in claathrin-mediated vesicular transport from the Golgi or endosomes. Disruption of the pathway for display of HIV-1 antigens, which prevents recognition of the virus by cytotoxic T cells, has been shown to involve the AP-1 complex (PMID: 15569716). Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:18971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18971) · Entrez [130340](https://www.ncbi.nlm.nih.gov/gene/130340) · UniProt [Q96PC3](https://www.uniprot.org/uniprotkb/Q96PC3) · Ensembl [ENSG00000152056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152056)

## Data

Gene col 7586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7586); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7586]; `tensor/DDL_lfc|DDL_z.npy` [7586]; `embed/gene_vectors.npy` [7586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7586 or target_col == 7586). Every well: [[AP1S3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1S3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
