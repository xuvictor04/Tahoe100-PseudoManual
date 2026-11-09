---
symbol: "BUB1B"
type: "gene"
col: 8030
ensembl_id: "ENSG00000156970"
name: "BUB1 mitotic checkpoint serine/threonine kinase B"
location: "15q15.1"
module: 22
arm: "+"
pooled_cpm: 49.97
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 38
n_dd_up_clean: 3
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# BUB1B

*BUB1 mitotic checkpoint serine/threonine kinase B* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (18 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.81× (z +8.8, q 1e-15, up in 37 of 46 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.23× (z +4.3, q 7e-04, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (17 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.445× (z -17.0, q 0e+00, down in 42 of 46 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.453× (z -16.6, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP11A]] (+0.96, fdr 7e-06), [[INCENP]] (+0.94, fdr 7e-06), [[KIF23]] (+0.94, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 19 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.81×** | +8.8 | 1e-15 | 37/46 (KATO III, NCI-H23, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.79×** | +8.6 | 2e-15 | 33/46 (KATO III, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +8.4 | 8e-15 | 14/46 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.76×** | +8.4 | 8e-15 | 31/45 (KATO III, C-33 A, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.74×** | +8.2 | 2e-14 | 36/45 (LoVo, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.73×** | +8.1 | 5e-14 | 39/45 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.34×** | +6.1 | 1e-07 | 33/46 (NCI-H23, LoVo, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **2.13×** | +5.9 | 3e-07 | 28/44 (RKO, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.48×** | +5.8 | 4e-07 | 25/43 (Panc 03.27, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.43×** | +5.2 | 8e-06 | 28/46 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.45×** | +5.2 | 8e-06 | 21/41 (A498, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.40×** | +4.9 | 4e-05 | 25/44 (HT-29, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +4.7 | 1e-04 | 26/46 (RKO, Panc 03.27, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~77% of this change | **1.38×** | +4.6 | 2e-04 | 23/45 (NCI-H23, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +4.3 | 7e-04 | 18/46 (HT-29, PANC-1, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.015 | 16/45 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.066 | 12/45 (H4, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 18 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8030.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.445×** | -17.0 | 0e+00 | 42/46 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.453×** | -16.6 | 0e+00 | 41/46 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.511×** | -10.0 | 4e-21 | 36/46 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.447×** | -9.7 | 6e-20 | 41/46 (A-427, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.635×** | -6.7 | 2e-09 | 34/46 (SNU-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.638×** | -6.3 | 3e-08 | 26/46 (KATO III, SNU-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.599×** | -6.2 | 6e-08 | 30/46 (SNU-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.770×** | -5.5 | 3e-06 | 26/46 (A-427, A498, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.771×** | -5.5 | 3e-06 | 24/46 (A498, LoVo, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.701×** | -5.1 | 2e-05 | 25/46 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | **0.553×** | -4.6 | 2e-04 | 23/42 (AN3 CA, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.737×** | -4.5 | 3e-04 | 21/45 (SNU-1, A549, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.687×** | -4.5 | 3e-04 | 22/46 (SNU-1, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.745×** | -4.4 | 5e-04 | 20/46 (SNU-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.666×** | -4.3 | 7e-04 | 19/46 (KATO III, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -4.3 | 8e-04 | 21/46 (SW480, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -3.9 | 0.003 | 19/45 (C32, A549, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.701×** | -3.7 | 0.005 | 19/46 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.006 | 15/46 (A-427, HCT15, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.784×** | -3.6 | 0.008 | 21/46 (C-33 A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.770×** | -3.6 | 0.008 | 17/45 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[palbociclib (drug)]] 5 µM |  | **0.637×** | -3.5 | 0.011 | 19/45 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -3.4 | 0.014 | 17/46 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.643×** | -3.4 | 0.014 | 16/45 (C32, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.733×** | -3.3 | 0.022 | 22/46 (CHP-212, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.856× | -3.3 | 0.022 | 15/46 (NCI-H460, SW480, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.92 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 43.7 | 0 | 7 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.203× (z -15.0) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.307× (z -11.1) |
| [[A498 (line)]] | wt | 37.0 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0966× (z -27.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.279× (z -14.9) |
| [[SNU-1 (line)]] | wt | 88.7 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0982× (z -17.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -12.6) |
| [[A-172 (line)]] | wt | 46.5 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.202× (z -16.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -10.6) |
| [[H4 (line)]] | wt | 61.1 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0790× (z -18.1) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -10.3) |
| [[C32 (line)]] | wt | 33.9 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -11.4) |
| [[KATO III (line)]] | alt | 41.3 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.27× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H2030 (line)]] | alt | 72.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.3) |
| [[A-427 (line)]] | wt | 72.1 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.133× (z -22.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.188× (z -19.0) |
| [[HOP62 (line)]] | alt | 54.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -13.0) |
| [[LoVo (line)]] | wt | 49.9 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.345× (z -11.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.357× (z -11.5) |
| [[LS 180 (line)]] | wt | 38.0 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.108× (z -17.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.314× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 41.6 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.280× (z -14.0) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -12.8) |
| [[RKO (line)]] | wt | 73.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 70.3 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.296× (z -12.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.5) |
| [[A549 (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 86.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -13.4) |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -11.1) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Ciclopirox (drug)]] 5 µM 0.328× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 50.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 77.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 29.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.369× (z -9.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW48 (line)]] | wt | 80.3 | 0 | 2 | — | [[Amsacrine (drug)]] 5 µM 0.313× (z -10.3) |
| [[AN3 CA (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.237× (z -12.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.125× (z -8.5) |
| [[HCT15 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.355× (z -8.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HT-29 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.387× (z -8.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.200× (z -9.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H2347 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.361× (z -11.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H661 (line)]] | alt | 89.8 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0615× (z -9.9) |
| [[PANC-1 (line)]] | alt | 55.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 74.0 | 0 | 1 | — | [[Ixazomib (drug)]] 5 µM 0.0691× (z -8.6) |
| [[SW1417 (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.459× (z -8.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW480 (line)]] | alt | 61.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP11A]] | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | STRING 796 |
| [[INCENP]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 912 |
| [[KIF23]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | STRING 926 |
| [[KIF4A]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 968 |
| [[NCAPH]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 915 |
| [[KIF15]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | STRING 923 |
| [[DLGAP5]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 981 |
| [[BIRC5]] | +0.91 | +0.88 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 987 |
| [[CCNA2]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 994 |
| [[PRC1]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 893 |
| [[TPX2]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | STRING 936 |
| [[ARHGAP11B]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | STRING 608 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BUB1B's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises BUB1B's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without PIMREG | 0.024 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises BUB1B's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.01× lower at baseline in the lines without PBK | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[NDC80]] | C | NDC80 activity raises BUB1B's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without NDC80 | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises BUB1B's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.75× lower at baseline in the lines without AURKB | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises BUB1B's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.34× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises BUB1B's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without CDC20 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises BUB1B's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 3.25× lower at baseline in the lines without DIAPH3, MELK | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; co-absent genes |
| [[TP53]] | C | TP53 activity strengthens BUB1B's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 16 not recorded | the TP53-altered lines respond 0.90× as strongly (z diff +0.23); strongest at Selinexor 0.5 µM: 0.54x vs 0.25x (z diff +2.9) | 0.792 over the table, 0.056 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.927). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.8, -54.6); signed map (-48.2, -42.9). **Vector** length 163, 60.5% of its response variance represented; |z| ≥ 3 in 1,412 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.75 to 60); *mitotic spindle* (hallmark, mean cos +0.76 to 38); *G2/M Transition* (reactome, mean cos +0.70 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | +6.7 | +8.2 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +5.7 | +6.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +5.1 | +5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.9 | +8.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.6 | +8.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.5 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -9.8 | -17.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -8.4 | -9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | -5.7 | -6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.3 | -6.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.6 | -5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | BUB1 mitotic checkpoint serine/threonine kinase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,161,023-40,221,123 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BUBR1, MAD3L, Bub1A, SSK1 |
| Gene groups (HGNC) | BUB1 mitotic checkpoint serine/threonine kinase family |
| Hallmark sets | E2F_TARGETS |
| Reactome | 27 pathways, smallest: Inactivation of APC/C via direct inhibition of the APC/C complex; Inhibition of the proteolytic activity of APC/C required for the onset of anaphase by mitotic spindle checkpoint components; APC-Cdc20 mediated degradation of Nek2A |
| Matched by | ensembl_id |

**Function**, from UniProt [O60566](https://www.uniprot.org/uniprotkb/O60566) (Mitotic checkpoint serine/threonine-protein kinase BUB1 beta):

> Kinase which is a component of the mitotic checkpoint complex (MCC), which inhibits APC/C and delays chromosome segregation until all chromosomes are properly attached to the mitotic spindle. The MCC, which consists of CDC20, MAD2L1/MAD2, BUB1B/BUBR1 and BUB3, is a key player of the spindle assembly checkpoint. The MCC-bound APC/C complex is inactive and this delays the metaphase/anaphase transition. When the spindle assembly checkpoint is silenced, the MCC-APC/C complex recruits the E2 enzyme …

**Summary**, from NCBI Gene [701](https://www.ncbi.nlm.nih.gov/gene/701):

> This gene encodes a kinase involved in spindle checkpoint function. The protein has been localized to the kinetochore and plays a role in the inhibition of the anaphase-promoting complex/cyclosome (APC/C), delaying the onset of anaphase and ensuring proper chromosome segregation. Impaired spindle checkpoint function has been found in many forms of cancer. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1149) · Entrez [701](https://www.ncbi.nlm.nih.gov/gene/701) · UniProt [O60566](https://www.uniprot.org/uniprotkb/O60566) · Ensembl [ENSG00000156970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156970)

## Data

Gene col 8030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8030); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8030]; `tensor/DDL_lfc|DDL_z.npy` [8030]; `embed/gene_vectors.npy` [8030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8030 or target_col == 8030). Every well: [[BUB1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BUB1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
