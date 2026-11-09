---
symbol: "DCAF17"
type: "gene"
col: 3724
ensembl_id: "ENSG00000115827"
name: "DDB1 and CUL4 associated factor 17"
location: "2q31.1"
module: 1
arm: "+"
pooled_cpm: 24.19
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DCAF17

*DDB1 and CUL4 associated factor 17* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +15.5, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.702× (z -7.4, q 9e-11, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOX2]] (+0.80, fdr 7e-06), [[IMPACT]] (+0.77, fdr 7e-06), [[TMA16]] (+0.69, fdr 1e-05); moves opposite to [[ZNHIT1]] (-0.57, fdr 1e-05), [[SUPT4H1]] (-0.55, fdr 4e-05), [[RASA4B]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADAMTS9-AS2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[USP46]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +15.5 | 0e+00 | 38/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +12.9 | 1e-35 | 36/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +11.4 | 1e-27 | 24/34 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +9.7 | 4e-20 | 35/46 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +9.0 | 2e-17 | 25/43 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +8.3 | 1e-14 | 25/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +7.7 | 1e-12 | 30/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +7.3 | 2e-11 | 22/40 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +6.8 | 5e-10 | 21/47 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +6.7 | 2e-09 | 24/48 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +6.4 | 1e-08 | 24/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +6.3 | 1e-08 | 24/48 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 4e-06 | 18/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.3 | 5e-06 | 13/48 (A-172, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +5.2 | 6e-06 | 13/48 (SW480, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +5.2 | 6e-06 | 20/48 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.0 | 2e-05 | 19/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 9/47 (NCI-H1573, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.004 | 7/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.6 | 0.007 | 6/47 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.014 | 4/48 (J82, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -7.4 | 9e-11 | 23/47 (SW480, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.709×** | -7.2 | 2e-10 | 23/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -6.9 | 1e-09 | 26/47 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.793×** | -4.8 | 2e-04 | 13/47 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.613×** | -4.5 | 1e-03 | 19/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.784×** | -3.6 | 0.028 | 13/44 (HS-578T, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.790×** | -3.5 | 0.037 | 15/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.859× | -3.2 | 0.11 | 10/47 (HepG2/C3A, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.864× | -3.0 | 0.14 | 15/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.865× | -3.0 | 0.14 | 7/47 (CHP-212, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 29.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.8) | [[Digitoxin (drug)]] 5 µM 0.272× (z -14.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 30.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.7) | [[Bortezomib (drug)]] 5 µM 0.105× (z -8.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +12.1) | — |
| [[KATO III (line)]] | alt | 17.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 29.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.439× (z -8.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.454× (z -8.5) |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0897× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.112× (z -13.1) |
| [[HT-29 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.8) | — |
| [[J82 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.353× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOX2]] | +0.80 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.77 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[TMA16]] | +0.69 | +0.78 / +0.51 | both halves | 1e-05 |  |
| [[TXNRD3]] | +0.68 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[GUF1]] | +0.68 | +0.76 / +0.59 | both halves | 7e-06 | STRING 491 |
| [[TADA2A]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[MIOS]] | +0.67 | +0.64 / +0.72 | both halves | 7e-06 | STRING 449 |
| [[ZNHIT6]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.67 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[DPH5]] | +0.66 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[TMEM209]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ATIC]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT1]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SUPT4H1]] | -0.55 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[RASA4B]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TSEN34]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TESK2]] | -0.54 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[STX5]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TSC22D4]] | -0.53 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[PRKD2]] | -0.53 | -0.58 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity lowers DCAF17's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 1.31× higher at baseline in the lines without ADAMTS9-AS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[MVB12B]] | B | MVB12B activity raises DCAF17's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without MVB12B | 0.074 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[LRRC8D]] | C | LRRC8D activity raises DCAF17's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP46]] | C | DCAF17's natural level strengthens USP46's drug response | DCAF17's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.15; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.3, -37.5); signed map (-0.8, -39.0). **Vector** length 91.0, 19.2% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +12.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.0 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -7.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.1 | +4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:171,434,217-171,485,052 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13096; previously C2orf37 |
| Gene groups (HGNC) | DDB1 and CUL4 associated factors |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5H9S7](https://www.uniprot.org/uniprotkb/Q5H9S7) (DDB1- and CUL4-associated factor 17):

> May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [80067](https://www.ncbi.nlm.nih.gov/gene/80067):

> This gene encodes a nuclear transmembrane protein that associates with cullin 4A/damaged DNA binding protein 1 ubiquitin ligase complex. Mutations in this gene are associated with Woodhouse-Sakati syndrome. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:25784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25784) · Entrez [80067](https://www.ncbi.nlm.nih.gov/gene/80067) · UniProt [Q5H9S7](https://www.uniprot.org/uniprotkb/Q5H9S7) · Ensembl [ENSG00000115827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115827)

## Data

Gene col 3724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3724); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3724]; `tensor/DDL_lfc|DDL_z.npy` [3724]; `embed/gene_vectors.npy` [3724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3724 or target_col == 3724). Every well: [[DCAF17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
