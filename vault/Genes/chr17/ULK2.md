---
symbol: "ULK2"
type: "gene"
col: 1366
ensembl_id: "ENSG00000083290"
name: "unc-51 like autophagy activating kinase 2"
location: "17p11.2"
module: 1
arm: "+"
pooled_cpm: 28.85
n_lines_expressing: 36
n_dd_up: 3
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 12
direction_downstream: 16
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ULK2

*unc-51 like autophagy activating kinase 2* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.35× (z +7.1, q 9e-10, up in 17 of 34 measured lines) ⚠ cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.38× (z +5.4, q 2e-05, up in 17 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (19 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.497× (z -11.6, q 3e-28, down in 26 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.620× (z -7.9, q 3e-13, down in 24 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNRD3]] (+0.65, fdr 7e-06), [[TTC7B]] (+0.64, fdr 7e-06), [[SNX24]] (+0.58, fdr 1e-05); moves opposite to [[CA9]] (-0.57, fdr 1e-05), [[IKZF2]] (-0.46, fdr 3e-05), [[PTPRR]] (-0.45, fdr 5e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[EBF4]] → it (grade B ⚠); 16 go from it, the strongest it → [[SLC9B2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.35×** | +7.1 | 9e-10 | 17/34 (J82, SW480, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 2e-05 | 17/33 (HEC-1-A, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.31×** | +4.5 | 0.001 | 16/33 (HOP62, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.0 | 0.33 | 9/34 (CHP-212, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.497×** | -11.6 | 3e-28 | 26/33 (NCI-H460, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.536×** | -9.9 | 1e-20 | 25/33 (SK-MEL-2, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.607×** | -8.3 | 3e-14 | 22/33 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.611×** | -8.2 | 5e-14 | 23/34 (J82, NCI-H460, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.620×** | -7.9 | 3e-13 | 24/33 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.649×** | -7.2 | 7e-11 | 21/34 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.739×** | -7.1 | 1e-10 | 21/34 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.695×** | -6.0 | 1e-07 | 18/33 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.714×** | -5.6 | 2e-06 | 19/34 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.715×** | -5.5 | 2e-06 | 20/33 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.710×** | -5.4 | 3e-06 | 17/33 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.725×** | -5.3 | 5e-06 | 15/33 (SW480, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.734×** | -5.1 | 1e-05 | 17/33 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.717×** | -5.1 | 1e-05 | 17/29 (NCI-H2030, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.816×** | -4.8 | 7e-05 | 15/33 (NCI-H2030, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -4.6 | 1e-04 | 15/34 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -4.5 | 2e-04 | 17/33 (A549, A-427, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.601×** | -4.4 | 3e-04 | 16/34 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.603×** | -4.4 | 3e-04 | 12/32 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.612×** | -4.2 | 6e-04 | 15/33 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.720×** | -3.9 | 0.002 | 11/34 (MIA PaCa-2, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.725×** | -3.8 | 0.003 | 11/34 (MIA PaCa-2, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.651×** | -3.7 | 0.004 | 12/33 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.017 | 12/33 (NCI-H23, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.685×** | -3.3 | 0.019 | 14/32 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.844× | -2.8 | 0.083 | 9/33 (C32, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.6 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 75.9 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -15.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 112 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.342× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 87.6 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[SK-MEL-2 (line)]] | alt | 63.2 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 58.6 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.324× (z -10.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.324× (z -10.7) |
| [[RKO (line)]] | wt | 41.1 | 0 | 5 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -15.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.318× (z -9.2) |
| [[A-172 (line)]] | wt | 48.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 34.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 74.6 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.215× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -9.5) |
| [[HOP62 (line)]] | alt | 28.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.289× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 52.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 14.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -10.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[C32 (line)]] | wt | 31.1 | 0 | 2 (2 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0513× (z -11.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[PANC-1 (line)]] | alt | 48.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[H4 (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -8.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW 1271 (line)]] | alt | 53.9 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0722× (z -8.9) |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.80 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.20 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNRD3]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TTC7B]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SNX24]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[MVB12B]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZNF354A]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[DGCR5]] | +0.54 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[DCAF17]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[HOMER2]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[UIMC1]] | +0.52 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[SLC4A3]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ANKRD6]] | +0.51 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[TADA2A]] | +0.51 | +0.56 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA9]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[IKZF2]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PTPRR]] | -0.45 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SNTB1]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ZNHIT1]] | -0.42 | -0.60 / -0.24 | both halves | 5e-04 |  |
| [[GPI]] | -0.41 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[TBC1D8B]] | -0.41 | -0.49 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF4]] | B | EBF4 activity raises ULK2's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 3.78× lower at baseline in the lines without EBF4 | 0.024 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[PTPRR]] | B | PTPRR activity lowers ULK2's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.05× higher at baseline in the lines without PTPRR | 0.030 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[FAXC]] | B | FAXC activity raises ULK2's level | lines that do not express FAXC (11) vs lines expressing it (39) | 3.81× lower at baseline in the lines without FAXC | 0.041 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[IKZF2]] | B | IKZF2 activity lowers ULK2's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.43× higher at baseline in the lines without IKZF2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ULK2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RASGEF1C]] | B | RASGEF1C activity raises ULK2's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 3.14× lower at baseline in the lines without RASGEF1C | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[FAM124A]] | B | FAM124A activity raises ULK2's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without FAM124A | 0.068 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[PRTG]] | B | PRTG activity raises ULK2's level | lines that do not express PRTG (14) vs lines expressing it (36) | 3.08× lower at baseline in the lines without PRTG | 0.076 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[CHD5]] | B | CHD5 activity raises ULK2's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.98× lower at baseline in the lines without CHD5 | 0.080 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[SNTB1]] | B | SNTB1 activity lowers ULK2's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.08× higher at baseline in the lines without SNTB1 | 0.082 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[SLC4A3]] | B | SLC4A3 activity raises ULK2's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 3.02× lower at baseline in the lines without SLC4A3 | 0.097 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[FSD1L]] | C | FSD1L activity raises ULK2's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 5.88× lower at baseline in the lines without FSD1L | 0.064 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 13, C 3. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC9B2]] | B | ULK2 activity raises SLC9B2's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.96× lower at baseline in the lines without ULK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[ADCK2]] | B | ULK2 activity raises ADCK2's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.11× lower at baseline in the lines without ULK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[PRTG]] | B | ULK2 activity raises PRTG's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 3.52× lower at baseline in the lines without ULK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[PM20D2]] | B | ULK2 activity raises PM20D2's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without ULK2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[PKN3]] | B | ULK2 activity raises PKN3's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without ULK2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[KLHL23]] | B | ULK2 activity raises KLHL23's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.21× lower at baseline in the lines without ULK2 | 0.066 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[RASGEF1C]] | B | ULK2 activity raises RASGEF1C's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 2.10× lower at baseline in the lines without ULK2 | 0.066 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[SNX24]] | B | ULK2 activity raises SNX24's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without ULK2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[FAM169A]] | B | ULK2 activity raises FAM169A's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 2.07× lower at baseline in the lines without ULK2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[HLCS]] | B | ULK2 activity raises HLCS's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.14× lower at baseline in the lines without ULK2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[NINL]] | B | ULK2 activity raises NINL's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 2.14× lower at baseline in the lines without ULK2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[CPLANE1]] | B | ULK2 activity raises CPLANE1's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without ULK2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.345). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (17.8, -13.2); signed map (-8.6, 25.4). **Vector** length 81.6, 20.0% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.1 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.0 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.9 | +0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.8 | -7.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.8 | -4.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.2 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.0 | -8.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -7.1 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | unc-51 like autophagy activating kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:19,770,829-19,867,936 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0623, Unc51.2, ATG1B |
| Gene groups (HGNC) | Autophagy related; Unc-51 like kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYT8](https://www.uniprot.org/uniprotkb/Q8IYT8) (Serine/threonine-protein kinase ULK2):

> Serine/threonine-protein kinase involved in autophagy in response to starvation. Acts upstream of phosphatidylinositol 3-kinase PIK3C3 to regulate the formation of autophagophores, the precursors of autophagosomes. Part of regulatory feedback loops in autophagy: acts both as a downstream effector and a negative regulator of mammalian target of rapamycin complex 1 (mTORC1) via interaction with RPTOR. Activated via phosphorylation by AMPK, also acts as a negative regulator of AMPK through …

**Summary**, from NCBI Gene [9706](https://www.ncbi.nlm.nih.gov/gene/9706):

> This gene encodes a protein that is similar to a serine/threonine kinase in C. elegans which is involved in axonal elongation. The structure of this protein is similar to the C. elegans protein in that both proteins have an N-terminal kinase domain, a central proline/serine rich (PS) domain, and a C-terminal (C) domain. The gene is located within the Smith-Magenis syndrome region on chromosome 17. Alternatively spliced transcript variants encoding the same protein have been identified. …

**Accessions** — [HGNC:13480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13480) · Entrez [9706](https://www.ncbi.nlm.nih.gov/gene/9706) · UniProt [Q8IYT8](https://www.uniprot.org/uniprotkb/Q8IYT8) · Ensembl [ENSG00000083290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083290)

## Data

Gene col 1366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1366); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1366]; `tensor/DDL_lfc|DDL_z.npy` [1366]; `embed/gene_vectors.npy` [1366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1366 or target_col == 1366). Every well: [[ULK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ULK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
