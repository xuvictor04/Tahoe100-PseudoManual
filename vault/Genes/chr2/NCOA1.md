---
symbol: "NCOA1"
type: "gene"
col: 1406
ensembl_id: "ENSG00000084676"
name: "nuclear receptor coactivator 1"
location: "2p23.3"
module: 74
arm: "+"
pooled_cpm: 182.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# NCOA1

*nuclear receptor coactivator 1* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +8.6, q 3e-15, up in 27 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.387× (z -25.1, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.540× (z -16.3, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD2B]] (+0.63, fdr 1e-05), [[ITSN2]] (+0.62, fdr 1e-05), [[CCDC126]] (+0.60, fdr 1e-05); moves opposite to [[GCN1]] (-0.59, fdr 1e-05), [[LINC03009]] (-0.58, fdr 4e-05), [[CORO1C]] (-0.57, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MLPH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +8.6 | 3e-15 | 27/49 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +8.2 | 7e-14 | 25/48 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +6.5 | 2e-08 | 29/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.25×** | +5.3 | 1e-05 | 35/50 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +4.9 | 1e-04 | 23/48 (SHP-77, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +4.8 | 2e-04 | 15/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +4.7 | 2e-04 | 24/48 (SW480, A-427, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +4.5 | 4e-04 | 21/49 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.20× | +4.5 | 4e-04 | 21/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +4.5 | 4e-04 | 21/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +4.5 | 4e-04 | 8/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.4 | 5e-04 | 23/48 (H4, SHP-77, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.17× | +4.2 | 0.001 | 16/49 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +4.0 | 0.003 | 16/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +3.8 | 0.006 | 9/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.015 | 17/50 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.034 | 10/49 (SW480, A498, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.2 | 0.037 | 1/48 (SK-MEL-2) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.387×** | -25.1 | 0e+00 | 48/49 (A-427, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.387×** | -24.1 | 0e+00 | 44/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.445×** | -19.8 | 0e+00 | 43/45 (Panc 03.27, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.540×** | -16.3 | 0e+00 | 44/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.702×** | -9.3 | 1e-18 | 42/48 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -8.4 | 3e-15 | 31/47 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.775×** | -6.7 | 1e-09 | 33/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.580×** | -6.6 | 2e-09 | 31/38 (HS-578T, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.783×** | -6.5 | 7e-09 | 29/48 (A549, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.818×** | -5.3 | 6e-06 | 22/48 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.827×** | -5.0 | 3e-05 | 23/48 (SNU-423, Panc 03.27, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.681×** | -4.7 | 1e-04 | 27/49 (NCI-H23, A498, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.838× | -4.5 | 3e-04 | 19/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.702×** | -4.3 | 6e-04 | 27/48 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.715×** | -4.1 | 0.002 | 25/48 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.744×** | -3.6 | 0.010 | 22/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.875× | -3.5 | 0.013 | 17/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.877× | -3.5 | 0.016 | 9/49 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.839× | -3.3 | 0.024 | 18/48 (PANC-1, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.763×** | -3.3 | 0.024 | 19/48 (NCI-H1573, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.887× | -3.2 | 0.037 | 12/48 (NCI-H1573, MIA PaCa-2, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.919× | -3.1 | 0.037 | 5/49 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.884× | -3.1 | 0.037 | 10/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.891× | -3.0 | 0.049 | 7/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.894× | -3.0 | 0.063 | 14/48 (NCI-H1573, NCI-H2030, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 269 | 0 | 15 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -24.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.360× (z -16.2) |
| [[SW480 (line)]] | alt | 248 | 2 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.359× (z -20.6) |
| [[NCI-H1573 (line)]] | alt | 258 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.545× (z -10.7) |
| [[C32 (line)]] | wt | 208 | 3 (1 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -11.8) |
| [[HS-578T (line)]] | alt | 156 | 0 | 8 (7 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0317× (z -22.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -13.2) |
| [[SW1417 (line)]] | alt | 241 | 1 | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -20.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.568× (z -10.0) |
| [[A-172 (line)]] | wt | 235 | 2 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.452× (z -14.0) |
| [[A549 (line)]] | wt | 307 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -27.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 217 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.516× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 160 | 2 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.236× (z -19.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.317× (z -16.0) |
| [[NCI-H23 (line)]] | alt | 202 | 0 | 7 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.404× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 210 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -26.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.437× (z -12.5) |
| [[A498 (line)]] | wt | 172 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -15.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 163 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +10.3) | [[Auranofin (drug)]] 5 µM 0.306× (z -16.4) |
| [[SNU-423 (line)]] | alt | 171 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -11.9) |
| [[H4 (line)]] | wt | 119 | 4 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 150 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -14.7) |
| [[HepG2_C3A (line)]] | wt | 164 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 154 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.436× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 198 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 184 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -28.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.564× (z -10.5) |
| [[SHP-77 (line)]] | alt | 219 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.473× (z -10.2) |
| [[A-427 (line)]] | wt | 315 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -39.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.575× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 207 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.417× (z -12.2) |
| [[HOP62 (line)]] | alt | 144 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.442× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.497× (z -9.4) |
| [[HT-29 (line)]] | alt | 124 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -12.9) |
| [[LS 180 (line)]] | wt | 137 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 201 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.563× (z -10.5) |
| [[SW 900 (line)]] | alt | 123 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.445× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.484× (z -8.9) |
| [[AN3 CA (line)]] | alt | 278 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -12.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 135 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[ULK-101 (drug)]] 5 µM 0.0700× (z -9.1) |
| [[SNU-1 (line)]] | wt | 194 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.456× (z -9.0) |
| [[C-33 A (line)]] | alt | 233 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.460× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 206 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -12.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -11.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 76.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.499× (z -8.6) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 316 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 226 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 231 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.267× (z -8.6) |
| [[BT-474 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.4) | — |
| [[J82 (line)]] | alt | 98.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.505× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0754× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 147 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.462× (z -9.1) |
| [[SW48 (line)]] | wt | 166 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.402× (z -9.5) |
| [[COLO 205 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD2B]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ITSN2]] | +0.62 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[CCDC126]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PIK3CA]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 | pathway: ESR-mediated signaling |
| [[UVRAG]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[WDFY3]] | +0.59 | +0.43 / +0.57 | both halves | 4e-05 | STRING 528 |
| [[EIF1B]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[DSTYK]] | +0.59 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[FDX2]] | +0.58 | +0.48 / +0.51 | both halves | 2e-05 | pathway: Biological oxidations |
| [[FBXO6]] | +0.58 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[HECTD4]] | +0.58 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SMDT1]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCN1]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[LINC03009]] | -0.58 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[CORO1C]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[BCAN-AS2]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ZNF587B]] | -0.54 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[NOC2L]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[NCBP1]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SLC19A1]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[NORAD]] | -0.52 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[ATG16L1]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[RFT1]] | -0.52 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[EBNA1BP2]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLPH]] | B | MLPH activity lowers NCOA1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.41× higher at baseline in the lines without MLPH | 0.041 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[SHOX2]] | B | SHOX2 activity raises NCOA1's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.33× lower at baseline in the lines without SHOX2 | 0.046 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[LINC01237]] | B | LINC01237 activity raises NCOA1's level | lines that do not express LINC01237 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without LINC01237 | 0.046 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.8, -26.9); signed map (-9.5, 9.5). **Vector** length 124, 41.9% of its response variance represented; |z| ≥ 3 in 1,421 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.8 | +4.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.8 | +5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.7 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +6.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.4 | +4.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.9 | -16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.6 | -19.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.8 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.3 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor coactivator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,491,254-24,770,702 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRC1, F-SRC-1, NCoA-1, KAT13A, RIP160, bHLHe74 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Lysine acetyltransferases; PAS domain containing |
| Reactome | 48 pathways, smallest: NR1H2 & NR1H3 regulate gene expression to control bile acid homeostasis; Synthesis of bile acids and bile salts via 27-hydroxycholesterol; Recycling of bile acids and salts |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15788](https://www.uniprot.org/uniprotkb/Q15788) (Nuclear receptor coactivator 1):

> Nuclear receptor coactivator that directly binds nuclear receptors and stimulates the transcriptional activities in a hormone-dependent fashion. Involved in the coactivation of different nuclear receptors, such as for steroids (PGR, GR and ER), retinoids (RXRs), thyroid hormone (TRs) and prostanoids (PPARs). Also involved in coactivation mediated by STAT3, STAT5A, STAT5B and STAT6 transcription factors. Displays histone acetyltransferase activity toward H3 and H4; the relevance of such activity …

**Summary**, from NCBI Gene [8648](https://www.ncbi.nlm.nih.gov/gene/8648):

> The protein encoded by this gene acts as a transcriptional coactivator for steroid and nuclear hormone receptors. It is a member of the p160/steroid receptor coactivator (SRC) family and like other family members has histone acetyltransferase activity and contains a nuclear localization signal, as well as bHLH and PAS domains. The product of this gene binds nuclear receptors directly and stimulates the transcriptional activities in a hormone-dependent fashion. Alternatively spliced transcript …

**Accessions** — [HGNC:7668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7668) · Entrez [8648](https://www.ncbi.nlm.nih.gov/gene/8648) · UniProt [Q15788](https://www.uniprot.org/uniprotkb/Q15788) · Ensembl [ENSG00000084676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084676)

## Data

Gene col 1406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1406); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1406]; `tensor/DDL_lfc|DDL_z.npy` [1406]; `embed/gene_vectors.npy` [1406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1406 or target_col == 1406). Every well: [[NCOA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCOA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
