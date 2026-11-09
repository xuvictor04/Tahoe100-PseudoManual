---
symbol: "FMNL2"
type: "gene"
col: 8104
ensembl_id: "ENSG00000157827"
name: "formin like 2"
location: "2q23.3"
module: 193
arm: "+"
pooled_cpm: 472.77
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 30
n_dd_up_clean: 8
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# FMNL2

*formin like 2* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.27× (z +5.6, q 1e-05, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.504× (z -22.7, q 0e+00, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK9]] (+0.63, fdr 1e-05), [[PAQR5]] (+0.63, fdr 1e-05), [[CAPRIN2]] (+0.60, fdr 7e-06); moves opposite to [[BTN3A1]] (-0.55, fdr 3e-05), [[RBM23]] (-0.53, fdr 2e-04), [[CNOT3]] (-0.52, fdr 8e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +5.6 | 1e-05 | 24/46 (AsPC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +5.5 | 1e-05 | 28/46 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.50×** | +4.9 | 1e-04 | 29/47 (NCI-H23, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.47×** | +4.8 | 3e-04 | 31/46 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.7 | 3e-04 | 22/45 (NCI-H1792, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.2 | 0.003 | 15/47 (SHP-77, CFPAC-1, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +4.0 | 0.005 | 18/46 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.0 | 0.005 | 21/46 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.006 | 25/46 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.7 | 0.011 | 16/47 (AN3 CA, A-427, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +3.7 | 0.011 | 20/45 (SHP-77, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.7 | 0.011 | 21/46 (SW1417, SW480, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.013 | 22/46 (SW480, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.6 | 0.015 | 15/46 (A-427, BT-474, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.024 | 17/46 (J82, NCI-H2030, …) | rises with dose |  |
| [[Penfluridol (drug)]] 5 µM |  | 1.17× | +3.3 | 0.034 | 17/45 (A498, HS-578T, …) | top dose only |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.16× | +3.2 | 0.043 | 9/47 (C32, PANC-1, …) | rises with dose | plate-row cell shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.10× | +3.1 | 0.047 | 5/46 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.048 | 16/46 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.504×** | -22.7 | 0e+00 | 35/47 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -20.0 | 0e+00 | 37/46 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.432×** | -19.7 | 0e+00 | 44/47 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -16.3 | 0e+00 | 39/43 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.497×** | -15.1 | 0e+00 | 40/44 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -12.7 | 4e-35 | 38/45 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -8.5 | 1e-15 | 27/46 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.736×** | -7.1 | 6e-11 | 33/46 (PANC-1, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.774×** | -6.9 | 5e-10 | 29/46 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.731×** | -6.7 | 1e-09 | 27/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.752×** | -6.7 | 1e-09 | 27/46 (C32, A549, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.807×** | -6.5 | 5e-09 | 29/47 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.759×** | -6.4 | 6e-09 | 29/45 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.766×** | -6.2 | 2e-08 | 28/46 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.758×** | -5.9 | 1e-07 | 30/46 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.808×** | -5.8 | 2e-07 | 25/46 (AsPC-1, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.798×** | -5.7 | 5e-07 | 26/47 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.787×** | -5.6 | 7e-07 | 25/47 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -5.2 | 7e-06 | 31/46 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.656×** | -5.2 | 7e-06 | 26/45 (NCI-H23, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.784×** | -4.8 | 4e-05 | 28/46 (AsPC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.801×** | -4.7 | 5e-05 | 25/45 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 586 | 2 | 17 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.03× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -21.9) |
| [[C32 (line)]] | wt | 1,108 | 0 | 16 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -28.2) |
| [[NCI-H23 (line)]] | alt | 689 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -37.5) |
| [[LOX-IMVI (line)]] | wt | 691 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -32.6) |
| [[MIA PaCa-2 (line)]] | alt | 1,384 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -37.0) |
| [[SK-MEL-2 (line)]] | alt | 913 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -24.1) |
| [[A549 (line)]] | wt | 936 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -30.7) |
| [[Hs 766T (line)]] | wt | 263 | 11 | 0 | [[Dexamethasone (drug)]] 5 µM 2.50× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 965 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -25.6) |
| [[HS-578T (line)]] | alt | 595 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -27.0) |
| [[NCI-H460 (line)]] | wt | 772 | 1 (1 ⚠) | 7 (4 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.34× (z +11.2) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -27.5) |
| [[RPMI-7951 (line)]] | alt | 632 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -19.5) |
| [[C-33 A (line)]] | alt | 920 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 406 | 2 (2 ⚠) | 5 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.63× (z +12.4) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.341× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.502× (z -13.6) |
| [[PANC-1 (line)]] | alt | 581 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -23.4) |
| [[SNU-423 (line)]] | alt | 591 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -21.8) |
| [[SW48 (line)]] | wt | 428 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.71× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -17.7) |
| [[HepG2_C3A (line)]] | wt | 751 | 0 | 6 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -17.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 685 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -15.5) |
| [[RKO (line)]] | wt | 539 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -23.4) |
| [[NCI-H1573 (line)]] | alt | 141 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -16.0) |
| [[SW 1271 (line)]] | alt | 1,056 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -14.9) |
| [[A498 (line)]] | wt | 618 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -9.1) |
| [[J82 (line)]] | alt | 267 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -13.6) |
| [[SW 900 (line)]] | alt | 308 | 3 (3 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.47× (z +10.2) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.7) |
| [[SW480 (line)]] | alt | 337 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.05 µM 1.65× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.63× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.513× (z -11.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 313 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -11.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 417 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -13.5) |
| [[SW1417 (line)]] | alt | 231 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.538× (z -8.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 308 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -11.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 220 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -14.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 154 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.90× (z +8.5) | [[Cobimetinib (drug)]] 0.5 µM 0.358× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 192 | 1 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.85× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.416× (z -8.6) ⚠ toxic |
| [[H4 (line)]] | wt | 304 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -13.5) |
| [[HOP62 (line)]] | alt | 337 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 273 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.15× (z +9.7) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -15.5) |
| [[SHP-77 (line)]] | alt | 215 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.03× (z +11.4) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.84× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 281 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.4) |
| [[HCT15 (line)]] | alt | 226 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -9.2) |
| [[KATO III (line)]] | alt | 214 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -10.9) |
| [[LS 180 (line)]] | wt | 258 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -12.0) |
| [[SNU-1 (line)]] | wt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.0) |
| [[AN3 CA (line)]] | alt | 326 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 73.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 537 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 510 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 537 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK9]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 | same gene group; pathway: CDC42 GTPase cycle |
| [[PAQR5]] | +0.63 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[CAPRIN2]] | +0.60 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[BMP6]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PPP2R2C]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[RASA2]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[CSGALNACT2]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.57 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[HK1]] | +0.57 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[PALS2]] | +0.57 | +0.68 / +0.38 | both halves | 6e-05 |  |
| [[PTPN12]] | +0.57 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[BMP2K]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A1]] | -0.55 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[RBM23]] | -0.53 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[CNOT3]] | -0.52 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[BTN3A3]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TAPBPL]] | -0.50 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[NSUN3]] | -0.49 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[PSMC2]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SAR1B]] | -0.49 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[P4HTM]] | -0.49 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[TLR3]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[XRN1]] | -0.49 | -0.59 / -0.32 | both halves | 1e-04 |  |
| [[MR1]] | -0.49 | -0.62 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises FMNL2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.0% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds |
| [[ITPRIP]] | B | ITPRIP activity raises FMNL2's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 2.38× lower at baseline in the lines without ITPRIP | 0.020 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises FMNL2's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without FAM78B | 0.025 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[BMP6]] | B | BMP6 activity raises FMNL2's level | lines that do not express BMP6 (23) vs lines expressing it (27) | 1.65× lower at baseline in the lines without BMP6 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000289418, LRRN2, LINC02864 |
| [[LDLRAD3]] | B | LDLRAD3 activity raises FMNL2's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.85× lower at baseline in the lines without LDLRAD3 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NPAS2]] | B | NPAS2 activity raises FMNL2's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.69× lower at baseline in the lines without NPAS2 | 0.094 | ⚠ within organs, on part of the lines |
| [[PALS2]] | C | PALS2 activity raises FMNL2's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 3.87× lower at baseline in the lines without PALS2 | 0.032 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[FSD1L]] | C | FSD1L activity raises FMNL2's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 3.22× lower at baseline in the lines without FSD1L | 0.067 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.5, 5.5); signed map (-0.2, 50.2). **Vector** length 134, 49.6% of its response variance represented; |z| ≥ 3 in 2,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +5.6 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.2 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.0 | -6.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.4 | +3.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.8 | -20.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.7 | -5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.6 | -4.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.5 | -6.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -6.4 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.3 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | formin like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:152,335,174-152,649,826 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1902; previously FHOD2 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Reactome | 7 pathways, smallest: RHOC GTPase cycle; RHO GTPases Activate Formins; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PY5](https://www.uniprot.org/uniprotkb/Q96PY5) (Formin-like protein 2):

> Plays a role in actin cytoskeleton dynamics and regulation of cell shape.

**Summary**, from NCBI Gene [114793](https://www.ncbi.nlm.nih.gov/gene/114793):

> This gene encodes a formin-related protein. Formin-related proteins have been implicated in morphogenesis, cytokinesis, and cell polarity. Alternatively spliced transcript variants encoding different isoforms have been described but their full-length nature has yet to be determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18267) · Entrez [114793](https://www.ncbi.nlm.nih.gov/gene/114793) · UniProt [Q96PY5](https://www.uniprot.org/uniprotkb/Q96PY5) · Ensembl [ENSG00000157827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157827)

## Data

Gene col 8104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8104); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8104]; `tensor/DDL_lfc|DDL_z.npy` [8104]; `embed/gene_vectors.npy` [8104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8104 or target_col == 8104). Every well: [[FMNL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMNL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
