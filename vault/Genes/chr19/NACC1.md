---
symbol: "NACC1"
type: "gene"
col: 8390
ensembl_id: "ENSG00000160877"
name: "nucleus accumbens associated 1"
location: "19p13.13"
module: 5
arm: "+"
pooled_cpm: 26.38
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NACC1

*nucleus accumbens associated 1* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +10.9, q 7e-25, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.718× (z -5.0, q 3e-04, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~24% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 0.591× (z -4.5, q 0.002, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP2]] (+0.66, fdr 7e-06), [[IPPK]] (+0.63, fdr 1e-05), [[FLAD1]] (+0.62, fdr 1e-05); moves opposite to [[TXNDC16]] (-0.62, fdr 1e-05), [[FPGT]] (-0.56, fdr 1e-05), [[MLF1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +10.9 | 7e-25 | 36/48 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +8.1 | 2e-13 | 35/47 (A-172, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +7.7 | 3e-12 | 37/47 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +6.0 | 4e-07 | 28/47 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +5.7 | 1e-06 | 27/45 (SW480, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.5 | 4e-06 | 27/47 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +5.3 | 9e-06 | 22/48 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.24×** | +5.0 | 4e-05 | 25/47 (NCI-H460, HS-578T, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +5.0 | 4e-05 | 22/48 (SK-MEL-2, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.35×** | +4.7 | 1e-04 | 24/46 (HT-29, SW1417, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.50×** | +4.7 | 2e-04 | 23/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **1.30×** | +4.1 | 0.002 | 16/38 (Panc 03.27, NCI-H1792, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.004 | 16/48 (HT-29, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.004 | 20/47 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.27×** | +3.9 | 0.004 | 20/47 (Panc 03.27, NCI-H1792, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.005 | 13/46 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.005 | 16/47 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.027 | 9/46 (A549, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.040 | 15/48 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.042 | 18/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.048 | 7/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8390.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.718×** | -5.0 | 3e-04 | 25/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.591×** | -4.5 | 0.002 | 21/48 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.770×** | -4.0 | 0.014 | 15/47 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.823×** | -3.8 | 0.022 | 19/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.825×** | -3.7 | 0.022 | 19/48 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.651×** | -3.7 | 0.023 | 18/47 (C-33 A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.831×** | -3.6 | 0.026 | 17/48 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.799×** | -3.5 | 0.029 | 15/47 (HepG2/C3A, SNU-423, …) | top dose only | position effect removed |
| [[AZD-8055 (drug)]] 5 µM |  | **0.673×** | -3.4 | 0.041 | 15/48 (NCI-H23, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.749×** | -3.4 | 0.041 | 11/48 (SW480, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.832× | -3.0 | 0.12 | 9/47 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.878× | -3.0 | 0.12 | 9/48 (RKO, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[A-427 (line)]] | wt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -13.3) |
| [[A549 (line)]] | wt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.7) | — |
| [[LoVo (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[NCI-H2030 (line)]] | alt | 31.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 43.6 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.313× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | — |
| [[PANC-1 (line)]] | alt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -9.3) ⚠ cell-cycle shift, explains ~65% of this change |
| [[SW480 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.414× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP2]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[IPPK]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[FLAD1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZNF668]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TBRG4]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ARPC5L]] | +0.60 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ZNF787]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 | STRING 425 |
| [[GATAD2A]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[E2F3]] | +0.58 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ZNF562]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[BCAR1]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ZGPAT]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | -0.62 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[FPGT]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[MLF1]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[AUH]] | -0.55 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[NR1D2]] | -0.55 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[TMEM167B]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CCDC28A]] | -0.53 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[KIZ]] | -0.52 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZBTB10]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 | same gene group |
| [[OPTN]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MAP3K2]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[FMR1]] | -0.51 | -0.45 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises NACC1's level | compounds that target MTOR: 3 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises NACC1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[MEX3A]] | B | MEX3A activity raises NACC1's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without MEX3A | 0.089 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (19.1, -20.8); signed map (-20.9, -2.0). **Vector** length 102, 23.9% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.1 | +8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.1 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.7 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | nucleus accumbens associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:13,116,862-13,141,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAC1, NAC-1, BEND8, BTBD30; previously BTBD14B |
| Gene groups (HGNC) | BEN domain containing; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RE7](https://www.uniprot.org/uniprotkb/Q96RE7) (Nucleus accumbens-associated protein 1):

> Functions as a transcriptional repressor. Seems to function as a transcriptional corepressor in neuronal cells through recruitment of HDAC3 and HDAC4. Contributes to tumor progression, and tumor cell proliferation and survival. This may be mediated at least in part through repressing transcriptional activity of GADD45GIP1. Required for recruiting the proteasome from the nucleus to the cytoplasm and dendritic spines.

**Summary**, from NCBI Gene [112939](https://www.ncbi.nlm.nih.gov/gene/112939):

> This gene encodes a member of the BTB/POZ protein family. BTB/POZ proteins are involved in several cellular processes including proliferation, apoptosis and transcription regulation. The encoded protein is a transcriptional repressor that plays a role in stem cell self-renewal and pluripotency maintenance. The encoded protein also suppresses transcription of the candidate tumor suppressor Gadd45GIP1, and expression of this gene may play a role in the progression of multiple types of cancer. A …

**Accessions** — [HGNC:20967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20967) · Entrez [112939](https://www.ncbi.nlm.nih.gov/gene/112939) · UniProt [Q96RE7](https://www.uniprot.org/uniprotkb/Q96RE7) · Ensembl [ENSG00000160877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160877)

## Data

Gene col 8390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8390); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8390]; `tensor/DDL_lfc|DDL_z.npy` [8390]; `embed/gene_vectors.npy` [8390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8390 or target_col == 8390). Every well: [[NACC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NACC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
