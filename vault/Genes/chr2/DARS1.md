---
symbol: "DARS1"
type: "gene"
col: 3730
ensembl_id: "ENSG00000115866"
name: "aspartyl-tRNA synthetase 1"
location: "2q21.3"
module: 28
arm: "+"
pooled_cpm: 196.6
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 2
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# DARS1

*aspartyl-tRNA synthetase 1* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.43× (z +7.6, q 1e-11, up in 34 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.39× (z +7.0, q 7e-10, up in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 4 lines (NCI-H1573 2.03×, HOP62 1.85×, NCI-H1792 2.22×, A-172 1.78×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 1.95×, A-172 1.61×, A498 1.53×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A498 2.08×, NCI-H1792 2.31×, PANC-1 1.64×; ⚠ cell-cycle shift, explains ~60% of this change).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.322× (z -24.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LZIC]] (+0.75, fdr 7e-06), [[USP40]] (+0.73, fdr 7e-06), [[DZIP3]] (+0.72, fdr 1e-05); moves opposite to [[SDHAP4]] (-0.65, fdr 1e-05), [[UBE2G1]] (-0.64, fdr 1e-05), [[DCUN1D2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SESTD1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3730.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 4 lines (NCI-H1573 2.03×, HOP62 1.85×, NCI-H1792 2.22×, A-172 1.78×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 1.95×, A-172 1.61×, A498 1.53×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A498 2.08×, NCI-H1792 2.31×, PANC-1 1.64×; ⚠ cell-cycle shift, explains ~60% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.6 | 1e-11 | 34/49 (RKO, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.0 | 7e-10 | 37/48 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.7 | 3e-06 | 38/48 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.1 | 4e-05 | 26/44 (A498, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.20×** | +4.0 | 0.008 | 23/48 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.9 | 0.010 | 0/50 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.20× | +3.7 | 0.017 | 24/48 (LoVo, NCI-H1792, …) | all doses, flat | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.068 | 17/47 (NCI-H1792, HepG2/C3A, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.15 | 13/48 (SW480, HCT15, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.322×** | -24.2 | 0e+00 | 48/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.323×** | -24.2 | 0e+00 | 48/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.359×** | -21.9 | 0e+00 | 48/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.447×** | -17.2 | 0e+00 | 48/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.483×** | -14.9 | 0e+00 | 47/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -14.9 | 0e+00 | 46/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -14.0 | 7e-43 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.525×** | -13.8 | 3e-41 | 48/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -12.7 | 2e-35 | 40/49 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -11.8 | 3e-30 | 46/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.577×** | -11.8 | 3e-30 | 48/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.649×** | -8.9 | 3e-17 | 41/47 (HOP62, HCT15, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.678×** | -8.3 | 4e-15 | 44/48 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.680×** | -8.2 | 8e-15 | 41/48 (PANC-1, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -8.2 | 1e-14 | 37/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.483×** | -8.1 | 1e-14 | 47/49 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.731×** | -6.3 | 1e-08 | 36/48 (HEC-1-A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.772×** | -5.5 | 1e-06 | 34/49 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -5.1 | 1e-05 | 32/48 (C32, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.809×** | -4.5 | 2e-04 | 26/48 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 260 | 3 (3 ⚠) | 14 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +19.1) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.318× (z -23.4) |
| [[SW480 (line)]] | alt | 268 | 1 (1 ⚠) | 16 (7 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.75× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -24.1) |
| [[H4 (line)]] | wt | 192 | 0 | 12 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.242× (z -15.6) |
| [[J82 (line)]] | alt | 185 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -20.3) |
| [[SNU-423 (line)]] | alt | 208 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 146 | 3 (2 ⚠) | 8 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.49× (z +10.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.22× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.237× (z -17.6) |
| [[A-427 (line)]] | wt | 184 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -19.0) |
| [[C32 (line)]] | wt | 215 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 174 | 1 (1 ⚠) | 9 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -19.3) |
| [[NCI-H23 (line)]] | alt | 281 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -24.1) |
| [[NCI-H460 (line)]] | wt | 180 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -18.2) |
| [[SNU-1 (line)]] | wt | 243 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.249× (z -17.2) |
| [[SW 900 (line)]] | alt | 212 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -15.5) |
| [[A-172 (line)]] | wt | 212 | 2 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.78× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.304× (z -19.1) |
| [[C-33 A (line)]] | alt | 209 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.302× (z -14.9) |
| [[COLO 205 (line)]] | alt | 181 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -14.9) |
| [[HT-29 (line)]] | alt | 150 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 311 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -22.8) |
| [[NCI-H1573 (line)]] | alt | 161 | 1 | 8 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.03× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.232× (z -21.0) |
| [[NCI-H2030 (line)]] | alt | 218 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -15.5) |
| [[A498 (line)]] | wt | 187 | 4 (4 ⚠) | 4 | [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +12.0) ⚠ cell-cycle shift, explains ~60% of this change | [[Panobinostat (drug)]] 0.5 µM 0.536× (z -10.1) |
| [[BT-474 (line)]] | alt | 133 | 1 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.175× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -15.7) |
| [[HCT15 (line)]] | alt | 278 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -19.6) |
| [[HepG2_C3A (line)]] | wt | 245 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -17.7) |
| [[HOP62 (line)]] | alt | 258 | 1 | 7 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.85× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -24.6) |
| [[HS-578T (line)]] | alt | 115 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.376× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.378× (z -12.1) |
| [[LoVo (line)]] | wt | 167 | 2 (2 ⚠) | 6 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.19× (z +11.2) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 5 µM 0.250× (z -20.7) |
| [[RKO (line)]] | wt | 209 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +13.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -19.3) |
| [[Hs 766T (line)]] | wt | 150 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -14.2) |
| [[LS 180 (line)]] | wt | 152 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.267× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 243 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -15.9) |
| [[SW1417 (line)]] | alt | 136 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -12.8) |
| [[KATO III (line)]] | alt | 104 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.374× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 142 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 0.5 µM 1.76× (z +9.2) ⚠ cell-cycle shift, explains ~60% of this change | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 206 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -16.3) |
| [[SHP-77 (line)]] | alt | 95.8 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.2) |
| [[A549 (line)]] | wt | 176 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 192 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 344 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 162 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.320× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 98.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -12.8) |
| [[SW48 (line)]] | wt | 133 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.317× (z -10.7) |
| [[AN3 CA (line)]] | alt | 164 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -11.0) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 88.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -9.5) |
| [[SW 1271 (line)]] | alt | 274 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.148× (z -12.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 231 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZIC]] | +0.75 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[USP40]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[DZIP3]] | +0.72 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[RAD50]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[COQ5]] | +0.71 | +0.74 / +0.58 | both halves | 8e-06 |  |
| [[RIMOC1]] | +0.71 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[LINC01473]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SPG11]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[FCF1]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[LINC00174]] | +0.68 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD26]] | +0.67 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[ZMYM4]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4]] | -0.65 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[UBE2G1]] | -0.64 | -0.71 / -0.50 | both halves | 1e-05 |  |
| [[DCUN1D2]] | -0.62 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.61 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[MFSD14CP]] | -0.61 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[C1orf216]] | -0.61 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[MOGS]] | -0.61 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.61 | -0.62 / -0.44 | both halves | 3e-05 | pathway: MITF-M-regulated melanocyte development |
| [[SGPP1]] | -0.60 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SESTD1]] | C | SESTD1 activity lowers DARS1's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without SESTD1 | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.0, 8.0); signed map (10.9, -25.0). **Vector** length 126, 48.0% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +17.0 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +16.8 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +15.1 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +14.4 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +10.4 | +5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.3 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.3 | -14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -8.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.1 | -11.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -17.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.3 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | aspartyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.3 — chr2:135,905,881-135,986,100 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 7 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P14868](https://www.uniprot.org/uniprotkb/P14868) (Aspartate--tRNA ligase, cytoplasmic):

> Catalyzes the specific attachment of an amino acid to its cognate tRNA in a 2 step reaction: the amino acid (AA) is first activated by ATP to form AA-AMP and then transferred to the acceptor end of the tRNA.

**Summary**, from NCBI Gene [1615](https://www.ncbi.nlm.nih.gov/gene/1615):

> This gene encodes a member of a multienzyme complex that functions in mediating the attachment of amino acids to their cognate tRNAs. The encoded protein ligates L-aspartate to tRNA(Asp). Mutations in this gene have been found in patients showing hypomyelination with brainstem and spinal cord involvement and leg spasticity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:2678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2678) · Entrez [1615](https://www.ncbi.nlm.nih.gov/gene/1615) · UniProt [P14868](https://www.uniprot.org/uniprotkb/P14868) · Ensembl [ENSG00000115866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115866)

## Data

Gene col 3730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3730); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3730]; `tensor/DDL_lfc|DDL_z.npy` [3730]; `embed/gene_vectors.npy` [3730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3730 or target_col == 3730). Every well: [[DARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
