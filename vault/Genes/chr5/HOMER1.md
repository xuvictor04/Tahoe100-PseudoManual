---
symbol: "HOMER1"
type: "gene"
col: 7624
ensembl_id: "ENSG00000152413"
name: "homer scaffold protein 1"
location: "5q14.1"
module: 101
arm: "+"
pooled_cpm: 84.17
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 27
n_dd_up_clean: 14
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# HOMER1

*homer scaffold protein 1* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.61× (z +36.1, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 0.745× (z -7.0, q 1e-09, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R14B-AS1]] (+0.63, fdr 1e-05), [[PHLDA2]] (+0.62, fdr 1e-05), [[LUCAT1]] (+0.62, fdr 1e-05); moves opposite to [[NUDT21]] (-0.61, fdr 1e-05), [[TMEM185A]] (-0.60, fdr 1e-05), [[RAB4A]] (-0.60, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.61×** | +36.1 | 0e+00 | 43/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +19.1 | 0e+00 | 39/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.64×** | +15.6 | 0e+00 | 39/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.84×** | +15.4 | 0e+00 | 41/47 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.41×** | +14.7 | 0e+00 | 44/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.04×** | +11.9 | 2e-30 | 41/47 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.88×** | +10.1 | 3e-22 | 35/47 (SW480, J82, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +9.6 | 6e-20 | 37/47 (HCT15, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.0 | 7e-14 | 33/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.4 | 6e-12 | 32/47 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.53×** | +7.1 | 9e-11 | 31/47 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.47×** | +6.4 | 6e-09 | 31/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 7e-08 | 30/47 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.45×** | +6.0 | 8e-08 | 30/49 (SW480, LS 180, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.93×** | +4.2 | 1e-03 | 15/47 (NCI-H2347, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.023 | 14/47 (LOX-IMVI, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.027 | 15/46 (A549, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.039 | 15/47 (LoVo, HCT15, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.039 | 14/47 (LoVo, HepG2/C3A, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.64×** | +3.2 | 0.040 | 13/47 (HEC-1-A, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.074 | 18/47 (H4, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7624.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.745×** | -7.0 | 1e-09 | 34/47 (NCI-H23, CHP-212, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.672×** | -6.9 | 1e-09 | 35/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.595×** | -6.6 | 7e-09 | 33/49 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.763×** | -6.4 | 2e-08 | 34/47 (C32, SHP-77, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.687×** | -6.3 | 4e-08 | 33/47 (NCI-H23, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.668×** | -6.2 | 4e-08 | 26/44 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.729×** | -5.3 | 1e-05 | 25/48 (C32, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.743×** | -5.0 | 5e-05 | 23/46 (H4, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.753×** | -4.6 | 2e-04 | 22/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.489×** | -4.6 | 3e-04 | 31/46 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -4.4 | 5e-04 | 23/43 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.504×** | -4.4 | 5e-04 | 25/49 (AsPC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.758×** | -4.4 | 5e-04 | 25/47 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.830×** | -4.3 | 6e-04 | 20/47 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.786×** | -4.0 | 0.002 | 21/47 (LoVo, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.768×** | -3.8 | 0.006 | 20/48 (SW480, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.814×** | -3.5 | 0.016 | 20/46 (AsPC-1, SW48, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.804×** | -3.4 | 0.019 | 20/46 (SW480, SW48, …) | all doses, flat |  |
| [[MK-3903 (drug)]] 5 µM |  | **0.595×** | -3.3 | 0.022 | 14/47 (SHP-77, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.823×** | -3.3 | 0.028 | 14/47 (NCI-H23, HS-578T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 90.0 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +46.6) | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 51.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +27.5) | — |
| [[SW480 (line)]] | alt | 87.2 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +26.2) | — |
| [[C32 (line)]] | wt | 243 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.0981× (z -21.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 132 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +30.0) | [[Adagrasib (drug)]] 0.05 µM 0.507× (z -16.7) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 81.3 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +26.4) | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 64.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +18.0) | — |
| [[HOP62 (line)]] | alt | 97.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +28.5) | — |
| [[NCI-H1573 (line)]] | alt | 207 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +23.0) | — |
| [[LOX-IMVI (line)]] | wt | 74.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +21.7) | — |
| [[NCI-H2347 (line)]] | alt | 98.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +29.1) | — |
| [[PANC-1 (line)]] | alt | 78.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +19.6) | — |
| [[A-427 (line)]] | wt | 122 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +16.8) | — |
| [[CFPAC-1 (line)]] | alt | 52.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +29.8) | — |
| [[HCT15 (line)]] | alt | 96.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +20.5) | — |
| [[HT-29 (line)]] | alt | 71.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 138 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +24.0) | [[Adagrasib (drug)]] 0.05 µM 0.574× (z -13.4) ⚠ position not correctable · without an alert: [[Radotinib (drug)]] 5 µM 0.427× (z -8.8) |
| [[RKO (line)]] | wt | 65.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -10.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 66.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.23× (z +23.9) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -13.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +13.4) | — |
| [[A549 (line)]] | wt | 44.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +14.0) | — |
| [[C-33 A (line)]] | alt | 219 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -11.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 112 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.00× (z +11.6) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.40× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 26.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +24.1) | — |
| [[J82 (line)]] | alt | 53.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +20.3) | — |
| [[LoVo (line)]] | wt | 96.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +21.5) | — |
| [[RPMI-7951 (line)]] | alt | 49.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +19.6) | — |
| [[SW 900 (line)]] | alt | 96.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +26.7) | — |
| [[SW48 (line)]] | wt | 140 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 57.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.7× (z +19.2) | — |
| [[HS-578T (line)]] | alt | 66.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 50.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 95.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 47.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 53.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.41× (z +13.9) | — |
| [[SNU-1 (line)]] | wt | 72.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +21.6) | — |
| [[AN3 CA (line)]] | alt | 47.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +15.3) | — |
| [[BT-474 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.88× (z +12.3) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 63.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 65.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +20.2) | — |
| [[SW 1271 (line)]] | alt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 43.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.95× (z +8.7) ⚠ unreliable plate only | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R14B-AS1]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PHLDA2]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SOWAHC]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[NIPAL1]] | +0.62 | +0.64 / +0.57 | both halves | 8e-06 |  |
| [[KCTD5]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PITPNC1]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[EGR3]] | +0.60 | +0.63 / +0.63 | both halves | 7e-06 | STRING 447 |
| [[ALG13]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.59 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[MCL1]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GPATCH2L]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT21]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TMEM185A]] | -0.60 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[RAB4A]] | -0.60 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[TNRC6A]] | -0.58 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ACSF2]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[USP30]] | -0.57 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[GUSBP2-1]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[COPS7B]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SNX4]] | -0.56 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[CDADC1]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[HSF2]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CRYZL1]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HOMER1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises HOMER1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.0, -4.2); signed map (0.1, 32.1). **Vector** length 130, 41.4% of its response variance represented; |z| ≥ 3 in 1,420 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.6 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +19.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +15.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.9 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.0 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -8.0 | -6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.0 | -6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -7.0 | -7.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -5.9 | -3.6 |
|  | [[NG25 (drug)]] 5 µM |  | -5.4 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -6.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | homer scaffold protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:79,372,636-79,514,134 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ves-1, SYN47, HOMER-1B |
| Gene groups (HGNC) | Homer scaffold proteins |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YM7](https://www.uniprot.org/uniprotkb/Q86YM7) (Homer protein homolog 1):

> Postsynaptic density scaffolding protein. Binds and cross-links cytoplasmic regions of GRM1, GRM5, ITPR1, DNM3, RYR1, RYR2, SHANK1 and SHANK3. By physically linking GRM1 and GRM5 with ER-associated ITPR1 receptors, it aids the coupling of surface receptors to intracellular calcium release. May also couple GRM1 to PI3 kinase through its interaction with AGAP2. Isoform 1 regulates the trafficking and surface expression of GRM5. Isoform 3 acts as a natural dominant negative, in dynamic competition …

**Summary**, from NCBI Gene [9456](https://www.ncbi.nlm.nih.gov/gene/9456):

> This gene encodes a member of the homer family of dendritic proteins. Members of this family regulate group 1 metabotrophic glutamate receptor function. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17512) · Entrez [9456](https://www.ncbi.nlm.nih.gov/gene/9456) · UniProt [Q86YM7](https://www.uniprot.org/uniprotkb/Q86YM7) · Ensembl [ENSG00000152413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152413)

## Data

Gene col 7624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7624); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7624]; `tensor/DDL_lfc|DDL_z.npy` [7624]; `embed/gene_vectors.npy` [7624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7624 or target_col == 7624). Every well: [[HOMER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOMER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
