---
symbol: "AMOTL2"
type: "gene"
col: 3515
ensembl_id: "ENSG00000114019"
name: "angiomotin like 2"
location: "3q22.2"
module: 123
arm: "+"
pooled_cpm: 57.06
n_lines_expressing: 46
n_dd_up: 30
n_dd_down: 28
n_dd_up_clean: 25
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# AMOTL2

*angiomotin like 2* — 3q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.48× (z +26.6, q 0e+00, up in 43 of 44 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 8.37× (z +16.8, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.208× (z -23.7, q 0e+00, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LATS2]] (+0.84, fdr 7e-06), [[AJUBA]] (+0.77, fdr 7e-06), [[EDN1]] (+0.68, fdr 7e-06); moves opposite to [[ZCCHC17]] (-0.58, fdr 2e-05), [[MFN1]] (-0.56, fdr 1e-05), [[RARS2]] (-0.55, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[WWC1]] → it (grade B ⚠); 3 go from it, the strongest it → [[LATS2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.48×** | +26.6 | 0e+00 | 43/44 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.37×** | +16.8 | 0e+00 | 43/45 (MIA PaCa-2, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.81×** | +15.6 | 0e+00 | 42/44 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.68×** | +14.3 | 3e-44 | 42/44 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +10.5 | 1e-23 | 32/44 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +9.6 | 5e-20 | 35/44 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.39×** | +9.6 | 5e-20 | 37/44 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +8.3 | 1e-14 | 29/43 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +7.0 | 2e-10 | 28/44 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +6.8 | 5e-10 | 29/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +6.3 | 1e-08 | 23/44 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.4 | 4e-06 | 25/44 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 4e-05 | 20/43 (COLO 205, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.7 | 1e-04 | 26/44 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +4.6 | 2e-04 | 22/44 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +4.5 | 3e-04 | 25/43 (COLO 205, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +4.3 | 6e-04 | 21/44 (HCT15, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.002 | 21/42 (J82, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.208×** | -23.7 | 0e+00 | 40/44 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.271×** | -19.7 | 0e+00 | 41/44 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.337×** | -16.4 | 0e+00 | 39/44 (HT-29, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.473×** | -11.3 | 2e-27 | 32/44 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.473×** | -10.9 | 2e-25 | 36/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.496×** | -10.2 | 2e-22 | 25/38 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.637×** | -9.6 | 5e-20 | 31/44 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.536×** | -9.4 | 3e-19 | 34/44 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.543×** | -9.2 | 2e-18 | 34/43 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.533×** | -9.0 | 2e-17 | 32/44 (SNU-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.583×** | -8.1 | 2e-14 | 32/44 (SNU-1, LoVo, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.578×** | -8.0 | 9e-14 | 29/43 (NCI-H23, SW48, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.623×** | -7.1 | 4e-11 | 24/42 (SNU-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.482×** | -5.8 | 3e-07 | 32/44 (BT-474, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.601×** | -5.5 | 2e-06 | 29/44 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.711×** | -5.2 | 8e-06 | 24/44 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.537×** | -4.9 | 3e-05 | 25/44 (RKO, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.723×** | -4.7 | 7e-05 | 22/43 (SNU-1, AN3 CA, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **0.733×** | -4.3 | 4e-04 | 19/43 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.579×** | -4.3 | 4e-04 | 22/44 (SW1417, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.741×** | -4.3 | 5e-04 | 23/44 (LoVo, HCT15, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.60 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 253 | 3 | 15 (8 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.97× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0990× (z -25.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.137× (z -21.7) |
| [[LOX-IMVI (line)]] | wt | 97.3 | 5 (1 ⚠) | 11 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +17.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.68× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.164× (z -17.8) |
| [[SW480 (line)]] | alt | 76.3 | 3 (1 ⚠) | 11 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.29× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.266× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 112 | 5 (2 ⚠) | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 9.26× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.150× (z -19.5) |
| [[NCI-H23 (line)]] | alt | 91.4 | 3 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.6× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.107× (z -19.0) |
| [[BT-474 (line)]] | alt | 67.3 | 6 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 3.66× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.0679× (z -21.9) |
| [[A498 (line)]] | wt | 48.8 | 5 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +33.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.5× (z +22.3) | [[Panobinostat (drug)]] 5 µM 0.170× (z -15.6) |
| [[A-172 (line)]] | wt | 97.4 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +24.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.45× (z +18.6) | [[Panobinostat (drug)]] 5 µM 0.145× (z -16.7) |
| [[A549 (line)]] | wt | 42.3 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +18.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.41× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.108× (z -15.4) |
| [[J82 (line)]] | alt | 99.6 | 3 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.92× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -17.8) |
| [[MIA PaCa-2 (line)]] | alt | 45.6 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +23.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 17.8× (z +17.8) | — |
| [[NCI-H460 (line)]] | wt | 29.9 | 4 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +18.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.65× (z +14.7) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.219× (z -12.5) |
| [[KATO III (line)]] | alt | 68.9 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +15.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.101× (z -19.9) |
| [[AsPC-1 (line)]] | alt | 69.1 | 3 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +20.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.71× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.0886× (z -18.9) |
| [[C-33 A (line)]] | alt | 55.8 | 2 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.105× (z -16.5) |
| [[LoVo (line)]] | wt | 55.7 | 2 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 16.2× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.0939× (z -20.9) |
| [[Panc 03.27 (line)]] | alt | 124 | 3 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.5× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -10.8) |
| [[RKO (line)]] | wt | 72.8 | 1 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 5 µM 0.147× (z -15.1) |
| [[SW48 (line)]] | wt | 65.7 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0825× (z -15.1) |
| [[HS-578T (line)]] | alt | 26.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 29.7× (z +23.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 30.7× (z +16.0) | — |
| [[HT-29 (line)]] | alt | 59.7 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0808× (z -19.5) |
| [[hTERT-HPNE (line)]] | wt | 45.9 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +21.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 11.1× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 73.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +20.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.00× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 55.2 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.5) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 5 µM 0.0928× (z -17.1) |
| [[SNU-423 (line)]] | alt | 38.1 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +21.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.10× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -12.8) |
| [[SW1417 (line)]] | alt | 139 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.333× (z -10.6) |
| [[HOP62 (line)]] | alt | 20.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +24.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.9× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 60.5 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 4.56× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.101× (z -14.7) |
| [[PANC-1 (line)]] | alt | 28.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +12.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 20.3× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +13.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 12.8× (z +11.5) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.119× (z -10.0) |
| [[A-427 (line)]] | wt | 59.9 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +15.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.50× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.189× (z -9.9) |
| [[H4 (line)]] | wt | 32.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +16.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.20× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -9.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 23.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +15.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 11.7× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 64.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.8× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 27.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +15.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.11× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 22.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.52× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 48.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +14.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2347 (line)]] | alt | 41.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.22 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LATS2]] | +0.84 | +0.81 / +0.80 | both halves | 7e-06 | pathway: Signaling by Hippo; STRING 934 |
| [[AJUBA]] | +0.77 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[EDN1]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TGIF2]] | +0.65 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[FOSL2]] | +0.64 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CCN1]] | +0.64 | +0.66 / +0.69 | both halves | 7e-06 | STRING 759 |
| [[HNRNPH2]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[REPIN1]] | +0.61 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[LINC01186]] | +0.61 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TIGD2]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SLFN12]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF462]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC17]] | -0.58 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MFN1]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RARS2]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.55 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[HSPB11]] | -0.55 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[SNHG30]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ATP2C1]] | -0.54 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[SMG1P5]] | -0.54 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SRD5A1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[GDAP2]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[DCUN1D4]] | -0.52 | -0.55 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWC1]] | B | WWC1 activity raises AMOTL2's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 2.50× lower at baseline in the lines without WWC1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[CCN1]] | B | CCN1 activity raises AMOTL2's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without CCN1 | 0.023 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[FSTL3]] | B | FSTL3 activity raises AMOTL2's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without FSTL3 | 0.045 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |
| [[DDAH1]] | C | DDAH1 activity raises AMOTL2's level | lines that do not express DDAH1 (3) vs lines expressing it (47) | 3.48× lower at baseline in the lines without DDAH1 | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| [[RBMS2]] | C | RBMS2 activity raises AMOTL2's level | lines that do not express RBMS2 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without RBMS2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HOMER3, ARHGAP10, TMEM144; maybe low, not absent; its own permutation p |
| [[ARHGEF17]] | C | ARHGEF17 activity raises AMOTL2's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without ARHGEF17 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[SLC9A3]] | C | SLC9A3 activity lowers AMOTL2's level | lines that do not express SLC9A3 (3) vs lines expressing it (47) | 3.06× higher at baseline in the lines without SLC9A3 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AIFM2, TESK2, HBEGF; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LATS2]] | C | AMOTL2 activity raises LATS2's level | lines that do not express AMOTL2 (4) vs lines expressing it (46) | 3.85× lower at baseline in the lines without AMOTL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: BCL2L1, RASSF7, FCHO1; its own permutation p |
| [[CCN1]] | C | AMOTL2 activity raises CCN1's level | lines that do not express AMOTL2 (4) vs lines expressing it (46) | 3.97× lower at baseline in the lines without AMOTL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: BCL2L1, RASSF7, FCHO1; its own permutation p |
| [[AJUBA]] | C | AMOTL2 activity raises AJUBA's level | lines that do not express AMOTL2 (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without AMOTL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: BCL2L1, RASSF7, FCHO1; its own permutation p |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.0, 12.5); signed map (42.3, 2.4). **Vector** length 147, 49.4% of its response variance represented; |z| ≥ 3 in 1,536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +12.3 | +26.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.1 | +15.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.8 | +14.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +16.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.9 | +3.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.6 | +4.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -10.0 | -11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -9.1 | -9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -9.0 | -9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -8.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -6.0 | -10.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.9 | -5.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.7 | -5.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -5.2 | -9.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | angiomotin like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.2 — chr3:134,355,347-134,375,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LCCP |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 1 pathways, smallest: Signaling by Hippo |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2J4](https://www.uniprot.org/uniprotkb/Q9Y2J4) (Angiomotin-like protein 2):

