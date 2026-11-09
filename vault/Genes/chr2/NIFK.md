---
symbol: "NIFK"
type: "gene"
col: 7895
ensembl_id: "ENSG00000155438"
name: "nucleolar protein interacting with the FHA domain of MKI67"
location: "2q14.3"
module: 1
arm: "+"
pooled_cpm: 43.61
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NIFK

*nucleolar protein interacting with the FHA domain of MKI67* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 3.46× (z +11.5, q 7e-28, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.873× (z -4.0, q 0.033, down in 11 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Folic acid (drug)]] 5 µM: 0.759× (z -3.7, q 0.049, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.620×, NCI-H23 0.652×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF6]] (+0.82, fdr 7e-06), [[CEBPZ]] (+0.81, fdr 7e-06), [[UTP14A]] (+0.80, fdr 7e-06); moves opposite to [[CLSTN1]] (-0.67, fdr 7e-06), [[PRKACA]] (-0.66, fdr 1e-05), [[TMEM30A]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.46×** | +11.5 | 7e-28 | 45/47 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.75×** | +9.4 | 2e-18 | 47/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.56×** | +8.4 | 1e-14 | 39/48 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.82×** | +7.9 | 5e-13 | 39/47 (CFPAC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +7.0 | 3e-10 | 40/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.11×** | +6.9 | 4e-10 | 43/48 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +6.7 | 2e-09 | 43/46 (SW 900, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.95×** | +6.2 | 5e-08 | 38/48 (NCI-H2347, CFPAC-1, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.84×** | +5.7 | 9e-07 | 40/48 (SW 900, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.83×** | +5.6 | 1e-06 | 38/48 (SNU-423, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.79×** | +5.4 | 4e-06 | 33/48 (CFPAC-1, SNU-423, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.55×** | +4.5 | 3e-04 | 39/48 (NCI-H2347, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.55×** | +3.9 | 0.004 | 30/47 (HepG2/C3A, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.006 | 30/48 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +3.5 | 0.021 | 24/48 (NCI-H1792, SW 900, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.99×** | +3.3 | 0.028 | 27/48 (SW1417, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.064 | 26/48 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.064 | 25/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.064 | 23/48 (H4, HOP62, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +2.9 | 0.077 | 24/48 (A-172, SW 900, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.83×** | +2.9 | 0.077 | 17/48 (SW1417, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.83×** | +2.9 | 0.077 | 23/46 (SW1417, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7895.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.620×, NCI-H23 0.652×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.873× | -4.0 | 0.033 | 11/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.752×** | -3.8 | 0.045 | 32/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Folic acid (drug)]] 5 µM |  | **0.759×** | -3.7 | 0.049 | 29/48 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.698× | -3.2 | 0.16 | 24/48 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.782× | -3.2 | 0.16 | 28/48 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 21.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 10.9× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 30.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.22× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 28.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.85× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 50.0 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.70× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 32.8 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.80× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 59.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.01× (z +12.3) | [[Adagrasib (drug)]] 0.05 µM 0.652× (z -10.1) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 71.2 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.35× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 27.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.62× (z +13.4) | — |
| [[H4 (line)]] | wt | 34.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.89× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +10.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.78× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 25.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.93× (z +9.0) | — |
| [[SW480 (line)]] | alt | 53.8 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.41× (z +10.8) | — |
| [[A-172 (line)]] | wt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.88× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 66.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.51× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 49.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.10× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.53× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.620× (z -10.2) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 62.0 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.49× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 34.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.87× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 49.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.64× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 57.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +8.8) | — |
| [[A-427 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 74.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF6]] | +0.82 | +0.81 / +0.82 | both halves | 7e-06 | STRING 978 |
| [[CEBPZ]] | +0.81 | +0.78 / +0.85 | both halves | 7e-06 | STRING 951 |
| [[UTP14A]] | +0.80 | +0.86 / +0.75 | both halves | 7e-06 | STRING 805 |
| [[ZNF593]] | +0.79 | +0.77 / +0.80 | both halves | 7e-06 | STRING 982 |
| [[ESF1]] | +0.79 | +0.77 / +0.80 | both halves | 7e-06 | STRING 868 |
| [[BRIX1]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 | STRING 999 |
| [[REXO4]] | +0.77 | +0.82 / +0.76 | both halves | 7e-06 | STRING 623 |
| [[ZNF146]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.73 | +0.75 / +0.74 | both halves | 7e-06 | STRING 601 |
| [[EIF5B]] | +0.72 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 | STRING 623 |
| [[TRMT10C]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 | STRING 686 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLSTN1]] | -0.67 | -0.67 / -0.71 | both halves | 7e-06 |  |
| [[PRKACA]] | -0.66 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.66 | -0.56 / -0.72 | both halves | 1e-05 |  |
| [[TWSG1]] | -0.65 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[ITM2B]] | -0.65 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[TECR]] | -0.61 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[CALM3]] | -0.60 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[LAMP2]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[GGH]] | -0.60 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[ADD3]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.59 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[ATP6AP1]] | -0.59 | -0.47 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity strengthens NIFK's drug response | lines that do not express ADD3 (5) vs lines expressing it (43) | the lines without ADD3 respond 0.66× as strongly (z diff +1.75); strongest at Homoharringtonine 5 µM: 0.96x vs 1.97x (z diff +5.9) | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3; target measured in part of the lines; artifact flags |
| [[ADD3]] | B | ADD3 activity lowers NIFK's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.31× higher at baseline in the lines without ADD3 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-40.4, 0.8); signed map (-1.8, -20.5). **Vector** length 100, 34.9% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +7.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein interacting with the FHA domain of MKI67 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:121,726,945-121,736,911 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Nop15, Nopp34, hNIFK; previously MKI67IP |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

UniProt [Q9BYG3](https://www.uniprot.org/uniprotkb/Q9BYG3) carries no function annotation.

**Summary**, from NCBI Gene [84365](https://www.ncbi.nlm.nih.gov/gene/84365):

> This gene encodes a protein that interacts with the forkhead-associated domain of the Ki-67 antigen. The encoded protein may bind RNA and may play a role in mitosis and cell cycle progression. Multiple pseudogenes exist on chromosomes 5, 10, 12, 15, and 19.[provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:17838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17838) · Entrez [84365](https://www.ncbi.nlm.nih.gov/gene/84365) · UniProt [Q9BYG3](https://www.uniprot.org/uniprotkb/Q9BYG3) · Ensembl [ENSG00000155438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155438)

## Data

Gene col 7895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7895); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7895]; `tensor/DDL_lfc|DDL_z.npy` [7895]; `embed/gene_vectors.npy` [7895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7895 or target_col == 7895). Every well: [[NIFK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIFK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
