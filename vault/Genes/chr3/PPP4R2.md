---
symbol: "PPP4R2"
type: "gene"
col: 8726
ensembl_id: "ENSG00000163605"
name: "protein phosphatase 4 regulatory subunit 2"
location: "3p13"
module: 12
arm: "+"
pooled_cpm: 171.07
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PPP4R2

*protein phosphatase 4 regulatory subunit 2* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +36.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.457× (z -22.4, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.663× (z -17.3, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.80, fdr 7e-06), [[COIL]] (+0.76, fdr 7e-06), [[PHAX]] (+0.75, fdr 7e-06); moves opposite to [[ZNF731P]] (-0.68, fdr 7e-06), [[BCAP31]] (-0.67, fdr 7e-06), [[UFD1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +36.4 | 0e+00 | 48/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **7.41×** | +31.1 | 0e+00 | 49/49 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.19×** | +22.4 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.16×** | +22.1 | 0e+00 | 48/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +19.8 | 0e+00 | 47/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +14.1 | 6e-43 | 43/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +10.0 | 1e-21 | 40/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +8.5 | 2e-15 | 33/47 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +7.5 | 5e-12 | 30/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +7.4 | 9e-12 | 33/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +7.1 | 8e-11 | 32/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +6.4 | 9e-09 | 27/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.20×** | +5.4 | 2e-06 | 22/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.33×** | +4.4 | 4e-04 | 24/48 (SK-MEL-2, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.16× | +4.2 | 0.001 | 16/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.013 | 19/48 (HEC-1-A, SW480, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.095 | 5/48 (HOP62, NCI-H2030, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -22.4 | 0e+00 | 44/44 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.502×** | -20.5 | 0e+00 | 49/49 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -17.3 | 0e+00 | 44/49 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.626×** | -12.9 | 9e-36 | 37/45 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.683×** | -11.3 | 1e-27 | 41/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.719×** | -9.8 | 1e-20 | 37/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.763×** | -8.0 | 7e-14 | 36/48 (SW480, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.805×** | -6.2 | 4e-08 | 25/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.823×** | -5.8 | 4e-07 | 22/48 (COLO 205, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.829×** | -5.6 | 1e-06 | 24/48 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.821×** | -5.4 | 3e-06 | 23/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.832×** | -5.3 | 6e-06 | 24/50 (HEC-1-A, SW480, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.867× | -4.3 | 9e-04 | 10/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.905× | -4.2 | 9e-04 | 16/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.913× | -3.8 | 0.005 | 2/48 (H4, NCI-H661) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.891× | -3.4 | 0.021 | 5/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.893× | -3.4 | 0.023 | 8/48 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.895× | -3.2 | 0.045 | 8/47 (NCI-H23, RPMI-7951, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.899× | -3.2 | 0.045 | 2/48 (LOX-IMVI, NCI-H1792) | inconsistent across doses |  |
| [[Almonertinib (hydrochloride) (drug)]] 0.5 µM |  | 0.900× | -3.2 | 0.045 | 6/48 (CHP-212, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 254 | 7 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +33.7) | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -29.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -19.2) |
| [[LoVo (line)]] | wt | 185 | 11 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.1× (z +26.3) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -20.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 205 | 9 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +26.7) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -21.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 124 | 9 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +37.5) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -13.2) |
| [[SW480 (line)]] | alt | 204 | 3 | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 9.17× (z +28.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -19.9) |
| [[A549 (line)]] | wt | 159 | 7 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +33.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -20.4) |
| [[C32 (line)]] | wt | 179 | 7 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.8) |
| [[HOP62 (line)]] | alt | 176 | 6 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 203 | 5 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 132 | 8 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +32.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -16.8) |
| [[SW1417 (line)]] | alt | 259 | 5 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +23.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -13.1) |
| [[HS-578T (line)]] | alt | 157 | 6 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +20.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -11.8) |
| [[A-172 (line)]] | wt | 154 | 7 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +26.4) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -31.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -13.7) |
| [[A498 (line)]] | wt | 129 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +29.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -15.9) |
| [[HT-29 (line)]] | alt | 138 | 3 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.51× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.507× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 146 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +18.4) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 196 | 7 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.5× (z +20.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.444× (z -11.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 166 | 4 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 216 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -12.2) |
| [[SNU-1 (line)]] | wt | 206 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -16.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 203 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +21.1) | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -11.5) |
| [[J82 (line)]] | alt | 188 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +25.4) | [[Dinaciclib (drug)]] 5 µM 0.613× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 170 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.74× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 261 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +22.2) | [[Dinaciclib (drug)]] 5 µM 0.510× (z -13.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 177 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.665× (z -9.2) |
| [[A-427 (line)]] | wt | 117 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.80× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -17.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 112 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -13.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 106 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.8) | — |
| [[Panc 03.27 (line)]] | alt | 275 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.479× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -9.1) |
| [[RKO (line)]] | wt | 208 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -14.2) |
| [[SNU-423 (line)]] | alt | 174 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +26.9) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -11.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 152 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -12.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 140 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -12.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 220 | 4 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.60× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 88.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +21.3) | — |
| [[NCI-H23 (line)]] | alt | 156 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.76× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -11.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 210 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.95× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -11.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 127 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.7) |
| [[BT-474 (line)]] | alt | 107 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +19.1) | — |
| [[HepG2_C3A (line)]] | wt | 245 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -12.1) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.2) |
| [[KATO III (line)]] | alt | 141 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +18.8) | — |
| [[AN3 CA (line)]] | alt | 240 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.5) |
| [[SHP-77 (line)]] | alt | 123 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.93× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -14.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 204 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.0) | — |
| [[H4 (line)]] | wt | 97.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.374× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 166 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.80 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[COIL]] | +0.76 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[PHAX]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.73 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[MRPS33]] | +0.71 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PEX12]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MIER1]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.69 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[CLK4]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.68 | +0.51 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.68 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[BCAP31]] | -0.67 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[UFD1]] | -0.66 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.60 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[PLOD3]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.59 | -0.39 / -0.64 | both halves | 5e-05 |  |
| [[PIGN]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PPP4R2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises PPP4R2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WHRN]] | C | WHRN activity raises PPP4R2's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.5, 3.3); signed map (1.6, -19.6). **Vector** length 105, 34.9% of its response variance represented; |z| ≥ 3 in 1,344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.6 | +14.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.8 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +19.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.0 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.2 | +7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -6.1 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | +2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.5 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.2 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | +0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | +0.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.3 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 4 regulatory subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p13 — chr3:72,996,803-73,069,198 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Protein phosphatase 4 regulatory subunits |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 5 pathways, smallest: Processing of DNA double-strand break ends; HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA); Homology Directed Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY27](https://www.uniprot.org/uniprotkb/Q9NY27) (Serine/threonine-protein phosphatase 4 regulatory subunit 2):

