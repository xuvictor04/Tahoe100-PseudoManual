---
symbol: "ALDOA"
type: "gene"
col: 7415
ensembl_id: "ENSG00000149925"
name: "aldolase, fructose-bisphosphate A"
location: "16p11.2"
module: 99
arm: "+"
pooled_cpm: 447.92
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# ALDOA

*aldolase, fructose-bisphosphate A* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.99× (z +8.5, q 9e-15, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.286× (z -21.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGK1]] (+0.78, fdr 7e-06), [[GAPDH]] (+0.71, fdr 7e-06), [[HK2]] (+0.68, fdr 9e-06); moves opposite to [[KLHL42]] (-0.65, fdr 5e-05), [[ZBTB8A]] (-0.64, fdr 4e-05), [[RNF115]] (-0.62, fdr 5e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +8.5 | 9e-15 | 43/48 (A-172, HOP62, …) | two highest doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +6.5 | 3e-08 | 38/48 (A-172, HOP62, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +5.4 | 1e-05 | 38/48 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.54×** | +5.3 | 2e-05 | 45/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.031 | 39/48 (Hs 766T, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.73×** | +3.5 | 0.040 | 35/48 (RKO, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.042 | 36/49 (C32, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.286×** | -21.9 | 0e+00 | 48/48 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.447×** | -9.9 | 8e-21 | 47/48 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.471×** | -8.9 | 8e-17 | 44/48 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.532×** | -7.5 | 9e-12 | 44/47 (HepG2/C3A, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -7.4 | 2e-11 | 39/49 (HCT15, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -5.2 | 2e-05 | 38/47 (Panc 03.27, HCT15, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.717×** | -4.1 | 0.003 | 43/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.614× | -3.1 | 0.12 | 38/49 (BT-474, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.623× | -3.1 | 0.14 | 35/48 (COLO 205, AN3 CA, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 817 | 1 | 6 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -23.1) |
| [[SW480 (line)]] | alt | 288 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -20.7) |
| [[A-172 (line)]] | wt | 508 | 3 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.90× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.6) |
| [[BT-474 (line)]] | alt | 400 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -20.3) |
| [[LoVo (line)]] | wt | 441 | 1 | 4 | [[Panobinostat (drug)]] 0.5 µM 2.27× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -16.4) |
| [[RKO (line)]] | wt | 489 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -21.4) |
| [[C-33 A (line)]] | alt | 359 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.7) |
| [[H4 (line)]] | wt | 485 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.64× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -19.9) |
| [[HEC-1-A (line)]] | alt | 354 | 1 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.37× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.1) |
| [[HOP62 (line)]] | alt | 476 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -15.6) |
| [[HT-29 (line)]] | alt | 502 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -23.0) |
| [[LOX-IMVI (line)]] | wt | 545 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -22.3) |
| [[MIA PaCa-2 (line)]] | alt | 612 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -21.3) |
| [[NCI-H1573 (line)]] | alt | 781 | 1 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -24.8) |
| [[NCI-H2347 (line)]] | alt | 456 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -28.2) |
| [[SK-MEL-2 (line)]] | alt | 420 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -19.8) |
| [[HepG2_C3A (line)]] | wt | 487 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -20.1) |
| [[HS-578T (line)]] | alt | 370 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.75× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -18.6) |
| [[KATO III (line)]] | alt | 559 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -25.0) |
| [[LS 180 (line)]] | wt | 502 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -20.8) |
| [[Panc 03.27 (line)]] | alt | 440 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -25.9) |
| [[PANC-1 (line)]] | alt | 504 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 414 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -17.8) |
| [[SW1417 (line)]] | alt | 412 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -19.2) |
| [[SW48 (line)]] | wt | 389 | 1 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -19.5) |
| [[A-427 (line)]] | wt | 338 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -25.3) |
| [[A498 (line)]] | wt | 320 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 362 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -20.0) |
| [[AsPC-1 (line)]] | alt | 551 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -24.3) |
| [[C32 (line)]] | wt | 599 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 582 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.18× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -19.6) |
| [[hTERT-HPNE (line)]] | wt | 492 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 252 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 337 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.1) |
| [[SHP-77 (line)]] | alt | 451 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.39× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -17.7) |
| [[SNU-1 (line)]] | wt | 543 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -21.3) |
| [[SNU-423 (line)]] | alt | 442 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.26× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.4) |
| [[SW 900 (line)]] | alt | 405 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -18.8) |
| [[A549 (line)]] | wt | 359 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -14.1) |
| [[CHP-212 (line)]] | wt | 281 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -16.5) |
| [[COLO 205 (line)]] | alt | 408 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.7) |
| [[Hs 766T (line)]] | wt | 594 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -12.0) |
| [[J82 (line)]] | alt | 507 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 291 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 312 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.6) |
| [[NCI-H661 (line)]] | alt | 257 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -14.7) |
| [[SW 1088 (line)]] | alt | 609 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.4) |
| [[SW 1271 (line)]] | alt | 733 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -19.2) |
| [[NCI-H2122 (line)]] | alt | 427 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 423 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGK1]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 962 |
| [[GAPDH]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 999 |
| [[HK2]] | +0.68 | +0.67 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 921 |
| [[LDHA]] | +0.66 | +0.70 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 973 |
| [[NCKIPSD]] | +0.66 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[NXPH4]] | +0.66 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[ENO1]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 988 |
| [[BRK1]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[SLC2A1]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 672 |
| [[ERO1A]] | +0.63 | +0.67 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[P4HB]] | +0.63 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[BSG]] | +0.63 | +0.70 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_UP |

