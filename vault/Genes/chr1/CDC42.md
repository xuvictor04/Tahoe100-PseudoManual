---
symbol: "CDC42"
type: "gene"
col: 969
ensembl_id: "ENSG00000070831"
name: "cell division cycle 42"
location: "1p36.12"
module: 111
arm: "+"
pooled_cpm: 140.96
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# CDC42

*cell division cycle 42* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.02× (z +19.3, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.732× (z -11.7, q 7e-29, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR3]] (+0.76, fdr 7e-06), [[YWHAZ]] (+0.74, fdr 7e-06), [[GNB1]] (+0.74, fdr 7e-06); moves opposite to [[TMEM101]] (-0.70, fdr 1e-05), [[MRPL32]] (-0.67, fdr 1e-05), [[SMIM26]] (-0.66, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[ZNF593]] (-0.63, fdr 3e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.02×** | +19.3 | 0e+00 | 48/49 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +17.9 | 0e+00 | 46/49 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +14.6 | 0e+00 | 38/44 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +11.3 | 2e-27 | 43/48 (LS 180, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +11.1 | 2e-26 | 39/45 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +8.9 | 6e-17 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +7.3 | 3e-11 | 30/47 (PANC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +5.4 | 4e-06 | 24/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.4 | 7e-04 | 22/48 (NCI-H460, NCI-H2030, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.16× | +4.0 | 0.004 | 18/47 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +4.0 | 0.004 | 10/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.9 | 0.004 | 18/38 (HEC-1-A, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.040 | 16/47 (SK-MEL-2, H4, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.13× | +3.1 | 0.073 | 5/47 (SK-MEL-2, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -11.7 | 7e-29 | 36/49 (HEC-1-A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.655×** | -11.2 | 7e-27 | 40/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.664×** | -10.9 | 3e-25 | 40/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.748×** | -7.7 | 2e-12 | 37/48 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.779×** | -6.6 | 4e-09 | 30/48 (HOP62, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.773×** | -6.6 | 5e-09 | 30/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.789×** | -6.3 | 2e-08 | 29/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.789×** | -6.3 | 2e-08 | 30/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.834× | -4.8 | 1e-04 | 22/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -4.7 | 1e-04 | 19/48 (A-427, LS 180, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 0.844× | -4.5 | 3e-04 | 20/48 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.893× | -4.2 | 0.001 | 4/48 (LoVo, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.739×** | -4.2 | 0.001 | 23/49 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.848× | -4.2 | 0.001 | 24/48 (HOP62, SW 900, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.903× | -3.8 | 0.005 | 8/48 (RPMI-7951, LoVo, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.866× | -3.8 | 0.005 | 14/48 (LS 180, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.876× | -3.4 | 0.022 | 8/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.921× | -3.1 | 0.056 | 2/48 (HOP62, SW 1271) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.921× | -3.1 | 0.056 | 10/48 (J82, HOP62, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.924× | -3.0 | 0.084 | 5/48 (HOP62, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 92.4 | 7 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 116 | 5 (2 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 9.06× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.446× (z -11.6) |
| [[PANC-1 (line)]] | alt | 160 | 5 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.29× (z +15.0) | [[Panobinostat (drug)]] 5 µM 0.540× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 148 | 4 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.69× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -14.4) |
| [[A498 (line)]] | wt | 107 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 147 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.96× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.415× (z -12.3) |
| [[HOP62 (line)]] | alt | 183 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.43× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -9.1) |
| [[A-427 (line)]] | wt | 120 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.35× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.78× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 115 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.46× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -11.0) |
| [[C32 (line)]] | wt | 90.6 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 6.12× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 265 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -9.7) |
| [[HS-578T (line)]] | alt | 175 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.92× (z +9.8) | — |
| [[KATO III (line)]] | alt | 151 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.24× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.16× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.628× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 138 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.85× (z +13.0) | [[Belinostat (drug)]] 5 µM 0.499× (z -10.9) |
| [[LS 180 (line)]] | wt | 164 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.23× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 134 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.66× (z +13.7) | — |
| [[J82 (line)]] | alt | 145 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +11.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 140 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +12.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 173 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 4.44× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.548× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 142 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.29× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 171 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.57× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 86.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +14.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 232 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.32× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.7) |
| [[HT-29 (line)]] | alt | 145 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.53× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 116 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 137 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.20× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 130 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.56× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 150 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.15× (z +11.3) | — |
| [[RKO (line)]] | wt | 112 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.21× (z +13.2) | — |
| [[SNU-1 (line)]] | wt | 100 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.83× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 107 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.01× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -8.8) |
| [[BT-474 (line)]] | alt | 141 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.43× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 127 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.18× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 148 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.70× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 167 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.19× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 119 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.19× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 93.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 92.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.87× (z +8.6) | — |
| [[SW48 (line)]] | wt | 184 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -8.7) |
| [[AN3 CA (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 244 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR3]] | +0.76 | +0.68 / +0.79 | both halves | 7e-06 | pathway: EPH-Ephrin signaling; STRING 841 |
| [[YWHAZ]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 754 |
| [[GNB1]] | +0.74 | +0.66 / +0.80 | both halves | 7e-06 | pathway: G beta:gamma signalling through CDC42; STRING 782 |
| [[WDR1]] | +0.70 | +0.53 / +0.77 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 417 |
| [[MAPRE1]] | +0.68 | +0.49 / +0.74 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 417 |
| [[ARPC4]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 | pathway: EPH-Ephrin signaling; STRING 745 |
| [[SZRD1]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[CAPNS1]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[RHOA]] | +0.65 | +0.66 / +0.70 | both halves | 7e-06 | same gene group; pathway: EPH-Ephrin signaling; STRING 955 |
| [[GNG12]] | +0.65 | +0.38 / +0.79 | both halves | 6e-05 | pathway: G beta:gamma signalling through CDC42; STRING 593 |
| [[NRAS]] | +0.64 | +0.61 / +0.69 | both halves | 7e-06 | pathway: MAPK family signaling cascades |
| [[YWHAQ]] | +0.63 | +0.53 / +0.70 | both halves | 1e-05 | pathway: RHO GTPase Effectors |

## Genes that move opposite

*46 of its nearest partners move opposite, 11 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM101]] | -0.70 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[MRPL32]] | -0.67 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.66 | -0.50 / -0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF593]] | -0.63 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[NKAP]] | -0.63 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.62 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[MRPS18C]] | -0.61 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[MBD4]] | -0.60 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[RP9P]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[LSM10]] | -0.59 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[MRPL23]] | -0.59 | -0.31 / -0.65 | both halves | 2e-04 |  |
| [[CROCCP2-1]] | -0.59 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[LEO1]] | -0.57 | -0.29 / -0.70 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CDC42's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.5, -18.5); signed map (-8.7, 34.6). **Vector** length 113, 34.0% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Response of endothelial cells to shear stress* (reactome, mean cos +0.60 to 5); *RHO GTPases activate PKNs* (reactome, mean cos +0.62 to 4); *Cellular responses to mechanical stimuli* (reactome, mean cos +0.60 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.8 | +17.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.6 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.4 | +11.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.4 | +19.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +11.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -1.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -2.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.9 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -3.1 | -6.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:22,052,627-22,101,360 (+) |
| Ensembl biotype | protein_coding |
| Also known as | G25K, CDC42Hs |
| Gene groups (HGNC) | Rho family GTPases |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 65 pathways, smallest: Inactivation of CDC42 and RAC1; CD28 dependent Vav1 pathway; RHO GTPases activate KTN1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P60953](https://www.uniprot.org/uniprotkb/P60953) (Cell division control protein 42 homolog):

> Plasma membrane-associated small GTPase which cycles between an active GTP-bound and an inactive GDP-bound state. In active state binds to a variety of effector proteins to regulate cellular responses. Involved in epithelial cell polarization processes. Regulates the bipolar attachment of spindle microtubules to kinetochores before chromosome congression in metaphase. Regulates cell migration. In neurons, plays a role in the extension and maintenance of the formation of filopodia, thin and …

**Summary**, from NCBI Gene [998](https://www.ncbi.nlm.nih.gov/gene/998):

> The protein encoded by this gene is a small GTPase of the Rho-subfamily, which regulates signaling pathways that control diverse cellular functions including cell morphology, migration, endocytosis and cell cycle progression. This protein is highly similar to Saccharomyces cerevisiae Cdc 42, and is able to complement the yeast cdc42-1 mutant. The product of oncogene Dbl was reported to specifically catalyze the dissociation of GDP from this protein. This protein could regulate actin …

**Accessions** — [HGNC:1736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1736) · Entrez [998](https://www.ncbi.nlm.nih.gov/gene/998) · UniProt [P60953](https://www.uniprot.org/uniprotkb/P60953) · Ensembl [ENSG00000070831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070831)

## Data

Gene col 969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 969); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 969]; `tensor/DDL_lfc|DDL_z.npy` [969]; `embed/gene_vectors.npy` [969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 969 or target_col == 969). Every well: [[CDC42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
