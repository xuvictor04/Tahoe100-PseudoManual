---
symbol: "PRCC"
type: "gene"
col: 6707
ensembl_id: "ENSG00000143294"
name: "proline rich mitotic checkpoint control factor"
location: "1q23.1"
module: 7
arm: "+"
pooled_cpm: 44.97
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PRCC

*proline rich mitotic checkpoint control factor* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 10.1× (z +29.2, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.529× (z -15.4, q 0e+00, down in 36 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.718× (z -8.0, q 2e-13, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP8]] (+0.74, fdr 7e-06), [[KMT2D]] (+0.69, fdr 7e-06), [[DDX23]] (+0.67, fdr 7e-06); moves opposite to [[SPAG9]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **10.1×** | +29.2 | 0e+00 | 48/49 (LoVo, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **6.12×** | +22.9 | 0e+00 | 45/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +11.7 | 3e-29 | 37/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +10.8 | 5e-25 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +10.5 | 2e-23 | 36/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +8.4 | 3e-15 | 35/48 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +8.4 | 5e-15 | 38/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +8.3 | 7e-15 | 36/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +7.9 | 1e-13 | 35/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +6.7 | 9e-10 | 0/49 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.2 | 9e-06 | 19/48 (A498, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +5.1 | 2e-05 | 22/47 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.9 | 3e-05 | 22/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 15/47 (LoVo, SW480, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.1 | 0.001 | 11/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.002 | 19/47 (LOX-IMVI, SW48, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.029 | 8/48 (NCI-H460, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.2 | 0.045 | 8/47 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.049 | 5/48 (NCI-H23, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.529×** | -15.4 | 0e+00 | 36/46 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.569×** | -13.2 | 4e-37 | 32/42 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.718×** | -8.0 | 2e-13 | 35/48 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -6.4 | 2e-08 | 24/48 (C32, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.769×** | -6.4 | 2e-08 | 22/48 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.771×** | -6.3 | 2e-08 | 23/48 (SHP-77, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.766×** | -5.3 | 1e-05 | 22/45 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.820×** | -4.8 | 1e-04 | 19/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.824×** | -4.7 | 2e-04 | 17/48 (SW1417, C32, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.767×** | -4.6 | 3e-04 | 18/46 (SW48, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.3 | 9e-04 | 17/48 (NCI-H2347, C32, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.844× | -4.1 | 0.002 | 15/48 (SHP-77, CHP-212, …) | inconsistent across doses | position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.839× | -3.7 | 0.009 | 14/47 (J82, LS 180, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.854× | -3.7 | 0.009 | 17/48 (SW48, HEC-1-A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.909× | -3.3 | 0.037 | 7/48 (SW 1271, SNU-1, …) | top dose only |  |
| [[Ritonavir (drug)]] 0.5 µM |  | 0.874× | -3.3 | 0.038 | 15/48 (H4, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.4 | 6 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.1× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -10.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 46.1 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 13.3× (z +12.7) | [[AZD2858 (drug)]] 0.5 µM 0.205× (z -10.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 45.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.3× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.0864× (z -30.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 48.3 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.2× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 87.9 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.0× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -15.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 36.9 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.6× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -10.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 41.6 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.0× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 43.5 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.0× (z +12.0) | [[Bortezomib (drug)]] 5 µM 0.122× (z -10.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 99.1 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.8× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 57.3 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -14.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 48.4 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 13.4× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -14.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 48.1 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.79× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -20.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.95× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0943× (z -24.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 73.8 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 7.51× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.0403× (z -31.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 69.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -9.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 40.1 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.87× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -13.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 38.0 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.06× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.9 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.6× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 44.0 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.8× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 64.5 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.33× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -19.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 50.1 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.44× (z +12.9) | — |
| [[A549 (line)]] | wt | 36.8 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.75× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 29.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.04× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 53.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.4× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 37.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 30.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.8× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 34.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.31× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 40.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.66× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.0× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 42.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.6× (z +9.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.239× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 60.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +11.9) | — |
| [[SW48 (line)]] | wt | 56.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.72× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 35.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 24.4× (z +11.6) | — |
| [[H4 (line)]] | wt | 42.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 56.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 29.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.7× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 32.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +11.3) | — |
| [[J82 (line)]] | alt | 32.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.02× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 30.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.32× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 34.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.51× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP8]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[KMT2D]] | +0.69 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DDX23]] | +0.67 | +0.73 / +0.67 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 485 |
| [[FEM1A]] | +0.67 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[CUL1]] | +0.66 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TSSC4]] | +0.66 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CHD8]] | +0.64 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[GTF3C4]] | +0.64 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ZNF629]] | +0.64 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SETD1A]] | +0.63 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CLP1]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[PPAN]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.64 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PRCC's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PRCC's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-31.0, -10.0); signed map (-9.5, -28.5). **Vector** length 91.5, 21.1% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.8 | +29.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +11.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.1 | +22.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +6.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +8.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | proline rich mitotic checkpoint control factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,750,610-156,800,815 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RCCP1 |
| Gene groups (HGNC) | Spliceosomal Bact complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92733](https://www.uniprot.org/uniprotkb/Q92733) (Proline-rich protein PRCC):

> May regulate cell cycle progression through interaction with MAD2L2.

**Summary**, from NCBI Gene [5546](https://www.ncbi.nlm.nih.gov/gene/5546):

> This gene encodes a protein that may play a role in pre-mRNA splicing. Chromosomal translocations (X;1)(p11;q21) that result in fusion of this gene to TFE3 (GeneID 7030) have been associated with papillary renal cell carcinoma. A PRCC-TFE3 fusion protein is expressed in affected carcinomas and is likely associated with altered gene transactivation. This fusion protein has also been associated with disruption of the cell cycle.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:9343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9343) · Entrez [5546](https://www.ncbi.nlm.nih.gov/gene/5546) · UniProt [Q92733](https://www.uniprot.org/uniprotkb/Q92733) · Ensembl [ENSG00000143294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143294)

## Data

Gene col 6707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6707); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6707]; `tensor/DDL_lfc|DDL_z.npy` [6707]; `embed/gene_vectors.npy` [6707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6707 or target_col == 6707). Every well: [[PRCC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRCC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
