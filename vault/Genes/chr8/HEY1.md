---
symbol: "HEY1"
type: "gene"
col: 8987
ensembl_id: "ENSG00000164683"
name: "hes related family bHLH transcription factor with YRPW motif 1"
location: "8q21.13"
module: 92
arm: "+"
pooled_cpm: 4.33
n_lines_expressing: 35
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# HEY1

*hes related family bHLH transcription factor with YRPW motif 1* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 3.24× (z +10.8, q 3e-24, up in 10 of 15 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.64× (z +9.2, q 7e-18, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.647× (z -4.3, q 0.009, down in 10 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C32 0.128×, Hs 766T 0.234×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.145×, CHP-212 0.184×; ⚠ cell-cycle shift, explains ~88% of this change); [[Daptomycin (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.182×, COLO 205 0.0946×; ⚠ unreliable plate only); [[vincristine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0289×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0871×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC20A1]] (+0.54, fdr 2e-05), [[TRIB2]] (+0.53, fdr 2e-05), [[MIR181A1HG]] (+0.52, fdr 9e-05); moves opposite to [[MAPKAP1]] (-0.42, fdr 1e-04), [[MAEA]] (-0.41, fdr 3e-04), [[SLC25A16]] (-0.40, fdr 5e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[DUSP6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.24×** | +10.8 | 3e-24 | 10/15 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.64×** | +9.2 | 7e-18 | 13/29 (SK-MEL-2, HOP62, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.49×** | +8.4 | 1e-14 | 0/6 | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +8.0 | 2e-13 | 12/31 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +7.7 | 2e-12 | 12/31 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.22×** | +7.6 | 3e-12 | 3/12 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.99×** | +6.5 | 5e-09 | 4/14 (HepG2/C3A, NCI-H661, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +5.9 | 3e-07 | 5/31 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +5.7 | 7e-07 | 10/31 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.74×** | +5.3 | 7e-06 | 7/30 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.2 | 1e-05 | 7/27 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +5.0 | 3e-05 | 9/30 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.018 | 8/27 (C32, Hs 766T, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.67×** | +3.5 | 0.019 | 1/11 (NCI-H460) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.48×** | +3.5 | 0.019 | 0/9 | all doses, stronger at high dose | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.66×** | +3.5 | 0.019 | 4/23 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.042 | 4/31 (C32, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.048 | 3/31 (C-33 A, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.079 | 3/30 (SHP-77, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.36×** | +2.9 | 0.083 | 1/26 (A549) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.53×** | +2.9 | 0.083 | 2/24 (HOP62, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Aprepitant (drug)]] 0.05 µM |  | **1.35×** | +2.9 | 0.083 | 1/31 (SHP-77) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8987.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C32 0.128×, Hs 766T 0.234×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.145×, CHP-212 0.184×; ⚠ cell-cycle shift, explains ~88% of this change); [[Daptomycin (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.182×, COLO 205 0.0946×; ⚠ unreliable plate only); [[vincristine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0289×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0871×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.647×** | -4.3 | 0.009 | 10/31 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.644×** | -4.2 | 0.009 | 11/28 (SK-MEL-2, COLO 205, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.646×** | -3.8 | 0.024 | 10/31 (A549, C32, …) | inconsistent across doses | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.697× | -3.3 | 0.10 | 2/29 (SW 900, LoVo) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.783× | -3.3 | 0.10 | 10/30 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.717× | -3.2 | 0.10 | 7/29 (NCI-H1573, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Capmatinib (drug)]] 0.5 µM |  | 0.628× | -3.1 | 0.10 | 2/31 (COLO 205, C32) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.709× | -3.1 | 0.10 | 11/28 (COLO 205, SK-MEL-2, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | 0.533× | -3.1 | 0.10 | 3/30 (C32, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.722× | -3.1 | 0.10 | 10/30 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.723× | -3.1 | 0.10 | 4/31 (SK-MEL-2, SW1417, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.744× | -3.1 | 0.10 | 8/31 (C32, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 43.2 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -11.4) |
| [[C32 (line)]] | wt | 21.8 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -13.8) |
| [[CHP-212 (line)]] | wt | 61.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0655× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Radotinib (drug)]] 0.5 µM 0.0703× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 3 (1 ⚠) | — | [[vincristine (drug)]] 0.5 µM 0.0289× (z -13.0) |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Peretinoin (drug)]] 5 µM 0.0490× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 7.70 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.6) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.242× (z -8.5) |
| [[A-172 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC20A1]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TRIB2]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[MIR181A1HG]] | +0.52 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[ETV1]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ATP2B1]] | +0.50 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[NUP62CL]] | +0.48 | +0.40 / +0.41 | both halves | 4e-05 |  |
| [[FZD4]] | +0.48 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[CLDN10-AS1]] | +0.48 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[RGL1]] | +0.47 | +0.36 / +0.44 | both halves | 9e-05 |  |
| [[TRA2B]] | +0.47 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[FMN1]] | +0.47 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[DUSP4]] | +0.46 | +0.42 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAP1]] | -0.42 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[MAEA]] | -0.41 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[SLC25A16]] | -0.40 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[CLIP1]] | -0.40 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[TBC1D22B]] | -0.39 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[UEVLD]] | -0.39 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[DESI1]] | -0.38 | -0.24 / -0.40 | both halves | 4e-04 |  |
| [[KLHL22]] | -0.38 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[NUTM2B-AS1]] | -0.38 | -0.28 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP6]] | B | HEY1 activity raises DUSP6's level | lines that do not express HEY1 (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without HEY1 | 0.096 | ⚠ within organs, on part of the lines; also absent: SLC2A14, SDK2, DTX3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.403). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.5, 9.1); signed map (7.9, 51.4). **Vector** length 54.6, 9.05% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.7 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.0 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +5.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -1.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.1 | -2.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.1 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | hes related family bHLH transcription factor with YRPW motif 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:79,762,371-79,767,857 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HESR-1, CHF2, HESR1, HRT-1, CHF-2, HERP2, bHLHb31 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Hey bHLH transcription factor family |
| Hallmark sets | HEDGEHOG_SIGNALING, WNT_BETA_CATENIN_SIGNALING |
| Reactome | 19 pathways, smallest: NOTCH4 Intracellular Domain Regulates Transcription; Cardiogenesis; NOTCH3 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5J3](https://www.uniprot.org/uniprotkb/Q9Y5J3) (Hairy/enhancer-of-split related with YRPW motif protein 1):

> Transcriptional repressor which binds preferentially to the canonical E box sequence 5'-CACGTG-3'. Downstream effector of Notch signaling required for cardiovascular development. Specifically required for the Notch-induced endocardial epithelial to mesenchymal transition, which is itself criticial for cardiac valve and septum development. May be required in conjunction with HEY2 to specify arterial cell fate or identity. Promotes maintenance of neuronal precursor cells and glial versus neuronal …

**Summary**, from NCBI Gene [23462](https://www.ncbi.nlm.nih.gov/gene/23462):

> This gene encodes a nuclear protein belonging to the hairy and enhancer of split-related (HESR) family of basic helix-loop-helix (bHLH)-type transcriptional repressors. Expression of this gene is induced by the Notch and c-Jun signal transduction pathways. Two similar and redundant genes in mouse are required for embryonic cardiovascular development, and are also implicated in neurogenesis and somitogenesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul …

**Accessions** — [HGNC:4880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4880) · Entrez [23462](https://www.ncbi.nlm.nih.gov/gene/23462) · UniProt [Q9Y5J3](https://www.uniprot.org/uniprotkb/Q9Y5J3) · Ensembl [ENSG00000164683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164683)

## Data

Gene col 8987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8987); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8987]; `tensor/DDL_lfc|DDL_z.npy` [8987]; `embed/gene_vectors.npy` [8987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8987 or target_col == 8987). Every well: [[HEY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
