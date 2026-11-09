---
symbol: "CDC27"
type: "gene"
col: 57
ensembl_id: "ENSG00000004897"
name: "cell division cycle 27"
location: "17q21.32"
module: 22
arm: "+"
pooled_cpm: 195.12
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CDC27

*cell division cycle 27* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.82× (z +14.8, q 0e+00, up in 43 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.70× (z +13.2, q 4e-37, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.567× (z -14.1, q 3e-42, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD5]] (+0.65, fdr 7e-06), [[MTF2]] (+0.59, fdr 1e-05), [[G2E3]] (+0.57, fdr 1e-05); moves opposite to [[DDX5]] (-0.51, fdr 8e-05), [[TAX1BP3]] (-0.49, fdr 4e-05), [[ELK4]] (-0.49, fdr 6e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 57.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +14.8 | 0e+00 | 43/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +13.2 | 4e-37 | 40/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +12.3 | 2e-32 | 45/49 (LoVo, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.43×** | +11.5 | 2e-28 | 42/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +9.2 | 5e-18 | 37/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +8.1 | 6e-14 | 37/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +6.1 | 6e-08 | 25/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.27×** | +5.6 | 1e-06 | 27/48 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +5.5 | 2e-06 | 28/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +5.0 | 3e-05 | 29/48 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.7 | 2e-04 | 24/38 (SW 900, SW480, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.40×** | +4.3 | 8e-04 | 29/47 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.13× | +4.2 | 0.001 | 20/48 (PANC-1, A549, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 1.19× | +4.1 | 0.002 | 22/47 (NCI-H23, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.003 | 22/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.072 | 15/48 (KATO III, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.072 | 6/48 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.13× | +3.0 | 0.074 | 20/48 (SW480, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.088 | 13/49 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 57.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.567×** | -14.1 | 3e-42 | 45/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.558×** | -13.9 | 1e-41 | 38/44 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -13.7 | 1e-40 | 36/49 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.597×** | -12.8 | 2e-35 | 46/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.544×** | -11.5 | 2e-28 | 44/49 (RKO, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.762×** | -9.6 | 1e-19 | 34/48 (A-172, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.663×** | -9.4 | 3e-19 | 36/45 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.704×** | -8.7 | 2e-16 | 37/48 (SW 900, Hs 766T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.827×** | -6.7 | 1e-09 | 25/48 (A-172, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -6.3 | 2e-08 | 0/50 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.800×** | -5.6 | 1e-06 | 31/48 (J82, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.818×** | -4.8 | 7e-05 | 24/48 (SNU-423, H4, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.829×** | -4.7 | 1e-04 | 23/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.823×** | -4.7 | 1e-04 | 26/50 (SNU-423, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.837× | -4.4 | 4e-04 | 24/48 (A-172, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.845× | -4.2 | 8e-04 | 21/48 (SW 900, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.844× | -3.9 | 0.003 | 20/47 (HS-578T, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.874× | -3.2 | 0.033 | 19/48 (NCI-H2347, hTERT-HPNE, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.915× | -3.2 | 0.039 | 6/48 (HOP62, J82, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.887× | -3.0 | 0.061 | 10/48 (SHP-77, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.903× | -2.9 | 0.086 | 6/48 (RKO, SW 900, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 57. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 222 | 10 (5 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.12× (z +21.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.79× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.525× (z -12.2) |
| [[PANC-1 (line)]] | alt | 126 | 10 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +19.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +19.2) | [[Panobinostat (drug)]] 5 µM 0.522× (z -10.1) |
| [[A498 (line)]] | wt | 230 | 3 (3 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -16.9) |
| [[NCI-H23 (line)]] | alt | 213 | 10 (5 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.61× (z +18.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.95× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -16.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 166 | 8 (3 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.61× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.572× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.627× (z -8.7) |
| [[HOP62 (line)]] | alt | 269 | 2 (1 ⚠) | 8 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.02× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.418× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 212 | 5 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +13.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.85× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -13.9) |
| [[HS-578T (line)]] | alt | 271 | 1 | 7 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.19× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -15.9) |
| [[LoVo (line)]] | wt | 151 | 6 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.91× (z +17.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.582× (z -9.0) |
| [[J82 (line)]] | alt | 177 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.458× (z -12.5) |
| [[KATO III (line)]] | alt | 145 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.87× (z +20.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +19.7) | — |
| [[NCI-H2030 (line)]] | alt | 240 | 5 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.435× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.490× (z -9.5) |
| [[SW 900 (line)]] | alt | 287 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.402× (z -13.0) |
| [[A549 (line)]] | wt | 285 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -18.5) |
| [[H4 (line)]] | wt | 264 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.434× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 331 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.326× (z -13.5) |
| [[RKO (line)]] | wt | 320 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -16.0) |
| [[A-172 (line)]] | wt | 183 | 1 | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 2.59× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -16.5) |
| [[Hs 766T (line)]] | wt | 215 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 223 | 3 (1 ⚠) | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.39× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.470× (z -11.2) |
| [[SNU-423 (line)]] | alt | 233 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -17.5) |
| [[C-33 A (line)]] | alt | 222 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 90.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.86× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 231 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.445× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.577× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 186 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 207 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 191 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.11× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.530× (z -8.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 154 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.26× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.535× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 200 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -10.1) |
| [[HCT15 (line)]] | alt | 235 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -13.4) |
| [[LS 180 (line)]] | wt | 130 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 265 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.31× (z +11.1) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 224 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.5) |
| [[SW48 (line)]] | wt | 181 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -14.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 116 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.510× (z -9.4) |
| [[BT-474 (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -8.8) |
| [[C32 (line)]] | wt | 183 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HepG2_C3A (line)]] | wt | 147 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.20× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 71.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.55× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 198 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 404 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 57), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD5]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MTF2]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[G2E3]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.56 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[MALSU1]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[FAM193B]] | +0.54 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[BORA]] | +0.52 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TTK]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 771 |
| [[DCAF7]] | +0.51 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[TMEM143]] | +0.51 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[DBF4]] | +0.50 | +0.34 / +0.50 | both halves | 1e-04 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[MMS19]] | +0.50 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.51 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[TAX1BP3]] | -0.49 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ELK4]] | -0.49 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[ZPR1]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[FSCN2]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[LIN7C]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[SBDS]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CCDC200]] | -0.46 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[PSME3]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 | STRING 579 |
| [[CHMP3]] | -0.45 | -0.50 / -0.37 | both halves | 8e-05 | pathway: Mitotic Anaphase |
| [[PITRM1]] | -0.45 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[WDR1]] | -0.44 | -0.38 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CDC27's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.351). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.2, -38.2); signed map (-44.9, -35.4). **Vector** length 104, 36.7% of its response variance represented; |z| ≥ 3 in 1,411 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +0.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.2 | +4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | +4.1 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | -1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | -2.1 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.7 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -3.5 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,117,703-47,189,422 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APC3, ANAPC3, NUC2; previously D0S1430E, D17S978E |
| Gene groups (HGNC) | Anaphase promoting complex; Tetratricopeptide repeat domain containing |
| Hallmark sets | HEME_METABOLISM, G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [P30260](https://www.uniprot.org/uniprotkb/P30260) (Cell division cycle protein 27 homolog):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [996](https://www.ncbi.nlm.nih.gov/gene/996):

> The protein encoded by this gene shares strong similarity with Saccharomyces cerevisiae protein Cdc27, and the gene product of Schizosaccharomyces pombe nuc 2. This protein is a component of the anaphase-promoting complex (APC), which is composed of eight protein subunits and is highly conserved in eukaryotic cells. This complex catalyzes the formation of cyclin B-ubiquitin conjugate, which is responsible for the ubiquitin-mediated proteolysis of B-type cyclins. The protein encoded by this gene …

**Accessions** — [HGNC:1728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1728) · Entrez [996](https://www.ncbi.nlm.nih.gov/gene/996) · UniProt [P30260](https://www.uniprot.org/uniprotkb/P30260) · Ensembl [ENSG00000004897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004897)

## Data

Gene col 57: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 57); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 57, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 57]; `tensor/DDL_lfc|DDL_z.npy` [57]; `embed/gene_vectors.npy` [57]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 57 or target_col == 57). Every well: [[CDC27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
