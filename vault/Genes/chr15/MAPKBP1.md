---
symbol: "MAPKBP1"
type: "gene"
col: 6066
ensembl_id: "ENSG00000137802"
name: "mitogen-activated protein kinase binding protein 1"
location: "15q15.1"
module: 29
arm: "-"
pooled_cpm: 41.02
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# MAPKBP1

*mitogen-activated protein kinase binding protein 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.81× (z +27.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.560× (z -15.0, q 0e+00, down in 29 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (C-33 A 0.184×, A-427 0.241×, SW48 0.157×, HEC-1-A 0.409×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C-33 A 0.0682×, RKO 0.193×, A549 0.287×, C32 0.367×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.371×, A498 0.365×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.346×).
> Its strongest partners by |cos| (72 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 29 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CELF1]] (+0.60, fdr 9e-05), [[VPS37C]] (+0.57, fdr 3e-04), [[MAP1S]] (+0.54, fdr 3e-04); moves opposite to [[CMPK1]] (-0.54, fdr 3e-05), [[HSPA14]] (-0.53, fdr 3e-05), [[PGM1]] (-0.53, fdr 6e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.81×** | +27.7 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.71×** | +26.8 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +22.5 | 0e+00 | 44/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +22.1 | 0e+00 | 40/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +15.2 | 0e+00 | 35/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +12.3 | 9e-33 | 38/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +10.6 | 3e-24 | 28/48 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +8.7 | 3e-16 | 31/47 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +7.9 | 2e-13 | 32/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +7.8 | 4e-13 | 30/48 (BT-474, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +7.1 | 5e-11 | 27/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +6.9 | 3e-10 | 25/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +6.5 | 4e-09 | 23/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +6.0 | 8e-08 | 22/47 (SW48, C32, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +6.0 | 8e-08 | 25/48 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +5.5 | 1e-06 | 21/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +5.2 | 8e-06 | 15/48 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +5.0 | 2e-05 | 21/48 (KATO III, HT-29, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6066.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (C-33 A 0.184×, A-427 0.241×, SW48 0.157×, HEC-1-A 0.409×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C-33 A 0.0682×, RKO 0.193×, A549 0.287×, C32 0.367×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.371×, A498 0.365×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.346×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.560×** | -15.0 | 0e+00 | 29/40 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.618×** | -12.9 | 9e-36 | 33/48 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.696×** | -9.0 | 4e-17 | 27/44 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~16% of this change | **0.813×** | -5.6 | 3e-06 | 22/46 (Hs 766T, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.871× | -3.4 | 0.069 | 14/47 (SW 900, NCI-H23, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 42.1 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +20.0) | — |
| [[J82 (line)]] | alt | 37.7 | 6 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.08× (z +18.1) | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 45.7 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 58.4 | 5 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.46× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 63.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.5) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0784× (z -11.6) ⚠ toxic |
| [[A498 (line)]] | wt | 41.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.60× (z +16.8) | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -10.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 49.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.80× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -11.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.0 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.21× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 39.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 47.1 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.96× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 40.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 26.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +12.6) | — |
| [[LoVo (line)]] | wt | 50.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 29.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.97× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 29.5 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 35.8 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +15.1) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.346× (z -8.8) |
| [[SW480 (line)]] | alt | 31.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +13.6) | — |
| [[A-172 (line)]] | wt | 38.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.6) | — |
| [[KATO III (line)]] | alt | 25.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.89× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.323× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 48.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.63× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 27.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 86.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 33.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.80× (z +11.2) | — |
| [[RKO (line)]] | wt | 63.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.68× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -16.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 31.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.46× (z +9.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.245× (z -10.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 72.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0682× (z -24.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.27× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 40.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 42.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +16.4) | — |
| [[SW1417 (line)]] | alt | 41.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +10.1) | — |
| [[A-427 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -13.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 24.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 52.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.34× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.118× (z -8.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -12.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 15 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CELF1]] | +0.60 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[VPS37C]] | +0.57 | +0.28 / +0.48 | both halves | 3e-04 |  |
| [[MAP1S]] | +0.54 | +0.28 / +0.51 | both halves | 3e-04 |  |
| [[MRPL14]] | +0.53 | +0.18 / +0.50 | ⚠ not reproduced | 1e-03 |  |
| [[CRTC1]] | +0.53 | +0.26 / +0.58 | both halves | 4e-04 |  |
| [[GGT7]] | +0.53 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[PUS3]] | +0.52 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[CYB561D1]] | +0.51 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[GTF2H5]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZNF316]] | +0.51 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[STX8]] | +0.50 | +0.27 / +0.43 | both halves | 3e-04 |  |
| [[WIPF2]] | +0.50 | +0.21 / +0.42 | both halves | 7e-04 |  |
| [[ZDHHC18]] | +0.49 | +0.35 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK1]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[HSPA14]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[PGM1]] | -0.53 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[KNTC1]] | -0.50 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[STRADB]] | -0.50 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[XNDC1N]] | -0.50 | -0.19 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[RAB27A]] | -0.50 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[SNHG31]] | -0.49 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[AIDA]] | -0.49 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[PRIMPOL]] | -0.49 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[HIPK1]] | -0.48 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[STX16]] | -0.48 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[RPN1]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF10]] | B | ZNF10 activity lowers MAPKBP1's level | lines that do not express ZNF10 (7) vs lines expressing it (43) | 1.22× higher at baseline in the lines without ZNF10 | 0.081 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.394). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-33.9, -23.3); signed map (-32.7, 1.2). **Vector** length 78.7, 16.4% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +26.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +8.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +3.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.0 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -15.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,774,434-41,827,855 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0596, NPHP20 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O60336](https://www.uniprot.org/uniprotkb/O60336) (Mitogen-activated protein kinase-binding protein 1):

> Negative regulator of NOD2 function. It down-regulates NOD2-induced processes such as activation of NF-kappa-B signaling, IL8 secretion and antibacterial response. Involved in JNK signaling pathway (By similarity).

**Summary**, from NCBI Gene [23005](https://www.ncbi.nlm.nih.gov/gene/23005):

> This gene encodes a scaffold protein that regulates the JNK (c-Jun N-terminal kinase) and NOD2 (nucleotide-binding oligomerization domain-containing protein 2) signaling pathways. The encoded protein interacts with another related JNK pathway scaffold protein, WDR62, via a conserved dimerization domain, and enhances JNK signaling. This protein may play a role in bacterial immunity by binding to the NOD2 receptor and negatively regulating downstream antibacterial and pro-inflammatory signaling. …

**Accessions** — [HGNC:29536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29536) · Entrez [23005](https://www.ncbi.nlm.nih.gov/gene/23005) · UniProt [O60336](https://www.uniprot.org/uniprotkb/O60336) · Ensembl [ENSG00000137802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137802)

## Data

Gene col 6066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6066); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6066]; `tensor/DDL_lfc|DDL_z.npy` [6066]; `embed/gene_vectors.npy` [6066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6066 or target_col == 6066). Every well: [[MAPKBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPKBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
