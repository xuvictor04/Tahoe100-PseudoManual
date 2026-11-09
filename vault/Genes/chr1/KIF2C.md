---
symbol: "KIF2C"
type: "gene"
col: 6667
ensembl_id: "ENSG00000142945"
name: "kinesin family member 2C"
location: "1p34.1"
module: 22
arm: "+"
pooled_cpm: 62.73
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 35
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KIF2C

*kinesin family member 2C* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.69× (z +7.2, q 3e-10, up in 31 of 46 measured lines) ⚠ cell-cycle shift, would explain all of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (Panc 03.27 4.21×, RKO 3.40×, NCI-H2347 2.53×, SW1417 2.33×, …; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 2.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (18 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.452× (z -15.5, q 0e+00, down in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.487× (z -9.9, q 6e-21, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA8]] (+0.95, fdr 7e-06), [[GTSE1]] (+0.94, fdr 7e-06), [[CDK1]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6667.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (Panc 03.27 4.21×, RKO 3.40×, NCI-H2347 2.53×, SW1417 2.33×, …; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 2.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.69×** | +7.2 | 3e-10 | 31/46 (KATO III, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.60×** | +6.5 | 2e-08 | 33/46 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.53×** | +5.6 | 3e-06 | 25/46 (Panc 03.27, A-172, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +5.6 | 3e-06 | 25/46 (Panc 03.27, RKO, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **2.10×** | +5.4 | 1e-05 | 31/45 (J82, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +4.9 | 9e-05 | 26/46 (NCI-H23, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.42×** | +4.8 | 1e-04 | 24/45 (HT-29, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.40×** | +4.6 | 3e-04 | 31/46 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.78×** | +4.2 | 0.002 | 21/46 (HT-29, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.9 | 0.005 | 27/46 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +3.9 | 0.005 | 26/46 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.6 | 0.015 | 21/45 (NCI-H23, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.19× | +3.5 | 0.024 | 17/46 (HT-29, J82, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.1 | 0.075 | 16/46 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.10 | 11/46 (HT-29, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6667.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.452×** | -15.5 | 0e+00 | 41/46 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.404×** | -12.5 | 2e-33 | 44/46 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.487×** | -9.9 | 6e-21 | 36/46 (SW480, Panc 03.27, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.497×** | -9.1 | 1e-17 | 34/46 (LOX-IMVI, KATO III, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.568×** | -7.8 | 7e-13 | 31/46 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.360×** | -7.4 | 2e-11 | 34/43 (HEC-1-A, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.623×** | -6.5 | 5e-09 | 38/46 (SNU-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.631×** | -6.4 | 1e-08 | 31/46 (A-172, SW48, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.745×** | -5.8 | 5e-07 | 28/46 (H4, A-427, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.683×** | -5.3 | 8e-06 | 25/45 (H4, LS 180, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.783×** | -4.8 | 1e-04 | 25/46 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.699×** | -4.7 | 1e-04 | 28/46 (NCI-H1573, A498, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.789×** | -4.6 | 2e-04 | 23/46 (A498, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.744×** | -4.1 | 0.002 | 23/46 (A498, A-427, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.745×** | -4.1 | 0.002 | 24/46 (SNU-1, HEC-1-A, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.748×** | -4.0 | 0.002 | 24/46 (H4, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.818×** | -3.8 | 0.004 | 19/46 (A-427, SNU-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -3.3 | 0.021 | 18/46 (CHP-212, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.788×** | -3.3 | 0.023 | 15/46 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.635×** | -3.3 | 0.023 | 13/45 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.644×** | -3.2 | 0.030 | 19/46 (A498, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.644×** | -3.2 | 0.030 | 19/45 (HOP62, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.785×** | -3.2 | 0.031 | 10/46 (A-427, CHP-212, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.799×** | -3.1 | 0.036 | 14/46 (HOP62, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +1.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 119 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0392× (z -18.3) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.111× (z -17.5) |
| [[A-172 (line)]] | wt | 43.3 | 0 | 7 (6 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.201× (z -12.9) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.386× (z -10.8) |
| [[A498 (line)]] | wt | 71.7 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.105× (z -27.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.343× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 44.3 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.131× (z -17.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.177× (z -10.4) |
| [[A549 (line)]] | wt | 38.1 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.220× (z -14.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.266× (z -9.0) |
| [[C32 (line)]] | wt | 59.4 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.330× (z -9.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.258× (z -8.5) |
| [[LS 180 (line)]] | wt | 39.4 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.106× (z -18.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.342× (z -9.0) |
| [[A-427 (line)]] | wt | 128 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.114× (z -24.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.233× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 66.7 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.265× (z -13.4) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.394× (z -9.4) |
| [[HOP62 (line)]] | alt | 105 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.385× (z -12.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.405× (z -8.5) |
| [[LoVo (line)]] | wt | 41.4 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.354× (z -12.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.442× (z -9.5) |
| [[HCT15 (line)]] | alt | 96.2 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.305× (z -11.4) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.266× (z -9.0) |
| [[KATO III (line)]] | alt | 45.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.93× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.255× (z -10.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[MIA PaCa-2 (line)]] | alt | 88.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 93.4 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.447× (z -9.3) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.321× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -14.0) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 35.1 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.241× (z -14.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[Panc 03.27 (line)]] | alt | 55.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +15.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.220× (z -16.7) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -9.9) |
| [[SW48 (line)]] | wt | 66.1 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.119× (z -12.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.266× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 38.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0674× (z -19.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H2347 (line)]] | alt | 65.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.360× (z -8.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[RKO (line)]] | wt | 55.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.252× (z -9.7) |
| [[SW480 (line)]] | alt | 66.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -10.6) |
| [[AN3 CA (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -14.2) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.271× (z -13.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[Hs 766T (line)]] | wt | 56.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.355× (z -9.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HS-578T (line)]] | alt | 69.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.294× (z -12.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[J82 (line)]] | alt | 78.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.304× (z -11.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[PANC-1 (line)]] | alt | 76.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 73.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.212× (z -9.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW1417 (line)]] | alt | 42.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA8]] | +0.95 | +0.95 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 977 |
| [[GTSE1]] | +0.94 | +0.92 / +0.93 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 754 |
| [[CDK1]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 972 |
| [[NDC80]] | +0.92 | +0.90 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 934 |
| [[TACC3]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 825 |
| [[DEPDC1B]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | STRING 654 |
| [[DLGAP5]] | +0.91 | +0.92 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 975 |
| [[AURKB]] | +0.91 | +0.92 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 996 |
| [[KIF18A]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 954 |
| [[TOP2A]] | +0.91 | +0.92 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 937 |
| [[TPX2]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[TROAP]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 833 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises KIF2C's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without PIMREG | 0.034 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises KIF2C's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without NEURL1B | 0.079 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NDC80]] | C | NDC80 activity raises KIF2C's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.70× lower at baseline in the lines without NDC80 | 0.024 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[MYLK2]] | C | MYLK2 activity raises KIF2C's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 3.42× lower at baseline in the lines without MYLK2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[AURKB]] | C | AURKB activity raises KIF2C's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.62× lower at baseline in the lines without AURKB | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises KIF2C's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.05× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; co-absent genes |
| [[PBK]] | C | PBK activity raises KIF2C's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.57× lower at baseline in the lines without PBK | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[C21orf58]] | C | C21orf58 activity raises KIF2C's level | lines that do not express C21orf58 (3) vs lines expressing it (47) | 3.13× lower at baseline in the lines without C21orf58 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.944). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.6, -55.9); signed map (-49.5, -42.3). **Vector** length 165, 62.8% of its response variance represented; |z| ≥ 3 in 1,490 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M Transition* (reactome, mean cos +0.73 to 28); *Mitotic G2-G2/M phases* (reactome, mean cos +0.73 to 28); *Cyclin A/B1/B2 associated events during G2/M transition* (reactome, mean cos +0.79 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +6.0 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +5.6 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +4.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +4.8 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.3 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.6 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -10.0 | -15.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -9.5 | -12.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | -8.8 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.8 | -9.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -7.9 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.8 | -4.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,739,818-44,767,767 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCAK, CT139; previously KNSL6 |
| Gene groups (HGNC) | Kinesins; Small nucleolar RNA protein coding host genes |
| Hallmark sets | SPERMATOGENESIS, G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 30 pathways, smallest: Kinesins; Processing of antigen in germinal center B cells; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99661](https://www.uniprot.org/uniprotkb/Q99661) (Kinesin-like protein KIF2C):

> In complex with KIF18B, constitutes the major microtubule plus-end depolymerizing activity in mitotic cells. Regulates the turnover of microtubules at the kinetochore and functions in chromosome segregation during mitosis. Plays a role in chromosome congression and is required for the lateral to end-on conversion of the chromosome-microtubule attachment.

**Summary**, from NCBI Gene [11004](https://www.ncbi.nlm.nih.gov/gene/11004):

> This gene encodes a kinesin-like protein that functions as a microtubule-dependent molecular motor. The encoded protein can depolymerize microtubules at the plus end, thereby promoting mitotic chromosome segregation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:6393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6393) · Entrez [11004](https://www.ncbi.nlm.nih.gov/gene/11004) · UniProt [Q99661](https://www.uniprot.org/uniprotkb/Q99661) · Ensembl [ENSG00000142945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142945)

## Data

Gene col 6667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6667); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6667]; `tensor/DDL_lfc|DDL_z.npy` [6667]; `embed/gene_vectors.npy` [6667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6667 or target_col == 6667). Every well: [[KIF2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
