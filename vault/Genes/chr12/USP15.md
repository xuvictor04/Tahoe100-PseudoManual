---
symbol: "USP15"
type: "gene"
col: 5738
ensembl_id: "ENSG00000135655"
name: "ubiquitin specific peptidase 15"
location: "12q14.1"
module: 1
arm: "-"
pooled_cpm: 248.07
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# USP15

*ubiquitin specific peptidase 15* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.26× (z +17.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.486× (z -14.9, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H1573 0.122×, NCI-H2347 0.329×, LS 180 0.246×, CFPAC-1 0.369×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.324×, SW1417 0.308×, CFPAC-1 0.376×, NCI-H2347 0.385×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.412×, A549 0.484×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.464×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARIH1]] (+0.60, fdr 1e-05), [[GBF1]] (+0.58, fdr 4e-05), [[RAB1A]] (+0.51, fdr 4e-05); moves opposite to [[ITPKB]] (-0.52, fdr 1e-04), [[ZNF253]] (-0.51, fdr 1e-04), [[RCC1L]] (-0.49, fdr 2e-04).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TYMP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.26×** | +17.4 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.95×** | +15.3 | 0e+00 | 49/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +14.7 | 0e+00 | 46/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +12.3 | 1e-32 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +12.0 | 4e-31 | 48/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +10.3 | 1e-22 | 45/48 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +9.7 | 3e-20 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +9.5 | 2e-19 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +9.4 | 2e-19 | 43/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.27×** | +9.1 | 4e-18 | 43/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +9.1 | 4e-18 | 42/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.5 | 3e-12 | 37/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.7 | 1e-09 | 34/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +5.6 | 1e-06 | 30/48 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +4.3 | 5e-04 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.9 | 0.004 | 23/48 (SW480, KATO III, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.006 | 21/48 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.7 | 0.007 | 13/48 (RKO, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5738.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H1573 0.122×, NCI-H2347 0.329×, LS 180 0.246×, CFPAC-1 0.369×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.324×, SW1417 0.308×, CFPAC-1 0.376×, NCI-H2347 0.385×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.412×, A549 0.484×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.464×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.486×** | -14.9 | 0e+00 | 40/44 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.566×** | -12.2 | 7e-32 | 45/49 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.790×** | -5.1 | 8e-05 | 34/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.803×** | -4.5 | 8e-04 | 25/47 (KATO III, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 0.845× | -3.6 | 0.033 | 22/48 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.850× | -3.5 | 0.042 | 15/48 (SK-MEL-2, AsPC-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.851× | -3.5 | 0.043 | 17/48 (LoVo, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 222 | 14 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.486× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 288 | 13 (6 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.508× (z -9.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 222 | 9 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 295 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -31.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 207 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +19.6) | [[Dinaciclib (drug)]] 0.5 µM 0.548× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 179 | 7 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.43× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 385 | 6 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 334 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -18.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 211 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +14.4) | — |
| [[HT-29 (line)]] | alt | 178 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -11.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 198 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -15.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 343 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 224 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -16.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 320 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -17.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 175 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 184 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -15.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 347 | 5 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 276 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +14.4) | — |
| [[COLO 205 (line)]] | alt | 234 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 145 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.51× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 298 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +13.5) | [[Docetaxel (drug)]] 0.05 µM 0.377× (z -11.3) ⚠ transcription drop |
| [[A549 (line)]] | wt | 328 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.83× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 366 | 3 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -13.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 268 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 183 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.467× (z -10.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 254 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -17.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 285 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.05× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -14.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 263 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -14.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 249 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.73× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.550× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 194 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -14.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 230 | 4 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.96× (z +10.8) | — |
| [[A-172 (line)]] | wt | 168 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 5.14× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.464× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 306 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -16.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 181 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.10× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 230 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.486× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 231 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.87× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -12.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 205 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.35× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 215 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 182 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 237 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -10.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 259 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 248 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.98× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 199 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 268 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 208 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.8) | — |
| [[NCI-H2122 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARIH1]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[GBF1]] | +0.58 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[RAB1A]] | +0.51 | +0.52 / +0.43 | both halves | 4e-05 |  |
| [[DNAJC1]] | +0.50 | +0.39 / +0.40 | both halves | 5e-05 |  |
| [[HLA-DRB1]] | +0.48 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[PIBF1]] | +0.47 | +0.38 / +0.33 | both halves | 1e-04 |  |
| [[IFITM2]] | +0.47 | +0.40 / +0.39 | both halves | 6e-05 |  |
| [[ATP5F1D]] ⚠ | +0.47 | +0.10 / +0.40 | ⚠ not reproduced | 0.003 | ⚠ in the vector space only through flagged drug-doses |
| [[DENND4A]] | +0.47 | +0.38 / +0.49 | both halves | 7e-05 | same gene group |
| [[MRTFA]] | +0.46 | +0.37 / +0.43 | both halves | 7e-05 |  |
| [[STK3]] | +0.46 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[TTC3P1]] | +0.45 | +0.36 / +0.30 | both halves | 2e-04 |  |
| [[EDF1]] | +0.45 | +0.37 / +0.21 | both halves | 7e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPKB]] | -0.52 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ZNF253]] | -0.51 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[RCC1L]] | -0.49 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[ZNF507]] | -0.48 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[ZNF100]] | -0.47 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[MCM3AP]] | -0.47 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[ZNF700]] | -0.47 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[WASH8P]] ⚠ | -0.47 | -0.37 / -0.30 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF649]] | -0.46 | -0.47 / -0.24 | both halves | 4e-04 |  |
| [[IGF2BP1]] | -0.46 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[DVL3]] | -0.46 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[TLCD3A]] | -0.46 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[MSANTD7]] | -0.45 | -0.43 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TYMP]] | B | TYMP activity raises USP15's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.24× lower at baseline in the lines without TYMP | 0.012 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[ZNF100]] | B | ZNF100 activity lowers USP15's level | lines that do not express ZNF100 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without ZNF100 | 0.034 | ⚠ within organs, on part of the lines; also absent: ZNF66, ENSG00000269237, SORT1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.253). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (17.8, -38.9); signed map (-48.8, 12.5). **Vector** length 87.5, 32.9% of its response variance represented; |z| ≥ 3 in 1,388 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +1.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.0 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | +14.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +3.9 |
|  | [[Infigratinib (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:62,260,338-62,417,431 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0529, UNPH4 |
| Gene groups (HGNC) | Ubiquitin specific peptidases; MicroRNA protein coding host genes |
| Hallmark sets | COMPLEMENT, HEME_METABOLISM |
| Reactome | 7 pathways, smallest: Downregulation of TGF-beta receptor signaling; TGF-beta receptor signaling activates SMADs; UCH proteinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4E8](https://www.uniprot.org/uniprotkb/Q9Y4E8) (Ubiquitin carboxyl-terminal hydrolase 15):

> Hydrolase that removes conjugated ubiquitin from target proteins and regulates various pathways such as the TGF-beta receptor signaling, NF-kappa-B and RNF41/NRDP1-PRKN pathways. Acts as a key regulator of TGF-beta receptor signaling pathway, but the precise mechanism is still unclear: according to a report, acts by promoting deubiquitination of monoubiquitinated R-SMADs (SMAD1, SMAD2 and/or SMAD3), thereby alleviating inhibition of R-SMADs and promoting activation of TGF-beta target genes. …

**Summary**, from NCBI Gene [9958](https://www.ncbi.nlm.nih.gov/gene/9958):

> This gene encodes a member of the ubiquitin specific protease (USP) family of deubiquitinating enzymes. USP enzymes play critical roles in ubiquitin-dependent processes through polyubiquitin chain disassembly and hydrolysis of ubiquitin-substrate bonds. The encoded protein associates with the COP9 signalosome, and also plays a role in transforming growth factor beta signalling through deubiquitination of receptor-activated SMAD transcription factors. Alternatively spliced transcript variants …

**Accessions** — [HGNC:12613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12613) · Entrez [9958](https://www.ncbi.nlm.nih.gov/gene/9958) · UniProt [Q9Y4E8](https://www.uniprot.org/uniprotkb/Q9Y4E8) · Ensembl [ENSG00000135655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135655)

## Data

Gene col 5738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5738); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5738]; `tensor/DDL_lfc|DDL_z.npy` [5738]; `embed/gene_vectors.npy` [5738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5738 or target_col == 5738). Every well: [[USP15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
