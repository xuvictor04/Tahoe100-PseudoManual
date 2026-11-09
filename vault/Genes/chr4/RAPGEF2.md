---
symbol: "RAPGEF2"
type: "gene"
col: 3077
ensembl_id: "ENSG00000109756"
name: "Rap guanine nucleotide exchange factor 2"
location: "4q32.1"
module: 1
arm: "-"
pooled_cpm: 215.07
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RAPGEF2

*Rap guanine nucleotide exchange factor 2* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.24× (z +6.2, q 3e-07, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.328× (z -22.9, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.580× (z -5.3, q 9e-06, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALGPS2]] (+0.60, fdr 2e-05), [[ZSWIM6]] (+0.60, fdr 1e-05), [[FRYL]] (+0.59, fdr 1e-05); moves opposite to [[RRN3P1]] (-0.55, fdr 3e-05), [[DCPS]] (-0.52, fdr 3e-05), [[SPRYD4]] (-0.51, fdr 3e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +6.2 | 3e-07 | 26/48 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +6.0 | 7e-07 | 32/47 (SNU-423, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.7 | 2e-06 | 32/48 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +5.3 | 1e-05 | 30/48 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.8 | 2e-04 | 27/45 (HCT15, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +4.4 | 8e-04 | 23/48 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +4.4 | 8e-04 | 26/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 8e-04 | 27/48 (HCT15, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.20×** | +3.8 | 0.010 | 23/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.010 | 22/48 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.20×** | +3.6 | 0.014 | 23/47 (H4, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.014 | 24/48 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.020 | 9/48 (SK-MEL-2, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.5 | 0.020 | 21/48 (A498, C32, …) | top dose only | composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.2 | 0.055 | 7/48 (A-172, HOP62, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.083 | 19/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.093 | 18/50 (A-427, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.328×** | -22.9 | 0e+00 | 46/49 (Panc 03.27, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.352×** | -20.6 | 0e+00 | 43/44 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.398×** | -15.0 | 0e+00 | 41/45 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.695×** | -7.5 | 1e-11 | 40/48 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.696×** | -7.5 | 1e-11 | 38/48 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.688×** | -7.4 | 1e-11 | 37/47 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.580×** | -5.3 | 9e-06 | 37/48 (NCI-H2347, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.594×** | -5.1 | 3e-05 | 41/48 (RKO, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.629×** | -4.5 | 4e-04 | 28/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.809×** | -4.4 | 7e-04 | 25/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.641×** | -4.3 | 8e-04 | 33/48 (LoVo, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.649×** | -4.2 | 0.001 | 30/48 (NCI-H2347, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.656×** | -4.1 | 0.002 | 22/38 (HS-578T, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.860× | -3.1 | 0.079 | 14/48 (NCI-H2347, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 422 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.487× (z -9.1) |
| [[C32 (line)]] | wt | 187 | 5 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -15.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 178 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +22.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -17.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 410 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 215 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 307 | 2 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.93× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 2.05× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -20.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 331 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -14.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 209 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -19.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 548 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -18.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 187 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.440× (z -11.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 241 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -14.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 169 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -12.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[KATO III (line)]] | alt | 235 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -22.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 357 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -19.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 65.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 280 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 164 | 1 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.24× (z +9.0) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -12.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 179 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -14.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 194 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -19.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 302 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -16.6) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 642 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -12.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 154 | 2 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 177 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -14.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 171 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.173× (z -22.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 231 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -13.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 178 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -13.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 285 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -15.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 275 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -15.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 291 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -22.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.422× (z -11.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 368 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -11.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -12.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -21.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 132 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGPS2]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ZSWIM6]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[FRYL]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PEAK1]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PLEKHA5]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TAOK3]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[HEBP2]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PARD3]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 | same gene group |
| [[ITSN1]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PINK1]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 | same gene group |
| [[KLF12]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[DAAM1]] | +0.53 | +0.39 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRN3P1]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[DCPS]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SPRYD4]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SMYD5]] | -0.49 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[TIGD1]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 | same gene group |
| [[GUF1]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[UBA5]] | -0.48 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[UMPS]] | -0.47 | -0.45 / -0.43 | both halves | 3e-05 | same gene group |
| [[PYM1]] | -0.47 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[FARSA]] | -0.47 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TMX2]] | -0.46 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[PARL]] | -0.46 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.397). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.5, 14.7); signed map (-15.1, 29.0). **Vector** length 117, 38.7% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.5 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.5 | +2.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.3 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.9 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -7.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -5.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.4 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | Rap guanine nucleotide exchange factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:159,103,013-159,360,174 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDZ-GEF1, RA-GEF, DKFZP586O1422, KIAA0313; previously PDZGEF1 |
| Gene groups (HGNC) | PDZ domain containing; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: RAF/MAP kinase cascade; MAPK1/MAPK3 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4G8](https://www.uniprot.org/uniprotkb/Q9Y4G8) (Rap guanine nucleotide exchange factor 2):

> Functions as a guanine nucleotide exchange factor (GEF), which activates Rap and Ras family of small GTPases by exchanging bound GDP for free GTP in a cAMP-dependent manner. Serves as a link between cell surface receptors and Rap/Ras GTPases in intracellular signaling cascades. Also acts as an effector for Rap1 by direct association with Rap1-GTP thereby leading to the amplification of Rap1-mediated signaling. Shows weak activity on HRAS. It is controversial whether RAPGEF2 binds cAMP and cGMP …

**Summary**, from NCBI Gene [9693](https://www.ncbi.nlm.nih.gov/gene/9693):

> Members of the RAS (see HRAS; MIM 190020) subfamily of GTPases function in signal transduction as GTP/GDP-regulated switches that cycle between inactive GDP- and active GTP-bound states. Guanine nucleotide exchange factors (GEFs), such as RAPGEF2, serve as RAS activators by promoting acquisition of GTP to maintain the active GTP-bound state and are the key link between cell surface receptors and RAS activation (Rebhun et al., 2000 [PubMed 10934204]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16854) · Entrez [9693](https://www.ncbi.nlm.nih.gov/gene/9693) · UniProt [Q9Y4G8](https://www.uniprot.org/uniprotkb/Q9Y4G8) · Ensembl [ENSG00000109756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109756)

## Data

Gene col 3077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3077); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3077]; `tensor/DDL_lfc|DDL_z.npy` [3077]; `embed/gene_vectors.npy` [3077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3077 or target_col == 3077). Every well: [[RAPGEF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAPGEF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
