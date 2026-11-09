---
symbol: "CDCA8"
type: "gene"
col: 5589
ensembl_id: "ENSG00000134690"
name: "cell division cycle associated 8"
location: "1p34.3"
module: 22
arm: "+"
pooled_cpm: 34.76
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CDCA8

*cell division cycle associated 8* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (16 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.56× (z +17.3, q 0e+00, up in 44 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +6.0, q 1e-07, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.543× (z -11.7, q 8e-29, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~89% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.796× (z -4.3, q 9e-04, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF2C]] (+0.95, fdr 7e-06), [[GTSE1]] (+0.95, fdr 7e-06), [[NDC80]] (+0.93, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.56×** | +17.3 | 0e+00 | 44/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **3.42×** | +16.7 | 0e+00 | 45/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.12×** | +14.4 | 6e-45 | 37/47 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.28×** | +11.2 | 6e-27 | 44/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.18×** | +10.6 | 3e-24 | 43/46 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **2.19×** | +10.3 | 1e-22 | 42/47 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~91% of this change | **1.83×** | +8.2 | 2e-14 | 35/44 (PANC-1, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.77×** | +7.8 | 4e-13 | 34/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.75×** | +7.6 | 1e-12 | 29/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | **1.62×** | +6.3 | 1e-08 | 25/46 (LoVo, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.41×** | +6.2 | 2e-08 | 29/47 (HT-29, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.0 | 1e-07 | 25/46 (AsPC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +5.1 | 2e-05 | 25/47 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.95×** | +4.8 | 8e-05 | 23/45 (PANC-1, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +4.7 | 9e-05 | 25/47 (SW 900, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.34×** | +4.0 | 0.002 | 19/47 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.003 | 23/47 (HT-29, PANC-1, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.019 | 10/44 (HOP62, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.023 | 13/46 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.055 | 13/47 (HOP62, A498, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.057 | 10/47 (SW480, J82, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.087 | 10/47 (NCI-H23, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.543×** | -11.7 | 8e-29 | 36/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.483×** | -9.9 | 2e-20 | 39/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.619×** | -6.1 | 2e-07 | 29/47 (HOP62, SK-MEL-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.642×** | -6.0 | 3e-07 | 36/47 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.684×** | -5.1 | 3e-05 | 22/46 (A498, SNU-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.715×** | -4.5 | 5e-04 | 22/43 (RKO, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.716×** | -4.5 | 5e-04 | 24/46 (A549, SNU-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -4.3 | 9e-04 | 24/47 (SHP-77, SW 1271, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.716×** | -4.3 | 9e-04 | 19/47 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.739×** | -4.1 | 0.003 | 20/47 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.007 | 22/47 (HT-29, HOP62, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.009 | 19/47 (H4, NCI-H460, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.013 | 23/47 (A498, LOX-IMVI, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.765×** | -3.6 | 0.013 | 12/47 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.627×** | -3.3 | 0.036 | 14/46 (RPMI-7951, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.841× | -3.3 | 0.036 | 14/47 (MIA PaCa-2, HCT15, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.777×** | -3.1 | 0.047 | 13/47 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.800×** | -3.0 | 0.073 | 15/46 (Hs 766T, KATO III, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +1.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 40.6 | 9 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +20.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 35.4 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.216× (z -17.5) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.459× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 36.0 | 2 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.179× (z -14.4) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.152× (z -11.2) |
| [[LS 180 (line)]] | wt | 31.4 | 2 (2 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.81× (z +11.5) ⚠ cell-cycle shift, explains ~48% of this change | [[Selinexor (drug)]] 5 µM 0.214× (z -13.1) ⚠ cell-cycle shift, explains ~89% of this change |
| [[NCI-H23 (line)]] | alt | 60.1 | 6 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.19× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 43.3 | 4 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +20.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.212× (z -10.4) ⚠ cell-cycle shift, explains ~87% of this change |
| [[NCI-H460 (line)]] | wt | 22.2 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.240× (z -13.6) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HOP62 (line)]] | alt | 58.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.60× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 5 µM 0.248× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 26.6 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.2× (z +14.7) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SW480 (line)]] | alt | 43.8 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.49× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-427 (line)]] | wt | 57.5 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.210× (z -17.5) ⚠ cell-cycle shift, explains ~89% of this change |
| [[H4 (line)]] | wt | 40.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 6.55× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Selinexor (drug)]] 5 µM 0.0816× (z -16.0) ⚠ cell-cycle shift, explains ~89% of this change |
| [[LoVo (line)]] | wt | 19.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.58× (z +12.1) ⚠ cell-cycle shift, explains ~48% of this change | [[Selinexor (drug)]] 5 µM 0.386× (z -8.6) ⚠ cell-cycle shift, explains ~89% of this change |
| [[NCI-H2347 (line)]] | alt | 41.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +13.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.433× (z -9.1) ⚠ cell-cycle shift, explains ~89% of this change |
| [[SW1417 (line)]] | alt | 35.0 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +10.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HS-578T (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 27.4 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.07× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[J82 (line)]] | alt | 42.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +9.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H2030 (line)]] | alt | 43.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +15.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.0946× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 44.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.154× (z -11.7) ⚠ cell-cycle shift, explains ~89% of this change |
| [[SW 900 (line)]] | alt | 36.8 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.65× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A549 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.176× (z -8.6) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 45.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.97× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.210× (z -9.6) ⚠ cell-cycle shift, explains ~89% of this change |
| [[Panc 03.27 (line)]] | alt | 32.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +16.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF2C]] | +0.95 | +0.95 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 977 |
| [[GTSE1]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 643 |
| [[NDC80]] | +0.93 | +0.94 / +0.93 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 907 |
| [[CDCA3]] | +0.93 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 975 |
| [[TACC3]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 904 |
| [[DLGAP5]] | +0.91 | +0.94 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 961 |
| [[SGO2]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 960 |
| [[TROAP]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | STRING 794 |
| [[CDK1]] | +0.91 | +0.92 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 990 |
| [[KIF18A]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 742 |
| [[UBE2C]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 966 |
| [[BUB1]] | +0.90 | +0.92 / +0.89 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 971 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CDCA8's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.25× lower at baseline in the lines without PIMREG | 0.012 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises CDCA8's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without NEURL1B | 0.090 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PBK]] | C | PBK activity raises CDCA8's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without PBK | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CDCA8's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without AURKB | 0.027 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises CDCA8's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.39× lower at baseline in the lines without NDC80 | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises CDCA8's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.69× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises CDCA8's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises CDCA8's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.86× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises CDCA8's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.56× lower at baseline in the lines without ACBD7 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.942). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.4, -56.4); signed map (-50.0, -41.9). **Vector** length 136, 49.7% of its response variance represented; |z| ≥ 3 in 1,359 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.76 to 60); *DREAM G2/M down* (control, mean cos +0.85 to 28); *mitotic spindle* (hallmark, mean cos +0.76 to 38).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~91% of this change | +6.1 | +8.2 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.8 | +14.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +6.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.6 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.3 | +2.3 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -8.1 | -9.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~99% of this change | -7.7 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -7.4 | -11.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.0 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -0.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.5 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle associated 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,692,481-37,709,719 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12042, MESRGP, BOR, DasraB |
| Gene groups (HGNC) | Chromosomal passenger complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 20 pathways, smallest: SUMOylation of DNA replication proteins; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53HL2](https://www.uniprot.org/uniprotkb/Q53HL2) (Borealin):

> Component of the chromosomal passenger complex (CPC), a complex that acts as a key regulator of mitosis. The CPC complex has essential functions at the centromere in ensuring correct chromosome alignment and segregation and is required for chromatin-induced microtubule stabilization and spindle assembly. Major effector of the TTK kinase in the control of attachment-error-correction and chromosome alignment.

**Summary**, from NCBI Gene [55143](https://www.ncbi.nlm.nih.gov/gene/55143):

> This gene encodes a component of the chromosomal passenger complex. This complex is an essential regulator of mitosis and cell division. This protein is cell-cycle regulated and is required for chromatin-induced microtubule stabilization and spindle formation. Alternate splicing results in multiple transcript variants. Pseudgenes of this gene are found on chromosomes 7, 8 and 16. [provided by RefSeq, Apr 2013]

**Accessions** — [HGNC:14629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14629) · Entrez [55143](https://www.ncbi.nlm.nih.gov/gene/55143) · UniProt [Q53HL2](https://www.uniprot.org/uniprotkb/Q53HL2) · Ensembl [ENSG00000134690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134690)

## Data

Gene col 5589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5589); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5589]; `tensor/DDL_lfc|DDL_z.npy` [5589]; `embed/gene_vectors.npy` [5589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5589 or target_col == 5589). Every well: [[CDCA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDCA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