> Regulates the translocation of phosphorylated SRC to peripheral cell-matrix adhesion sites. Required for proper architecture of actin filaments. Plays a role in coupling actin fibers to cell junctions in endothelial cells and is therefore required for correct endothelial cell morphology via facilitating transcellular transmission of mechanical force resulting in endothelial cell elongation (By similarity). Required for the anchoring of radial actin fibers to CDH1 junction complexes at the cell …

**Summary**, from NCBI Gene [51421](https://www.ncbi.nlm.nih.gov/gene/51421):

> Angiomotin is a protein that binds angiostatin, a circulating inhibitor of the formation of new blood vessels (angiogenesis). Angiomotin mediates angiostatin inhibition of endothelial cell migration and tube formation in vitro. The protein encoded by this gene is related to angiomotin and is a member of the motin protein family. Alternative splicing results in multiple transcript variants of this gene. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:17812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17812) · Entrez [51421](https://www.ncbi.nlm.nih.gov/gene/51421) · UniProt [Q9Y2J4](https://www.uniprot.org/uniprotkb/Q9Y2J4) · Ensembl [ENSG00000114019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114019)

## Data

Gene col 3515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3515); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3515]; `tensor/DDL_lfc|DDL_z.npy` [3515]; `embed/gene_vectors.npy` [3515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3515 or target_col == 3515). Every well: [[AMOTL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMOTL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
