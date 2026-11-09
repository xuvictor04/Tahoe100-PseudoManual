---
symbol: "FOXP1"
type: "gene"
col: 3598
ensembl_id: "ENSG00000114861"
name: "forkhead box P1"
location: "3p13"
module: 143
arm: "+"
pooled_cpm: 271.64
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 42
n_dd_up_clean: 16
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# FOXP1

*forkhead box P1* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +5.7, q 5e-06, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (22 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.586× (z -12.2, q 2e-31, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERBIN]] (+0.63, fdr 1e-05), [[ATXN7L1]] (+0.63, fdr 1e-05), [[PPP1R9A]] (+0.62, fdr 7e-06); moves opposite to [[PLXNB3]] (-0.59, fdr 1e-05), [[RARS2]] (-0.59, fdr 1e-05), [[PCYT1A]] (-0.58, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.7 | 5e-06 | 30/44 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.81×** | +4.7 | 6e-04 | 30/46 (LS 180, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +4.2 | 0.004 | 27/45 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.004 | 25/43 (A549, HOP62, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +3.7 | 0.020 | 30/44 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.020 | 29/45 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.024 | 24/44 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.025 | 25/45 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.030 | 23/44 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.030 | 24/44 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.039 | 15/44 (LOX-IMVI, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.049 | 21/44 (Panc 03.27, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.052 | 21/44 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.052 | 18/45 (BT-474, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.058 | 21/44 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.066 | 19/44 (LOX-IMVI, J82, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.078 | 19/44 (BT-474, HOP62, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 22 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -12.2 | 2e-31 | 34/45 (HepG2/C3A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.483×** | -11.7 | 2e-29 | 38/44 (NCI-H23, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.490×** | -11.1 | 4e-26 | 35/43 (LOX-IMVI, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.497×** | -10.8 | 3e-25 | 32/40 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.519×** | -10.6 | 4e-24 | 38/44 (SHP-77, COLO 205, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.522×** | -10.5 | 1e-23 | 33/44 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.536×** | -10.1 | 7e-22 | 38/44 (SHP-77, COLO 205, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.537×** | -10.0 | 1e-21 | 34/44 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.557×** | -9.4 | 3e-19 | 32/44 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.548×** | -8.6 | 5e-16 | 36/44 (KATO III, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.591×** | -8.5 | 1e-15 | 34/44 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.548×** | -8.2 | 2e-14 | 34/45 (LoVo, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.586×** | -8.0 | 8e-14 | 34/41 (LoVo, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.617×** | -7.8 | 3e-13 | 30/44 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.637×** | -7.3 | 1e-11 | 34/44 (SHP-77, COLO 205, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -6.7 | 6e-10 | 27/44 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.498×** | -5.5 | 8e-07 | 33/44 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.498×** | -5.5 | 8e-07 | 28/44 (LoVo, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.515×** | -5.3 | 3e-06 | 33/44 (LoVo, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.636×** | -5.2 | 4e-06 | 35/44 (NCI-H23, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.552×** | -4.7 | 5e-05 | 29/44 (LoVo, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.565×** | -4.5 | 1e-04 | 31/44 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.845× | -3.8 | 0.002 | 18/45 (CFPAC-1, SNU-1, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.770×** | -3.7 | 0.003 | 25/44 (LoVo, SHP-77, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.727×** | -3.7 | 0.004 | 28/45 (LoVo, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.730×** | -3.6 | 0.005 | 26/44 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 199 | 0 | 18 (13 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -18.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.207× (z -16.1) |
| [[SNU-1 (line)]] | wt | 1,139 | 0 | 18 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -14.8) |
| [[COLO 205 (line)]] | alt | 459 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -18.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.313× (z -13.8) |
| [[LoVo (line)]] | wt | 651 | 0 | 16 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.329× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 493 | 0 | 15 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -17.4) |
| [[MIA PaCa-2 (line)]] | alt | 145 | 0 | 15 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -15.4) |
| [[SW480 (line)]] | alt | 213 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -17.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.280× (z -14.9) |
| [[KATO III (line)]] | alt | 409 | 0 | 14 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -17.3) |
| [[HepG2_C3A (line)]] | wt | 647 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -19.3) |
| [[SHP-77 (line)]] | alt | 380 | 0 | 12 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -19.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 310 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -17.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -12.5) |
| [[A-427 (line)]] | wt | 228 | 0 | 10 (7 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.335× (z -13.5) |
| [[HT-29 (line)]] | alt | 366 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -13.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 344 | 0 | 9 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -14.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 248 | 0 | 7 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.365× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 212 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -12.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H1792 (line)]] | alt | 243 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.8) |
| [[SNU-423 (line)]] | alt | 337 | 3 (3 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +15.2) ⚠ cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -11.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LS 180 (line)]] | wt | 525 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.460× (z -9.7) |
| [[SW 900 (line)]] | alt | 399 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -11.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.9) |
| [[SW48 (line)]] | wt | 239 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -12.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.279× (z -10.7) |
| [[HCT15 (line)]] | alt | 214 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -12.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.364× (z -9.1) |
| [[HOP62 (line)]] | alt | 231 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +21.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +13.7) | — |
| [[RKO (line)]] | wt | 234 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -13.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 178 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +26.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.39× (z +18.4) | — |
| [[BT-474 (line)]] | alt | 273 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[C-33 A (line)]] | alt | 179 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 379 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 400 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.214× (z -14.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.402× (z -8.6) |
| [[AN3 CA (line)]] | alt | 318 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.267× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 364 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.08× (z +14.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 171 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.04× (z +10.0) | — |
| [[A549 (line)]] | wt | 337 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -13.0) |
| [[Hs 766T (line)]] | wt | 503 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.306× (z -9.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 292 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 162 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.92× (z +11.3) | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.126× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 244 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 73.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.24× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 148 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.98× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 40.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 48.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 313 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERBIN]] | +0.63 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[ATXN7L1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R9A]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[NEDD4L]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[PARD3B]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[FJX1]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ALCAM]] | +0.57 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[NFIB]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[DNAH6]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ATF7IP]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RFX3]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[C11orf96]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNB3]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[RARS2]] | -0.59 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[PCYT1A]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ZFYVE21]] | -0.56 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[ATPAF1]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[WDR37]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[CHFR]] | -0.55 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[DHDDS]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SZT2]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 | same gene group |
| [[RINT1]] | -0.54 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers FOXP1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Temsirolimus) | 62% of the class's compounds vs 4.5% of all compounds | 0.017 | ⚠ off-target possible; 5 compounds |
| [[PDE4D]] | B | PDE4D activity raises FOXP1's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without PDE4D | 0.081 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[DNAH6]] | C | DNAH6 activity raises FOXP1's level | lines that do not express DNAH6 (4) vs lines expressing it (46) | 3.32× lower at baseline in the lines without DNAH6 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IQCM, LINC02932, LINC00907; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, -8.1); signed map (14.8, -12.2). **Vector** length 123, 44.9% of its response variance represented; |z| ≥ 3 in 1,782 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +11.3 | -0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +9.2 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | -3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.2 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.6 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -11.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.6 | -5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -5.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -5.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box P1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p13 — chr3:70,954,693-71,583,978 (-) |
| Ensembl biotype | protein_coding |
| Also known as | QRF1, 12CC4, HSPC215, hFKH1B |
| Gene groups (HGNC) | Forkhead boxes; MicroRNA protein coding host genes |
| Reactome | 1 pathways, smallest: Transcriptional regulation of pluripotent stem cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H334](https://www.uniprot.org/uniprotkb/Q9H334) (Forkhead box protein P1):

> Transcriptional repressor. Can act with CTBP1 to synergistically repress transcription but CTPBP1 is not essential (By similarity). Plays an important role in the specification and differentiation of lung epithelium. Acts cooperatively with FOXP4 to regulate lung secretory epithelial cell fate and regeneration by restricting the goblet cell lineage program; the function may involve regulation of AGR2. Essential transcriptional regulator of B-cell development. Involved in regulation of cardiac …

**Summary**, from NCBI Gene [27086](https://www.ncbi.nlm.nih.gov/gene/27086):

> This gene belongs to subfamily P of the forkhead box (FOX) transcription factor family. Forkhead box transcription factors play important roles in the regulation of tissue- and cell type-specific gene transcription during both development and adulthood. Forkhead box P1 protein contains both DNA-binding- and protein-protein binding-domains. This gene may act as a tumor suppressor as it is lost in several tumor types and maps to a chromosomal region (3p14.1) reported to contain a tumor suppressor …

**Accessions** — [HGNC:3823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3823) · Entrez [27086](https://www.ncbi.nlm.nih.gov/gene/27086) · UniProt [Q9H334](https://www.uniprot.org/uniprotkb/Q9H334) · Ensembl [ENSG00000114861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114861)

## Data

Gene col 3598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3598); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3598]; `tensor/DDL_lfc|DDL_z.npy` [3598]; `embed/gene_vectors.npy` [3598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3598 or target_col == 3598). Every well: [[FOXP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
