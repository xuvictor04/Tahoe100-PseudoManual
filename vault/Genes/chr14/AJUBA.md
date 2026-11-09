---
symbol: "AJUBA"
type: "gene"
col: 4977
ensembl_id: "ENSG00000129474"
name: "ajuba LIM protein"
location: "14q11.2"
module: 123
arm: "+"
pooled_cpm: 13.16
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 13
n_dd_up_clean: 24
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# AJUBA

*ajuba LIM protein* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.24× (z +21.1, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.387× (z -12.1, q 4e-31, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMOTL2]] (+0.77, fdr 7e-06), [[REPIN1]] (+0.70, fdr 7e-06), [[SYDE2]] (+0.69, fdr 7e-06); moves opposite to [[RARS2]] (-0.58, fdr 2e-05), [[NAPG]] (-0.57, fdr 5e-05), [[ZCCHC17]] (-0.56, fdr 3e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[STAT5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.24×** | +21.1 | 0e+00 | 37/44 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.69×** | +12.6 | 5e-34 | 33/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.57×** | +11.5 | 2e-28 | 33/45 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +7.4 | 2e-11 | 27/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +6.7 | 3e-09 | 8/47 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +6.5 | 9e-09 | 25/44 (LS 180, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.62×** | +6.1 | 7e-08 | 27/45 (A549, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.60×** | +5.7 | 6e-07 | 23/44 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +4.8 | 1e-04 | 15/47 (LoVo, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.04×** | +4.8 | 1e-04 | 16/40 (CFPAC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 1e-04 | 22/46 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.48×** | +4.7 | 1e-04 | 16/44 (AsPC-1, HCT15, …) | inconsistent across doses | position effect removed |
| [[AZD-7648 (drug)]] 5 µM |  | **1.90×** | +4.3 | 9e-04 | 9/41 (NCI-H2030, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.001 | 18/47 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 18/46 (A549, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.003 | 18/43 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.003 | 18/46 (LoVo, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4977.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.387×** | -12.1 | 4e-31 | 37/46 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.503×** | -8.8 | 4e-16 | 28/46 (LoVo, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.544×** | -7.5 | 1e-11 | 33/44 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.547×** | -7.3 | 4e-11 | 31/44 (LOX-IMVI, HT-29, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.582×** | -6.9 | 5e-10 | 25/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.597×** | -6.6 | 4e-09 | 29/46 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.606×** | -6.4 | 1e-08 | 25/46 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.495×** | -4.7 | 2e-04 | 18/45 (A498, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.793×** | -4.2 | 0.001 | 14/46 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.723×** | -4.2 | 0.002 | 17/46 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Naproxen (drug)]] 5 µM |  | **0.714×** | -4.2 | 0.002 | 11/44 (AN3 CA, NCI-H2347, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.745×** | -3.8 | 0.008 | 18/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.664×** | -3.7 | 0.008 | 9/46 (A-427, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | 0.777× | -3.0 | 0.11 | 15/44 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 16.3 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +8.5) | [[Ixazomib citrate (drug)]] 0.5 µM 0.182× (z -9.9) |
| [[A-427 (line)]] | wt | 21.2 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +10.0) | [[Ixazomib citrate (drug)]] 5 µM 0.140× (z -12.6) |
| [[LoVo (line)]] | wt | 24.9 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.189× (z -12.4) |
| [[PANC-1 (line)]] | alt | 8.72 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +18.1) | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.251× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.145× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 8.94 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +14.1) | — |
| [[SW480 (line)]] | alt | 22.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.271× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 18.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +15.9) | — |
| [[H4 (line)]] | wt | 14.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +15.0) | — |
| [[KATO III (line)]] | alt | 18.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +12.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.210× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 8.13 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 14.1× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 24.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +9.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[SW1417 (line)]] | alt | 26.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.1) | — |
| [[A549 (line)]] | wt | 7.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.137× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 7.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +14.5) | — |
| [[J82 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.63 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0637× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +13.9) | — |
| [[RPMI-7951 (line)]] | alt | 6.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.93× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 7.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +13.0) | — |
| [[A-172 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMOTL2]] | +0.77 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[REPIN1]] | +0.70 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[SYDE2]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[FOSL2]] | +0.65 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[TRIP6]] | +0.64 | +0.58 / +0.62 | both halves | 8e-06 | STRING 543 |
| [[LGALSL-DT]] | +0.63 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[PLXNB2]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[TGIF2]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[LATS2]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 | STRING 983 |
| [[NFIX]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[VEZF1]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RARS2]] | -0.58 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[NAPG]] | -0.57 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[ZCCHC17]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[MAP2K1]] | -0.56 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[ABTB3]] | -0.56 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[INTS4]] | -0.55 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ARPC1A]] | -0.55 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[ARPC1B]] | -0.55 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[GNAI3]] | -0.54 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[WDR59]] | -0.54 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[MYO9B]] | -0.54 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[ISCA1]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAT5A]] | B | STAT5A activity lowers AJUBA's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.64× higher at baseline in the lines without STAT5A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[LINC01186]] | B | LINC01186 activity raises AJUBA's level | lines that do not express LINC01186 (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without LINC01186 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC01836, STXBP2, EEPD1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers AJUBA's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[ARHGEF17]] | C | ARHGEF17 activity raises AJUBA's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |
| [[AMOTL2]] | C | AMOTL2 activity raises AJUBA's level | lines that do not express AMOTL2 (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without AMOTL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: BCL2L1, RASSF7, FCHO1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.596). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.0, 12.5); signed map (42.2, 2.5). **Vector** length 111, 26.7% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Signaling by Hippo* (reactome, mean cos +0.61 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +21.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +12.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.9 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.5 | +4.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.3 | -12.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.5 | -8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.5 | -7.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.9 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | ajuba LIM protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,971,177-22,982,551 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15563; previously JUB |
| Gene groups (HGNC) | Ajuba family |
| Reactome | 16 pathways, smallest: Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha; Cellular response to hypoxia; Activation of HOX genes during differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IF1](https://www.uniprot.org/uniprotkb/Q96IF1) (LIM domain-containing protein ajuba):

> Adapter or scaffold protein which participates in the assembly of numerous protein complexes and is involved in several cellular processes such as cell fate determination, cytoskeletal organization, repression of gene transcription, mitosis, cell-cell adhesion, cell differentiation, proliferation and migration. Contributes to the linking and/or strengthening of epithelia cell-cell junctions in part by linking adhesive receptors to the actin cytoskeleton. May be involved in signal transduction …

**Summary**, from NCBI Gene [84962](https://www.ncbi.nlm.nih.gov/gene/84962):

> Enables alpha-catenin binding activity and transcription corepressor activity. Involved in several processes, including miRNA-mediated gene silencing by inhibition of translation; negative regulation of hippo signaling; and regulation of cellular response to hypoxia. Acts upstream of or within miRNA-mediated post-transcriptional gene silencing and positive regulation of protein-containing complex assembly. Located in P-body; cell-cell junction; and nucleus. [provided by Alliance of Genome …

**Accessions** — [HGNC:20250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20250) · Entrez [84962](https://www.ncbi.nlm.nih.gov/gene/84962) · UniProt [Q96IF1](https://www.uniprot.org/uniprotkb/Q96IF1) · Ensembl [ENSG00000129474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129474)

## Data

Gene col 4977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4977); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4977]; `tensor/DDL_lfc|DDL_z.npy` [4977]; `embed/gene_vectors.npy` [4977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4977 or target_col == 4977). Every well: [[AJUBA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AJUBA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
