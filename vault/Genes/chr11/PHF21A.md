---
symbol: "PHF21A"
type: "gene"
col: 5691
ensembl_id: "ENSG00000135365"
name: "PHD finger protein 21A"
location: "11p11.2"
module: 106
arm: "+"
pooled_cpm: 260.4
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 48
n_dd_up_clean: 6
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# PHF21A

*PHD finger protein 21A* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.47× (z +8.0, q 1e-12, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (24 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.410× (z -17.5, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.508× (z -13.8, q 2e-41, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBR5]] (+0.66, fdr 7e-06), [[ACBD5]] (+0.62, fdr 1e-05), [[ATP23]] (+0.61, fdr 2e-05); moves opposite to [[PYCR3]] (-0.60, fdr 1e-05), [[VKORC1L1]] (-0.58, fdr 1e-05), [[SLC35C1]] (-0.58, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLF9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +8.0 | 1e-12 | 37/49 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +5.3 | 3e-05 | 26/48 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +5.2 | 4e-05 | 37/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +4.9 | 2e-04 | 31/48 (NCI-H2347, J82, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.22×** | +4.2 | 0.003 | 25/50 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.007 | 23/49 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.037 | 25/49 (BT-474, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.037 | 21/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.039 | 27/50 (HOP62, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.039 | 14/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.12× | +3.4 | 0.039 | 5/48 (COLO 205, SHP-77, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.039 | 17/49 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.039 | 9/48 (BT-474, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.071 | 17/48 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.071 | 15/49 (HS-578T, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 26 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.410×** | -17.5 | 0e+00 | 42/44 (NCI-H23, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.428×** | -17.4 | 0e+00 | 48/49 (C32, SW 1271, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.410×** | -16.8 | 0e+00 | 43/45 (SNU-423, C32, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.508×** | -13.8 | 2e-41 | 44/48 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.520×** | -13.4 | 1e-38 | 45/48 (SNU-423, C32, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.525×** | -13.1 | 2e-37 | 43/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.532×** | -12.9 | 5e-36 | 36/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.538×** | -12.7 | 6e-35 | 46/48 (NCI-H1792, SNU-423, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.530×** | -12.5 | 6e-34 | 44/47 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.552×** | -12.1 | 4e-32 | 37/48 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.551×** | -11.7 | 7e-30 | 44/47 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.576×** | -11.3 | 1e-27 | 48/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.584×** | -11.0 | 3e-26 | 43/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.620×** | -9.8 | 7e-21 | 42/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.647×** | -8.9 | 3e-17 | 41/48 (SNU-423, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.661×** | -8.4 | 1e-15 | 44/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -8.0 | 3e-14 | 44/48 (NCI-H1573, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.715×** | -6.8 | 2e-10 | 38/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.719×** | -6.7 | 5e-10 | 33/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.801×** | -6.4 | 4e-09 | 32/49 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.750×** | -5.6 | 4e-07 | 36/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.685×** | -5.5 | 8e-07 | 38/48 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.613×** | -5.2 | 4e-06 | 40/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.778×** | -5.1 | 6e-06 | 31/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.619×** | -5.1 | 6e-06 | 39/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.620×** | -5.1 | 6e-06 | 41/46 (H4, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.622×** | -5.1 | 7e-06 | 37/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 516 | 0 | 24 (18 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -25.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -20.2) |
| [[C32 (line)]] | wt | 904 | 0 | 23 (17 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -32.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0828× (z -27.7) |
| [[NCI-H460 (line)]] | wt | 291 | 0 | 23 (16 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.280× (z -18.5) |
| [[NCI-H1573 (line)]] | alt | 294 | 0 | 22 (15 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -22.0) |
| [[NCI-H1792 (line)]] | alt | 410 | 0 | 21 (17 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -34.7) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -18.1) |
| [[HepG2_C3A (line)]] | wt | 266 | 0 | 19 (15 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.156× (z -20.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -13.4) |
| [[SW480 (line)]] | alt | 259 | 0 | 17 (14 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.334× (z -18.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.404× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 332 | 0 | 16 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.168× (z -22.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.257× (z -17.9) |
| [[SK-MEL-2 (line)]] | alt | 386 | 0 | 16 (13 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.237× (z -17.6) |
| [[CFPAC-1 (line)]] | alt | 205 | 0 | 13 (7 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.288× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 388 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0355× (z -46.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 283 | 1 | 10 (9 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.11× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -11.2) |
| [[SW 900 (line)]] | alt | 158 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -14.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -10.4) |
| [[A549 (line)]] | wt | 348 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -27.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.419× (z -12.2) |
| [[LoVo (line)]] | wt | 141 | 2 | 8 (6 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 1.95× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.386× (z -14.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.512× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 253 | 0 | 10 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -21.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.382× (z -11.7) |
| [[SHP-77 (line)]] | alt | 226 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -15.3) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -10.4) |
| [[PANC-1 (line)]] | alt | 327 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.530× (z -11.5) |
| [[SNU-1 (line)]] | wt | 305 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.305× (z -14.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.413× (z -10.7) |
| [[AN3 CA (line)]] | alt | 415 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.316× (z -11.2) |
| [[Hs 766T (line)]] | wt | 250 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.491× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 264 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -12.6) |
| [[C-33 A (line)]] | alt | 425 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -13.6) |
| [[H4 (line)]] | wt | 365 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.252× (z -14.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -12.1) |
| [[RKO (line)]] | wt | 249 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.2) ⚠ cell-cycle shift, explains ~54% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.526× (z -9.2) |
| [[HOP62 (line)]] | alt | 233 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.462× (z -9.8) |
| [[HT-29 (line)]] | alt | 158 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.413× (z -11.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.461× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 229 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -15.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -10.3) |
| [[SW1417 (line)]] | alt | 211 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 314 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.447× (z -11.8) |
| [[COLO 205 (line)]] | alt | 153 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -17.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -10.1) |
| [[HS-578T (line)]] | alt | 227 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 217 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.384× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 142 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.12× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.429× (z -10.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.483× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 155 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.69× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.448× (z -9.7) |
| [[CHP-212 (line)]] | wt | 304 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HCT15 (line)]] | alt | 258 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -10.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 147 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +16.5) ⚠ cell-cycle shift, explains ~54% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -13.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 259 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.387× (z -13.4) |
| [[A498 (line)]] | wt | 181 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.340× (z -13.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 120 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -12.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 125 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.9) ⚠ cell-cycle shift, explains ~54% of this change | [[Auranofin (drug)]] 5 µM 0.375× (z -10.7) |
| [[NCI-H661 (line)]] | alt | 385 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 356 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0352× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.314× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 241 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBR5]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ACBD5]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ATP23]] | +0.61 | +0.47 / +0.61 | both halves | 2e-05 | STRING 902 |
| [[RCOR3]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 | same gene group; STRING 605 |
| [[POLR3GL]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SSBP2]] | +0.60 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[CNTNAP1]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ZNF292]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PER1]] | +0.59 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[CDKN1B]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[BCL6]] | +0.58 | +0.50 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYCR3]] | -0.60 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[VKORC1L1]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[SLC35C1]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ZNF83]] | -0.57 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[GHRLOS]] | -0.56 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[KCNC4]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[RRP7BP-1]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 | pathway: Chromatin modifying enzymes; STRING 604 |
| [[CAPN2]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[KCTD13]] | -0.53 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[TBILA]] | -0.53 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MPP3]] | -0.52 | -0.42 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF9]] | B | KLF9 activity raises PHF21A's level | lines that do not express KLF9 (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without KLF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: NDC80, WDR54, ADGRB2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.3, -25.9); signed map (-6.7, 7.7). **Vector** length 121, 52.2% of its response variance represented; |z| ≥ 3 in 2,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.9 | -0.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +8.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.6 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.5 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +5.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.1 | +2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.7 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.6 | +4.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -16.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -8.6 | -17.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -13.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.8 | -11.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.7 | -12.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -6.1 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.8 | -6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -5.5 | -5.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -5.3 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 21A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:45,929,319-46,121,454 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BHC80, KIAA1696, BM-006 |
| Gene groups (HGNC) | PHD finger proteins; CoREST complex subunits |
| Reactome | 8 pathways, smallest: HDACs deacetylate histones; Potential therapeutics for SARS; Factors involved in megakaryocyte development and platelet production |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BD5](https://www.uniprot.org/uniprotkb/Q96BD5) (PHD finger protein 21A):

> Component of the BHC complex, a corepressor complex that represses transcription of neuron-specific genes in non-neuronal cells. The BHC complex is recruited at RE1/NRSE sites by REST and acts by deacetylating and demethylating specific sites on histones, thereby acting as a chromatin modifier. In the BHC complex, it may act as a scaffold. Inhibits KDM1A-mediated demethylation of 'Lys-4' of histone H3 in vitro, suggesting a role in demethylation regulation.

**Summary**, from NCBI Gene [51317](https://www.ncbi.nlm.nih.gov/gene/51317):

> The PHF21A gene encodes BHC80, a component of a BRAF35 (MIM 605535)/histone deacetylase (HDAC; see MIM 601241) complex (BHC) that mediates repression of neuron-specific genes through the cis-regulatory element known as repressor element-1 (RE1) or neural restrictive silencer (NRS) (Hakimi et al., 2002 [PubMed 12032298]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:24156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24156) · Entrez [51317](https://www.ncbi.nlm.nih.gov/gene/51317) · UniProt [Q96BD5](https://www.uniprot.org/uniprotkb/Q96BD5) · Ensembl [ENSG00000135365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135365)

## Data

Gene col 5691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5691); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5691]; `tensor/DDL_lfc|DDL_z.npy` [5691]; `embed/gene_vectors.npy` [5691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5691 or target_col == 5691). Every well: [[PHF21A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF21A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
