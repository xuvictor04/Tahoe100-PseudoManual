---
symbol: "EXOC5"
type: "gene"
col: 946
ensembl_id: "ENSG00000070367"
name: "exocyst complex component 5"
location: "14q22.3"
module: 25
arm: "+"
pooled_cpm: 109.15
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# EXOC5

*exocyst complex component 5* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.54× (z +10.2, q 1e-21, up in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.33× (z +6.8, q 3e-09, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.756× (z -9.3, q 6e-18, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLD]] (+0.70, fdr 7e-06), [[UBQLN1]] (+0.67, fdr 7e-06), [[SCCPDH]] (+0.64, fdr 2e-05); moves opposite to [[POLR1C]] (-0.71, fdr 7e-06), [[KCNJ14]] (-0.57, fdr 1e-05), [[PRRT3-AS1]] (-0.55, fdr 7e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYO5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +10.2 | 1e-21 | 40/49 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +6.8 | 3e-09 | 37/48 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +6.7 | 3e-09 | 36/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.8 | 8e-07 | 28/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +5.7 | 1e-06 | 30/49 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +5.1 | 3e-05 | 29/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.5 | 4e-04 | 25/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +4.5 | 4e-04 | 24/45 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +4.5 | 4e-04 | 24/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.22×** | +4.5 | 4e-04 | 25/48 (NCI-H23, A549, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +4.4 | 5e-04 | 21/48 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.20×** | +4.4 | 5e-04 | 23/48 (NCI-H23, C-33 A, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.17× | +3.7 | 0.010 | 13/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.021 | 16/48 (SW48, A549, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | 1.16× | +3.4 | 0.023 | 18/47 (PANC-1, J82, …) | top dose only |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.025 | 12/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.088 | 3/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -9.3 | 6e-18 | 31/49 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.711×** | -8.0 | 2e-13 | 31/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.737×** | -7.2 | 1e-10 | 33/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.751×** | -4.8 | 2e-04 | 35/48 (RKO, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.845× | -4.0 | 0.008 | 21/48 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.802×** | -3.7 | 0.020 | 22/49 (J82, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.054 | 21/48 (SW 1271, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.865× | -3.3 | 0.068 | 21/48 (HOP62, C32, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.827×** | -3.2 | 0.089 | 17/48 (NCI-H460, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.876× | -3.1 | 0.098 | 16/48 (J82, A-172, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | 0.872× | -3.1 | 0.098 | 17/47 (LOX-IMVI, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 79.0 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.98× (z +11.8) | — |
| [[A549 (line)]] | wt | 121 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.8) |
| [[HOP62 (line)]] | alt | 116 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.89× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 74.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -11.5) |
| [[SW480 (line)]] | alt | 99.0 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 3.36× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.572× (z -9.3) |
| [[KATO III (line)]] | alt | 67.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 97.0 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.11× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 168 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.76× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 144 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +15.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 159 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -9.4) |
| [[C32 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -8.5) ⚠ cell-cycle shift, explains ~18% of this change |
| [[CHP-212 (line)]] | wt | 96.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.183× (z -9.1) |
| [[LoVo (line)]] | wt | 90.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.44× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 99.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +10.3) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[NCI-H1792 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -15.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 81.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.199× (z -9.5) |
| [[SW48 (line)]] | wt | 133 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -8.5) |
| [[A-172 (line)]] | wt | 92.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 98.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.67 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SCCPDH]] | +0.64 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[TMTC3]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[TWF1]] | +0.63 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[MTMR6]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[API5]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[SSX2IP]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ELMOD2]] | +0.61 | +0.49 / +0.62 | both halves | 2e-05 |  |
| [[MBTPS2]] | +0.61 | +0.40 / +0.70 | both halves | 5e-05 |  |
| [[ANXA7]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[OCRL]] | +0.60 | +0.39 / +0.69 | both halves | 6e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1C]] | -0.71 | -0.63 / -0.75 | both halves | 7e-06 |  |
| [[KCNJ14]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[PRRT3-AS1]] | -0.55 | -0.38 / -0.67 | both halves | 7e-05 |  |
| [[MIR17HG]] | -0.54 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[USP36]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ELL]] | -0.54 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[ISG20L2]] | -0.53 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[SNX8]] | -0.53 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[TTLL3]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[RBM38]] | -0.52 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[ZBTB7A]] | -0.52 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[UBE2CP5]] | -0.52 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO5A]] | B | MYO5A activity raises EXOC5's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without MYO5A | 0.040 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.2, -15.9); signed map (-16.4, -41.0). **Vector** length 111, 30.5% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.5 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.3 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +0.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.3 | -4.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | exocyst complex component 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:57,200,507-57,268,905 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEC10, SEC10P; previously SEC10L1 |
| Gene groups (HGNC) | Exocyst complex |
| Reactome | 10 pathways, smallest: VxPx cargo-targeting to cilium; Insulin processing; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O00471](https://www.uniprot.org/uniprotkb/O00471) (Exocyst complex component 5):

> Component of the exocyst complex involved in the docking of exocytic vesicles with fusion sites on the plasma membrane.

**Summary**, from NCBI Gene [10640](https://www.ncbi.nlm.nih.gov/gene/10640):

> The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex, including this protein, are found to interact with the actin cytoskeletal remodeling and vesicle …

**Accessions** — [HGNC:10696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10696) · Entrez [10640](https://www.ncbi.nlm.nih.gov/gene/10640) · UniProt [O00471](https://www.uniprot.org/uniprotkb/O00471) · Ensembl [ENSG00000070367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070367)

## Data

Gene col 946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 946); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 946]; `tensor/DDL_lfc|DDL_z.npy` [946]; `embed/gene_vectors.npy` [946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 946 or target_col == 946). Every well: [[EXOC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
