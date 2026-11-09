---
symbol: "MAP3K1"
type: "gene"
col: 1733
ensembl_id: "ENSG00000095015"
name: "mitogen-activated protein kinase kinase kinase 1"
location: "5q11.2"
module: 217
arm: "+"
pooled_cpm: 66.53
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# MAP3K1

*mitogen-activated protein kinase kinase kinase 1* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.53× (z +20.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.421× (z -19.5, q 0e+00, down in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.585× (z -12.1, q 2e-31, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3R1]] (+0.64, fdr 7e-06), [[ZNF608]] (+0.62, fdr 1e-05), [[LCOR]] (+0.59, fdr 1e-05); moves opposite to [[GTPBP2]] (-0.60, fdr 1e-05), [[SAMD4B]] (-0.56, fdr 3e-05), [[KLC1]] (-0.56, fdr 1e-05).
> It is in [[Module 217]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CGN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.53×** | +20.2 | 0e+00 | 44/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +17.0 | 0e+00 | 37/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +11.1 | 3e-26 | 35/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +9.1 | 2e-17 | 34/49 (BT-474, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +6.5 | 7e-09 | 25/49 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.7 | 1e-06 | 24/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +5.4 | 5e-06 | 23/48 (LS 180, HT-29, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.0 | 5e-05 | 15/48 (KATO III, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +4.9 | 5e-05 | 23/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +4.5 | 3e-04 | 18/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +4.1 | 0.002 | 14/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.20× | +4.1 | 0.002 | 18/48 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.20× | +4.0 | 0.002 | 18/48 (KATO III, LS 180, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.002 | 17/48 (BT-474, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.9 | 0.003 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.007 | 8/48 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.017 | 10/48 (HS-578T, AsPC-1, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.026 | 9/48 (HepG2/C3A, AN3 CA, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.3 | 0.029 | 9/48 (CFPAC-1, KATO III, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 1.16× | +3.3 | 0.031 | 11/48 (SW 900, HS-578T, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.039 | 8/50 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.072 | 7/48 (SW480, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.076 | 7/48 (LoVo, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.421×** | -19.5 | 0e+00 | 40/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.415×** | -19.1 | 0e+00 | 34/40 (AN3 CA, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.585×** | -12.1 | 2e-31 | 39/48 (SW480, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.570×** | -11.7 | 2e-29 | 35/43 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.753×** | -6.1 | 9e-08 | 28/47 (C32, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.833×** | -5.8 | 6e-07 | 23/49 (C32, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.778×** | -5.6 | 1e-06 | 27/47 (C32, HT-29, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.780×** | -5.6 | 2e-06 | 27/47 (C32, A498, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.710×** | -5.5 | 2e-06 | 23/48 (HT-29, Panc 03.27, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.793×** | -5.2 | 9e-06 | 23/48 (Panc 03.27, SW480, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.731×** | -5.0 | 2e-05 | 22/47 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.804×** | -4.9 | 4e-05 | 21/48 (C32, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.810×** | -4.7 | 9e-05 | 20/48 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.825×** | -4.3 | 6e-04 | 20/48 (Panc 03.27, C32, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.840× | -3.8 | 0.006 | 20/47 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.859× | -3.4 | 0.021 | 12/49 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.025 | 18/46 (SNU-1, AN3 CA, …) | two highest doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.854× | -3.3 | 0.030 | 11/48 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Pimitespib (drug)]] 5 µM |  | **0.782×** | -2.9 | 0.093 | 10/47 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.784×** | -2.9 | 0.096 | 8/48 (HEC-1-A, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 117 | 2 | 7 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 4.35× (z +12.9) | [[Auranofin (drug)]] 5 µM 0.238× (z -13.1) |
| [[A498 (line)]] | wt | 61.5 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +20.6) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.424× (z -8.8) |
| [[CHP-212 (line)]] | wt | 456 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 5 µM 0.299× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 133 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.455× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 184 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.323× (z -12.6) |
| [[LS 180 (line)]] | wt | 81.9 | 4 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.80× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 107 | 2 | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.69× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -18.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 97.9 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.326× (z -16.2) |
| [[BT-474 (line)]] | alt | 116 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 78.6 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.432× (z -9.5) |
| [[KATO III (line)]] | alt | 53.3 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -16.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 37.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -11.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 45.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -8.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 158 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -14.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 97.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.282× (z -11.9) |
| [[J82 (line)]] | alt | 67.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -13.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 64.3 | 3 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.52× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -14.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 46.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 83.1 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 70.2 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.63× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -12.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0688× (z -16.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 39.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 54.8 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.40× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 24.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.7) ⚠ cell-cycle shift, explains ~9% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 76.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 60.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -13.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 99.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.409× (z -10.4) |
| [[A-427 (line)]] | wt | 49.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.95× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -17.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 27.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +13.9) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[NCI-H596 (line)]] | alt | 71.6 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.383× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 37.4 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0719× (z -8.6) |
| [[RKO (line)]] | wt | 29.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.5) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[SNU-1 (line)]] | wt | 36.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.1) | — |
| [[SW 1271 (line)]] | alt | 49.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0703× (z -8.9) |
| [[C-33 A (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3R1]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | pathway: Fc epsilon receptor (FCERI) signaling; STRING 472 |
| [[ZNF608]] | +0.62 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[LCOR]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[KCTD3]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CDC14A]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 | STRING 416 |
| [[HMG20A]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[MTFP1]] | +0.57 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[YAP1]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 | STRING 407 |
| [[SPRY1]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[BCOR]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[IKBKE]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 | pathway: DDX58/IFIH1-mediated induction of interferon-alpha/beta |
| [[TGFBR2]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTPBP2]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[SAMD4B]] | -0.56 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[KLC1]] | -0.56 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[CHFR]] | -0.55 | -0.45 / -0.61 | both halves | 3e-05 | same gene group |
| [[TPD52L2]] | -0.55 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[YKT6]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[TANGO2]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ADCY7]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[GOLGA3]] | -0.53 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[DIP2A]] | -0.52 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[RBM44]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SZT2]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGN]] | B | CGN activity raises MAP3K1's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without CGN | 0.019 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[SHROOM3]] | B | SHROOM3 activity raises MAP3K1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without SHROOM3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.5, 15.1); signed map (44.6, -1.6). **Vector** length 114, 30.9% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.4 | +20.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +11.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.7 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +17.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.0 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +2.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.9 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.9 | -12.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.5 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -11.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -5.4 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.0 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:56,815,549-56,896,152 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MEKK, MAPKKK1; previously MEKK1 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers SWIM-type; Mitogen-activated protein kinase kinase kinases; STE11 kinase family; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | KRAS_SIGNALING_UP, HYPOXIA |
| Reactome | 18 pathways, smallest: TRAF6 mediated NF-kB activation; FCERI mediated MAPK activation; DDX58/IFIH1-mediated induction of interferon-alpha/beta |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13233](https://www.uniprot.org/uniprotkb/Q13233) (Mitogen-activated protein kinase kinase kinase 1):

> Component of a protein kinase signal transduction cascade. Activates the ERK and JNK kinase pathways by phosphorylation of MAP2K1 and MAP2K4. May phosphorylate the MAPK8/JNK1 kinase. Activates CHUK and IKBKB, the central protein kinases of the NF-kappa-B pathway.

**Summary**, from NCBI Gene [4214](https://www.ncbi.nlm.nih.gov/gene/4214):

> The protein encoded by this gene is a serine/threonine kinase and is part of some signal transduction cascades, including the ERK and JNK kinase pathways as well as the NF-kappa-B pathway. The encoded protein is activated by autophosphorylation and requires magnesium as a cofactor in phosphorylating other proteins. This protein has E3 ligase activity conferred by a plant homeodomain (PHD) in its N-terminus and phospho-kinase activity conferred by a kinase domain in its C-terminus. [provided by …

**Accessions** — [HGNC:6848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6848) · Entrez [4214](https://www.ncbi.nlm.nih.gov/gene/4214) · UniProt [Q13233](https://www.uniprot.org/uniprotkb/Q13233) · Ensembl [ENSG00000095015](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095015)

## Data

Gene col 1733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1733); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1733]; `tensor/DDL_lfc|DDL_z.npy` [1733]; `embed/gene_vectors.npy` [1733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1733 or target_col == 1733). Every well: [[MAP3K1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
