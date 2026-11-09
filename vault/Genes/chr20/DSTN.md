---
symbol: "DSTN"
type: "gene"
col: 4683
ensembl_id: "ENSG00000125868"
name: "destrin, actin depolymerizing factor"
location: "20p12.1"
module: 45
arm: "+"
pooled_cpm: 295.19
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# DSTN

*destrin, actin depolymerizing factor* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +16.2, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.80×, A549 6.63×, HOP62 4.70×, HS-578T 5.70×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 3.95×, A549 5.03×, HOP62 4.04×, NCI-H460 4.95×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (PANC-1 3.18×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.743× (z -3.8, q 0.071, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-1 0.397×, NCI-H2347 0.463×, LS 180 0.509×, SW480 0.574×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL6IP5]] (+0.66, fdr 1e-05), [[PPP1CB]] (+0.60, fdr 1e-05), [[FXR1]] (+0.56, fdr 1e-05); moves opposite to [[EMG1]] (-0.56, fdr 4e-05), [[NIP7]] (-0.56, fdr 3e-05), [[ZNF562]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4683.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.80×, A549 6.63×, HOP62 4.70×, HS-578T 5.70×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 3.95×, A549 5.03×, HOP62 4.04×, NCI-H460 4.95×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (PANC-1 3.18×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +16.2 | 0e+00 | 49/49 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +12.0 | 9e-31 | 44/44 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.55×** | +11.8 | 7e-30 | 43/45 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.34×** | +4.0 | 0.009 | 32/48 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.38×** | +3.9 | 0.012 | 31/47 (C32, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4683.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SNU-1 0.397×, NCI-H2347 0.463×, LS 180 0.509×, SW480 0.574×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.743×** | -3.8 | 0.071 | 34/48 (NCI-H2347, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.076 | 26/48 (SNU-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 267 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +15.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 178 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 342 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 263 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -8.7) |
| [[A498 (line)]] | wt | 429 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +14.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 382 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +18.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 142 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +12.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 332 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 310 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +17.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 478 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 450 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +16.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 231 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +12.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 218 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 328 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 211 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 94.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.62× (z +16.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 134 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 195 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +15.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 437 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +19.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 451 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 210 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +13.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 246 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 166 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.21× (z +11.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 188 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +13.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 184 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +11.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 551 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 230 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 196 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +13.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.03× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 448 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 205 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 303 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 245 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 299 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 325 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 377 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 172 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 412 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.9) |
| [[SW 900 (line)]] | alt | 320 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 187 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 196 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +11.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 400 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 247 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 441 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 441 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 235 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6IP5]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PPP1CB]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[FXR1]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PEBP1]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[YPEL2]] | +0.55 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ATP6V1A]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[FNBP1L]] | +0.54 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[RALBP1]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[VAT1]] | +0.52 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[TKT]] | +0.52 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ANXA11]] | +0.52 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[JAK1]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMG1]] | -0.56 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[NIP7]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ZNF562]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[AFG3L1P]] | -0.53 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[SPOUT1]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ZNF41]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[PUS1]] | -0.52 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[TTC4]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CD2BP2]] | -0.51 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[RPAP1]] | -0.50 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[ST3GAL3]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MTG2]] | -0.50 | -0.39 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-5.5, -8.2); signed map (-32.2, -16.1). **Vector** length 101, 36.7% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +1.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.5 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +1.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.4 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.7 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -2.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | -4.0 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | destrin, actin depolymerizing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:17,570,075-17,609,919 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADF, ACTDP |
| Gene groups (HGNC) | Cofilin family |
| Matched by | ensembl_id |

**Function**, from UniProt [P60981](https://www.uniprot.org/uniprotkb/P60981) (Destrin):

> Actin-depolymerizing protein. Severs actin filaments (F-actin) and binds to actin monomers (G-actin). Acts in a pH-independent manner.

**Summary**, from NCBI Gene [11034](https://www.ncbi.nlm.nih.gov/gene/11034):

> The product of this gene belongs to the actin-binding proteins ADF family. This family of proteins is responsible for enhancing the turnover rate of actin in vivo. This gene encodes the actin depolymerizing protein that severs actin filaments (F-actin) and binds to actin monomers (G-actin). Two transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15750) · Entrez [11034](https://www.ncbi.nlm.nih.gov/gene/11034) · UniProt [P60981](https://www.uniprot.org/uniprotkb/P60981) · Ensembl [ENSG00000125868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125868)

## Data

Gene col 4683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4683); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4683]; `tensor/DDL_lfc|DDL_z.npy` [4683]; `embed/gene_vectors.npy` [4683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4683 or target_col == 4683). Every well: [[DSTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
