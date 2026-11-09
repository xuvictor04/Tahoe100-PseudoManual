---
symbol: "TRMT6"
type: "gene"
col: 1576
ensembl_id: "ENSG00000089195"
name: "tRNA methyltransferase 6 non-catalytic subunit"
location: "20p12.3"
module: 5
arm: "+"
pooled_cpm: 24.82
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TRMT6

*tRNA methyltransferase 6 non-catalytic subunit* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.17× (z +11.7, q 7e-29, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.835× (z -3.9, q 0.038, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.642×; ⚠ position not correctable); [[Simotinib (drug)]] 5 µM in 1 line (C-33 A 0.239×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAK16]] (+0.73, fdr 7e-06), [[NOM1]] (+0.70, fdr 7e-06), [[PNO1]] (+0.69, fdr 7e-06); moves opposite to [[TESK2]] (-0.61, fdr 1e-05), [[DBP]] (-0.58, fdr 5e-05), [[CAT]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MPZL3]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +11.7 | 7e-29 | 41/47 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.17×** | +11.6 | 7e-29 | 41/44 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +11.5 | 4e-28 | 38/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +10.8 | 3e-25 | 40/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.65×** | +10.7 | 1e-24 | 32/47 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.01×** | +10.1 | 4e-22 | 25/33 (KATO III, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.87×** | +8.7 | 2e-16 | 31/41 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.74×** | +8.4 | 4e-15 | 32/48 (SW480, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.78×** | +8.3 | 4e-15 | 36/46 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.77×** | +8.3 | 8e-15 | 32/48 (SW480, SHP-77, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.70×** | +8.0 | 6e-14 | 34/48 (SW480, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +7.9 | 1e-13 | 38/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.3 | 1e-11 | 36/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +6.7 | 1e-09 | 33/48 (LOX-IMVI, LoVo, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.48×** | +5.9 | 1e-07 | 28/48 (SW480, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +5.7 | 3e-07 | 27/48 (HOP62, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 1e-04 | 22/48 (COLO 205, HOP62, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.002 | 17/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.002 | 17/46 (NCI-H1792, Hs 766T, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.003 | 17/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.008 | 16/48 (NCI-H460, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.009 | 20/47 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.016 | 17/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.027 | 14/46 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.048 | 14/48 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.642×; ⚠ position not correctable); [[Simotinib (drug)]] 5 µM in 1 line (C-33 A 0.239×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -3.9 | 0.038 | 16/48 (SW1417, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.778×** | -3.8 | 0.038 | 16/48 (AsPC-1, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.797×** | -3.4 | 0.094 | 16/48 (AsPC-1, C32, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.850× | -3.4 | 0.094 | 17/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.804× | -3.3 | 0.11 | 17/48 (J82, RKO, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.834× | -3.0 | 0.22 | 8/48 (AsPC-1, C32, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.0 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.74× (z +9.6) | — |
| [[KATO III (line)]] | alt | 17.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.34× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~30% of this change | [[Adagrasib (drug)]] 0.05 µM 0.642× (z -9.7) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 35.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 86.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.239× (z -8.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 19.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[RPMI-7951 (line)]] | alt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[A-172 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAK16]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 | STRING 703 |
| [[NOM1]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[PNO1]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[LSG1]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 | STRING 493 |
| [[GTPBP4]] | +0.65 | +0.71 / +0.57 | both halves | 9e-06 | STRING 769 |
| [[UTP11]] | +0.65 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[WDR4]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 | pathway: tRNA modification in the nucleus and cytosol; STRING 909 |
| [[NIP7]] | +0.65 | +0.71 / +0.57 | both halves | 1e-05 | STRING 461 |
| [[ABCE1]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[UTP15]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 | STRING 462 |
| [[EIF2S1]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 | STRING 440 |
| [[GRWD1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 | STRING 537 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TESK2]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[DBP]] | -0.58 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[CAT]] | -0.58 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[STK38]] | -0.58 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[PTMA]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.56 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[NPC2]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[NR3C2]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CRY2]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[AAMDC]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[AHDC1]] | -0.54 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity lowers TRMT6's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.38× higher at baseline in the lines without MPZL3 | 0.036 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[NR3C1]] | B | NR3C1 activity raises TRMT6's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.3% of all compounds | 0.099 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | C | TRMT6's natural level lowers the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (makes them more sensitive) | TRMT6's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.285 over the table, 0.041 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.0, -35.6); signed map (-3.1, -46.5). **Vector** length 95.0, 24.1% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.56 to 13); *rRNA processing* (reactome, mean cos +0.51 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +7.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +10.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.4 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.4 | +0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.2 | -0.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 6 non-catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:5,937,228-5,950,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCD10, MGC5029, Gcd10p, CGI-09 |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJA5](https://www.uniprot.org/uniprotkb/Q9UJA5) (tRNA):

> Substrate-binding subunit of tRNA (adenine-N(1)-)-methyltransferase, which catalyzes the formation of N(1)-methyladenine at position 58 (m1A58) in initiator methionyl-tRNA. Together with the TRMT61A catalytic subunit, part of a mRNA N(1)-methyltransferase complex that mediates methylation of adenosine residues at the N(1) position of a small subset of mRNAs: N(1) methylation takes place in tRNA T-loop-like structures of mRNAs and is only present at low stoichiometries.

**Summary**, from NCBI Gene [51605](https://www.ncbi.nlm.nih.gov/gene/51605):

> This gene encodes a member of the tRNA methyltransferase 6 protein family. A similar protein in yeast is part of a two component methyltransferase, which is involved in the posttranslational modification that produces the modified nucleoside 1-methyladenosine in tRNAs. Modified 1-methyladenosine influences initiator methionine stability and may be involved in the replication of human immunodeficiency virus type 1. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:20900](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20900) · Entrez [51605](https://www.ncbi.nlm.nih.gov/gene/51605) · UniProt [Q9UJA5](https://www.uniprot.org/uniprotkb/Q9UJA5) · Ensembl [ENSG00000089195](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089195)

## Data

Gene col 1576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1576); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1576]; `tensor/DDL_lfc|DDL_z.npy` [1576]; `embed/gene_vectors.npy` [1576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1576 or target_col == 1576). Every well: [[TRMT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
