---
symbol: "CLIP4"
type: "gene"
col: 3654
ensembl_id: "ENSG00000115295"
name: "CAP-Gly domain containing linker protein family member 4"
location: "2p23.2"
module: 133
arm: "+"
pooled_cpm: 96.16
n_lines_expressing: 38
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# CLIP4

*CAP-Gly domain containing linker protein family member 4* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.62× (z +8.0, q 9e-13, up in 26 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.332× (z -18.1, q 0e+00, down in 34 of 36 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.527× (z -14.7, q 0e+00, down in 32 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LURAP1L-AS1]] (+0.55, fdr 3e-05), [[ANK2]] (+0.52, fdr 1e-05), [[SYNE1]] (+0.51, fdr 4e-05); moves opposite to [[TBC1D8]] (-0.47, fdr 4e-05), [[PTPN1]] (-0.46, fdr 7e-05), [[PTPN12]] (-0.45, fdr 1e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TBC1D8]] → it (grade B ⚠); 3 go from it, the strongest it → [[TRIO]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +8.0 | 9e-13 | 26/36 (A498, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.8 | 4e-09 | 21/36 (LOX-IMVI, A549, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.3 | 3e-05 | 18/36 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.9 | 1e-04 | 20/35 (C32, A-172, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +4.4 | 0.001 | 15/36 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 0.002 | 18/35 (C32, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 19/35 (PANC-1, A-172, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.20× | +4.2 | 0.002 | 16/36 (HS-578T, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.006 | 12/37 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.18× | +3.9 | 0.006 | 16/36 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.29×** | +3.7 | 0.010 | 15/38 (C32, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.011 | 13/36 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.018 | 12/37 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.018 | 17/36 (Panc 03.27, A-172, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | 1.16× | +3.5 | 0.018 | 11/37 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.019 | 16/36 (A-172, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.019 | 13/36 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.019 | 10/36 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.029 | 11/36 (HT-29, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.332×** | -18.1 | 0e+00 | 34/36 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.356×** | -16.9 | 0e+00 | 35/36 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -14.7 | 0e+00 | 32/37 (SNU-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.415×** | -14.4 | 7e-45 | 32/36 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -10.1 | 6e-22 | 30/35 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.773×** | -5.9 | 4e-07 | 17/36 (NCI-H2347, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.713×** | -5.5 | 2e-06 | 22/36 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.708×** | -5.5 | 2e-06 | 19/36 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.714×** | -5.3 | 8e-06 | 19/36 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.741×** | -4.9 | 6e-05 | 23/36 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.744×** | -4.8 | 7e-05 | 19/37 (NCI-H2347, RPMI-7951, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -4.3 | 6e-04 | 18/37 (HEC-1-A, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.780×** | -3.9 | 0.004 | 15/36 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.614×** | -3.7 | 0.010 | 13/36 (NCI-H2347, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.797×** | -3.6 | 0.014 | 17/32 (Panc 03.27, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.806×** | -3.5 | 0.016 | 15/36 (NCI-H2347, Panc 03.27, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.808×** | -3.4 | 0.021 | 14/36 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.817×** | -3.3 | 0.029 | 14/36 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.874× | -3.0 | 0.061 | 14/36 (NCI-H2347, Panc 03.27, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.750×** | -3.0 | 0.061 | 13/36 (J82, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.831×** | -3.0 | 0.061 | 11/36 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.835× | -2.9 | 0.077 | 11/36 (NCI-H2347, Panc 03.27, …) | all doses, flat |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.840× | -2.8 | 0.097 | 6/36 (SNU-1, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 295 | 0 | 13 (11 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -23.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -12.6) |
| [[HT-29 (line)]] | alt | 95.7 | 1 (1 ⚠) | 9 (8 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.36× (z +8.8) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.0907× (z -17.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 437 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -22.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -17.3) |
| [[PANC-1 (line)]] | alt | 170 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -17.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 516 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -19.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -10.9) |
| [[A-172 (line)]] | wt | 98.3 | 2 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.33× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -15.4) |
| [[C32 (line)]] | wt | 127 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 181 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 73.0 | 3 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.15× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.282× (z -11.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 310 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -14.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 251 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.0) |
| [[SNU-423 (line)]] | alt | 98.4 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -12.3) |
| [[SW1417 (line)]] | alt | 62.0 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 47.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +8.8) | [[Adagrasib (drug)]] 0.05 µM 0.658× (z -11.0) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 71.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.398× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 94.9 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -12.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.1) |
| [[SHP-77 (line)]] | alt | 64.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 86.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -8.7) |
| [[A549 (line)]] | wt | 69.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 43.3 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.13× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 69.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 59.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +21.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.97× (z +14.5) | — |
| [[NCI-H2030 (line)]] | alt | 93.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 25.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.15× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -8.6) ⚠ toxic |
| [[J82 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H596 (line)]] | alt | 73.7 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.111× (z -9.1) |
| [[SNU-1 (line)]] | wt | 70.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -20.6) |
| [[SW 1088 (line)]] | alt | 96.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0613× (z -9.7) |
| [[SW 1271 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0768× (z -11.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 5.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 94.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.24 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 23.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.79 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.42 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LURAP1L-AS1]] | +0.55 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[ANK2]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SYNE1]] | +0.51 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[ANKRD30B]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SLC7A11]] | +0.49 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[KCP]] | +0.48 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[NIBAN1]] | +0.48 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[KCNIP4]] | +0.48 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[LRMDA]] | +0.48 | +0.36 / +0.45 | both halves | 9e-05 |  |
| [[SLCO2B1]] | +0.48 | +0.38 / +0.36 | both halves | 9e-05 |  |
| [[LINC00536]] | +0.48 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[GNPDA1]] | +0.48 | +0.42 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D8]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PTPN1]] | -0.46 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[PTPN12]] | -0.45 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[FOXO1]] | -0.44 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[CLEC11A]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[RPGR]] | -0.43 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[ANPEP]] | -0.42 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[CLMP]] | -0.42 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[MLKL]] | -0.42 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[GBA2]] | -0.42 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[ANGPTL4]] | -0.41 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[SYNJ1]] | -0.41 | -0.31 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TBC1D8 activity raises CLIP4's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 2.54× lower at baseline in the lines without TBC1D8 | 0.024 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[ATP6V0D2]] | B | ATP6V0D2 activity raises CLIP4's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 3.24× lower at baseline in the lines without ATP6V0D2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIO]] | B | CLIP4 activity raises TRIO's level | lines that do not express CLIP4 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without CLIP4 | 0.073 | ⚠ within organs, on part of the lines; also absent: RTL8C, ENSG00000289526, MSN |
| cells under [[Sodium Salicylate (drug)]] 0.5 µM | B | CLIP4 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express CLIP4 (12) vs lines expressing it (36) | the lines without CLIP4: 1.19× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: RTL8C, ENSG00000289526, MSN |
| cells under [[Sodium Salicylate (drug)]] 5 µM | B | CLIP4 activity lowers the cells' numbers under Sodium Salicylate 5 µM (makes them more sensitive) | lines that do not express CLIP4 (12) vs lines expressing it (36) | the lines without CLIP4: 1.10× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: RTL8C, ENSG00000289526, MSN |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.3, 24.4); signed map (39.8, 22.8). **Vector** length 108, 28.5% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +0.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.2 | -5.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.7 | -14.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +0.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.4 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | CAP-Gly domain containing linker protein family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2 — chr2:29,097,705-29,199,777 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21069; previously RSNL2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q8N3C7](https://www.uniprot.org/uniprotkb/Q8N3C7) carries no function annotation.

**Summary**, from NCBI Gene [79745](https://www.ncbi.nlm.nih.gov/gene/79745):

> Predicted to enable microtubule plus-end binding activity. Predicted to be involved in cytoplasmic microtubule organization. Predicted to be active in cell cortex; microtubule plus-end; and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26108) · Entrez [79745](https://www.ncbi.nlm.nih.gov/gene/79745) · UniProt [Q8N3C7](https://www.uniprot.org/uniprotkb/Q8N3C7) · Ensembl [ENSG00000115295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115295)

## Data

Gene col 3654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3654); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3654]; `tensor/DDL_lfc|DDL_z.npy` [3654]; `embed/gene_vectors.npy` [3654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3654 or target_col == 3654). Every well: [[CLIP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLIP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
