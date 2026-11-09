---
symbol: "SIKE1"
type: "gene"
col: 585
ensembl_id: "ENSG00000052723"
name: "suppressor of IKBKE 1"
location: "1p13.2"
module: 49
arm: "+"
pooled_cpm: 40.57
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SIKE1

*suppressor of IKBKE 1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.68× (z +13.1, q 2e-36, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.382× (z -12.7, q 3e-34, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2C]] (+0.58, fdr 1e-05), [[PITHD1]] (+0.57, fdr 1e-05), [[STAM2]] (+0.53, fdr 8e-05); moves opposite to [[WEE1]] (-0.57, fdr 1e-05), [[SAMD1]] (-0.47, fdr 8e-05), [[PHLPP1]] (-0.47, fdr 6e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +13.1 | 2e-36 | 42/47 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.66×** | +12.7 | 1e-34 | 40/47 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.57×** | +11.4 | 5e-28 | 33/46 (Panc 03.27, J82, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +10.4 | 3e-23 | 38/47 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.52×** | +10.1 | 5e-22 | 28/41 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +9.8 | 2e-20 | 33/46 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +7.9 | 3e-13 | 29/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +6.5 | 4e-09 | 25/47 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.20× | +6.5 | 6e-09 | 22/47 (Panc 03.27, A-172, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +5.7 | 7e-07 | 22/47 (A-172, RKO, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +5.4 | 3e-06 | 22/46 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +5.3 | 7e-06 | 17/46 (NCI-H23, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +5.1 | 1e-05 | 20/47 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.23×** | +5.1 | 2e-05 | 19/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +5.0 | 2e-05 | 20/47 (SK-MEL-2, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.20×** | +4.7 | 9e-05 | 18/47 (A-172, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.5 | 2e-04 | 21/47 (LS 180, PANC-1, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.3 | 4e-04 | 13/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.6 | 0.007 | 10/47 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.022 | 12/46 (SW480, RKO, …) | all doses, flat | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.022 | 5/47 (SK-MEL-2, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Brimonidine (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.067 | 9/47 (A549, HOP62, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.067 | 2/47 (SK-MEL-2, J82) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.12× | +2.8 | 0.097 | 13/47 (SW1417, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.382×** | -12.7 | 3e-34 | 40/47 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -12.3 | 2e-32 | 36/47 (RKO, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.776×** | -6.4 | 3e-08 | 26/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.795×** | -5.8 | 1e-06 | 21/47 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.822×** | -4.9 | 9e-05 | 24/47 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.846× | -4.0 | 0.007 | 16/46 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | 0.866× | -3.5 | 0.040 | 11/47 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.875× | -3.2 | 0.088 | 18/46 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 0.5 µM |  | 0.885× | -3.1 | 0.13 | 4/47 (CFPAC-1, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 43.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 1.91× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[TAK-901 (drug)]] 5 µM 0.265× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 130 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.89× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 71.0 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.196× (z -8.6) |
| [[LS 180 (line)]] | wt | 54.3 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.20× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 45.3 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.35× (z +8.6) ⚠ toxic | [[PH-797804 (drug)]] 5 µM 0.204× (z -8.8) |
| [[RKO (line)]] | wt | 47.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0462× (z -14.2) |
| [[A-172 (line)]] | wt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 39.3 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0791× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.422× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2C]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PITHD1]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[STAM2]] | +0.53 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[TTC1]] | +0.53 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[DNAJC24]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[ELMOD2]] | +0.52 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[PLPBP]] | +0.51 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[ZNF484]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MOCS2]] | +0.50 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[CDC16]] | +0.50 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[DYNC1LI2]] | +0.49 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[ACP1]] | +0.49 | +0.33 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WEE1]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SAMD1]] | -0.47 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[PHLPP1]] | -0.47 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[NR2F1]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[DDX39A]] | -0.45 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[RTF1]] | -0.45 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[SIN3A]] | -0.45 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ARID1A]] | -0.44 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[OVOL2]] | -0.43 | -0.27 / -0.33 | both halves | 3e-04 |  |
| [[AP4M1]] | -0.43 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[CUL3]] | -0.43 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[HMGB1]] | -0.43 | -0.34 / -0.40 | both halves | 1e-04 | pathway: DDX58/IFIH1-mediated induction of interferon-alpha/beta |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.336). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.1, -51.6); signed map (-30.9, -25.3). **Vector** length 75.6, 14.0% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +7.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -12.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -12.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.5 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.5 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | +0.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | suppressor of IKBKE 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:114,769,479-114,780,685 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21168, SIKE |
| Gene groups (HGNC) | STRIPAK complex |
| Reactome | 12 pathways, smallest: TRAF3-dependent IRF activation pathway; TRAF6 mediated IRF7 activation; SARS-CoV-1 activates/modulates innate immune responses |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRV8](https://www.uniprot.org/uniprotkb/Q9BRV8) (Suppressor of IKBKE 1):

> Physiological suppressor of IKK-epsilon and TBK1 that plays an inhibitory role in virus- and TLR3-triggered IRF3. Inhibits TLR3-mediated activation of interferon-stimulated response elements (ISRE) and the IFN-beta promoter. May act by disrupting the interactions of IKBKE or TBK1 with TICAM1/TRIF, IRF3 and RIGI. Does not inhibit NF-kappa-B activation pathways. Associates with the striatin-interacting phosphatase and kinase (STRIPAK) core complex, forming the extended (SIKE1:SLMAP)STRIPAK …

**Summary**, from NCBI Gene [80143](https://www.ncbi.nlm.nih.gov/gene/80143):

> SIKE interacts with IKK-epsilon (IKBKE; MIM 605048) and TBK1 (MIM 604834) and acts as a suppressor of TLR3 (MIM 603029) and virus-triggered interferon activation pathways (Huang et al., 2005 [PubMed 16281057]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26119) · Entrez [80143](https://www.ncbi.nlm.nih.gov/gene/80143) · UniProt [Q9BRV8](https://www.uniprot.org/uniprotkb/Q9BRV8) · Ensembl [ENSG00000052723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000052723)

## Data

Gene col 585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 585); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 585]; `tensor/DDL_lfc|DDL_z.npy` [585]; `embed/gene_vectors.npy` [585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 585 or target_col == 585). Every well: [[SIKE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIKE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
