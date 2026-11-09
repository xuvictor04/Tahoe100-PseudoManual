---
symbol: "VIRMA"
type: "gene"
col: 9039
ensembl_id: "ENSG00000164944"
name: "vir like m6A methyltransferase associated"
location: "8q22.1"
module: 12
arm: "+"
pooled_cpm: 123.72
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# VIRMA

*vir like m6A methyltransferase associated* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 6.23× (z +26.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.412× (z -24.5, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.665× (z -15.9, q 0e+00, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOK2]] (+0.78, fdr 7e-06), [[DRG1]] (+0.78, fdr 7e-06), [[PPIL4]] (+0.77, fdr 7e-06); moves opposite to [[DIAPH1]] (-0.60, fdr 1e-05), [[SRPK1]] (-0.59, fdr 8e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BCAS2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.23×** | +26.5 | 0e+00 | 48/49 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.89×** | +19.7 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +12.3 | 2e-32 | 34/48 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +8.1 | 1e-13 | 31/48 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +6.3 | 5e-08 | 29/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +6.2 | 5e-08 | 30/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +5.7 | 1e-06 | 36/47 (SK-MEL-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.46×** | +5.6 | 2e-06 | 33/49 (A498, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +5.0 | 4e-05 | 22/48 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.15× | +3.9 | 0.005 | 18/48 (Panc 03.27, SW480, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.15× | +3.8 | 0.009 | 18/48 (RKO, NCI-H23, …) | top dose only | composition shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.017 | 1/48 (A-172) | rises with dose | plate-row cell shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.08× | +3.1 | 0.074 | 13/48 (NCI-H1573, Panc 03.27, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.412×** | -24.5 | 0e+00 | 46/49 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -22.3 | 0e+00 | 40/44 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -15.9 | 0e+00 | 39/49 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.654×** | -10.9 | 3e-25 | 37/45 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -10.5 | 1e-23 | 34/48 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -8.4 | 6e-15 | 36/50 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -7.2 | 6e-11 | 23/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.792×** | -6.4 | 1e-08 | 25/48 (HOP62, NCI-H2347, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.827×** | -5.2 | 1e-05 | 24/48 (HOP62, RPMI-7951, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.830×** | -5.1 | 2e-05 | 24/48 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -4.6 | 2e-04 | 0/50 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | 0.853× | -4.2 | 0.001 | 21/47 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.859× | -4.2 | 0.001 | 19/48 (HOP62, A-172, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.870× | -3.8 | 0.006 | 19/48 (SW 1088, SW1417, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.885× | -3.3 | 0.031 | 13/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.798×** | -3.2 | 0.041 | 19/48 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.890× | -3.2 | 0.049 | 12/48 (SW 1088, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 133 | 2 | 9 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 6.94× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 125 | 4 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -11.3) |
| [[HS-578T (line)]] | alt | 223 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.31× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 218 | 2 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.26× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -18.1) |
| [[NCI-H2030 (line)]] | alt | 136 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.78× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 138 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.31× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -11.3) |
| [[RKO (line)]] | wt | 171 | 4 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.3× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0531× (z -41.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -16.0) |
| [[A498 (line)]] | wt | 220 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.84× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -24.5) |
| [[H4 (line)]] | wt | 135 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.07× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 112 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -19.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 88.1 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.16× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -11.6) |
| [[SW 900 (line)]] | alt | 160 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.18× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -8.5) |
| [[A549 (line)]] | wt | 123 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 191 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.23× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -29.0) |
| [[CFPAC-1 (line)]] | alt | 114 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.36× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -13.1) |
| [[Hs 766T (line)]] | wt | 132 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.35× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -14.5) |
| [[KATO III (line)]] | alt | 119 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.36× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -15.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 127 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.19× (z +17.3) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 74.8 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.58× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.3) |
| [[A-427 (line)]] | wt | 73.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -22.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 108 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.73× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.2) |
| [[C32 (line)]] | wt | 118 | 1 | 3 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.51× (z +12.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 85.9 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.88× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.522× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 122 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.32× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -15.3) |
| [[J82 (line)]] | alt | 125 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.41× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 165 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.86× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -10.5) |
| [[SNU-423 (line)]] | alt | 88.9 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -10.8) |
| [[SW1417 (line)]] | alt | 135 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.95× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -14.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 113 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.76× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -15.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 114 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.9× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -19.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 79.1 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.9× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 99.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -27.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 147 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.09× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -24.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 103 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.45× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 86.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.78× (z +12.0) | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 2 (1 ⚠) | — | [[DT-061 (drug)]] 5 µM 0.0985× (z -9.0) |
| [[HCT15 (line)]] | alt | 134 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.84× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -9.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 89.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.47× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 78.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 13.2× (z +16.6) | — |
| [[NCI-H1792 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.28× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -10.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 95.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -10.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 75.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 72.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.1× (z +14.6) | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 116 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.16× (z +11.1) | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0618× (z -12.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOK2]] | +0.78 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[DRG1]] | +0.78 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.77 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[KBTBD7]] | +0.74 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[SNRPB2]] | +0.73 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.71 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[CINP]] | +0.70 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[RBSN]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[SDE2]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[ASB8]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[BNIP1]] | +0.70 | +0.77 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 | same gene group |
| [[SRPK1]] | -0.59 | -0.58 / -0.61 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VIRMA's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF223]] | B | ZNF223 activity raises VIRMA's level | lines that do not express ZNF223 (11) vs lines expressing it (39) | 1.26× lower at baseline in the lines without ZNF223 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZNF284, TGFB1I1, ZNF891 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises VIRMA's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PSMB5]] | B | PSMB5 activity lowers VIRMA's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAS2]] | C | VIRMA's natural level weakens BCAS2's drug response | VIRMA's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.13; direction not clear | 0.099 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.8, -7.1); signed map (-13.7, -10.3). **Vector** length 114, 34.6% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +26.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.1 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +19.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +8.1 |
|  | [[NG25 (drug)]] 5 µM |  | +5.3 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +0.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.6 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.4 | -0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.0 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -7.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | vir like m6A methyltransferase associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,487,689-94,553,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434I116, fSAP121; previously KIAA1429 |
| Gene groups (HGNC) | m6A methyltransferase complex; WTAP complex; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q69YN4](https://www.uniprot.org/uniprotkb/Q69YN4) (Protein virilizer homolog):

> Associated component of the WMM complex, a complex that mediates N6-methyladenosine (m6A) methylation of RNAs, a modification that plays a role in the efficiency of mRNA splicing and RNA processing. Acts as a key regulator of m6A methylation by promoting m6A methylation of mRNAs in the 3'-UTR near the stop codon: recruits the catalytic core components METTL3 and METTL14, thereby guiding m6A methylation at specific sites. Required for mRNA polyadenylation via its role in selective m6A …

**Summary**, from NCBI Gene [25962](https://www.ncbi.nlm.nih.gov/gene/25962):

> Enables RNA binding activity. Involved in mRNA processing. Located in RNA N6-methyladenosine methyltransferase complex and nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24500) · Entrez [25962](https://www.ncbi.nlm.nih.gov/gene/25962) · UniProt [Q69YN4](https://www.uniprot.org/uniprotkb/Q69YN4) · Ensembl [ENSG00000164944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164944)

## Data

Gene col 9039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9039); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9039]; `tensor/DDL_lfc|DDL_z.npy` [9039]; `embed/gene_vectors.npy` [9039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9039 or target_col == 9039). Every well: [[VIRMA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VIRMA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
