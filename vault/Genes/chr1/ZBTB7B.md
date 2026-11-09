---
symbol: "ZBTB7B"
type: "gene"
col: 8366
ensembl_id: "ENSG00000160685"
name: "zinc finger and BTB domain containing 7B"
location: "1q21.3"
module: 110
arm: "+"
pooled_cpm: 15.7
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# ZBTB7B

*zinc finger and BTB domain containing 7B* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.61× (z +6.9, q 2e-09, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.475× (z -15.5, q 0e+00, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF1A]] (+0.63, fdr 7e-06), [[COASY]] (+0.55, fdr 1e-05), [[IQSEC2]] (+0.53, fdr 1e-05); moves opposite to [[AP1S2]] (-0.54, fdr 1e-05), [[PLAU]] (-0.49, fdr 3e-05), [[LRRC8C]] (-0.48, fdr 2e-04).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NEBL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +6.9 | 2e-09 | 29/46 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +6.0 | 7e-07 | 29/46 (PANC-1, HEC-1-A, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.27×** | +5.0 | 1e-04 | 19/48 (SHP-77, LS 180, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +4.9 | 2e-04 | 16/47 (NCI-H23, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +4.5 | 7e-04 | 16/47 (LS 180, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 0.002 | 15/46 (A498, AsPC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +4.2 | 0.002 | 17/47 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.014 | 12/43 (COLO 205, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.017 | 11/43 (SHP-77, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.6 | 0.020 | 0/48 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.026 | 12/46 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.027 | 9/46 (NCI-H460, HOP62, …) | rises with dose | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.068 | 11/46 (NCI-H1573, A498, …) | two highest doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.075 | 3/43 (A498, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.078 | 2/46 (SW480, LS 180) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.475×** | -15.5 | 0e+00 | 30/45 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.482×** | -10.8 | 2e-24 | 34/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -9.4 | 1e-18 | 29/45 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.541×** | -9.1 | 2e-17 | 29/47 (NCI-H460, HT-29, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.536×** | -8.9 | 9e-17 | 33/46 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.559×** | -8.6 | 8e-16 | 33/47 (A498, HT-29, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -7.6 | 2e-12 | 29/46 (A-172, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.641×** | -6.6 | 4e-09 | 32/46 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.682×** | -5.7 | 1e-06 | 24/44 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.730×** | -4.5 | 4e-04 | 19/45 (RKO, NCI-H1573, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.744×** | -4.4 | 6e-04 | 19/46 (NCI-H460, BT-474, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.755×** | -4.0 | 0.003 | 12/23 (LS 180, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -3.8 | 0.007 | 21/48 (SW 900, SW480, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.787×** | -3.6 | 0.015 | 15/46 (AN3 CA, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.790×** | -3.5 | 0.018 | 13/46 (NCI-H1792, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.796×** | -3.3 | 0.039 | 9/46 (RKO, C-33 A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.668×** | -3.1 | 0.057 | 11/44 (Hs 766T, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.674×** | -3.1 | 0.068 | 17/47 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 28.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 24.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.6) |
| [[LS 180 (line)]] | wt | 28.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -15.7) |
| [[A498 (line)]] | wt | 27.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -11.3) |
| [[KATO III (line)]] | alt | 20.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.0) |
| [[A-172 (line)]] | wt | 17.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.4) |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.0) |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -14.0) |
| [[SW480 (line)]] | alt | 13.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0873× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.375× (z -11.2) |
| [[BT-474 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.1) |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[HOP62 (line)]] | alt | 5.90 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -9.2) |
| [[J82 (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.8) |
| [[LoVo (line)]] | wt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.8) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.5) |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -10.2) |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0968× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF1A]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[COASY]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[IQSEC2]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[LYSMD1]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CYP4F3]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[DNAJC17]] | +0.50 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PWWP2B]] | +0.49 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[SH3TC1]] | +0.49 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZNF581]] | +0.49 | +0.37 / +0.55 | both halves | 8e-05 | same gene group |
| [[TSC22D3]] | +0.48 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[SLC22A18]] | +0.48 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[ABCF3]] | +0.48 | +0.46 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1S2]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PLAU]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[LRRC8C]] | -0.48 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[SLC4A7]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[UACA]] | -0.46 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[PPFIBP1]] | -0.46 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[RUNX1]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 | STRING 542 |
| [[PPP3CB]] | -0.45 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CEP135]] | -0.45 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ANTXR2]] | -0.45 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[ATP13A3]] | -0.44 | -0.22 / -0.49 | both halves | 6e-04 |  |
| [[KIAA1549L]] | -0.44 | -0.28 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEBL]] | B | NEBL activity raises ZBTB7B's level | lines that do not express NEBL (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without NEBL | 0.022 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[TRPC6]] | B | TRPC6 activity raises ZBTB7B's level | lines that do not express TRPC6 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without TRPC6 | 0.057 | ⚠ within organs, on part of the lines; also absent: UNC80, ARHGAP30, ENSG00000236283; maybe low, not absent |
| [[KIAA1522]] | B | KIAA1522 activity strengthens ZBTB7B's drug response | lines that do not express KIAA1522 (5) vs lines expressing it (43) | the lines without KIAA1522 respond 0.30× as strongly (z diff +2.29); strongest at Idarubicin (hydrochloride) 5 µM: 1.54x vs 0.59x (z diff +6.4) | 0.090 | ⚠ across organs; also absent: ENSG00000257489, TRIB3, PBX4; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction -0.314). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.5, -5.6); signed map (-12.4, -26.5). **Vector** length 93.8, 20.2% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +6.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.2 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +3.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.4 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | -4.7 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | -4.7 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -9.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:155,002,630-155,018,523 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZBTB15, c-Krox, hcKrox, ZNF857B, vGAF, ThPOK; previously ZFP67 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O15156](https://www.uniprot.org/uniprotkb/O15156) (Zinc finger and BTB domain-containing protein 7B):

> Transcription regulator that acts as a key regulator of lineage commitment of immature T-cell precursors. Exerts distinct biological functions in the mammary epithelial cells and T cells in a tissue-specific manner. Necessary and sufficient for commitment of CD4 lineage, while its absence causes CD8 commitment. Development of immature T-cell precursors (thymocytes) to either the CD4 helper or CD8 killer T-cell lineages correlates precisely with their T-cell receptor specificity for major …

**Summary**, from NCBI Gene [51043](https://www.ncbi.nlm.nih.gov/gene/51043):

> This gene encodes a zinc finger-containing transcription factor that acts as a key regulator of lineage commitment of immature T-cell precursors. It is necessary and sufficient for commitment of CD4 lineage, while its absence causes CD8 commitment. It also functions as a transcriptional repressor of type I collagen genes. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:18668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18668) · Entrez [51043](https://www.ncbi.nlm.nih.gov/gene/51043) · UniProt [O15156](https://www.uniprot.org/uniprotkb/O15156) · Ensembl [ENSG00000160685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160685)

## Data

Gene col 8366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8366); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8366]; `tensor/DDL_lfc|DDL_z.npy` [8366]; `embed/gene_vectors.npy` [8366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8366 or target_col == 8366). Every well: [[ZBTB7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
