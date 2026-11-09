---
symbol: "MTF2"
type: "gene"
col: 6671
ensembl_id: "ENSG00000143033"
name: "metal response element binding transcription factor 2"
location: "1p22.1"
module: 65
arm: "+"
pooled_cpm: 117.74
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# MTF2

*metal response element binding transcription factor 2* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.57× (z +16.1, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.16× (z +14.6, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.317× (z -18.9, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Esmolol (hydrochloride) (drug)]] 5 µM: 0.814× (z -3.5, q 0.047, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC34]] (+0.70, fdr 1e-05), [[CTDSPL2]] (+0.67, fdr 7e-06), [[MALSU1]] (+0.66, fdr 8e-06); moves opposite to [[PEPD]] (-0.65, fdr 7e-06), [[DESI1]] (-0.63, fdr 1e-05), [[CEP170B]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +16.1 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.41×** | +15.0 | 0e+00 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.16×** | +14.6 | 0e+00 | 48/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.88×** | +12.1 | 2e-31 | 46/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.93×** | +10.7 | 9e-25 | 46/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.51×** | +9.9 | 4e-21 | 32/48 (RKO, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.69×** | +8.9 | 4e-17 | 41/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.68×** | +8.8 | 6e-17 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.50×** | +6.9 | 4e-10 | 40/48 (LoVo, A-172, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.38×** | +5.3 | 8e-06 | 31/47 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.34×** | +5.0 | 3e-05 | 38/48 (NCI-H1573, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.34×** | +5.0 | 3e-05 | 26/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.6 | 2e-04 | 28/48 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +4.6 | 2e-04 | 27/48 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.008 | 26/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.037 | 17/48 (NCI-H2030, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.317×** | -18.9 | 0e+00 | 42/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.396×** | -12.4 | 9e-33 | 45/49 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -10.7 | 1e-24 | 40/45 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.814×** | -3.5 | 0.047 | 24/48 (LS 180, AsPC-1, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.814×** | -3.5 | 0.047 | 23/48 (PANC-1, MIA PaCa-2, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.815×** | -3.4 | 0.058 | 19/48 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.871× | -3.4 | 0.058 | 12/48 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.787×** | -3.2 | 0.088 | 17/47 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.833× | -3.1 | 0.11 | 20/48 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.830× | -3.1 | 0.11 | 15/49 (HT-29, LS 180, …) | top dose only | plate-row cell shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.839× | -3.0 | 0.13 | 17/48 (SW48, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 86.0 | 10 (9 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.68× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.73× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 169 | 8 (6 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 4.25× (z +20.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 9.00× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -20.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 89.3 | 8 (6 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.38× (z +19.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.59× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 82.3 | 9 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.00× (z +22.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.25× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 171 | 5 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.42× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 157 | 6 (5 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 4.57× (z +18.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.02× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -19.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 165 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.51× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -24.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 81.9 | 6 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.83× (z +18.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.45× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 122 | 4 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +14.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.22× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -17.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 125 | 4 (2 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.56× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -14.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 145 | 5 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.83× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 78.8 | 4 (3 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.71× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.16× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -17.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 149 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +20.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.05× (z +11.3) | — |
| [[SW48 (line)]] | wt | 134 | 5 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 6.75× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -14.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 79.9 | 3 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.07× (z +11.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 6.16× (z +10.0) | [[Selinexor (drug)]] 5 µM 0.398× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 127 | 4 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +12.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 153 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.80× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -20.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 141 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.73× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -11.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 124 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.83× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 136 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.77× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -16.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 97.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.73× (z +14.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.295× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 89.4 | 3 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.41× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 8.38× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 191 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.29× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 111 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.05× (z +10.1) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.305× (z -10.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 150 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.63× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 66.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +19.1) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[AsPC-1 (line)]] | alt | 89.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +12.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 177 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.34× (z +9.0) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 72.2 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.68× (z +11.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HepG2_C3A (line)]] | wt | 91.4 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.01× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.70× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 178 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -13.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 48.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.43× (z +8.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -8.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 58.6 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.72× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 89.4 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.79× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.44× (z +11.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 229 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 89.6 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 12.7× (z +10.6) | — |
| [[CHP-212 (line)]] | wt | 73.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 68.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.44× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 98.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.60× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.55× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -10.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 87.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC34]] | +0.70 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[CTDSPL2]] | +0.67 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.66 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[SASS6]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[RNF145]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[ORC4]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[HPF1]] | +0.64 | +0.28 / +0.68 | both halves | 3e-04 |  |
| [[CENPW]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NUP54]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CHEK2]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MIS18BP1]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEPD]] | -0.65 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[DESI1]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[CEP170B]] | -0.61 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[ZPR1]] | -0.60 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[ELK4]] | -0.59 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[FLII]] | -0.59 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[LTO1]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SH3BP5-AS1]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CHMP3]] | -0.58 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.1, -38.2); signed map (-44.6, -35.6). **Vector** length 99.6, 36.7% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.6 | +5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.4 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.8 | +8.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -10.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +3.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | metal response element binding transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:93,079,235-93,139,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | M96, PCL2, TDRD19A |
| Gene groups (HGNC) | PHD finger proteins; Tudor domain containing |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 2 pathways, smallest: PRC2 methylates histones and DNA; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y483](https://www.uniprot.org/uniprotkb/Q9Y483) (Metal-response element-binding transcription factor 2):

> Polycomb group (PcG) protein that specifically binds histone H3 trimethylated at 'Lys-36' (H3K36me3) and recruits the PRC2 complex, thus enhancing PRC2 H3K27me3 methylation activity. Regulates the transcriptional networks during embryonic stem cell self-renewal and differentiation (By similarity). Promotes recruitment of the PRC2 complex to the inactive X chromosome in differentiating XX ES cells and PRC2 recruitment to target genes in undifferentiated ES cells (By similarity). Required to …

**Summary**, from NCBI Gene [22823](https://www.ncbi.nlm.nih.gov/gene/22823):

> Enables transcription corepressor binding activity. Predicted to be involved in several processes, including negative regulation of gene expression, epigenetic; segment specification; and stem cell population maintenance. Predicted to act upstream of or within cellular response to leukemia inhibitory factor. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29535) · Entrez [22823](https://www.ncbi.nlm.nih.gov/gene/22823) · UniProt [Q9Y483](https://www.uniprot.org/uniprotkb/Q9Y483) · Ensembl [ENSG00000143033](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143033)

## Data

Gene col 6671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6671); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6671]; `tensor/DDL_lfc|DDL_z.npy` [6671]; `embed/gene_vectors.npy` [6671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6671 or target_col == 6671). Every well: [[MTF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
