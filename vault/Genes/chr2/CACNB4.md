---
symbol: "CACNB4"
type: "gene"
col: 11283
ensembl_id: "ENSG00000182389"
name: "calcium voltage-gated channel auxiliary subunit beta 4"
location: "2q23.3"
module: 134
arm: "+"
pooled_cpm: 50.25
n_lines_expressing: 42
n_dd_up: 16
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# CACNB4

*calcium voltage-gated channel auxiliary subunit beta 4* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.83× (z +17.4, q 0e+00, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.487× (z -20.7, q 0e+00, down in 30 of 39 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.444× (z -15.9, q 0e+00, down in 34 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDK2]] (+0.67, fdr 7e-06), [[FAM210A]] (+0.62, fdr 1e-05), [[LINC03009-1]] (+0.59, fdr 1e-05); moves opposite to [[TMEM254]] (-0.54, fdr 2e-05), [[ZNF252P]] (-0.52, fdr 3e-05), [[ZNF214]] (-0.52, fdr 4e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PANTR1]] → it (grade B ⚠); 6 go from it, the strongest it → cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +17.4 | 0e+00 | 32/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +17.3 | 0e+00 | 32/39 (HOP62, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.26×** | +16.6 | 0e+00 | 33/40 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +9.4 | 1e-18 | 25/40 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +7.8 | 9e-13 | 18/32 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +7.7 | 2e-12 | 18/39 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 4e-08 | 19/39 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.4 | 5e-06 | 19/40 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 1e-04 | 13/41 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +4.3 | 9e-04 | 14/40 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.23×** | +4.0 | 0.003 | 15/40 (A549, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.20× | +3.7 | 0.012 | 6/40 (HepG2/C3A, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.013 | 12/40 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.015 | 12/38 (LoVo, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.016 | 6/40 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.024 | 13/40 (J82, HCT15, …) | rises with dose |  |
| [[Baicalin (drug)]] 5 µM |  | 1.12× | +3.2 | 0.042 | 1/41 (HEC-1-A) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.057 | 9/38 (A-172, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.057 | 15/41 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.487×** | -20.7 | 0e+00 | 30/39 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.444×** | -15.9 | 0e+00 | 34/39 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.575×** | -11.3 | 3e-27 | 27/39 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.597×** | -10.5 | 1e-23 | 27/39 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -10.0 | 2e-21 | 22/40 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -10.0 | 2e-21 | 23/35 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -8.3 | 1e-14 | 23/38 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.558×** | -6.2 | 4e-08 | 17/41 (LoVo, HCT15, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.773×** | -5.1 | 3e-05 | 20/39 (C-33 A, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **0.775×** | -5.0 | 3e-05 | 17/28 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.786×** | -4.9 | 5e-05 | 20/37 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.800×** | -4.6 | 2e-04 | 18/39 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.859× | -4.4 | 5e-04 | 11/40 (SW 1271, NCI-H2347, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.666×** | -4.3 | 6e-04 | 14/39 (NCI-H1792, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.818×** | -4.1 | 0.001 | 14/39 (SNU-1, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.829×** | -3.8 | 0.004 | 19/40 (Hs 766T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -3.8 | 0.005 | 14/38 (HEC-1-A, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.752×** | -3.1 | 0.061 | 9/37 (MIA PaCa-2, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.868× | -2.9 | 0.092 | 5/39 (AN3 CA, CHP-212, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.869× | -2.9 | 0.092 | 7/40 (A-427, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 583 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -22.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.172× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 92.6 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -29.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -20.2) |
| [[C-33 A (line)]] | alt | 247 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0928× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.222× (z -13.2) |
| [[LoVo (line)]] | wt | 133 | 3 (1 ⚠) | 6 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.81× (z +10.6) ⚠ unreliable plate only · without an alert: [[Belinostat (drug)]] 0.5 µM 2.50× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -15.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.340× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 286 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -23.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.234× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 62.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -19.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -10.4) |
| [[SW480 (line)]] | alt | 54.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 78.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -26.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.155× (z -17.1) |
| [[C32 (line)]] | wt | 76.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -14.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.131× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 30.9 | 3 | 2 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +10.7) | [[Harringtonine (drug)]] 5 µM 0.180× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 14.9 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.08× (z +14.2) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.103× (z -8.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 237 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 75.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -17.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 19.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.89× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 29.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.72× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 91.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -14.0) |
| [[PANC-1 (line)]] | alt | 16.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.13× (z +13.8) | — |
| [[A-427 (line)]] | wt | 24.9 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.95× (z +10.6) | — |
| [[J82 (line)]] | alt | 16.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.28× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.04× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.43× (z +9.2) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 29.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.76× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 14.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.87× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 14.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.14× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -10.0) ⚠ toxic |
| [[H4 (line)]] | wt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 67.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.93× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0677× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.138× (z -9.2) |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.166× (z -9.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 12.8 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.0724× (z -9.1) |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.68 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.91 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDK2]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LINC03009-1]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[HK1]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[VDAC1]] | +0.57 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[RIMKLA]] | +0.56 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[DDHD1]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SLC47A1]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CRYBB2P1-1]] | +0.55 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[REEP1]] | +0.55 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[JAKMIP1]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SCD5]] | +0.55 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM254]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZNF252P]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ZNF214]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ATG2B]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MKS1]] | -0.49 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[MAT2B]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ZZEF1]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SMARCE1]] | -0.48 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[SENP6]] | -0.48 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[RC3H2]] | -0.47 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TAF9]] | -0.46 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SCAF8]] | -0.46 | -0.30 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PANTR1]] | B | PANTR1 activity raises CACNB4's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 1.92× lower at baseline in the lines without PANTR1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | B | CACNB4 activity raises the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (protects the cells) | lines that do not express CACNB4 (8) vs lines expressing it (40) | the lines without CACNB4: 0.88× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| [[SCD5]] | B | CACNB4 activity raises SCD5's level | lines that do not express CACNB4 (8) vs lines expressing it (42) | 3.53× lower at baseline in the lines without CACNB4 | 0.039 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| [[CERK]] | B | CACNB4 activity raises CERK's level | lines that do not express CACNB4 (8) vs lines expressing it (42) | 1.27× lower at baseline in the lines without CACNB4 | 0.045 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| [[ZNF483]] | B | CACNB4 activity raises ZNF483's level | lines that do not express CACNB4 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without CACNB4 | 0.065 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| [[HAGLR]] | B | CACNB4 activity raises HAGLR's level | lines that do not express CACNB4 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without CACNB4 | 0.074 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM | B | CACNB4 activity raises the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (protects the cells) | lines that do not express CACNB4 (8) vs lines expressing it (40) | the lines without CACNB4: 0.87× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.7, -19.5); signed map (-41.7, 25.0). **Vector** length 101, 22.7% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.5 | +17.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +17.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.6 | +16.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.5 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.8 | +7.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.1 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -15.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.6 | -20.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -10.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit beta 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:151,832,771-152,099,167 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EJM4 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; Calcium voltage-gated channel auxiliary beta subunits; SH3 domain containing |
| Reactome | 7 pathways, smallest: Presynaptic depolarization and calcium channel opening; NCAM1 interactions; NCAM signaling for neurite out-growth |
| Matched by | ensembl_id |

