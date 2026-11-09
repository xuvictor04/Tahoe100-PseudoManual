---
symbol: "HSPA14"
type: "gene"
col: 11918
ensembl_id: "ENSG00000187522"
name: "heat shock protein family A (Hsp70) member 14"
location: "10p13"
module: 71
arm: "+"
pooled_cpm: 32.88
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# HSPA14

*heat shock protein family A (Hsp70) member 14* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (23 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +20.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.912× (z -5.8, q 5e-06, down in 3 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 0.852× (z -4.0, q 0.008, down in 14 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOPBP1]] (+0.68, fdr 1e-05), [[TOP3A]] (+0.65, fdr 1e-05), [[NDOR1]] (+0.63, fdr 1e-05); moves opposite to [[RHOB]] (-0.67, fdr 1e-05), [[TPPP]] (-0.60, fdr 3e-05), [[JUND]] (-0.59, fdr 5e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 26 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +20.6 | 0e+00 | 46/48 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +12.4 | 5e-33 | 41/47 (SW480, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.99×** | +12.2 | 1e-31 | 42/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.58×** | +11.4 | 5e-28 | 35/47 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.87×** | +11.1 | 2e-26 | 40/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.27×** | +11.0 | 5e-26 | 43/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +10.0 | 9e-22 | 37/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.69×** | +9.0 | 2e-17 | 35/47 (LoVo, J82, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.61×** | +8.1 | 3e-14 | 27/37 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **1.64×** | +8.0 | 6e-14 | 36/44 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.57×** | +7.7 | 6e-13 | 34/47 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.53×** | +7.5 | 3e-12 | 33/47 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.55×** | +7.5 | 3e-12 | 29/48 (SW480, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +7.4 | 7e-12 | 35/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.50×** | +7.2 | 2e-11 | 34/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.4 | 7e-09 | 26/47 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.1 | 3e-08 | 29/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.8 | 4e-05 | 26/48 (SNU-423, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.7 | 7e-05 | 22/47 (LS 180, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.015 | 13/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.25×** | +2.9 | 0.065 | 8/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +2.8 | 0.068 | 9/48 (NCI-H1573, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -5.8 | 5e-06 | 3/48 (NCI-H23, HCT15, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.788×** | -4.2 | 0.007 | 17/48 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.790×** | -4.0 | 0.008 | 14/47 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.852× | -4.0 | 0.008 | 14/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.652×** | -4.0 | 0.008 | 13/47 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.802×** | -3.9 | 0.009 | 20/47 (LS 180, CHP-212, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.803×** | -3.7 | 0.014 | 19/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.817×** | -3.6 | 0.023 | 11/47 (RKO, NCI-H2347, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -3.4 | 0.047 | 10/47 (A-172, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.813×** | -3.3 | 0.047 | 16/47 (SW480, H4, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.702×** | -3.3 | 0.054 | 15/47 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.835× | -3.2 | 0.064 | 16/48 (HCT15, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 28.3 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +10.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.87× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 37.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.67× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 22.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.7) | — |
| [[RKO (line)]] | wt | 76.2 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +9.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 42.0 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.82× (z +11.3) | — |
| [[A-172 (line)]] | wt | 43.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.90× (z +9.8) | — |
| [[A549 (line)]] | wt | 35.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 21.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 30.8 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +11.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 33.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +11.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 37.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.45× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 23.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +10.6) | — |
| [[A498 (line)]] | wt | 43.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 39.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +16.1) | — |
| [[C32 (line)]] | wt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +14.7) | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0894× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +8.8) | — |
| [[J82 (line)]] | alt | 43.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 32.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 54.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 27.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 39.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +12.4) | — |
| [[A-427 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOPBP1]] | +0.68 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[TOP3A]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NDOR1]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[POLE3]] | +0.61 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ELAVL1]] | +0.61 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[DNAJC9]] | +0.60 | +0.41 / +0.67 | both halves | 4e-05 | STRING 706 |
| [[NUP107]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 | pathway: Cellular response to heat stress; STRING 528 |
| [[CENPO]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[LRR1]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DYRK4]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[ZNF718]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[RAD51AP1]] | +0.58 | +0.43 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOB]] | -0.67 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[TPPP]] | -0.60 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[JUND]] | -0.59 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[KLF2]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ACTG1]] | -0.54 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[TUBB2A]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MAPKBP1]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[TMEM150A]] | -0.51 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[TUBB2B]] | -0.50 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[LENG9]] | -0.50 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[DMXL1]] | -0.50 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[IFTAP]] | -0.50 | -0.21 / -0.42 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.4, -40.8); signed map (-40.7, -39.7). **Vector** length 64.4, 13.2% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.57 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +20.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.6 | +7.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +2.9 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | -0.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.0 | -0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | -0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -3.8 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.2 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.8 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:14,838,306-14,871,741 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSP70-4, HSP70L1 |
| Gene groups (HGNC) | Heat shock 70kDa proteins |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VDF9](https://www.uniprot.org/uniprotkb/Q0VDF9) (Heat shock 70 kDa protein 14):

> Component of the ribosome-associated complex (RAC), a complex involved in folding or maintaining nascent polypeptides in a folding-competent state. In the RAC complex, binds to the nascent polypeptide chain, while DNAJC2 stimulates its ATPase activity.

**Summary**, from NCBI Gene [51182](https://www.ncbi.nlm.nih.gov/gene/51182):

> Predicted to enable ATP hydrolysis activity; heat shock protein binding activity; and protein folding chaperone. Predicted to be involved in protein refolding. Located in cytosol and ribosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29526) · Entrez [51182](https://www.ncbi.nlm.nih.gov/gene/51182) · UniProt [Q0VDF9](https://www.uniprot.org/uniprotkb/Q0VDF9) · Ensembl [ENSG00000187522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187522)

## Data

Gene col 11918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11918); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11918]; `tensor/DDL_lfc|DDL_z.npy` [11918]; `embed/gene_vectors.npy` [11918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11918 or target_col == 11918). Every well: [[HSPA14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
