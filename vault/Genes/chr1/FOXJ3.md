---
symbol: "FOXJ3"
type: "gene"
col: 12688
ensembl_id: "ENSG00000198815"
name: "forkhead box J3"
location: "1p34.2"
module: 168
arm: "+"
pooled_cpm: 220.74
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# FOXJ3

*forkhead box J3* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 5.32× (z +15.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.327× (z -19.2, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.778× (z -6.3, q 3e-08, down in 29 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX1]] (+0.77, fdr 7e-06), [[MED17]] (+0.70, fdr 7e-06), [[SNRPA1]] (+0.68, fdr 7e-06); moves opposite to [[BRPF3]] (-0.64, fdr 3e-05), [[AKT1S1]] (-0.63, fdr 1e-04), [[LZIC]] (-0.62, fdr 5e-05).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RASEF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **5.32×** | +15.6 | 0e+00 | 47/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **5.29×** | +15.5 | 0e+00 | 48/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +8.1 | 1e-13 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.5 | 1e-08 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.4 | 6e-06 | 29/38 (NCI-H1573, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 3e-05 | 32/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 9e-04 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.024 | 24/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.6 | 0.024 | 25/47 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12688.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.327×** | -19.2 | 0e+00 | 43/44 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.377×** | -17.4 | 0e+00 | 47/49 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -6.5 | 2e-08 | 40/47 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -6.3 | 3e-08 | 29/49 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.758×** | -4.9 | 9e-05 | 30/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.763×** | -4.8 | 1e-04 | 38/48 (SW 1271, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.3 | 0.001 | 24/48 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.821×** | -3.4 | 0.048 | 25/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.837× | -3.2 | 0.086 | 22/48 (A549, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.837× | -3.2 | 0.086 | 20/48 (C32, NCI-H2347, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.841× | -3.1 | 0.093 | 18/48 (NCI-H2030, SW 900, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.885× | -3.1 | 0.093 | 14/48 (HOP62, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 389 | 2 | 8 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 9.51× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -23.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.332× (z -12.1) |
| [[PANC-1 (line)]] | alt | 242 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -15.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 235 | 6 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.73× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -12.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 206 | 6 (1 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.99× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -20.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 142 | 2 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 7.16× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.632× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 277 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.68× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 215 | 2 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.97× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.648× (z -10.1) |
| [[HOP62 (line)]] | alt | 266 | 2 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 8.00× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.596× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 219 | 3 (2 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.84× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.51× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -16.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 194 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 6.03× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 184 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 8.45× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 225 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.38× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 240 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.21× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 182 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.48× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 298 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.66× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.521× (z -9.3) |
| [[A-427 (line)]] | wt | 199 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.30× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -13.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 166 | 2 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.19× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -12.1) |
| [[C-33 A (line)]] | alt | 222 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.68× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -12.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 192 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.18× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -11.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 208 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 7.40× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -12.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 191 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.40× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 288 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 7.54× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 239 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 7.82× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -14.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 281 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.55× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -22.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 160 | 3 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.03× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.14× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.500× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 207 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.64× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -13.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 248 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.59× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -18.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 168 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.22× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -16.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 185 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.81× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -16.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 210 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.87× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -11.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 180 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.98× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -15.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 205 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.49× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 219 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.14× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -13.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 238 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.20× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 148 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.41× (z +13.7) | — |
| [[RKO (line)]] | wt | 290 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.27× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -17.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 314 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.86× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 269 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.51× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 158 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0876× (z -14.4) ⚠ transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.228× (z -8.7) |
| [[SW 900 (line)]] | alt | 210 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.00× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -13.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 239 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -11.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 319 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.63× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 233 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.91× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -15.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 220 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.74× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 229 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 208 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 232 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX1]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[MED17]] | +0.70 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[SNRPA1]] | +0.68 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[PMS2P3]] | +0.67 | +0.78 / +0.48 | both halves | 2e-05 |  |
| [[PMS2P3-1]] | +0.67 | +0.82 / +0.51 | both halves | 1e-05 |  |
| [[ALG9]] | +0.67 | +0.78 / +0.47 | both halves | 2e-05 |  |
| [[MMS19]] | +0.66 | +0.79 / +0.39 | both halves | 6e-05 |  |
| [[RNF4]] | +0.66 | +0.83 / +0.47 | both halves | 2e-05 |  |
| [[USP3]] | +0.65 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[SEC11A]] | +0.64 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[RYK]] | +0.63 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[NUDT21]] | +0.63 | +0.74 / +0.57 | both halves | 8e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRPF3]] | -0.64 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.63 | -0.76 / -0.35 | both halves | 1e-04 |  |
| [[LZIC]] | -0.62 | -0.73 / -0.40 | both halves | 5e-05 |  |
| [[ANKLE2]] | -0.61 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[TIA1]] | -0.59 | -0.72 / -0.36 | both halves | 1e-04 |  |
| [[SLC9A8]] | -0.59 | -0.68 / -0.39 | both halves | 6e-05 |  |
| [[GGPS1]] | -0.59 | -0.72 / -0.40 | both halves | 5e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.73 / -0.28 | both halves | 3e-04 |  |
| [[NOTCH2NLB]] | -0.58 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[SCAF1]] | -0.58 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.58 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[KRBOX5]] | -0.57 | -0.69 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASEF]] | B | RASEF activity lowers FOXJ3's level | lines that do not express RASEF (20) vs lines expressing it (30) | 1.10× higher at baseline in the lines without RASEF | 0.073 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[P3H3]] | B | P3H3 activity raises FOXJ3's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.19× lower at baseline in the lines without P3H3 | 0.088 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.0, -13.7); signed map (-34.5, -9.9). **Vector** length 101, 37.1% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.1 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +15.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +5.2 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.5 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.8 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box J3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,176,539-42,335,877 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1041 |
| Gene groups (HGNC) | Forkhead boxes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPW0](https://www.uniprot.org/uniprotkb/Q9UPW0) (Forkhead box protein J3):

> Transcriptional activator of MEF2C involved in the regulation of adult muscle fiber type identity and skeletal muscle regeneration (By similarity). Plays an important role in spermatogenesis (By similarity). Required for the survival of spermatogonia and participates in spermatocyte meiosis (By similarity).

**Summary**, from NCBI Gene [22887](https://www.ncbi.nlm.nih.gov/gene/22887):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and sequence-specific double-stranded DNA binding activity. Involved in positive regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29178) · Entrez [22887](https://www.ncbi.nlm.nih.gov/gene/22887) · UniProt [Q9UPW0](https://www.uniprot.org/uniprotkb/Q9UPW0) · Ensembl [ENSG00000198815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198815)

## Data

Gene col 12688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12688); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12688]; `tensor/DDL_lfc|DDL_z.npy` [12688]; `embed/gene_vectors.npy` [12688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12688 or target_col == 12688). Every well: [[FOXJ3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXJ3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
