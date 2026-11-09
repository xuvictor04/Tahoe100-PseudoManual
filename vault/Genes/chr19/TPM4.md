---
symbol: "TPM4"
type: "gene"
col: 9467
ensembl_id: "ENSG00000167460"
name: "tropomyosin 4"
location: "19p13.12-p13.11"
module: 111
arm: "+"
pooled_cpm: 457.52
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 31
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# TPM4

*tropomyosin 4* — 19p13.12-p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.77× (z +14.8, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 1.35× (z +4.7, q 3e-04, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.359× (z -16.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO1C]] (+0.70, fdr 7e-06), [[MYH9]] (+0.68, fdr 7e-06), [[ACTB]] (+0.67, fdr 7e-06); moves opposite to [[MRPL32]] (-0.56, fdr 2e-05), [[MORN4]] (-0.55, fdr 1e-05), [[RNF135]] (-0.54, fdr 2e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +14.8 | 0e+00 | 49/49 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +14.8 | 0e+00 | 44/44 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +11.1 | 2e-26 | 42/45 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.46×** | +6.1 | 2e-07 | 38/47 (A-172, COLO 205, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.35×** | +4.7 | 3e-04 | 40/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 3e-04 | 36/47 (A-172, COLO 205, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 37/47 (A-172, HT-29, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.29×** | +4.1 | 0.002 | 34/48 (A-172, COLO 205, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.007 | 32/46 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.007 | 28/48 (Panc 03.27, CFPAC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.007 | 20/49 (CFPAC-1, A-172, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.012 | 30/48 (A-172, NCI-H460, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.052 | 32/48 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.15× | +3.2 | 0.064 | 10/48 (HepG2/C3A, LOX-IMVI, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.064 | 7/49 (CHP-212, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9467.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.359×** | -16.5 | 0e+00 | 47/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.506×** | -15.5 | 0e+00 | 42/49 (HepG2/C3A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -14.3 | 3e-44 | 42/48 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.414×** | -14.2 | 1e-43 | 46/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.461×** | -12.5 | 1e-33 | 45/48 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.543×** | -9.5 | 3e-19 | 38/47 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.588×** | -7.7 | 1e-12 | 43/48 (RKO, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.631×** | -7.4 | 8e-12 | 40/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.636×** | -6.9 | 4e-10 | 42/48 (HS-578T, LOX-IMVI, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.664×** | -6.6 | 2e-09 | 39/48 (HS-578T, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.672×** | -6.4 | 8e-09 | 40/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.680×** | -6.2 | 3e-08 | 38/48 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.494×** | -6.0 | 1e-07 | 44/45 (HepG2/C3A, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.729×** | -5.1 | 1e-05 | 37/48 (A549, BT-474, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.727×** | -4.9 | 3e-05 | 34/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.745×** | -4.6 | 2e-04 | 35/49 (HepG2/C3A, SNU-423, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.823×** | -4.4 | 3e-04 | 25/48 (A549, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.752×** | -4.4 | 3e-04 | 27/48 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.602×** | -4.3 | 5e-04 | 35/49 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -4.1 | 9e-04 | 21/48 (A549, BT-474, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.625×** | -4.0 | 0.002 | 31/48 (BT-474, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.631×** | -3.9 | 0.002 | 28/49 (LoVo, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 539 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -26.1) |
| [[SW480 (line)]] | alt | 397 | 2 (2 ⚠) | 10 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.61× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -20.1) |
| [[BT-474 (line)]] | alt | 266 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -19.4) |
| [[NCI-H460 (line)]] | wt | 327 | 3 (3 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.35× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -17.9) |
| [[A549 (line)]] | wt | 400 | 3 (3 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.32× (z +20.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.357× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 503 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -29.6) |
| [[C32 (line)]] | wt | 287 | 2 (2 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.236× (z -15.2) |
| [[HOP62 (line)]] | alt | 397 | 3 (3 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +15.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -13.5) |
| [[HS-578T (line)]] | alt | 1,197 | 3 (3 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +14.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.366× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 767 | 3 (3 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.357× (z -14.1) |
| [[A-172 (line)]] | wt | 834 | 6 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Peretinoin (drug)]] 5 µM 1.86× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.424× (z -12.4) |
| [[C-33 A (line)]] | alt | 305 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.05 µM 3.56× (z +14.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.338× (z -13.1) |
| [[COLO 205 (line)]] | alt | 327 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -27.3) |
| [[KATO III (line)]] | alt | 431 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -20.3) |
| [[LOX-IMVI (line)]] | wt | 521 | 2 (2 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 386 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +12.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.229× (z -16.8) |
| [[HCT15 (line)]] | alt | 768 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -14.5) |
| [[HT-29 (line)]] | alt | 353 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.14× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.227× (z -18.7) |
| [[J82 (line)]] | alt | 432 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +14.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.336× (z -14.0) |
| [[LoVo (line)]] | wt | 277 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -22.8) |
| [[NCI-H1573 (line)]] | alt | 276 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 738 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.36× (z +17.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -18.8) |
| [[SK-MEL-2 (line)]] | alt | 265 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.1) |
| [[SW1417 (line)]] | alt | 456 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +11.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -14.4) |
| [[SW48 (line)]] | wt | 552 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.40× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.324× (z -14.0) |
| [[A-427 (line)]] | wt | 236 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +15.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.354× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 522 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.5) |
| [[Hs 766T (line)]] | wt | 394 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.21× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 502 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -18.8) |
| [[SHP-77 (line)]] | alt | 261 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -14.0) |
| [[SNU-423 (line)]] | alt | 512 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +19.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.490× (z -8.6) |
| [[SW 900 (line)]] | alt | 256 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +12.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -13.6) |
| [[H4 (line)]] | wt | 985 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -13.3) |
| [[LS 180 (line)]] | wt | 657 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 379 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +10.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 555 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -18.2) |
| [[PANC-1 (line)]] | alt | 189 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +15.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 721 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 683 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.66× (z +14.1) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.436× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 246 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +19.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -14.5) |
| [[RKO (line)]] | wt | 629 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.9) |
| [[A498 (line)]] | wt | 537 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +21.2) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 324 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +12.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 394 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 437 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +10.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.1) |
| [[SW 1271 (line)]] | alt | 408 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -10.5) |
| [[NCI-H2122 (line)]] | alt | 384 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 397 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 645 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO1C]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 | STRING 423 |
| [[MYH9]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 | pathway: Signaling by ALK fusions and activated point mutants; STRING 882 |
| [[ACTB]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 | STRING 496 |
| [[WDR1]] | +0.67 | +0.66 / +0.71 | both halves | 7e-06 | STRING 548 |
| [[ACTN1]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 | STRING 677 |
| [[ITGB1]] | +0.65 | +0.65 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[VCL]] | +0.65 | +0.57 / +0.56 | both halves | 1e-05 | pathway: Muscle contraction; STRING 711 |
| [[CSRP1]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[CTNNAL1]] | +0.62 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[MACF1]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ANXA5]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ANXA2]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 | pathway: Muscle contraction |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL32]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[MORN4]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[RNF135]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NELFA]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[COA6]] | -0.53 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ELMOD3]] | -0.53 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[METTL22]] | -0.53 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[THAP3]] | -0.52 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[LRRC37B]] | -0.52 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NDUFB4]] | -0.52 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[FNTB]] | -0.52 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[SAT2]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TPM4's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PHLDB2]] | B | PHLDB2 activity raises TPM4's level | lines that do not express PHLDB2 (11) vs lines expressing it (39) | 1.30× lower at baseline in the lines without PHLDB2 | 0.093 | ⚠ within organs, on part of the lines; also absent: MDFIC, KITLG, CCDC85A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.2, 25.4); signed map (-7.7, 35.3). **Vector** length 104, 42.7% of its response variance represented; |z| ≥ 3 in 1,887 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Platelet activation, signaling and aggregation* (reactome, mean cos +0.51 to 11); *Cell-extracellular matrix interactions* (reactome, mean cos +0.52 to 5); *RHO GTPase Effectors* (reactome, mean cos +0.54 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +14.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.2 | +6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.1 | +4.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.0 | +4.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.9 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | -3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.3 | -9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.9 | -7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.0 | -6.9 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.9 | -3.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | tropomyosin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12-p13.11 — chr19:16,067,021-16,103,002 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Tropomyosins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 10 pathways, smallest: Striated Muscle Contraction; RHOV GTPase cycle; Smooth Muscle Contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P67936](https://www.uniprot.org/uniprotkb/P67936) (Tropomyosin alpha-4 chain):

> Binds to actin filaments in muscle and non-muscle cells. Plays a central role, in association with the troponin complex, in the calcium dependent regulation of vertebrate striated muscle contraction. Smooth muscle contraction is regulated by interaction with caldesmon. In non-muscle cells is implicated in stabilizing cytoskeleton actin filaments (By similarity). Binds calcium. Plays a role in platelet biogenesis.

**Summary**, from NCBI Gene [7171](https://www.ncbi.nlm.nih.gov/gene/7171):

> This gene encodes a member of the tropomyosin family of actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosins are dimers of coiled-coil proteins that polymerize end-to-end along the major groove in most actin filaments. They provide stability to the filaments and regulate access of other actin-binding proteins. In muscle cells, they regulate muscle contraction by controlling the binding of myosin heads to …

**Accessions** — [HGNC:12013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12013) · Entrez [7171](https://www.ncbi.nlm.nih.gov/gene/7171) · UniProt [P67936](https://www.uniprot.org/uniprotkb/P67936) · Ensembl [ENSG00000167460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167460)

## Data

Gene col 9467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9467); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9467]; `tensor/DDL_lfc|DDL_z.npy` [9467]; `embed/gene_vectors.npy` [9467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9467 or target_col == 9467). Every well: [[TPM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
