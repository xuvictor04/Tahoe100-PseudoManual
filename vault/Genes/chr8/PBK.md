---
symbol: "PBK"
type: "gene"
col: 9595
ensembl_id: "ENSG00000168078"
name: "PDZ binding kinase"
location: "8p21.1"
module: 67
arm: "+"
pooled_cpm: 31.65
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 139
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# PBK

*PDZ binding kinase* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.18× (z +13.0, q 9e-36, up in 40 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change. The strongest without an alert is [[Berbamine (drug)]] 0.05 µM: 1.38× (z +3.6, q 0.017, up in 18 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.80×, A498 3.87×, A549 5.27×, NCI-H460 4.65×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 3.57×, A-172 4.56×, A549 4.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 2.94×).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.496× (z -7.8, q 4e-12, down in 30 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIT]] (+0.91, fdr 7e-06), [[MAD2L1]] (+0.91, fdr 7e-06), [[PARPBP]] (+0.90, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GGH]] → it (grade B ⚠); 139 go from it, the strongest it → [[NCAPG2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 17 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9595.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.80×, A498 3.87×, A549 5.27×, NCI-H460 4.65×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 3.57×, A-172 4.56×, A549 4.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 2.94×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **3.18×** | +13.0 | 9e-36 | 40/42 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **3.05×** | +12.0 | 8e-31 | 35/37 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.27×** | +8.5 | 4e-15 | 32/40 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~96% of this change | **1.64×** | +5.5 | 4e-06 | 26/42 (PANC-1, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.41×** | +5.5 | 4e-06 | 33/44 (SW 900, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.48×** | +4.4 | 1e-03 | 21/42 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.42×** | +3.8 | 0.010 | 23/43 (LoVo, A-427, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.39×** | +3.8 | 0.012 | 23/44 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.6 | 0.017 | 21/44 (NCI-H23, KATO III, …) | all doses, flat | composition shift |
| [[Berbamine (drug)]] 0.05 µM |  | **1.38×** | +3.6 | 0.017 | 18/44 (NCI-H460, LS 180, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.77×** | +3.4 | 0.038 | 18/42 (RKO, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.34×** | +3.3 | 0.048 | 14/44 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.22×** | +3.2 | 0.058 | 11/44 (RPMI-7951, Panc 03.27, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.22×** | +3.2 | 0.061 | 13/44 (A549, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.1 | 0.076 | 16/41 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.496×** | -7.8 | 4e-12 | 30/44 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -7.0 | 8e-10 | 27/44 (H4, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.541×** | -6.8 | 2e-09 | 30/44 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.652×** | -6.7 | 3e-09 | 27/44 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.722×** | -5.1 | 4e-05 | 33/44 (HCT15, RPMI-7951, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.731×** | -4.9 | 1e-04 | 24/44 (A-427, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.645×** | -4.8 | 1e-04 | 25/44 (SHP-77, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.649×** | -4.8 | 1e-04 | 31/44 (A498, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.652×** | -4.7 | 1e-04 | 28/44 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.572×** | -4.4 | 6e-04 | 23/44 (A-427, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.587×** | -4.3 | 7e-04 | 31/44 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -4.2 | 0.001 | 20/43 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.606×** | -4.1 | 0.002 | 25/44 (LS 180, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.597×** | -4.1 | 0.002 | 21/44 (NCI-H23, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.705×** | -3.9 | 0.004 | 21/42 (NCI-H460, RPMI-7951, …) | two highest doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.708×** | -3.8 | 0.005 | 23/44 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.788×** | -3.7 | 0.007 | 22/44 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.544×** | -3.5 | 0.013 | 19/43 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.737×** | -3.4 | 0.022 | 16/44 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **0.563×** | -3.3 | 0.024 | 15/44 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.592×** | -3.0 | 0.057 | 16/43 (A-427, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.762×** | -3.0 | 0.063 | 16/43 (RKO, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.600×** | -3.0 | 0.067 | 17/44 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.80 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 33.6 | 1 (1 ⚠) | 7 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Selinexor (drug)]] 5 µM 0.179× (z -19.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -14.0) |
| [[A-172 (line)]] | wt | 32.4 | 2 (2 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.166× (z -11.2) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.381× (z -8.5) |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 40.4 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.1) |
| [[SNU-1 (line)]] | wt | 48.6 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0785× (z -17.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.155× (z -12.6) |
| [[A-427 (line)]] | wt | 76.8 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.211× (z -17.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.1) |
| [[Hs 766T (line)]] | wt | 29.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -10.4) |
| [[PANC-1 (line)]] | alt | 16.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Selinexor (drug)]] 5 µM 0.441× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 33.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.5) |
| [[A549 (line)]] | wt | 27.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Amsacrine (drug)]] 5 µM 0.363× (z -8.6) |
| [[H4 (line)]] | wt | 46.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0549× (z -18.1) |
| [[LoVo (line)]] | wt | 18.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -11.4) |
| [[SW48 (line)]] | wt | 44.9 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.151× (z -10.1) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.292× (z -9.3) |
| [[AN3 CA (line)]] | alt | 54.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -9.0) |
| [[HCT15 (line)]] | alt | 57.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 41.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.1) |
| [[HOP62 (line)]] | alt | 29.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.6) |
| [[HS-578T (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.143× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.6) |
| [[KATO III (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.30× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.216× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 40.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 7.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIT]] | +0.91 | +0.89 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[MAD2L1]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 952 |
| [[PARPBP]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | STRING 669 |
| [[NEIL3]] | +0.90 | +0.89 / +0.87 | both halves | 7e-06 | STRING 557 |
| [[KIF15]] | +0.90 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 873 |
| [[SHCBP1]] | +0.89 | +0.89 / +0.90 | both halves | 7e-06 | STRING 834 |
| [[SPC25]] | +0.89 | +0.91 / +0.89 | both halves | 7e-06 | STRING 877 |
| [[BUB1B]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | STRING 937 |
| [[NCAPD3]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | STRING 406 |
| [[AURKB]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 791 |
| [[UBE2T]] | +0.87 | +0.91 / +0.81 | both halves | 7e-06 | STRING 805 |
| [[NCAPH]] | +0.87 | +0.86 / +0.84 | both halves | 7e-06 | STRING 791 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GGH]] | B | GGH activity raises PBK's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without GGH | 0.018 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[PIMREG]] | C | PIMREG activity raises PBK's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 3.07× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises PBK's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.31× lower at baseline in the lines without AURKB | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[DSCC1]] | C | DSCC1 activity raises PBK's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.57× lower at baseline in the lines without DSCC1 | 0.041 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises PBK's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 4.05× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[NDC80]] | C | NDC80 activity raises PBK's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.09× lower at baseline in the lines without NDC80 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises PBK's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.73× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*139 arrows, 139 of them with an alert ⚠; grade A 0, B 0, C 139. Shown: the 12 strongest; 127 more arrows (127 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCAPG2]] | C | PBK activity raises NCAPG2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without PBK | 0.004 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[PCLAF]] | C | PBK activity raises PCLAF's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without PBK | 0.004 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[TUBB]] | C | PBK activity raises TUBB's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without PBK | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[GUSB]] | C | PBK activity raises GUSB's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.17× lower at baseline in the lines without PBK | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[GMNN]] | C | PBK activity raises GMNN's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without PBK | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CCNB2]] | C | PBK activity raises CCNB2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.40× lower at baseline in the lines without PBK | 0.008 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CENPF]] | C | PBK activity raises CENPF's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.62× lower at baseline in the lines without PBK | 0.009 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[PPP2R5D]] | C | PBK activity raises PPP2R5D's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.03× lower at baseline in the lines without PBK | 0.009 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[UBE2S]] | C | PBK activity raises UBE2S's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.66× lower at baseline in the lines without PBK | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CEP78]] | C | PBK activity raises CEP78's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without PBK | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[KIF15]] | C | PBK activity raises KIF15's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.32× lower at baseline in the lines without PBK | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CKAP2L]] | C | PBK activity raises CKAP2L's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.46× lower at baseline in the lines without PBK | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.937). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.0, -52.9); signed map (-45.7, -41.4). **Vector** length 134, 46.6% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.82 to 12); *Mitotic Prometaphase* (reactome, mean cos +0.80 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.76 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +4.1 | +12.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | +4.0 | +13.0 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +3.6 | +5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | -0.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.0 | +1.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | +3.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.9 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -7.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -5.7 | -6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.4 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.5 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | PDZ binding kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:27,809,624-27,838,082 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TOPK, FLJ14385, Nori-3, SPK, CT84 |
| Gene groups (HGNC) | PDZ binding kinase family |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KB5](https://www.uniprot.org/uniprotkb/Q96KB5) (Lymphokine-activated killer T-cell-originated protein kinase):

> Phosphorylates MAP kinase p38. Seems to be active only in mitosis. May also play a role in the activation of lymphoid cells. When phosphorylated, forms a complex with TP53, leading to TP53 destabilization and attenuation of G2/M checkpoint during doxorubicin-induced DNA damage.

**Summary**, from NCBI Gene [55872](https://www.ncbi.nlm.nih.gov/gene/55872):

> This gene encodes a serine/threonine protein kinase related to the dual specific mitogen-activated protein kinase kinase (MAPKK) family. Evidence suggests that mitotic phosphorylation is required for its catalytic activity. The encoded protein may be involved in the activation of lymphoid cells and support testicular functions, with a suggested role in the process of spermatogenesis. Overexpression of this gene has been implicated in tumorigenesis. Alternative splicing results in multiple …

**Accessions** — [HGNC:18282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18282) · Entrez [55872](https://www.ncbi.nlm.nih.gov/gene/55872) · UniProt [Q96KB5](https://www.uniprot.org/uniprotkb/Q96KB5) · Ensembl [ENSG00000168078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168078)

## Data

Gene col 9595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9595); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9595]; `tensor/DDL_lfc|DDL_z.npy` [9595]; `embed/gene_vectors.npy` [9595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9595 or target_col == 9595). Every well: [[PBK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PBK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
