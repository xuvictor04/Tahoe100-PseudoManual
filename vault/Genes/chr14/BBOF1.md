---
symbol: "BBOF1"
type: "gene"
col: 4087
ensembl_id: "ENSG00000119636"
name: "basal body orientation factor 1"
location: "14q24.3"
module: 41
arm: "+"
pooled_cpm: 13.69
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 26
n_dd_up_clean: 8
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# BBOF1

*basal body orientation factor 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +10.2, q 8e-22, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.413× (z -11.2, q 2e-26, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSCP1]] (+0.68, fdr 7e-06), [[MORN2]] (+0.63, fdr 1e-05), [[CWC25]] (+0.62, fdr 7e-06); moves opposite to [[OSBPL10]] (-0.56, fdr 1e-05), [[VANGL1]] (-0.55, fdr 1e-05), [[GLO1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[COPZ2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +10.2 | 8e-22 | 29/46 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +7.4 | 4e-11 | 15/25 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.5 | 7e-06 | 16/35 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.2 | 0.003 | 15/29 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.006 | 16/48 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.007 | 22/46 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.011 | 15/48 (C-33 A, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.012 | 15/48 (CFPAC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.027 | 11/48 (HOP62, NCI-H2030, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.041 | 10/48 (KATO III, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.060 | 11/48 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.29×** | +3.2 | 0.065 | 11/48 (CFPAC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.413×** | -11.2 | 2e-26 | 38/48 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.581×** | -9.7 | 6e-20 | 39/48 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -8.6 | 1e-15 | 33/46 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.538×** | -7.9 | 6e-13 | 33/48 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.567×** | -7.2 | 8e-11 | 31/48 (NCI-H1573, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -6.9 | 6e-10 | 28/48 (LoVo, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -6.1 | 1e-07 | 27/47 (H4, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.620×** | -6.0 | 1e-07 | 25/46 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.661×** | -5.2 | 1e-05 | 20/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.682×** | -4.8 | 7e-05 | 24/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.682×** | -4.7 | 2e-04 | 24/40 (C-33 A, SW 900, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -4.5 | 4e-04 | 22/44 (C32, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -4.4 | 4e-04 | 21/47 (A-172, SNU-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.701×** | -4.2 | 9e-04 | 18/46 (SW48, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -4.0 | 0.002 | 20/48 (HOP62, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.735×** | -3.9 | 0.003 | 17/45 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.004 | 17/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.750×** | -3.6 | 0.008 | 10/47 (KATO III, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.752×** | -3.5 | 0.015 | 15/47 (LoVo, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.147× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 12.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.15× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 24.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0696× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.131× (z -10.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.239× (z -10.3) |
| [[A-172 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +8.6) | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.215× (z -8.8) |
| [[C-33 A (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0891× (z -9.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 14.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0318× (z -12.9) |
| [[HCT15 (line)]] | alt | 9.55 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0807× (z -8.5) |
| [[LS 180 (line)]] | wt | 3.88 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0570× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.258× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 18.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 8.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.4× (z +14.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.27 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0857× (z -9.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0746× (z -13.2) |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 10.3 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0634× (z -8.8) |
| [[A498 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSCP1]] | +0.68 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[MORN2]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[CWC25]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ALDH6A1]] | +0.61 | +0.49 / +0.71 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[FAM161B]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[IQCK]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[STK19]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ZNF490]] | +0.56 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[MPC1]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LCA5L]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[GOLGA2]] | +0.56 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[GPAT4-AS1]] | +0.55 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[LRRC27]] | +0.54 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBPL10]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[VANGL1]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[GLO1]] | -0.54 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[PRRG1]] | -0.53 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[USB1]] | -0.53 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[GALNT14]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SLC48A1]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CCT5]] | -0.51 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[TUSC3]] | -0.51 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[CDYL]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[RGS19]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CHST10]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COPZ2]] | B | COPZ2 activity raises BBOF1's level | lines that do not express COPZ2 (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without COPZ2 | 0.019 | ⚠ within organs, on part of the lines; also absent: WDR54, ADGRE5, L3MBTL1; maybe low, not absent |
| [[XK]] | B | XK activity lowers BBOF1's level | lines that do not express XK (18) vs lines expressing it (32) | 1.43× higher at baseline in the lines without XK | 0.029 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[CRACD]] | B | CRACD activity lowers BBOF1's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.45× higher at baseline in the lines without CRACD | 0.046 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers BBOF1's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (3.6, -34.2); signed map (-8.1, -2.4). **Vector** length 86.4, 18.3% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +7.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.7 | +3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.6 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.2 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | basal body orientation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,019,349-74,082,863 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBB10; previously C14orf45, CCDC176 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8ND07](https://www.uniprot.org/uniprotkb/Q8ND07) (Basal body-orientation factor 1):

> Plays an essential role in sperm motility and male fertility by stabilizing the sperm flagellar axonemal structure. May be required for the stability of ODF2 and MANS1 proteins. Dispensable for the assembly and function of motile cilia.

**Summary**, from NCBI Gene [80127](https://www.ncbi.nlm.nih.gov/gene/80127):

> Predicted to be involved in sperm axoneme assembly. Predicted to act upstream of or within several processes, including cilium movement involved in cell motility; negative regulation of microtubule depolymerization; and protein stabilization. Predicted to be located in axoneme; ciliary basal body; and sperm flagellum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19855) · Entrez [80127](https://www.ncbi.nlm.nih.gov/gene/80127) · UniProt [Q8ND07](https://www.uniprot.org/uniprotkb/Q8ND07) · Ensembl [ENSG00000119636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119636)

## Data

Gene col 4087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4087); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4087]; `tensor/DDL_lfc|DDL_z.npy` [4087]; `embed/gene_vectors.npy` [4087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4087 or target_col == 4087). Every well: [[BBOF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBOF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
