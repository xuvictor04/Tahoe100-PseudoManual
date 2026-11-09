---
symbol: "LRP6"
type: "gene"
col: 935
ensembl_id: "ENSG00000070018"
name: "LDL receptor related protein 6"
location: "12p13.2"
module: 197
arm: "+"
pooled_cpm: 132.68
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# LRP6

*LDL receptor related protein 6* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.47× (z +28.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.720× (z -10.1, q 3e-21, down in 26 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.842× (z -3.9, q 0.009, down in 13 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW1417 0.296×, SW480 0.332×, NCI-H23 0.358×, LoVo 0.388×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (KATO III 0.310×, LS 180 0.352×, NCI-H2030 0.337×, Panc 03.27 0.432×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.416×, C-33 A 0.378×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.447×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEO1]] (+0.60, fdr 1e-05), [[MAGI1]] (+0.58, fdr 1e-05), [[RSBN1L]] (+0.56, fdr 1e-05); moves opposite to [[PITRM1]] (-0.53, fdr 1e-04), [[TPD52L2]] (-0.51, fdr 1e-05), [[ZNF621]] (-0.50, fdr 4e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +28.8 | 0e+00 | 48/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +24.6 | 0e+00 | 47/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +22.5 | 0e+00 | 48/48 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +21.4 | 0e+00 | 40/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +20.4 | 0e+00 | 43/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +15.9 | 0e+00 | 42/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +15.9 | 0e+00 | 45/48 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.54×** | +15.5 | 0e+00 | 43/49 (HT-29, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +13.6 | 5e-40 | 41/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +13.5 | 5e-40 | 40/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +12.1 | 5e-32 | 39/48 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +10.8 | 2e-25 | 41/49 (NCI-H23, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +10.3 | 3e-23 | 30/48 (LoVo, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.2 | 9e-23 | 30/48 (NCI-H23, H4, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +8.8 | 4e-17 | 35/48 (HEC-1-A, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +6.6 | 2e-09 | 23/48 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 935.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW1417 0.296×, SW480 0.332×, NCI-H23 0.358×, LoVo 0.388×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (KATO III 0.310×, LS 180 0.352×, NCI-H2030 0.337×, Panc 03.27 0.432×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.416×, C-33 A 0.378×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.447×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -10.1 | 3e-21 | 26/44 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.792×** | -7.5 | 3e-11 | 24/49 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -6.5 | 1e-08 | 0/50 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.869× | -4.2 | 0.004 | 19/45 (A-427, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.842× | -3.9 | 0.009 | 13/48 (LS 180, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.900× | -3.4 | 0.070 | 6/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.869× | -3.2 | 0.093 | 10/47 (A-427, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.826×** | -3.2 | 0.093 | 13/48 (SW 900, C32, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 0.876× | -3.0 | 0.15 | 9/49 (SW 900, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 166 | 10 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.567× (z -9.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 191 | 10 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -17.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 272 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 210 | 9 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.54× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -17.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 100 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +21.7) | — |
| [[SW1417 (line)]] | alt | 142 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -18.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 117 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +18.3) | [[Dinaciclib (drug)]] 0.05 µM 0.493× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 235 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -16.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 290 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 133 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +18.3) | [[Lonafarnib (drug)]] 5 µM 0.106× (z -14.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 315 | 4 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.81× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -18.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 89.4 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 71.5 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +16.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 123 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +19.4) | — |
| [[A549 (line)]] | wt | 130 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +17.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -10.5) ⚠ cell-cycle shift, explains ~88% of this change |
| [[Panc 03.27 (line)]] | alt | 169 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 76.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +18.2) | — |
| [[RKO (line)]] | wt | 183 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.399× (z -12.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 196 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +16.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.447× (z -13.8) |
| [[HOP62 (line)]] | alt | 103 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +14.9) | — |
| [[J82 (line)]] | alt | 73.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.16× (z +17.3) | — |
| [[NCI-H2030 (line)]] | alt | 151 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -16.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 65.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +18.6) | — |
| [[AsPC-1 (line)]] | alt | 48.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 219 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 39.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 58.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 63.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 119 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +17.7) | — |
| [[A-172 (line)]] | wt | 38.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 114 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 75.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 109 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +15.0) | — |
| [[NCI-H460 (line)]] | wt | 82.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +14.6) | — |
| [[RPMI-7951 (line)]] | alt | 72.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 60.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 213 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.98× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -12.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 112 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.65× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 159 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 208 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 68.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 126 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +10.5) | — |
| [[SW48 (line)]] | wt | 121 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.54× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEO1]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MAGI1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[RSBN1L]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TCF7L2]] | +0.56 | +0.44 / +0.49 | both halves | 3e-05 | pathway: Signaling by WNT; STRING 509 |
| [[KAT6A]] | +0.56 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[STIM2]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[STAU2]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SMAD6]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ARHGEF12]] | +0.53 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CTDSPL]] | +0.53 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[CUL3]] | +0.52 | +0.36 / +0.54 | both halves | 9e-05 | pathway: Signaling by WNT |
| [[MRTFB]] | +0.52 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITRM1]] | -0.53 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[TPD52L2]] | -0.51 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ZNF621]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[RECQL5]] | -0.49 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[ZNF550]] | -0.47 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[ZBTB43]] | -0.47 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[FAM219A]] | -0.46 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[TAF13]] | -0.45 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[DDX49]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ZDHHC6]] | -0.45 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[DUSP28]] | -0.45 | -0.43 / -0.32 | both halves | 1e-04 |  |
| [[ZNF841]] | -0.43 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.2, 38.0); signed map (4.9, 12.8). **Vector** length 98.1, 29.3% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +15.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +12.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +3.7 | +7.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +10.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.2 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.4 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:12,116,025-12,267,044 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADCAD2 |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Reactome | 8 pathways, smallest: Signaling by RNF43 mutants; Negative regulation of TCF-dependent signaling by WNT ligand antagonists; Regulation of FZD by ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [O75581](https://www.uniprot.org/uniprotkb/O75581) (Low-density lipoprotein receptor-related protein 6):

> Component of the Wnt-Fzd-LRP5-LRP6 complex that triggers beta-catenin signaling through inducing aggregation of receptor-ligand complexes into ribosome-sized signalosomes. Cell-surface coreceptor of Wnt/beta-catenin signaling, which plays a pivotal role in various processes including retinal angiogenesis and bone formation. The Wnt-induced Fzd/LRP6 coreceptor complex recruits DVL1 polymers to the plasma membrane which, in turn, recruits the AXIN1/GSK3B-complex to the cell surface promoting the …

**Summary**, from NCBI Gene [4040](https://www.ncbi.nlm.nih.gov/gene/4040):

> This gene encodes a member of the low density lipoprotein (LDL) receptor gene family. LDL receptors are transmembrane cell surface proteins involved in receptor-mediated endocytosis of lipoprotein and protein ligands. The protein encoded by this gene functions as a receptor or, with Frizzled, a co-receptor for Wnt and thereby transmits the canonical Wnt/beta-catenin signaling cascade. Through its interaction with the Wnt/beta-catenin signaling cascade this gene plays a role in the regulation of …

**Accessions** — [HGNC:6698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6698) · Entrez [4040](https://www.ncbi.nlm.nih.gov/gene/4040) · UniProt [O75581](https://www.uniprot.org/uniprotkb/O75581) · Ensembl [ENSG00000070018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070018)

## Data

Gene col 935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 935); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 935]; `tensor/DDL_lfc|DDL_z.npy` [935]; `embed/gene_vectors.npy` [935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 935 or target_col == 935). Every well: [[LRP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
