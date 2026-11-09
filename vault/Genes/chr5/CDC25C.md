---
symbol: "CDC25C"
type: "gene"
col: 8156
ensembl_id: "ENSG00000158402"
name: "cell division cycle 25C"
location: "5q31.2"
module: 22
arm: "+"
pooled_cpm: 43.15
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 42
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CDC25C

*cell division cycle 25C* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +19.8, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (20 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.317× (z -16.5, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.429× (z -12.1, q 2e-31, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF2C]] (+0.88, fdr 7e-06), [[CDCA8]] (+0.86, fdr 7e-06), [[CDCA3]] (+0.84, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +19.8 | 0e+00 | 44/48 (Panc 03.27, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +7.8 | 2e-12 | 32/48 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.9 | 1e-09 | 33/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.47×** | +5.6 | 3e-06 | 24/48 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.08×** | +5.5 | 4e-06 | 31/47 (J82, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.43×** | +5.2 | 2e-05 | 26/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.41×** | +5.0 | 5e-05 | 27/48 (KATO III, C-33 A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +4.7 | 2e-04 | 23/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.82×** | +4.5 | 4e-04 | 22/48 (PANC-1, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.36×** | +4.4 | 5e-04 | 23/48 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.35×** | +4.3 | 9e-04 | 22/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.29×** | +3.7 | 0.011 | 17/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.28×** | +3.6 | 0.014 | 13/48 (HEC-1-A, A498, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.029 | 12/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.3 | 0.037 | 13/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.051 | 14/48 (SHP-77, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8156.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.317×** | -16.5 | 0e+00 | 47/48 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.429×** | -12.1 | 2e-31 | 42/48 (A-427, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.439×** | -11.8 | 9e-30 | 41/46 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.574×** | -11.2 | 4e-27 | 32/48 (A-427, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.471×** | -10.8 | 6e-25 | 37/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -9.6 | 5e-20 | 33/39 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.535×** | -8.3 | 1e-14 | 30/43 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.543×** | -8.2 | 1e-14 | 36/48 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.571×** | -7.7 | 7e-13 | 39/48 (HS-578T, A498, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.393×** | -7.0 | 1e-10 | 34/48 (SW1417, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.400×** | -6.9 | 3e-10 | 36/48 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.623×** | -6.8 | 6e-10 | 31/48 (HEC-1-A, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.625×** | -6.7 | 8e-10 | 30/48 (H4, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.634×** | -6.5 | 3e-09 | 32/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.750×** | -5.8 | 2e-07 | 26/48 (A498, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.480×** | -5.5 | 1e-06 | 29/48 (H4, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -4.9 | 3e-05 | 26/48 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.529×** | -4.8 | 5e-05 | 24/48 (HEC-1-A, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.533×** | -4.7 | 7e-05 | 25/48 (HepG2/C3A, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.721×** | -4.7 | 8e-05 | 24/48 (AN3 CA, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 5 µM |  | **0.571×** | -4.2 | 7e-04 | 24/47 (HCT15, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.745×** | -4.0 | 0.002 | 20/47 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.610×** | -3.7 | 0.005 | 18/48 (SW480, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 64.7 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0242× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 29.0 | 0 | 7 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.186× (z -13.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.246× (z -10.9) |
| [[SW480 (line)]] | alt | 43.7 | 3 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +13.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -10.8) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.371× (z -9.6) |
| [[A498 (line)]] | wt | 29.7 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.305× (z -13.6) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.342× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 54.3 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +14.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.212× (z -15.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -9.2) |
| [[HOP62 (line)]] | alt | 67.6 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.298× (z -15.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.295× (z -10.9) |
| [[A-172 (line)]] | wt | 33.1 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.334× (z -10.9) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.412× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 37.4 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -13.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 37.6 | 3 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 51.4 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.320× (z -11.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.364× (z -10.2) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0497× (z -16.9) |
| [[MIA PaCa-2 (line)]] | alt | 75.2 | 1 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -13.2) |
| [[SHP-77 (line)]] | alt | 89.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.190× (z -11.0) |
| [[A-427 (line)]] | wt | 76.0 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.200× (z -17.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.215× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 16.0 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +11.2) | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0418× (z -13.8) |
| [[C32 (line)]] | wt | 24.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +11.5) | [[AZD2858 (drug)]] 0.5 µM 0.0526× (z -11.8) ⚠ toxic |
| [[J82 (line)]] | alt | 42.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.1 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.162× (z -14.1) ⚠ cell-cycle shift, explains ~59% of this change |
| [[PANC-1 (line)]] | alt | 62.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 24.7 | 0 | 3 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.225× (z -10.2) |
| [[C-33 A (line)]] | alt | 59.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 38.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +11.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -10.4) |
| [[HCT15 (line)]] | alt | 62.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -11.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (mesylate) (drug)]] 5 µM 0.0537× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 29.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -12.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 23.8 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.19× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | — |
| [[LoVo (line)]] | wt | 31.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 20.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0841× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 53.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +16.9) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.230× (z -11.0) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 29.2 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.278× (z -9.5) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 33.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +16.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +12.7) | — |
| [[SW1417 (line)]] | alt | 59.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +13.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.256× (z -10.7) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 40.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 38.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 38.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.150× (z -8.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SNU-423 (line)]] | alt | 57.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 30.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF2C]] | +0.88 | +0.90 / +0.87 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 907 |
| [[CDCA8]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 821 |
| [[CDCA3]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 | STRING 662 |
| [[PTTG1]] | +0.83 | +0.81 / +0.84 | both halves | 7e-06 | STRING 716 |
| [[GTSE1]] | +0.82 | +0.80 / +0.84 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 721 |
| [[CDCA2]] | +0.82 | +0.81 / +0.82 | both halves | 7e-06 | same gene group; STRING 713 |
| [[SGO2]] | +0.82 | +0.83 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[KIF22]] | +0.81 | +0.78 / +0.83 | both halves | 7e-06 | STRING 576 |
| [[OIP5]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 | STRING 573 |
| [[CDK1]] | +0.81 | +0.82 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 999 |
| [[PIMREG]] | +0.80 | +0.74 / +0.84 | both halves | 7e-06 | STRING 593 |
| [[TACC3]] | +0.80 | +0.81 / +0.80 | both halves | 7e-06 | STRING 581 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CDC25C's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without PIMREG | 0.059 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CDC25C's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PTTG1]] | C | PTTG1's natural level strengthens CDC25C's drug response | PTTG1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.08; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[AURKB]] | C | AURKB activity raises CDC25C's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without AURKB | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CIT]] | C | CIT's natural level strengthens CDC25C's drug response | CIT's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.28; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PBK]] | C | PBK activity raises CDC25C's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without PBK | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.5, -56.3); signed map (-50.6, -41.0). **Vector** length 165, 59.2% of its response variance represented; |z| ≥ 3 in 1,481 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.62 to 60); *Mitotic Prometaphase* (reactome, mean cos +0.58 to 48); *E2F targets* (hallmark, mean cos +0.59 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +19.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +7.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | +5.1 | +5.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.6 | +5.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.2 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +3.0 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.8 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.5 | -16.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -9.7 | -11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.7 | -12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.1 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.0 | -6.5 |
|  | [[EX229 (drug)]] 5 µM |  | -6.8 | -7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.6 | -7.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.3 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 25C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,285,269-138,338,355 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPP1R60; previously CDC25 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Class III Cys-based CDC25 phosphatases |
| Reactome | 23 pathways, smallest: Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex; Polo-like kinase mediated events; TP53 Regulates Transcription of Genes Involved in G2 Cell Cycle Arrest |
| Matched by | ensembl_id |

**Function**, from UniProt [P30307](https://www.uniprot.org/uniprotkb/P30307) (M-phase inducer phosphatase 3):

> Functions as a dosage-dependent inducer in mitotic control. Tyrosine protein phosphatase required for progression of the cell cycle. When phosphorylated, highly effective in activating G2 cells into prophase. Directly dephosphorylates CDK1 and activates its kinase activity.

**Summary**, from NCBI Gene [995](https://www.ncbi.nlm.nih.gov/gene/995):

> This gene encodes a conserved protein that plays a key role in the regulation of cell division. The encoded protein directs dephosphorylation of cyclin B-bound CDC2 and triggers entry into mitosis. It also suppresses p53-induced growth arrest. Multiple alternatively spliced transcript variants of this gene have been described. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:1727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1727) · Entrez [995](https://www.ncbi.nlm.nih.gov/gene/995) · UniProt [P30307](https://www.uniprot.org/uniprotkb/P30307) · Ensembl [ENSG00000158402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158402)

## Data

Gene col 8156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8156); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8156]; `tensor/DDL_lfc|DDL_z.npy` [8156]; `embed/gene_vectors.npy` [8156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8156 or target_col == 8156). Every well: [[CDC25C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC25C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
