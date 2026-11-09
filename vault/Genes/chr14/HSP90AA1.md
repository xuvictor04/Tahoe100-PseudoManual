---
symbol: "HSP90AA1"
type: "gene"
col: 1294
ensembl_id: "ENSG00000080824"
name: "heat shock protein 90 alpha family class A member 1"
location: "14q32.31"
module: 60
arm: "+"
pooled_cpm: 957.09
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSP90AA1

*heat shock protein 90 alpha family class A member 1* — 14q32.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 13.9× (z +24.9, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.319×, A-427 0.424×, C-33 A 0.392×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SHP-77 0.345×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.728×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90AA2P]] (+0.83, fdr 7e-06), [[HSP90AB1]] (+0.80, fdr 7e-06), [[CCT4]] (+0.79, fdr 7e-06); moves opposite to [[YY1AP1]] (-0.64, fdr 1e-05), [[PER1]] (-0.55, fdr 1e-05), [[TNRC6C]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CHORDC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **13.9×** | +24.9 | 0e+00 | 48/48 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **13.9×** | +24.9 | 0e+00 | 48/48 (HT-29, C32, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **13.0×** | +24.2 | 0e+00 | 48/48 (HT-29, hTERT-HPNE, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **8.00×** | +18.6 | 0e+00 | 48/48 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **6.56×** | +17.8 | 0e+00 | 49/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **5.80×** | +16.0 | 0e+00 | 44/44 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.72×** | +11.5 | 1e-28 | 45/45 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **8.22×** | +10.4 | 1e-23 | 45/45 (CFPAC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **2.90×** | +9.7 | 2e-20 | 46/47 (COLO 205, C32, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **6.50×** | +9.3 | 1e-18 | 47/47 (A-172, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **4.70×** | +9.0 | 2e-17 | 49/49 (CFPAC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.15×** | +7.2 | 2e-11 | 45/48 (SK-MEL-2, A-172, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.94×** | +6.3 | 2e-08 | 42/48 (hTERT-HPNE, HOP62, …) | two highest doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.52×** | +5.6 | 1e-06 | 47/48 (CHP-212, MIA PaCa-2, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **3.07×** | +5.5 | 1e-06 | 45/48 (BT-474, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.76×** | +5.1 | 9e-06 | 38/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 5e-04 | 39/47 (HOP62, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.004 | 35/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 0.05 µM |  | **1.49×** | +3.5 | 0.011 | 42/49 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.018 | 37/48 (A549, NCI-H1792, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.056 | 35/48 (A549, HS-578T, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.064 | 37/48 (A498, A-427, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 5 µM |  | **1.24×** | +2.8 | 0.089 | 29/48 (NCI-H460, J82, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.319×, A-427 0.424×, C-33 A 0.392×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SHP-77 0.345×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.728×; ⚠ position not correctable).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 585 | 13 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 22.8× (z +25.0) | — |
| [[C32 (line)]] | wt | 576 | 13 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 45.7× (z +28.4) | — |
| [[hTERT-HPNE (line)]] | wt | 531 | 13 (8 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 28.6× (z +26.2) | — |
| [[NCI-H1792 (line)]] | alt | 383 | 13 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +20.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 10.7× (z +17.8) | — |
| [[SHP-77 (line)]] | alt | 1,561 | 11 (6 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 14.1× (z +22.2) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 616 | 12 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.8× (z +18.8) | — |
| [[CFPAC-1 (line)]] | alt | 907 | 12 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.4× (z +25.4) | — |
| [[SK-MEL-2 (line)]] | alt | 1,135 | 12 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 20.4× (z +24.1) | — |
| [[SNU-423 (line)]] | alt | 480 | 12 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 29.7× (z +24.8) | — |
| [[HS-578T (line)]] | alt | 532 | 11 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 23.7× (z +24.4) | — |
| [[HT-29 (line)]] | alt | 540 | 11 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 32.7× (z +28.9) | — |
| [[SW 900 (line)]] | alt | 861 | 11 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 21.1× (z +26.4) | — |
| [[A549 (line)]] | wt | 516 | 10 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.3× (z +20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 22.1× (z +20.8) | — |
| [[H4 (line)]] | wt | 447 | 10 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 23.5× (z +20.3) | — |
| [[HOP62 (line)]] | alt | 860 | 10 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 30.6× (z +21.4) | — |
| [[Panc 03.27 (line)]] | alt | 874 | 10 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 22.5× (z +27.1) | — |
| [[SW1417 (line)]] | alt | 869 | 10 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 17.6× (z +26.5) | — |
| [[A498 (line)]] | wt | 590 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 15.1× (z +21.5) | — |
| [[COLO 205 (line)]] | alt | 434 | 9 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 26.1× (z +21.5) | — |
| [[HepG2_C3A (line)]] | wt | 735 | 9 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.68× (z +15.7) | — |
| [[J82 (line)]] | alt | 900 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 13.9× (z +21.2) | — |
| [[LOX-IMVI (line)]] | wt | 927 | 9 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.3× (z +18.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 1,348 | 9 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +18.7) | — |
| [[RPMI-7951 (line)]] | alt | 623 | 9 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.0× (z +23.8) | — |
| [[CHP-212 (line)]] | wt | 881 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 16.1× (z +19.7) | — |
| [[Hs 766T (line)]] | wt | 375 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 19.4× (z +21.5) | — |
| [[KATO III (line)]] | alt | 1,216 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 14.2× (z +20.1) | — |
| [[LoVo (line)]] | wt | 691 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 21.6× (z +23.2) | — |
| [[NCI-H1573 (line)]] | alt | 499 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 13.1× (z +16.4) | — |
| [[NCI-H2347 (line)]] | alt | 1,758 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 13.9× (z +23.0) | — |
| [[NCI-H460 (line)]] | wt | 848 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.9× (z +17.5) | — |
| [[SW 1271 (line)]] | alt | 985 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 29.9× (z +20.3) | — |
| [[HEC-1-A (line)]] | alt | 997 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 22.6× (z +24.0) | — |
| [[PANC-1 (line)]] | alt | 531 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.27× (z +18.9) | — |
| [[SNU-1 (line)]] | wt | 870 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 18.7× (z +24.1) | — |
| [[SW480 (line)]] | alt | 1,594 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 17.5× (z +20.4) | — |
| [[A-427 (line)]] | wt | 1,968 | 5 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.21× (z +16.5) | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 913 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 15.6× (z +20.4) | — |
| [[BT-474 (line)]] | alt | 1,494 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 18.0× (z +26.0) | — |
| [[LS 180 (line)]] | wt | 1,127 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 15.1× (z +19.0) | — |
| [[NCI-H2030 (line)]] | alt | 2,433 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.18× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 874 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.20× (z +17.6) | — |
| [[RKO (line)]] | wt | 1,017 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.5× (z +20.9) | — |
| [[SW48 (line)]] | wt | 1,693 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.6× (z +18.3) | — |
| [[HCT15 (line)]] | alt | 1,294 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.95× (z +13.7) | — |
| [[SW 1088 (line)]] | alt | 587 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 35.0× (z +16.5) | — |
| [[C-33 A (line)]] | alt | 1,597 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 11.8× (z +18.8) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 1,086 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.6× (z +13.6) | — |
| [[NCI-H2122 (line)]] | alt | 948 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 899 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AA2P]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AB1]] | +0.80 | +0.75 / +0.82 | both halves | 7e-06 | same gene group; pathway: Assembly and release of respiratory syncytial virus (RSV) virions; STRING 997 |
| [[CCT4]] | +0.79 | +0.74 / +0.79 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium; STRING 783 |
| [[HSPD1]] | +0.78 | +0.75 / +0.79 | both halves | 7e-06 | STRING 963 |
| [[CACYBP]] | +0.78 | +0.72 / +0.82 | both halves | 7e-06 | STRING 863 |
| [[HSP90AB3P]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[HSPA8]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | pathway: Attenuation phase; STRING 999 |
| [[STIP1]] | +0.73 | +0.79 / +0.70 | both halves | 7e-06 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 999 |
| [[HSPE1]] | +0.73 | +0.72 / +0.76 | both halves | 7e-06 | STRING 942 |
| [[TCP1]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium; STRING 906 |
| [[CCT3]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium; STRING 767 |
| [[HSP90AB2P]] | +0.70 | +0.67 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1AP1]] | -0.64 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[PER1]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 | pathway: Cilium Assembly |
| [[ETFRF1]] | -0.53 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[LSM14B]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PHPT1]] | -0.52 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[POLR1H]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RSPRY1]] | -0.51 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[CMC4]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[COQ9]] | -0.51 | -0.38 / -0.49 | both halves | 7e-05 | pathway: Metabolism of cofactors |
| [[METTL25B]] | -0.51 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[FAM200B]] | -0.51 | -0.29 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHORDC1]] | C | CHORDC1's natural level strengthens HSP90AA1's drug response | CHORDC1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.13; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.844). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.7, -11.4); signed map (-26.1, -28.9). **Vector** length 110, 54.4% of its response variance represented; |z| ≥ 3 in 1,518 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of HSF1-mediated heat shock response* (reactome, mean cos +0.53 to 13); *mTORC1 signaling* (hallmark, mean cos +0.58 to 13); *AUF1 (hnRNP D0) binds and destabilizes mRNA* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.9 | +18.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.8 | +24.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.8 | +24.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.0 | +24.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +9.0 | +10.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.7 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +3.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.2 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein 90 alpha family class A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.31 — chr14:102,080,742-102,139,699 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hsp89, Hsp90, FLJ31884, HSP90N; previously HSPC1, HSPCA, HSPCAL4 |
| Gene groups (HGNC) | Heat shock 90kDa proteins |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 112 pathways, smallest: Assembly and release of respiratory syncytial virus (RSV) virions; Respiratory syncytial virus genome replication; Drug resistance in ERBB2 KD mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P07900](https://www.uniprot.org/uniprotkb/P07900) (Heat shock protein HSP 90-alpha):

> Molecular chaperone that promotes the maturation, structural maintenance and proper regulation of specific target proteins involved for instance in cell cycle control and signal transduction. Undergoes a functional cycle that is linked to its ATPase activity which is essential for its chaperone activity. This cycle probably induces conformational changes in the client proteins, thereby causing their activation. Interacts dynamically with various co-chaperones that modulate its substrate …

**Summary**, from NCBI Gene [3320](https://www.ncbi.nlm.nih.gov/gene/3320):

> The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:5253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5253) · Entrez [3320](https://www.ncbi.nlm.nih.gov/gene/3320) · UniProt [P07900](https://www.uniprot.org/uniprotkb/P07900) · Ensembl [ENSG00000080824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080824)

## Data

Gene col 1294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1294); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1294]; `tensor/DDL_lfc|DDL_z.npy` [1294]; `embed/gene_vectors.npy` [1294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1294 or target_col == 1294). Every well: [[HSP90AA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSP90AA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