> Regulatory subunit of serine/threonine-protein phosphatase 4 (PP4). May regulate the activity of PPP4C at centrosomal microtubule organizing centers. Its interaction with the SMN complex leads to enhance the temporal localization of snRNPs, suggesting a role of PPP4C in maturation of spliceosomal snRNPs. The PPP4C-PPP4R2-PPP4R3A PP4 complex specifically dephosphorylates H2AX phosphorylated on 'Ser-140' (gamma-H2AX) generated during DNA replication and required for DNA double strand break …

**Summary**, from NCBI Gene [151987](https://www.ncbi.nlm.nih.gov/gene/151987):

> The protein encoded by this gene is a regulatory subunit of the serine/threonine-protein phosphatase 4 complex. In addition to being required for efficient DNA double strand break repair, this complex plays a role in organization of microtubules at centrosomes and processing of spliceosomal snRNPs. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:18296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18296) · Entrez [151987](https://www.ncbi.nlm.nih.gov/gene/151987) · UniProt [Q9NY27](https://www.uniprot.org/uniprotkb/Q9NY27) · Ensembl [ENSG00000163605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163605)

## Data

Gene col 8726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8726); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8726]; `tensor/DDL_lfc|DDL_z.npy` [8726]; `embed/gene_vectors.npy` [8726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8726 or target_col == 8726). Every well: [[PPP4R2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP4R2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
