---
symbol: "SNX9"
type: "gene"
col: 5055
ensembl_id: "ENSG00000130340"
name: "sorting nexin 9"
location: "6q25.3"
module: 206
arm: "+"
pooled_cpm: 283.45
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 34
n_dd_up_clean: 20
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# SNX9

*sorting nexin 9* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +17.1, q 0e+00, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.246× (z -28.9, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.252× (z -28.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMC2]] (+0.62, fdr 7e-06), [[PIK3CD]] (+0.62, fdr 1e-05), [[TRPV3]] (+0.62, fdr 1e-05); moves opposite to [[SEC24C]] (-0.47, fdr 9e-04, ⚠ not reproduced).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PHLDA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +17.1 | 0e+00 | 35/48 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.51×** | +9.9 | 1e-20 | 43/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +9.3 | 3e-18 | 35/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +8.9 | 1e-16 | 36/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.51×** | +8.4 | 3e-15 | 31/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +7.8 | 6e-13 | 40/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +7.5 | 7e-12 | 38/48 (HT-29, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +7.2 | 5e-11 | 35/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +6.8 | 7e-10 | 35/49 (HT-29, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +6.5 | 4e-09 | 31/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +6.3 | 2e-08 | 30/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +6.1 | 6e-08 | 34/48 (HT-29, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.9 | 1e-07 | 30/38 (NCI-H2030, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +5.9 | 1e-07 | 35/48 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.6 | 8e-07 | 30/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +5.5 | 1e-06 | 31/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.58×** | +4.9 | 3e-05 | 33/48 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 1e-04 | 25/48 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +4.3 | 4e-04 | 27/47 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.001 | 26/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.246×** | -28.9 | 0e+00 | 47/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.252×** | -28.3 | 0e+00 | 48/48 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.290×** | -25.5 | 0e+00 | 47/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.578×** | -16.0 | 0e+00 | 40/49 (SW1417, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.510×** | -13.8 | 2e-41 | 45/48 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.522×** | -12.9 | 6e-36 | 37/44 (A-427, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.588×** | -10.9 | 7e-26 | 46/48 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.595×** | -10.3 | 6e-23 | 42/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.646×** | -9.0 | 1e-17 | 35/49 (RKO, LS 180, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.640×** | -8.8 | 5e-17 | 40/48 (SW480, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.761×** | -6.7 | 9e-10 | 34/48 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.535×** | -6.7 | 9e-10 | 43/49 (SW1417, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.715×** | -6.6 | 1e-09 | 38/50 (SW480, SW1417, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.721×** | -6.5 | 4e-09 | 36/48 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.786×** | -6.0 | 6e-08 | 30/48 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.783×** | -5.6 | 7e-07 | 28/50 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.762×** | -5.6 | 8e-07 | 29/49 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.827×** | -5.4 | 2e-06 | 23/49 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.615×** | -5.2 | 5e-06 | 32/48 (SW480, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.834× | -5.2 | 6e-06 | 23/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.801×** | -5.0 | 1e-05 | 28/49 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -5.0 | 2e-05 | 21/48 (HEC-1-A, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 417 | 4 (1 ⚠) | 20 (6 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.82× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.183× (z -25.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.193× (z -24.9) |
| [[NCI-H460 (line)]] | wt | 218 | 17 (6 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.53× (z +24.2) | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -17.6) |
| [[NCI-H1573 (line)]] | alt | 237 | 10 (4 ⚠) | 9 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 6.70× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.284× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 470 | 8 (2 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +18.1) | [[Belinostat (drug)]] 5 µM 0.234× (z -18.0) |
| [[PANC-1 (line)]] | alt | 292 | 8 (2 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +22.8) | [[Panobinostat (drug)]] 5 µM 0.213× (z -22.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.218× (z -21.7) |
| [[HEC-1-A (line)]] | alt | 457 | 1 | 13 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.06× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -23.0) |
| [[HT-29 (line)]] | alt | 149 | 8 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.175× (z -23.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.245× (z -19.0) |
| [[SW1417 (line)]] | alt | 646 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -27.9) |
| [[HepG2_C3A (line)]] | wt | 305 | 6 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 340 | 1 | 12 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -27.4) |
| [[A549 (line)]] | wt | 184 | 5 (2 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +21.3) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -18.5) |
| [[BT-474 (line)]] | alt | 149 | 11 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.74× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[CFPAC-1 (line)]] | alt | 244 | 2 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -21.8) |
| [[LoVo (line)]] | wt | 352 | 3 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.113× (z -32.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.148× (z -28.5) |
| [[NCI-H23 (line)]] | alt | 234 | 0 | 11 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.569× (z -19.9) ⚠ position not correctable · without an alert: [[Belinostat (drug)]] 5 µM 0.275× (z -13.0) |
| [[SW48 (line)]] | wt | 711 | 1 | 10 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.87× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.143× (z -20.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.154× (z -19.3) |
| [[hTERT-HPNE (line)]] | wt | 390 | 1 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.218× (z -16.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -16.6) |
| [[MIA PaCa-2 (line)]] | alt | 266 | 2 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +21.0) | [[Panobinostat (drug)]] 5 µM 0.126× (z -28.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.162× (z -25.3) |
| [[SNU-423 (line)]] | alt | 450 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +27.7) | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -19.4) |
| [[C32 (line)]] | wt | 247 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.22× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -14.7) |
| [[Hs 766T (line)]] | wt | 186 | 5 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +28.6) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -13.0) |
| [[LS 180 (line)]] | wt | 386 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -25.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.157× (z -24.1) |
| [[A-172 (line)]] | wt | 199 | 3 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +29.1) | [[Panobinostat (drug)]] 5 µM 0.270× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.284× (z -13.7) |
| [[H4 (line)]] | wt | 138 | 3 (1 ⚠) | 4 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.92× (z +12.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.218× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.284× (z -11.7) |
| [[KATO III (line)]] | alt | 497 | 2 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.143× (z -24.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.168× (z -22.3) |
| [[NCI-H1792 (line)]] | alt | 337 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -19.0) |
| [[RKO (line)]] | wt | 270 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -20.8) |
| [[A498 (line)]] | wt | 146 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +24.2) | [[Belinostat (drug)]] 5 µM 0.368× (z -13.5) |
| [[COLO 205 (line)]] | alt | 169 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.69× (z +28.0) | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -20.4) |
| [[HOP62 (line)]] | alt | 244 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -16.5) |
| [[HS-578T (line)]] | alt | 321 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 188 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.215× (z -23.5) |
| [[NCI-H2030 (line)]] | alt | 271 | 3 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.450× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 249 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -11.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.386× (z -11.2) |
| [[SW 900 (line)]] | alt | 236 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.246× (z -16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.284× (z -14.5) |
| [[A-427 (line)]] | wt | 139 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.369× (z -14.9) |
| [[C-33 A (line)]] | alt | 156 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -16.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.315× (z -13.4) |
| [[HCT15 (line)]] | alt | 315 | 1 | 4 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.78× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.393× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 244 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -20.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.207× (z -19.0) |
| [[AN3 CA (line)]] | alt | 274 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -13.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.294× (z -11.4) |
| [[J82 (line)]] | alt | 172 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -12.8) |
| [[SNU-1 (line)]] | wt | 240 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.393× (z -10.2) |
| [[CHP-212 (line)]] | wt | 165 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -10.1) |
| [[SHP-77 (line)]] | alt | 142 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.393× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.422× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 206 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +26.2) | — |
| [[SW 1271 (line)]] | alt | 226 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2122 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMC2]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PIK3CD]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 | STRING 660 |
| [[TRPV3]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[LINC00513]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[HMGA1]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[UPP1]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CDCP1]] | +0.57 | +0.60 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[SMCO2]] | +0.56 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[LAMB3]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ITGA2]] | +0.56 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[PLAU]] | +0.56 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[FOSL1]] | +0.56 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC24C]] | -0.47 | -0.18 / -0.47 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHLDA2]] | B | PHLDA2 activity raises SNX9's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without PHLDA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[CLCF1]] | B | CLCF1 activity raises SNX9's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without CLCF1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises SNX9's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds |
| [[DELEC1]] | B | DELEC1 activity raises SNX9's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without DELEC1 | 0.039 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[LAMB3]] | B | LAMB3 activity raises SNX9's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.40× lower at baseline in the lines without LAMB3 | 0.055 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[UPP1]] | B | UPP1 activity raises SNX9's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without UPP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[FOSL1]] | B | FOSL1 activity raises SNX9's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without FOSL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[PLAUR]] | B | PLAUR activity raises SNX9's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 1.34× lower at baseline in the lines without PLAUR | 0.089 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[SYT14]] | B | SYT14 activity lowers SNX9's level | lines that do not express SYT14 (29) vs lines expressing it (21) | 1.05× higher at baseline in the lines without SYT14 | 0.091 | ⚠ within organs, on part of the lines; also absent: ITGA4, MMP2, PHACTR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.9, -0.8); signed map (2.5, 33.8). **Vector** length 104, 42.4% of its response variance represented; |z| ≥ 3 in 2,467 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.6 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.0 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +8.7 | -12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +8.6 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +7.7 | +8.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +5.3 | +2.2 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +4.6 | +3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +6.5 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +3.9 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.0 | +8.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.4 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.6 | -5.6 |
|  | [[NG25 (drug)]] 5 µM |  | -4.5 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.5 | -5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.4 | -6.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:157,700,387-157,945,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SH3PX1, SDP1, SH3PXD3A |
| Gene groups (HGNC) | Sorting nexins; PX-BAR domain containing; SH3 domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 5 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5X1](https://www.uniprot.org/uniprotkb/Q9Y5X1) (Sorting nexin-9):

> Involved in endocytosis and intracellular vesicle trafficking, both during interphase and at the end of mitosis. Required for efficient progress through mitosis and cytokinesis. Required for normal formation of the cleavage furrow at the end of mitosis. Plays a role in endocytosis via clathrin-coated pits, but also clathrin-independent, actin-dependent fluid-phase endocytosis. Plays a role in macropinocytosis. Promotes internalization of TNFR. Promotes degradation of EGFR after EGF signaling. …

**Summary**, from NCBI Gene [51429](https://www.ncbi.nlm.nih.gov/gene/51429):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phosphoinositide binding domain, and are involved in intracellular trafficking. The encoded protein does not contain a coiled coil region, like some family members, but does contain a SRC homology domain near its N-terminus. The encoded protein is reported to have a variety of interaction partners, including of adaptor protein 2 , dynamin, tyrosine kinase non-receptor 2, Wiskott-Aldrich syndrome-like, and …

**Accessions** — [HGNC:14973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14973) · Entrez [51429](https://www.ncbi.nlm.nih.gov/gene/51429) · UniProt [Q9Y5X1](https://www.uniprot.org/uniprotkb/Q9Y5X1) · Ensembl [ENSG00000130340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130340)

## Data

Gene col 5055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5055); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5055]; `tensor/DDL_lfc|DDL_z.npy` [5055]; `embed/gene_vectors.npy` [5055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5055 or target_col == 5055). Every well: [[SNX9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
