---
symbol: "SEC22A"
type: "gene"
col: 4279
ensembl_id: "ENSG00000121542"
name: "SEC22 homolog A, vesicle trafficking protein"
location: "3q21.1"
module: 41
arm: "+"
pooled_cpm: 146.4
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SEC22A

*SEC22 homolog A, vesicle trafficking protein* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.62× (z +9.2, q 2e-17, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.300× (z -23.0, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.578× (z -10.5, q 2e-23, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP54]] (+0.79, fdr 7e-06), [[ACBD3]] (+0.76, fdr 7e-06), [[TMEM258]] (+0.74, fdr 7e-06); moves opposite to [[PSME3]] (-0.70, fdr 7e-06), [[TOR1A]] (-0.68, fdr 7e-06), [[HNRNPK]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +9.2 | 2e-17 | 40/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +7.7 | 3e-12 | 39/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.8 | 2e-09 | 32/48 (SW1417, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +6.2 | 1e-07 | 33/48 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 2e-05 | 32/49 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.015 | 12/49 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.015 | 25/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.063 | 23/48 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.16 | 13/48 (A498, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.300×** | -23.0 | 0e+00 | 48/49 (Panc 03.27, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.302×** | -21.1 | 0e+00 | 42/45 (A-427, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.352×** | -19.2 | 0e+00 | 41/44 (H4, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.578×** | -10.5 | 2e-23 | 44/48 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.582×** | -10.3 | 5e-23 | 44/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.639×** | -8.6 | 1e-15 | 39/48 (HOP62, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.640×** | -8.5 | 1e-15 | 36/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -7.7 | 1e-12 | 38/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -7.6 | 2e-12 | 36/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.670×** | -7.3 | 1e-11 | 34/47 (SNU-423, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -7.1 | 8e-11 | 32/49 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.696×** | -6.9 | 2e-10 | 30/48 (HS-578T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -6.5 | 3e-09 | 36/48 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.702×** | -6.4 | 7e-09 | 40/48 (H4, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -6.1 | 4e-08 | 27/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.606×** | -5.0 | 2e-05 | 31/48 (RPMI-7951, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.659×** | -4.2 | 9e-04 | 26/49 (AsPC-1, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.813×** | -3.9 | 0.002 | 22/48 (KATO III, LS 180, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.865× | -3.9 | 0.002 | 14/48 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -3.7 | 0.005 | 25/48 (HS-578T, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 196 | 0 | 18 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -15.6) |
| [[H4 (line)]] | wt | 212 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0236× (z -38.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.212× (z -16.6) |
| [[HS-578T (line)]] | alt | 292 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -14.9) |
| [[SW480 (line)]] | alt | 104 | 3 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +12.6) | [[Digitoxin (drug)]] 0.5 µM 0.290× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 179 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -19.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 106 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.363× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.406× (z -12.1) |
| [[SNU-423 (line)]] | alt | 107 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -17.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.296× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 196 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.251× (z -17.5) |
| [[J82 (line)]] | alt | 133 | 1 | 6 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.05× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.410× (z -11.3) |
| [[A-172 (line)]] | wt | 127 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.321× (z -13.2) |
| [[C32 (line)]] | wt | 87.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -17.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 194 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.94× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 180 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 225 | 1 | 5 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.89× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.319× (z -8.7) |
| [[SW1417 (line)]] | alt | 155 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -13.7) |
| [[A498 (line)]] | wt | 147 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.453× (z -11.3) |
| [[Hs 766T (line)]] | wt | 181 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.451× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -9.3) |
| [[LS 180 (line)]] | wt | 161 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0705× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.347× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 177 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.442× (z -8.7) |
| [[PANC-1 (line)]] | alt | 148 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.239× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -9.0) |
| [[A549 (line)]] | wt | 153 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.470× (z -8.7) |
| [[BT-474 (line)]] | alt | 137 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 143 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 195 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.309× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 76.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -9.6) |
| [[SW 900 (line)]] | alt | 117 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.411× (z -9.0) |
| [[A-427 (line)]] | wt | 163 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -22.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 105 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.395× (z -10.6) |
| [[HT-29 (line)]] | alt | 155 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -12.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 121 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -15.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 94.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 97.8 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -14.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 124 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -11.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 220 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 167 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 94.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.478× (z -8.5) |
| [[COLO 205 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -11.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -16.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54]] | +0.79 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.76 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.74 | +0.77 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[GOLPH3L]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[GBF1]] | +0.73 | +0.68 / +0.62 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SLC17A5]] | +0.73 | +0.59 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SSR2]] | +0.71 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | +0.71 | +0.61 / +0.76 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MINDY2]] | +0.71 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.70 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ABHD18]] | +0.70 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[TULP3]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.70 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[TOR1A]] | -0.68 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.67 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.67 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[CCT5]] | -0.66 | -0.69 / -0.70 | both halves | 7e-06 |  |
| [[PRRC2B]] | -0.65 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.65 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[TMX3]] | -0.64 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[ZNF300]] | -0.64 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[PPP2CA]] | -0.63 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SEC22A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SEC22A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.4, -35.1); signed map (-48.8, 12.9). **Vector** length 154, 59.1% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.50 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +6.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +4.3 | +2.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +3.9 | +3.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.8 | +2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.5 | +3.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.7 | -21.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.7 | -10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.7 | -19.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.6 | -8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.2 | -6.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.9 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SEC22 homolog A, vesicle trafficking protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:123,201,927-123,274,136 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SEC22L2 |
| Gene groups (HGNC) | SNAREs |
| Reactome | 6 pathways, smallest: COPII-mediated vesicle transport; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IW7](https://www.uniprot.org/uniprotkb/Q96IW7) (Vesicle-trafficking protein SEC22a):

> May be involved in vesicle transport between the ER and the Golgi complex.

**Summary**, from NCBI Gene [26984](https://www.ncbi.nlm.nih.gov/gene/26984):

> The protein encoded by this gene belongs to the member of the SEC22 family of vesicle trafficking proteins. This protein has similarity to rat SEC22 and may act in the early stages of the secretory pathway. [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:20260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20260) · Entrez [26984](https://www.ncbi.nlm.nih.gov/gene/26984) · UniProt [Q96IW7](https://www.uniprot.org/uniprotkb/Q96IW7) · Ensembl [ENSG00000121542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121542)

## Data

Gene col 4279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4279); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4279]; `tensor/DDL_lfc|DDL_z.npy` [4279]; `embed/gene_vectors.npy` [4279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4279 or target_col == 4279). Every well: [[SEC22A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC22A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
