---
symbol: "FBXL2"
type: "gene"
col: 7728
ensembl_id: "ENSG00000153558"
name: "F-box and leucine rich repeat protein 2"
location: "3p22.3"
module: 30
arm: "+"
pooled_cpm: 129.94
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# FBXL2

*F-box and leucine rich repeat protein 2* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.43× (z +6.8, q 6e-09, up in 31 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.319× (z -21.6, q 0e+00, down in 35 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.480× (z -20.4, q 0e+00, down in 37 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC66A3]] (+0.69, fdr 7e-06), [[GALNT11]] (+0.64, fdr 7e-06), [[DUSP18]] (+0.62, fdr 1e-05); moves opposite to [[PAN2]] (-0.55, fdr 5e-05), [[HNRNPL]] (-0.55, fdr 4e-05), [[ALDH16A1]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.43×** | +6.8 | 6e-09 | 31/40 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +6.2 | 1e-07 | 27/41 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.2 | 1e-07 | 26/41 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +6.0 | 2e-07 | 28/41 (SK-MEL-2, HCT15, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 7e-07 | 24/40 (NCI-H2030, SW480, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +4.9 | 1e-04 | 15/41 (PANC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.5 | 5e-04 | 21/41 (SHP-77, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.26×** | +4.5 | 5e-04 | 27/41 (C-33 A, C32, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.18× | +4.5 | 5e-04 | 10/42 (PANC-1, SW480, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +3.8 | 0.008 | 18/41 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.008 | 21/41 (A-427, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +3.7 | 0.008 | 20/41 (H4, LoVo, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.010 | 14/42 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.011 | 17/43 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.012 | 15/42 (SW480, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.012 | 20/42 (SHP-77, A498, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.014 | 15/42 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | 1.20× | +3.4 | 0.023 | 16/40 (A498, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.319×** | -21.6 | 0e+00 | 35/39 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.350×** | -20.7 | 0e+00 | 40/42 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.480×** | -20.4 | 0e+00 | 37/42 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.504×** | -19.1 | 0e+00 | 40/41 (A549, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.508×** | -13.3 | 2e-38 | 40/41 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -12.1 | 8e-32 | 35/41 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.542×** | -11.2 | 5e-27 | 31/39 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -11.0 | 2e-26 | 36/41 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.591×** | -10.0 | 2e-21 | 32/43 (A-172, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.610×** | -9.4 | 4e-19 | 33/41 (LOX-IMVI, A549, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.659×** | -8.2 | 1e-14 | 33/41 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.754×** | -7.9 | 2e-13 | 31/41 (HOP62, SW1417, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.660×** | -7.9 | 2e-13 | 28/40 (HOP62, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -7.0 | 8e-11 | 31/42 (SNU-423, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.839× | -4.9 | 4e-05 | 17/41 (HCT15, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.052 | 13/41 (NCI-H460, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 147 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -23.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -19.5) |
| [[A-172 (line)]] | wt | 290 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -26.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.150× (z -23.6) |
| [[HOP62 (line)]] | alt | 263 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -24.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.270× (z -15.2) |
| [[SNU-423 (line)]] | alt | 168 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 152 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -21.0) |
| [[MIA PaCa-2 (line)]] | alt | 171 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.278× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 299 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.239× (z -15.6) |
| [[PANC-1 (line)]] | alt | 122 | 2 | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.86× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -17.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -16.4) |
| [[A549 (line)]] | wt | 276 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -26.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -20.1) |
| [[CFPAC-1 (line)]] | alt | 162 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -17.3) |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.240× (z -14.7) |
| [[SW480 (line)]] | alt | 108 | 1 (1 ⚠) | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.95× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.422× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 186 | 1 | 5 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.04× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 117 | 3 (1 ⚠) | 3 (2 ⚠) | [[Trametinib (drug)]] 5 µM 2.03× (z +9.4) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 1.91× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.462× (z -10.0) |
| [[SW1417 (line)]] | alt | 113 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.552× (z -9.8) |
| [[HCT15 (line)]] | alt | 158 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.233× (z -13.9) |
| [[J82 (line)]] | alt | 101 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -12.1) |
| [[LoVo (line)]] | wt | 133 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 145 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 143 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 63.0 | 2 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.61× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.178× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.324× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 99.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 184 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -17.1) |
| [[AN3 CA (line)]] | alt | 152 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 97.5 | 1 | 2 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.57× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -15.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 137 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 99.5 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.24× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 147 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 154 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 68.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 1271 (line)]] | alt | 210 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 72.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.378× (z -10.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -15.9) |
| [[BT-474 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CHP-212 (line)]] | wt | 124 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.0) |
| [[H4 (line)]] | wt | 77.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -11.4) |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC66A3]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[GALNT11]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[DUSP18]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[STARD9]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[EPS15]] | +0.58 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[MGST3]] | +0.57 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[C11orf80]] | +0.57 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[CRLF3]] | +0.57 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[PSMD9]] | +0.57 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[KLC3]] | +0.57 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[DIP2A]] | +0.56 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[FSD1L]] | +0.56 | +0.49 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAN2]] | -0.55 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[HNRNPL]] | -0.55 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[ALDH16A1]] | -0.54 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[MAGOHB]] | -0.53 | -0.64 / -0.25 | both halves | 4e-04 |  |
| [[HNRNPA2B1]] | -0.53 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ERH]] | -0.52 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[PSME3IP1]] | -0.52 | -0.61 / -0.27 | both halves | 3e-04 |  |
| [[ANAPC13]] | -0.52 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[ZNF362]] | -0.51 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[MIS12]] | -0.51 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[COX18]] | -0.50 | -0.65 / -0.23 | both halves | 5e-04 |  |
| [[MCTS1]] | -0.50 | -0.58 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FBXL2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[STARD9]] | B | STARD9 activity raises FBXL2's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 3.31× lower at baseline in the lines without STARD9 | 0.072 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[FSD1L]] | C | FSD1L activity raises FBXL2's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 8.09× lower at baseline in the lines without FSD1L | 0.002 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[CLTCL1]] | C | CLTCL1 activity raises FBXL2's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 7.60× lower at baseline in the lines without CLTCL1 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.6, -1.8); signed map (-37.9, -2.6). **Vector** length 127, 44.2% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.9 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.7 | +6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.8 | +6.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.9 | +5.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -7.4 | -19.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.5 | -13.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.6 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -11.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:33,277,025-33,403,662 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBL2, FBL3 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKC9](https://www.uniprot.org/uniprotkb/Q9UKC9) (F-box/LRR-repeat protein 2):

> Calcium-activated substrate recognition component of the SCF (SKP1-cullin-F-box protein) E3 ubiquitin-protein ligase complex, SCF(FBXL2), which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Unlike many F-box proteins, FBXL2 does not seem to target phosphodegron within its substrates but rather calmodulin-binding motifs and is thereby antagonized by calmodulin. This is the case for the cyclins CCND2 and CCND3 which polyubiquitination and subsequent …

**Summary**, from NCBI Gene [25827](https://www.ncbi.nlm.nih.gov/gene/25827):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13598) · Entrez [25827](https://www.ncbi.nlm.nih.gov/gene/25827) · UniProt [Q9UKC9](https://www.uniprot.org/uniprotkb/Q9UKC9) · Ensembl [ENSG00000153558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153558)

## Data

Gene col 7728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7728); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7728]; `tensor/DDL_lfc|DDL_z.npy` [7728]; `embed/gene_vectors.npy` [7728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7728 or target_col == 7728). Every well: [[FBXL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
