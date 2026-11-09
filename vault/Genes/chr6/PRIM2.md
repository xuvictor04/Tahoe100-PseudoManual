---
symbol: "PRIM2"
type: "gene"
col: 7068
ensembl_id: "ENSG00000146143"
name: "DNA primase subunit 2"
location: "6p11.2"
module: 6
arm: "+"
pooled_cpm: 96.94
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PRIM2

*DNA primase subunit 2* — 6p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.14× (z +21.9, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.85× (z +9.4, q 4e-19, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.460× (z -17.0, q 0e+00, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.533× (z -9.3, q 3e-18, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA5]] (+0.80, fdr 7e-06), [[CEP128]] (+0.78, fdr 7e-06), [[MMS22L]] (+0.77, fdr 7e-06); moves opposite to [[ETFRF1]] (-0.67, fdr 1e-05), [[TCEANC]] (-0.60, fdr 3e-05), [[ZNF213]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LGALS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **4.14×** | +21.9 | 0e+00 | 48/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.46×** | +19.1 | 0e+00 | 48/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.89×** | +16.3 | 0e+00 | 48/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.89×** | +9.8 | 2e-20 | 40/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.85×** | +9.4 | 4e-19 | 42/48 (C32, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +7.9 | 2e-13 | 40/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +6.3 | 2e-08 | 36/48 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.8 | 6e-07 | 30/48 (SW480, SW1417, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +5.3 | 9e-06 | 31/49 (LoVo, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +4.7 | 1e-04 | 27/49 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 1e-04 | 32/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.7 | 1e-04 | 28/48 (LoVo, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +4.0 | 0.003 | 26/48 (HT-29, SNU-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.6 | 0.012 | 21/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.6 | 0.012 | 25/48 (SNU-423, HT-29, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.013 | 24/47 (HS-578T, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.016 | 20/48 (C32, NCI-H2347, …) | top dose only |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.018 | 24/48 (HepG2/C3A, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.033 | 20/47 (C32, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.0 | 0.059 | 17/48 (LoVo, SW1417, …) | top dose only |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.065 | 15/48 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.072 | 20/48 (SNU-423, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.460×** | -17.0 | 0e+00 | 45/48 (LoVo, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.533×** | -9.3 | 3e-18 | 43/48 (COLO 205, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.549×** | -9.2 | 4e-18 | 42/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -7.4 | 2e-11 | 32/44 (HCT15, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -6.7 | 3e-09 | 30/49 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.631×** | -6.6 | 5e-09 | 30/45 (J82, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.679×** | -6.0 | 2e-07 | 34/48 (NCI-H661, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.690×** | -5.7 | 7e-07 | 30/49 (NCI-H23, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.784×** | -5.3 | 6e-06 | 35/48 (A-427, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -5.1 | 2e-05 | 36/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.783×** | -3.8 | 0.008 | 23/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.786×** | -3.7 | 0.009 | 27/48 (A-172, SW480, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.020 | 20/48 (LOX-IMVI, A549, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **0.791×** | -3.4 | 0.025 | 23/48 (LOX-IMVI, SHP-77, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.736×** | -3.4 | 0.028 | 23/48 (SW480, A-172, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.89 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 144 | 5 (3 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.88× (z +15.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.40× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.436× (z -8.9) |
| [[LoVo (line)]] | wt | 77.4 | 6 (4 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.22× (z +18.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.63× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -20.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 211 | 1 (1 ⚠) | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +8.5) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -18.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.300× (z -11.7) |
| [[HOP62 (line)]] | alt | 114 | 4 (3 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.71× (z +13.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.83× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -15.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -8.9) |
| [[KATO III (line)]] | alt | 111 | 2 (2 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +10.4) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.365× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 122 | 5 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.38× (z +16.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.37× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -13.3) |
| [[A-172 (line)]] | wt | 61.2 | 3 (3 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.57× (z +15.3) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.329× (z -9.0) |
| [[C32 (line)]] | wt | 61.2 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.76× (z +15.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.86× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 95.9 | 3 (3 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.51× (z +14.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.215× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 39.7 | 3 (2 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.41× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 224 | 3 (3 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +12.2) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -24.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 60.8 | 3 (3 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.14× (z +15.3) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.384× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 97.9 | 3 (3 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.86× (z +12.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 122 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.28× (z +12.3) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 57.2 | 3 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.94× (z +14.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -14.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.296× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 51.3 | 4 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.92× (z +15.8) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 108 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.36× (z +14.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -15.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 110 | 3 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.14× (z +14.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -17.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.353× (z -10.0) |
| [[SW480 (line)]] | alt | 113 | 3 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.64× (z +15.6) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.479× (z -8.6) |
| [[A498 (line)]] | wt | 59.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.26× (z +11.9) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -13.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 48.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.88× (z +16.2) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 67.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.10× (z +9.9) ⚠ cell-cycle shift, explains ~36% of this change | [[Harringtonine (drug)]] 5 µM 0.311× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 74.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.15× (z +13.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 143 | 1 (1 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -15.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.381× (z -9.8) |
| [[HT-29 (line)]] | alt | 72.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.28× (z +13.2) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 148 | 1 (1 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +9.3) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 108 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.49× (z +10.8) ⚠ cell-cycle shift, explains ~36% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -9.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 94.1 | 2 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +11.4) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 79.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.97× (z +12.4) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 50.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.18× (z +17.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HCT15 (line)]] | alt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0586× (z -22.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 60.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.69× (z +16.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 56.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.41× (z +15.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 88.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +11.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2347 (line)]] | alt | 56.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +14.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SHP-77 (line)]] | alt | 157 | 1 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.97× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -12.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 78.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.09× (z +12.2) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 5 µM 0.219× (z -11.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 54.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.59× (z +13.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[C-33 A (line)]] | alt | 118 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +11.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[COLO 205 (line)]] | alt | 134 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.278× (z -10.9) |
| [[Hs 766T (line)]] | wt | 56.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.89× (z +10.6) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -11.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -12.7) ⚠ transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 116 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.46× (z +10.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 51.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.35× (z +8.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 154 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA5]] | +0.80 | +0.84 / +0.73 | both halves | 7e-06 |  |
| [[CEP128]] | +0.78 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.77 | +0.82 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RTTN]] | +0.77 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[FANCB]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[POLA1]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 999 |
| [[RNGTT]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[FANCA]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[BLM]] | +0.73 | +0.73 / +0.67 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 418 |
| [[POLQ]] | +0.71 | +0.72 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CDC45]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 924 |
| [[DTL]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 | same gene group; STRING 809 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETFRF1]] | -0.67 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.60 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ZNF213]] | -0.60 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H6]] | -0.60 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[GLIS2]] | -0.59 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[MAP3K2-DT]] | -0.58 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[TCEAL4]] | -0.58 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3]] | B | LGALS3 activity lowers PRIM2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.72× higher at baseline in the lines without LGALS3 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[TOP1]] | B | TOP1 activity lowers PRIM2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises PRIM2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without TCF19 | 0.069 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises PRIM2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.76× lower at baseline in the lines without CDC25A | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.5, -46.4); signed map (-38.0, -40.3). **Vector** length 154, 58.0% of its response variance represented; |z| ≥ 3 in 1,396 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.53 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.53 to 45); *Activation of ATR in response to replication stress* (reactome, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.7 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +9.4 | +9.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.6 | +21.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.4 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +5.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.7 | +2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -16.9 | -17.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -12.1 | -9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.1 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.2 | -9.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.3 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -3.0 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | DNA primase subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p11.2 — chr6:57,314,805-57,646,850 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PRIM2A |
| Gene groups (HGNC) | MicroRNA protein coding host genes; DNA primase complex subunits |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 26 pathways, smallest: DNA replication initiation; Inhibition of replication initiation of damaged DNA by RB1/E2F1; Telomere C-strand synthesis initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49643](https://www.uniprot.org/uniprotkb/P49643) (DNA primase large subunit):

> Regulatory subunit of the DNA primase complex and component of the DNA polymerase alpha complex (also known as the alpha DNA polymerase-primase complex) which play an essential role in the initiation of DNA synthesis. During the S phase of the cell cycle, the DNA polymerase alpha complex (composed of a catalytic subunit POLA1, an accessory subunit POLA2 and two primase subunits, the catalytic subunit PRIM1 and the regulatory subunit PRIM2) is recruited to DNA at the replicative forks via direct …

**Summary**, from NCBI Gene [5558](https://www.ncbi.nlm.nih.gov/gene/5558):

> This gene encodes the 58 kilodalton subunit of DNA primase, an enzyme that plays a key role in the replication of DNA. The encoded protein forms a heterodimer with a 49 kilodalton subunit. This heterodimer functions as a DNA-directed RNA polymerase to synthesize small RNA primers that are used to create Okazaki fragments on the lagging strand of the DNA. Alternative splicing of this gene results in multiple transcript variants. This gene has a related pseudogene, which is also present on …

**Accessions** — [HGNC:9370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9370) · Entrez [5558](https://www.ncbi.nlm.nih.gov/gene/5558) · UniProt [P49643](https://www.uniprot.org/uniprotkb/P49643) · Ensembl [ENSG00000146143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146143)

## Data

Gene col 7068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7068); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7068]; `tensor/DDL_lfc|DDL_z.npy` [7068]; `embed/gene_vectors.npy` [7068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7068 or target_col == 7068). Every well: [[PRIM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRIM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
