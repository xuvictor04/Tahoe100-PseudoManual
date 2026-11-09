---
symbol: "ARHGAP27P1-BPTFP1-KPNA2P3"
type: "gene"
col: 13273
ensembl_id: "ENSG00000215769"
name: "ARHGAP27P1-BPTFP1-KPNA2P3 readthrough, transcribed pseudogene"
location: "17q24.1"
module: 34
arm: "+"
pooled_cpm: 26.31
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 27
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ARHGAP27P1-BPTFP1-KPNA2P3

*ARHGAP27P1-BPTFP1-KPNA2P3 readthrough, transcribed pseudogene* — 17q24.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.628× (z -7.9, q 1e-12, down in 26 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.518× (z -7.9, q 1e-12, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA2P3]] (+0.92, fdr 7e-06, ⚠ same locus), [[PLEKHM1P1]] (+0.75, fdr 7e-06, ⚠ same locus), [[PLEKHM1]] (+0.71, fdr 7e-06), [[ARHGAP27]] (+0.71, fdr 7e-06), [[C11orf91]] (+0.70, fdr 7e-06); moves opposite to [[CFAP418]] (-0.59, fdr 1e-05), [[CNTNAP1]] (-0.55, fdr 1e-05), [[SGCE]] (-0.54, fdr 2e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[LINC02582]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.34× | +3.5 | 0.15 | 9/48 (KATO III, A498, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.23× | +3.5 | 0.15 | 16/48 (SW480, HOP62, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.46× | +3.2 | 0.24 | 7/47 (Panc 03.27, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.26 | 12/48 (MIA PaCa-2, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.628×** | -7.9 | 1e-12 | 26/47 (AsPC-1, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -7.9 | 1e-12 | 36/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -6.6 | 9e-09 | 34/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -6.2 | 8e-08 | 28/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -5.7 | 1e-06 | 28/47 (SW480, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -5.1 | 3e-05 | 28/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.660×** | -5.0 | 5e-05 | 25/47 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -4.9 | 7e-05 | 25/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.460×** | -4.9 | 7e-05 | 25/44 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.678×** | -4.5 | 4e-04 | 22/47 (KATO III, SW480, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.691×** | -4.4 | 5e-04 | 23/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.499×** | -4.3 | 6e-04 | 24/45 (SW480, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -4.1 | 0.002 | 17/47 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.740×** | -3.6 | 0.013 | 14/48 (SW 1271, C-33 A, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.577×** | -3.4 | 0.022 | 18/44 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.026 | 16/48 (SW480, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.675×** | -3.4 | 0.027 | 9/48 (KATO III, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -3.0 | 0.066 | 14/47 (LoVo, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.2 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -13.0) |
| [[LoVo (line)]] | wt | 59.1 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 53.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0873× (z -20.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 33.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -9.0) |
| [[Hs 766T (line)]] | wt | 35.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.148× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -9.6) |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 48.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.618× (z -10.3) ⚠ position not correctable |
| [[SNU-423 (line)]] | alt | 33.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -9.0) |
| [[A-427 (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[A549 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 47.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -15.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0586× (z -11.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0759× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 19.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.225× (z -8.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 16.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0994× (z -8.5) |
| [[A-172 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA2P3]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PLEKHM1P1]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 | ⚠ same locus (3.6 kb, same strand: neighbours can correlate without regulation) |
| [[PLEKHM1]] | +0.71 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[ARHGAP27]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[C11orf91]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[WNT2B]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[LSMEM2]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[UCKL1-AS1]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[TMC7]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[RAPGEF3]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[LEMD1]] | +0.59 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[BLZF2P]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PHYHD1]] | +0.59 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP418]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[CNTNAP1]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[SGCE]] | -0.54 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[HINT3]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CISD2]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TMEM106B]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[AMOT]] | -0.49 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[SCARB2]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[RAB11FIP2]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PAIP1]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02582]] | B | LINC02582 activity strengthens ARHGAP27P1-BPTFP1-KPNA2P3's drug response | lines that do not express LINC02582 (41) vs lines expressing it (7) | the lines without LINC02582 respond 0.38× as strongly (z diff +3.53); strongest at Homoharringtonine 5 µM: 0.72x vs 0.25x (z diff +6.9) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; target measured in part of the lines; artifact flags |
| [[ITGB4]] | B | ITGB4 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without ITGB4 | 0.007 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[B3GNT3]] | B | B3GNT3 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without B3GNT3 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[PTPRE]] | B | PTPRE activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without PTPRE | 0.011 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[GJB3]] | B | GJB3 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without GJB3 | 0.015 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[SH3TC2]] | B | SH3TC2 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 1.45× lower at baseline in the lines without SH3TC2 | 0.022 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent |
| [[TFF2]] | B | TFF2 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.15× lower at baseline in the lines without TFF2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[LSMEM2]] | B | LSMEM2 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without LSMEM2 | 0.026 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[LEMD1]] | B | LEMD1 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without LEMD1 | 0.032 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[TINAGL1]] | B | TINAGL1 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without TINAGL1 | 0.034 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[PADI1]] | B | PADI1 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without PADI1 | 0.045 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[DHRS9]] | B | DHRS9 activity strengthens ARHGAP27P1-BPTFP1-KPNA2P3's drug response | lines that do not express DHRS9 (40) vs lines expressing it (8) | the lines without DHRS9 respond 0.48× as strongly (z diff +2.54); strongest at Harringtonine 5 µM: 0.73x vs 0.32x (z diff +4.4) | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.9, 54.0); signed map (0.8, 36.6). **Vector** length 112, 29.6% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +3.5 |
| fall | [[Binimetinib (drug)]] 0.5 µM |  | -4.8 | -2.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.3 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.2 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ARHGAP27P1-BPTFP1-KPNA2P3 readthrough, transcribed pseudogene |
| Locus type | readthrough (other) |
| Location | 17q24.1 — chr17:64,749,663-64,781,707 (-) |
| Ensembl biotype | lncRNA |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [109286553](https://www.ncbi.nlm.nih.gov/gene/109286553):

> This locus represents naturally-occurring readthrough transcription between multiple unprocessed pseudogene loci. Readthrough transcripts likely do not encode functional proteins. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:52873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52873) · Entrez [109286553](https://www.ncbi.nlm.nih.gov/gene/109286553) · Ensembl [ENSG00000215769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215769)

## Data

Gene col 13273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13273); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13273]; `tensor/DDL_lfc|DDL_z.npy` [13273]; `embed/gene_vectors.npy` [13273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13273 or target_col == 13273). Every well: [[ARHGAP27P1-BPTFP1-KPNA2P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP27P1-BPTFP1-KPNA2P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
