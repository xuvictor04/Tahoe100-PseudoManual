---
symbol: "GPX3"
type: "gene"
col: 13059
ensembl_id: "ENSG00000211445"
name: "glutathione peroxidase 3"
location: "5q33.1"
module: 50
arm: "+"
pooled_cpm: 11.22
n_lines_expressing: 24
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 13
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# GPX3

*glutathione peroxidase 3* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.51× (z +15.5, q 0e+00, up in 17 of 18 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.17× (z +10.0, q 3e-21, up in 19 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.572× (z -5.1, q 2e-04, down in 15 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (H4 0.0222×, NCI-H1792 0.130×, A498 0.262×, HepG2/C3A 0.124×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (H4 0.0953×, NCI-H2347 0.273×, A498 0.330×, HepG2/C3A 0.169×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.129×); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2030 0.0853×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITM2C]] (+0.57, fdr 1e-05), [[JAM3]] (+0.56, fdr 2e-05), [[B4GALNT1]] (+0.55, fdr 2e-05); moves opposite to [[CKMT2-AS1]] (-0.50, fdr 1e-04), [[LINC00174]] (-0.48, fdr 1e-04), [[INO80D]] (-0.48, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 13 go from it, the strongest it → [[GLOD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **5.51×** | +15.5 | 0e+00 | 17/18 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.49×** | +13.1 | 6e-37 | 13/13 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.06×** | +11.8 | 8e-30 | 13/15 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.17×** | +10.0 | 3e-21 | 19/22 (A498, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.68×** | +9.0 | 3e-17 | 19/21 (HOP62, PANC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.70×** | +8.5 | 1e-15 | 20/22 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.43×** | +8.1 | 6e-14 | 18/21 (HOP62, HT-29, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.21×** | +7.2 | 4e-11 | 17/21 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.20×** | +7.2 | 5e-11 | 19/21 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.18×** | +7.1 | 7e-11 | 17/21 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **2.22×** | +7.0 | 1e-10 | 15/20 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.69×** | +6.8 | 6e-10 | 13/22 (HepG2/C3A, NCI-H2347, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.01×** | +6.3 | 1e-08 | 17/21 (PANC-1, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.0 | 1e-07 | 15/22 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +5.3 | 4e-06 | 14/21 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +5.1 | 1e-05 | 17/21 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.24×** | +3.8 | 0.004 | 15/22 (A549, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.004 | 9/22 (NCI-H1792, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.005 | 9/22 (CFPAC-1, SW1417, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Thymol (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.014 | 14/22 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +2.8 | 0.091 | 11/22 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13059.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (H4 0.0222×, NCI-H1792 0.130×, A498 0.262×, HepG2/C3A 0.124×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (H4 0.0953×, NCI-H2347 0.273×, A498 0.330×, HepG2/C3A 0.169×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.129×); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2030 0.0853×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.572×** | -5.1 | 2e-04 | 15/22 (H4, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.694× | -3.2 | 0.33 | 6/22 (H4, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.518× | -3.1 | 0.33 | 5/22 (NCI-H460, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 87.3 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.71× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 42.3 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -8.6) |
| [[PANC-1 (line)]] | alt | 2.82 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.5× (z +9.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 10.3× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 39.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -10.4) |
| [[H4 (line)]] | wt | 69.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0222× (z -19.4) |
| [[HOP62 (line)]] | alt | 9.75 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 8.04× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 8.06 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 8.62× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 69.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -12.3) |
| [[SW1417 (line)]] | alt | 27.5 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.16× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 7.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 7.06 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0853× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 9.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.129× (z -9.9) |
| [[A-172 (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.667 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2C]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[JAM3]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[B4GALNT1]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[EGFL7]] | +0.55 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[PROCR]] | +0.54 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ECM1]] | +0.54 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[PLBD2]] | +0.53 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[SCPEP1]] | +0.52 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[GUCY1B1]] | +0.52 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[SLC22A17]] | +0.51 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[LAPTM4B]] | +0.51 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[PCDHB2]] | +0.51 | +0.55 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKMT2-AS1]] | -0.50 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[LINC00174]] | -0.48 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[INO80D]] | -0.48 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[PDCD7]] | -0.47 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[PPIG]] | -0.47 | -0.44 / -0.39 | both halves | 5e-05 | STRING 459 |
| [[ZNF696]] | -0.47 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.46 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[AFG3L1P]] | -0.45 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[LINC02340]] | -0.45 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[GLOD4]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TRIP11]] | -0.44 | -0.41 / -0.32 | both halves | 1e-04 |  |
| [[CYP20A1]] | -0.43 | -0.49 / -0.20 | ⚠ not reproduced | 7e-04 |  |
| [[BCDIN3D]] | -0.43 | -0.36 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPX3's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CCDC69]] | B | CCDC69 activity raises GPX3's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 2.73× lower at baseline in the lines without CCDC69 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NXPE3]] | B | NXPE3 activity raises GPX3's level | lines that do not express NXPE3 (5) vs lines expressing it (45) | 3.34× lower at baseline in the lines without NXPE3 | 0.096 | ⚠ within organs, on part of the lines; also absent: FAM171B, TTC23L, LCA5; maybe low, not absent |
| [[CD74]] | C | CD74 activity raises GPX3's level | lines that do not express CD74 (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without CD74 | 0.031 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLOD4]] | B | GPX3 activity lowers GLOD4's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.30× higher at baseline in the lines without GPX3 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[LGALS3BP]] | B | GPX3 activity raises LGALS3BP's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without GPX3 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[CTSD]] | B | GPX3 activity raises CTSD's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.77× lower at baseline in the lines without GPX3 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[TMEM161A]] | B | GPX3 activity lowers TMEM161A's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.45× higher at baseline in the lines without GPX3 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[ZNF696]] | B | GPX3 activity lowers ZNF696's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.34× higher at baseline in the lines without GPX3 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[RAB39A]] | B | GPX3 activity lowers RAB39A's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.33× higher at baseline in the lines without GPX3 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[PSAP]] | B | GPX3 activity raises PSAP's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.29× lower at baseline in the lines without GPX3 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| cells under [[Terfenadine (drug)]] 5 µM | B | GPX3 activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express GPX3 (26) vs lines expressing it (22) | the lines without GPX3: 0.93× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[PTPRS]] | B | GPX3 activity lowers PTPRS's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.46× higher at baseline in the lines without GPX3 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[PSMB2]] | B | GPX3 activity lowers PSMB2's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.13× higher at baseline in the lines without GPX3 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[BDP1]] | B | GPX3 activity lowers BDP1's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.05× higher at baseline in the lines without GPX3 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[HSP90AA2P]] | B | GPX3 activity lowers HSP90AA2P's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.24× higher at baseline in the lines without GPX3 | 0.0999 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.5, 0.3); signed map (-53.4, -12.7). **Vector** length 57.8, 14.1% of its response variance represented; |z| ≥ 3 in 631 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.3 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.2 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +11.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +9.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +3.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | -1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | glutathione peroxidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:151,020,591-151,028,988 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Selenoproteins; Glutathione peroxidase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, MYOGENESIS, APOPTOSIS, UV_RESPONSE_UP, ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Detoxification of Reactive Oxygen Species; Cellular response to chemical stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P22352](https://www.uniprot.org/uniprotkb/P22352) (Glutathione peroxidase 3):

> Protects cells and enzymes from oxidative damage, by catalyzing the reduction of hydrogen peroxide, lipid peroxides and organic hydroperoxide, by glutathione.

**Summary**, from NCBI Gene [2878](https://www.ncbi.nlm.nih.gov/gene/2878):

> The protein encoded by this gene belongs to the glutathione peroxidase family, members of which catalyze the reduction of organic hydroperoxides and hydrogen peroxide (H2O2) by glutathione, and thereby protect cells against oxidative damage. Several isozymes of this gene family exist in vertebrates, which vary in cellular location and substrate specificity. This isozyme is secreted, and is abundantly found in plasma. Downregulation of expression of this gene by promoter hypermethylation has …

**Accessions** — [HGNC:4555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4555) · Entrez [2878](https://www.ncbi.nlm.nih.gov/gene/2878) · UniProt [P22352](https://www.uniprot.org/uniprotkb/P22352) · Ensembl [ENSG00000211445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211445)

## Data

Gene col 13059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13059); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13059]; `tensor/DDL_lfc|DDL_z.npy` [13059]; `embed/gene_vectors.npy` [13059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13059 or target_col == 13059). Every well: [[GPX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
