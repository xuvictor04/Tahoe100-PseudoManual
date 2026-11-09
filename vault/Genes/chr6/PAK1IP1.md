---
symbol: "PAK1IP1"
type: "gene"
col: 3291
ensembl_id: "ENSG00000111845"
name: "PAK1 interacting protein 1"
location: "6p24.2"
module: 1
arm: "+"
pooled_cpm: 24.09
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 6
n_dd_up_clean: 28
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PAK1IP1

*PAK1 interacting protein 1* — 6p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.48× (z +21.9, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 4.43× (z +18.5, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.719× (z -3.9, q 0.052, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 0.590× (z -3.5, q 0.062, down in 16 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRS1]] (+0.81, fdr 7e-06), [[UTP14A]] (+0.79, fdr 7e-06), [[BRIX1]] (+0.79, fdr 7e-06); moves opposite to [[GNAS]] (-0.68, fdr 7e-06), [[YPEL5]] (-0.66, fdr 7e-06), [[SARAF]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.48×** | +21.9 | 0e+00 | 47/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.43×** | +18.5 | 0e+00 | 47/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.89×** | +16.2 | 0e+00 | 47/48 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **11.3×** | +15.8 | 0e+00 | 48/48 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.70×** | +12.3 | 7e-33 | 44/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.95×** | +11.6 | 4e-29 | 40/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.47×** | +10.8 | 3e-25 | 41/45 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.03×** | +8.8 | 9e-17 | 45/47 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.08×** | +8.4 | 2e-15 | 30/42 (NCI-H1792, NCI-H23, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.96×** | +8.4 | 4e-15 | 34/47 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.81×** | +7.4 | 8e-12 | 34/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.80×** | +7.3 | 1e-11 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.80×** | +7.3 | 1e-11 | 32/48 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.77×** | +7.1 | 5e-11 | 35/47 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.64×** | +6.2 | 3e-08 | 31/45 (NCI-H1792, HT-29, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.61×** | +5.7 | 5e-07 | 31/47 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.30×** | +5.4 | 2e-06 | 34/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.19×** | +5.1 | 1e-05 | 26/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.18×** | +5.1 | 1e-05 | 28/47 (A498, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **2.00×** | +4.5 | 2e-04 | 24/46 (Hs 766T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +4.4 | 2e-04 | 22/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.92×** | +4.2 | 5e-04 | 24/47 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.2 | 5e-04 | 25/48 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.66×** | +4.2 | 6e-04 | 19/47 (NCI-H460, AsPC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.719×** | -3.9 | 0.052 | 23/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.590×** | -3.5 | 0.062 | 16/47 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.062 | 25/47 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.753×** | -3.4 | 0.062 | 13/47 (SNU-1, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.754×** | -3.4 | 0.062 | 19/47 (AsPC-1, C32, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.594×** | -3.4 | 0.062 | 13/47 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 0.845× | -3.0 | 0.18 | 11/48 (NCI-H23, NCI-H460, …) | top dose only | position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | 0.631× | -3.0 | 0.18 | 13/47 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.2 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +16.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.99× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 17.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +16.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.97× (z +11.8) | — |
| [[A-172 (line)]] | wt | 14.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +16.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.36× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 34.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +14.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.68× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 29.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.86× (z +12.4) | — |
| [[A549 (line)]] | wt | 16.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +15.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.59× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 16.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.92× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 14.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +14.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.04× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 23.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +14.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.12× (z +12.1) | — |
| [[J82 (line)]] | alt | 49.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.62× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.77× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 39.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.46× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.41× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 15.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +13.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.22× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 18.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.51× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +13.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.89× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +14.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.0× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 53.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 19.3× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 19.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.21× (z +9.7) | — |
| [[A498 (line)]] | wt | 21.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 17.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +13.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.98× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.60× (z +8.6) | — |
| [[KATO III (line)]] | alt | 21.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 22.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.99× (z +9.4) | — |
| [[RKO (line)]] | wt | 45.8 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 10.2× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 28.7 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.46× (z +9.7) | — |
| [[SW480 (line)]] | alt | 26.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0883× (z -10.2) |
| [[C32 (line)]] | wt | 16.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[COLO 205 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 14.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SHP-77 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.34× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.53× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRS1]] | +0.81 | +0.82 / +0.81 | both halves | 7e-06 | STRING 852 |
| [[UTP14A]] | +0.79 | +0.81 / +0.77 | both halves | 7e-06 | STRING 535 |
| [[BRIX1]] | +0.79 | +0.83 / +0.73 | both halves | 7e-06 | STRING 898 |
| [[RRP15]] | +0.79 | +0.82 / +0.80 | both halves | 7e-06 | STRING 890 |
| [[RIOK1]] | +0.78 | +0.73 / +0.81 | both halves | 7e-06 | STRING 588 |
| [[NOC3L]] | +0.78 | +0.75 / +0.80 | both halves | 7e-06 | STRING 600 |
| [[MAK16]] | +0.76 | +0.78 / +0.77 | both halves | 7e-06 | STRING 884 |
| [[BYSL]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | STRING 757 |
| [[UTP15]] | +0.75 | +0.82 / +0.75 | both halves | 7e-06 | same gene group; STRING 543 |
| [[LTV1]] | +0.74 | +0.67 / +0.81 | both halves | 7e-06 | STRING 638 |
| [[DDX10]] | +0.73 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[IFRD2]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.68 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[YPEL5]] | -0.66 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[SARAF]] | -0.63 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[LASP1]] | -0.62 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[MXD4]] | -0.62 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[PHF1]] | -0.62 | -0.71 / -0.66 | both halves | 7e-06 |  |
| [[CRELD1]] | -0.60 | -0.56 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.815). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.4, -37.6); signed map (-0.5, -42.5). **Vector** length 88.1, 25.3% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.56 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.58 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.58 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +18.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +7.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +15.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +11.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +5.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.7 | +7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -3.3 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | +3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | PAK1 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.2 — chr6:10,694,972-10,709,782 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20624, hPIP1, PIP1, bA421M1.5, MAK11, WDR84 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWT1](https://www.uniprot.org/uniprotkb/Q9NWT1) (p21-activated protein kinase-interacting protein 1):

> Negatively regulates the PAK1 kinase. PAK1 is a member of the PAK kinase family, which has been shown to play a positive role in the regulation of signaling pathways involving MAPK8 and RELA. PAK1 exists as an inactive homodimer, which is activated by binding of small GTPases such as CDC42 to an N-terminal regulatory domain. PAK1IP1 also binds to the N-terminus of PAK1, and inhibits the specific activation of PAK1 by CDC42. May be involved in ribosomal large subunit assembly.

**Summary**, from NCBI Gene [55003](https://www.ncbi.nlm.nih.gov/gene/55003):

> Predicted to enable protein kinase inhibitor activity. Involved in regulation of signal transduction by p53 class mediator and ribosomal large subunit biogenesis. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20882) · Entrez [55003](https://www.ncbi.nlm.nih.gov/gene/55003) · UniProt [Q9NWT1](https://www.uniprot.org/uniprotkb/Q9NWT1) · Ensembl [ENSG00000111845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111845)

## Data

Gene col 3291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3291); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3291]; `tensor/DDL_lfc|DDL_z.npy` [3291]; `embed/gene_vectors.npy` [3291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3291 or target_col == 3291). Every well: [[PAK1IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAK1IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
