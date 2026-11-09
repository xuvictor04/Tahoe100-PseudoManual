---
symbol: "KLHL20"
type: "gene"
col: 1149
ensembl_id: "ENSG00000076321"
name: "kelch like family member 20"
location: "1q25.1"
module: 119
arm: "+"
pooled_cpm: 67.78
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# KLHL20

*kelch like family member 20* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.03× (z +23.2, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.420× (z -21.4, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.816× (z -4.8, q 1e-04, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H460 0.233×, RKO 0.116×, A-427 0.170×, NCI-H2347 0.282×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.165×, HEC-1-A 0.123×, RPMI-7951 0.128×, SW1417 0.229×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0912×, C32 0.184×, NCI-H2030 0.236×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX57]] (+0.73, fdr 7e-06), [[CHMP2A]] (+0.70, fdr 1e-05), [[TTI2]] (+0.68, fdr 7e-06); moves opposite to [[MOB1A]] (-0.58, fdr 1e-05), [[UBQLN4]] (-0.57, fdr 2e-05), [[HUWE1]] (-0.57, fdr 2e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1149.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.03×** | +23.2 | 0e+00 | 48/49 (SW480, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.98×** | +14.1 | 1e-42 | 42/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +11.6 | 1e-28 | 40/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +10.9 | 2e-25 | 39/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +8.8 | 1e-16 | 34/48 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +7.3 | 2e-11 | 30/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +6.2 | 6e-08 | 31/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +6.1 | 7e-08 | 23/48 (BT-474, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +5.2 | 1e-05 | 23/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +5.0 | 4e-05 | 18/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +4.9 | 5e-05 | 24/48 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.014 | 18/48 (LS 180, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.014 | 12/49 (AsPC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.019 | 10/49 (A-427, SHP-77, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.15× | +3.4 | 0.030 | 16/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.061 | 3/50 (HOP62, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.066 | 6/48 (LS 180, Hs 766T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.081 | 11/48 (NCI-H1792, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1149.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H460 0.233×, RKO 0.116×, A-427 0.170×, NCI-H2347 0.282×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.165×, HEC-1-A 0.123×, RPMI-7951 0.128×, SW1417 0.229×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0912×, C32 0.184×, NCI-H2030 0.236×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.420×** | -21.4 | 0e+00 | 45/49 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -19.2 | 0e+00 | 40/42 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.547×** | -13.8 | 9e-41 | 39/45 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.610×** | -11.7 | 1e-29 | 36/47 (SNU-423, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -4.9 | 9e-05 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.821×** | -4.8 | 1e-04 | 23/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.816×** | -4.8 | 1e-04 | 22/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~11% of this change | 0.837× | -4.4 | 9e-04 | 20/47 (NCI-H2347, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.845× | -4.2 | 0.002 | 15/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.846× | -4.1 | 0.002 | 17/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.864× | -3.6 | 0.017 | 15/49 (NCI-H1573, NCI-H661, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.896× | -3.6 | 0.018 | 6/48 (CHP-212, LOX-IMVI, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.876× | -3.3 | 0.049 | 9/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.881× | -3.1 | 0.074 | 9/48 (HT-29, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 83.3 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.03× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0912× (z -28.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 81.7 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.10× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -27.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 84.5 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.39× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 61.9 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.49× (z +12.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 71.3 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 102 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.20× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -24.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 66.4 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.27× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -22.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 97.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -11.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.4 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 63.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 18.8× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 78.2 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.20× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -11.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 75.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.7× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -23.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 68.9 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.64× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.278× (z -11.5) ⚠ toxic |
| [[SW1417 (line)]] | alt | 66.3 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.67× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -15.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 64.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.332× (z -12.1) ⚠ toxic |
| [[A498 (line)]] | wt | 70.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.70× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 77.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -15.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 50.9 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.27× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -12.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 54.5 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.8× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 89.2 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.14× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 70.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.62× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 95.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.86× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 66.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.49× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -14.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 64.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.58× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 73.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.8× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -10.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 72.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.22× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -13.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 53.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 53.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -15.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 54.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.57× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.488× (z -9.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 68.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -19.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 75.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -14.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 48.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -20.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 43.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 44.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.60× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 59.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.72× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 45.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.62× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 65.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.02× (z +8.7) | — |
| [[SW48 (line)]] | wt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -11.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX57]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[CHMP2A]] | +0.70 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TTI2]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SPOP]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | same gene group; STRING 924 |
| [[IGBP1]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[CWC15]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[FAM222B]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[NSFP1]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[TIMM29]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SUGP1]] | +0.65 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ADPRS]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[UBQLN4]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[HUWE1]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ELK4]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[HNRNPA2B1]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 | STRING 594 |
| [[ADSS2]] | -0.56 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[FKBP4]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.3, -10.4); signed map (-9.3, -10.4). **Vector** length 108, 29.6% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.1 | +23.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.9 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +14.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.6 | -11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -19.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.6 | -21.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -13.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1 — chr1:173,714,941-173,786,692 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KLEIP, KHLHX |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2M5](https://www.uniprot.org/uniprotkb/Q9Y2M5) (Kelch-like protein 20):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex involved in interferon response and anterograde Golgi to endosome transport. The BCR(KLHL20) E3 ubiquitin ligase complex mediates the ubiquitination of DAPK1, leading to its degradation by the proteasome, thereby acting as a negative regulator of apoptosis. The BCR(KLHL20) E3 ubiquitin ligase complex also specifically mediates 'Lys-33'-linked ubiquitination. Involved in anterograde Golgi to endosome …

**Summary**, from NCBI Gene [27252](https://www.ncbi.nlm.nih.gov/gene/27252):

> The protein encoded by this gene is a member of the kelch family of proteins, which is characterized by a 44-56 amino acid repeat motif. The kelch motif appears in many different polypeptide contexts and contains multiple potential protein-protein contact sites. Members of this family are present both throughout the cell and extracellularly, with diverse activities. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25056) · Entrez [27252](https://www.ncbi.nlm.nih.gov/gene/27252) · UniProt [Q9Y2M5](https://www.uniprot.org/uniprotkb/Q9Y2M5) · Ensembl [ENSG00000076321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076321)

## Data

Gene col 1149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1149); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1149]; `tensor/DDL_lfc|DDL_z.npy` [1149]; `embed/gene_vectors.npy` [1149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1149 or target_col == 1149). Every well: [[KLHL20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
