---
symbol: "KIF15"
type: "gene"
col: 8783
ensembl_id: "ENSG00000163808"
name: "kinesin family member 15"
location: "3p21.31"
module: 22
arm: "+"
pooled_cpm: 42.4
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KIF15

*kinesin family member 15* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.71× (z +9.8, q 6e-20, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~78% of this change. The strongest without an alert is [[Berbamine (drug)]] 0.05 µM: 1.24× (z +3.7, q 0.012, up in 8 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (NCI-H2030 2.53×, NCI-H2347 2.37×, HS-578T 3.20×, RKO 2.38×, …; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.546× (z -15.7, q 0e+00, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.780× (z -6.4, q 1e-08, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPG]] (+0.93, fdr 7e-06), [[NCAPH]] (+0.92, fdr 7e-06), [[KIF11]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8783.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (NCI-H2030 2.53×, NCI-H2347 2.37×, HS-578T 3.20×, RKO 2.38×, …; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.71×** | +9.8 | 6e-20 | 36/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +9.7 | 6e-20 | 31/47 (NCI-H2030, NCI-H2347, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.51×** | +7.6 | 8e-12 | 33/46 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +6.7 | 4e-09 | 26/47 (NCI-H2347, LoVo, …) | top dose only | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.27×** | +6.2 | 5e-08 | 29/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.38×** | +5.8 | 5e-07 | 28/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.35×** | +5.4 | 4e-06 | 27/47 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.31×** | +4.9 | 6e-05 | 24/46 (NCI-H2030, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.29×** | +4.7 | 2e-04 | 20/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.23×** | +3.8 | 0.007 | 19/46 (NCI-H1573, NCI-H23, …) | inconsistent across doses | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.48×** | +3.8 | 0.008 | 15/46 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.012 | 8/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.5 | 0.020 | 17/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.053 | 9/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.081 | 7/47 (C32, HT-29, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +3.0 | 0.081 | 9/47 (RKO, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.546×** | -15.7 | 0e+00 | 39/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.483×** | -12.5 | 2e-33 | 41/47 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.673×** | -6.9 | 1e-09 | 35/47 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.503×** | -6.6 | 6e-09 | 23/42 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.631×** | -6.6 | 6e-09 | 26/47 (LS 180, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.780×** | -6.4 | 1e-08 | 24/47 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.634×** | -5.9 | 2e-07 | 26/47 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.770×** | -4.8 | 1e-04 | 19/47 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.758×** | -4.8 | 1e-04 | 23/47 (H4, HCT15, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.639×** | -4.3 | 1e-03 | 21/46 (A-427, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -4.3 | 1e-03 | 23/47 (A-427, SW48, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.643×** | -4.2 | 0.001 | 21/45 (Hs 766T, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.756×** | -4.0 | 0.003 | 17/47 (MIA PaCa-2, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.813×** | -3.8 | 0.006 | 18/47 (SHP-77, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.8 | 0.007 | 24/47 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.822×** | -3.6 | 0.010 | 13/46 (RKO, A-172, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.815×** | -3.5 | 0.012 | 13/46 (NCI-H460, RKO, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.017 | 16/47 (SW48, SW480, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.834× | -3.3 | 0.023 | 15/47 (SW 900, HEC-1-A, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.881× | -3.3 | 0.027 | 8/47 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.887× | -3.1 | 0.042 | 11/47 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.042 | 10/47 (NCI-H1573, C32, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.809×** | -3.0 | 0.053 | 9/46 (LS 180, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.803×** | -2.9 | 0.085 | 9/47 (A-427, H4, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 37.8 | 0 | 8 (7 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.154× (z -15.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.310× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 38.2 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.185× (z -18.2) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.290× (z -8.9) |
| [[A-427 (line)]] | wt | 82.8 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.210× (z -21.1) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.502× (z -9.4) |
| [[H4 (line)]] | wt | 40.0 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.133× (z -14.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SK-MEL-2 (line)]] | alt | 68.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 68.5 | 0 | 4 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.187× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.248× (z -9.2) |
| [[A-172 (line)]] | wt | 38.1 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.287× (z -12.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.413× (z -9.2) |
| [[A498 (line)]] | wt | 27.4 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.328× (z -13.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 48.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 34.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.436× (z -9.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.170× (z -12.4) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A549 (line)]] | wt | 24.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 84.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.250× (z -13.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.177× (z -14.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HCT15 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.354× (z -9.2) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HEC-1-A (line)]] | alt | 88.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.204× (z -9.7) ⚠ toxic |
| [[HOP62 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.496× (z -8.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HS-578T (line)]] | alt | 31.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 71.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.392× (z -16.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 51.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 59.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 60.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPG]] | +0.93 | +0.93 / +0.92 | both halves | 7e-06 | STRING 919 |
| [[NCAPH]] | +0.92 | +0.92 / +0.93 | both halves | 7e-06 | STRING 892 |
| [[KIF11]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 983 |
| [[BUB1B]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | STRING 923 |
| [[AURKB]] | +0.91 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 858 |
| [[NDC80]] | +0.91 | +0.89 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 900 |
| [[CDK1]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 856 |
| [[PBK]] | +0.90 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 873 |
| [[SKA3]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | STRING 636 |
| [[KNL1]] | +0.89 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 619 |
| [[MKI67]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 935 |
| [[PLK4]] | +0.89 | +0.88 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 850 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises KIF15's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.54× lower at baseline in the lines without PIMREG | 0.010 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[ZNF726]] | B | ZNF726 activity raises KIF15's level | lines that do not express ZNF726 (20) vs lines expressing it (30) | 1.42× lower at baseline in the lines without ZNF726 | 0.086 | ⚠ within organs, on part of the lines; also absent: SUSD5, RNF150, BVES |
| [[PBK]] | C | PBK activity raises KIF15's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.32× lower at baseline in the lines without PBK | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises KIF15's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.11× lower at baseline in the lines without NDC80 | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises KIF15's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.95× lower at baseline in the lines without AURKB | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises KIF15's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 3.41× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[FAM72D]] | C | FAM72D activity raises KIF15's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises KIF15's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.25× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises KIF15's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.63× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.906). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.3, -53.4); signed map (-47.2, -43.8). **Vector** length 150, 49.7% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.78 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.70 to 48); *E2F targets* (hallmark, mean cos +0.70 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.3 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +9.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | +4.0 | +4.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +3.2 | +3.8 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +3.1 | +3.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.4 | +3.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +1.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.2 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -9.7 | -15.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -8.8 | -12.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | -6.3 | -6.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | -5.7 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -4.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.3 | -6.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:44,761,721-44,873,376 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HKLP2, NY-BR-62; previously KNSL7 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 13 pathways, smallest: Kinesins; Processing of antigen in germinal center B cells; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS87](https://www.uniprot.org/uniprotkb/Q9NS87) (Kinesin-like protein KIF15):

> Plus-end directed kinesin-like motor enzyme involved in mitotic spindle assembly.

**Summary**, from NCBI Gene [56992](https://www.ncbi.nlm.nih.gov/gene/56992):

> Predicted to enable ATP hydrolysis activity; microtubule binding activity; and plus-end-directed microtubule motor activity. Predicted to be involved in centrosome separation; microtubule-based movement; and mitotic spindle assembly. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17273) · Entrez [56992](https://www.ncbi.nlm.nih.gov/gene/56992) · UniProt [Q9NS87](https://www.uniprot.org/uniprotkb/Q9NS87) · Ensembl [ENSG00000163808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163808)

## Data

Gene col 8783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8783); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8783]; `tensor/DDL_lfc|DDL_z.npy` [8783]; `embed/gene_vectors.npy` [8783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8783 or target_col == 8783). Every well: [[KIF15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
