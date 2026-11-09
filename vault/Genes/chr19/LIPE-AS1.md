---
symbol: "LIPE-AS1"
type: "gene"
col: 13146
ensembl_id: "ENSG00000213904"
name: "LIPE antisense RNA 1"
location: "19q13.2"
module: 28
arm: "-"
pooled_cpm: 66.97
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 25
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# LIPE-AS1

*LIPE antisense RNA 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.37× (z +16.9, q 0e+00, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.424× (z -16.9, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02649]] (+0.72, fdr 1e-05), [[TPT1-AS1]] (+0.71, fdr 7e-06), [[EXD3]] (+0.64, fdr 7e-06); moves opposite to [[AASDHPPT]] (-0.58, fdr 6e-04), [[COX11]] (-0.57, fdr 3e-05), [[CILK1]] (-0.56, fdr 6e-04).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +16.9 | 0e+00 | 39/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.37×** | +16.9 | 0e+00 | 37/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +14.9 | 0e+00 | 38/46 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +11.8 | 5e-30 | 34/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +11.0 | 3e-26 | 36/46 (BT-474, KATO III, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +9.4 | 4e-19 | 33/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +7.9 | 2e-13 | 31/46 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 6e-09 | 31/46 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.9 | 2e-07 | 26/46 (HOP62, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.3 | 7e-06 | 23/46 (RKO, NCI-H1792, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.30×** | +5.2 | 1e-05 | 21/46 (BT-474, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +5.1 | 2e-05 | 27/46 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 15/46 (J82, LS 180, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.015 | 16/46 (HS-578T, C-33 A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +3.4 | 0.022 | 19/45 (SW480, A549, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.035 | 13/46 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.424×** | -16.9 | 0e+00 | 41/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.429×** | -16.0 | 0e+00 | 43/46 (SW480, MIA PaCa-2, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.229×** | -15.2 | 0e+00 | 42/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.480×** | -14.4 | 6e-45 | 40/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.246×** | -14.4 | 7e-45 | 40/46 (COLO 205, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.490×** | -13.5 | 2e-39 | 40/45 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.532×** | -12.4 | 2e-33 | 38/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.532×** | -12.4 | 2e-33 | 34/46 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -10.1 | 5e-22 | 31/42 (KATO III, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.620×** | -9.4 | 4e-19 | 32/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.623×** | -9.3 | 7e-19 | 33/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.644×** | -8.6 | 3e-16 | 37/46 (SNU-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.812×** | -5.8 | 3e-07 | 24/46 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **0.749×** | -5.7 | 5e-07 | 27/46 (A-172, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -5.4 | 2e-06 | 27/46 (PANC-1, HCT15, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -4.6 | 1e-04 | 24/46 (PANC-1, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.783×** | -4.5 | 2e-04 | 21/45 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.804×** | -4.3 | 5e-04 | 20/46 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -4.0 | 0.002 | 19/46 (A-172, C32, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **0.820×** | -3.7 | 0.004 | 18/46 (NCI-H1792, A498, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.739×** | -3.1 | 0.043 | 15/46 (NCI-H1792, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 83.8 | 6 | 13 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +12.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -23.4) |
| [[PANC-1 (line)]] | alt | 46.0 | 2 | 13 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +9.1) | [[Digitoxin (drug)]] 0.5 µM 0.182× (z -19.4) |
| [[HT-29 (line)]] | alt | 119 | 3 | 10 (7 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.73× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -14.7) |
| [[KATO III (line)]] | alt | 98.8 | 5 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.61× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 88.9 | 1 | 10 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +9.3) | [[Harringtonine (drug)]] 0.5 µM 0.268× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 196 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.233× (z -16.7) |
| [[A-172 (line)]] | wt | 62.2 | 3 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +12.8) | [[Harringtonine (drug)]] 5 µM 0.215× (z -14.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.285× (z -11.8) |
| [[A549 (line)]] | wt | 86.4 | 4 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +14.7) | [[Harringtonine (drug)]] 0.5 µM 0.181× (z -15.2) |
| [[HOP62 (line)]] | alt | 54.5 | 4 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.310× (z -11.3) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.134× (z -10.6) |
| [[LoVo (line)]] | wt | 78.2 | 2 | 8 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.87× (z +11.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.217× (z -18.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -16.0) |
| [[A-427 (line)]] | wt | 109 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.272× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 266 | 1 (1 ⚠) | 8 (6 ⚠) | [[Selinexor (drug)]] 5 µM 1.67× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0608× (z -35.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0268× (z -24.8) |
| [[A498 (line)]] | wt | 53.4 | 4 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +13.6) | [[Harringtonine (drug)]] 5 µM 0.190× (z -15.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.371× (z -9.3) |
| [[SNU-1 (line)]] | wt | 189 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -11.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0959× (z -10.7) |
| [[C-33 A (line)]] | alt | 173 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0861× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0653× (z -13.0) |
| [[LS 180 (line)]] | wt | 45.5 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.45× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.206× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -12.7) |
| [[BT-474 (line)]] | alt | 50.8 | 2 | 3 | [[Tucidinostat (drug)]] 5 µM 3.47× (z +13.1) | [[Digitoxin (drug)]] 0.5 µM 0.268× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 35.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.46× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.305× (z -10.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 59.4 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.20× (z +10.0) | [[Harringtonine (drug)]] 0.5 µM 0.268× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 49.6 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +8.8) | [[Harringtonine (drug)]] 0.5 µM 0.278× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 21.2 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +18.8) | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0670× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 49.1 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.270× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 33.2 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -8.9) |
| [[SHP-77 (line)]] | alt | 47.3 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.167× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 24.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 64.1 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0422× (z -15.0) |
| [[H4 (line)]] | wt | 69.2 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.169× (z -12.8) |
| [[J82 (line)]] | alt | 34.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 41.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.339× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 102 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.105× (z -12.1) |
| [[SW 900 (line)]] | alt | 59.4 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.5) | [[PH-797804 (drug)]] 5 µM 0.124× (z -8.8) |
| [[SW1417 (line)]] | alt | 44.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -9.1) |
| [[C32 (line)]] | wt | 51.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 32.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 67.9 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +8.5) | [[TAK-901 (drug)]] 5 µM 0.111× (z -9.3) |
| [[SW48 (line)]] | wt | 117 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.287× (z -9.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0316× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1271 (line)]] | alt | 76.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0814× (z -9.7) |
| [[AN3 CA (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 49.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02649]] | +0.72 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | +0.71 | +0.60 / +0.66 | both halves | 7e-06 | same gene group |
| [[EXD3]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TPTEP2-CSNK1E]] | +0.58 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[RABGEF1]] | +0.57 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[TTLL3]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SLC37A3]] | +0.56 | +0.15 / +0.71 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZNF143]] | +0.54 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[PPP1R32]] | +0.52 | +0.26 / +0.54 | both halves | 4e-04 |  |
| [[CATSPERG]] | +0.52 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LMBR1]] | +0.52 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[DRD4]] | +0.52 | +0.32 / +0.54 | both halves | 2e-04 |  |
| [[KCNK6]] | +0.51 | +0.22 / +0.57 | both halves | 6e-04 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AASDHPPT]] | -0.58 | -0.22 / -0.62 | both halves | 6e-04 |  |
| [[COX11]] | -0.57 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CILK1]] | -0.56 | -0.22 / -0.68 | both halves | 6e-04 |  |
| [[ZNF772]] | -0.56 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[EXOSC10]] | -0.55 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[MDM1]] | -0.54 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[SCRN3]] | -0.54 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[AIFM1]] | -0.53 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[AMACR]] | -0.53 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[TTC30A]] | -0.52 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[PAIP1]] | -0.51 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[ACTR8]] | -0.51 | -0.36 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LIPE-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.432). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (20.7, -18.1); signed map (6.4, 10.5). **Vector** length 78.6, 20.6% of its response variance represented; |z| ≥ 3 in 1,481 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +14.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | -2.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -15.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | -14.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -12.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.6 | -16.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | LIPE antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.2 — chr19:42,397,114-42,652,367 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48589) · Entrez [100996307](https://www.ncbi.nlm.nih.gov/gene/100996307) · Ensembl [ENSG00000213904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213904)

## Data

Gene col 13146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13146); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13146]; `tensor/DDL_lfc|DDL_z.npy` [13146]; `embed/gene_vectors.npy` [13146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13146 or target_col == 13146). Every well: [[LIPE-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIPE-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
