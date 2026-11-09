---
symbol: "PHLDA2"
type: "gene"
col: 11203
ensembl_id: "ENSG00000181649"
name: "pleckstrin homology like domain family A member 2"
location: "11p15.4"
module: 101
arm: "+"
pooled_cpm: 33.62
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 33
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# PHLDA2

*pleckstrin homology like domain family A member 2* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.78× (z +14.9, q 0e+00, up in 41 of 41 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.46× (z +10.3, q 2e-22, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.281× (z -5.5, q 2e-05, down in 37 of 41 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.367× (z -4.7, q 9e-04, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R14B-AS1]] (+0.69, fdr 7e-06), [[HBEGF]] (+0.66, fdr 7e-06), [[EPHA2]] (+0.64, fdr 7e-06); moves opposite to [[CBX1]] (-0.61, fdr 1e-05), [[RNF20]] (-0.56, fdr 4e-05), [[ATP5F1C]] (-0.55, fdr 3e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PRSS22]] → it (grade B ⚠); 33 go from it, the strongest it → [[SNX9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **8.78×** | +14.9 | 0e+00 | 41/41 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **10.5×** | +11.0 | 1e-25 | 40/40 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.46×** | +10.3 | 2e-22 | 39/41 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.46×** | +9.8 | 2e-20 | 41/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **6.58×** | +9.1 | 7e-18 | 36/36 (NCI-H460, C32, …) | all doses, flat | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **7.00×** | +9.1 | 9e-18 | 36/38 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **6.31×** | +9.0 | 3e-17 | 40/40 (NCI-H460, SW48, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.91×** | +6.6 | 2e-09 | 35/40 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **3.89×** | +6.1 | 6e-08 | 31/35 (NCI-H460, RPMI-7951, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **3.55×** | +5.9 | 2e-07 | 29/34 (NCI-H460, C32, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **3.30×** | +5.8 | 3e-07 | 37/41 (NCI-H460, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.40×** | +5.7 | 5e-07 | 35/41 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **3.39×** | +5.7 | 5e-07 | 35/40 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.90×** | +5.2 | 9e-06 | 35/40 (SW480, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.86×** | +5.1 | 1e-05 | 35/40 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.86×** | +4.3 | 6e-04 | 30/41 (A-172, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.21×** | +3.9 | 0.003 | 30/41 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.99×** | +3.2 | 0.033 | 32/40 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.73×** | +3.1 | 0.050 | 23/40 (MIA PaCa-2, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.91×** | +3.0 | 0.054 | 26/41 (NCI-H1792, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.281×** | -5.5 | 2e-05 | 37/41 (NCI-H23, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.367×** | -4.7 | 9e-04 | 34/40 (SW48, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.511×** | -4.5 | 0.001 | 35/41 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.406×** | -4.0 | 0.008 | 29/40 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.194×** | -3.9 | 0.010 | 37/41 (SW48, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.534×** | -3.7 | 0.019 | 28/41 (C32, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.470×** | -3.6 | 0.025 | 25/41 (NCI-H23, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.478×** | -3.6 | 0.025 | 29/40 (NCI-H23, SW48, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.594×** | -3.5 | 0.034 | 26/41 (NCI-H1792, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.490×** | -3.3 | 0.052 | 25/40 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.487×** | -3.3 | 0.052 | 24/41 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.257×** | -3.2 | 0.055 | 28/41 (SW48, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.95 per unit of S-phase module lfc, +1.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.54 | 15 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +13.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 36.6× (z +11.2) | — |
| [[C32 (line)]] | wt | 35.6 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +13.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 17.9× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 5 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +11.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.42× (z +8.8) | [[Cobimetinib (drug)]] 5 µM 0.0450× (z -8.6) |
| [[A-172 (line)]] | wt | 29.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +13.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 16.9× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 51.5 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 38.4× (z +19.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +12.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +12.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 24.5× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +15.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 16.8× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 47.0 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +18.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 17.9× (z +12.2) | — |
| [[A549 (line)]] | wt | 16.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +11.6) | — |
| [[H4 (line)]] | wt | 22.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.76× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 31.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +13.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +13.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 27.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +14.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 16.3× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 4 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0325× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Trametinib (drug)]] 0.05 µM 0.171× (z -9.2) |
| [[SW48 (line)]] | wt | 73.6 | 2 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 18.8× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Cobimetinib (drug)]] 5 µM 0.0743× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 19.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.5× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[SNU-423 (line)]] | alt | 11.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.3× (z +13.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.08× (z +9.0) | — |
| [[SW480 (line)]] | alt | 17.6 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 10.8× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 9.04× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 18.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.2× (z +13.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +9.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.06× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +10.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HS-578T (line)]] | alt | 50.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.03× (z +9.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.04× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 15.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +12.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[CFPAC-1 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +15.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Hs 766T (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +13.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[J82 (line)]] | alt | 73.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.76× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +9.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +11.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 38.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 13.5× (z +9.7) ⚠ toxic | — |
| [[SW1417 (line)]] | alt | 71.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +10.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R14B-AS1]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[HBEGF]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EPHA2]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[S100A11]] | +0.64 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[FAM43A]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[HOMER1]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[AGO2]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[STK10]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[PLK3]] | +0.61 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[UPP1]] | +0.61 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[DUSP5-DT]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SPHK1]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX1]] | -0.61 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[RNF20]] | -0.56 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[ATP5F1C]] | -0.55 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[NUDT21]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CCDC6]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[KAT7]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[BAP1]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SUDS3]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CNOT7]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[SNRNP200]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[GFM2]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[OPA1]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS22]] | B | PRSS22 activity raises PHLDA2's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without PRSS22 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[MAP2K1]] | B | MAP2K1 activity raises PHLDA2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers PHLDA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises PHLDA2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[RASSF8-AS1]] | B | RASSF8-AS1 activity lowers PHLDA2's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 2.18× higher at baseline in the lines without RASSF8-AS1 | 0.090 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[GOLT1A]] | B | GOLT1A activity raises PHLDA2's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without GOLT1A | 0.097 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[C11orf91]] | C | C11orf91 activity raises PHLDA2's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 2.94× lower at baseline in the lines without C11orf91 | 0.003 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202; co-absent with the target |
| [[IL27RA]] | C | IL27RA activity lowers PHLDA2's level | lines that do not express IL27RA (3) vs lines expressing it (47) | 2.85× higher at baseline in the lines without IL27RA | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ITGA2B, TMEM132A, CLEC2D; maybe low, not absent; its own permutation p |
| [[CDKN1A]] | C | CDKN1A activity raises PHLDA2's level | lines that do not express CDKN1A (3) vs lines expressing it (47) | 3.96× lower at baseline in the lines without CDKN1A | 0.076 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| [[PLEKHN1]] | C | PLEKHN1 activity raises PHLDA2's level | lines that do not express PLEKHN1 (3) vs lines expressing it (47) | 3.81× lower at baseline in the lines without PLEKHN1 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 27, C 6. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX9]] | B | PHLDA2 activity raises SNX9's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without PHLDA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[IL4R]] | B | PHLDA2 activity raises IL4R's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.61× lower at baseline in the lines without PHLDA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[TNFAIP8]] | B | PHLDA2 activity raises TNFAIP8's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.17× lower at baseline in the lines without PHLDA2 | 0.008 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[CDKN1A]] | B | PHLDA2 activity raises CDKN1A's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.55× lower at baseline in the lines without PHLDA2 | 0.009 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[EHD1]] | B | PHLDA2 activity raises EHD1's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.26× lower at baseline in the lines without PHLDA2 | 0.010 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[CLCF1]] | B | PHLDA2 activity raises CLCF1's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.75× lower at baseline in the lines without PHLDA2 | 0.011 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[S100A11]] | B | PHLDA2 activity raises S100A11's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.66× lower at baseline in the lines without PHLDA2 | 0.012 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[LAMB3]] | B | PHLDA2 activity raises LAMB3's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 5.52× lower at baseline in the lines without PHLDA2 | 0.037 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[CD58]] | B | PHLDA2 activity raises CD58's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without PHLDA2 | 0.038 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[LIF]] | B | PHLDA2 activity raises LIF's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 3.35× lower at baseline in the lines without PHLDA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[ANTXR2]] | B | PHLDA2 activity raises ANTXR2's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 3.70× lower at baseline in the lines without PHLDA2 | 0.041 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[RFFL]] | B | PHLDA2 activity raises RFFL's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without PHLDA2 | 0.046 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.9, -3.3); signed map (0.7, 32.6). **Vector** length 93.1, 40.1% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.6 | +14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +9.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.6 | +11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.9 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -1.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.5 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.4 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology like domain family A member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:2,928,273-2,929,420 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IPL, BWR1C, HLDA2; previously TSSC3 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53GA4](https://www.uniprot.org/uniprotkb/Q53GA4) (Pleckstrin homology-like domain family A member 2):

> Plays a role in regulating placenta growth. May act via its PH domain that competes with other PH domain-containing proteins, thereby preventing their binding to membrane lipids (By similarity).

**Summary**, from NCBI Gene [7262](https://www.ncbi.nlm.nih.gov/gene/7262):

> This gene is located in a cluster of imprinted genes on chromosome 11p15.5, which is considered to be an important tumor suppressor gene region. Alterations in this region may be associated with the Beckwith-Wiedemann syndrome, Wilms tumor, rhabdomyosarcoma, adrenocortical carcinoma, and lung, ovarian, and breast cancer. This gene has been shown to be imprinted, with preferential expression from the maternal allele in placenta and liver. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:12385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12385) · Entrez [7262](https://www.ncbi.nlm.nih.gov/gene/7262) · UniProt [Q53GA4](https://www.uniprot.org/uniprotkb/Q53GA4) · Ensembl [ENSG00000181649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181649)

## Data

Gene col 11203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11203); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11203]; `tensor/DDL_lfc|DDL_z.npy` [11203]; `embed/gene_vectors.npy` [11203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11203 or target_col == 11203). Every well: [[PHLDA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHLDA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