## Genes that move opposite

*40 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL42]] | -0.65 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[ZBTB8A]] | -0.64 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[RNF115]] | -0.62 | -0.66 / -0.39 | both halves | 5e-05 |  |
| [[POLR3C]] | -0.61 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[GABPB2]] | -0.61 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[FBXO4]] | -0.60 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[SLTM]] | -0.59 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[ITPA]] | -0.59 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[GABPB1]] | -0.59 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[FAIM]] | -0.59 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[PPP3CB-AS1]] | -0.59 | -0.52 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[CCAR1]] | -0.58 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[UPF3A]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ALDOA's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NDRG1]] | B | NDRG1 activity raises ALDOA's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.26× lower at baseline in the lines without NDRG1 | 0.086 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, -15.2); signed map (-37.2, 28.3). **Vector** length 159, 61.0% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.56 to 7); *Regulation of pyruvate metabolism* (reactome, mean cos +0.55 to 4); *Pyruvate metabolism* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +14.1 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +13.1 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +11.5 | +5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.0 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.7 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +3.2 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.3 | -21.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.2 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -9.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -8.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -6.4 | -4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.6 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.1 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | aldolase, fructose-bisphosphate A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,064,164-30,070,457 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Aldolase, fructose-bisphosphate family |
| Hallmark sets | FATTY_ACID_METABOLISM, UV_RESPONSE_UP, GLYCOLYSIS, HYPOXIA, ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 10 pathways, smallest: Gluconeogenesis; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P04075](https://www.uniprot.org/uniprotkb/P04075) (Fructose-bisphosphate aldolase A):

> Catalyzes the reversible conversion of beta-D-fructose 1,6-bisphosphate (FBP) into two triose phosphate and plays a key role in glycolysis and gluconeogenesis. In addition, also functions as a scaffolding protein (By similarity). In response to glucose deprivation, FBP dissociates from aldolase and acts as an adapter that promotes AMP-activated protein kinase (AMPK) activity: mechanistically, associates with transient receptor potential channels TrpV (TRPV1-TRPV4), promoting inhibition of the …

**Summary**, from NCBI Gene [226](https://www.ncbi.nlm.nih.gov/gene/226):

> This gene encodes a member of the class I fructose-bisphosphate aldolase protein family. The encoded protein is a glycolytic enzyme that catalyzes the reversible conversion of fructose-1,6-bisphosphate to glyceraldehyde 3-phosphate and dihydroxyacetone phosphate. Three aldolase isozymes (A, B, and C), encoded by three different genes, are differentially expressed during development. Mutations in this gene have been associated with Glycogen Storage Disease XII, an autosomal recessive disorder …

**Accessions** — [HGNC:414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:414) · Entrez [226](https://www.ncbi.nlm.nih.gov/gene/226) · UniProt [P04075](https://www.uniprot.org/uniprotkb/P04075) · Ensembl [ENSG00000149925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149925)

## Data

Gene col 7415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7415); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7415]; `tensor/DDL_lfc|DDL_z.npy` [7415]; `embed/gene_vectors.npy` [7415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7415 or target_col == 7415). Every well: [[ALDOA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDOA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
