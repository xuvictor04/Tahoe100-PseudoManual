---
symbol: "SPTLC2"
type: "gene"
col: 1995
ensembl_id: "ENSG00000100596"
name: "serine palmitoyltransferase long chain base subunit 2"
location: "14q24.3"
module: 77
arm: "+"
pooled_cpm: 123.26
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# SPTLC2

*serine palmitoyltransferase long chain base subunit 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.69× (z +15.1, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.523× (z -18.0, q 0e+00, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.688× (z -15.3, q 0e+00, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.71, fdr 4e-05), [[CORO2A]] (+0.71, fdr 7e-06), [[LPCAT4]] (+0.69, fdr 1e-05); moves opposite to [[TIA1]] (-0.72, fdr 1e-05), [[DCAF8]] (-0.68, fdr 2e-05), [[MED12]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TMEM92]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +15.1 | 0e+00 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +12.7 | 1e-34 | 40/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +11.8 | 5e-30 | 38/48 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +7.4 | 3e-11 | 30/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +6.1 | 1e-07 | 26/48 (SW480, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +5.8 | 8e-07 | 23/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +5.6 | 1e-06 | 23/49 (NCI-H2030, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +5.5 | 3e-06 | 22/47 (C32, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +5.4 | 5e-06 | 16/49 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.20× | +5.2 | 1e-05 | 21/48 (NCI-H1792, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.9 | 4e-05 | 19/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +4.8 | 7e-05 | 21/47 (PANC-1, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.18× | +4.5 | 4e-04 | 20/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.13× | +3.7 | 0.010 | 15/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.4 | 0.028 | 3/48 (RKO, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.030 | 9/47 (C32, NCI-H1792, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.12× | +3.3 | 0.035 | 10/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | 1.11× | +3.0 | 0.094 | 8/48 (MIA PaCa-2, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1995.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -18.0 | 0e+00 | 36/44 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.565×** | -16.5 | 0e+00 | 39/49 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.688×** | -15.3 | 0e+00 | 35/48 (HS-578T, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.568×** | -13.1 | 5e-37 | 32/45 (Panc 03.27, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.642×** | -12.3 | 1e-32 | 39/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.665×** | -11.8 | 4e-30 | 36/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -9.3 | 8e-19 | 26/49 (HT-29, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.802×** | -9.0 | 2e-17 | 31/48 (A-172, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.786×** | -6.7 | 2e-09 | 27/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.831×** | -5.1 | 2e-05 | 19/48 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | 0.842× | -5.0 | 4e-05 | 23/48 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.856× | -4.5 | 4e-04 | 19/48 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.854× | -4.4 | 5e-04 | 19/47 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.862× | -4.3 | 7e-04 | 20/48 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.958× | -4.3 | 8e-04 | 3/50 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.886× | -4.1 | 0.002 | 13/48 (C32, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.875× | -3.8 | 0.004 | 18/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.912× | -3.8 | 0.005 | 3/48 (J82, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.879× | -3.7 | 0.005 | 14/47 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.913× | -3.7 | 0.005 | 4/48 (J82, A549, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.910× | -3.7 | 0.005 | 3/49 (C32, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.893× | -3.1 | 0.037 | 15/48 (C32, SK-MEL-2, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.817×** | -3.1 | 0.046 | 20/48 (MIA PaCa-2, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 98.7 | 8 | 10 (7 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.29× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.389× (z -12.6) |
| [[HOP62 (line)]] | alt | 108 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.367× (z -13.7) |
| [[HS-578T (line)]] | alt | 111 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -22.0) |
| [[A-172 (line)]] | wt | 122 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.448× (z -15.1) |
| [[KATO III (line)]] | alt | 99.3 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 277 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.9) |
| [[LoVo (line)]] | wt | 140 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.473× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 120 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.499× (z -14.3) |
| [[SW480 (line)]] | alt | 119 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 189 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -10.9) |
| [[PANC-1 (line)]] | alt | 71.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.92× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.601× (z -8.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 155 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -12.7) |
| [[LS 180 (line)]] | wt | 144 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 59.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -10.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 170 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0602× (z -35.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.567× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 98.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.7) |
| [[A498 (line)]] | wt | 103 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -9.3) |
| [[Hs 766T (line)]] | wt | 102 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.555× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.644× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 151 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 106 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.586× (z -9.1) |
| [[A-427 (line)]] | wt | 91.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.96× (z +9.6) | — |
| [[A549 (line)]] | wt | 126 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.7) |
| [[BT-474 (line)]] | alt | 122 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.125× (z -14.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.431× (z -10.7) |
| [[C32 (line)]] | wt | 83.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.529× (z -8.6) |
| [[H4 (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -15.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -14.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 138 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -16.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.541× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -19.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 73.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.436× (z -8.9) |
| [[SW 900 (line)]] | alt | 86.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -16.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 270 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -12.3) |
| [[COLO 205 (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.2) |
| [[HT-29 (line)]] | alt | 226 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -14.6) |
| [[SHP-77 (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -14.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 151 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.46× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.71 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[CORO2A]] | +0.71 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[LPCAT4]] | +0.69 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[TWF2]] | +0.68 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[FLNB]] | +0.66 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[INPP5F]] | +0.66 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[KIF21B]] | +0.66 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[PBX4]] | +0.65 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CYTH3]] | +0.64 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PCMT1]] | +0.64 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[MYO9B]] | +0.64 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[RASA2]] | +0.64 | +0.69 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.72 | -0.71 / -0.56 | both halves | 1e-05 |  |
| [[DCAF8]] | -0.68 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[MED12]] | -0.67 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[GALNT7-DT]] | -0.66 | -0.64 / -0.22 | both halves | 6e-04 |  |
| [[BAZ2B]] | -0.66 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[OXA1L-DT]] | -0.66 | -0.63 / -0.27 | both halves | 3e-04 |  |
| [[TMEM202-AS1]] | -0.64 | -0.64 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[ZFP91]] | -0.64 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MFF-DT]] | -0.64 | -0.60 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[TTC32]] | -0.64 | -0.65 / -0.23 | both halves | 5e-04 |  |
| [[ZNF764]] | -0.63 | -0.64 / -0.34 | both halves | 1e-04 |  |
| [[CASD1]] | -0.63 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[LINC00240]] | -0.63 | -0.66 / -0.22 | both halves | 6e-04 |  |
| [[C11orf58]] | -0.63 | -0.61 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92]] | B | TMEM92 activity raises SPTLC2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.26× lower at baseline in the lines without TMEM92 | 0.028 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[PAQR5]] | B | PAQR5 activity raises SPTLC2's level | lines that do not express PAQR5 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without PAQR5 | 0.035 | ⚠ within organs, on part of the lines; also absent: ADORA2B |
| [[KIF21B]] | B | KIF21B activity raises SPTLC2's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without KIF21B | 0.046 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CARD11]] | B | CARD11 activity raises SPTLC2's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.23× lower at baseline in the lines without CARD11 | 0.065 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[KRT81]] | B | KRT81 activity raises SPTLC2's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 1.21× lower at baseline in the lines without KRT81 | 0.071 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9 |
| [[HDAC6]] | B | HDAC6 activity lowers SPTLC2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (6.0, 4.6); signed map (-20.7, 34.7). **Vector** length 134, 40.8% of its response variance represented; |z| ≥ 3 in 1,470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +9.8 | +11.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +9.6 | +12.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +9.5 | +15.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.5 | +7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.6 | -15.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -11.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.2 | -12.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.7 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -13.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -9.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.6 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | serine palmitoyltransferase long chain base subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,505,997-77,616,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0526, LCB2, LCB2A, hLCB2a |
| Gene groups (HGNC) | Serine palmitoyltransferase long chain base subunits |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O15270](https://www.uniprot.org/uniprotkb/O15270) (Serine palmitoyltransferase 2):

> Component of the serine palmitoyltransferase multisubunit enzyme (SPT) that catalyzes the initial and rate-limiting step in sphingolipid biosynthesis by condensing L-serine and activated acyl-CoA (most commonly palmitoyl-CoA) to form long-chain bases. The SPT complex is composed of SPTLC1, SPTLC2 or SPTLC3 and SPTSSA or SPTSSB. Within this complex, the heterodimer consisting of SPTLC1 and SPTLC2/SPTLC3 forms the catalytic core. The composition of the serine palmitoyltransferase (SPT) complex …

**Summary**, from NCBI Gene [9517](https://www.ncbi.nlm.nih.gov/gene/9517):

> This gene encodes a long chain base subunit of serine palmitoyltransferase. Serine palmitoyltransferase, which consists of two different subunits, is the key enzyme in sphingolipid biosynthesis. It catalyzes the pyridoxal-5-prime-phosphate-dependent condensation of L-serine and palmitoyl-CoA to 3-oxosphinganine. Mutations in this gene were identified in patients with hereditary sensory neuropathy type I. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:11278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11278) · Entrez [9517](https://www.ncbi.nlm.nih.gov/gene/9517) · UniProt [O15270](https://www.uniprot.org/uniprotkb/O15270) · Ensembl [ENSG00000100596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100596)

## Data

Gene col 1995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1995); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1995]; `tensor/DDL_lfc|DDL_z.npy` [1995]; `embed/gene_vectors.npy` [1995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1995 or target_col == 1995). Every well: [[SPTLC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTLC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
