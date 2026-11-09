---
symbol: "ECD"
type: "gene"
col: 4384
ensembl_id: "ENSG00000122882"
name: "ecdysoneless cell cycle regulator"
location: "10q22.2"
module: 212
arm: "+"
pooled_cpm: 79.44
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# ECD

*ecdysoneless cell cycle regulator* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.36× (z +13.5, q 8e-39, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.626× (z -7.2, q 3e-10, down in 33 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.824× (z -4.2, q 0.005, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KHDC4]] (+0.68, fdr 7e-06), [[TVP23B]] (+0.67, fdr 1e-05), [[TXN2]] (+0.65, fdr 1e-05); moves opposite to [[YWHAH]] (-0.54, fdr 1e-05), [[KAT6A]] (-0.53, fdr 2e-05), [[ROCK2]] (-0.52, fdr 1e-05).
> It is in [[Module 212]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4384.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.36×** | +13.5 | 8e-39 | 47/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.49×** | +10.1 | 2e-21 | 43/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +8.5 | 3e-15 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.8 | 2e-09 | 33/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +6.0 | 2e-07 | 32/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.8 | 7e-07 | 34/48 (SNU-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +4.8 | 1e-04 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.7 | 1e-04 | 28/48 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +4.7 | 2e-04 | 35/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.005 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.012 | 26/48 (PANC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.16× | +3.3 | 0.050 | 18/48 (PANC-1, HT-29, …) | rises with dose | low cells (technical?) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.050 | 11/49 (SK-MEL-2, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.10 | 18/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -7.2 | 3e-10 | 33/49 (CHP-212, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -6.8 | 2e-09 | 31/43 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -4.2 | 0.005 | 28/48 (NCI-H1573, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.773×** | -4.0 | 0.011 | 29/48 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.795×** | -3.5 | 0.047 | 24/47 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.735×** | -3.4 | 0.065 | 22/48 (A-427, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.798×** | -3.3 | 0.065 | 24/48 (SW 1088, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.065 | 22/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.751×** | -3.1 | 0.094 | 23/47 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.094 | 22/48 (NCI-H1573, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.811× | -3.1 | 0.10 | 23/47 (NCI-H1573, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.812× | -3.1 | 0.10 | 21/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.820× | -3.0 | 0.10 | 19/48 (HS-578T, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.3 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +13.6) | — |
| [[SW480 (line)]] | alt | 89.0 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.63× (z +12.7) | — |
| [[LoVo (line)]] | wt | 66.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.06× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -11.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 105 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 107 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.29× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 73.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +9.5) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0922× (z -9.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 66.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.82× (z +10.8) | — |
| [[KATO III (line)]] | alt | 55.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.85× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 57.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.16× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 78.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.45× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 82.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 97.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.02× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -13.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 92.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.49× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 65.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.66× (z +8.9) | — |
| [[A-427 (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.427× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 82.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.466× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 77.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.72× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 61.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 66.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 99.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 85.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.83× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 103 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.8× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 51.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.98× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 77.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 59.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.50× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 70.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 67.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.36× (z +8.5) | — |
| [[NCI-H661 (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0583× (z -11.0) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 62.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.89× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 78.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 96.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHDC4]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[TVP23B]] | +0.67 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[TXN2]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[WDR5B-DT]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SNIP1]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[COPA]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[GP6-AS1]] | +0.60 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[INTS4]] | +0.59 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[CUL7]] | +0.59 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[PPIL3]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TMEM39A]] | +0.59 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MED26]] | +0.58 | +0.75 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAH]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[KAT6A]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ROCK2]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TRIO]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[DST]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[KPNA1]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[USP25]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.6, -26.2); signed map (-44.0, 10.7). **Vector** length 92.7, 27.1% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +5.7 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +5.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +13.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +10.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | -0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ecdysoneless cell cycle regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,130,155-73,169,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hSGT1, GCR2 |
| Hallmark sets | GLYCOLYSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [O95905](https://www.uniprot.org/uniprotkb/O95905) (Protein ecdysoneless homolog):

> Regulator of p53/TP53 stability and function. Inhibits MDM2-mediated degradation of p53/TP53 possibly by cooperating in part with TXNIP. May be involved transcriptional regulation. In vitro has intrinsic transactivation activity enhanced by EP300. May be a transcriptional activator required for the expression of glycolytic genes. Involved in regulation of cell cycle progression. Proposed to disrupt Rb-E2F binding leading to transcriptional activation of E2F proteins. The cell cycle -regulating …

**Summary**, from NCBI Gene [11319](https://www.ncbi.nlm.nih.gov/gene/11319):

> Enables histone acetyltransferase binding activity. Involved in positive regulation of transcription by RNA polymerase II. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17029) · Entrez [11319](https://www.ncbi.nlm.nih.gov/gene/11319) · UniProt [O95905](https://www.uniprot.org/uniprotkb/O95905) · Ensembl [ENSG00000122882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122882)

## Data

Gene col 4384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4384); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4384]; `tensor/DDL_lfc|DDL_z.npy` [4384]; `embed/gene_vectors.npy` [4384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4384 or target_col == 4384). Every well: [[ECD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
