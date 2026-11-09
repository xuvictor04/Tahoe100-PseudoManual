---
symbol: "MCTS1"
type: "gene"
col: 13838
ensembl_id: "ENSG00000232119"
name: "MCTS1 re-initiation and release factor"
location: "Xq24"
module: 148
arm: "+"
pooled_cpm: 32.18
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# MCTS1

*MCTS1 re-initiation and release factor* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.23× (z +15.4, q 0e+00, up in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +9.0, q 5e-17, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.606× (z -9.6, q 3e-19, down in 29 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.709× (z -6.6, q 1e-08, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLHC1]] (+0.72, fdr 2e-05), [[NEK9]] (+0.71, fdr 3e-05), [[LEKR1]] (+0.70, fdr 2e-05); moves opposite to [[MAST3]] (-0.74, fdr 1e-05), [[SEMA6C]] (-0.71, fdr 8e-06), [[FAM118A]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[TASOR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +15.4 | 0e+00 | 36/43 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +14.3 | 1e-43 | 29/34 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +9.0 | 5e-17 | 31/46 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.5 | 4e-15 | 31/46 (KATO III, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +8.3 | 2e-14 | 24/38 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.7 | 1e-12 | 33/47 (HOP62, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.2 | 7e-11 | 34/47 (A-427, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +5.5 | 3e-06 | 27/46 (HOP62, SNU-423, …) | two highest doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.2 | 1e-05 | 24/45 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +5.1 | 2e-05 | 22/47 (HOP62, HT-29, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.7 | 2e-04 | 18/47 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.6 | 2e-04 | 19/42 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.26×** | +4.4 | 4e-04 | 19/45 (AsPC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.031 | 13/47 (SNU-423, SW480, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.060 | 8/47 (HOP62, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -9.6 | 3e-19 | 29/45 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.709×** | -6.6 | 1e-08 | 25/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.761×** | -5.3 | 3e-05 | 21/46 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.766×** | -5.1 | 4e-05 | 24/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.768×** | -5.1 | 4e-05 | 23/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.794×** | -4.4 | 8e-04 | 23/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.660×** | -4.2 | 0.002 | 18/39 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.811×** | -4.0 | 0.004 | 17/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.673×** | -4.0 | 0.004 | 14/45 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.829×** | -3.6 | 0.016 | 19/47 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.839× | -3.3 | 0.057 | 8/47 (NCI-H2347, MIA PaCa-2, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 61.9 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.76× (z +14.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.431× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.499× (z -10.2) |
| [[SNU-423 (line)]] | alt | 36.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 25.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 22.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.309× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 46.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +11.4) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.488× (z -9.9) |
| [[A498 (line)]] | wt | 47.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 45.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.392× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 32.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.73× (z +10.2) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.361× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 35.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -10.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 34.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.371× (z -9.5) |
| [[LoVo (line)]] | wt | 30.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.8) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[NCI-H23 (line)]] | alt | 43.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 32.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 45.9 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.142× (z -8.8) |
| [[A-172 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLHC1]] | +0.72 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[NEK9]] | +0.71 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[LEKR1]] | +0.70 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[PSME3IP1]] | +0.69 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[COX18]] | +0.69 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[MAGOHB]] | +0.68 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[ANAPC13]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TIMMDC1]] | +0.67 | +0.74 / +0.30 | both halves | 2e-04 |  |
| [[ST7L]] | +0.67 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | +0.67 | +0.70 / +0.34 | both halves | 1e-04 |  |
| [[RAB30-DT]] | +0.67 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[RFX3-DT]] | +0.66 | +0.64 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.74 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[SEMA6C]] | -0.71 | -0.57 / -0.60 | both halves | 8e-06 |  |
| [[FAM118A]] | -0.69 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[PBX4]] | -0.69 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.69 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[BRAT1]] | -0.67 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TSPAN33]] | -0.67 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[PI4KAP2]] | -0.66 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[SNN]] | -0.66 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[CARHSP1]] | -0.66 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[BRF1]] | -0.66 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[FBXL16]] | -0.65 | -0.56 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MCTS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises MCTS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises MCTS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RTN4R]] | C | RTN4R activity raises MCTS1's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without RTN4R | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TASOR]] | C | MCTS1's natural level strengthens TASOR's drug response | MCTS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.11; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | MCTS1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | MCTS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.455 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-6.7, 1.7); signed map (15.4, -28.1). **Vector** length 84.1, 17.2% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.5 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +4.1 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.3 | +0.7 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +1.2 | +0.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | MCTS1 re-initiation and release factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:120,594,010-120,621,159 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCT-1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULC4](https://www.uniprot.org/uniprotkb/Q9ULC4) (Malignant T-cell-amplified sequence 1):

> Translation regulator forming a complex with DENR to promote translation reinitiation. Translation reinitiation is the process where the small ribosomal subunit remains attached to the mRNA following termination of translation of a regulatory upstream ORF (uORF), and resume scanning on the same mRNA molecule to initiate translation of a downstream ORF, usually the main ORF (mORF). The MCTS1/DENR complex is pivotal to two linked mechanisms essential for translation reinitiation. Firstly, the …

**Summary**, from NCBI Gene [28985](https://www.ncbi.nlm.nih.gov/gene/28985):

> Enables RNA cap binding activity; ribosomal small subunit binding activity; and translation initiation factor activity. Involved in IRES-dependent viral translational initiation; cytoplasmic translational initiation; and ribosome disassembly. Located in cytosol. Is active in cytoplasm. Implicated in immunodeficiency 118. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23357) · Entrez [28985](https://www.ncbi.nlm.nih.gov/gene/28985) · UniProt [Q9ULC4](https://www.uniprot.org/uniprotkb/Q9ULC4) · Ensembl [ENSG00000232119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232119)

## Data

Gene col 13838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13838); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13838]; `tensor/DDL_lfc|DDL_z.npy` [13838]; `embed/gene_vectors.npy` [13838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13838 or target_col == 13838). Every well: [[MCTS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCTS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
