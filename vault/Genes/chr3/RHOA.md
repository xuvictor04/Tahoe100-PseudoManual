---
symbol: "RHOA"
type: "gene"
col: 863
ensembl_id: "ENSG00000067560"
name: "ras homolog family member A"
location: "3p21.31"
module: 111
arm: "+"
pooled_cpm: 240.2
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# RHOA

*ras homolog family member A* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +23.1, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.89× (z +14.8, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.724× (z -11.0, q 3e-25, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42]] (+0.65, fdr 7e-06), [[CDC42BPB]] (+0.65, fdr 7e-06), [[CAPZB]] (+0.63, fdr 7e-06); moves opposite to [[PBDC1]] (-0.60, fdr 1e-05), [[KIAA1586]] (-0.58, fdr 1e-05), [[ZNF330]] (-0.55, fdr 4e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HHEX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +23.1 | 0e+00 | 47/49 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +21.5 | 0e+00 | 41/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +14.9 | 0e+00 | 43/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.89×** | +14.8 | 0e+00 | 47/47 (RPMI-7951, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.80×** | +14.1 | 6e-43 | 45/47 (SHP-77, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +10.3 | 4e-23 | 45/49 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **1.36×** | +7.3 | 2e-11 | 37/48 (HEC-1-A, SHP-77, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +7.2 | 3e-11 | 29/48 (HCT15, SHP-77, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +6.1 | 8e-08 | 26/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.27×** | +5.8 | 4e-07 | 34/48 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.9 | 5e-05 | 25/48 (LS 180, SW480, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.9 | 5e-05 | 20/49 (CFPAC-1, C-33 A, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.8 | 6e-05 | 24/38 (A-172, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.22×** | +4.7 | 8e-05 | 25/48 (HCT15, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.23×** | +4.7 | 1e-04 | 24/47 (C-33 A, HCT15, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 1e-04 | 25/49 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.42×** | +4.4 | 4e-04 | 29/48 (hTERT-HPNE, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Malotilate (drug)]] 0.5 µM |  | 1.20× | +4.3 | 4e-04 | 20/48 (A498, SNU-423, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +4.2 | 7e-04 | 24/48 (SW48, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.16× | +4.1 | 0.001 | 21/49 (NCI-H460, HOP62, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.724×** | -11.0 | 3e-25 | 36/48 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.736×** | -7.4 | 5e-11 | 40/48 (NCI-H2347, J82, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.755×** | -6.5 | 1e-08 | 32/47 (SNU-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.849× | -5.6 | 4e-06 | 22/48 (C-33 A, SW 900, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.796×** | -5.3 | 1e-05 | 29/48 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.818×** | -4.8 | 1e-04 | 24/48 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.832×** | -4.4 | 8e-04 | 24/48 (LoVo, HCT15, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.835× | -4.3 | 0.001 | 22/48 (J82, NCI-H1792, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.716×** | -4.2 | 0.002 | 27/47 (SNU-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.888× | -4.0 | 0.003 | 12/48 (A-427, SNU-1, …) | rises with dose |  |
| [[SBI-0640756 (drug)]] 5 µM |  | **0.735×** | -3.9 | 0.006 | 27/48 (SW480, C-33 A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.906× | -3.4 | 0.036 | 8/48 (A549, J82, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.875× | -3.2 | 0.057 | 13/48 (HCT15, HOP62, …) | rises with dose |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.912× | -3.1 | 0.070 | 1/48 (COLO 205) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 321 | 8 (4 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.82× (z +13.5) | — |
| [[SW480 (line)]] | alt | 219 | 7 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +22.7) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.03× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -13.9) |
| [[A-172 (line)]] | wt | 246 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 2.25× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 265 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +18.0) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 2.46× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -12.0) |
| [[LS 180 (line)]] | wt | 254 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 2.39× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.651× (z -9.1) |
| [[PANC-1 (line)]] | alt | 158 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +23.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.47× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 550 | 3 | 4 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.95× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.362× (z -14.0) ⚠ toxic · without an alert: [[NG25 (drug)]] 5 µM 0.238× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 287 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.84× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 240 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.70× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -11.3) |
| [[LoVo (line)]] | wt | 268 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.92× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.73× (z +9.4) | [[Harringtonine (drug)]] 5 µM 0.489× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 226 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.42× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 255 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 2.31× (z +11.5) | — |
| [[J82 (line)]] | alt | 303 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 1.89× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 207 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 2.33× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 188 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +16.1) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 2.00× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 244 | 5 (3 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.34× (z +16.3) | — |
| [[A549 (line)]] | wt | 231 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +19.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 320 | 4 (2 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.22× (z +11.6) | — |
| [[H4 (line)]] | wt | 145 | 4 (2 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.48× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 259 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 2.26× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 161 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +17.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -12.9) |
| [[KATO III (line)]] | alt | 188 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +20.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 199 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 2.07× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 338 | 2 | 2 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.32× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -16.7) |
| [[RKO (line)]] | wt | 282 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.16× (z +10.0) | — |
| [[A-427 (line)]] | wt | 301 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.79× (z +9.6) | — |
| [[A498 (line)]] | wt | 165 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +18.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 312 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 1.80× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 186 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 159 | 3 (1 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.49× (z +15.3) | — |
| [[SK-MEL-2 (line)]] | alt | 358 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.82× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 207 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 191 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.02× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 239 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +14.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 225 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 4.38× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 252 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -13.0) |
| [[C32 (line)]] | wt | 227 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 477 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +11.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 200 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +15.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 167 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +10.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 288 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 173 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 157 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42]] | +0.65 | +0.66 / +0.70 | both halves | 7e-06 | same gene group; pathway: EPH-Ephrin signaling; STRING 955 |
| [[CDC42BPB]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | STRING 561 |
| [[CAPZB]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[IQGAP1]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 | pathway: RHO GTPase Effectors; STRING 880 |
| [[L1CAM]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[CHP1]] | +0.61 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[MAP4]] | +0.60 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ADD1]] | +0.60 | +0.62 / +0.61 | both halves | 7e-06 | STRING 440 |
| [[TMOD3]] | +0.60 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SLC25A39]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[STX2]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[RSU1]] | +0.59 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBDC1]] | -0.60 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[KIAA1586]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ZNF330]] | -0.55 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[ZNF503]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MRPS18C]] | -0.54 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[AASDH]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[THUMPD2]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CWC22]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[IL27RA]] | -0.54 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[MRPL46]] | -0.54 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[RPAP1]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HHEX]] | B | HHEX activity raises RHOA's level | lines that do not express HHEX (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without HHEX | 0.060 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL |
| [[VAT1]] | C | VAT1 activity strengthens RHOA's drug response | lines that do not express VAT1 (3) vs lines expressing it (46) | the lines without VAT1 respond 0.57× as strongly (z diff +1.43); strongest at Dinaciclib 5 µM: 0.94x vs 2.43x (z diff +8.4) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: SH2B3, C12orf75, SKAP2; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.5, 10.3); signed map (-10.8, 35.3). **Vector** length 142, 46.5% of its response variance represented; |z| ≥ 3 in 1,616 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHO GTPases activate PAKs* (reactome, mean cos +0.53 to 4); *RHO GTPases activate IQGAPs* (reactome, mean cos +0.56 to 4); *RHOV GTPase cycle* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +9.2 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.7 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +21.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +23.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +7.8 | +14.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +6.1 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.7 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.4 | +4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.2 | +7.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.1 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.6 | -5.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.9 | -2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,359,139-49,412,998 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Rho12, RHOH12; previously ARH12, ARHA |
| Gene groups (HGNC) | Rho family GTPases |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 57 pathways, smallest: Axonal growth stimulation; SLIT2:ROBO1 increases RHOA activity; Axonal growth inhibition (RHOA activation) |
| Matched by | ensembl_id |

