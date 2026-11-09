---
symbol: "SOX12"
type: "gene"
col: 10861
ensembl_id: "ENSG00000177732"
name: "SRY-box transcription factor 12"
location: "20p13"
module: 3
arm: "+"
pooled_cpm: 19.95
n_lines_expressing: 45
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 14
direction_downstream: 3
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SOX12

*SRY-box transcription factor 12* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.18× (z +5.5, q 2e-05, up in 11 of 43 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.41× (z +3.9, q 0.025, up in 20 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 1.55×, NCI-H23 1.52×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.184× (z -23.3, q 0e+00, down in 41 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LZTS2]] (+0.61, fdr 7e-06), [[SAMD11]] (+0.60, fdr 1e-05), [[MAZ]] (+0.60, fdr 7e-06); moves opposite to [[ACSL5]] (-0.50, fdr 5e-05), [[MYO5C]] (-0.49, fdr 2e-05), [[MYO7B]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[LINC01589]] → it (grade B ⚠); 3 go from it, the strongest it → [[ITGB6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10861.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 1.55×, NCI-H23 1.52×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +5.5 | 2e-05 | 11/43 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.025 | 20/43 (HOP62, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.8 | 0.025 | 21/41 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.44×** | +3.6 | 0.050 | 23/42 (NCI-H23, A-172, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.088 | 18/42 (A549, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.184×** | -23.3 | 0e+00 | 41/42 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.198×** | -15.2 | 0e+00 | 38/42 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.215×** | -15.0 | 0e+00 | 39/41 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.314×** | -11.3 | 2e-27 | 39/43 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.341×** | -10.5 | 1e-23 | 40/43 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.357×** | -10.0 | 1e-21 | 36/42 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.381×** | -9.4 | 4e-19 | 31/43 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.390×** | -9.2 | 3e-18 | 35/43 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.380×** | -8.2 | 1e-14 | 38/43 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.444×** | -7.9 | 2e-13 | 34/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.458×** | -7.6 | 1e-12 | 36/42 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.583×** | -7.4 | 6e-12 | 30/41 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.504×** | -6.7 | 1e-09 | 32/41 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -6.4 | 6e-09 | 31/42 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.520×** | -6.4 | 7e-09 | 32/43 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.630×** | -4.5 | 2e-04 | 25/43 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -4.2 | 7e-04 | 25/43 (LOX-IMVI, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.664×** | -4.0 | 0.002 | 21/42 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.665×** | -4.0 | 0.002 | 21/42 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -3.6 | 0.007 | 21/40 (RPMI-7951, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 36.7 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0167× (z -40.9) |
| [[PANC-1 (line)]] | alt | 30.2 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0707× (z -29.8) |
| [[NCI-H460 (line)]] | wt | 30.4 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -24.4) |
| [[LOX-IMVI (line)]] | wt | 31.5 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0424× (z -26.9) |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 1 (1 ⚠) | 6 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.55× (z +10.5) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0889× (z -23.9) |
| [[A-427 (line)]] | wt | 32.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.5) |
| [[C32 (line)]] | wt | 32.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 36.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0615× (z -25.2) |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -18.0) |
| [[A549 (line)]] | wt | 26.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0782× (z -20.9) |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -12.4) |
| [[HOP62 (line)]] | alt | 24.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 23.7 | 1 (1 ⚠) | 3 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +8.8) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -22.0) |
| [[RKO (line)]] | wt | 28.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -20.1) |
| [[SW480 (line)]] | alt | 19.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -17.0) |
| [[H4 (line)]] | wt | 39.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0959× (z -12.3) |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -15.3) |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0191× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 8.64 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -12.3) |
| [[J82 (line)]] | alt | 17.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -9.5) |
| [[SW48 (line)]] | wt | 18.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -9.9) |
| [[BT-474 (line)]] | alt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -18.1) |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0261× (z -14.4) |
| [[HepG2_C3A (line)]] | wt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.1) |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -8.6) |
| [[HT-29 (line)]] | alt | 9.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.4) |
| [[LoVo (line)]] | wt | 8.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 9.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 8.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 34.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -17.6) |
| [[SHP-77 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.85 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZTS2]] | +0.61 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SAMD11]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[MAZ]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[PRICKLE3]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CAMSAP3]] | +0.51 | +0.55 / +0.27 | both halves | 3e-04 |  |
| [[SERTAD3]] | +0.51 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ANO8]] | +0.51 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[ARHGAP35]] | +0.50 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[HCFC1R1]] | +0.50 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[SAMD1]] | +0.49 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[RTL8A]] | +0.48 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PKD1]] | +0.48 | +0.37 / +0.57 | both halves | 8e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL5]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[MYO5C]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MYO7B]] | -0.46 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[SYK]] | -0.45 | -0.54 / -0.23 | both halves | 5e-04 |  |
| [[NPSR1-AS1]] | -0.44 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[LINC01559]] | -0.44 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[APPL2]] | -0.44 | -0.26 / -0.51 | both halves | 3e-04 |  |
| [[GSAP]] | -0.43 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[NOSTRIN]] | -0.43 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[LASTR]] | -0.42 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[TMEM30B]] | -0.42 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[ITGB6]] | -0.42 | -0.40 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01589]] | B | LINC01589 activity lowers SOX12's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 2.00× higher at baseline in the lines without LINC01589 | 0.001 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |
| [[MROH3P]] | B | MROH3P activity lowers SOX12's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.13× higher at baseline in the lines without MROH3P | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[ITGB6]] | B | ITGB6 activity lowers SOX12's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.50× higher at baseline in the lines without ITGB6 | 0.005 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[LINC01559]] | B | LINC01559 activity lowers SOX12's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 2.20× higher at baseline in the lines without LINC01559 | 0.010 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[TMEM30B]] | B | TMEM30B activity lowers SOX12's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 2.16× higher at baseline in the lines without TMEM30B | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[ABCC3]] | B | ABCC3 activity lowers SOX12's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 1.93× higher at baseline in the lines without ABCC3 | 0.018 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[SAMD11]] | B | SAMD11 activity raises SOX12's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without SAMD11 | 0.021 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[LINC02474]] | B | LINC02474 activity lowers SOX12's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 2.33× higher at baseline in the lines without LINC02474 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975 |
| [[LASTR]] | B | LASTR activity lowers SOX12's level | lines that do not express LASTR (22) vs lines expressing it (28) | 1.91× higher at baseline in the lines without LASTR | 0.027 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[ACSL5]] | B | ACSL5 activity lowers SOX12's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.54× higher at baseline in the lines without ACSL5 | 0.027 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[SYK]] | B | SYK activity lowers SOX12's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.21× higher at baseline in the lines without SYK | 0.047 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[MAPK13]] | B | MAPK13 activity lowers SOX12's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 1.72× higher at baseline in the lines without MAPK13 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB6]] | B | SOX12 activity lowers ITGB6's level | lines that do not express SOX12 (5) vs lines expressing it (45) | 14.56× higher at baseline in the lines without SOX12 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENAH, ACOT12, SSBP2; maybe low, not absent |
| [[MAZ]] | B | SOX12 activity raises MAZ's level | lines that do not express SOX12 (5) vs lines expressing it (45) | 1.41× lower at baseline in the lines without SOX12 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENAH, ACOT12, SSBP2; maybe low, not absent |
| [[PKD1]] | B | SOX12 activity raises PKD1's level | lines that do not express SOX12 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without SOX12 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENAH, ACOT12, SSBP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.289). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.0, 26.5); signed map (-29.6, 30.1). **Vector** length 79.6, 20.4% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.6 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +2.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.9 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.7 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SRY-box transcription factor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:325,552-330,224 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SOX22 |
| Gene groups (HGNC) | SRY-box transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [O15370](https://www.uniprot.org/uniprotkb/O15370) (Transcription factor SOX-12):

> Transcription factor that binds to DNA at the consensus sequence 5'-ACCAAAG-3' (By similarity). Acts as a transcriptional activator (By similarity). Binds cooperatively with POU3F2/BRN2 or POU3F1/OCT6 to gene promoters, which enhances transcriptional activation (By similarity). Involved in the differentiation of naive CD4-positive T-cells into peripherally induced regulatory T (pT reg) cells under inflammatory conditions (By similarity). Binds to the promoter region of the FOXP3 gene and …

**Summary**, from NCBI Gene [6666](https://www.ncbi.nlm.nih.gov/gene/6666):

> Members of the SOX family of transcription factors are characterized by the presence of a DNA-binding high mobility group (HMG) domain, homologous to the HMG box of sex-determining region Y (SRY). Forming a subgroup of the HMG domain superfamily, SOX proteins have been implicated in cell fate decisions in a diverse range of developmental processes. SOX transcription factors have diverse tissue-specific expression patterns during early development and have been proposed to act as target-specific …

**Accessions** — [HGNC:11198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11198) · Entrez [6666](https://www.ncbi.nlm.nih.gov/gene/6666) · UniProt [O15370](https://www.uniprot.org/uniprotkb/O15370) · Ensembl [ENSG00000177732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177732)

## Data

Gene col 10861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10861); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10861]; `tensor/DDL_lfc|DDL_z.npy` [10861]; `embed/gene_vectors.npy` [10861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10861 or target_col == 10861). Every well: [[SOX12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
