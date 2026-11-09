---
symbol: "CALM2"
type: "gene"
col: 6824
ensembl_id: "ENSG00000143933"
name: "calmodulin 2"
location: "2p21"
module: 34
arm: "+"
pooled_cpm: 355.01
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CALM2

*calmodulin 2* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (22 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.73× (z +16.8, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +6.2, q 6e-08, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.725× (z -3.7, q 0.085, down in 39 of 50 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 0.814× (z -3.6, q 0.085, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (AsPC-1 0.403×); [[Binimetinib (drug)]] 0.05 µM in 1 line (AsPC-1 0.543×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HOP62 0.450×; ⚠ cell-cycle shift, explains ~57% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.505×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA6]] (+0.61, fdr 1e-05), [[TMSB4X]] (+0.59, fdr 1e-05), [[EPB41L2]] (+0.59, fdr 1e-05); moves opposite to [[ZNF581]] (-0.60, fdr 1e-05), [[SLC25A38]] (-0.59, fdr 1e-05), [[PEX16]] (-0.58, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 23 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.73×** | +16.8 | 0e+00 | 49/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.04×** | +13.6 | 9e-40 | 44/44 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.72×** | +11.8 | 8e-30 | 45/45 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +6.2 | 6e-08 | 41/48 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.63×** | +6.2 | 6e-08 | 40/48 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +5.6 | 2e-06 | 30/48 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.57×** | +5.6 | 2e-06 | 40/47 (C32, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.51×** | +5.2 | 1e-05 | 41/48 (hTERT-HPNE, AsPC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.53×** | +5.2 | 1e-05 | 38/50 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.50×** | +5.1 | 2e-05 | 37/48 (hTERT-HPNE, HOP62, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +4.6 | 3e-04 | 32/49 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.42×** | +4.5 | 4e-04 | 37/48 (hTERT-HPNE, HOP62, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +4.4 | 4e-04 | 34/48 (hTERT-HPNE, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.40×** | +4.3 | 8e-04 | 33/48 (hTERT-HPNE, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.39×** | +4.2 | 1e-03 | 34/48 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 28/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.002 | 33/47 (HOP62, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.005 | 28/48 (C32, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.005 | 30/47 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.010 | 34/48 (NCI-H1573, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.021 | 22/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.031 | 29/49 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.032 | 31/48 (AsPC-1, CFPAC-1, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.57×** | +3.0 | 0.052 | 30/46 (NCI-H1573, CFPAC-1, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +2.9 | 0.063 | 24/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.36×** | +2.8 | 0.093 | 27/49 (HOP62, NCI-H23, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.26×** | +2.7 | 0.097 | 25/47 (A549, C32, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6824.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (AsPC-1 0.403×); [[Binimetinib (drug)]] 0.05 µM in 1 line (AsPC-1 0.543×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HOP62 0.450×; ⚠ cell-cycle shift, explains ~57% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.505×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.725×** | -3.7 | 0.085 | 39/50 (AsPC-1, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.814×** | -3.6 | 0.085 | 32/48 (AsPC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.748×** | -3.5 | 0.085 | 36/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.764× | -3.3 | 0.14 | 40/48 (C32, NCI-H1573, …) | rises with dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.838× | -3.2 | 0.15 | 21/48 (SW1417, AsPC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 224 | 12 (12 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.11× (z +18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 329 | 7 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.75× (z +8.7) | [[Ixazomib citrate (drug)]] 5 µM 0.450× (z -8.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 341 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.9× (z +24.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AsPC-1 (line)]] | alt | 628 | 4 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +13.3) ⚠ cell-cycle shift, explains ~82% of this change | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.403× (z -9.3) |
| [[C32 (line)]] | wt | 238 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.68× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 318 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.40× (z +18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 170 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.88× (z +19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 222 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.52× (z +18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 497 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.73× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 298 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.94× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 226 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HS-578T (line)]] | alt | 279 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1573 (line)]] | alt | 152 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 382 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 900 (line)]] | alt | 388 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW1417 (line)]] | alt | 548 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A498 (line)]] | wt | 420 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[C-33 A (line)]] | alt | 225 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 536 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[H4 (line)]] | wt | 300 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 343 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 263 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 291 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[J82 (line)]] | alt | 316 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 511 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2030 (line)]] | alt | 411 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2347 (line)]] | alt | 559 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 214 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 561 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RPMI-7951 (line)]] | alt | 347 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 431 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 251 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CHP-212 (line)]] | wt | 205 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[COLO 205 (line)]] | alt | 236 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.90× (z +8.5) | — |
| [[RKO (line)]] | wt | 242 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 256 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 362 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW48 (line)]] | wt | 311 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 418 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[BT-474 (line)]] | alt | 268 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.90× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 390 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 288 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 501 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 248 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 489 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 449 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 378 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA6]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TMSB4X]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[EPB41L2]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CTNNAL1]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TPM4]] | +0.58 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[STMN1]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[H2AZ2]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MKI67]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[KNL1]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[TEAD1]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CNTRL]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ANLN]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF581]] | -0.60 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[SLC25A38]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PEX16]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NAGPA]] | -0.58 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[COQ4]] | -0.57 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[SUPV3L1]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[TENT2]] | -0.53 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[GPATCH3]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[VPS33A]] | -0.53 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[TRMT2A]] | -0.53 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[NDUFS3]] | -0.52 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[TMLHE]] | -0.52 | -0.36 / -0.66 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CALM2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.403). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.5, -5.8); signed map (-5.6, 35.1). **Vector** length 106, 44.1% of its response variance represented; |z| ≥ 3 in 1,409 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.3 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +3.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.7 | +2.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.2 | +2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +4.1 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | +4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +2.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~99% of this change | -8.0 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -7.8 | -2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | +0.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.0 | -1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.5 | -0.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.6 | -1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:47,160,084-47,176,921 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PHKD, PHKD2, CAMII |
| Gene groups (HGNC) | Receptor ligands; EF-hand domain containing; Phosphorylase kinase subunits |
| Reactome | 6 pathways, smallest: CASP4 inflammasome assembly; Enterobacterial factors antagonize host defense; Non-canonical inflammasome activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DP24](https://www.uniprot.org/uniprotkb/P0DP24) (Calmodulin-2):

> Calmodulin acts as part of a calcium signal transduction pathway by mediating the control of a large number of enzymes, ion channels, aquaporins and other proteins through calcium-binding. Calcium-binding is required for the activation of calmodulin. Among the enzymes to be stimulated by the calmodulin-calcium complex are a number of protein kinases, such as myosin light-chain kinases and calmodulin-dependent protein kinase type II (CaMK2), and phosphatases. Together with CCP110 and centrin, is …

**Summary**, from NCBI Gene [805](https://www.ncbi.nlm.nih.gov/gene/805):

> This gene is a member of the calmodulin gene family. There are three distinct calmodulin genes dispersed throughout the genome that encode the identical protein, but differ at the nucleotide level. Calmodulin is a calcium binding protein that plays a role in signaling pathways, cell cycle progression and proliferation. Several infants with severe forms of long-QT syndrome (LQTS) who displayed life-threatening ventricular arrhythmias together with delayed neurodevelopment and epilepsy were found …

**Accessions** — [HGNC:1445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1445) · Entrez [805](https://www.ncbi.nlm.nih.gov/gene/805) · UniProt [P0DP24](https://www.uniprot.org/uniprotkb/P0DP24) · Ensembl [ENSG00000143933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143933)

## Data

Gene col 6824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6824); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6824]; `tensor/DDL_lfc|DDL_z.npy` [6824]; `embed/gene_vectors.npy` [6824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6824 or target_col == 6824). Every well: [[CALM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
