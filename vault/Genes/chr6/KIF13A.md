---
symbol: "KIF13A"
type: "gene"
col: 5980
ensembl_id: "ENSG00000137177"
name: "kinesin family member 13A"
location: "6p22.3"
module: 92
arm: "+"
pooled_cpm: 182.97
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# KIF13A

*kinesin family member 13A* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.30× (z +6.4, q 7e-08, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.460× (z -27.5, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDSUB1]] (+0.66, fdr 7e-06), [[MLLT10]] (+0.61, fdr 7e-06), [[RNF130]] (+0.57, fdr 1e-05); moves opposite to [[ZNF597]] (-0.63, fdr 2e-05), [[SPRY4]] (-0.58, fdr 3e-05), [[CCNT1]] (-0.58, fdr 1e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +6.4 | 7e-08 | 32/46 (C32, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.28×** | +6.2 | 1e-07 | 33/49 (C32, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 6e-04 | 21/47 (C32, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.19× | +4.4 | 0.002 | 18/48 (C32, HOP62, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.3 | 0.002 | 11/47 (C32, RKO, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +4.3 | 0.002 | 19/48 (C32, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +4.0 | 0.005 | 7/47 (C32, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.011 | 14/46 (C32, NCI-H2347, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.020 | 24/47 (C32, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.027 | 21/49 (C32, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +3.4 | 0.036 | 17/47 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.039 | 12/47 (C32, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.039 | 17/47 (C32, HOP62, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.3 | 0.039 | 6/47 (BT-474, CFPAC-1, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.039 | 15/48 (C32, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.039 | 15/47 (C32, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.460×** | -27.5 | 0e+00 | 45/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.353×** | -26.1 | 0e+00 | 47/47 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.357×** | -25.8 | 0e+00 | 47/47 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.409×** | -21.6 | 0e+00 | 40/43 (LS 180, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.424×** | -21.5 | 0e+00 | 46/47 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.433×** | -21.0 | 0e+00 | 44/48 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.621×** | -16.9 | 0e+00 | 35/47 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.529×** | -15.4 | 0e+00 | 42/49 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.518×** | -15.2 | 0e+00 | 39/44 (HepG2/C3A, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.559×** | -14.6 | 0e+00 | 38/47 (HT-29, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.571×** | -13.5 | 1e-39 | 42/47 (HS-578T, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.614×** | -12.2 | 1e-32 | 37/47 (SW48, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.709×** | -12.2 | 2e-32 | 37/47 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.627×** | -11.3 | 9e-28 | 42/46 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.667×** | -10.1 | 2e-22 | 39/47 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.683×** | -9.5 | 6e-20 | 38/47 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.564×** | -7.5 | 2e-12 | 33/48 (LoVo, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.804×** | -5.4 | 1e-06 | 26/47 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -4.5 | 2e-04 | 13/47 (PANC-1, A498, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.862× | -3.7 | 0.005 | 15/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.870× | -3.5 | 0.011 | 11/47 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.770×** | -3.4 | 0.013 | 18/46 (SW48, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | 0.885× | -3.0 | 0.047 | 5/47 (SW 1088, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 269 | 14 (1 ⚠) | 9 (7 ⚠) | [[Binimetinib (drug)]] 5 µM 2.65× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 215 | 1 (1 ⚠) | 17 (10 ⚠) | [[Trametinib (drug)]] 5 µM 1.88× (z +9.3) ⚠ cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -24.1) |
| [[MIA PaCa-2 (line)]] | alt | 163 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -23.4) |
| [[HOP62 (line)]] | alt | 217 | 2 (1 ⚠) | 15 (8 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.09× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.294× (z -16.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.298× (z -16.4) |
| [[A-172 (line)]] | wt | 233 | 0 | 16 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -19.1) |
| [[NCI-H2347 (line)]] | alt | 176 | 0 | 15 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -24.0) |
| [[NCI-H460 (line)]] | wt | 150 | 0 | 15 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -19.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -18.3) |
| [[SNU-423 (line)]] | alt | 430 | 0 | 15 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -23.0) |
| [[CFPAC-1 (line)]] | alt | 187 | 0 | 14 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -25.6) |
| [[HS-578T (line)]] | alt | 314 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -26.3) |
| [[LoVo (line)]] | wt | 136 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -23.9) |
| [[Hs 766T (line)]] | wt | 149 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -17.7) |
| [[LS 180 (line)]] | wt | 278 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -26.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.225× (z -23.6) |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 237 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -23.6) |
| [[NCI-H23 (line)]] | alt | 209 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -24.4) |
| [[RPMI-7951 (line)]] | alt | 228 | 0 | 10 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.369× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 189 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -18.5) |
| [[SNU-1 (line)]] | wt | 256 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.462× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 258 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.237× (z -18.1) |
| [[HT-29 (line)]] | alt | 126 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -15.4) |
| [[J82 (line)]] | alt | 329 | 1 (1 ⚠) | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 96.3 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -26.4) |
| [[NCI-H2030 (line)]] | alt | 252 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -27.3) |
| [[SW 900 (line)]] | alt | 151 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -13.3) |
| [[A498 (line)]] | wt | 139 | 2 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.297× (z -18.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -17.9) |
| [[HCT15 (line)]] | alt | 220 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -18.4) |
| [[hTERT-HPNE (line)]] | wt | 244 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -13.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.315× (z -11.9) |
| [[PANC-1 (line)]] | alt | 212 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -29.2) |
| [[SW1417 (line)]] | alt | 161 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -16.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.298× (z -15.5) |
| [[SW480 (line)]] | alt | 92.3 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -18.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -16.8) |
| [[C-33 A (line)]] | alt | 260 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.353× (z -11.4) |
| [[SW48 (line)]] | wt | 154 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -20.3) |
| [[A-427 (line)]] | wt | 162 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -17.7) |
| [[A549 (line)]] | wt | 150 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -22.1) |
| [[AN3 CA (line)]] | alt | 302 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 130 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 132 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -17.4) |
| [[H4 (line)]] | wt | 167 | 1 | 4 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.18× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -14.8) |
| [[KATO III (line)]] | alt | 121 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -16.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.374× (z -13.3) |
| [[RKO (line)]] | wt | 98.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -13.0) |
| [[NCI-H661 (line)]] | alt | 285 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -10.0) |
| [[SW 1271 (line)]] | alt | 224 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.174× (z -10.8) |
| [[BT-474 (line)]] | alt | 124 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -10.9) |
| [[CHP-212 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.268× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 209 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDSUB1]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MLLT10]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RNF130]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[TENT4B]] | +0.57 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[RHOT1]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[MAP3K2]] | +0.55 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[HSF2]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[BMPR1A]] | +0.54 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[PLPP1]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[TBC1D12]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TRIM37]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[DSTYK]] | +0.52 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF597]] | -0.63 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[SPRY4]] | -0.58 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[CCNT1]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[MCL1]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SLC30A7]] | -0.57 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[CDC42EP2]] | -0.56 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[EGR3]] | -0.55 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[LINC02458]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SPRY2]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[LINC01844]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[LINC02454]] | -0.54 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KIF13A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAB32]] | B | RAB32 activity raises KIF13A's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 1.76× lower at baseline in the lines without RAB32 | 0.058 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[NT5E]] | B | NT5E activity raises KIF13A's level | lines that do not express NT5E (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without NT5E | 0.059 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[DCBLD2]] | B | DCBLD2 activity strengthens KIF13A's drug response | lines that do not express DCBLD2 (9) vs lines expressing it (40) | the lines without DCBLD2 respond 0.81× as strongly (z diff +1.73); strongest at Dinaciclib 5 µM: 0.56x vs 0.41x (z diff +3.0) | 0.065 | ⚠ within organs, on part of the lines; also absent: C12orf75, ST3GAL6, OSBPL6; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[C11orf91]] | B | C11orf91 activity raises KIF13A's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without C11orf91 | 0.075 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[LINC02454]] | B | LINC02454 activity raises KIF13A's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without LINC02454 | 0.089 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[HMGA2]] | B | HMGA2 activity raises KIF13A's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 1.42× lower at baseline in the lines without HMGA2 | 0.095 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[ELK3]] | C | ELK3 activity raises KIF13A's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without ELK3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction -0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.8, -9.4); signed map (-27.7, -11.8). **Vector** length 105, 37.6% of its response variance represented; |z| ≥ 3 in 1,637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +6.7 | +4.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +6.6 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.2 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +6.1 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.7 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +6.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -6.5 | -15.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -5.1 | -21.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.1 | -15.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 13A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:17,759,183-17,987,635 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA500C11.2, RBKIN |
| Gene groups (HGNC) | Kinesins |
| Reactome | 3 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1H9](https://www.uniprot.org/uniprotkb/Q9H1H9) (Kinesin-like protein KIF13A):

> Plus end-directed microtubule-dependent motor protein involved in intracellular transport and regulating various processes such as mannose-6-phosphate receptor (M6PR) transport to the plasma membrane, endosomal sorting during melanosome biogenesis and cytokinesis. Mediates the transport of M6PR-containing vesicles from trans-Golgi network to the plasma membrane via direct interaction with the AP-1 complex. During melanosome maturation, required for delivering melanogenic enzymes from recycling …

**Summary**, from NCBI Gene [63971](https://www.ncbi.nlm.nih.gov/gene/63971):

> This gene encodes a member of the kinesin family of microtubule-based motor proteins that function in the positioning of endosomes. This family member can direct mannose-6-phosphate receptor-containing vesicles from the trans-Golgi network to the plasma membrane, and it is necessary for the steady-state distribution of late endosomes/lysosomes. It is also required for the translocation of FYVE-CENT and TTC19 from the centrosome to the midbody during cytokinesis, and it plays a role in …

**Accessions** — [HGNC:14566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14566) · Entrez [63971](https://www.ncbi.nlm.nih.gov/gene/63971) · UniProt [Q9H1H9](https://www.uniprot.org/uniprotkb/Q9H1H9) · Ensembl [ENSG00000137177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137177)

## Data

Gene col 5980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5980); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5980]; `tensor/DDL_lfc|DDL_z.npy` [5980]; `embed/gene_vectors.npy` [5980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5980 or target_col == 5980). Every well: [[KIF13A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF13A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
