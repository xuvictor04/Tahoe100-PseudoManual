---
symbol: "BNIP3L"
type: "gene"
col: 2495
ensembl_id: "ENSG00000104765"
name: "BCL2 interacting protein 3 like"
location: "8p21.2"
module: 79
arm: "+"
pooled_cpm: 340.56
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 33
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# BNIP3L

*BCL2 interacting protein 3 like* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.39× (z +6.0, q 9e-07, up in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 9 lines (SHP-77 2.69×, MIA PaCa-2 2.12×, SNU-423 1.96×, SNU-1 2.58×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 2.37×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SNU-1 5.16×).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.285× (z -32.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNMT]] (+0.74, fdr 7e-06), [[FAM117B]] (+0.71, fdr 7e-06), [[PAIP2]] (+0.70, fdr 7e-06); moves opposite to [[YTHDC2]] (-0.59, fdr 7e-06), [[GPATCH4]] (-0.58, fdr 1e-05), [[LTV1]] (-0.58, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DPYSL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2495.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 9 lines (SHP-77 2.69×, MIA PaCa-2 2.12×, SNU-423 1.96×, SNU-1 2.58×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 2.37×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SNU-1 5.16×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +6.0 | 9e-07 | 28/48 (SHP-77, MIA PaCa-2, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.78×** | +5.6 | 8e-06 | 43/48 (RPMI-7951, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.16× | +4.0 | 0.011 | 16/48 (KATO III, SHP-77, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.28× | +3.2 | 0.18 | 23/48 (HOP62, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.285×** | -32.7 | 0e+00 | 47/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.276×** | -23.7 | 0e+00 | 48/48 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.302×** | -21.2 | 0e+00 | 48/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.374×** | -18.1 | 0e+00 | 48/48 (A498, AsPC-1, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.489×** | -12.7 | 8e-35 | 44/47 (NCI-H1573, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.543×** | -11.2 | 2e-27 | 43/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.552×** | -10.5 | 6e-24 | 44/47 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.669×** | -10.5 | 9e-24 | 39/48 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.586×** | -9.8 | 4e-21 | 43/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.586×** | -9.8 | 4e-21 | 40/48 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.694×** | -9.5 | 1e-19 | 35/49 (NCI-H2030, A549, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.383×** | -9.2 | 1e-18 | 48/48 (AsPC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.400×** | -8.8 | 5e-17 | 45/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.607×** | -8.8 | 5e-17 | 36/44 (NCI-H1573, Hs 766T, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.404×** | -8.7 | 1e-16 | 46/48 (A498, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.438×** | -8.0 | 6e-14 | 46/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -7.6 | 7e-13 | 40/48 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.518×** | -6.3 | 7e-09 | 44/48 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.629×** | -6.1 | 3e-08 | 39/48 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -5.6 | 5e-07 | 27/48 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.744×** | -5.4 | 1e-06 | 42/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.740×** | -5.3 | 2e-06 | 32/48 (NCI-H1573, RKO, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.706×** | -4.6 | 1e-04 | 42/49 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 855 | 0 | 14 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.312× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 571 | 1 | 13 (6 ⚠) | [[Auranofin (drug)]] 5 µM 2.12× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -32.8) |
| [[AsPC-1 (line)]] | alt | 796 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -40.1) |
| [[hTERT-HPNE (line)]] | wt | 724 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -20.9) |
| [[A-172 (line)]] | wt | 531 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -30.4) |
| [[NCI-H1573 (line)]] | alt | 451 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -36.7) |
| [[RPMI-7951 (line)]] | alt | 519 | 0 | 12 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.357× (z -14.0) |
| [[H4 (line)]] | wt | 543 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -19.9) |
| [[HEC-1-A (line)]] | alt | 326 | 1 | 10 (5 ⚠) | [[Auranofin (drug)]] 5 µM 1.77× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -23.9) |
| [[HOP62 (line)]] | alt | 387 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -28.2) |
| [[HCT15 (line)]] | alt | 654 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 392 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -30.6) |
| [[SK-MEL-2 (line)]] | alt | 354 | 1 | 9 (6 ⚠) | [[Auranofin (drug)]] 5 µM 1.82× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.376× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 304 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -33.3) |
| [[Hs 766T (line)]] | wt | 454 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -34.8) |
| [[J82 (line)]] | alt | 195 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 277 | 2 (2 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.208× (z -17.4) |
| [[SNU-1 (line)]] | wt | 395 | 2 | 7 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.58× (z +10.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.0562× (z -30.9) |
| [[SW 900 (line)]] | alt | 311 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -26.2) |
| [[A498 (line)]] | wt | 184 | 0 | 8 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.202× (z -22.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.175× (z -12.9) |
| [[PANC-1 (line)]] | alt | 172 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -23.5) |
| [[SNU-423 (line)]] | alt | 308 | 1 | 7 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.96× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -27.7) |
| [[A-427 (line)]] | wt | 261 | 1 | 6 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.96× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -22.0) |
| [[C32 (line)]] | wt | 299 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.258× (z -16.5) |
| [[HepG2_C3A (line)]] | wt | 313 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -28.7) |
| [[NCI-H2030 (line)]] | alt | 526 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -27.7) |
| [[A549 (line)]] | wt | 401 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -30.7) |
| [[KATO III (line)]] | alt | 253 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.07× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -18.6) |
| [[LOX-IMVI (line)]] | wt | 230 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 487 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -25.3) |
| [[Panc 03.27 (line)]] | alt | 211 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -27.4) |
| [[SW480 (line)]] | alt | 225 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.213× (z -18.3) |
| [[NCI-H1792 (line)]] | alt | 358 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -13.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -13.4) |
| [[RKO (line)]] | wt | 182 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -18.5) |
| [[SHP-77 (line)]] | alt | 311 | 1 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.69× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -22.8) |
| [[SW48 (line)]] | wt | 361 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -16.6) |
| [[BT-474 (line)]] | alt | 242 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -17.2) |
| [[C-33 A (line)]] | alt | 311 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -20.0) |
| [[COLO 205 (line)]] | alt | 231 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.0) |
| [[HT-29 (line)]] | alt | 121 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -21.4) |
| [[LoVo (line)]] | wt | 228 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.38× (z +9.8) | [[Harringtonine (drug)]] 5 µM 0.302× (z -13.0) |
| [[LS 180 (line)]] | wt | 288 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -22.6) |
| [[CHP-212 (line)]] | wt | 343 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.0) |
| [[SW 1088 (line)]] | alt | 391 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.211× (z -9.3) |
| [[SW1417 (line)]] | alt | 111 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -12.1) |
| [[AN3 CA (line)]] | alt | 261 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.342× (z -8.9) |
| [[SW 1271 (line)]] | alt | 287 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.7) |
| [[NCI-H2122 (line)]] | alt | 454 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 374 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNMT]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[FAM117B]] | +0.71 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[PAIP2]] | +0.70 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[NDRG1]] | +0.68 | +0.80 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[PNPLA8]] | +0.66 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.65 | +0.81 / +0.54 | both halves | 1e-05 |  |
| [[MXI1]] | +0.65 | +0.71 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM; STRING 591 |
| [[ANKRD37]] | +0.65 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[TCP11L2]] | +0.65 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[NARF]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[UBXN7]] | +0.63 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[SNX25]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YTHDC2]] | -0.59 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.58 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[LTV1]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.58 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[UTP20]] | -0.57 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SMARCB1]] | -0.55 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[MCCC2]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[DHX37]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[POGK]] | -0.54 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[MTPAP]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SLC5A6]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[RAD51D]] | -0.54 | -0.46 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPYSL2]] | B | DPYSL2 activity raises BNIP3L's level | lines that do not express DPYSL2 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without DPYSL2 | 0.083 | ⚠ within organs, on part of the lines; also absent: PHLDA1, PARP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.2, -13.3); signed map (-35.0, 27.0). **Vector** length 142, 58.6% of its response variance represented; |z| ≥ 3 in 1,977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.5 | +6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +7.7 | -11.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +7.5 | -9.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +7.1 | -9.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +6.1 | +5.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.5 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.1 | +2.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.7 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.7 | -18.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -10.5 | -8.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -10.3 | -9.2 |
|  | [[EX229 (drug)]] 5 µM |  | -10.0 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.8 | -21.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -9.1 | -8.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.7 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 interacting protein 3 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:26,383,054-26,505,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Nix, BNIP3a |
| Hallmark sets | APOPTOSIS, HEME_METABOLISM, HYPOXIA |
| Reactome | 3 pathways, smallest: TP53 Regulates Transcription of Genes Involved in Cytochrome C Release; TP53 Regulates Transcription of Cell Death Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [O60238](https://www.uniprot.org/uniprotkb/O60238) (BCL2/adenovirus E1B 19 kDa protein-interacting protein 3-like):

> Induces apoptosis. Interacts with viral and cellular anti-apoptosis proteins. Can overcome the suppressors BCL-2 and BCL-XL, although high levels of BCL-XL expression will inhibit apoptosis. Inhibits apoptosis induced by BNIP3. Involved in mitochondrial quality control via its interaction with SPATA18/MIEAP: in response to mitochondrial damage, participates in mitochondrial protein catabolic process (also named MALM) leading to the degradation of damaged proteins inside mitochondria. The …

**Summary**, from NCBI Gene [665](https://www.ncbi.nlm.nih.gov/gene/665):

> This gene encodes a protein that belongs to the pro-apoptotic subfamily within the Bcl-2 family of proteins. The encoded protein binds to Bcl-2 and possesses the BH3 domain. The protein directly targets mitochondria and causes apoptotic changes, including loss of membrane potential and the release of cytochrome c. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:1085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1085) · Entrez [665](https://www.ncbi.nlm.nih.gov/gene/665) · UniProt [O60238](https://www.uniprot.org/uniprotkb/O60238) · Ensembl [ENSG00000104765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104765)

## Data

Gene col 2495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2495); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2495]; `tensor/DDL_lfc|DDL_z.npy` [2495]; `embed/gene_vectors.npy` [2495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2495 or target_col == 2495). Every well: [[BNIP3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BNIP3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
