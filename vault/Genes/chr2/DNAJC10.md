---
symbol: "DNAJC10"
type: "gene"
col: 1178
ensembl_id: "ENSG00000077232"
name: "DnaJ heat shock protein family (Hsp40) member C10"
location: "2q32.1"
module: 20
arm: "+"
pooled_cpm: 103.33
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DNAJC10

*DnaJ heat shock protein family (Hsp40) member C10* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +26.4, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.34× (z +7.0, q 2e-10, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.720× (z -7.9, q 1e-12, down in 30 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.731× (z -7.1, q 3e-10, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGGT1]] (+0.68, fdr 7e-06), [[SSX2IP]] (+0.66, fdr 7e-06), [[TXNDC5]] (+0.63, fdr 1e-05); moves opposite to [[MRPL32]] (-0.63, fdr 5e-05), [[IP6K2]] (-0.62, fdr 2e-05), [[CCDC142]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +26.4 | 0e+00 | 46/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +24.8 | 0e+00 | 43/44 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +17.1 | 0e+00 | 43/45 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.45×** | +9.0 | 5e-17 | 35/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.37×** | +7.6 | 2e-12 | 37/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +7.0 | 2e-10 | 28/48 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +6.8 | 1e-09 | 34/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.33×** | +6.7 | 2e-09 | 27/47 (SW480, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.31×** | +6.5 | 4e-09 | 32/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.29×** | +5.8 | 3e-07 | 27/48 (SW480, Hs 766T, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +5.3 | 7e-06 | 31/48 (NCI-H1792, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.22×** | +4.8 | 9e-05 | 22/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +4.3 | 7e-04 | 21/49 (AsPC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.001 | 24/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.9 | 0.003 | 7/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.025 | 16/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.025 | 12/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.2 | 0.041 | 10/48 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.082 | 18/48 (SW1417, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.082 | 15/48 (NCI-H1792, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1178.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -7.9 | 1e-12 | 30/48 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.731×** | -7.1 | 3e-10 | 34/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -7.0 | 5e-10 | 28/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.805×** | -5.2 | 2e-05 | 24/48 (LoVo, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.762×** | -4.7 | 3e-04 | 22/48 (H4, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.711×** | -4.3 | 0.002 | 22/49 (A498, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.808×** | -4.3 | 0.002 | 23/48 (SHP-77, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.889× | -4.0 | 0.004 | 13/48 (A498, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.857× | -3.7 | 0.012 | 20/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.7 | 0.013 | 19/48 (HT-29, SNU-1, …) | two highest doses | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.834× | -3.6 | 0.014 | 15/48 (SW 1271, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.017 | 18/48 (A498, Panc 03.27, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.903× | -3.5 | 0.023 | 10/48 (NCI-H2030, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.3 | 0.034 | 21/48 (SNU-1, BT-474, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.910× | -3.2 | 0.047 | 8/48 (C32, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.839× | -3.0 | 0.091 | 11/49 (PANC-1, A498, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 59.0 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.87× (z +18.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 2.44× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 57.0 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.93× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 82.4 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +21.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 175 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.82× (z +16.2) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.560× (z -13.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[AsPC-1 (line)]] | alt | 37.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.06× (z +13.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 140 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +17.7) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.580× (z -9.4) |
| [[HS-578T (line)]] | alt | 151 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -10.7) ⚠ cell-cycle shift, explains ~95% of this change |
| [[J82 (line)]] | alt | 129 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +13.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.440× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 77.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +13.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 108 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +11.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +14.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 145 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +13.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 63.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +14.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 114 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +11.1) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.131× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[HEC-1-A (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 133 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 95.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +17.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 48.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +16.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 81.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +18.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +12.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 83.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 121 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +13.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.511× (z -8.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 73.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +12.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.417× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 118 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +16.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 69.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +14.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 70.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +13.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.401× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 92.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +14.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 99.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +15.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 149 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.9) ⚠ cell-cycle shift, explains ~95% of this change |
| [[NCI-H460 (line)]] | wt | 140 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +18.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 82.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 73.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +12.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 94.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +12.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 47.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.19× (z +14.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 95.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +11.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.436× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 89.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +10.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGGT1]] | +0.68 | +0.58 / +0.72 | both halves | 7e-06 | STRING 728 |
| [[SSX2IP]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.63 | +0.49 / +0.65 | both halves | 1e-05 | same gene group; STRING 477 |
| [[ELMOD2]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TMED7]] | +0.61 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[PUS7L]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SSR1]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[UCHL5]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ZDHHC21]] | +0.58 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[IPO5]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SPCS3]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 | pathway: Dengue Virus Genome Translation and Replication |
| [[AIFM1]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL32]] | -0.63 | -0.40 / -0.68 | both halves | 5e-05 |  |
| [[IP6K2]] | -0.62 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[CCDC142]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[UXT]] | -0.59 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[BSDC1]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | -0.58 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[NGDN]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[EAPP]] | -0.57 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[NDUFA13]] ⚠ | -0.57 | -0.50 / -0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCC3]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[VPS39-DT]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[MRPS36]] ⚠ | -0.56 | -0.47 / -0.55 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM27]] | -0.55 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[DNLZ]] | -0.54 | -0.40 / -0.60 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises DNAJC10's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.3, -35.6); signed map (-18.0, -43.9). **Vector** length 134, 41.6% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +26.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +24.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +17.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +5.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.9 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.1 | -7.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.9 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.6 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -3.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -4.8 | -4.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -4.3 | -3.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -4.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:182,716,255-182,794,464 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERdj5, PDIA19 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; Protein disulfide isomerases; Oxidoreductases |
| Reactome | 4 pathways, smallest: Maturation of DENV proteins; Dengue Virus Genome Translation and Replication; Dengue Virus Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXB1](https://www.uniprot.org/uniprotkb/Q8IXB1) (Endoplasmic reticulum disulfide reductase DNAJC10):

> Endoplasmic reticulum disulfide reductase that collaborates directly with the chaperone BIP/HSPA5 (GRP78) to maintain protein quality control by facilitating either the correct folding or the targeted degradation of misfolded proteins. Essential for efficient maturation of newly synthesized polypeptides in the endoplasmic reticulum, binds to substrate proteins and specifically catalyzes the reduction and removal of improper (non-native) disulfide bonds during the folding process. In endoplasmic …

**Summary**, from NCBI Gene [54431](https://www.ncbi.nlm.nih.gov/gene/54431):

> This gene encodes an endoplasmic reticulum co-chaperone which is part of the endoplasmic reticulum-associated degradation complex involved in recognizing and degrading misfolded proteins. The encoded protein reduces incorrect disulfide bonds in misfolded glycoproteins. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:24637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24637) · Entrez [54431](https://www.ncbi.nlm.nih.gov/gene/54431) · UniProt [Q8IXB1](https://www.uniprot.org/uniprotkb/Q8IXB1) · Ensembl [ENSG00000077232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077232)

## Data

Gene col 1178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1178); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1178]; `tensor/DDL_lfc|DDL_z.npy` [1178]; `embed/gene_vectors.npy` [1178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1178 or target_col == 1178). Every well: [[DNAJC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
