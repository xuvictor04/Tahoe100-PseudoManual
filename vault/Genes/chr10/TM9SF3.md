---
symbol: "TM9SF3"
type: "gene"
col: 1174
ensembl_id: "ENSG00000077147"
name: "transmembrane 9 superfamily member 3"
location: "10q24.1"
module: 20
arm: "+"
pooled_cpm: 296.55
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TM9SF3

*transmembrane 9 superfamily member 3* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.76× (z +12.6, q 2e-33, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.581× (z -12.9, q 5e-35, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC5]] (+0.71, fdr 7e-06), [[RPN1]] (+0.67, fdr 7e-06), [[DDOST]] (+0.66, fdr 7e-06); moves opposite to [[PDRG1]] (-0.65, fdr 7e-06), [[MRPL46]] (-0.64, fdr 1e-05), [[TRIM47]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.76×** | +12.6 | 2e-33 | 48/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +10.0 | 4e-21 | 43/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +8.8 | 3e-16 | 36/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +8.3 | 1e-14 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +8.1 | 6e-14 | 41/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +7.7 | 1e-12 | 33/45 (SK-MEL-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.6 | 2e-12 | 40/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.4 | 6e-06 | 31/38 (SK-MEL-2, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | **1.23×** | +5.0 | 4e-05 | 27/49 (A-172, PANC-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +4.2 | 0.002 | 23/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.16× | +3.6 | 0.017 | 18/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -12.9 | 5e-35 | 46/48 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.615×** | -11.5 | 3e-28 | 48/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -10.6 | 4e-24 | 44/48 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.753×** | -9.5 | 3e-19 | 29/48 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.794×** | -7.7 | 1e-12 | 31/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.745×** | -7.0 | 3e-10 | 38/48 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.771×** | -5.9 | 3e-07 | 30/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -5.7 | 7e-07 | 29/47 (SW 900, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.790×** | -5.6 | 2e-06 | 25/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.805×** | -5.1 | 2e-05 | 25/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.805×** | -5.1 | 2e-05 | 31/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -4.7 | 1e-04 | 15/48 (A-427, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -4.6 | 2e-04 | 25/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.875× | -4.5 | 3e-04 | 15/48 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.831×** | -4.4 | 5e-04 | 24/48 (RKO, SNU-423, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.831×** | -4.2 | 9e-04 | 23/47 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.876× | -3.6 | 0.009 | 10/48 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 477 | 1 | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.379× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 255 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +15.5) | — |
| [[LoVo (line)]] | wt | 308 | 2 | 6 | [[TAK-901 (drug)]] 5 µM 3.10× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.429× (z -15.3) |
| [[PANC-1 (line)]] | alt | 317 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +16.8) | — |
| [[NCI-H2347 (line)]] | alt | 273 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -14.5) |
| [[SW480 (line)]] | alt | 280 | 6 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 3.74× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.652× (z -11.3) |
| [[A-172 (line)]] | wt | 244 | 4 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.35× (z +10.6) | [[Harringtonine (drug)]] 5 µM 0.569× (z -9.1) |
| [[A498 (line)]] | wt | 332 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 303 | 5 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.581× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 368 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +13.8) | — |
| [[COLO 205 (line)]] | alt | 401 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.416× (z -13.6) |
| [[HEC-1-A (line)]] | alt | 300 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.40× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.635× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 402 | 3 | 2 | [[Digitoxin (drug)]] 0.5 µM 1.99× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.496× (z -10.1) |
| [[KATO III (line)]] | alt | 343 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.495× (z -12.2) |
| [[SW1417 (line)]] | alt | 395 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.509× (z -10.4) |
| [[A-427 (line)]] | wt | 273 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.04× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.480× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 248 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.85× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.564× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 237 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.8) | [[Cobimetinib (drug)]] 5 µM 0.508× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 277 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.24× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.522× (z -10.3) |
| [[RKO (line)]] | wt | 412 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.499× (z -10.8) |
| [[SNU-1 (line)]] | wt | 292 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 311 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.578× (z -10.5) |
| [[HCT15 (line)]] | alt | 420 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.511× (z -8.5) |
| [[HOP62 (line)]] | alt | 326 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.06× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.88× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 274 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 263 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.45× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 216 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 197 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.33× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.61× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 269 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.90× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | [[Panobinostat (drug)]] 5 µM 0.511× (z -10.8) |
| [[A549 (line)]] | wt | 310 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.543× (z -8.5) |
| [[AN3 CA (line)]] | alt | 384 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.1) |
| [[C-33 A (line)]] | alt | 278 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.633× (z -9.0) |
| [[H4 (line)]] | wt | 355 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 260 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 253 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.32× (z +9.0) | [[Bortezomib (drug)]] 5 µM 0.234× (z -10.8) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 275 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.05× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.655× (z -8.6) |
| [[SW 900 (line)]] | alt | 405 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.431× (z -11.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.514× (z -9.2) |
| [[BT-474 (line)]] | alt | 248 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.76× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 245 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.99× (z +9.1) | — |
| [[J82 (line)]] | alt | 178 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -11.9) |
| [[LS 180 (line)]] | wt | 342 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.12× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 269 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 276 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 312 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | +0.71 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[RPN1]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[DDOST]] | +0.66 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[PDIA3]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[GANAB]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PDIA6]] | +0.64 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[TMED7]] | +0.64 | +0.67 / +0.71 | both halves | 7e-06 | STRING 600 |
| [[TMED10]] | +0.64 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TMEM167A]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[STT3A]] | +0.62 | +0.61 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDRG1]] | -0.65 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[MRPL46]] | -0.64 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[TRIM47]] | -0.60 | -0.73 / -0.57 | both halves | 1e-05 |  |
| [[FDX2]] | -0.60 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[NSUN5]] | -0.59 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[NT5C]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[LRRC8E]] | -0.58 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[NSMCE3]] | -0.58 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[TUBB2A]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PWWP2B]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SLC31A2]] | -0.56 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[ZNF579]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-23.6, -22.2); signed map (-24.9, -39.7). **Vector** length 115, 43.1% of its response variance represented; |z| ≥ 3 in 1,412 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +12.3 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | +12.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +11.8 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.5 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | -4.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.0 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | -7.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | -1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.4 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.1 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 9 superfamily member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:96,518,110-96,587,452 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMBP |
| Gene groups (HGNC) | Transmembrane 9 superfamily members |
| Matched by | ensembl_id |

UniProt [Q9HD45](https://www.uniprot.org/uniprotkb/Q9HD45) carries no function annotation.

**Summary**, from NCBI Gene [56889](https://www.ncbi.nlm.nih.gov/gene/56889):

> Predicted to be involved in protein localization to membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21529) · Entrez [56889](https://www.ncbi.nlm.nih.gov/gene/56889) · UniProt [Q9HD45](https://www.uniprot.org/uniprotkb/Q9HD45) · Ensembl [ENSG00000077147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077147)

## Data

Gene col 1174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1174); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1174]; `tensor/DDL_lfc|DDL_z.npy` [1174]; `embed/gene_vectors.npy` [1174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1174 or target_col == 1174). Every well: [[TM9SF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM9SF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
