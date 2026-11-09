---
symbol: "MAGI3"
type: "gene"
col: 1302
ensembl_id: "ENSG00000081026"
name: "membrane associated guanylate kinase, WW and PDZ domain containing 3"
location: "1p13.2"
module: 1
arm: "-"
pooled_cpm: 179.71
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MAGI3

*membrane associated guanylate kinase, WW and PDZ domain containing 3* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.48× (z +11.0, q 2e-25, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.515× (z -17.8, q 0e+00, down in 33 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.757× (z -7.8, q 8e-13, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEAK1]] (+0.59, fdr 1e-05), [[MEGF9]] (+0.56, fdr 1e-05), [[SYNE2]] (+0.56, fdr 1e-05); moves opposite to [[ZNF2]] (-0.59, fdr 2e-05), [[EIF3D]] (-0.57, fdr 1e-05), [[ZNF333]] (-0.55, fdr 4e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +11.0 | 2e-25 | 30/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +10.4 | 5e-23 | 24/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +9.7 | 9e-20 | 31/47 (C-33 A, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +9.3 | 3e-18 | 28/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +9.2 | 4e-18 | 37/47 (RKO, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +9.0 | 1e-17 | 25/47 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +8.0 | 1e-13 | 27/47 (RKO, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +7.6 | 2e-12 | 29/47 (NCI-H2030, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +6.6 | 2e-09 | 26/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +6.3 | 1e-08 | 24/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +6.2 | 3e-08 | 30/48 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +6.2 | 3e-08 | 27/48 (HT-29, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.21×** | +5.2 | 9e-06 | 25/46 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +4.7 | 1e-04 | 22/49 (C32, C-33 A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.18× | +4.7 | 1e-04 | 21/47 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +4.4 | 4e-04 | 18/46 (LoVo, SW48, …) | rises with dose | low cells (technical?) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.001 | 23/47 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +4.0 | 0.002 | 16/46 (AsPC-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -17.8 | 0e+00 | 33/43 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.585×** | -15.0 | 0e+00 | 35/48 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.583×** | -13.9 | 7e-42 | 26/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.528×** | -9.3 | 2e-18 | 30/37 (HS-578T, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.751×** | -8.0 | 2e-13 | 32/47 (KATO III, SW48, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.757×** | -7.8 | 8e-13 | 32/47 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -7.5 | 6e-12 | 26/46 (HepG2/C3A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.767×** | -7.4 | 1e-11 | 25/47 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.803×** | -5.9 | 3e-07 | 26/47 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.681×** | -5.6 | 1e-06 | 25/48 (HS-578T, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.689×** | -5.4 | 3e-06 | 27/47 (HS-578T, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.834× | -5.1 | 2e-05 | 22/47 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.847× | -4.6 | 2e-04 | 22/47 (SNU-1, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.842× | -4.5 | 3e-04 | 22/46 (C32, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.737×** | -4.4 | 3e-04 | 24/47 (LoVo, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.752×** | -4.2 | 0.001 | 21/47 (LoVo, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.758×** | -4.0 | 0.002 | 25/48 (SHP-77, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.867× | -4.0 | 0.002 | 17/47 (HCT15, NCI-H23, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.920× | -3.2 | 0.043 | 2/47 (A498, H4) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.893× | -3.0 | 0.067 | 11/47 (HS-578T, SW480, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.895× | -3.0 | 0.077 | 9/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 167 | 4 (3 ⚠) | 9 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.63× (z +13.5) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.86× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -27.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.524× (z -12.3) |
| [[A-172 (line)]] | wt | 136 | 1 | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -16.8) |
| [[C32 (line)]] | wt | 72.7 | 8 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +20.1) | [[Harringtonine (drug)]] 0.05 µM 0.370× (z -8.9) |
| [[HS-578T (line)]] | alt | 190 | 0 | 9 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.200× (z -13.2) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.202× (z -13.1) |
| [[LoVo (line)]] | wt | 329 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 112 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +18.7) | — |
| [[HT-29 (line)]] | alt | 387 | 3 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -14.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 136 | 3 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -12.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.230× (z -9.2) |
| [[SW1417 (line)]] | alt | 194 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -17.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 274 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -18.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 115 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +23.0) | — |
| [[HEC-1-A (line)]] | alt | 234 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.616× (z -8.9) |
| [[LS 180 (line)]] | wt | 382 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -20.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 161 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.513× (z -10.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 235 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.73× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -13.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 179 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 195 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.515× (z -9.6) |
| [[SNU-423 (line)]] | alt | 156 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -12.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 362 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.504× (z -11.2) |
| [[J82 (line)]] | alt | 143 | 1 (1 ⚠) | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.54× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -16.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 138 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 106 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +9.2) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.457× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 143 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -12.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 504 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -20.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 134 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -17.6) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.387× (z -10.5) |
| [[SW 900 (line)]] | alt | 140 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.461× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 117 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.43× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.34× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 202 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 249 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -15.7) ⚠ toxic |
| [[HOP62 (line)]] | alt | 79.1 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.35× (z +10.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 155 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -10.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[hTERT-HPNE (line)]] | wt | 92.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 138 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.594× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 186 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[IQ 1 (drug)]] 5 µM 0.297× (z -9.2) |
| [[SW 1088 (line)]] | alt | 140 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.0692× (z -11.5) |
| [[AN3 CA (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.421× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.429× (z -10.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 87.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.3) | — |
| [[SW48 (line)]] | wt | 229 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -15.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | +0.59 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[MEGF9]] | +0.56 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SYNE2]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZNRF2]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PLEKHA5]] | +0.54 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[PDE5A]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ARL15]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[RAPGEF2]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 | same gene group; STRING 931 |
| [[PHLPP1]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[CDC42SE2]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[ATP1B1]] | +0.51 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[ADD3]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF2]] | -0.59 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[EIF3D]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ZNF333]] | -0.55 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[PES1]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ZNF202]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MTG1]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ZNF783]] ⚠ | -0.52 | -0.51 / -0.46 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DET1]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZNF561]] | -0.52 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[RRN3]] | -0.51 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[GTF2H3]] | -0.51 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[PEX10]] | -0.51 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ZNF696]] | -0.51 | -0.52 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity raises MAGI3's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.63× lower at baseline in the lines without ADD3 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[ATP1B1]] | B | ATP1B1 activity raises MAGI3's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without ATP1B1 | 0.055 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-51.8, 9.0); signed map (-15.8, 28.6). **Vector** length 128, 41.3% of its response variance represented; |z| ≥ 3 in 1,535 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +8.2 | +11.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.5 | +6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +6.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.6 | +7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.6 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +8.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +3.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.1 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.8 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.4 | -7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -17.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -6.2 | -9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated guanylate kinase, WW and PDZ domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:113,390,515-113,685,923 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAGI-3 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TCQ9](https://www.uniprot.org/uniprotkb/Q5TCQ9) (Membrane-associated guanylate kinase, WW and PDZ domain-containing protein 3):

> Acts as a scaffolding protein at cell-cell junctions, thereby regulating various cellular and signaling processes. Cooperates with PTEN to modulate the kinase activity of AKT1. Its interaction with PTPRB and tyrosine phosphorylated proteins suggests that it may link receptor tyrosine phosphatase with its substrates at the plasma membrane. In polarized epithelial cells, involved in efficient trafficking of TGFA to the cell surface. Regulates the ability of LPAR2 to activate ERK and RhoA …

**Summary**, from NCBI Gene [260425](https://www.ncbi.nlm.nih.gov/gene/260425):

> Predicted to enable GMP kinase activity. Predicted to be involved in signal transduction. Predicted to act upstream of or within positive regulation of JUN kinase activity. Located in cell junction. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29647) · Entrez [260425](https://www.ncbi.nlm.nih.gov/gene/260425) · UniProt [Q5TCQ9](https://www.uniprot.org/uniprotkb/Q5TCQ9) · Ensembl [ENSG00000081026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081026)

## Data

Gene col 1302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1302); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1302]; `tensor/DDL_lfc|DDL_z.npy` [1302]; `embed/gene_vectors.npy` [1302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1302 or target_col == 1302). Every well: [[MAGI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
