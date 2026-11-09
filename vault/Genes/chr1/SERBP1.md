---
symbol: "SERBP1"
type: "gene"
col: 6659
ensembl_id: "ENSG00000142864"
name: "SERPINE1 mRNA binding protein 1"
location: "1p31.3"
module: 4
arm: "+"
pooled_cpm: 242.57
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SERBP1

*SERPINE1 mRNA binding protein 1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.99× (z +13.7, q 6e-40, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.40× (z +4.2, q 0.001, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.792× (z -4.1, q 0.021, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~44% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.536×, SW48 0.476×, HEC-1-A 0.580×; ⚠ cell-cycle shift, explains ~0% of this change); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.273×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.778×; ⚠ position not correctable); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.199×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX10]] (+0.73, fdr 7e-06), [[CEP83]] (+0.72, fdr 7e-06), [[CLYBL]] (+0.71, fdr 7e-06); moves opposite to [[RAB5B]] (-0.60, fdr 7e-06), [[PI4K2B]] (-0.60, fdr 1e-05), [[KLC4]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TGFBR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.99×** | +13.7 | 6e-40 | 49/49 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.90×** | +12.8 | 4e-35 | 44/44 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.12×** | +8.7 | 8e-16 | 42/45 (HS-578T, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.62×** | +5.8 | 9e-07 | 39/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.54×** | +5.4 | 8e-06 | 38/48 (A-172, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.51×** | +5.1 | 3e-05 | 37/48 (H4, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.50×** | +5.0 | 4e-05 | 40/48 (H4, NCI-H460, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.49×** | +5.0 | 5e-05 | 32/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +4.8 | 1e-04 | 29/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.44×** | +4.5 | 3e-04 | 36/48 (NCI-H1792, C32, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.43×** | +4.5 | 4e-04 | 33/48 (A-172, Hs 766T, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.43×** | +4.4 | 4e-04 | 34/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.4 | 5e-04 | 38/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.001 | 35/48 (AN3 CA, BT-474, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~87% of this change | **1.40×** | +4.2 | 0.001 | 39/48 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.012 | 38/48 (MIA PaCa-2, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.016 | 31/48 (NCI-H1792, HS-578T, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.68×** | +3.4 | 0.021 | 37/48 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.029 | 31/48 (LOX-IMVI, C32, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.034 | 39/48 (A498, SNU-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.60×** | +3.1 | 0.047 | 36/48 (C32, CFPAC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.051 | 35/48 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.18× | +2.9 | 0.086 | 10/48 (A-427, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6659.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.536×, SW48 0.476×, HEC-1-A 0.580×; ⚠ cell-cycle shift, explains ~0% of this change); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.273×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.778×; ⚠ position not correctable); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.199×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.792×** | -4.1 | 0.021 | 43/48 (SW1417, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.787× | -3.0 | 0.44 | 39/48 (A498, SHP-77, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 156 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.26× (z +17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 3.20× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 225 | 8 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 127 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[CFPAC-1 (line)]] | alt | 188 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HOP62 (line)]] | alt | 179 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[RPMI-7951 (line)]] | alt | 249 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[C32 (line)]] | wt | 138 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 150 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 151 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.31× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A498 (line)]] | wt | 246 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A549 (line)]] | wt | 151 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[H4 (line)]] | wt | 224 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[Hs 766T (line)]] | wt | 162 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 217 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[J82 (line)]] | alt | 297 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 330 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW 900 (line)]] | alt | 140 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 322 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.89× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HCT15 (line)]] | alt | 306 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HEC-1-A (line)]] | alt | 303 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 213 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 212 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 278 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 305 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 268 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Panc 03.27 (line)]] | alt | 216 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 324 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[RKO (line)]] | wt | 356 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 326 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 306 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[AsPC-1 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[CHP-212 (line)]] | wt | 175 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 192 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LS 180 (line)]] | wt | 289 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2030 (line)]] | alt | 250 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H23 (line)]] | alt | 379 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2347 (line)]] | alt | 183 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H596 (line)]] | alt | 222 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.273× (z -10.2) |
| [[NCI-H661 (line)]] | alt | 374 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 244 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.199× (z -8.8) |
| [[SW1417 (line)]] | alt | 243 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW48 (line)]] | wt | 356 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 290 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 399 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 261 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 169 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX10]] | +0.73 | +0.75 / +0.73 | both halves | 7e-06 | STRING 401 |
| [[CEP83]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CLYBL]] | +0.71 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[NAA15]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[NOC3L]] | +0.66 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[TAF1B]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[MGA]] | +0.65 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[DKC1]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 | STRING 450 |
| [[IPO7]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[C1QBP]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5B]] | -0.60 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[PI4K2B]] | -0.60 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[KLC4]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TTI2]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[ZNF821]] | -0.58 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZFPL1]] | -0.57 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[FAM229A]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[KLHDC2]] | -0.57 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[PPP1R42]] | -0.57 | -0.22 / -0.51 | both halves | 6e-04 |  |
| [[ZNF547]] | -0.56 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[WBP1]] | -0.56 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZNF490]] | -0.56 | -0.24 / -0.56 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFBR2]] | B | TGFBR2 activity lowers SERBP1's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 1.53× higher at baseline in the lines without TGFBR2 | 0.031 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[EFNB2]] | B | EFNB2 activity lowers SERBP1's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.29× higher at baseline in the lines without EFNB2 | 0.042 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[VAMP5]] | B | VAMP5 activity lowers SERBP1's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.30× higher at baseline in the lines without VAMP5 | 0.057 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[TERT]] | B | TERT activity raises SERBP1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.18× lower at baseline in the lines without TERT | 0.062 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[JPH1]] | B | JPH1 activity lowers SERBP1's level | lines that do not express JPH1 (15) vs lines expressing it (35) | 1.18× higher at baseline in the lines without JPH1 | 0.065 | ⚠ within organs, on part of the lines; also absent: UGT8, CADPS2, PTPRE |
| [[EFNB2]] | B | EFNB2 activity strengthens SERBP1's drug response | lines that do not express EFNB2 (15) vs lines expressing it (34) | the lines without EFNB2 respond 0.71× as strongly (z diff +1.61); strongest at Homoharringtonine 5 µM: 1.09x vs 1.37x (z diff +2.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141; target measured in part of the lines; artifact flags |
| [[SACS]] | B | SACS activity raises SERBP1's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without SACS | 0.071 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[LINC01232]] | B | LINC01232 activity lowers SERBP1's level | lines that do not express LINC01232 (11) vs lines expressing it (39) | 1.21× higher at baseline in the lines without LINC01232 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000286856, SERPINB1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.0, -42.5); signed map (-6.3, -48.4). **Vector** length 93.4, 43.6% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.2 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | -5.3 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.8 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | SERPINE1 mRNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:67,407,810-67,430,415 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-55, CHD3IP, HABP4L, Hero45, PAIRBP1, PAI-RBP1, DKFZP564M2423 |
| Hallmark sets | MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NC51](https://www.uniprot.org/uniprotkb/Q8NC51) (SERPINE1 mRNA-binding protein 1):

> Ribosome-binding protein that promotes ribosome hibernation, a process during which ribosomes are stabilized in an inactive state and preserved from proteasomal degradation. Acts via its association with EEF2/eEF2 factor, sequestering EEF2/eEF2 at the A-site of the ribosome and promoting ribosome stabilization and storage in an inactive state (By similarity). May also play a role in the regulation of mRNA stability: binds to the 3'-most 134 nt of the SERPINE1/PAI1 mRNA, a region which confers …

**Summary**, from NCBI Gene [26135](https://www.ncbi.nlm.nih.gov/gene/26135):

> Enables several functions, including SUMO binding activity; mRNA 3'-UTR binding activity; and translation repressor activity. Involved in PML body organization and ribosome hibernation. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17860) · Entrez [26135](https://www.ncbi.nlm.nih.gov/gene/26135) · UniProt [Q8NC51](https://www.uniprot.org/uniprotkb/Q8NC51) · Ensembl [ENSG00000142864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142864)

## Data

Gene col 6659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6659); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6659]; `tensor/DDL_lfc|DDL_z.npy` [6659]; `embed/gene_vectors.npy` [6659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6659 or target_col == 6659). Every well: [[SERBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
