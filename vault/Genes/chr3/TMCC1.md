---
symbol: "TMCC1"
type: "gene"
col: 10291
ensembl_id: "ENSG00000172765"
name: "transmembrane and coiled-coil domain family 1"
location: "3q22.1"
module: 54
arm: "+"
pooled_cpm: 199.76
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TMCC1

*transmembrane and coiled-coil domain family 1* — 3q22.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (SW480 4.06×, A-427 3.97×, SW1417 2.94×; ⚠ cell-cycle shift, explains ~34% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (KATO III 2.23×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 2.09×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 1.52×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.508× (z -24.1, q 0e+00, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.683× (z -13.5, q 1e-39, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP3S2]] (+0.54, fdr 3e-05), [[SLMAP]] (+0.52, fdr 3e-05), [[PROSER2]] (+0.51, fdr 1e-05); moves opposite to [[IL11RA]] (-0.52, fdr 4e-05), [[NID1]] (-0.46, fdr 9e-05), [[PRKAR1A]] (-0.44, fdr 2e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ALS2CL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10291.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (SW480 4.06×, A-427 3.97×, SW1417 2.94×; ⚠ cell-cycle shift, explains ~34% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (KATO III 2.23×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 2.09×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 1.52×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.18× | +4.0 | 0.023 | 18/47 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.20× | +3.9 | 0.023 | 19/50 (A-172, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.5 | 0.088 | 15/49 (J82, SNU-423, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.17 | 6/48 (A-427, BT-474, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +3.1 | 0.26 | 5/48 (BT-474, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 24 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.508×** | -24.1 | 0e+00 | 40/48 (LoVo, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.410×** | -22.4 | 0e+00 | 46/49 (Panc 03.27, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.422×** | -20.8 | 0e+00 | 41/44 (A-427, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.446×** | -18.7 | 0e+00 | 43/45 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.514×** | -16.1 | 0e+00 | 44/47 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.567×** | -13.7 | 1e-40 | 37/48 (A498, HEC-1-A, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -13.5 | 1e-39 | 34/49 (A-172, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.584×** | -13.5 | 1e-39 | 38/48 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.604×** | -12.6 | 9e-35 | 39/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.607×** | -12.5 | 3e-34 | 36/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.615×** | -12.2 | 2e-32 | 36/48 (LS 180, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.676×** | -9.8 | 4e-21 | 32/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **0.686×** | -9.5 | 1e-19 | 39/48 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.714×** | -8.4 | 1e-15 | 34/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.743×** | -7.5 | 3e-12 | 32/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -5.0 | 2e-05 | 20/48 (A-172, SW1417, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.700×** | -4.7 | 7e-05 | 30/48 (Panc 03.27, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.779×** | -3.3 | 0.021 | 17/48 (Panc 03.27, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.912× | -3.2 | 0.022 | 7/48 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.879× | -3.2 | 0.024 | 8/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.785×** | -3.2 | 0.026 | 18/47 (HCT15, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.787×** | -3.1 | 0.029 | 20/48 (LOX-IMVI, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.800×** | -2.9 | 0.056 | 15/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 0.05 µM |  | 0.889× | -2.8 | 0.086 | 8/49 (CHP-212, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 340 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -30.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -21.0) |
| [[LoVo (line)]] | wt | 263 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -33.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -18.2) |
| [[SW480 (line)]] | alt | 283 | 1 (1 ⚠) | 15 (13 ⚠) | [[TAK-901 (drug)]] 5 µM 4.06× (z +10.8) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 5 µM 0.212× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -13.5) |
| [[A-172 (line)]] | wt | 192 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -25.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -21.1) |
| [[KATO III (line)]] | alt | 297 | 2 (1 ⚠) | 12 (11 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -20.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -27.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -14.2) |
| [[J82 (line)]] | alt | 125 | 0 | 13 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -31.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.420× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 116 | 0 | 13 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -16.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.541× (z -9.8) |
| [[LS 180 (line)]] | wt | 216 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -27.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -14.6) |
| [[HT-29 (line)]] | alt | 261 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -21.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -13.7) |
| [[SW1417 (line)]] | alt | 359 | 1 (1 ⚠) | 10 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 2.94× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -12.7) |
| [[HOP62 (line)]] | alt | 120 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -13.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -11.5) |
| [[HS-578T (line)]] | alt | 163 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -21.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -10.1) |
| [[A498 (line)]] | wt | 139 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -30.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.437× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 252 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 212 | 1 | 8 (7 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.52× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.384× (z -14.0) |
| [[BT-474 (line)]] | alt | 346 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -14.8) |
| [[C32 (line)]] | wt | 137 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -27.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -19.8) |
| [[PANC-1 (line)]] | alt | 209 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 155 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 157 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -13.3) |
| [[COLO 205 (line)]] | alt | 242 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -20.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 176 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 7 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.190× (z -22.2) |
| [[SNU-423 (line)]] | alt | 155 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -26.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 180 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -16.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 355 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 144 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.313× (z -14.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -10.4) |
| [[SW 900 (line)]] | alt | 109 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.305× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -10.5) |
| [[A-427 (line)]] | wt | 365 | 1 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.97× (z +10.0) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 5 µM 0.0874× (z -32.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 258 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -30.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 203 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -11.3) |
| [[AN3 CA (line)]] | alt | 188 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.247× (z -11.2) |
| [[HCT15 (line)]] | alt | 217 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.413× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 81.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -16.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 193 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 225 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.479× (z -10.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -12.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -10.4) |
| [[SW48 (line)]] | wt | 137 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.240× (z -13.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[CHP-212 (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -10.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 1088 (line)]] | alt | 126 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.103× (z -9.5) |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3S2]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SLMAP]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PROSER2]] | +0.51 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SLC38A9]] | +0.51 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[KATNBL1]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PSMA7]] | +0.50 | +0.32 / +0.48 | both halves | 2e-04 |  |
| [[R3HCC1L]] | +0.50 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[VPS13D]] | +0.49 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[PTPN3]] | +0.48 | +0.54 / +0.37 | both halves | 7e-05 |  |
| [[ANO10]] | +0.48 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[AURKAIP1]] | +0.47 | +0.25 / +0.49 | both halves | 4e-04 |  |
| [[EPS15]] | +0.46 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL11RA]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[NID1]] | -0.46 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[PRKAR1A]] | -0.44 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[SMARCA1]] | -0.43 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[DPY19L2P2-1]] | -0.43 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[SYNGAP1]] | -0.42 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[GNL1]] | -0.42 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[PLEKHG2]] | -0.42 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[EDARADD]] | -0.41 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[CUL4B]] | -0.41 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[COL7A1]] | -0.41 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[HNRNPL]] | -0.41 | -0.40 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALS2CL]] | B | ALS2CL activity raises TMCC1's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without ALS2CL | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[C1orf116]] | B | C1orf116 activity strengthens TMCC1's drug response | lines that do not express C1orf116 (31) vs lines expressing it (18) | the lines without C1orf116 respond 0.85× as strongly (z diff +0.98); strongest at Digitoxin 5 µM: 0.65x vs 0.48x (z diff +2.6) | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; target measured in part of the lines; artifact flags |
| [[C1orf116]] | B | C1orf116 activity raises TMCC1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 1.49× lower at baseline in the lines without C1orf116 | 0.099 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.371). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.3, 33.9); signed map (-45.3, 28.8). **Vector** length 93.8, 30.3% of its response variance represented; |z| ≥ 3 in 1,438 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.1 | +1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +0.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -7.4 | -20.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.4 | -18.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -6.1 | -22.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -12.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.2 | +0.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane and coiled-coil domain family 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:129,647,792-129,893,711 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0779 |
| Gene groups (HGNC) | Transmembrane and coiled-coil domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O94876](https://www.uniprot.org/uniprotkb/O94876) (Transmembrane and coiled-coil domains protein 1):

> Endoplasmic reticulum membrane protein that promotes endoplasmic reticulum-associated endosome fission. Localizes to contact sites between the endoplasmic reticulum and endosomes and acts by promoting recruitment of the endoplasmic reticulum to endosome tubules for fission. Endosome membrane fission of early and late endosomes is essential to separate regions destined for lysosomal degradation from carriers to be recycled to the plasma membrane.

**Summary**, from NCBI Gene [23023](https://www.ncbi.nlm.nih.gov/gene/23023):

> Enables identical protein binding activity. Involved in several processes, including endosome fission; endosome membrane tubulation; and membrane fission. Located in cytosol; endoplasmic reticulum-endosome membrane contact site; and rough endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29116) · Entrez [23023](https://www.ncbi.nlm.nih.gov/gene/23023) · UniProt [O94876](https://www.uniprot.org/uniprotkb/O94876) · Ensembl [ENSG00000172765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172765)

## Data

Gene col 10291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10291); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10291]; `tensor/DDL_lfc|DDL_z.npy` [10291]; `embed/gene_vectors.npy` [10291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10291 or target_col == 10291). Every well: [[TMCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
