---
symbol: "CCL28"
type: "gene"
col: 7575
ensembl_id: "ENSG00000151882"
name: "C-C motif chemokine ligand 28"
location: "5p12"
module: 144
arm: "+"
pooled_cpm: 14.2
n_lines_expressing: 26
n_dd_up: 26
n_dd_down: 24
n_dd_up_clean: 20
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# CCL28

*C-C motif chemokine ligand 28* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +12.8, q 5e-35, up in 3 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.356× (z -13.6, q 1e-39, down in 23 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2orf49]] (+0.55, fdr 2e-05), [[FAM13C]] (+0.54, fdr 3e-05), [[EGLN1]] (+0.54, fdr 2e-05); moves opposite to [[ASAP2]] (-0.60, fdr 2e-05), [[THSD4]] (-0.51, fdr 4e-05), [[BCAR3]] (-0.50, fdr 7e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NFATC4]] → it (grade B ⚠); 10 go from it, the strongest it → [[C11orf52]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +12.8 | 5e-35 | 3/23 (HepG2/C3A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +7.9 | 8e-13 | 4/20 (LS 180, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.0 | 5e-07 | 4/21 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +5.8 | 8e-07 | 11/24 (HEC-1-A, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +5.6 | 3e-06 | 19/24 (HEC-1-A, HT-29, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.45×** | +5.1 | 3e-05 | 12/24 (HEC-1-A, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.6 | 4e-04 | 11/24 (HEC-1-A, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +4.4 | 7e-04 | 11/24 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 9e-04 | 14/24 (HT-29, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 11/24 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.002 | 8/24 (NCI-H1792, RPMI-7951, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.004 | 8/24 (LOX-IMVI, SW 900, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +3.8 | 0.007 | 10/24 (HOP62, SW 900, …) | rises with dose | low cells (technical?) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.007 | 8/24 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +3.6 | 0.012 | 11/24 (HEC-1-A, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.012 | 6/24 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.013 | 9/24 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +3.4 | 0.019 | 3/21 (C32, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.019 | 5/24 (SW 900, RPMI-7951, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.356×** | -13.6 | 1e-39 | 23/24 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.388×** | -12.5 | 2e-33 | 22/24 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.440×** | -10.9 | 4e-25 | 22/24 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -9.0 | 3e-17 | 17/24 (LOX-IMVI, SW 900, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.618×** | -9.0 | 3e-17 | 22/23 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -8.5 | 2e-15 | 19/24 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.544×** | -8.1 | 7e-14 | 19/23 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.568×** | -7.5 | 6e-12 | 18/24 (SNU-423, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.569×** | -7.0 | 1e-10 | 20/24 (C32, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.628×** | -6.1 | 4e-08 | 16/23 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.630×** | -6.1 | 6e-08 | 19/24 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.883× | -5.8 | 3e-07 | 5/24 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.646×** | -5.8 | 3e-07 | 18/24 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.648×** | -5.7 | 4e-07 | 17/24 (SNU-423, SW 900, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -4.5 | 2e-04 | 16/24 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.726×** | -4.2 | 8e-04 | 7/24 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 43.3 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0303× (z -36.0) |
| [[C32 (line)]] | wt | 123 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0774× (z -30.1) |
| [[NCI-H2347 (line)]] | alt | 61.8 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -22.5) |
| [[NCI-H1792 (line)]] | alt | 56.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -23.1) |
| [[SW 900 (line)]] | alt | 36.3 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -16.9) |
| [[LOX-IMVI (line)]] | wt | 24.3 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 74.4 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -20.7) |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -13.8) |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -17.5) |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.113× (z -11.4) |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.8) |
| [[SW480 (line)]] | alt | 12.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 5.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -9.0) |
| [[HOP62 (line)]] | alt | 8.05 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.2) |
| [[J82 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.5) |
| [[A-172 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf49]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[FAM13C]] | +0.54 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[EGLN1]] | +0.54 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[ZNF292]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ACBD5]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[DCAF5]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SEC31B]] | +0.52 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[EYA1]] | +0.52 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FMO5]] | +0.52 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[RBKS]] | +0.51 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[PHF21A]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PIAS2]] | +0.51 | +0.48 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASAP2]] | -0.60 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[THSD4]] | -0.51 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[BCAR3]] | -0.50 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[LRP8]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ITGA6]] | -0.47 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[MICAL2]] | -0.47 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[PLXNA1]] | -0.47 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[NPIPB4]] | -0.46 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[PXN]] | -0.46 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[ARHGAP39]] | -0.45 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[RANGAP1]] | -0.45 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[AGO2]] | -0.45 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFATC4]] | B | NFATC4 activity raises CCL28's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without NFATC4 | 0.055 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CCL28's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[LOXL4]] | C | LOXL4 activity raises CCL28's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without LOXL4 | 0.021 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises CCL28's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.08× lower at baseline in the lines without WFDC2 | 0.046 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf52]] | B | CCL28 activity raises C11orf52's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.61× lower at baseline in the lines without CCL28 | 0.014 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[CYP27A1]] | B | CCL28 activity raises CYP27A1's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without CCL28 | 0.051 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[RANGAP1]] | B | CCL28 activity lowers RANGAP1's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.19× higher at baseline in the lines without CCL28 | 0.055 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[SNTB1]] | B | CCL28 activity raises SNTB1's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 2.75× lower at baseline in the lines without CCL28 | 0.060 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[FMO5]] | B | CCL28 activity raises FMO5's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.75× lower at baseline in the lines without CCL28 | 0.063 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[NPEPPS]] | B | CCL28 activity raises NPEPPS's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.33× lower at baseline in the lines without CCL28 | 0.067 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[BPNT1]] | B | CCL28 activity raises BPNT1's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.29× lower at baseline in the lines without CCL28 | 0.071 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[FNIP2]] | B | CCL28 activity raises FNIP2's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.54× lower at baseline in the lines without CCL28 | 0.073 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[GALM]] | B | CCL28 activity raises GALM's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without CCL28 | 0.075 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |
| [[WFDC2]] | C | CCL28 activity raises WFDC2's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without CCL28 | 0.026 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74; co-absent with the target |

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, -21.9); signed map (-32.5, 27.7). **Vector** length 77.0, 21.0% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +3.2 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.6 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +5.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -9.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | C-C motif chemokine ligand 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:43,376,645-43,412,391 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCYA28, MEC, CCK1 |
| Gene groups (HGNC) | Chemokine ligands |
| Reactome | 7 pathways, smallest: Chemokine receptors bind chemokines; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRJ3](https://www.uniprot.org/uniprotkb/Q9NRJ3) (C-C motif chemokine 28):

> Chemotactic activity for resting CD4, CD8 T-cells and eosinophils. Binds to CCR3 and CCR10 and induces calcium mobilization in a dose-dependent manner.

**Summary**, from NCBI Gene [56477](https://www.ncbi.nlm.nih.gov/gene/56477):

> This antimicrobial gene belongs to the subfamily of small cytokine CC genes. Cytokines are a family of secreted proteins involved in immunoregulatory and inflammatory processes. The CC cytokines are proteins characterized by two adjacent cysteines. The cytokine encoded by this gene displays chemotactic activity for resting CD4 or CD8 T cells and eosinophils. The product of this gene binds to chemokine receptors CCR3 and CCR10. This chemokine may play a role in the physiology of extracutaneous …

**Accessions** — [HGNC:17700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17700) · Entrez [56477](https://www.ncbi.nlm.nih.gov/gene/56477) · UniProt [Q9NRJ3](https://www.uniprot.org/uniprotkb/Q9NRJ3) · Ensembl [ENSG00000151882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151882)

## Data

Gene col 7575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7575); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7575]; `tensor/DDL_lfc|DDL_z.npy` [7575]; `embed/gene_vectors.npy` [7575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7575 or target_col == 7575). Every well: [[CCL28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCL28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
