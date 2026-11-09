---
symbol: "CCNB1"
type: "gene"
col: 5504
ensembl_id: "ENSG00000134057"
name: "cyclin B1"
location: "5q13.2"
module: 22
arm: "+"
pooled_cpm: 47.88
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 31
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CCNB1

*cyclin B1* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +12.6, q 8e-34, up in 32 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.44× (z +6.4, q 1e-08, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.507× (z -8.3, q 4e-14, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~95% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.687× (z -6.7, q 3e-09, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLK1]] (+0.93, fdr 7e-06), [[CCNB2]] (+0.93, fdr 7e-06), [[BUB1]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.05×** | +12.6 | 8e-34 | 32/47 (Panc 03.27, NCI-H2030, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **2.43×** | +11.0 | 7e-26 | 45/47 (PANC-1, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.11×** | +9.3 | 2e-18 | 40/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **3.09×** | +7.4 | 2e-11 | 37/46 (PANC-1, J82, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.80×** | +7.3 | 2e-11 | 35/46 (KATO III, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.79×** | +7.2 | 4e-11 | 32/46 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.83×** | +7.2 | 4e-11 | 32/47 (A549, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.75×** | +7.0 | 2e-10 | 38/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.47×** | +6.8 | 7e-10 | 38/47 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.44×** | +6.4 | 1e-08 | 36/47 (HT-29, HEC-1-A, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.62×** | +5.9 | 3e-07 | 32/47 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.57×** | +5.6 | 1e-06 | 26/46 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.56×** | +5.5 | 2e-06 | 34/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.53×** | +5.3 | 4e-06 | 30/47 (HOP62, HT-29, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.52×** | +5.2 | 6e-06 | 30/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.49×** | +4.8 | 5e-05 | 27/47 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +4.6 | 2e-04 | 24/46 (HOP62, SW 900, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.49×** | +4.5 | 2e-04 | 26/47 (SW 900, NCI-H460, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.001 | 25/46 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.002 | 21/47 (SW 900, HT-29, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.004 | 20/47 (HOP62, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 1.19× | +3.1 | 0.040 | 16/47 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.047 | 19/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.047 | 13/47 (HT-29, SW 900, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 0.05 µM |  | **1.27×** | +2.8 | 0.091 | 13/47 (NCI-H2347, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.507×** | -8.3 | 4e-14 | 39/47 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.503×** | -8.3 | 4e-14 | 43/47 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.630×** | -8.2 | 4e-14 | 36/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.562×** | -7.2 | 7e-11 | 37/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.687×** | -6.7 | 3e-09 | 31/47 (A498, H4, …) | top dose only |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.599×** | -6.4 | 1e-08 | 34/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.593×** | -6.3 | 2e-08 | 33/47 (H4, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -5.9 | 3e-07 | 32/47 (SK-MEL-2, AsPC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.618×** | -5.9 | 3e-07 | 30/47 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.722×** | -5.5 | 3e-06 | 31/47 (SNU-1, SW48, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.435×** | -5.5 | 3e-06 | 32/47 (A549, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.655×** | -4.9 | 4e-05 | 29/47 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.683×** | -4.8 | 7e-05 | 27/47 (HCT15, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.686×** | -4.7 | 9e-05 | 32/47 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.692×** | -4.6 | 1e-04 | 25/47 (NCI-H2347, A498, …) | all doses, flat | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.673×** | -4.6 | 1e-04 | 24/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -4.0 | 0.002 | 20/47 (SW1417, NCI-H2347, …) | rises with dose | position effect removed |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.731×** | -4.0 | 0.002 | 23/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.740×** | -3.8 | 0.004 | 25/47 (SW48, NCI-H460, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.730×** | -3.7 | 0.006 | 23/46 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.755×** | -3.5 | 0.010 | 15/47 (LS 180, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ciclopirox (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.017 | 15/47 (Hs 766T, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.761×** | -3.4 | 0.017 | 20/47 (SW48, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.769×** | -3.3 | 0.019 | 11/47 (A549, NCI-H2347, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +1.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 47.4 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0880× (z -29.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.358× (z -12.4) |
| [[KATO III (line)]] | alt | 31.7 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.22× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.156× (z -14.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.191× (z -9.1) |
| [[LS 180 (line)]] | wt | 40.0 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.220× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 37.7 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.266× (z -8.6) ⚠ cell-cycle shift, explains ~74% of this change |
| [[A-427 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.220× (z -15.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 40.3 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.7) ⚠ cell-cycle shift, would explain all of this change | [[Amsacrine (drug)]] 5 µM 0.406× (z -8.9) |
| [[C32 (line)]] | wt | 29.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.195× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 62.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.174× (z -11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.219× (z -9.9) |
| [[HOP62 (line)]] | alt | 24.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 32.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 43.8 | 2 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 5.40× (z +9.7) ⚠ transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 2.97× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 59.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 46.4 | 2 (2 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 3.29× (z +9.9) ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[SW 900 (line)]] | alt | 50.0 | 2 (2 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 4.25× (z +9.7) ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 47.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 34.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.403× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 46.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +15.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 36.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 50.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.185× (z -11.0) |
| [[SNU-1 (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.177× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 117 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 71.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLK1]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 999 |
| [[CCNB2]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of NIMA Kinases NEK9, NEK6, NEK7; STRING 998 |
| [[BUB1]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 992 |
| [[DLGAP5]] | +0.92 | +0.91 / +0.93 | both halves | 7e-06 | STRING 965 |
| [[KIF20A]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | STRING 954 |
| [[AURKA]] | +0.92 | +0.91 / +0.94 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 979 |
| [[KNSTRN]] | +0.91 | +0.89 / +0.93 | both halves | 7e-06 | STRING 609 |
| [[CENPF]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 988 |
| [[CCNA2]] | +0.90 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: APC/C-mediated degradation of cell cycle proteins; STRING 995 |
| [[ARHGAP11A]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | STRING 582 |
| [[DEPDC1]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | STRING 871 |
| [[ASPM]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | STRING 952 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CCNB1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.31× lower at baseline in the lines without PIMREG | 0.023 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CCNB1's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NDC80]] | C | NDC80 activity raises CCNB1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without NDC80 | 0.057 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CCNB1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.68× lower at baseline in the lines without AURKB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises CCNB1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.76× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[SAPCD2]] | C | SAPCD2 activity raises CCNB1's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.59× lower at baseline in the lines without SAPCD2 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises CCNB1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.96× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent genes |
| [[PBK]] | C | PBK activity raises CCNB1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.55× lower at baseline in the lines without PBK | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.918). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.7, -57.0); signed map (-50.9, -43.2). **Vector** length 154, 58.0% of its response variance represented; |z| ≥ 3 in 1,621 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.74 to 60); *E2F targets* (hallmark, mean cos +0.70 to 46); *mitotic spindle* (hallmark, mean cos +0.74 to 38).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +9.0 | +12.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | +8.6 | +11.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +6.9 | +7.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +5.9 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | +7.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.8 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.6 | +5.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.3 | +3.0 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +3.1 | +4.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.1 | +3.0 |
| fall | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -7.5 | -8.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -7.2 | -8.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -6.7 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.5 | -4.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -6.4 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -5.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.2 | -6.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -5.1 | -5.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -5.1 | -4.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -4.7 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclin B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,167,135-69,178,245 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CCNB |
| Gene groups (HGNC) | Cyclins |
| Reactome | 52 pathways, smallest: G2/M DNA replication checkpoint; Phosphorylation of Emi1; Activation of NIMA Kinases NEK9, NEK6, NEK7 |
| Matched by | ensembl_id |

**Function**, from UniProt [P14635](https://www.uniprot.org/uniprotkb/P14635) (G2/mitotic-specific cyclin-B1):

> Essential for the control of the cell cycle at the G2/M (mitosis) transition. Binds and activates cyclin-dependent protein kinase CDK1/CDC2.

**Summary**, from NCBI Gene [891](https://www.ncbi.nlm.nih.gov/gene/891):

> The protein encoded by this gene is a regulatory protein involved in mitosis. The gene product complexes with p34(cdc2) to form the maturation-promoting factor (MPF). The encoded protein is necessary for proper control of the G2/M transition phase of the cell cycle. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:1579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1579) · Entrez [891](https://www.ncbi.nlm.nih.gov/gene/891) · UniProt [P14635](https://www.uniprot.org/uniprotkb/P14635) · Ensembl [ENSG00000134057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134057)

## Data

Gene col 5504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5504); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5504]; `tensor/DDL_lfc|DDL_z.npy` [5504]; `embed/gene_vectors.npy` [5504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5504 or target_col == 5504). Every well: [[CCNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
