---
symbol: "ZFYVE1"
type: "gene"
col: 9197
ensembl_id: "ENSG00000165861"
name: "zinc finger FYVE-type containing 1"
location: "14q24.2"
module: 4
arm: "-"
pooled_cpm: 41.89
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 16
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ZFYVE1

*zinc finger FYVE-type containing 1* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +15.1, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.326× (z -18.7, q 0e+00, down in 34 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.699× (z -6.2, q 6e-08, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AAMDC]] (+0.70, fdr 7e-06), [[MICU1]] (+0.69, fdr 7e-06), [[SYNRG]] (+0.67, fdr 7e-06); moves opposite to [[NAA15]] (-0.77, fdr 7e-06), [[PRKDC]] (-0.69, fdr 7e-06), [[CCT5]] (-0.68, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FNBP1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +15.1 | 0e+00 | 42/48 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +12.5 | 4e-33 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +11.6 | 7e-29 | 38/48 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +8.7 | 7e-16 | 35/48 (NCI-H2030, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +8.1 | 7e-14 | 27/49 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.9 | 2e-13 | 29/48 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +7.2 | 4e-11 | 30/48 (A-427, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +6.9 | 5e-10 | 28/48 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +6.7 | 1e-09 | 31/49 (A498, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.6 | 2e-09 | 26/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.5 | 3e-09 | 26/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.9 | 2e-07 | 27/48 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +5.7 | 6e-07 | 24/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.83×** | +5.5 | 2e-06 | 29/49 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.26×** | +5.4 | 2e-06 | 26/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 2e-05 | 25/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.62×** | +4.4 | 4e-04 | 19/49 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.326×** | -18.7 | 0e+00 | 34/37 (SW 900, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.400×** | -15.9 | 0e+00 | 42/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.413×** | -14.2 | 2e-43 | 34/39 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.577×** | -9.5 | 2e-19 | 29/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.699×** | -6.2 | 6e-08 | 30/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.585×** | -4.9 | 1e-04 | 22/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.636×** | -4.1 | 0.003 | 21/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.796×** | -4.0 | 0.005 | 20/48 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.796×** | -3.9 | 0.005 | 18/49 (A498, A-172, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.663×** | -3.7 | 0.011 | 17/48 (NCI-H2347, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.817×** | -3.5 | 0.021 | 16/48 (A498, RKO, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.680×** | -3.5 | 0.021 | 15/48 (NCI-H1792, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.863× | -3.5 | 0.021 | 17/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.828×** | -3.3 | 0.043 | 14/48 (KATO III, RKO, …) | inconsistent across doses |  |
| [[Flutamide (drug)]] 5 µM |  | **0.831×** | -3.2 | 0.049 | 6/48 (A498, Panc 03.27, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.832×** | -3.2 | 0.050 | 10/48 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.839× | -3.0 | 0.080 | 7/48 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.720×** | -3.0 | 0.091 | 15/48 (CFPAC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.843× | -3.0 | 0.093 | 11/48 (NCI-H460, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.7 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.1 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.28× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -15.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 89.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -22.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 61.5 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 75.9 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -14.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 41.7 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 28.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -13.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 42.7 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -15.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 53.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.313× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 76.4 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 49.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 21.1 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 24.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.93× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 64.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.0791× (z -22.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 78.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -17.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 63.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0572× (z -24.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 32.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.326× (z -9.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 79.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.74× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 37.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -10.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 29.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0818× (z -15.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 15.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.25× (z +9.3) | — |
| [[C32 (line)]] | wt | 49.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0575× (z -21.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 45.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0771× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 35.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0881× (z -15.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 44.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0986× (z -16.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 28.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 25.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 58.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 51.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -10.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0918× (z -11.3) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -10.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.8) | — |
| [[KATO III (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0929× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.0) | — |
| [[RKO (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -13.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAMDC]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[MICU1]] | +0.69 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SYNRG]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SIRT2]] | +0.66 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[TSC22D4]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZSWIM8]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NEU1]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[YPEL3]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ABCA5]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[GABARAP]] ⚠ | +0.63 | +0.65 / +0.61 | both halves | 7e-06 | STRING 745; ⚠ in the vector space only through flagged drug-doses |
| [[NPC2]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA15]] | -0.77 | -0.75 / -0.75 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.69 | -0.69 / -0.69 | both halves | 7e-06 |  |
| [[CCT5]] | -0.68 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[ATIC]] | -0.66 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[MACROH2A1]] | -0.66 | -0.69 / -0.58 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.65 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[VWA8]] | -0.64 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[TMX3]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[TCERG1]] | -0.63 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[G3BP1]] | -0.63 | -0.63 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FNBP1]] | C | FNBP1 activity lowers ZFYVE1's level | lines that do not express FNBP1 (4) vs lines expressing it (46) | 1.02× higher at baseline in the lines without FNBP1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CITED2, WHAMMP3, RDX; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.5, -46.7); signed map (-11.0, 7.0). **Vector** length 108, 32.3% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +4.0 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +3.6 | +4.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.5 | +3.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.9 | +0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -14.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger FYVE-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:72,969,451-73,027,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DFCP1, KIAA1589, TAFF1, PPP1R172; previously ZNFN2A1 |
| Gene groups (HGNC) | Zinc fingers FYVE-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBF4](https://www.uniprot.org/uniprotkb/Q9HBF4) (Zinc finger FYVE domain-containing protein 1):

> Plays a role in the formation of lipid droplets (LDs) which are storage organelles at the center of lipid and energy homeostasis. Regulates the morphology, size and distribution of LDs. Mediates the formation of endoplasmic reticulum-lipid droplets (ER-LD) contacts by forming a complex with RAB18 and ZW10. Binds to phosphatidylinositol 3-phosphate (PtdIns3P) through FYVE-type zinc finger.; (Microbial infection) Upon SARS coronavirus-2/SARS-CoV-2 infection, mediates through binding with …

**Summary**, from NCBI Gene [53349](https://www.ncbi.nlm.nih.gov/gene/53349):

> The FYVE domain mediates the recruitment of proteins involved in membrane trafficking and cell signaling to phosphatidylinositol 3-phosphate-containing membranes. This protein contains two zinc-binding FYVE domains in tandem and is reported to localize to the Golgi apparatus. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:13180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13180) · Entrez [53349](https://www.ncbi.nlm.nih.gov/gene/53349) · UniProt [Q9HBF4](https://www.uniprot.org/uniprotkb/Q9HBF4) · Ensembl [ENSG00000165861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165861)

## Data

Gene col 9197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9197); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9197]; `tensor/DDL_lfc|DDL_z.npy` [9197]; `embed/gene_vectors.npy` [9197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9197 or target_col == 9197). Every well: [[ZFYVE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFYVE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
