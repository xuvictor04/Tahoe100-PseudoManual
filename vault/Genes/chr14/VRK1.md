---
symbol: "VRK1"
type: "gene"
col: 2018
ensembl_id: "ENSG00000100749"
name: "VRK serine/threonine kinase 1"
location: "14q32.2"
module: 6
arm: "+"
pooled_cpm: 51.05
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# VRK1

*VRK serine/threonine kinase 1* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (20 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +16.9, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.31× (z +5.2, q 7e-06, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.743× (z -8.5, q 1e-14, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[palbociclib (drug)]] 5 µM: 0.644× (z -4.5, q 6e-04, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MELK]] (+0.89, fdr 7e-06), [[GINS1]] (+0.86, fdr 7e-06), [[WDHD1]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 27 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.81×** | +16.9 | 0e+00 | 45/48 (SW1417, Panc 03.27, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.27×** | +15.9 | 0e+00 | 42/47 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **2.09×** | +14.8 | 0e+00 | 44/48 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.89×** | +12.2 | 2e-32 | 43/48 (SW480, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.78×** | +11.5 | 1e-28 | 42/48 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.68×** | +10.4 | 2e-23 | 42/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.57×** | +9.1 | 1e-17 | 30/48 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.49×** | +7.7 | 1e-12 | 26/42 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.36×** | +5.9 | 2e-07 | 26/48 (RKO, LoVo, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.8 | 4e-07 | 23/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.33×** | +5.7 | 8e-07 | 23/47 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +5.3 | 7e-06 | 22/48 (PANC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +5.2 | 7e-06 | 25/48 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.29×** | +4.7 | 1e-04 | 23/44 (NCI-H2347, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.26×** | +4.6 | 2e-04 | 20/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.003 | 15/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.016 | 15/48 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.021 | 13/48 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.027 | 8/48 (SW480, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.052 | 14/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.052 | 13/48 (SW480, HOP62, …) | rises with dose |  |
| [[Amsacrine (drug)]] 0.5 µM |  | 1.15× | +2.7 | 0.099 | 6/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2018.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.743×** | -8.5 | 1e-14 | 28/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.672×** | -8.0 | 3e-13 | 32/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.726×** | -6.1 | 2e-07 | 24/48 (SW48, LS 180, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -4.8 | 2e-04 | 4/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.846× | -4.8 | 2e-04 | 19/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.644×** | -4.5 | 6e-04 | 23/47 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.815×** | -4.1 | 0.003 | 17/48 (RKO, KATO III, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.866× | -4.1 | 0.003 | 18/48 (HCT15, KATO III, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.754×** | -4.1 | 0.003 | 18/48 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.830×** | -3.8 | 0.009 | 20/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.836× | -3.6 | 0.015 | 15/48 (SW480, SW1417, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.859× | -3.5 | 0.023 | 18/48 (A-427, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.740×** | -3.1 | 0.084 | 17/43 (SNU-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.859× | -3.1 | 0.084 | 13/47 (RKO, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.860× | -3.0 | 0.084 | 11/48 (HCT15, SW48, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.05 µM |  | 0.853× | -3.0 | 0.084 | 12/48 (SHP-77, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.811×** | -3.0 | 0.084 | 8/48 (LOX-IMVI, LoVo, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.88 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 92.9 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 49.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.0) ⚠ cell-cycle shift, explains ~43% of this change | [[Selinexor (drug)]] 5 µM 0.536× (z -8.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 84.0 | 4 (4 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +14.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[C32 (line)]] | wt | 33.9 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +10.8) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[Panc 03.27 (line)]] | alt | 72.7 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +14.6) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 37.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.397× (z -10.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A498 (line)]] | wt | 19.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.321× (z -12.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 40.9 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[H4 (line)]] | wt | 49.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.262× (z -10.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HS-578T (line)]] | alt | 35.2 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +9.9) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HT-29 (line)]] | alt | 27.7 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.9) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 52.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +9.8) ⚠ cell-cycle shift, explains ~43% of this change | [[Selinexor (drug)]] 5 µM 0.434× (z -10.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 61.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +10.9) ⚠ cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 26.4 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +13.9) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 41.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +11.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 49.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.9) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 31.7 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +12.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 41.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.4) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SW1417 (line)]] | alt | 61.5 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +16.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 58.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.299× (z -15.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +11.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[BT-474 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.9) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +10.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 55.3 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +12.0) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 41.7 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[J82 (line)]] | alt | 69.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[LoVo (line)]] | wt | 42.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +9.1) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[LS 180 (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.228× (z -13.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-1 (line)]] | wt | 58.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0651× (z -8.6) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 86.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0848× (z -9.7) |
| [[AN3 CA (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MELK]] | +0.89 | +0.88 / +0.91 | both halves | 7e-06 | STRING 425 |
| [[GINS1]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.86 | +0.87 / +0.86 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | pathway: Mitotic Anaphase |
| [[XRCC2]] | +0.85 | +0.86 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[CENPK]] | +0.84 | +0.84 / +0.86 | both halves | 7e-06 | pathway: Mitotic Anaphase; STRING 433 |
| [[POLQ]] | +0.83 | +0.84 / +0.85 | both halves | 7e-06 |  |
| [[FANCI]] | +0.83 | +0.81 / +0.83 | both halves | 7e-06 | STRING 403 |
| [[MCM8]] | +0.82 | +0.82 / +0.81 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 |  |
| [[FANCA]] | +0.82 | +0.79 / +0.85 | both halves | 7e-06 |  |
| [[DDIAS]] | +0.81 | +0.84 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises VRK1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without TCF19 | 0.036 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises VRK1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.94× lower at baseline in the lines without E2F8 | 0.048 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises VRK1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without CDC25A | 0.069 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises VRK1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.14× lower at baseline in the lines without DSCC1 | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises VRK1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.64× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises VRK1's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; its own permutation p |
| [[MCM2]] | C | MCM2 activity raises VRK1's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without MCM2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent; its own permutation p |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises VRK1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 1.82× lower at baseline in the lines without E2F1, MCM3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises VRK1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without MCM10 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.866). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.7, -45.3); signed map (-39.5, -47.6). **Vector** length 136, 44.6% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.65 to 65); *DNA strand elongation* (reactome, mean cos +0.69 to 28); *DNA Replication* (reactome, mean cos +0.67 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +8.7 | +15.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +8.1 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.1 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.1 | +7.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.9 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.9 | +3.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.6 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -8.7 | -8.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -7.2 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.9 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.4 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.0 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | VRK serine/threonine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:96,797,304-96,954,846 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | VRK serine/threonine kinase family |
| Reactome | 9 pathways, smallest: Initiation of Nuclear Envelope (NE) Reformation; Nuclear Envelope Breakdown; Nuclear Envelope (NE) Reassembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99986](https://www.uniprot.org/uniprotkb/Q99986) (Serine/threonine-protein kinase VRK1):

> Serine/threonine kinase involved in the regulation of key cellular processes including the cell cycle, nuclear condensation, transcription regulation, and DNA damage response. Controls chromatin organization and remodeling by mediating phosphorylation of histone H3 on 'Thr-4' and histone H2AX (H2aXT4ph). It also phosphorylates KAT5 in response to DNA damage, promoting KAT5 association with chromatin and histone acetyltransferase activity. Is involved in the regulation of cell cycle progression …

**Summary**, from NCBI Gene [7443](https://www.ncbi.nlm.nih.gov/gene/7443):

> This gene encodes a member of the vaccinia-related kinase (VRK) family of serine/threonine protein kinases. This gene is widely expressed in human tissues and has increased expression in actively dividing cells, such as those in testis, thymus, fetal liver, and carcinomas. Its protein localizes to the nucleus and has been shown to promote the stability and nuclear accumulation of a transcriptionally active p53 molecule and, in vitro, to phosphorylate Thr18 of p53 and reduce p53 ubiquitination. …

**Accessions** — [HGNC:12718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12718) · Entrez [7443](https://www.ncbi.nlm.nih.gov/gene/7443) · UniProt [Q99986](https://www.uniprot.org/uniprotkb/Q99986) · Ensembl [ENSG00000100749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100749)

## Data

Gene col 2018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2018); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2018]; `tensor/DDL_lfc|DDL_z.npy` [2018]; `embed/gene_vectors.npy` [2018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2018 or target_col == 2018). Every well: [[VRK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VRK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
