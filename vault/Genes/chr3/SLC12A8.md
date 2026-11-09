---
symbol: "SLC12A8"
type: "gene"
col: 13322
ensembl_id: "ENSG00000221955"
name: "solute carrier family 12 member 8"
location: "3q21.2"
module: 4
arm: "+"
pooled_cpm: 48.87
n_lines_expressing: 33
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SLC12A8

*solute carrier family 12 member 8* — 3q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 5 µM: 2.28× (z +6.9, q 3e-09, up in 17 of 28 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 1.32× (z +3.6, q 0.048, up in 8 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 3 lines (A-172 8.81×, LOX-IMVI 4.81×, H4 2.80×); [[Panobinostat (drug)]] 5 µM in 3 lines (HOP62 8.65×, H4 8.37×, A-172 12.3×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HOP62 7.07×, A-172 9.77×, H4 5.19×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.328× (z -25.3, q 0e+00, down in 26 of 31 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.316× (z -17.8, q 0e+00, down in 27 of 31 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRP8]] (+0.50, fdr 3e-05), [[LINC02474]] (+0.50, fdr 9e-05), [[POLR3E]] (+0.50, fdr 3e-05); moves opposite to [[CLEC2B]] (-0.47, fdr 1e-04), [[AAMDC]] (-0.46, fdr 4e-05), [[TMEM107]] (-0.46, fdr 9e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC38A5]] → it (grade B ⚠); 7 go from it, the strongest it → [[BID]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13322.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 3 lines (A-172 8.81×, LOX-IMVI 4.81×, H4 2.80×); [[Panobinostat (drug)]] 5 µM in 3 lines (HOP62 8.65×, H4 8.37×, A-172 12.3×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HOP62 7.07×, A-172 9.77×, H4 5.19×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +6.9 | 3e-09 | 17/28 (A-172, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.8 | 4e-04 | 15/31 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.32×** | +4.5 | 0.001 | 9/30 (A-172, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.048 | 8/31 (NCI-H2347, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.32×** | +3.5 | 0.048 | 12/31 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.3 | 0.079 | 2/31 (HOP62, NCI-H1792) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.22× | +3.1 | 0.14 | 6/31 (SW1417, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.328×** | -25.3 | 0e+00 | 26/31 (HEC-1-A, SW1417, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.316×** | -17.8 | 0e+00 | 27/31 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.527×** | -10.3 | 2e-22 | 24/30 (SW480, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -9.0 | 2e-17 | 20/31 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.588×** | -8.5 | 2e-15 | 22/31 (LoVo, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.635×** | -7.3 | 3e-11 | 21/31 (HEC-1-A, KATO III, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.642×** | -7.1 | 1e-10 | 21/31 (KATO III, HT-29, …) | rises with dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.456×** | -6.6 | 3e-09 | 19/31 (SW48, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.707×** | -5.6 | 2e-06 | 16/31 (J82, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.714×** | -5.4 | 4e-06 | 18/31 (SW48, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.723×** | -5.2 | 1e-05 | 20/30 (SW48, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -5.2 | 1e-05 | 19/30 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.716×** | -5.0 | 3e-05 | 18/27 (LoVo, RKO, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.562×** | -4.8 | 5e-05 | 18/31 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.752×** | -4.6 | 2e-04 | 15/31 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.646×** | -3.7 | 0.007 | 15/31 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 71.2 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -19.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0959× (z -18.3) |
| [[LoVo (line)]] | wt | 69.4 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0323× (z -30.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0936× (z -23.0) |
| [[A498 (line)]] | wt | 49.2 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -21.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.166× (z -14.5) |
| [[KATO III (line)]] | alt | 54.6 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0757× (z -20.4) |
| [[LS 180 (line)]] | wt | 39.9 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -19.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0835× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 25.9 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -16.5) |
| [[SW1417 (line)]] | alt | 54.6 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -26.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.123× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 78.8 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -28.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.126× (z -21.4) |
| [[SW48 (line)]] | wt | 65.6 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0502× (z -19.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.114× (z -13.5) |
| [[SW480 (line)]] | alt | 43.1 | 0 | 8 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.117× (z -20.3) |
| [[A-172 (line)]] | wt | 20.5 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 8.81× (z +15.3) | — |
| [[BT-474 (line)]] | alt | 46.3 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -22.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.316× (z -8.8) |
| [[H4 (line)]] | wt | 77.3 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.37× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 43.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.162× (z -13.7) |
| [[J82 (line)]] | alt | 763 | 1 (1 ⚠) | 5 (3 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.75× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -16.7) |
| [[Panc 03.27 (line)]] | alt | 38.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -20.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.163× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 74.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -22.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.120× (z -12.3) |
| [[HOP62 (line)]] | alt | 22.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.65× (z +13.5) | — |
| [[NCI-H2347 (line)]] | alt | 32.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.50× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -18.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.145× (z -13.1) |
| [[A-427 (line)]] | wt | 32.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -16.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -8.6) |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.207× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 20.9 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.81× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 34.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.106× (z -11.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.136× (z -10.2) |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0941× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.59 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.77 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP8]] | +0.50 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[LINC02474]] | +0.50 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[POLR3E]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[SYK]] | +0.49 | +0.58 / +0.28 | both halves | 3e-04 |  |
| [[FAM222A-AS1]] | +0.49 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PINX1-1]] | +0.49 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[MTAP]] | +0.49 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[LARGE2]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[SEL1L3]] | +0.48 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[HKDC1]] | +0.48 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PUS1]] | +0.48 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[EIF4G3]] | +0.47 | +0.44 / +0.41 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLEC2B]] | -0.47 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[AAMDC]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TMEM107]] | -0.46 | -0.37 / -0.40 | both halves | 9e-05 |  |
| [[FAM161B]] | -0.46 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[LIX1L]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[OGA]] | -0.45 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[DCAF15]] | -0.45 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[DNAAF9]] | -0.45 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[HNRNPLL]] | -0.45 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[DMTF1]] | -0.44 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[ZC2HC1A]] | -0.44 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[CSPG4]] | -0.44 | -0.52 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC38A5]] | B | SLC38A5 activity raises SLC12A8's level | lines that do not express SLC38A5 (35) vs lines expressing it (15) | 1.90× lower at baseline in the lines without SLC38A5 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: XIST, HEPH, KRT5 |
| [[PSMB5]] | B | PSMB5 activity lowers SLC12A8's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02474]] | B | LINC02474 activity raises SLC12A8's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 1.94× lower at baseline in the lines without LINC02474 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975 |
| [[SLC38A5]] | B | SLC38A5 activity strengthens SLC12A8's drug response | lines that do not express SLC38A5 (20) vs lines expressing it (11) | the lines without SLC38A5 respond 0.56× as strongly (z diff +2.56); strongest at Panobinostat 5 µM: 0.74x vs 0.31x (z diff +4.3) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: XIST, HEPH, KRT5; target measured in part of the lines; artifact flags |
| [[LYPD6B]] | C | LYPD6B activity raises SLC12A8's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 2.76× lower at baseline in the lines without LYPD6B | 0.051 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BID]] | B | SLC12A8 activity raises BID's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 1.56× lower at baseline in the lines without SLC12A8 | 0.008 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[SPTBN2]] | B | SLC12A8 activity raises SPTBN2's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 2.09× lower at baseline in the lines without SLC12A8 | 0.031 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[DLK2]] | B | SLC12A8 activity lowers DLK2's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 1.91× higher at baseline in the lines without SLC12A8 | 0.033 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[LINC02474]] | B | SLC12A8 activity raises LINC02474's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without SLC12A8 | 0.058 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[PLAG1]] | B | SLC12A8 activity raises PLAG1's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 1.20× lower at baseline in the lines without SLC12A8 | 0.076 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[FRAS1]] | B | SLC12A8 activity raises FRAS1's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 2.30× lower at baseline in the lines without SLC12A8 | 0.088 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[SYK]] | C | SLC12A8 activity raises SYK's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 4.01× lower at baseline in the lines without SLC12A8 | 0.038 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.2, 46.4); signed map (13.1, -3.5). **Vector** length 102, 27.7% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.4 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.6 | +4.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.2 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.3 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -17.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.0 | -5.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 12 member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.2 — chr3:125,082,636-125,212,864 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CCC9 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 12 |
| Matched by | ensembl_id |

**Function**, from UniProt [A0AV02](https://www.uniprot.org/uniprotkb/A0AV02) (Solute carrier family 12 member 8):

> Cation/chloride cotransporter that may play a role in the control of keratinocyte proliferation.

**Summary**, from NCBI Gene [84561](https://www.ncbi.nlm.nih.gov/gene/84561):

> This gene is thought to be a candidate for psoriasis susceptibility. Several alternatively spliced transcript variants of this gene have been described, but the full-length nature of some of these variants has not been determined. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:15595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15595) · Entrez [84561](https://www.ncbi.nlm.nih.gov/gene/84561) · UniProt [A0AV02](https://www.uniprot.org/uniprotkb/A0AV02) · Ensembl [ENSG00000221955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221955)

## Data

Gene col 13322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13322); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13322]; `tensor/DDL_lfc|DDL_z.npy` [13322]; `embed/gene_vectors.npy` [13322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13322 or target_col == 13322). Every well: [[SLC12A8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC12A8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
