---
symbol: "NPTN"
type: "gene"
col: 8002
ensembl_id: "ENSG00000156642"
name: "neuroplastin"
location: "15q24.1"
module: 11
arm: "-"
pooled_cpm: 168.4
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NPTN

*neuroplastin* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.91× (z +19.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.608× (z -8.8, q 7e-16, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.780× (z -4.4, q 0.001, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.249×, NCI-H2347 0.360×, CFPAC-1 0.310×, AsPC-1 0.328×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.374×, SW1417 0.376×, LS 180 0.431×, SW480 0.439×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.266×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.468×); [[Sonidegib (drug)]] 5 µM in 1 line (RPMI-7951 0.257×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TWSG1]] (+0.68, fdr 7e-06), [[GM2A]] (+0.64, fdr 3e-05), [[RAB8B]] (+0.64, fdr 1e-05); moves opposite to [[DNAJC11]] (-0.69, fdr 1e-05), [[NOL8]] (-0.66, fdr 7e-06), [[PSMD7]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.91×** | +19.6 | 0e+00 | 48/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +15.3 | 0e+00 | 47/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.88×** | +11.5 | 1e-28 | 45/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +9.7 | 6e-20 | 41/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +9.1 | 8e-18 | 34/48 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +8.5 | 2e-15 | 40/48 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +7.2 | 5e-11 | 35/48 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +6.5 | 7e-09 | 39/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +6.3 | 2e-08 | 33/48 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +6.2 | 3e-08 | 39/49 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.5 | 2e-06 | 32/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.8 | 6e-05 | 29/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.8 | 6e-05 | 24/48 (KATO III, SW48, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +4.5 | 2e-04 | 28/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.002 | 30/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.005 | 28/48 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.007 | 25/49 (HOP62, CFPAC-1, …) | rises with dose | plate-row cell shift |
| [[Tadalafil (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.012 | 25/48 (RKO, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8002.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.249×, NCI-H2347 0.360×, CFPAC-1 0.310×, AsPC-1 0.328×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.374×, SW1417 0.376×, LS 180 0.431×, SW480 0.439×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.266×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.468×); [[Sonidegib (drug)]] 5 µM in 1 line (RPMI-7951 0.257×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -8.8 | 7e-16 | 36/44 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -6.0 | 7e-07 | 28/47 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.744×** | -5.5 | 9e-06 | 32/49 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.780×** | -4.4 | 0.001 | 27/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -4.1 | 0.006 | 16/48 (H4, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.812×** | -3.9 | 0.011 | 23/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -3.2 | 0.096 | 18/48 (LS 180, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.831× | -3.1 | 0.12 | 19/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.848× | -3.1 | 0.13 | 16/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.0 | 0.13 | 20/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.850× | -3.0 | 0.14 | 22/48 (NCI-H1792, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 107 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.61× (z +26.8) | — |
| [[PANC-1 (line)]] | alt | 105 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.37× (z +24.0) | — |
| [[KATO III (line)]] | alt | 113 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.29× (z +28.0) | — |
| [[SW480 (line)]] | alt | 158 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.84× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -16.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 156 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +16.3) | — |
| [[H4 (line)]] | wt | 218 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 91.4 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 208 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +14.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.447× (z -9.3) ⚠ toxic |
| [[HT-29 (line)]] | alt | 135 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +15.1) | — |
| [[LoVo (line)]] | wt | 216 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.499× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 271 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 210 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.266× (z -13.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 346 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 123 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 248 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 245 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 71.1 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.48× (z +10.2) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 175 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +16.2) | — |
| [[J82 (line)]] | alt | 97.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 194 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 234 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 312 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -13.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 129 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 288 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Sonidegib (drug)]] 5 µM 0.257× (z -8.6) |
| [[C-33 A (line)]] | alt | 121 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 330 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 119 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.485× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 196 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +11.6) | — |
| [[HS-578T (line)]] | alt | 130 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.57× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 184 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 116 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +13.1) | — |
| [[SW48 (line)]] | wt | 159 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +10.3) | — |
| [[A498 (line)]] | wt | 98.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 212 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 153 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 171 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 135 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +8.9) | — |
| [[A-172 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 168 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 152 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*24 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TWSG1]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[GM2A]] | +0.64 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[RAB8B]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[NXPH4]] | +0.63 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ELL3]] | +0.63 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[HDAC3]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[FHIP1A]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.61 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[PPP1R2]] | +0.60 | +0.66 / +0.39 | both halves | 5e-05 |  |
| [[IGSF3]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ARSA]] | +0.59 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[IGSF8]] | +0.59 | +0.61 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*76 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | -0.69 | -0.76 / -0.51 | both halves | 1e-05 |  |
| [[NOL8]] | -0.66 | -0.72 / -0.59 | both halves | 7e-06 |  |
| [[PSMD7]] | -0.65 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[NME6]] | -0.64 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[INTS14]] | -0.64 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[RPP38]] | -0.64 | -0.74 / -0.50 | both halves | 1e-05 |  |
| [[ABRAXAS2]] | -0.62 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CBLL1]] | -0.62 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[MTG2]] | -0.61 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[ICE2]] | -0.61 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.61 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[DNTTIP2]] | -0.61 | -0.70 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity raises NPTN's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.33× lower at baseline in the lines without IRF6 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MICE]] | B | MICE activity raises NPTN's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without MICE | 0.019 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[TTYH2]] | B | TTYH2 activity lowers NPTN's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 1.29× higher at baseline in the lines without TTYH2 | 0.085 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |
| [[SH3D21]] | C | SH3D21 activity raises NPTN's level | lines that do not express SH3D21 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without SH3D21 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000286677; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.6, 0.9); signed map (-30.8, 22.0). **Vector** length 93.9, 31.2% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.3 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.3 | -0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.7 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | neuroplastin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:73,560,014-73,634,134 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR1, GP55, GP65, np65, np55; previously SDFR1 |
| Gene groups (HGNC) | I-set domain containing; Basigin family |
| Reactome | 4 pathways, smallest: GABA receptor activation; Neurotransmitter receptors and postsynaptic signal transmission; Transmission across Chemical Synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y639](https://www.uniprot.org/uniprotkb/Q9Y639) (Neuroplastin):

> Accessory subunit of plasma membrane calcium-transporting ATPase ATP2B2/PMCA2 that stabilizes the transporter at the cell surface (By similarity). Also acts as a chaperone for ATP2B1; stabilizes ATP2B1 and increases its ATPase activity. Probable homophilic and heterophilic cell adhesion molecule involved in long term potentiation at hippocampal excitatory synapses through activation of p38MAPK (By similarity). May also regulate neurite outgrowth by activating the FGFR1 signaling pathway (By …

**Summary**, from NCBI Gene [27020](https://www.ncbi.nlm.nih.gov/gene/27020):

> This gene encodes a type I transmembrane protein belonging to the Ig superfamily. The protein is believed to be involved in cell-cell interactions or cell-substrate interactions. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2009]

**Accessions** — [HGNC:17867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17867) · Entrez [27020](https://www.ncbi.nlm.nih.gov/gene/27020) · UniProt [Q9Y639](https://www.uniprot.org/uniprotkb/Q9Y639) · Ensembl [ENSG00000156642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156642)

## Data

Gene col 8002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8002); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8002]; `tensor/DDL_lfc|DDL_z.npy` [8002]; `embed/gene_vectors.npy` [8002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8002 or target_col == 8002). Every well: [[NPTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
