---
symbol: "WSB1"
type: "gene"
col: 3018
ensembl_id: "ENSG00000109046"
name: "WD repeat and SOCS box containing 1"
location: "17q11.1"
module: 144
arm: "+"
pooled_cpm: 365.05
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# WSB1

*WD repeat and SOCS box containing 1* — 17q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.55× (z +6.4, q 8e-08, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.462× (z -10.7, q 5e-24, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.750× (z -4.2, q 0.002, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBPJ]] (+0.72, fdr 7e-06), [[TRIM7-AS2]] (+0.71, fdr 1e-05), [[OGA]] (+0.66, fdr 7e-06); moves opposite to [[CAPRIN1]] (-0.64, fdr 1e-05), [[TMEM33]] (-0.63, fdr 1e-05), [[XRCC5]] (-0.61, fdr 3e-05).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +6.4 | 8e-08 | 39/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.3 | 8e-08 | 37/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +4.6 | 7e-04 | 44/48 (hTERT-HPNE, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 8e-04 | 39/49 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +4.4 | 0.001 | 44/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.034 | 35/48 (SHP-77, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.057 | 31/49 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.057 | 31/49 (LS 180, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.057 | 30/48 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.068 | 32/49 (A549, RPMI-7951, …) | top dose only | plate-row cell shift; position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.068 | 31/48 (HCT15, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.068 | 25/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.23× | +3.0 | 0.11 | 25/48 (MIA PaCa-2, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3018.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -10.7 | 5e-24 | 40/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.482×** | -9.4 | 1e-18 | 43/45 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.529×** | -9.2 | 6e-18 | 40/49 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -6.1 | 1e-07 | 41/47 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -6.1 | 1e-07 | 36/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.661×** | -6.0 | 2e-07 | 46/48 (SW 900, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.674×** | -5.7 | 9e-07 | 43/48 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.710×** | -5.0 | 5e-05 | 39/48 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.750×** | -4.2 | 0.002 | 30/48 (C-33 A, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.016 | 26/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.629×** | -3.5 | 0.023 | 34/49 (C-33 A, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.032 | 27/48 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **0.760×** | -3.3 | 0.041 | 33/49 (LS 180, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.799×** | -3.3 | 0.046 | 29/48 (SW 900, A549, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.660×** | -3.1 | 0.062 | 26/48 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.666×** | -3.1 | 0.073 | 25/49 (SW 900, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.813×** | -3.0 | 0.086 | 26/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 571 | 0 | 9 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 444 | 6 (4 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.58× (z +15.8) | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 578 | 1 (1 ⚠) | 6 (5 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.97× (z +12.2) ⚠ cell-cycle shift, explains ~10% of this change | [[Dinaciclib (drug)]] 5 µM 0.281× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.461× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 671 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -15.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 461 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -10.7) |
| [[A549 (line)]] | wt | 348 | 1 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.28× (z +10.4) ⚠ cell-cycle shift, explains ~10% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 328 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 571 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 431 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.88× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -12.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 308 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -10.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 543 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 429 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 335 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.48× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.444× (z -8.5) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 646 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -12.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 468 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -12.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 368 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.407× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 198 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +18.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 381 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -11.0) |
| [[KATO III (line)]] | alt | 300 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 473 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -19.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 422 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -10.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 320 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.380× (z -9.9) |
| [[A-427 (line)]] | wt | 234 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -17.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 400 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 542 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 336 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 308 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.331× (z -11.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 432 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.377× (z -8.7) ⚠ toxic |
| [[J82 (line)]] | alt | 375 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +8.6) | — |
| [[LoVo (line)]] | wt | 237 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 343 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +11.4) | — |
| [[RKO (line)]] | wt | 320 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.399× (z -8.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 362 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 303 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 460 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 323 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 475 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 367 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 287 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 312 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 337 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 263 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 423 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 431 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 631 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 251 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 223 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBPJ]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[TRIM7-AS2]] | +0.71 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[OGA]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ARID4B]] | +0.64 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[ADM]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[DCTN6-DT]] | +0.64 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[CCS]] | +0.63 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[RNF122]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ZFYVE1]] | +0.62 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[C1orf56]] | +0.62 | +0.29 / +0.74 | both halves | 2e-04 |  |
| [[SEC61G]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[POLR2H]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPRIN1]] | -0.64 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.63 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.61 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[MTHFD1]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[NCBP1]] | -0.60 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[SLC25A24]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PRELID3B]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[IPO5]] | -0.58 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[EIF2S1]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[NAA15]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[SSU72]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[SGPL1]] | -0.58 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.6, -22.9); signed map (-31.7, 24.9). **Vector** length 155, 58.9% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.7 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +6.0 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +2.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +4.3 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +4.2 | +2.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -9.4 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.6 | -9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -10.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat and SOCS box containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.1 — chr17:27,294,076-27,315,926 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564A122, DKFZp564B0482, SWIP1 |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | HYPOXIA |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6I7](https://www.uniprot.org/uniprotkb/Q9Y6I7) (WD repeat and SOCS box-containing protein 1):

> Probable substrate-recognition component of a SCF-like ECS (Elongin-Cullin-SOCS-box protein) E3 ubiquitin ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Recognizes type II iodothyronine deiodinase/DIO2. Confers constitutive instability to HIPK2 through proteasomal degradation.

**Summary**, from NCBI Gene [26118](https://www.ncbi.nlm.nih.gov/gene/26118):

> This gene encodes a member of the WD-protein subfamily. This protein shares a high sequence identity to mouse and chick proteins. It contains several WD-repeats spanning most of the protein and an SOCS box in the C-terminus. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19221) · Entrez [26118](https://www.ncbi.nlm.nih.gov/gene/26118) · UniProt [Q9Y6I7](https://www.uniprot.org/uniprotkb/Q9Y6I7) · Ensembl [ENSG00000109046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109046)

## Data

Gene col 3018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3018); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3018]; `tensor/DDL_lfc|DDL_z.npy` [3018]; `embed/gene_vectors.npy` [3018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3018 or target_col == 3018). Every well: [[WSB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WSB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
