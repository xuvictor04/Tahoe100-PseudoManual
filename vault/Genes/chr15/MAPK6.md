---
symbol: "MAPK6"
type: "gene"
col: 930
ensembl_id: "ENSG00000069956"
name: "mitogen-activated protein kinase 6"
location: "15q21.2"
module: 133
arm: "+"
pooled_cpm: 149.17
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# MAPK6

*mitogen-activated protein kinase 6* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +17.0, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.787× (z -4.9, q 7e-04, down in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~16% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H1573 0.303×, C-33 A 0.280×, LoVo 0.408×, HT-29 0.426×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0963×, KATO III 0.480×, HT-29 0.539×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.298×, HT-29 0.560×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.392×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1088 0.112×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAFG]] (+0.62, fdr 2e-05), [[NRSN2-AS1]] (+0.62, fdr 3e-05), [[CLIP1]] (+0.61, fdr 1e-05); moves opposite to [[CASP2]] (-0.62, fdr 4e-05), [[SKP2]] (-0.57, fdr 1e-04), [[SHMT1]] (-0.55, fdr 1e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPINK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +17.0 | 0e+00 | 40/48 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.22×** | +16.1 | 0e+00 | 48/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +15.8 | 0e+00 | 48/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +13.3 | 3e-38 | 40/48 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +11.8 | 6e-30 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.76×** | +11.4 | 4e-28 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +11.1 | 1e-26 | 42/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +10.5 | 7e-24 | 45/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +10.3 | 7e-23 | 46/48 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +10.1 | 3e-22 | 33/49 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.50×** | +9.7 | 2e-20 | 43/49 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +9.3 | 8e-19 | 43/48 (LoVo, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +8.3 | 3e-15 | 46/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +6.8 | 4e-10 | 40/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.39×** | +6.6 | 2e-09 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.4 | 5e-09 | 31/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +5.2 | 7e-06 | 25/49 (CFPAC-1, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 930.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H1573 0.303×, C-33 A 0.280×, LoVo 0.408×, HT-29 0.426×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0963×, KATO III 0.480×, HT-29 0.539×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.298×, HT-29 0.560×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.392×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1088 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.787×** | -4.9 | 7e-04 | 29/48 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.819×** | -3.9 | 0.026 | 24/44 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.837× | -3.6 | 0.056 | 20/48 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | 0.833× | -3.4 | 0.082 | 21/45 (A-427, KATO III, …) | all doses, flat | composition shift |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.847× | -3.4 | 0.082 | 17/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.745× | -3.1 | 0.16 | 19/47 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 0.890× | -3.1 | 0.18 | 6/49 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 304 | 6 (2 ⚠) | 6 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 174 | 12 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.92× (z +23.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +22.9) | — |
| [[NCI-H1573 (line)]] | alt | 205 | 10 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.85× (z +20.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.83× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -14.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 188 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +21.5) | — |
| [[SW 900 (line)]] | alt | 126 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +16.4) | — |
| [[BT-474 (line)]] | alt | 140 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 133 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +17.3) | — |
| [[LoVo (line)]] | wt | 210 | 7 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.28× (z +12.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 1.89× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -13.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 169 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +18.6) | — |
| [[SW480 (line)]] | alt | 106 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +19.1) | — |
| [[COLO 205 (line)]] | alt | 170 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +23.4) | — |
| [[hTERT-HPNE (line)]] | wt | 157 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 124 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.5) | — |
| [[H4 (line)]] | wt | 130 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 148 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.9) | — |
| [[J82 (line)]] | alt | 138 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 166 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +12.6) | — |
| [[C32 (line)]] | wt | 116 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +15.9) | — |
| [[NCI-H1792 (line)]] | alt | 177 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.67× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 112 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +24.1) | — |
| [[A-172 (line)]] | wt | 145 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +18.7) | — |
| [[A498 (line)]] | wt | 163 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.5) | — |
| [[CFPAC-1 (line)]] | alt | 167 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.48× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 101 | 3 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.61× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.1) | [[Thymol (drug)]] 0.5 µM 0.392× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 107 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.43× (z +11.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 2.06× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 276 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.517× (z -9.2) ⚠ cell-cycle shift, explains ~14% of this change |
| [[KATO III (line)]] | alt | 203 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.480× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[LS 180 (line)]] | wt | 175 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 111 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 88.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 95.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +24.4) | — |
| [[SW1417 (line)]] | alt | 137 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +11.7) | — |
| [[A549 (line)]] | wt | 221 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.23× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 116 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.8) | — |
| [[NCI-H2347 (line)]] | alt | 112 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +13.8) | — |
| [[A-427 (line)]] | wt | 89.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0963× (z -27.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[LOX-IMVI (line)]] | wt | 110 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.47× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 184 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.87× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -8.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -14.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 91.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +12.1) | — |
| [[RKO (line)]] | wt | 166 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 88.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.33× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 119 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.112× (z -8.6) |
| [[SW48 (line)]] | wt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 149 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFG]] | +0.62 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[NRSN2-AS1]] | +0.62 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[CLIP1]] | +0.61 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LINC01564]] | +0.59 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[INTS6-AS1]] | +0.57 | +0.26 / +0.50 | both halves | 4e-04 |  |
| [[SPATC1]] | +0.57 | +0.28 / +0.52 | both halves | 3e-04 |  |
| [[HSD17B3]] | +0.57 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[KIF21A]] | +0.56 | +0.42 / +0.35 | both halves | 1e-04 |  |
| [[LURAP1L-AS1]] | +0.56 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[LINC00616]] | +0.56 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[NPHS1]] | +0.56 | +0.28 / +0.49 | both halves | 3e-04 |  |
| [[DMGDH]] | +0.56 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP2]] | -0.62 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[SKP2]] | -0.57 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[SHMT1]] | -0.55 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[TMEM245]] | -0.55 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ELP1]] | -0.54 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[NOC2L]] | -0.54 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[GUSB]] | -0.53 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[UNG]] | -0.53 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[MSH2]] | -0.53 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[NCAPD3]] | -0.52 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[NUDT21]] | -0.52 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[PTCD3]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINK1]] | B | SPINK1 activity raises MAPK6's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.29× lower at baseline in the lines without SPINK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[CRYM]] | B | CRYM activity raises MAPK6's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.23× lower at baseline in the lines without CRYM | 0.093 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.9, 23.5); signed map (12.2, -6.5). **Vector** length 88.1, 28.9% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.9 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +0.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +0.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.6 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | +9.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.5 | -3.6 |
|  | [[NG25 (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.7 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.9 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:51,952,106-52,067,375 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERK3, p97MAPK, HsT17250; previously PRKM6 |
| Gene groups (HGNC) | Atypical mitogen-activated protein kinases |
| Reactome | 2 pathways, smallest: MAPK6/MAPK4 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16659](https://www.uniprot.org/uniprotkb/Q16659) (Mitogen-activated protein kinase 6):

> Atypical MAPK protein. Phosphorylates microtubule-associated protein 2 (MAP2) and MAPKAPK5. The precise role of the complex formed with MAPKAPK5 is still unclear, but the complex follows a complex set of phosphorylation events: upon interaction with atypical MAPKAPK5, ERK3/MAPK6 is phosphorylated at Ser-189 and then mediates phosphorylation and activation of MAPKAPK5, which in turn phosphorylates ERK3/MAPK6. May promote entry in the cell cycle (By similarity).

**Summary**, from NCBI Gene [5597](https://www.ncbi.nlm.nih.gov/gene/5597):

> The protein encoded by this gene is a member of the Ser/Thr protein kinase family, and is most closely related to mitogen-activated protein kinases (MAP kinases). MAP kinases also known as extracellular signal-regulated kinases (ERKs), are activated through protein phosphorylation cascades and act as integration points for multiple biochemical signals. This kinase is localized in the nucleus, and has been reported to be activated in fibroblasts upon treatment with serum or phorbol esters. …

**Accessions** — [HGNC:6879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6879) · Entrez [5597](https://www.ncbi.nlm.nih.gov/gene/5597) · UniProt [Q16659](https://www.uniprot.org/uniprotkb/Q16659) · Ensembl [ENSG00000069956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069956)

## Data

Gene col 930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 930); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 930]; `tensor/DDL_lfc|DDL_z.npy` [930]; `embed/gene_vectors.npy` [930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 930 or target_col == 930). Every well: [[MAPK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
