---
symbol: "SLC50A1"
type: "gene"
col: 9781
ensembl_id: "ENSG00000169241"
name: "solute carrier family 50 member 1"
location: "1q22"
module: 14
arm: "+"
pooled_cpm: 26.09
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 19
n_dd_up_clean: 16
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SLC50A1

*solute carrier family 50 member 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +9.5, q 1e-18, up in 32 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +9.3, q 6e-18, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.619× (z -6.9, q 3e-09, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYLD]] (+0.61, fdr 1e-05), [[IRF1]] (+0.60, fdr 1e-05), [[ASS1]] (+0.60, fdr 1e-05); moves opposite to [[HERC2P3]] (-0.57, fdr 7e-06), [[GBX2-AS1]] (-0.55, fdr 1e-05), [[ERCC3]] (-0.55, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MUC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +9.5 | 1e-18 | 32/41 (NCI-H2030, C32, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +9.3 | 6e-18 | 28/47 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +7.1 | 3e-10 | 26/36 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +7.0 | 4e-10 | 9/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.57×** | +6.2 | 5e-08 | 18/33 (KATO III, NCI-H2030, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +5.7 | 1e-06 | 25/46 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +5.7 | 1e-06 | 28/47 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +5.5 | 3e-06 | 28/43 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +4.9 | 5e-05 | 22/48 (A-172, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +4.9 | 5e-05 | 24/47 (A-172, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 9e-05 | 22/46 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.6 | 2e-04 | 27/48 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 7e-04 | 22/48 (A-172, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 1e-03 | 20/46 (LS 180, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.002 | 21/48 (AsPC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.004 | 17/48 (AsPC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.008 | 19/48 (AsPC-1, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.6 | 0.010 | 18/48 (COLO 205, C32, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.013 | 19/47 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.014 | 16/47 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.015 | 16/45 (A498, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.024 | 17/47 (A-427, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9781.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.619×** | -6.9 | 3e-09 | 34/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -6.5 | 2e-08 | 32/47 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.425×** | -6.4 | 3e-08 | 29/44 (A-427, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.654×** | -5.6 | 3e-06 | 26/48 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.680×** | -5.5 | 4e-06 | 27/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -5.3 | 1e-05 | 30/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.519×** | -4.9 | 7e-05 | 22/46 (NCI-H1792, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -4.8 | 1e-04 | 28/46 (COLO 205, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.542×** | -4.6 | 3e-04 | 25/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -4.5 | 4e-04 | 23/46 (NCI-H2030, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.574×** | -4.2 | 0.002 | 18/45 (COLO 205, Hs 766T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -3.9 | 0.004 | 20/47 (AsPC-1, LoVo, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.761×** | -3.6 | 0.014 | 18/47 (BT-474, SW1417, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.787×** | -3.4 | 0.024 | 17/47 (NCI-H460, A549, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.792×** | -3.3 | 0.031 | 21/47 (COLO 205, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.035 | 17/47 (KATO III, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 37.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.36× (z +15.8) | — |
| [[NCI-H2030 (line)]] | alt | 43.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 43.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0426× (z -12.9) |
| [[COLO 205 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 12.5 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0838× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0927× (z -10.7) |
| [[HS-578T (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +9.4) | — |
| [[KATO III (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +11.5) ⚠ position not correctable | — |
| [[NCI-H460 (line)]] | wt | 25.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.318× (z -9.5) |
| [[RKO (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.308× (z -8.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYLD]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[IRF1]] | +0.60 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ASS1]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.60 | +0.59 / +0.65 | both halves | 7e-06 | STRING 504; ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[TNFAIP2]] | +0.59 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[DENND4A]] | +0.59 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[PSME1]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[REL]] | +0.56 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[TSPAN31]] | +0.56 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[GBP2]] | +0.55 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[BCL3]] | +0.55 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[GCA]] | +0.55 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[PSMB9]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P3]] | -0.57 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[GBX2-AS1]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ERCC3]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[COX10]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[ZNF551]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[POP1]] | -0.52 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[C19orf12]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[TRMT1]] | -0.51 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[HERC2P9]] | -0.51 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[CUL4A]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[XPO4]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SNRPD1]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC1]] | B | MUC1 activity raises SLC50A1's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without MUC1 | 0.026 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[RSPH1]] | B | RSPH1 activity raises SLC50A1's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without RSPH1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises SLC50A1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without ELF3-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[EFNA1]] | B | EFNA1 activity raises SLC50A1's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without EFNA1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[ELF3]] | B | ELF3 activity raises SLC50A1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.55× lower at baseline in the lines without ELF3 | 0.077 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[TJP3]] | B | TJP3 activity raises SLC50A1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.53× lower at baseline in the lines without TJP3 | 0.078 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SLC50A1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[CGN]] | B | CGN activity raises SLC50A1's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.38× lower at baseline in the lines without CGN | 0.088 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[FZD5]] | C | FZD5 activity raises SLC50A1's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without FZD5 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, 3.8); signed map (45.1, 6.2). **Vector** length 91.9, 21.2% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +9.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.1 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.8 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 50 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,135,344-155,138,857 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCP, RP11-540D14.5, slv, RZPDo834D038D, HsSWEET1, SWEET1; previously RAG1AP1 |
| Gene groups (HGNC) | Solute carrier family 50 |
| Reactome | 3 pathways, smallest: Cellular hexose transport; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRV3](https://www.uniprot.org/uniprotkb/Q9BRV3) (Sugar transporter SWEET1):

> Mediates sugar transport across membranes. May stimulate V(D)J recombination by the activation of RAG1.

**Summary**, from NCBI Gene [55974](https://www.ncbi.nlm.nih.gov/gene/55974):

> Enables glucoside transmembrane transporter activity. Predicted to be involved in carbohydrate transport. Located in Golgi apparatus and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30657) · Entrez [55974](https://www.ncbi.nlm.nih.gov/gene/55974) · UniProt [Q9BRV3](https://www.uniprot.org/uniprotkb/Q9BRV3) · Ensembl [ENSG00000169241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169241)

## Data

Gene col 9781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9781); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9781]; `tensor/DDL_lfc|DDL_z.npy` [9781]; `embed/gene_vectors.npy` [9781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9781 or target_col == 9781). Every well: [[SLC50A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC50A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
