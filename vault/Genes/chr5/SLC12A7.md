---
symbol: "SLC12A7"
type: "gene"
col: 3468
ensembl_id: "ENSG00000113504"
name: "solute carrier family 12 member 7"
location: "5p15.33"
module: 14
arm: "+"
pooled_cpm: 29.96
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SLC12A7

*solute carrier family 12 member 7* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.96× (z +51.2, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.688× (z -6.2, q 4e-07, down in 21 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANO9]] (+0.73, fdr 7e-06), [[MLLT6]] (+0.70, fdr 7e-06), [[STAT5A]] (+0.70, fdr 7e-06); moves opposite to [[POGLUT2]] (-0.60, fdr 1e-05), [[RECQL]] (-0.56, fdr 2e-05), [[TRAPPC1]] (-0.53, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CX3CL1]] → it (grade B ⚠); 2 go from it, the strongest it → [[BID]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.96×** | +51.2 | 0e+00 | 37/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **8.32×** | +33.6 | 0e+00 | 38/42 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.92×** | +17.7 | 0e+00 | 29/40 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +13.3 | 3e-38 | 31/40 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +8.5 | 3e-15 | 32/42 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +8.0 | 2e-13 | 20/41 (HT-29, BT-474, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +7.3 | 2e-11 | 27/41 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.8 | 5e-10 | 22/42 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.3 | 2e-08 | 20/38 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 7e-08 | 21/41 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +5.6 | 9e-07 | 20/41 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.2 | 8e-06 | 18/42 (SW1417, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +5.0 | 2e-05 | 12/31 (SW 900, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.006 | 16/42 (NCI-H1792, A549, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.015 | 13/41 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.017 | 12/41 (RKO, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.022 | 9/37 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3468.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.688×** | -6.2 | 4e-07 | 21/41 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.708×** | -5.7 | 3e-06 | 20/42 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.737×** | -4.8 | 2e-04 | 17/38 (COLO 205, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.767×** | -4.4 | 0.002 | 15/42 (SW 1088, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.853× | -3.7 | 0.024 | 8/43 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.061 | 11/41 (HepG2/C3A, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.815×** | -3.4 | 0.061 | 14/42 (SW480, PANC-1, …) | all doses, flat | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -3.3 | 0.061 | 1/43 (BT-474) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.819×** | -3.3 | 0.064 | 7/42 (SW480, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 16.5 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 33.9× (z +27.0) | — |
| [[PANC-1 (line)]] | alt | 79.9 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +38.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.374× (z -10.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.437× (z -9.0) |
| [[A-172 (line)]] | wt | 23.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 38.6× (z +30.1) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 13.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.4× (z +35.4) | — |
| [[NCI-H2347 (line)]] | alt | 41.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +33.2) | — |
| [[A498 (line)]] | wt | 39.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +33.9) | — |
| [[A549 (line)]] | wt | 24.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.9× (z +28.8) | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +26.4) | — |
| [[HT-29 (line)]] | alt | 68.0 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +17.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 21.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +26.2) | — |
| [[SW480 (line)]] | alt | 53.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.313× (z -10.9) |
| [[HOP62 (line)]] | alt | 8.42 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.5× (z +24.7) | — |
| [[J82 (line)]] | alt | 22.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.6× (z +30.8) | — |
| [[KATO III (line)]] | alt | 58.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 15.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +28.0) | — |
| [[Panc 03.27 (line)]] | alt | 96.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +17.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 16.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +16.5) | — |
| [[CFPAC-1 (line)]] | alt | 23.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +21.6) | — |
| [[CHP-212 (line)]] | wt | 52.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.128× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 17.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +11.4) | — |
| [[HCT15 (line)]] | alt | 15.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +9.2) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.145× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 23.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +22.7) | — |
| [[Hs 766T (line)]] | wt | 19.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +18.1) | — |
| [[LoVo (line)]] | wt | 28.8 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.36× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 9.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +18.5) | — |
| [[RPMI-7951 (line)]] | alt | 8.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.77× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 12.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +19.0) | — |
| [[A-427 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0636× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 63.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +13.8) | — |
| [[COLO 205 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.154× (z -12.8) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 34.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.99× (z +13.8) | — |
| [[SW1417 (line)]] | alt | 47.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.12 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO9]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[MLLT6]] | +0.70 | +0.62 / +0.63 | both halves | 7e-06 | same gene group |
| [[STAT5A]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PTP4A3]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[REPIN1]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PRDM16]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 | same gene group |
| [[PLXNB2]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TNFRSF14]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[STAP2]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[NFIX]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT2]] | -0.60 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[RECQL]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TRAPPC1]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[GNAI3]] | -0.52 | -0.52 / -0.38 | both halves | 7e-05 | same gene group |
| [[INTS4]] | -0.52 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[IER3IP1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TAF5L]] | -0.50 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[GRB2]] | -0.49 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[PCMT1]] | -0.49 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[CHCHD2]] | -0.49 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ARPC1A]] | -0.49 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[PDCD10]] | -0.49 | -0.56 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CX3CL1]] | B | CX3CL1 activity raises SLC12A7's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without CX3CL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[ANO9]] | B | ANO9 activity raises SLC12A7's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.38× lower at baseline in the lines without ANO9 | 0.061 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[HDAC6]] | B | HDAC6 activity raises SLC12A7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TRIM29]] | B | TRIM29 activity raises SLC12A7's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without TRIM29 | 0.095 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[LGALSL-DT]] | C | LGALSL-DT activity raises SLC12A7's level | lines that do not express LGALSL-DT (4) vs lines expressing it (46) | 3.80× lower at baseline in the lines without LGALSL-DT | 0.018 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |
| [[CPEB2]] | C | CPEB2 activity strengthens SLC12A7's drug response | lines that do not express CPEB2 (3) vs lines expressing it (39) | the lines without CPEB2 respond 0.51× as strongly (z diff +2.24); strongest at Homoharringtonine 0.5 µM: 0.84x vs 3.47x (z diff +7.3) | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: SFXN3, CDKN1A, LRIG3; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BID]] | B | SLC12A7 activity raises BID's level | lines that do not express SLC12A7 (6) vs lines expressing it (44) | 2.19× lower at baseline in the lines without SLC12A7 | 0.060 | ⚠ within organs, on part of the lines; also absent: LRP5, MTARC2, LYN; maybe low, not absent; its own permutation p |
| [[TNFAIP2]] | B | SLC12A7 activity raises TNFAIP2's level | lines that do not express SLC12A7 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without SLC12A7 | 0.064 | ⚠ within organs, on part of the lines; also absent: LRP5, MTARC2, LYN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 3.5); signed map (45.7, 7.4). **Vector** length 103, 24.5% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +51.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +33.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.9 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +8.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | -0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +3.5 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | -5.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 12 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:1,050,384-1,112,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCC4, DKFZP434F076 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 12 |
| Reactome | 4 pathways, smallest: Cation-coupled Chloride cotransporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y666](https://www.uniprot.org/uniprotkb/Q9Y666) (Solute carrier family 12 member 7):

> Mediates electroneutral potassium-chloride cotransport when activated by cell swelling. May mediate K(+) uptake into Deiters' cells in the cochlea and contribute to K(+) recycling in the inner ear. Important for the survival of cochlear outer and inner hair cells and the maintenance of the organ of Corti. May be required for basolateral Cl(-) extrusion in the kidney and contribute to renal acidification (By similarity).

**Summary**, from NCBI Gene [10723](https://www.ncbi.nlm.nih.gov/gene/10723):

> Enables protein kinase binding activity. Predicted to be involved in several processes, including chloride ion homeostasis; monoatomic ion transmembrane transport; and potassium ion homeostasis. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10915) · Entrez [10723](https://www.ncbi.nlm.nih.gov/gene/10723) · UniProt [Q9Y666](https://www.uniprot.org/uniprotkb/Q9Y666) · Ensembl [ENSG00000113504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113504)

## Data

Gene col 3468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3468); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3468]; `tensor/DDL_lfc|DDL_z.npy` [3468]; `embed/gene_vectors.npy` [3468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3468 or target_col == 3468). Every well: [[SLC12A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC12A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
