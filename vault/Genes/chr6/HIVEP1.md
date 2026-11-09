---
symbol: "HIVEP1"
type: "gene"
col: 1758
ensembl_id: "ENSG00000095951"
name: "HIVEP zinc finger 1"
location: "6p24.1"
module: 57
arm: "-"
pooled_cpm: 125.19
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 21
n_dd_up_clean: 14
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# HIVEP1

*HIVEP zinc finger 1* — 6p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.20× (z +40.2, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.343× (z -21.2, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF2]] (+0.74, fdr 7e-06), [[HIVEP2]] (+0.69, fdr 7e-06), [[BAZ1A]] (+0.67, fdr 1e-05); moves opposite to [[MKRN2]] (-0.67, fdr 1e-05), [[VAMP7]] (-0.65, fdr 1e-05), [[MED23]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF462]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.20×** | +40.2 | 0e+00 | 46/46 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.14×** | +21.8 | 0e+00 | 46/46 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +16.6 | 0e+00 | 40/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.28×** | +16.3 | 0e+00 | 43/46 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.04×** | +14.1 | 4e-43 | 45/46 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +13.5 | 1e-39 | 45/46 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +13.2 | 1e-37 | 39/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.01×** | +11.4 | 3e-28 | 41/47 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.4 | 2e-15 | 28/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +7.2 | 3e-11 | 33/45 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +6.7 | 1e-09 | 30/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 8e-08 | 27/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +5.8 | 3e-07 | 31/46 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.67×** | +5.3 | 5e-06 | 36/46 (NCI-H2347, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +4.7 | 1e-04 | 28/46 (HEC-1-A, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.010 | 21/46 (SW 900, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.013 | 17/46 (CFPAC-1, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.343×** | -21.2 | 0e+00 | 44/46 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.379×** | -19.2 | 0e+00 | 46/46 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.478×** | -14.6 | 0e+00 | 43/47 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.486×** | -14.3 | 2e-44 | 41/46 (AsPC-1, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.520×** | -12.5 | 1e-33 | 36/42 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.358×** | -10.7 | 1e-24 | 44/46 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.694×** | -10.3 | 7e-23 | 37/46 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.648×** | -8.0 | 1e-13 | 31/43 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.723×** | -6.5 | 7e-09 | 33/46 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.727×** | -6.3 | 1e-08 | 33/47 (SNU-423, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.714×** | -6.2 | 3e-08 | 32/46 (A549, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -5.4 | 3e-06 | 29/46 (HT-29, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -4.8 | 8e-05 | 23/46 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.801×** | -4.4 | 4e-04 | 23/46 (A498, LOX-IMVI, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.808×** | -4.2 | 9e-04 | 24/46 (SHP-77, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.811×** | -4.2 | 0.001 | 26/46 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.724×** | -3.4 | 0.025 | 17/45 (NCI-H23, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.783×** | -3.1 | 0.053 | 16/46 (NCI-H23, A-427, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 292 | 7 | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.204× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 82.8 | 12 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +30.5) | [[Panobinostat (drug)]] 5 µM 0.364× (z -12.9) |
| [[A549 (line)]] | wt | 150 | 7 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +28.5) | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -17.8) |
| [[HOP62 (line)]] | alt | 113 | 11 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +29.0) | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -11.8) |
| [[HS-578T (line)]] | alt | 137 | 9 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +22.4) | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -17.0) |
| [[SNU-423 (line)]] | alt | 148 | 8 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +28.6) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.335× (z -11.3) |
| [[Hs 766T (line)]] | wt | 256 | 7 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +20.9) | [[Panobinostat (drug)]] 5 µM 0.206× (z -15.9) |
| [[J82 (line)]] | alt | 208 | 8 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +30.2) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.312× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 197 | 8 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +26.1) | [[Panobinostat (drug)]] 5 µM 0.157× (z -21.0) |
| [[BT-474 (line)]] | alt | 149 | 9 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +18.4) | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -18.7) |
| [[NCI-H1792 (line)]] | alt | 141 | 8 (1 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.87× (z +20.7) | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -14.1) |
| [[A-172 (line)]] | wt | 163 | 5 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +23.8) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 113 | 7 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +31.2) | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -13.7) |
| [[A498 (line)]] | wt | 119 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +26.3) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 83.4 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +28.3) | — |
| [[LOX-IMVI (line)]] | wt | 143 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 101 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +21.8) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 153 | 5 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +24.3) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.363× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 185 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +23.6) | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -11.4) |
| [[LoVo (line)]] | wt | 105 | 4 | 4 | [[Harringtonine (drug)]] 5 µM 3.13× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.418× (z -11.3) |
| [[PANC-1 (line)]] | alt | 120 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.36× (z +40.7) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -12.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 73.8 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.264× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 150 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.173× (z -17.7) |
| [[RPMI-7951 (line)]] | alt | 106 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +18.0) | — |
| [[SW 900 (line)]] | alt | 82.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +23.1) | — |
| [[LS 180 (line)]] | wt | 107 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.463× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 112 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +24.9) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.428× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 90.7 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +19.4) | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -15.1) |
| [[HT-29 (line)]] | alt | 265 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -15.8) |
| [[KATO III (line)]] | alt | 90.8 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +21.3) | [[Panobinostat (drug)]] 5 µM 0.391× (z -9.2) |
| [[C32 (line)]] | wt | 67.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +19.6) | — |
| [[hTERT-HPNE (line)]] | wt | 84.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 118 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +24.0) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -14.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 95.4 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.373× (z -9.7) |
| [[SW1417 (line)]] | alt | 105 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -14.1) |
| [[SW48 (line)]] | wt | 101 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.256× (z -10.9) |
| [[A-427 (line)]] | wt | 76.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +24.5) | — |
| [[COLO 205 (line)]] | alt | 67.4 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.40× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 110 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.29× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 68.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +15.2) | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.429× (z -9.8) ⚠ transcription drop · without an alert: [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.436× (z -9.6) |
| [[C-33 A (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 90.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +17.6) | — |
| [[RKO (line)]] | wt | 90.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -10.4) |
| [[CHP-212 (line)]] | wt | 20.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF2]] | +0.74 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[HIVEP2]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 | same gene group; STRING 460 |
| [[BAZ1A]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TSC22D1]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[GALNT7-DT]] | +0.64 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[HSPBAP1]] | +0.63 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[ZBED5]] | +0.63 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[LINC00944]] | +0.62 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[BAHCC1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ANXA2R-AS1]] | +0.61 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[CLOCK]] | +0.61 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SATB2]] | +0.61 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN2]] | -0.67 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[VAMP7]] | -0.65 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MED23]] | -0.64 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[OPA1]] | -0.64 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[LONP2]] | -0.63 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[RNF216P1]] | -0.63 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[RTCA]] | -0.60 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PLA2G12A]] | -0.60 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[HIBCH]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[EDRF1]] | -0.60 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[EDEM2]] | -0.60 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[FRG1CP]] | -0.59 | -0.50 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF462]] | B | ZNF462 activity lowers HIVEP1's level | lines that do not express ZNF462 (5) vs lines expressing it (45) | 1.88× higher at baseline in the lines without ZNF462 | 0.054 | ⚠ within organs, on part of the lines; also absent: PDE11A, ENSG00000214803 |
| [[CACNA2D1]] | B | CACNA2D1 activity lowers HIVEP1's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.12× higher at baseline in the lines without CACNA2D1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[SATB2]] | C | SATB2 activity lowers HIVEP1's level | lines that do not express SATB2 (3) vs lines expressing it (47) | 2.14× higher at baseline in the lines without SATB2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP3, MCF2, LCA5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.0, -5.4); signed map (16.6, -8.5). **Vector** length 126, 43.6% of its response variance represented; |z| ≥ 3 in 1,665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.5 | +8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.1 | +21.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +40.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.3 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -8.8 | -6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.8 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.1 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.1 | -19.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.0 | -10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -5.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.5 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | HIVEP zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.1 — chr6:12,008,762-12,164,999 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CIRIP, MBP-1, CRYBP1, PRDII-BF1, ZAS1, Schnurri-1, ZNF40A; previously ZNF40 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P15822](https://www.uniprot.org/uniprotkb/P15822) (Zinc finger protein 40):

> This protein specifically binds to the DNA sequence 5'-GGGACTTTCC-3' which is found in the enhancer elements of numerous viral promoters such as those of SV40, CMV, or HIV-1. In addition, related sequences are found in the enhancer elements of a number of cellular promoters, including those of the class I MHC, interleukin-2 receptor, and interferon-beta genes. It may act in T-cell activation. Involved in activating HIV-1 gene expression. Isoform 2 and isoform 3 also bind to the IPCS (IRF1 and …

**Summary**, from NCBI Gene [3096](https://www.ncbi.nlm.nih.gov/gene/3096):

> This gene encodes a transcription factor belonging to the ZAS family, members of which are large proteins that contain a ZAS domain - a modular protein structure consisting of a pair of C2H2 zinc fingers with an acidic-rich region and a serine/threonine-rich sequence. These proteins bind specifically to the DNA sequence motif, GGGACTTTCC, found in the enhancer elements of several viral promoters, including human immunodeficiency virus (HIV), and to related sequences found in the enhancer …

**Accessions** — [HGNC:4920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4920) · Entrez [3096](https://www.ncbi.nlm.nih.gov/gene/3096) · UniProt [P15822](https://www.uniprot.org/uniprotkb/P15822) · Ensembl [ENSG00000095951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095951)

## Data

Gene col 1758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1758); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1758]; `tensor/DDL_lfc|DDL_z.npy` [1758]; `embed/gene_vectors.npy` [1758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1758 or target_col == 1758). Every well: [[HIVEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIVEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
