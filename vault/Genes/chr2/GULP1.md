---
symbol: "GULP1"
type: "gene"
col: 6871
ensembl_id: "ENSG00000144366"
name: "GULP PTB domain containing engulfment adaptor 1"
location: "2q32.1-q32.2"
module: 68
arm: "+"
pooled_cpm: 168.73
n_lines_expressing: 46
n_dd_up: 32
n_dd_down: 6
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# GULP1

*GULP PTB domain containing engulfment adaptor 1* — 2q32.1-q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.88× (z +40.7, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.399× (z -19.6, q 0e+00, down in 42 of 44 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 5 lines (CHP-212 0.0736×, A-172 0.113×, Panc 03.27 0.171×, C32 0.266×, …; ⚠ cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (CHP-212 0.0751×, A-172 0.122×, Panc 03.27 0.172×, SW1417 0.246×; ⚠ cell-cycle shift, explains ~37% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (CHP-212 0.108×, Panc 03.27 0.199×, A-172 0.219×; ⚠ cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.343×, SHP-77 0.581×); [[Tucidinostat (drug)]] 5 µM in 1 line (Panc 03.27 0.478×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (A-172 0.416×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMK2D]] (+0.70, fdr 7e-06), [[LINC01090]] (+0.69, fdr 1e-05, ⚠ same locus), [[C11orf58]] (+0.65, fdr 2e-05), [[RNF103-CHMP3]] (+0.65, fdr 1e-05); moves opposite to [[TAF5L]] (-0.57, fdr 1e-04), [[EFNA3]] (-0.55, fdr 3e-05), [[SPTLC2]] (-0.55, fdr 8e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LRP1B]] → it (grade B ⚠); 9 go from it, the strongest it → cells under [[Topotecan (hydrochloride) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.88×** | +40.7 | 0e+00 | 39/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.27×** | +25.1 | 0e+00 | 38/44 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.87×** | +21.5 | 0e+00 | 41/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +15.5 | 0e+00 | 35/44 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +14.2 | 7e-44 | 35/44 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.94×** | +14.1 | 5e-43 | 35/44 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.86×** | +13.1 | 3e-37 | 37/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +12.4 | 3e-33 | 36/44 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +8.3 | 5e-15 | 28/43 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.27×** | +7.1 | 5e-11 | 24/44 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +6.2 | 3e-08 | 25/43 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Penfluridol (drug)]] 5 µM |  | **1.28×** | +5.0 | 3e-05 | 25/43 (KATO III, HEC-1-A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.93×** | +4.9 | 4e-05 | 23/45 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +4.8 | 6e-05 | 22/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.6 | 1e-04 | 23/44 (RKO, NCI-H2030, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **1.25×** | +4.5 | 2e-04 | 20/44 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.4 | 4e-04 | 18/44 (J82, A-427, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +4.3 | 5e-04 | 21/44 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6871.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 5 lines (CHP-212 0.0736×, A-172 0.113×, Panc 03.27 0.171×, C32 0.266×, …; ⚠ cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (CHP-212 0.0751×, A-172 0.122×, Panc 03.27 0.172×, SW1417 0.246×; ⚠ cell-cycle shift, explains ~37% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (CHP-212 0.108×, Panc 03.27 0.199×, A-172 0.219×; ⚠ cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.343×, SHP-77 0.581×); [[Tucidinostat (drug)]] 5 µM in 1 line (Panc 03.27 0.478×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (A-172 0.416×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.399×** | -19.6 | 0e+00 | 42/44 (CHP-212, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.417×** | -18.6 | 0e+00 | 41/44 (CHP-212, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.483×** | -15.5 | 0e+00 | 35/44 (CHP-212, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.675×** | -8.1 | 1e-13 | 31/43 (HT-29, CHP-212, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.722×** | -6.9 | 4e-10 | 30/44 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.825×** | -4.1 | 0.004 | 20/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.842× | -3.7 | 0.019 | 21/44 (Panc 03.27, CHP-212, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.860× | -3.2 | 0.083 | 18/44 (CHP-212, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 176 | 16 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.62× (z +44.1) | [[Panobinostat (drug)]] 5 µM 0.436× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 342 | 6 | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +37.9) | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -25.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.416× (z -10.4) |
| [[COLO 205 (line)]] | alt | 337 | 11 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +30.0) | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 262 | 12 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +25.4) | [[Panobinostat (drug)]] 5 µM 0.290× (z -12.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 188 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +43.2) | — |
| [[HT-29 (line)]] | alt | 104 | 8 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +30.4) | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -13.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 211 | 9 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +23.6) | [[Panobinostat (drug)]] 5 µM 0.291× (z -13.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 133 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +38.6) | [[Panobinostat (drug)]] 5 µM 0.474× (z -8.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[CHP-212 (line)]] | wt | 1,178 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0736× (z -26.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.343× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 205 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +30.7) | [[Panobinostat (drug)]] 5 µM 0.377× (z -9.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 60.3 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +30.0) | — |
| [[NCI-H1573 (line)]] | alt | 294 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +25.3) | — |
| [[NCI-H2030 (line)]] | alt | 263 | 8 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +36.0) | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -9.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 327 | 3 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +20.7) | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -19.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.478× (z -11.8) |
| [[C32 (line)]] | wt | 290 | 6 | 3 (3 ⚠) | [[Cobimetinib (drug)]] 0.5 µM 2.50× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -15.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 145 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +21.0) | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -14.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 176 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 4.80× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 284 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.322× (z -14.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 83.5 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +29.4) | — |
| [[SNU-423 (line)]] | alt | 152 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +21.8) | [[Panobinostat (drug)]] 5 µM 0.277× (z -14.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 79.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +17.8) | — |
| [[AsPC-1 (line)]] | alt | 449 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +18.2) | [[Panobinostat (drug)]] 5 µM 0.204× (z -15.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Dexamethasone (drug)]] 5 µM 0.381× (z -9.4) |
| [[H4 (line)]] | wt | 66.0 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 5.01× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 209 | 1 | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 3.19× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.358× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.581× (z -9.9) |
| [[SW1417 (line)]] | alt | 284 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.246× (z -16.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 159 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.367× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[AN3 CA (line)]] | alt | 244 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -11.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 196 | 3 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.60× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.443× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 298 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.70× (z +19.1) | [[Panobinostat (drug)]] 5 µM 0.256× (z -14.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW 900 (line)]] | alt | 133 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.5) | [[Docetaxel (drug)]] 0.05 µM 0.365× (z -11.1) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 119 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.387× (z -8.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 94.4 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.89× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.409× (z -12.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 97.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +20.8) | — |
| [[HCT15 (line)]] | alt | 44.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +17.1) | — |
| [[hTERT-HPNE (line)]] | wt | 64.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 71.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +23.7) | — |
| [[PANC-1 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.493× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Hs 766T (line)]] | wt | 77.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.332× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 94.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +21.0) | — |
| [[NCI-H661 (line)]] | alt | 641 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -12.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 74.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +16.5) | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0733× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[C-33 A (line)]] | alt | 34.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 61.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK2D]] | +0.70 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LINC01090]] | +0.69 | +0.64 / +0.54 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[C11orf58]] | +0.65 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RNF103-CHMP3]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[LRP1B]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[GUCY1A2]] | +0.64 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.63 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.62 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[TTC6]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.60 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[RRAGC-DT]] | +0.60 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | +0.60 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[THSD7A]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | -0.57 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[EFNA3]] | -0.55 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SPTLC2]] | -0.55 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[MINK1]] | -0.54 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[NPHP4]] | -0.54 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[POGLUT2]] | -0.53 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ZHX3]] | -0.53 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[NBPF3]] | -0.53 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[ATP7B]] | -0.53 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[PDIA5]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 | same gene group |
| [[DHTKD1]] | -0.52 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[ELP1]] | -0.52 | -0.48 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP1B]] | B | LRP1B activity lowers GULP1's level | lines that do not express LRP1B (24) vs lines expressing it (26) | 1.10× higher at baseline in the lines without LRP1B | 0.054 | ⚠ within organs, on part of the lines; also absent: GLRB, VEGFC, SPANXA2-OT1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises GULP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Topotecan (hydrochloride) (drug)]] 5 µM | C | GULP1 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express GULP1 (4) vs lines expressing it (44) | the lines without GULP1: 0.46× the cells of the other lines | 0.036 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1 |
| [[ARHGAP42]] | C | GULP1 activity raises ARHGAP42's level | lines that do not express GULP1 (4) vs lines expressing it (46) | 4.81× lower at baseline in the lines without GULP1 | 0.069 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1 |
| [[CPEB2]] | C | GULP1 activity raises CPEB2's level | lines that do not express GULP1 (4) vs lines expressing it (46) | 2.83× lower at baseline in the lines without GULP1 | 0.080 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1 |
| [[GNAI3]] | C | GULP1 activity strengthens GNAI3's drug response | lines that do not express GULP1 (4) vs lines expressing it (45) | the lines without GULP1 respond 0.45× as strongly (z diff +2.50); strongest at Dinaciclib 5 µM: 1.06x vs 0.62x (z diff +5.6) | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1; target measured in part of the lines; artifact flags |
| [[ATP7B]] | C | GULP1 activity lowers ATP7B's level | lines that do not express GULP1 (4) vs lines expressing it (46) | 2.50× higher at baseline in the lines without GULP1 | 0.085 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1 |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | GULP1 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express GULP1 (4) vs lines expressing it (44) | the lines without GULP1: 0.43× the cells of the other lines | 0.087 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1 |
| [[CAMK2D]] | C | GULP1 activity raises CAMK2D's level | lines that do not express GULP1 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without GULP1 | 0.091 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1 |
| [[MGAT4B]] | C | GULP1 activity strengthens MGAT4B's drug response | lines that do not express GULP1 (4) vs lines expressing it (44) | the lines without GULP1 respond 0.79× as strongly (z diff +0.49); strongest at Dinaciclib 5 µM: 0.18x vs 1.47x (z diff +9.3) | 0.096 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1; target measured in part of the lines; both ways; artifact flags |
| cells under [[Menadione (drug)]] 0.5 µM | C | GULP1's natural level raises the cells' numbers under Menadione 0.5 µM (protects the cells) | GULP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.384 over the table, 0.069 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (17.6, 13.5); signed map (28.4, -1.2). **Vector** length 139, 45.9% of its response variance represented; |z| ≥ 3 in 1,704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.1 | +25.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +40.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +21.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.6 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.0 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.7 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +5.3 | +4.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.6 | -18.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -7.5 | -19.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.9 | -15.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | GULP PTB domain containing engulfment adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1-q32.2 — chr2:188,291,669-188,595,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CED6, CED-6, GULP |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBP9](https://www.uniprot.org/uniprotkb/Q9UBP9) (PTB domain-containing engulfment adapter protein 1):

> May function as an adapter protein. Required for efficient phagocytosis of apoptotic cells. Modulates cellular glycosphingolipid and cholesterol transport. May play a role in the internalization and endosomal trafficking of various LRP1 ligands, such as PSAP. Increases cellular levels of GTP-bound ARF6.

**Summary**, from NCBI Gene [51454](https://www.ncbi.nlm.nih.gov/gene/51454):

> The protein encoded by this gene is an adapter protein necessary for the engulfment of apoptotic cells by phagocytes. Several transcript variants, some protein coding and some thought not to be protein coding, have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:18649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18649) · Entrez [51454](https://www.ncbi.nlm.nih.gov/gene/51454) · UniProt [Q9UBP9](https://www.uniprot.org/uniprotkb/Q9UBP9) · Ensembl [ENSG00000144366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144366)

## Data

Gene col 6871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6871); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6871]; `tensor/DDL_lfc|DDL_z.npy` [6871]; `embed/gene_vectors.npy` [6871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6871 or target_col == 6871). Every well: [[GULP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GULP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
