---
symbol: "SYNJ2BP"
type: "gene"
col: 13105
ensembl_id: "ENSG00000213463"
name: "synaptojanin 2 binding protein"
location: "14q24.2"
module: 25
arm: "+"
pooled_cpm: 35.93
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SYNJ2BP

*synaptojanin 2 binding protein* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.32× (z +15.7, q 0e+00, up in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.53× (z +8.2, q 2e-14, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.730× (z -8.7, q 3e-15, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HINT3]] (+0.62, fdr 1e-05), [[DLD]] (+0.61, fdr 4e-05), [[TMTC3]] (+0.60, fdr 3e-05); moves opposite to [[TPRN]] (-0.58, fdr 2e-04), [[AXIN1]] (-0.56, fdr 3e-05), [[MIR17HG]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ENPP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +15.7 | 0e+00 | 37/42 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +13.6 | 1e-39 | 39/46 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +11.5 | 2e-28 | 33/44 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +8.2 | 2e-14 | 36/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +8.0 | 1e-13 | 35/48 (SW480, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +6.9 | 5e-10 | 33/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +5.9 | 3e-07 | 25/48 (BT-474, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 3e-06 | 30/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.4 | 4e-06 | 2/49 (NCI-H23, MIA PaCa-2) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 1e-04 | 22/48 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.58×** | +4.6 | 2e-04 | 17/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.4 | 4e-04 | 25/47 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 4e-04 | 17/48 (NCI-H23, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.4 | 5e-04 | 21/48 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.004 | 16/48 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.004 | 19/47 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.009 | 13/49 (CFPAC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.018 | 16/47 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.031 | 6/48 (RPMI-7951, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.730×** | -8.7 | 3e-15 | 30/47 (COLO 205, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.678×** | -7.5 | 1e-11 | 27/47 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -6.6 | 6e-09 | 30/48 (Panc 03.27, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.523×** | -6.6 | 6e-09 | 31/49 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.580×** | -5.5 | 4e-06 | 28/48 (SW480, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.769×** | -5.1 | 3e-05 | 24/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.769×** | -3.6 | 0.021 | 14/47 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.853× | -3.1 | 0.14 | 12/48 (MIA PaCa-2, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 28.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 50.3 | 1 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.76× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.436× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.294× (z -8.7) |
| [[A-427 (line)]] | wt | 47.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 1.89× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 45.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.8) |
| [[COLO 205 (line)]] | alt | 76.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 48.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 17.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.462× (z -8.9) |
| [[LoVo (line)]] | wt | 49.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 33.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 85.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 34.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.9) |
| [[SW48 (line)]] | wt | 34.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.90× (z +9.6) ⚠ toxic; transcription drop | [[Orlistat (drug)]] 0.05 µM 0.189× (z -8.7) |
| [[A-172 (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.56× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 12.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +10.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.3) |
| [[HCT15 (line)]] | alt | 64.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -10.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.204× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 1 | — | [[SBI-0640756 (drug)]] 5 µM 0.0562× (z -11.8) |
| [[KATO III (line)]] | alt | 38.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 42.7 | 1 | 0 | [[Selinexor (drug)]] 5 µM 1.92× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 58.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +11.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 52.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -12.1) |
| [[PANC-1 (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 53.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HINT3]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[DLD]] | +0.61 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[TMTC3]] | +0.60 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[APOOL]] | +0.59 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[SUDS3]] | +0.58 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[LIN7C]] | +0.57 | +0.42 / +0.61 | both halves | 4e-05 | same gene group |
| [[MOCS2]] | +0.57 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[SF3B1]] | +0.56 | +0.37 / +0.65 | both halves | 7e-05 |  |
| [[MBTPS2]] | +0.56 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[RAD23B]] | +0.56 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[DYNC1LI2]] | +0.55 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[RBM41]] | +0.55 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPRN]] | -0.58 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[AXIN1]] | -0.56 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[MIR17HG]] | -0.56 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ZMYND19]] | -0.56 | -0.46 / -0.69 | both halves | 3e-05 |  |
| [[RAB11FIP3]] | -0.55 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[USP20]] | -0.55 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[TLNRD1]] | -0.53 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[UBALD2]] | -0.52 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[DHRS7B]] | -0.52 | -0.32 / -0.55 | both halves | 1e-04 |  |
| [[ZNF200]] | -0.51 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[PPP1R14B-AS1]] | -0.50 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[F12]] | -0.50 | -0.32 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP4]] | B | ENPP4 activity raises SYNJ2BP's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.61× lower at baseline in the lines without ENPP4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.4, -15.4); signed map (-17.2, -42.5). **Vector** length 89.5, 19.7% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +13.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.5 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | synaptojanin 2 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:70,366,499-70,417,090 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Arip2 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P57105](https://www.uniprot.org/uniprotkb/P57105) (Synaptojanin-2-binding protein):

> Regulates endocytosis of activin type 2 receptor kinases through the Ral/RALBP1-dependent pathway and may be involved in suppression of activin-induced signal transduction.

**Summary**, from NCBI Gene [55333](https://www.ncbi.nlm.nih.gov/gene/55333):

> Predicted to enable type II activin receptor binding activity. Involved in several processes, including negative regulation of endothelial cell migration; negative regulation of sprouting angiogenesis; and regulation of signal transduction. Located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18955) · Entrez [55333](https://www.ncbi.nlm.nih.gov/gene/55333) · UniProt [P57105](https://www.uniprot.org/uniprotkb/P57105) · Ensembl [ENSG00000213463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213463)

## Data

Gene col 13105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13105); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13105]; `tensor/DDL_lfc|DDL_z.npy` [13105]; `embed/gene_vectors.npy` [13105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13105 or target_col == 13105). Every well: [[SYNJ2BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNJ2BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