**Function**, from UniProt [P61586](https://www.uniprot.org/uniprotkb/P61586) (Transforming protein RhoA):

> Small GTPase which cycles between an active GTP-bound and an inactive GDP-bound state. Mainly associated with cytoskeleton organization, in active state binds to a variety of effector proteins to regulate cellular responses such as cytoskeletal dynamics, cell migration and cell cycle. Regulates a signal transduction pathway linking plasma membrane receptors to the assembly of focal adhesions and actin stress fibers. Involved in a microtubule-dependent signal that is required for the myosin …

**Summary**, from NCBI Gene [387](https://www.ncbi.nlm.nih.gov/gene/387):

> This gene encodes a member of the Rho family of small GTPases, which cycle between inactive GDP-bound and active GTP-bound states and function as molecular switches in signal transduction cascades. Rho proteins promote reorganization of the actin cytoskeleton and regulate cell shape, attachment, and motility. Overexpression of this gene is associated with tumor cell proliferation and metastasis. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:667) · Entrez [387](https://www.ncbi.nlm.nih.gov/gene/387) · UniProt [P61586](https://www.uniprot.org/uniprotkb/P61586) · Ensembl [ENSG00000067560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067560)

## Data

Gene col 863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 863); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 863]; `tensor/DDL_lfc|DDL_z.npy` [863]; `embed/gene_vectors.npy` [863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 863 or target_col == 863). Every well: [[RHOA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
