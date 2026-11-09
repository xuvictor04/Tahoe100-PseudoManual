---
symbol: "CAMK2D"
type: "gene"
col: 6979
ensembl_id: "ENSG00000145349"
name: "calcium/calmodulin dependent protein kinase II delta"
location: "4q26"
module: 68
arm: "+"
pooled_cpm: 206.08
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# CAMK2D

*calcium/calmodulin dependent protein kinase II delta* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +23.5, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.557× (z -13.7, q 4e-40, down in 40 of 45 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 0.825× (z -4.3, q 8e-04, down in 23 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 6 lines (SW480 0.341×, LOX-IMVI 0.310×, LS 180 0.389×, Hs 766T 0.348×, …; ⚠ cell-cycle shift, explains ~38% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (LOX-IMVI 0.272×, LS 180 0.366×, SW480 0.381×, Hs 766T 0.329×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LS 180 0.378×, LoVo 0.405×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1088 0.0730×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.206×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HT-29 0.634×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GULP1]] (+0.70, fdr 7e-06), [[CPEB2]] (+0.68, fdr 1e-05), [[PTPRK]] (+0.65, fdr 1e-05); moves opposite to [[TAF5L]] (-0.58, fdr 5e-05), [[ABHD17A]] (-0.58, fdr 6e-05), [[WDR5]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CPEB2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +23.5 | 0e+00 | 41/45 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +15.4 | 0e+00 | 39/45 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +9.1 | 2e-17 | 32/45 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +8.2 | 3e-14 | 28/45 (COLO 205, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +6.1 | 1e-07 | 25/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +6.1 | 1e-07 | 22/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.18× | +5.4 | 6e-06 | 21/45 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.23×** | +4.9 | 6e-05 | 20/45 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.002 | 20/44 (RKO, AsPC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.18× | +3.8 | 0.009 | 19/44 (H4, A-172, …) | rises with dose |  |
| [[Penfluridol (drug)]] 5 µM |  | 1.17× | +3.6 | 0.016 | 19/44 (A498, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.018 | 19/45 (NCI-H460, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.020 | 18/46 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.030 | 7/45 (Hs 766T, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.030 | 20/45 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.058 | 17/45 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.060 | 16/47 (RKO, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.060 | 18/45 (H4, A498, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.067 | 10/44 (RKO, AsPC-1, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.074 | 13/45 (LOX-IMVI, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.074 | 14/44 (H4, SNU-1, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6979.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 6 lines (SW480 0.341×, LOX-IMVI 0.310×, LS 180 0.389×, Hs 766T 0.348×, …; ⚠ cell-cycle shift, explains ~38% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (LOX-IMVI 0.272×, LS 180 0.366×, SW480 0.381×, Hs 766T 0.329×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LS 180 0.378×, LoVo 0.405×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1088 0.0730×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.206×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HT-29 0.634×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.557×** | -13.7 | 4e-40 | 40/45 (LOX-IMVI, LS 180, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.585×** | -12.6 | 1e-33 | 42/45 (SW480, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.583×** | -12.2 | 1e-31 | 32/46 (LS 180, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.586×** | -12.1 | 2e-31 | 32/41 (KATO III, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.688×** | -8.8 | 2e-16 | 39/45 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.684×** | -8.6 | 1e-15 | 35/44 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.696×** | -8.5 | 2e-15 | 34/45 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.711×** | -7.4 | 1e-11 | 27/42 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.821×** | -4.4 | 6e-04 | 24/47 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.825×** | -4.3 | 8e-04 | 23/45 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.838× | -4.0 | 0.003 | 19/45 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.697×** | -3.6 | 0.018 | 17/35 (SK-MEL-2, A-172, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 197 | 14 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +44.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.580× (z -9.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 63.5 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +24.1) | — |
| [[C32 (line)]] | wt | 265 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +21.6) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[LS 180 (line)]] | wt | 363 | 2 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +16.9) | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -15.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 217 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +22.6) | [[Panobinostat (drug)]] 0.5 µM 0.514× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 475 | 2 | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -13.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 221 | 0 | 8 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -16.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 299 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -16.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 190 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.443× (z -8.7) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 173 | 3 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.403× (z -12.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 204 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +24.7) | [[Dinaciclib (drug)]] 0.5 µM 0.509× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[hTERT-HPNE (line)]] | wt | 263 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +17.3) | — |
| [[LoVo (line)]] | wt | 238 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +22.8) | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HepG2_C3A (line)]] | wt | 229 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -10.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 197 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.412× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 395 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.442× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.634× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 305 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 305 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.400× (z -13.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 92.2 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +28.0) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 285 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.362× (z -11.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[COLO 205 (line)]] | alt | 381 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.18× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.384× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 195 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW 900 (line)]] | alt | 257 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 162 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.349× (z -13.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 90.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +17.8) | — |
| [[KATO III (line)]] | alt | 254 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 207 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.70× (z +8.6) | [[Docetaxel (drug)]] 0.05 µM 0.529× (z -10.3) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 210 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 211 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +12.7) | — |
| [[A549 (line)]] | wt | 143 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 198 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.465× (z -9.3) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 166 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -11.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 148 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[AN3 CA (line)]] | alt | 294 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -9.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 145 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 190 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 208 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.371× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 245 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.468× (z -11.0) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 200 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0730× (z -11.6) |
| [[SW 1271 (line)]] | alt | 161 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.206× (z -9.1) |
| [[C-33 A (line)]] | alt | 25.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 41.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 231 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GULP1]] | +0.70 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[CPEB2]] | +0.68 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.62 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[LACTB2]] | +0.60 | +0.60 / +0.28 | both halves | 3e-04 |  |
| [[RIPK2-DT]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TMEM192]] | +0.59 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[LITAF]] | +0.59 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[RNF103-CHMP3]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[GALNT7-DT]] | +0.58 | +0.57 / +0.31 | both halves | 2e-04 |  |
| [[PATL2]] | +0.56 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[SNX16]] | +0.56 | +0.58 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | -0.58 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[ABHD17A]] | -0.58 | -0.61 / -0.39 | both halves | 6e-05 | pathway: MAPK family signaling cascades |
| [[WDR5]] | -0.58 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[AP1M1]] | -0.57 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MSTO2P]] | -0.56 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[WASF3]] | -0.56 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[FBXW2]] | -0.55 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[TSFM]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[MINK1]] | -0.54 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[HMOX2]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SPRYD3]] | -0.53 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[THOC3]] | -0.53 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPEB2]] | C | CPEB2 activity raises CAMK2D's level | lines that do not express CPEB2 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without CPEB2 | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: SFXN3, CDKN1A, LRIG3; maybe low, not absent; co-absent with the target |
| [[GULP1]] | C | GULP1 activity raises CAMK2D's level | lines that do not express GULP1 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without GULP1 | 0.091 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (19.7, 13.2); signed map (46.9, 13.8). **Vector** length 122, 37.2% of its response variance represented; |z| ≥ 3 in 1,395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +15.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +23.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.8 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.2 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.0 | -13.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -6.9 | -12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.0 | -8.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.9 | -8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.9 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent protein kinase II delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:113,418,054-113,761,927 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CAMKD |
| Gene groups (HGNC) | CAMK2 family |
| Reactome | 56 pathways, smallest: CaMK IV-mediated phosphorylation of CREB; Ras activation upon Ca2+ influx through NMDA receptor; Unblocking of NMDA receptors, glutamate binding and activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13557](https://www.uniprot.org/uniprotkb/Q13557) (Calcium/calmodulin-dependent protein kinase type II subunit delta):

> Calcium/calmodulin-dependent protein kinase involved in the regulation of Ca(2+) homeostatis and excitation-contraction coupling (ECC) in heart by targeting ion channels, transporters and accessory proteins involved in Ca(2+) influx into the myocyte, Ca(2+) release from the sarcoplasmic reticulum (SR), SR Ca(2+) uptake and Na(+) and K(+) channel transport. Targets also transcription factors and signaling molecules to regulate heart function. In its activated form, is involved in the …

**Summary**, from NCBI Gene [817](https://www.ncbi.nlm.nih.gov/gene/817):

> The product of this gene belongs to the serine/threonine protein kinase family and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. Calcium signaling is crucial for several aspects of plasticity at glutamatergic synapses. In mammalian cells, the enzyme is composed of four different chains: alpha, beta, gamma, and delta. The product of this gene is a delta chain. Alternative splicing results in multiple transcript variants encoding distinct isoforms. Distinct isoforms of this chain …

**Accessions** — [HGNC:1462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1462) · Entrez [817](https://www.ncbi.nlm.nih.gov/gene/817) · UniProt [Q13557](https://www.uniprot.org/uniprotkb/Q13557) · Ensembl [ENSG00000145349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145349)

## Data

Gene col 6979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6979); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6979]; `tensor/DDL_lfc|DDL_z.npy` [6979]; `embed/gene_vectors.npy` [6979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6979 or target_col == 6979). Every well: [[CAMK2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMK2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
