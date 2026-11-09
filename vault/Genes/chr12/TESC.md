---
symbol: "TESC"
type: "gene"
col: 1557
ensembl_id: "ENSG00000088992"
name: "tescalcin"
location: "12q24.22"
module: 162
arm: "+"
pooled_cpm: 14.32
n_lines_expressing: 27
n_dd_up: 12
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# TESC

*tescalcin* — 12q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.19× (z +13.1, q 2e-36, up in 20 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.571× (z -6.7, q 2e-08, down in 17 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EML4]] (+0.66, fdr 1e-05), [[EPHB3]] (+0.58, fdr 6e-05), [[AZGP1]] (+0.57, fdr 3e-05); moves opposite to [[MTRF1]] (-0.46, fdr 2e-04), [[SUPT7L]] (-0.45, fdr 2e-04), [[PDCD6IP-DT]] (-0.45, fdr 3e-04).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TMEM163]] → it (grade B ⚠); 11 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.19×** | +13.1 | 2e-36 | 20/25 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +9.9 | 2e-20 | 19/25 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +9.5 | 4e-19 | 11/25 (HCT15, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.10×** | +8.8 | 3e-16 | 10/25 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.01×** | +8.3 | 2e-14 | 7/15 (HT-29, SW1417, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +7.7 | 2e-12 | 15/25 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.82×** | +7.1 | 9e-11 | 9/25 (SW1417, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.60×** | +5.2 | 2e-05 | 3/14 (SW1417, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.56×** | +5.0 | 3e-05 | 5/12 (NCI-H1573, LoVo, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.005 | 4/24 (SHP-77, HT-29, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.7 | 0.012 | 6/25 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.37×** | +3.6 | 0.018 | 7/22 (LoVo, HCT15, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | 1.29× | +3.0 | 0.11 | 4/23 (NCI-H1573, SW1417, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1557.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.571×** | -6.7 | 2e-08 | 17/25 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.696×** | -6.1 | 3e-07 | 17/25 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.702×** | -5.9 | 5e-07 | 11/25 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.638×** | -5.3 | 1e-05 | 15/25 (NCI-H460, KATO III, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.652×** | -5.1 | 4e-05 | 12/25 (CFPAC-1, NCI-H460, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.673×** | -4.7 | 2e-04 | 14/24 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.666×** | -4.6 | 3e-04 | 13/25 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.658×** | -4.6 | 3e-04 | 11/25 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.676×** | -4.5 | 5e-04 | 13/25 (CFPAC-1, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.695×** | -4.3 | 9e-04 | 11/25 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.694×** | -4.2 | 0.002 | 13/25 (SW480, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.782×** | -4.1 | 0.002 | 10/25 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.721×** | -3.9 | 0.004 | 13/25 (SW480, RKO, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.730×** | -3.7 | 0.007 | 10/25 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.732×** | -3.7 | 0.008 | 9/25 (NCI-H460, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.778×** | -3.7 | 0.008 | 10/25 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.753×** | -3.7 | 0.008 | 8/25 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 35.4 | 0 | 6 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.120× (z -10.0) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.144× (z -9.7) |
| [[SW480 (line)]] | alt | 16.6 | 0 | 6 | — | [[Trametinib (drug)]] 0.5 µM 0.310× (z -10.0) |
| [[KATO III (line)]] | alt | 87.8 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.174× (z -10.8) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.378× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 64.1 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.287× (z -9.5) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.306× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 7.83 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0465× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 24.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0966× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.209× (z -9.9) |
| [[A-427 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.327× (z -10.6) ⚠ cell-cycle shift, explains ~94% of this change |
| [[RKO (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.192× (z -8.5) |
| [[A-172 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.928 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EML4]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[EPHB3]] | +0.58 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[AZGP1]] | +0.57 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SMOX]] | +0.56 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[SMOC1]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD22]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[SYT13]] | +0.54 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[CEMIP]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TMEM163]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ARHGAP26]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[IQGAP2]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[IGFL4]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTRF1]] | -0.46 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[SUPT7L]] | -0.45 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[PDCD6IP-DT]] | -0.45 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[TADA2B]] | -0.45 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[YARS2]] | -0.45 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[RNF14]] | -0.45 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[PAAF1]] | -0.45 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[TSR2]] | -0.45 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[VPS39]] | -0.44 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[CLIP1]] | -0.44 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM163]] | B | TMEM163 activity raises TESC's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.91× lower at baseline in the lines without TMEM163 | 0.048 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[VSIG1]] | B | VSIG1 activity weakens TESC's drug response | lines that do not express VSIG1 (17) vs lines expressing it (8) | the lines without VSIG1 respond 1.35× as strongly (z diff -1.12); strongest at Panobinostat 0.5 µM: 1.96x vs 0.87x (z diff -3.3) | 0.069 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; target measured in part of the lines; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TESC's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TESC's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NCMAP]] | C | NCMAP activity raises TESC's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 4.32× lower at baseline in the lines without NCMAP | 0.005 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent; co-absent with the target |
| [[SPNS2]] | C | SPNS2 activity raises TESC's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 3.20× lower at baseline in the lines without SPNS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N; co-absent with the target |
| [[CYP24A1]] | C | CYP24A1 activity raises TESC's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 3.35× lower at baseline in the lines without CYP24A1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[SMOC1]] | C | SMOC1 activity raises TESC's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without SMOC1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises TESC's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 3.02× lower at baseline in the lines without FGFBP1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | TESC activity raises LMTK3's level | lines that do not express TESC (23) vs lines expressing it (27) | 2.95× lower at baseline in the lines without TESC | 0.005 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[NUP62CL]] | B | TESC activity raises NUP62CL's level | lines that do not express TESC (23) vs lines expressing it (27) | 2.47× lower at baseline in the lines without TESC | 0.028 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[ZG16B]] | B | TESC activity raises ZG16B's level | lines that do not express TESC (23) vs lines expressing it (27) | 1.73× lower at baseline in the lines without TESC | 0.031 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[FGFR4]] | B | TESC activity raises FGFR4's level | lines that do not express TESC (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without TESC | 0.060 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[FCHO1]] | B | TESC activity raises FCHO1's level | lines that do not express TESC (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without TESC | 0.075 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[AFAP1]] | B | TESC activity lowers AFAP1's level | lines that do not express TESC (23) vs lines expressing it (27) | 2.35× higher at baseline in the lines without TESC | 0.079 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| cells under [[Dinaciclib (drug)]] 5 µM | B | TESC activity lowers the cells' numbers under Dinaciclib 5 µM (makes them more sensitive) | lines that do not express TESC (23) vs lines expressing it (25) | the lines without TESC: 3.13× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[SLC52A3]] | C | TESC activity raises SLC52A3's level | lines that do not express TESC (23) vs lines expressing it (27) | 2.52× lower at baseline in the lines without TESC | 0.059 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1; co-absent with the target |
| [[PLS1]] | C | TESC activity raises PLS1's level | lines that do not express TESC (23) vs lines expressing it (27) | 3.61× lower at baseline in the lines without TESC | 0.062 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1; co-absent with the target |
| [[AZGP1]] | C | TESC activity raises AZGP1's level | lines that do not express TESC (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without TESC | 0.083 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1; co-absent with the target |
| [[NCMAP]] | C | TESC activity raises NCMAP's level | lines that do not express TESC (23) vs lines expressing it (27) | 2.07× lower at baseline in the lines without TESC | 0.087 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.596). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.0, 16.9); signed map (8.2, 53.5). **Vector** length 77.5, 20.9% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +3.4 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.4 | +8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | tescalcin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.22 — chr12:117,038,923-117,099,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSC, FLJ20607, CHP3 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BS2](https://www.uniprot.org/uniprotkb/Q96BS2) (Calcineurin B homologous protein 3):

> Functions as an integral cofactor in cell pH regulation by controlling plasma membrane-type Na(+)/H(+) exchange activity. Promotes the maturation, transport, cell surface stability and exchange activity of SLC9A1/NHE1 at the plasma membrane. Promotes the induction of hematopoietic stem cell differentiation toward megakaryocytic lineage. Essential for the coupling of ERK cascade activation with the expression of ETS family genes in megakaryocytic differentiation. Also involved in granulocytic …

**Summary**, from NCBI Gene [54997](https://www.ncbi.nlm.nih.gov/gene/54997):

> Enables calcium ion binding activity. Involved in several processes, including positive regulation of myeloid cell differentiation; positive regulation of sodium:proton antiporter activity; and regulation of gene expression. Located in several cellular components, including cytosol; lamellipodium; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26065) · Entrez [54997](https://www.ncbi.nlm.nih.gov/gene/54997) · UniProt [Q96BS2](https://www.uniprot.org/uniprotkb/Q96BS2) · Ensembl [ENSG00000088992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088992)

## Data

Gene col 1557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1557); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1557]; `tensor/DDL_lfc|DDL_z.npy` [1557]; `embed/gene_vectors.npy` [1557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1557 or target_col == 1557). Every well: [[TESC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TESC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
