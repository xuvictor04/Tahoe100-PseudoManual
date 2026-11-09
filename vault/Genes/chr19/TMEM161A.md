---
symbol: "TMEM161A"
type: "gene"
col: 748
ensembl_id: "ENSG00000064545"
name: "transmembrane protein 161A"
location: "19p13.11"
module: 72
arm: "+"
pooled_cpm: 8.38
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# TMEM161A

*transmembrane protein 161A* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 4.16× (z +25.0, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.564× (z -15.0, q 0e+00, down in 33 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD39]] (+0.80, fdr 7e-06), [[NEIL2]] (+0.71, fdr 7e-06), [[BABAM1]] (+0.70, fdr 1e-05); moves opposite to [[TNRC6C]] (-0.59, fdr 3e-05), [[FAM200B]] (-0.58, fdr 6e-05), [[CGGBP1]] (-0.57, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GPX3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **4.16×** | +25.0 | 0e+00 | 41/43 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.59×** | +23.7 | 0e+00 | 42/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.91×** | +19.8 | 0e+00 | 41/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.06×** | +10.8 | 3e-25 | 22/27 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +10.5 | 2e-23 | 21/37 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.14×** | +10.1 | 6e-22 | 33/46 (PANC-1, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.66×** | +9.4 | 4e-19 | 21/33 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.62×** | +9.0 | 2e-17 | 26/46 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +8.3 | 8e-15 | 20/46 (PANC-1, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.54×** | +8.0 | 5e-14 | 20/46 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.54×** | +7.8 | 5e-13 | 8/16 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.49×** | +7.4 | 6e-12 | 22/46 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 8e-09 | 16/41 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.33×** | +5.3 | 6e-06 | 4/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +4.5 | 3e-04 | 7/46 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.5 | 0.013 | 5/47 (SHP-77, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.017 | 7/46 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.017 | 0/47 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.023 | 7/44 (AN3 CA, NCI-H23, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.047 | 1/43 (SW48) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.048 | 1/40 (C-33 A) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.054 | 4/42 (H4, PANC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.077 | 1/42 (MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.085 | 2/43 (HS-578T, MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.564×** | -15.0 | 0e+00 | 33/44 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.711×** | -6.3 | 8e-08 | 18/46 (SNU-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.756×** | -5.2 | 4e-05 | 15/46 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.785×** | -4.5 | 0.001 | 12/42 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.800×** | -4.1 | 0.006 | 14/42 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.810×** | -3.9 | 0.009 | 15/45 (SNU-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.863× | -3.9 | 0.009 | 5/46 (A498, RKO, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.692×** | -3.6 | 0.025 | 5/45 (C-33 A, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.824×** | -3.4 | 0.036 | 13/45 (NCI-H23, HS-578T, …) | top dose only | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **0.822×** | -3.3 | 0.046 | 6/45 (BT-474, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.3 | 0.059 | 6/46 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.841× | -3.1 | 0.095 | 8/44 (MIA PaCa-2, J82, …) | top dose only |  |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.849× | -3.0 | 0.11 | 2/46 (SW 900, BT-474) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.67 | 3 | 1 | [[Bortezomib (drug)]] 0.05 µM 4.89× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 9.05 | 1 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.65× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.0700× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.6) |
| [[C32 (line)]] | wt | 9.38 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0964× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.258× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.0) |
| [[SW480 (line)]] | alt | 8.67 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.37× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 4.69 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0771× (z -8.9) |
| [[HS-578T (line)]] | alt | 8.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.1) |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.96 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.113× (z -10.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD39]] | +0.80 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[NEIL2]] | +0.71 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[BABAM1]] | +0.70 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[EPS15L1]] | +0.69 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[DFFA]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[HERC2P2]] | +0.68 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[CACYBP]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PACC1]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[FAM241B]] | +0.68 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[POP1]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ATP2C1]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[CDC123]] | +0.67 | +0.65 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.59 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[FAM200B]] | -0.58 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[CGGBP1]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[EP300]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[REL]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPX3]] | B | GPX3 activity lowers TMEM161A's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.45× higher at baseline in the lines without GPX3 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[DUXAP9]] | B | DUXAP9 activity raises TMEM161A's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without DUXAP9 | 0.045 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[AGTPBP1]] | C | AGTPBP1 activity raises TMEM161A's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.796). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.1, -9.0); signed map (-26.8, -26.4). **Vector** length 81.6, 14.9% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of DVL* (reactome, mean cos +0.54 to 12); *proteasome* (control, mean cos +0.54 to 11); *NIK-->noncanonical NF-kB signaling* (reactome, mean cos +0.53 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.5 | +23.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.8 | +25.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +19.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.5 | +10.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.6 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.3 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.05 µM |  | +1.0 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -15.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.2 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -2.9 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.8 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.8 | +1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | -0.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 161A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,119,169-19,138,513 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39645, FLJ20422 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX61](https://www.uniprot.org/uniprotkb/Q9NX61) (Transmembrane protein 161A):

> May play a role in protection against oxidative stress. Overexpression leads to reduced levels of oxidant-induced DNA damage and apoptosis.

**Summary**, from NCBI Gene [54929](https://www.ncbi.nlm.nih.gov/gene/54929):

> Involved in several processes, including cellular response to UV; regulation of cellular response to stress; and response to retinoic acid. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26020) · Entrez [54929](https://www.ncbi.nlm.nih.gov/gene/54929) · UniProt [Q9NX61](https://www.uniprot.org/uniprotkb/Q9NX61) · Ensembl [ENSG00000064545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064545)

## Data

Gene col 748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 748); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 748]; `tensor/DDL_lfc|DDL_z.npy` [748]; `embed/gene_vectors.npy` [748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 748 or target_col == 748). Every well: [[TMEM161A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM161A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
