---
symbol: "MAILR"
type: "gene"
col: 14796
ensembl_id: "ENSG00000253320"
name: "macrophage interferon regulatory lncRNA"
location: "8q22.3"
module: 23
arm: "+"
pooled_cpm: 18.17
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 22
n_dd_up_clean: 25
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MAILR

*macrophage interferon regulatory lncRNA* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.00× (z +40.6, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.502× (z -10.1, q 3e-21, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.580× (z -8.0, q 2e-13, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKN2-AS1]] (+0.83, fdr 6e-05), [[PPP1R12A-AS2]] (+0.83, fdr 5e-05), [[CHD1-DT]] (+0.81, fdr 1e-05); moves opposite to [[GTF2E2]] (-0.68, fdr 1e-04), [[STUB1]] (-0.67, fdr 1.00, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.00×** | +40.6 | 0e+00 | 46/46 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.57×** | +21.6 | 0e+00 | 41/45 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +20.4 | 0e+00 | 38/46 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +14.4 | 1e-44 | 37/47 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +11.0 | 3e-26 | 35/48 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +10.1 | 3e-22 | 32/47 (HOP62, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +9.8 | 9e-21 | 27/42 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.51×** | +8.6 | 5e-16 | 30/48 (NCI-H1573, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +7.5 | 4e-12 | 28/48 (C-33 A, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.4 | 6e-12 | 28/45 (BT-474, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 4e-07 | 26/48 (KATO III, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +5.3 | 4e-06 | 13/32 (LOX-IMVI, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +4.9 | 4e-05 | 17/47 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.92×** | +4.7 | 1e-04 | 14/46 (BT-474, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 19/47 (C32, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 19/46 (C-33 A, SW480, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.002 | 9/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.003 | 11/48 (NCI-H23, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14796.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.502×** | -10.1 | 3e-21 | 36/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.517×** | -9.7 | 8e-20 | 32/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.556×** | -8.3 | 2e-14 | 26/45 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -8.0 | 2e-13 | 30/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -8.0 | 2e-13 | 34/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.590×** | -7.7 | 9e-13 | 25/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -7.7 | 1e-12 | 30/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.646×** | -6.4 | 1e-08 | 24/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.412×** | -6.4 | 1e-08 | 23/45 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.671×** | -4.2 | 0.002 | 11/48 (PANC-1, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.574×** | -4.0 | 0.004 | 14/44 (H4, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.781×** | -3.6 | 0.013 | 14/48 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.770×** | -3.6 | 0.013 | 16/47 (BT-474, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.774×** | -3.4 | 0.032 | 10/48 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.798×** | -3.3 | 0.037 | 20/47 (PANC-1, SW480, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.646×** | -3.1 | 0.063 | 8/48 (PANC-1, A549, …) | two highest doses | noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.809×** | -3.1 | 0.063 | 10/48 (HOP62, A-172, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.811×** | -3.1 | 0.067 | 7/48 (SW1417, C-33 A, …) | inconsistent across doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.794×** | -3.0 | 0.070 | 7/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.810×** | -2.9 | 0.095 | 19/48 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.0 | 3 | 12 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +17.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0957× (z -23.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.165× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 44.7 | 4 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 14.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +16.5) | — |
| [[HOP62 (line)]] | alt | 23.2 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.66× (z +16.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 13.6 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +18.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 38.6 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +16.7) | [[TAK-901 (drug)]] 0.05 µM 0.160× (z -10.6) |
| [[HT-29 (line)]] | alt | 9.06 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.10× (z +14.4) | [[Silodosin (drug)]] 5 µM 0.155× (z -8.7) |
| [[J82 (line)]] | alt | 10.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +17.7) | — |
| [[LOX-IMVI (line)]] | wt | 9.72 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +16.5) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.140× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 16.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +18.5) | — |
| [[A-172 (line)]] | wt | 30.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +15.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.219× (z -10.7) ⚠ toxic |
| [[A549 (line)]] | wt | 27.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 30.8 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +11.2) | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.136× (z -10.1) |
| [[H4 (line)]] | wt | 30.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +22.4) | — |
| [[HS-578T (line)]] | alt | 27.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.49× (z +17.1) | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.15× (z +19.1) | — |
| [[RPMI-7951 (line)]] | alt | 17.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.02× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 7.44 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +17.1) | — |
| [[A498 (line)]] | wt | 31.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +14.6) | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 2 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0777× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 7.49 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +15.1) | — |
| [[COLO 205 (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 9.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 14.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +17.5) | — |
| [[LoVo (line)]] | wt | 7.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +19.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 8.52 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.29× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.128× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 8.90 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.88× (z +16.3) | — |
| [[RKO (line)]] | wt | 7.66 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.1× (z +17.0) | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 11.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +14.9) | — |
| [[SW1417 (line)]] | alt | 31.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +17.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 7.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.4× (z +16.5) | — |
| [[HepG2_C3A (line)]] | wt | 9.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.71× (z +12.9) | — |
| [[KATO III (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 5.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.10× (z +13.9) | — |
| [[SW48 (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +9.5) | — |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 22 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2-AS1]] | +0.83 | +0.86 / +0.39 | both halves | 6e-05 |  |
| [[PPP1R12A-AS2]] | +0.83 | +0.85 / +0.39 | both halves | 5e-05 |  |
| [[CHD1-DT]] | +0.81 | +0.79 / +0.49 | both halves | 1e-05 |  |
| [[ERCC6L2-AS1]] | +0.80 | +0.81 / +0.38 | both halves | 6e-05 |  |
| [[ANKRD17-DT]] | +0.80 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[THAP2]] | +0.80 | +0.81 / +0.37 | both halves | 8e-05 |  |
| [[RFX3-DT]] | +0.80 | +0.83 / +0.42 | both halves | 4e-05 |  |
| [[MFF-DT]] | +0.80 | +0.75 / +0.39 | both halves | 6e-05 |  |
| [[MAD2L1-DT]] | +0.80 | +0.82 / +0.40 | both halves | 4e-05 |  |
| [[EPM2A-DT]] | +0.79 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.79 | +0.83 / +0.25 | both halves | 4e-04 |  |
| [[SEPTIN7-DT]] | +0.79 | +0.82 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2E2]] | -0.68 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[STUB1]] | -0.67 | -0.50 / +0.00 | ⚠ one half (not replicated) | 1.00 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAILR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises MAILR's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without SOCS2-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises MAILR's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.50× lower at baseline in the lines without PLS3-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.854). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.9, 15.9); signed map (24.8, -9.7). **Vector** length 99.5, 25.2% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +40.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +20.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +21.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.4 | +10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +14.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +7.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +3.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -8.2 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.6 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -6.2 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.6 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -7.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Berbamine (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | macrophage interferon regulatory lncRNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q22.3 — chr8:102,864,271-103,002,424 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MAIL1, H22954; previously AZIN1-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51558](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51558) · Entrez [100506753](https://www.ncbi.nlm.nih.gov/gene/100506753) · Ensembl [ENSG00000253320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253320)

## Data

Gene col 14796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14796); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14796]; `tensor/DDL_lfc|DDL_z.npy` [14796]; `embed/gene_vectors.npy` [14796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14796 or target_col == 14796). Every well: [[MAILR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAILR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
