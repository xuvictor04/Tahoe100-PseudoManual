---
symbol: "ACAP2"
type: "gene"
col: 3540
ensembl_id: "ENSG00000114331"
name: "ArfGAP with coiled-coil, ankyrin repeat and PH domains 2"
location: "3q29"
module: 46
arm: "-"
pooled_cpm: 231.9
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ACAP2

*ArfGAP with coiled-coil, ankyrin repeat and PH domains 2* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.82× (z +21.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.639× (z -14.5, q 7e-45, down in 35 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SW480 0.499×, NCI-H1792 0.383×, NCI-H1573 0.490×, hTERT-HPNE 0.383×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.424×, LoVo 0.430×, HT-29 0.424×, SW480 0.591×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.433×, LS 180 0.413×, KATO III 0.453×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.589×, A-172 0.657×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.681×); [[Fenofibrate (drug)]] 0.5 µM in 1 line (SW 1088 0.170×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PWWP3A]] (+0.63, fdr 1e-05), [[GPR89B]] (+0.62, fdr 1e-05), [[DAP3]] (+0.58, fdr 2e-05); moves opposite to [[ZBED5-AS1]] (-0.61, fdr 7e-05), [[LINC00938]] (-0.61, fdr 4e-05), [[C5orf15]] (-0.60, fdr 3e-05).
> It sits in the **-** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CTSO]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +21.0 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +17.4 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +16.0 | 0e+00 | 46/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +14.6 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +13.6 | 4e-40 | 39/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +10.7 | 6e-25 | 25/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +8.3 | 1e-14 | 32/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +7.5 | 4e-12 | 27/48 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +6.7 | 1e-09 | 23/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +6.7 | 1e-09 | 30/45 (HEC-1-A, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +5.8 | 4e-07 | 32/49 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +5.4 | 3e-06 | 20/48 (LoVo, A498, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.31×** | +5.0 | 3e-05 | 25/48 (HT-29, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +4.8 | 6e-05 | 26/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.07× | +3.6 | 0.014 | 4/48 (SNU-1, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.19× | +3.2 | 0.044 | 12/49 (LoVo, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.063 | 8/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3540.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SW480 0.499×, NCI-H1792 0.383×, NCI-H1573 0.490×, hTERT-HPNE 0.383×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.424×, LoVo 0.430×, HT-29 0.424×, SW480 0.591×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.433×, LS 180 0.413×, KATO III 0.453×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.589×, A-172 0.657×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.681×); [[Fenofibrate (drug)]] 0.5 µM in 1 line (SW 1088 0.170×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.639×** | -14.5 | 7e-45 | 35/45 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.757×** | -9.3 | 3e-18 | 27/44 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.772×** | -9.1 | 3e-17 | 30/49 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.811×** | -7.3 | 3e-11 | 29/48 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -6.9 | 4e-10 | 13/48 (A-172, HOP62, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.727×** | -5.8 | 5e-07 | 24/38 (Panc 03.27, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.843× | -5.7 | 8e-07 | 21/47 (LOX-IMVI, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.896× | -5.4 | 4e-06 | 15/49 (KATO III, SW48, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -4.5 | 5e-04 | 0/50 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.859× | -3.8 | 0.008 | 16/47 (Hs 766T, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.899× | -3.5 | 0.024 | 2/48 (HEC-1-A, KATO III) | inconsistent across doses |  |
| [[Megestrol (drug)]] 5 µM |  | 0.939× | -3.1 | 0.092 | 0/49 | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.914× | -3.0 | 0.12 | 4/47 (NCI-H1573, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 322 | 8 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.94× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -21.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 230 | 7 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -14.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 289 | 7 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +25.8) | [[Dinaciclib (drug)]] 0.05 µM 0.499× (z -15.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 318 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +22.0) | [[Dinaciclib (drug)]] 0.5 µM 0.531× (z -10.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 272 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -14.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 259 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +15.1) | — |
| [[KATO III (line)]] | alt | 356 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.95× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -14.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 280 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.530× (z -11.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 210 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.89× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 163 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +15.7) | — |
| [[A-172 (line)]] | wt | 266 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.63× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.657× (z -11.3) |
| [[J82 (line)]] | alt | 278 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.526× (z -11.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 271 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.87× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -14.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 348 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.00× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.497× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 265 | 1 (1 ⚠) | 4 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.52× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.589× (z -12.8) |
| [[SW1417 (line)]] | alt | 282 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.588× (z -9.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 146 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.510× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 230 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.87× (z +11.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.612× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 171 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.81× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 153 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.552× (z -11.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 211 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 167 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +16.2) | — |
| [[HepG2_C3A (line)]] | wt | 153 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 203 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.75× (z +10.0) | [[Docetaxel (drug)]] 0.05 µM 0.572× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~24% of this change |
| [[HS-578T (line)]] | alt | 286 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.81× (z +10.8) | [[TAK-901 (drug)]] 5 µM 0.387× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 281 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.51× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.490× (z -13.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 230 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.85× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.603× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 213 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 186 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.76× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 201 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.492× (z -10.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 224 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.492× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 236 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 194 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.74× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 201 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.82× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 250 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 271 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.508× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 158 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.79× (z +9.3) | — |
| [[RKO (line)]] | wt | 246 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.85× (z +10.1) | — |
| [[SW 1088 (line)]] | alt | 219 | 0 | 1 | — | [[Fenofibrate (drug)]] 0.5 µM 0.170× (z -10.2) |
| [[C-33 A (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 174 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 189 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PWWP3A]] | +0.63 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[GPR89B]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[DAP3]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[BICD2]] | +0.58 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[LRRFIP1]] | +0.57 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[EPS15L1]] | +0.55 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[EXOC6B]] | +0.55 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[TWF2]] | +0.55 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[ERC1]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[DNAJB1]] | +0.54 | +0.40 / +0.44 | both halves | 4e-05 |  |
| [[LMBR1]] | +0.54 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[PCYT1A]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED5-AS1]] | -0.61 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[LINC00938]] | -0.61 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[C5orf15]] | -0.60 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[AHI1-DT]] | -0.57 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[TTC32]] | -0.56 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[ZKSCAN8]] | -0.56 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TAF9B]] | -0.54 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[SRSF1]] | -0.54 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[TAPBP]] | -0.53 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[UFL1-AS1]] | -0.53 | -0.42 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[LINC03015]] | -0.53 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[HNRNPH3]] | -0.52 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[ALG10B]] | -0.52 | -0.57 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSO]] | B | CTSO activity raises ACAP2's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without CTSO | 0.089 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[HDAC6]] | B | HDAC6 activity lowers ACAP2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers ACAP2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | ACAP2's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | ACAP2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.67 | 0.305 over the table, 0.034 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **-** arm (projection on the module's main direction -0.482). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.9, 18.7); signed map (-44.3, 4.8). **Vector** length 122, 37.4% of its response variance represented; |z| ≥ 3 in 1,319 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.3 | +14.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +13.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +8.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.1 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.7 | +5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -12.7 | -14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.8 | -5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -9.2 | -6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -8.7 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -1.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with coiled-coil, ankyrin repeat and PH domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:195,274,745-195,443,044 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0041, CNT-B2; previously CENTB2 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15057](https://www.uniprot.org/uniprotkb/Q15057) (Arf-GAP with coiled-coil, ANK repeat and PH domain-containing protein 2):

> GTPase-activating protein (GAP) for ADP ribosylation factor 6 (ARF6). Does not show GAP activity for RAB35.

**Summary**, from NCBI Gene [23527](https://www.ncbi.nlm.nih.gov/gene/23527):

> Enables GTPase activator activity. Acts upstream of or within actin filament-based process. Located in plasma membrane and ruffle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16469) · Entrez [23527](https://www.ncbi.nlm.nih.gov/gene/23527) · UniProt [Q15057](https://www.uniprot.org/uniprotkb/Q15057) · Ensembl [ENSG00000114331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114331)

## Data

Gene col 3540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3540); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3540]; `tensor/DDL_lfc|DDL_z.npy` [3540]; `embed/gene_vectors.npy` [3540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3540 or target_col == 3540). Every well: [[ACAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
