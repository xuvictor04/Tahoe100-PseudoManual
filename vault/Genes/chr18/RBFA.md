---
symbol: "RBFA"
type: "gene"
col: 2151
ensembl_id: "ENSG00000101546"
name: "ribosome binding factor A"
location: "18q23"
module: 33
arm: "+"
pooled_cpm: 17.68
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RBFA

*ribosome binding factor A* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.03× (z +11.3, q 8e-27, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.528× (z -14.1, q 4e-42, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMSS1]] (+0.65, fdr 7e-06), [[NLE1]] (+0.64, fdr 1e-05), [[JPH1]] (+0.64, fdr 7e-06); moves opposite to [[DNASE1]] (-0.57, fdr 9e-05), [[LRP2BP]] (-0.56, fdr 3e-04), [[RNF217-AS1]] (-0.55, fdr 4e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +11.3 | 8e-27 | 39/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.88×** | +10.1 | 2e-21 | 33/41 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +9.5 | 6e-19 | 36/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.74×** | +8.5 | 2e-15 | 18/27 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +8.4 | 6e-15 | 31/47 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.59×** | +6.9 | 6e-10 | 19/34 (A549, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.54×** | +4.9 | 6e-05 | 16/45 (SK-MEL-2, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.7 | 2e-04 | 18/41 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +3.8 | 0.010 | 15/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.015 | 14/47 (RKO, NCI-H1573, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.021 | 11/44 (RKO, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.030 | 9/44 (LOX-IMVI, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.24×** | +3.3 | 0.034 | 21/47 (PANC-1, BT-474, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.23×** | +3.3 | 0.034 | 10/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.050 | 5/47 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.050 | 4/48 (HEC-1-A, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.058 | 6/46 (NCI-H23, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.080 | 9/47 (SHP-77, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -14.1 | 4e-42 | 37/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.371×** | -8.3 | 4e-14 | 32/48 (SK-MEL-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.375×** | -8.2 | 5e-14 | 30/44 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -6.2 | 8e-08 | 23/46 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.666×** | -6.1 | 1e-07 | 21/48 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.755×** | -4.5 | 6e-04 | 17/48 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.584×** | -4.5 | 6e-04 | 19/39 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -4.3 | 0.001 | 19/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.839× | -3.9 | 0.006 | 21/48 (SW480, PANC-1, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.787×** | -3.8 | 0.007 | 16/47 (SNU-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.777×** | -3.8 | 0.007 | 16/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.788×** | -3.8 | 0.007 | 17/47 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.812×** | -3.3 | 0.041 | 16/47 (H4, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.826×** | -3.0 | 0.093 | 13/46 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -3.0 | 0.093 | 15/48 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 17.6 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -14.1) |
| [[PANC-1 (line)]] | alt | 53.2 | 1 (1 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 2.46× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -14.8) |
| [[SW480 (line)]] | alt | 14.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.9) |
| [[BT-474 (line)]] | alt | 25.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +17.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 35.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.142× (z -12.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 16.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 28.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -19.7) |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0584× (z -10.0) |
| [[SW48 (line)]] | wt | 24.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.9) |
| [[A-427 (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.95× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.124× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.248× (z -8.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.1) |
| [[RKO (line)]] | wt | 28.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -8.6) |
| [[A-172 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMSS1]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NLE1]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[JPH1]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CEP83]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[DCAF4]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[RCL1]] | +0.61 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[NPM3]] | +0.60 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TAF4B]] | +0.59 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[WRN]] | +0.59 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[TSEN2]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[EIF2B3]] | +0.58 | +0.39 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNASE1]] | -0.57 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[LRP2BP]] | -0.56 | -0.26 / -0.39 | both halves | 3e-04 |  |
| [[RNF217-AS1]] | -0.55 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[C2]] | -0.55 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[PNISR-AS1]] | -0.54 | -0.16 / -0.43 | ⚠ not reproduced | 0.001 |  |
| [[KLHL3]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[SPAG4]] | -0.54 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[EPHX1]] | -0.54 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[PXDNL]] | -0.53 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[PIPOX]] | -0.53 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[ZNF75D]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SRP14]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PDHX]] | -0.52 | -0.40 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RBFA's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM78B]] | B | FAM78B activity raises RBFA's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.62× lower at baseline in the lines without FAM78B | 0.021 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[TENT5A]] | B | TENT5A activity lowers RBFA's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 1.81× higher at baseline in the lines without TENT5A | 0.040 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[NTN4]] | B | NTN4 activity lowers RBFA's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.46× higher at baseline in the lines without NTN4 | 0.064 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[SLC16A4]] | B | SLC16A4 activity lowers RBFA's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 1.57× higher at baseline in the lines without SLC16A4 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[SPAG4]] | B | SPAG4 activity lowers RBFA's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.54× higher at baseline in the lines without SPAG4 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.4, -43.0); signed map (-2.4, -57.4). **Vector** length 90.7, 19.1% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +11.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +9.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.2 | +3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | +3.7 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.2 | -14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosome binding factor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:80,034,389-80,050,651 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21172, HsT169; previously C18orf22 |
| Matched by | ensembl_id |

UniProt [Q8N0V3](https://www.uniprot.org/uniprotkb/Q8N0V3) carries no function annotation.

**Summary**, from NCBI Gene [79863](https://www.ncbi.nlm.nih.gov/gene/79863):

> Enables rRNA binding activity and ribosomal small subunit binding activity. Involved in mitochondrial small ribosomal subunit assembly. Located in mitochondrion. Is active in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26120](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26120) · Entrez [79863](https://www.ncbi.nlm.nih.gov/gene/79863) · UniProt [Q8N0V3](https://www.uniprot.org/uniprotkb/Q8N0V3) · Ensembl [ENSG00000101546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101546)

## Data

Gene col 2151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2151); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2151]; `tensor/DDL_lfc|DDL_z.npy` [2151]; `embed/gene_vectors.npy` [2151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2151 or target_col == 2151). Every well: [[RBFA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBFA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
