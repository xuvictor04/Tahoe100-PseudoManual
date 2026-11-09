---
symbol: "SIRT1"
type: "gene"
col: 1770
ensembl_id: "ENSG00000096717"
name: "sirtuin 1"
location: "10q21.3"
module: 69
arm: "+"
pooled_cpm: 72.89
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# SIRT1

*sirtuin 1* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.54× (z +40.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.469× (z -12.2, q 3e-31, down in 35 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.771× (z -4.4, q 0.002, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SHP-77 0.130×, AN3 CA 0.0671×, SW48 0.0835×, A549 0.181×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.172×, SNU-1 0.133×, SW480 0.350×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.0948×, NCI-H2347 0.263×, LoVo 0.280×; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0458×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (AN3 CA 0.261×); [[Ritonavir (drug)]] 0.5 µM in 1 line (SW 1271 0.0793×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPC1]] (+0.69, fdr 7e-06), [[EP300]] (+0.68, fdr 2e-05), [[PNRC1]] (+0.67, fdr 7e-06); moves opposite to [[BCAP31]] (-0.61, fdr 1e-05), [[KIF21B]] (-0.60, fdr 6e-05), [[RNGTT]] (-0.59, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.54×** | +40.5 | 0e+00 | 47/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.06×** | +22.5 | 0e+00 | 48/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.67×** | +21.7 | 0e+00 | 48/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.96×** | +18.1 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.34×** | +14.2 | 1e-43 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +12.8 | 1e-35 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.04×** | +11.9 | 1e-30 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +10.4 | 2e-23 | 39/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.77×** | +8.6 | 8e-16 | 41/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.29×** | +7.0 | 2e-10 | 35/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.46×** | +6.3 | 1e-08 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +6.3 | 2e-08 | 29/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.1 | 6e-08 | 32/48 (J82, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.5 | 2e-06 | 32/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.3 | 4e-06 | 22/49 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +4.7 | 8e-05 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.001 | 26/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1770.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SHP-77 0.130×, AN3 CA 0.0671×, SW48 0.0835×, A549 0.181×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.172×, SNU-1 0.133×, SW480 0.350×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.0948×, NCI-H2347 0.263×, LoVo 0.280×; ⚠ toxic; transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0458×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (AN3 CA 0.261×); [[Ritonavir (drug)]] 0.5 µM in 1 line (SW 1271 0.0793×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.469×** | -12.2 | 3e-31 | 35/41 (SHP-77, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.509×** | -11.3 | 3e-27 | 39/49 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.567×** | -8.8 | 3e-16 | 34/45 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.771×** | -4.4 | 0.002 | 28/48 (CFPAC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Belzutifan (drug)]] 5 µM |  | 0.690× | -3.1 | 0.21 | 13/47 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 72.3 | 15 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +29.6) | — |
| [[SW480 (line)]] | alt | 60.0 | 12 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +28.0) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -12.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 69.1 | 11 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +27.2) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 109 | 9 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.64× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.0835× (z -17.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 74.8 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +30.0) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -12.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 82.8 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +27.5) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 133 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +19.6) | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 46.7 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +34.8) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -13.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 40.2 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +22.6) | — |
| [[LOX-IMVI (line)]] | wt | 43.2 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +26.2) | — |
| [[RKO (line)]] | wt | 53.0 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +17.6) | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -12.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 52.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +28.2) | — |
| [[NCI-H1792 (line)]] | alt | 60.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +22.3) | — |
| [[NCI-H23 (line)]] | alt | 53.3 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +26.3) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -18.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 78.0 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +24.6) | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -12.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 90.5 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +29.7) | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -10.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 70.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +26.2) | — |
| [[A498 (line)]] | wt | 67.8 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +32.6) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -12.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 120 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +21.3) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -16.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 71.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +20.8) | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 70.2 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +37.2) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 96.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +29.9) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 51.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 38.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +31.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0948× (z -16.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 55.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +30.5) | — |
| [[HEC-1-A (line)]] | alt | 50.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 64.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +18.7) | — |
| [[Panc 03.27 (line)]] | alt | 84.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -13.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 119 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.27× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 100 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +19.8) | — |
| [[HepG2_C3A (line)]] | wt | 108 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.2) | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 44.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +19.6) | — |
| [[hTERT-HPNE (line)]] | wt | 62.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +25.0) | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +24.5) | — |
| [[AN3 CA (line)]] | alt | 149 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.261× (z -9.3) |
| [[H4 (line)]] | wt | 51.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 73.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 45.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +19.4) | — |
| [[SNU-1 (line)]] | wt | 66.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -15.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 68.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +9.0) | [[Ritonavir (drug)]] 0.5 µM 0.0793× (z -8.8) |
| [[HCT15 (line)]] | alt | 84.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 72.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +17.3) | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0458× (z -14.2) |
| [[SHP-77 (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -18.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC1]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[EP300]] | +0.68 | +0.61 / +0.48 | both halves | 2e-05 | pathway: Cellular response to heat stress; STRING 972 |
| [[PNRC1]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CHD2]] | +0.66 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[THAP1]] | +0.66 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.65 | +0.64 / +0.44 | both halves | 3e-05 | pathway: Cellular response to heat stress; STRING 754 |
| [[RFX1]] | +0.65 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[NR1D2]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[REL]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 | STRING 622 |
| [[KLF4]] | +0.63 | +0.65 / +0.64 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 482 |
| [[GTF2IRD2B]] | +0.62 | +0.69 / +0.29 | both halves | 3e-04 |  |
| [[RBM43]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.61 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[KIF21B]] | -0.60 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[RNGTT]] | -0.59 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.59 | -0.58 / -0.60 | both halves | 8e-06 |  |
| [[LIMK1]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[FBXW2]] | -0.58 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[STRAP]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 | pathway: Adherens junctions interactions |
| [[PSMD14]] | -0.58 | -0.65 / -0.53 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[PSMD2]] | -0.57 | -0.57 / -0.46 | both halves | 2e-05 | pathway: Adherens junctions interactions |
| [[PSMD13]] | -0.57 | -0.67 / -0.40 | both halves | 5e-05 | pathway: Adherens junctions interactions |
| [[ANXA6]] | -0.57 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[TCF3]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 | pathway: Adherens junctions interactions |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.0, -31.1); signed map (-7.1, 9.8). **Vector** length 104, 31.9% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.2 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +22.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.2 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | +2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.9 | +2.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.5 | +1.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.9 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.1 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | sirtuin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:67,884,656-67,918,390 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIR2L1 |
| Gene groups (HGNC) | Sirtuins; eNoSC complex |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 31 pathways, smallest: Regulation of MITF-M dependent genes involved in metabolism; Regulation of FOXO transcriptional activity by acetylation; SIRT1 negatively regulates rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EB6](https://www.uniprot.org/uniprotkb/Q96EB6) (NAD-dependent protein deacetylase sirtuin-1):

> NAD-dependent protein deacetylase that links transcriptional regulation directly to intracellular energetics and participates in the coordination of several separated cellular functions such as cell cycle, response to DNA damage, metabolism, apoptosis and autophagy. Can modulate chromatin function through deacetylation of histones and can promote alterations in the methylation of histones and DNA, leading to transcriptional repression. Deacetylates a broad range of transcription factors and …

**Summary**, from NCBI Gene [23411](https://www.ncbi.nlm.nih.gov/gene/23411):

> This gene encodes a member of the sirtuin family of proteins, homologs to the yeast Sir2 protein. Members of the sirtuin family are characterized by a sirtuin core domain and grouped into four classes. The functions of human sirtuins have not yet been determined; however, yeast sirtuin proteins are known to regulate epigenetic gene silencing and suppress recombination of rDNA. Studies suggest that the human sirtuins may function as intracellular regulatory proteins with …

**Accessions** — [HGNC:14929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14929) · Entrez [23411](https://www.ncbi.nlm.nih.gov/gene/23411) · UniProt [Q96EB6](https://www.uniprot.org/uniprotkb/Q96EB6) · Ensembl [ENSG00000096717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096717)

## Data

Gene col 1770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1770); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1770]; `tensor/DDL_lfc|DDL_z.npy` [1770]; `embed/gene_vectors.npy` [1770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1770 or target_col == 1770). Every well: [[SIRT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIRT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
