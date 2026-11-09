---
symbol: "MAPK9"
type: "gene"
col: 570
ensembl_id: "ENSG00000050748"
name: "mitogen-activated protein kinase 9"
location: "5q35.3"
module: 12
arm: "-"
pooled_cpm: 41.13
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MAPK9

*mitogen-activated protein kinase 9* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.06× (z +12.9, q 2e-35, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.678× (z -6.9, q 2e-09, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.730× (z -3.6, q 0.035, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACD3]] (+0.71, fdr 7e-06), [[MACROH2A1]] (+0.69, fdr 7e-06), [[YWHAQ]] (+0.69, fdr 7e-06); moves opposite to [[POLR1H]] (-0.72, fdr 7e-06), [[CCDC174]] (-0.72, fdr 7e-06), [[MED19]] (-0.70, fdr 7e-06).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZSWIM5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PLCG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +12.9 | 2e-35 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +12.8 | 4e-35 | 46/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +11.3 | 3e-27 | 35/38 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +11.2 | 5e-27 | 44/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +10.4 | 2e-23 | 37/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +8.3 | 1e-14 | 30/42 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +8.2 | 1e-14 | 41/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +7.5 | 3e-12 | 31/48 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +6.3 | 2e-08 | 36/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.41×** | +6.2 | 4e-08 | 29/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.1 | 5e-08 | 31/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +5.9 | 2e-07 | 25/48 (H4, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 5e-06 | 30/48 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.8 | 7e-05 | 21/48 (HS-578T, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.16× | +3.8 | 0.006 | 18/48 (A498, LS 180, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.094 | 10/48 (LoVo, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 570.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.678×** | -6.9 | 2e-09 | 28/48 (A-172, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.702×** | -6.1 | 3e-07 | 29/48 (NCI-H460, SNU-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.817×** | -5.1 | 6e-05 | 23/48 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.768×** | -4.7 | 3e-04 | 25/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.730×** | -3.6 | 0.035 | 17/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.735×** | -3.5 | 0.038 | 19/48 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.872× | -3.5 | 0.044 | 12/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.751×** | -3.3 | 0.071 | 9/48 (HCT15, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.9 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.06× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 51.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.39× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.418× (z -9.2) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H1573 (line)]] | alt | 25.1 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.16× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.45× (z +9.1) | — |
| [[A-172 (line)]] | wt | 52.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 18.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 41.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +9.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +16.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 50.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.7) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[A549 (line)]] | wt | 38.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.137× (z -9.0) ⚠ toxic |
| [[J82 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 40.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.6) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.43× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 62.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.47× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 53.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.35× (z +11.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 39.2 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0919× (z -8.6) |
| [[SW 900 (line)]] | alt | 52.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 48.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACD3]] | +0.71 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[MACROH2A1]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[YWHAQ]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[BCAP31]] | +0.68 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[EXT2]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[IPO5]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[C1orf198]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.65 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[NCKAP1]] | +0.65 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[ANKRD52]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1H]] | -0.72 | -0.62 / -0.70 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.72 | -0.58 / -0.73 | both halves | 7e-06 |  |
| [[MED19]] | -0.70 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[MFAP1]] | -0.70 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[C14orf119]] | -0.70 | -0.52 / -0.74 | both halves | 1e-05 |  |
| [[OFD1]] | -0.70 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[MED18]] | -0.69 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[SCAND1]] | -0.68 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.68 | -0.46 / -0.70 | both halves | 3e-05 |  |
| [[MRPS18C]] | -0.67 | -0.54 / -0.66 | both halves | 1e-05 | STRING 561 |
| [[TMEM265]] | -0.67 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[PDCD7]] | -0.66 | -0.56 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSWIM5]] | B | ZSWIM5 activity lowers MAPK9's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 1.36× higher at baseline in the lines without ZSWIM5 | 0.089 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCG1]] | C | MAPK9's natural level weakens PLCG1's drug response | MAPK9's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.37; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.9, -27.5); signed map (-20.4, -47.1). **Vector** length 106, 26.7% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.8 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +2.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.0 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -8.0 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.8 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.1 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -4.6 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:180,233,143-180,292,099 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JNK2, p54a, SAPK; previously PRKM9 |
| Gene groups (HGNC) | Mitogen-activated protein kinase 8-10 (JNK) family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 33 pathways, smallest: Activation of the AP-1 family of transcription factors; JNK (c-Jun kinases) phosphorylation and  activation mediated by activated human TAK1; FCERI mediated MAPK activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P45984](https://www.uniprot.org/uniprotkb/P45984) (Mitogen-activated protein kinase 9):

> Serine/threonine-protein kinase involved in various processes such as cell proliferation, differentiation, migration, transformation and programmed cell death. Extracellular stimuli such as pro-inflammatory cytokines or physical stress stimulate the stress-activated protein kinase/c-Jun N-terminal kinase (SAP/JNK) signaling pathway. In this cascade, two dual specificity kinases MAP2K4/MKK4 and MAP2K7/MKK7 phosphorylate and activate MAPK9/JNK2. In turn, MAPK9/JNK2 phosphorylates a number of …

**Summary**, from NCBI Gene [5601](https://www.ncbi.nlm.nih.gov/gene/5601):

> The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase targets specific transcription factors, and thus mediates immediate-early gene expression in response to various cell stimuli. It is most closely related to MAPK8, both of which are involved in UV …

**Accessions** — [HGNC:6886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6886) · Entrez [5601](https://www.ncbi.nlm.nih.gov/gene/5601) · UniProt [P45984](https://www.uniprot.org/uniprotkb/P45984) · Ensembl [ENSG00000050748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050748)

## Data

Gene col 570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 570); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 570]; `tensor/DDL_lfc|DDL_z.npy` [570]; `embed/gene_vectors.npy` [570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 570 or target_col == 570). Every well: [[MAPK9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
