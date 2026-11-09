---
symbol: "DUSP18"
type: "gene"
col: 9407
ensembl_id: "ENSG00000167065"
name: "dual specificity phosphatase 18"
location: "22q12.2"
module: 3
arm: "+"
pooled_cpm: 17.17
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DUSP18

*dual specificity phosphatase 18* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.05× (z +9.3, q 1e-17, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.447× (z -14.7, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBL]] (+0.64, fdr 1e-05), [[TRADD]] (+0.63, fdr 1e-05), [[ULK1]] (+0.63, fdr 1e-05); moves opposite to [[SRSF1]] (-0.66, fdr 1e-05), [[ILF3]] (-0.65, fdr 1e-05), [[FUBP1]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PTGFRN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +9.3 | 1e-17 | 39/48 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +7.5 | 1e-11 | 36/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +6.7 | 3e-09 | 31/47 (A498, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.55×** | +5.7 | 2e-06 | 31/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.0 | 7e-05 | 20/41 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +4.9 | 1e-04 | 24/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.008 | 21/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.8 | 0.011 | 16/47 (A-172, COLO 205, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.024 | 12/48 (NCI-H23, J82, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.027 | 12/47 (SNU-423, C-33 A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.5 | 0.027 | 11/42 (NCI-H2030, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.035 | 17/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.053 | 8/47 (NCI-H2030, SNU-423, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.064 | 15/47 (HOP62, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.447×** | -14.7 | 0e+00 | 42/47 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.234×** | -9.8 | 3e-20 | 39/48 (A-172, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.471×** | -9.7 | 7e-20 | 37/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.484×** | -9.4 | 1e-18 | 32/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.293×** | -8.3 | 2e-14 | 38/44 (LOX-IMVI, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -7.9 | 3e-13 | 36/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.547×** | -7.5 | 7e-12 | 30/47 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -7.3 | 3e-11 | 25/46 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -6.8 | 9e-10 | 26/47 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -4.9 | 5e-05 | 20/42 (NCI-H1573, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.491×** | -4.8 | 9e-05 | 17/26 (HS-578T, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.731×** | -3.8 | 0.007 | 18/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.749×** | -3.7 | 0.009 | 20/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.755×** | -3.6 | 0.013 | 17/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.767×** | -3.4 | 0.025 | 18/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.068 | 9/47 (LS 180, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -15.5) |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -20.0) |
| [[PANC-1 (line)]] | alt | 23.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.0) |
| [[A-172 (line)]] | wt | 26.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 23.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -11.9) |
| [[A549 (line)]] | wt | 17.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -14.8) |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -8.6) |
| [[LoVo (line)]] | wt | 24.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.165× (z -13.9) |
| [[LS 180 (line)]] | wt | 22.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.174× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -9.3) |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -8.8) |
| [[SW480 (line)]] | alt | 18.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -12.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -8.5) |
| [[BT-474 (line)]] | alt | 7.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -11.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.2) |
| [[KATO III (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -8.8) |
| [[RKO (line)]] | wt | 6.21 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0637× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -11.9) |
| [[A-427 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBL]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[TRADD]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ULK1]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SLC35E4]] | +0.63 | +0.43 / +0.62 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[VRK3]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[FBXL2]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[WIPF2]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CAMLG]] | +0.62 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[MYO9B]] | +0.62 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[MTM1]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PLIN3]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TMEM191A-1]] | +0.60 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[JOSD2]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF1]] | -0.66 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ILF3]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[FUBP1]] | -0.64 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[SNX5]] | -0.64 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.63 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[HNRNPD]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.62 | -0.39 / -0.66 | both halves | 6e-05 |  |
| [[MCCC2]] | -0.60 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ERH]] | -0.59 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[U2AF2]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PFAS]] | -0.58 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[GUF1]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGFRN]] | B | PTGFRN activity lowers DUSP18's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.24× higher at baseline in the lines without PTGFRN | 0.098 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.7, -1.4); signed map (-24.3, 8.3). **Vector** length 86.1, 19.5% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.2 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +6.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.4 | -14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.7 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -7.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -8.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,652,051-30,667,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DUSP20 |
| Gene groups (HGNC) | Atypical dual specificity phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEJ0](https://www.uniprot.org/uniprotkb/Q8NEJ0) (Dual specificity protein phosphatase 18):

> Can dephosphorylate single and diphosphorylated synthetic MAPK peptides, with preference for the phosphotyrosine and diphosphorylated forms over phosphothreonine. In vitro, dephosphorylates p-nitrophenyl phosphate (pNPP). In bone tissue, upon activation of the G(q)-dependent KISS1/KISS1R signaling pathway, DUSP18 is recruited to the KISS1R C-terminus where it dephosphorylates SRC, resulting in down-regulation of osteoclast differentiation and activity, and consequently suppression of bone …

**Summary**, from NCBI Gene [150290](https://www.ncbi.nlm.nih.gov/gene/150290):

> Dual-specificity phosphatases (DUSPs) constitute a large heterogeneous subgroup of the type I cysteine-based protein-tyrosine phosphatase superfamily. DUSPs are characterized by their ability to dephosphorylate both tyrosine and serine/threonine residues. They have been implicated as major modulators of critical signaling pathways. DUSP18 contains the consensus DUSP C-terminal catalytic domain but lacks the N-terminal CH2 domain found in the MKP (mitogen-activated protein kinase phosphatase) …

**Accessions** — [HGNC:18484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18484) · Entrez [150290](https://www.ncbi.nlm.nih.gov/gene/150290) · UniProt [Q8NEJ0](https://www.uniprot.org/uniprotkb/Q8NEJ0) · Ensembl [ENSG00000167065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167065)

## Data

Gene col 9407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9407); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9407]; `tensor/DDL_lfc|DDL_z.npy` [9407]; `embed/gene_vectors.npy` [9407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9407 or target_col == 9407). Every well: [[DUSP18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
