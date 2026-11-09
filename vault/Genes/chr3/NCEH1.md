---
symbol: "NCEH1"
type: "gene"
col: 6948
ensembl_id: "ENSG00000144959"
name: "neutral cholesterol ester hydrolase 1"
location: "3q26.31"
module: 120
arm: "+"
pooled_cpm: 198.25
n_lines_expressing: 44
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# NCEH1

*neutral cholesterol ester hydrolase 1* — 3q26.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.12× (z +6.5, q 4e-08, up in 29 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (HS-578T 8.15×, A498 4.13×, CFPAC-1 3.48×, SNU-423 4.59×, …; ⚠ cell-cycle shift, explains ~79% of this change); [[TAK-901 (drug)]] 5 µM in 5 lines (CFPAC-1 5.64×, Panc 03.27 5.06×, SNU-423 7.30×, J82 4.59×, …); [[Harringtonine (drug)]] 5 µM in 3 lines (HS-578T 5.65×, A498 3.49×, NCI-H1792 3.80×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 2.27×).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.554× (z -9.8, q 9e-20, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENC1]] (+0.62, fdr 7e-06), [[NFE2L3]] (+0.61, fdr 9e-06), [[SEMA3A]] (+0.60, fdr 9e-06); moves opposite to [[UBE2Q2]] (-0.51, fdr 3e-05), [[ALDH2]] (-0.51, fdr 3e-05), [[SNX3]] (-0.51, fdr 2e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CLDN1]] → it (grade B ⚠); 6 go from it, the strongest it → [[SOX9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6948.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (HS-578T 8.15×, A498 4.13×, CFPAC-1 3.48×, SNU-423 4.59×, …; ⚠ cell-cycle shift, explains ~79% of this change); [[TAK-901 (drug)]] 5 µM in 5 lines (CFPAC-1 5.64×, Panc 03.27 5.06×, SNU-423 7.30×, J82 4.59×, …); [[Harringtonine (drug)]] 5 µM in 3 lines (HS-578T 5.65×, A498 3.49×, NCI-H1792 3.80×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 2.27×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +6.5 | 4e-08 | 29/43 (CFPAC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.49×** | +6.3 | 8e-08 | 23/42 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.30×** | +6.1 | 2e-07 | 23/42 (HS-578T, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.42×** | +5.8 | 8e-07 | 21/43 (HOP62, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +4.9 | 1e-04 | 21/42 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +4.3 | 0.002 | 22/42 (A498, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.28×** | +4.1 | 0.003 | 19/42 (RKO, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.28×** | +4.0 | 0.004 | 20/42 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.9 | 0.007 | 18/42 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.25×** | +3.7 | 0.010 | 19/42 (HOP62, SNU-423, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.016 | 22/42 (NCI-H1573, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.23×** | +3.4 | 0.038 | 18/42 (BT-474, KATO III, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.20×** | +3.1 | 0.092 | 18/41 (HOP62, MIA PaCa-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.20× | +3.0 | 0.10 | 18/42 (KATO III, SNU-1, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | 1.21× | +3.0 | 0.10 | 12/42 (RKO, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.554×** | -9.8 | 9e-20 | 35/42 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.566×** | -9.4 | 1e-18 | 32/42 (Panc 03.27, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.566×** | -8.9 | 1e-16 | 34/42 (SW48, A498, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.647×** | -7.2 | 8e-11 | 33/42 (NCI-H460, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -6.1 | 9e-08 | 31/42 (SNU-1, SW48, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.752×** | -4.5 | 5e-04 | 22/41 (NCI-H460, SW48, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.762×** | -4.5 | 6e-04 | 20/41 (SW48, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.765×** | -4.4 | 6e-04 | 24/42 (A498, Panc 03.27, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.765×** | -4.4 | 6e-04 | 26/42 (A498, Hs 766T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.772×** | -4.3 | 0.001 | 23/42 (SW48, NCI-H2030, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.779×** | -4.1 | 0.002 | 24/42 (A498, SW 1088, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.638×** | -3.9 | 0.005 | 20/42 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.850× | -3.8 | 0.006 | 19/42 (Panc 03.27, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.645×** | -3.8 | 0.006 | 20/40 (A498, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.794×** | -3.6 | 0.012 | 19/44 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.863× | -3.5 | 0.019 | 11/42 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.814×** | -3.4 | 0.022 | 20/42 (A498, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.822×** | -3.2 | 0.035 | 22/42 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.688×** | -3.2 | 0.035 | 22/42 (NCI-H2030, SNU-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 272 | 4 (4 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +21.5) ⚠ cell-cycle shift, explains ~79% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.304× (z -12.9) |
| [[SW480 (line)]] | alt | 365 | 0 | 10 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.216× (z -15.4) |
| [[SW48 (line)]] | wt | 518 | 0 | 9 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.104× (z -15.1) |
| [[NCI-H2030 (line)]] | alt | 349 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.251× (z -13.4) |
| [[SNU-1 (line)]] | wt | 465 | 4 (3 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.80× (z +11.2) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.27× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[BT-474 (line)]] | alt | 87.7 | 5 (4 ⚠) | 1 | [[Digitoxin (drug)]] 0.5 µM 2.86× (z +9.4) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.66× (z +8.9) | [[Auranofin (drug)]] 5 µM 0.340× (z -9.6) |
| [[HOP62 (line)]] | alt | 97.3 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +17.9) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[CFPAC-1 (line)]] | alt | 214 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +19.8) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.64× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 79.5 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +16.8) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[NCI-H460 (line)]] | wt | 139 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -15.5) |
| [[SNU-423 (line)]] | alt | 84.7 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +19.6) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.30× (z +9.4) | — |
| [[J82 (line)]] | alt | 153 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.4) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.59× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.454× (z -9.3) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 200 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.1) ⚠ cell-cycle shift, explains ~79% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -15.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.300× (z -9.8) |
| [[HS-578T (line)]] | alt | 94.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +26.2) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[HT-29 (line)]] | alt | 307 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.277× (z -9.7) |
| [[KATO III (line)]] | alt | 284 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.95× (z +12.4) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[NCI-H2347 (line)]] | alt | 181 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | [[Auranofin (drug)]] 5 µM 0.439× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 544 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.2) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.06× (z +9.9) | [[Auranofin (drug)]] 5 µM 0.177× (z -20.2) |
| [[RKO (line)]] | wt | 56.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.8) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[SW1417 (line)]] | alt | 755 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -18.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.258× (z -11.6) |
| [[A-172 (line)]] | wt | 77.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.4) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[HEC-1-A (line)]] | alt | 254 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.428× (z -10.5) |
| [[Hs 766T (line)]] | wt | 259 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.5) ⚠ cell-cycle shift, explains ~79% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.411× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 286 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.230× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 85.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.8) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[A-427 (line)]] | wt | 260 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 201 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.315× (z -9.4) |
| [[COLO 205 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.1) ⚠ cell-cycle shift, explains ~79% of this change |
| [[H4 (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[LoVo (line)]] | wt | 83.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.49× (z +8.5) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[LS 180 (line)]] | wt | 233 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.336× (z -8.9) |
| [[SW 1271 (line)]] | alt | 386 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.152× (z -10.7) |
| [[AN3 CA (line)]] | alt | 45.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENC1]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[NFE2L3]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[SEMA3A]] | +0.60 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[TNFRSF21]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LIMA1]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[AMIGO2]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CCN1]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[NUAK2]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[FHL2]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[VCL]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ECT2]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 | ⚠ same locus (39.5 kb: neighbours can correlate without regulation) |
| [[RBMS2]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2Q2]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ALDH2]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SNX3]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RTCA]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RUFY2]] | -0.49 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[PCYT1A]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CLPP]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ZFAND2A]] | -0.47 | -0.45 / -0.43 | both halves | 4e-05 |  |
| [[RNF14]] | -0.47 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[VIPAS39]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[DIP2C]] | -0.46 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[LINC00662]] | -0.45 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN1]] | B | CLDN1 activity raises NCEH1's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 2.47× lower at baseline in the lines without CLDN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |
| [[FGD6]] | B | FGD6 activity raises NCEH1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 2.16× lower at baseline in the lines without FGD6 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[SOX9]] | B | SOX9 activity raises NCEH1's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.65× lower at baseline in the lines without SOX9 | 0.086 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX9]] | B | NCEH1 activity raises SOX9's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 3.63× lower at baseline in the lines without NCEH1 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |
| [[DCUN1D4]] | B | NCEH1 activity lowers DCUN1D4's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 1.55× higher at baseline in the lines without NCEH1 | 0.057 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |
| [[FAM107B]] | B | NCEH1 activity raises FAM107B's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 3.69× lower at baseline in the lines without NCEH1 | 0.062 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |
| [[RUFY2]] | B | NCEH1 activity raises RUFY2's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 1.20× lower at baseline in the lines without NCEH1 | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |
| [[VCL]] | B | NCEH1 activity raises VCL's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without NCEH1 | 0.086 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |
| [[PCYT1A]] | B | NCEH1 activity raises PCYT1A's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without NCEH1 | 0.092 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.9, 14.6); signed map (15.1, 41.7). **Vector** length 148, 47.0% of its response variance represented; |z| ≥ 3 in 1,536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.6 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +4.6 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.6 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.9 | -9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -8.4 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.4 | -9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.3 | -7.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -5.1 | -3.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.4 | -3.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | neutral cholesterol ester hydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.31 — chr3:172,630,249-172,711,218 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1363, NCEH; previously AADACL1 |
| Gene groups (HGNC) | Arylacetamide deacetylase family |
| Reactome | 4 pathways, smallest: LDL clearance; Plasma lipoprotein clearance; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PIU2](https://www.uniprot.org/uniprotkb/Q6PIU2) (Neutral cholesterol ester hydrolase 1):

> Hydrolyzes 2-acetyl monoalkylglycerol ether (1-O-alkyl-2-acetyl-sn-glycerol), the penultimate precursor of the pathway for de novo synthesis of platelet-activating factor. May be responsible for the hydrolysis of cholesterol esters (such as cholesteryl (9Z-octadecenoate)) in macrophages (By similarity). Also involved in organ detoxification by hydrolyzing exogenous organophosphorus compounds (By similarity). May contribute to cancer pathogenesis by promoting tumor cell migration.

**Summary**, from NCBI Gene [57552](https://www.ncbi.nlm.nih.gov/gene/57552):

> Predicted to enable serine hydrolase activity. Predicted to be involved in ether lipid metabolic process. Predicted to act upstream of or within protein dephosphorylation and xenobiotic metabolic process. Located in membrane. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:29260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29260) · Entrez [57552](https://www.ncbi.nlm.nih.gov/gene/57552) · UniProt [Q6PIU2](https://www.uniprot.org/uniprotkb/Q6PIU2) · Ensembl [ENSG00000144959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144959)

## Data

Gene col 6948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6948); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6948]; `tensor/DDL_lfc|DDL_z.npy` [6948]; `embed/gene_vectors.npy` [6948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6948 or target_col == 6948). Every well: [[NCEH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCEH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
