---
symbol: "PI4KB"
type: "gene"
col: 6735
ensembl_id: "ENSG00000143393"
name: "phosphatidylinositol 4-kinase beta"
location: "1q21.3"
module: 12
arm: "+"
pooled_cpm: 53.19
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PI4KB

*phosphatidylinositol 4-kinase beta* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +19.5, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.607× (z -12.5, q 3e-33, down in 36 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.830× (z -6.6, q 6e-09, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCP1A]] (+0.76, fdr 7e-06), [[CES2]] (+0.71, fdr 7e-06), [[CCDC174]] (+0.69, fdr 7e-06); moves opposite to [[IPO7]] (-0.66, fdr 7e-06), [[GART]] (-0.64, fdr 7e-06), [[GMPS]] (-0.62, fdr 8e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TNFRSF10C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +19.5 | 0e+00 | 40/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.17×** | +15.1 | 0e+00 | 42/49 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +14.8 | 0e+00 | 43/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +9.1 | 1e-17 | 35/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +7.2 | 9e-11 | 36/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +7.1 | 1e-10 | 29/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +6.4 | 1e-08 | 29/48 (A-172, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.9 | 3e-07 | 28/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +5.2 | 1e-05 | 26/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +5.1 | 2e-05 | 15/48 (A-172, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +4.9 | 4e-05 | 22/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.8 | 6e-05 | 20/47 (NCI-H1573, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 1e-04 | 22/48 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.2 | 0.001 | 17/48 (SNU-1, A-427, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 16/48 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 13/49 (A498, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.022 | 11/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.061 | 9/49 (HCT15, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.607×** | -12.5 | 3e-33 | 36/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -12.4 | 1e-32 | 28/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.713×** | -7.8 | 9e-13 | 29/45 (C32, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -6.6 | 6e-09 | 25/48 (A-172, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.811×** | -5.2 | 2e-05 | 25/48 (SW480, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.814×** | -5.2 | 2e-05 | 24/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.809×** | -5.1 | 3e-05 | 21/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -4.6 | 4e-04 | 0/49 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.842× | -4.2 | 0.002 | 17/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | 0.793× | -3.0 | 0.14 | 8/48 (SW 1271, SW 900, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.1 | 9 (3 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.01× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -20.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 73.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +24.3) | [[Panobinostat (drug)]] 5 µM 0.503× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H23 (line)]] | alt | 75.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -17.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 43.0 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -11.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 39.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -14.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 95.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.9) | — |
| [[A549 (line)]] | wt | 49.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +16.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.07× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 46.5 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.57× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -18.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 75.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 66.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 46.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -12.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 49.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 36.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -12.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 49.6 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -11.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 46.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.36× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.531× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 32.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 66.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 68.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 65.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 67.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.71× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -17.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -13.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 66.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0895× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 40.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 53.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCP1A]] | +0.76 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[CES2]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[YJU2B]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RBM5]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ZNF579]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SUMO4]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TJAP1]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[OSCP1]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[KBTBD4]] | +0.64 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[COIL]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO7]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[GART]] | -0.64 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[GMPS]] | -0.62 | -0.61 / -0.57 | both halves | 8e-06 |  |
| [[RBBP7]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[IPO5]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.61 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TMTC4]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[DKC1]] | -0.59 | -0.63 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF10C]] | B | TNFRSF10C activity raises PI4KB's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.18× lower at baseline in the lines without TNFRSF10C | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PI4KB's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.4, 4.2); signed map (-6.1, -9.2). **Vector** length 99.7, 23.8% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +19.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +14.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +15.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +4.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.3 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +2.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.5 | -7.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -0.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.9 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol 4-kinase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,291,797-151,327,715 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PI4K-BETA, pi4K92; previously PIK4CB |
| Gene groups (HGNC) | Phosphatidylinositol 4-kinase type 3 family |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the Golgi membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBF8](https://www.uniprot.org/uniprotkb/Q9UBF8) (Phosphatidylinositol 4-kinase beta):

> Phosphorylates phosphatidylinositol (PI) in the first committed step in the production of the second messenger inositol-1,4,5,-trisphosphate (PIP). May regulate Golgi disintegration/reorganization during mitosis, possibly via its phosphorylation. Involved in Golgi-to-plasma membrane trafficking (By similarity). May play an important role in the inner ear development.; (Microbial infection) Plays an essential role in Aichi virus RNA replication. Recruited by ACBD3 at the viral replication …

**Summary**, from NCBI Gene [5298](https://www.ncbi.nlm.nih.gov/gene/5298):

> Enables 1-phosphatidylinositol 4-kinase activity and 14-3-3 protein binding activity. Involved in inner ear development and phosphatidylinositol phosphate biosynthetic process. Acts upstream of or within lysosome organization. Located in Golgi membrane. Is active in cytoplasmic side of trans-Golgi network membrane. Implicated in autosomal dominant nonsyndromic deafness 87. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8984) · Entrez [5298](https://www.ncbi.nlm.nih.gov/gene/5298) · UniProt [Q9UBF8](https://www.uniprot.org/uniprotkb/Q9UBF8) · Ensembl [ENSG00000143393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143393)

## Data

Gene col 6735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6735); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6735]; `tensor/DDL_lfc|DDL_z.npy` [6735]; `embed/gene_vectors.npy` [6735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6735 or target_col == 6735). Every well: [[PI4KB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PI4KB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