**Function**, from UniProt [O00305](https://www.uniprot.org/uniprotkb/O00305) (Voltage-dependent L-type calcium channel subunit beta-4):

> The beta subunit of voltage-dependent calcium channels contributes to the function of the calcium channel by increasing peak calcium current, shifting the voltage dependencies of activation and inactivation, modulating G protein inhibition and controlling the alpha-1 subunit membrane targeting.

**Summary**, from NCBI Gene [785](https://www.ncbi.nlm.nih.gov/gene/785):

> This gene encodes a member of the beta subunit family of voltage-dependent calcium channel complex proteins. Calcium channels mediate the influx of calcium ions into the cell upon membrane polarization and consist of a complex of alpha-1, alpha-2/delta, beta, and gamma subunits in a 1:1:1:1 ratio. Various versions of each of these subunits exist, either expressed from similar genes or the result of alternative splicing. The protein encoded by this locus plays an important role in calcium …

**Accessions** — [HGNC:1404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1404) · Entrez [785](https://www.ncbi.nlm.nih.gov/gene/785) · UniProt [O00305](https://www.uniprot.org/uniprotkb/O00305) · Ensembl [ENSG00000182389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182389)

## Data

Gene col 11283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11283); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11283]; `tensor/DDL_lfc|DDL_z.npy` [11283]; `embed/gene_vectors.npy` [11283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11283 or target_col == 11283). Every well: [[CACNB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
