---
symbol: "MTPN"
type: "gene"
col: 2684
ensembl_id: "ENSG00000105887"
name: "myotrophin"
location: "7q33"
module: 42
arm: "+"
pooled_cpm: 176.5
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# MTPN

*myotrophin* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +18.0, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.26× (z +12.6, q 4e-34, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.792× (z -7.0, q 2e-09, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.467×, J82 0.488×, LoVo 0.618×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.438×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB5C]] (+0.67, fdr 7e-06), [[PPHLN1]] (+0.64, fdr 7e-06), [[TMBIM6]] (+0.64, fdr 1e-05); moves opposite to [[NFYB]] (-0.57, fdr 1e-05), [[RELB]] (-0.56, fdr 2e-05), [[CEBPD]] (-0.56, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.38×** | +18.0 | 0e+00 | 48/49 (PANC-1, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +17.7 | 0e+00 | 44/45 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.06×** | +14.5 | 4e-45 | 42/44 (PANC-1, A549, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.26×** | +12.6 | 4e-34 | 48/49 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +10.4 | 2e-23 | 44/48 (C32, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.57×** | +9.4 | 6e-19 | 48/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +9.3 | 1e-18 | 42/48 (HT-29, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +9.2 | 3e-18 | 44/48 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.53×** | +8.8 | 1e-16 | 46/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +7.7 | 7e-13 | 42/48 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +7.0 | 2e-10 | 32/49 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +6.8 | 4e-10 | 33/38 (C32, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.36×** | +6.4 | 8e-09 | 35/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.9 | 1e-07 | 37/48 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +5.9 | 1e-07 | 37/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 2e-05 | 40/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.001 | 26/48 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.004 | 29/47 (PANC-1, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.012 | 24/48 (HEC-1-A, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.016 | 11/48 (SW1417, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.034 | 22/49 (A498, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.034 | 13/48 (A-427, HCT15, …) | inconsistent across doses |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.042 | 22/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2684.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.467×, J82 0.488×, LoVo 0.618×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.438×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.792×** | -7.0 | 2e-09 | 27/48 (A-427, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.770×** | -5.3 | 3e-05 | 31/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.819×** | -3.5 | 0.095 | 24/50 (AsPC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 173 | 10 (7 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.91× (z +16.3) | — |
| [[NCI-H460 (line)]] | wt | 130 | 9 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.29× (z +20.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 187 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 251 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.56× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.17× (z +10.3) | — |
| [[C32 (line)]] | wt | 539 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.44× (z +12.8) | — |
| [[LoVo (line)]] | wt | 131 | 5 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.10× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -9.4) |
| [[PANC-1 (line)]] | alt | 190 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.30× (z +17.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.88× (z +8.7) | — |
| [[A498 (line)]] | wt | 245 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 159 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.05× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 153 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.37× (z +14.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 95.9 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.20× (z +9.7) | — |
| [[A-427 (line)]] | wt | 173 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -15.3) |
| [[Hs 766T (line)]] | wt | 240 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.66× (z +8.5) | — |
| [[J82 (line)]] | alt | 164 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 145 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.67× (z +9.6) | — |
| [[RKO (line)]] | wt | 245 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.10× (z +14.9) | — |
| [[SNU-423 (line)]] | alt | 148 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.18× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +8.9) | — |
| [[SW48 (line)]] | wt | 159 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.75× (z +9.6) | — |
| [[A-172 (line)]] | wt | 147 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.90× (z +12.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 135 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.71× (z +17.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 260 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[C-33 A (line)]] | alt | 117 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.21× (z +12.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 168 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.84× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 122 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.14× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 140 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 201 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 178 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 125 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.18× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 160 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.30× (z +13.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 120 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.77× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 161 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 222 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.08× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.75× (z +11.7) | — |
| [[H4 (line)]] | wt | 208 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.74× (z +9.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 176 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.85× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 166 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 146 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.72× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 275 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 146 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.00× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 153 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.44× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 161 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 190 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +9.7) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[AN3 CA (line)]] | alt | 190 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5C]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[PPHLN1]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TMBIM6]] | +0.64 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[CAP1]] | +0.63 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PSMB7]] | +0.62 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[EIF3H]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GDAP2]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TMED4]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[AP2B1]] | +0.57 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[TM9SF2]] | +0.56 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[STRAP]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[VDAC2]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFYB]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[RELB]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CEBPD]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[PIM3]] | -0.56 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[WDR75]] | -0.56 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TRMT10B]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[DECR2]] | -0.56 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[REPIN1]] | -0.55 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TMEM265]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CLK4]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[UPF3B]] | -0.53 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[TMEM42]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.8, -12.0); signed map (-52.4, -7.4). **Vector** length 108, 40.1% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +12.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +5.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.3 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -12.3 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.9 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.2 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.8 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | myotrophin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:135,926,760-135,977,359 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MYOTROPHIN, GCDP, V-1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P58546](https://www.uniprot.org/uniprotkb/P58546) (Myotrophin):

> Promotes dimerization of NF-kappa-B subunits and regulates NF-kappa-B transcription factor activity (By similarity). Plays a role in the regulation of the growth of actin filaments. Inhibits the activity of the F-actin-capping protein complex formed by the CAPZA1 and CAPZB heterodimer. Promotes growth of cardiomyocytes, but not cardiomyocyte proliferation. Promotes cardiac muscle hypertrophy.

**Summary**, from NCBI Gene [136319](https://www.ncbi.nlm.nih.gov/gene/136319):

> The transcript produced from this gene is bi-cistronic and can encode both myotrophin and leucine zipper protein 6. The myotrophin protein is associated with cardiac hypertrophy, where it is involved in the conversion of NFkappa B p50-p65 heterodimers to p50-p50 and p65-p65 homodimers. This protein also has a potential function in cerebellar morphogenesis, and it may be involved in the differentiation of cerebellar neurons, particularly of granule cells. A cryptic ORF at the 3' end of this …

**Accessions** — [HGNC:15667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15667) · Entrez [136319](https://www.ncbi.nlm.nih.gov/gene/136319) · UniProt [P58546](https://www.uniprot.org/uniprotkb/P58546) · Ensembl [ENSG00000105887](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105887)

## Data

Gene col 2684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2684); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2684]; `tensor/DDL_lfc|DDL_z.npy` [2684]; `embed/gene_vectors.npy` [2684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2684 or target_col == 2684). Every well: [[MTPN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTPN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
