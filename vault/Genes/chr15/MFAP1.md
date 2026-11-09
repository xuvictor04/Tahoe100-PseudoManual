---
symbol: "MFAP1"
type: "gene"
col: 6378
ensembl_id: "ENSG00000140259"
name: "microfibril associated protein 1"
location: "15q15.3"
module: 12
arm: "+"
pooled_cpm: 43.51
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MFAP1

*microfibril associated protein 1* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.48× (z +27.6, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.653× (z -6.5, q 5e-08, down in 26 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 0.190×, LoVo 0.267×, SW480 0.308×, A-427 0.249×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.177×, RKO 0.173×, KATO III 0.330×, NCI-H2030 0.357×, …; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.197×; ⚠ cell-cycle shift, would explain all of this change); [[Rapamycin (drug)]] 0.5 µM in 1 line (SW 1271 0.0725×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.80, fdr 7e-06), [[MRPS18C]] (+0.73, fdr 7e-06), [[TOPORS]] (+0.72, fdr 7e-06); moves opposite to [[MAPK9]] (-0.70, fdr 7e-06), [[MFSD14B]] (-0.66, fdr 7e-06), [[STT3B]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.48×** | +27.6 | 0e+00 | 45/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.95×** | +17.2 | 0e+00 | 45/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.54×** | +14.2 | 9e-44 | 45/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +10.0 | 2e-21 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.87×** | +8.7 | 2e-16 | 43/49 (LoVo, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +8.2 | 2e-14 | 37/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.65×** | +7.9 | 2e-13 | 41/48 (A498, PANC-1, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.61×** | +7.6 | 3e-12 | 39/48 (A-172, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.60×** | +7.5 | 6e-12 | 37/48 (SNU-1, SW480, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +7.2 | 4e-11 | 39/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.55×** | +7.0 | 1e-10 | 34/48 (KATO III, A549, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.5 | 4e-09 | 30/48 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.43×** | +5.7 | 5e-07 | 28/47 (SNU-1, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.5 | 2e-06 | 31/48 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.9 | 3e-05 | 30/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.003 | 18/48 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.003 | 21/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.074 | 9/49 (CHP-212, SHP-77, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.20×** | +2.9 | 0.084 | 17/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6378.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 0.190×, LoVo 0.267×, SW480 0.308×, A-427 0.249×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.177×, RKO 0.173×, KATO III 0.330×, NCI-H2030 0.357×, …; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.197×; ⚠ cell-cycle shift, would explain all of this change); [[Rapamycin (drug)]] 0.5 µM in 1 line (SW 1271 0.0725×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -6.5 | 5e-08 | 26/41 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.682×** | -6.0 | 4e-07 | 31/49 (HCT15, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -4.9 | 2e-04 | 24/47 (HepG2/C3A, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.813×** | -4.5 | 8e-04 | 24/48 (HS-578T, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.770×** | -3.8 | 0.015 | 21/44 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.807×** | -3.4 | 0.068 | 19/48 (SW 1088, KATO III, …) | inconsistent across doses |  |
| [[Adenine (drug)]] 5 µM |  | 0.865× | -3.2 | 0.13 | 11/48 (MIA PaCa-2, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 71.3 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +28.3) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 64.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +28.4) | — |
| [[PANC-1 (line)]] | alt | 45.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +22.5) | — |
| [[A-172 (line)]] | wt | 36.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -10.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 30.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +19.9) | — |
| [[NCI-H2030 (line)]] | alt | 60.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 36.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +20.3) | — |
| [[A498 (line)]] | wt | 45.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +20.7) | — |
| [[KATO III (line)]] | alt | 57.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 47.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +21.4) | — |
| [[RKO (line)]] | wt | 58.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -10.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 32.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 32.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +19.3) | — |
| [[HS-578T (line)]] | alt | 27.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +16.8) | — |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +18.3) | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +18.3) | — |
| [[SW480 (line)]] | alt | 46.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -12.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 33.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 69.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 46.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 36.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -10.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 43.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +16.1) | — |
| [[LS 180 (line)]] | wt | 35.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +14.4) | — |
| [[NCI-H23 (line)]] | alt | 47.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 60.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +14.8) | — |
| [[SK-MEL-2 (line)]] | alt | 43.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +13.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 35.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 37.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 49.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +16.8) | — |
| [[HCT15 (line)]] | alt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -13.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 41.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +13.4) | — |
| [[J82 (line)]] | alt | 47.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +14.0) | — |
| [[NCI-H2347 (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 43.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 38.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.89× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +14.0) | — |
| [[SW 1271 (line)]] | alt | 55.7 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0725× (z -9.2) |
| [[SW1417 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.80 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.73 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.72 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[SNW1]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 967 |
| [[MRFAP1L1]] | +0.71 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.71 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[FAM32A]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TJAP1]] | +0.70 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[MED18]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.69 | +0.75 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 597 |
| [[PRPF38B]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | -0.70 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[MFSD14B]] | -0.66 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[STT3B]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[NCKAP1]] | -0.64 | -0.72 / -0.66 | both halves | 7e-06 |  |
| [[NUDT3]] | -0.63 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[SMG1P3]] | -0.63 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[LAPTM4B]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[HACD3]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.60 | -0.61 / -0.57 | both halves | 8e-06 |  |
| [[CRTAP]] | -0.60 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.60 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[GLB1]] | -0.59 | -0.62 / -0.57 | both halves | 8e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.8, 3.4); signed map (0.3, -15.7). **Vector** length 111, 32.2% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.7 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +27.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +17.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.5 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.9 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +0.8 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | microfibril associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,804,492-43,824,690 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AMP |
| Gene groups (HGNC) | Spliceosomal B complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P55081](https://www.uniprot.org/uniprotkb/P55081) (Microfibrillar-associated protein 1):

> Involved in pre-mRNA splicing as a component of the spliceosome.

**Summary**, from NCBI Gene [4236](https://www.ncbi.nlm.nih.gov/gene/4236):

> Enables RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in microfibril and nucleoplasm. Part of U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7032) · Entrez [4236](https://www.ncbi.nlm.nih.gov/gene/4236) · UniProt [P55081](https://www.uniprot.org/uniprotkb/P55081) · Ensembl [ENSG00000140259](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140259)

## Data

Gene col 6378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6378); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6378]; `tensor/DDL_lfc|DDL_z.npy` [6378]; `embed/gene_vectors.npy` [6378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6378 or target_col == 6378). Every well: [[MFAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
