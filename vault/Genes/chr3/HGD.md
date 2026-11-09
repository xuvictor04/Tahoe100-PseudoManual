---
symbol: "HGD"
type: "gene"
col: 3511
ensembl_id: "ENSG00000113924"
name: "homogentisate 1,2-dioxygenase"
location: "3q13.33"
module: 8
arm: "+"
pooled_cpm: 10.11
n_lines_expressing: 35
n_dd_up: 30
n_dd_down: 10
n_dd_up_clean: 23
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 25
direction_downstream: 16
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HGD

*homogentisate 1,2-dioxygenase* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.72× (z +15.5, q 0e+00, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.424× (z -10.2, q 2e-21, down in 22 of 31 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[A1CF]] (+0.66, fdr 7e-06), [[ACTR3C]] (+0.66, fdr 1e-05), [[PLCH1]] (+0.66, fdr 7e-06); moves opposite to [[FAM89B]] (-0.54, fdr 1e-04), [[SLC66A3]] (-0.51, fdr 1e-04), [[CAMSAP1]] (-0.51, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[ARHGEF38]] → it (grade B ⚠); 16 go from it, the strongest it → [[KIF3A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.72×** | +15.5 | 0e+00 | 19/31 (LoVo, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.30×** | +13.8 | 5e-41 | 13/25 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +13.3 | 5e-38 | 11/26 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.77×** | +9.4 | 5e-19 | 11/33 (A-172, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.9 | 4e-13 | 10/24 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.7 | 1e-12 | 6/20 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.1 | 1e-10 | 1/10 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.46×** | +6.3 | 2e-08 | 13/31 (LS 180, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +6.0 | 1e-07 | 1/15 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.49×** | +4.7 | 2e-04 | 12/30 (HEC-1-A, HT-29, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +4.5 | 4e-04 | 11/30 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.45×** | +4.3 | 7e-04 | 11/30 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.001 | 3/32 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.001 | 12/30 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.41×** | +4.0 | 0.002 | 12/32 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.003 | 13/30 (A549, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.003 | 8/30 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.004 | 10/30 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.006 | 2/26 (RPMI-7951, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +3.6 | 0.009 | 3/29 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.011 | 11/30 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3511.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.424×** | -10.2 | 2e-21 | 22/31 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.489×** | -8.5 | 7e-15 | 20/31 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.611×** | -5.8 | 1e-06 | 16/32 (H4, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.698×** | -4.3 | 0.003 | 13/28 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.504×** | -4.2 | 0.003 | 7/29 (HEC-1-A, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.805×** | -3.7 | 0.024 | 6/31 (HS-578T, HCT15, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.807×** | -3.6 | 0.024 | 12/31 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.760×** | -3.3 | 0.075 | 15/32 (COLO 205, SW1417, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.089 | 6/31 (A498, HT-29, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | **0.829×** | -3.2 | 0.089 | 0/32 | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.764× | -3.1 | 0.11 | 4/31 (RKO, SW 900, …) | inconsistent across doses | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.768× | -3.0 | 0.12 | 2/30 (LS 180, SW 900) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -14.0) |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0618× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.162× (z -11.7) |
| [[A498 (line)]] | wt | 32.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -12.6) |
| [[COLO 205 (line)]] | alt | 87.6 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0658× (z -16.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.198× (z -10.0) |
| [[HT-29 (line)]] | alt | 44.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -12.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.158× (z -12.5) |
| [[SW480 (line)]] | alt | 15.9 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0918× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -12.7) |
| [[KATO III (line)]] | alt | 21.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 3.31 | 0 | 1 | — | [[Clopidogrel (drug)]] 0.5 µM 0.0559× (z -8.7) |
| [[LS 180 (line)]] | wt | 12.3 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.60× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[A1CF]] | +0.66 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ACTR3C]] | +0.66 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SPATA6L]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[BTBD16]] | +0.64 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[ABCC2]] | +0.60 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[SGK2]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ABCC6]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[MGAM2]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SLC7A7]] | +0.59 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[HNF4G]] | +0.57 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[STEAP2-AS1]] | +0.56 | +0.53 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89B]] | -0.54 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[SLC66A3]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[CAMSAP1]] | -0.51 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[EHBP1L1]] | -0.51 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[ZNRF1]] | -0.49 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[TNK2]] | -0.48 | -0.41 / -0.21 | both halves | 6e-04 |  |
| [[AFAP1]] | -0.48 | -0.47 / -0.21 | both halves | 6e-04 |  |
| [[RTN2]] | -0.48 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[PDLIM7]] | -0.48 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[GNAI2]] | -0.47 | -0.41 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[KIF3A]] | -0.47 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[INPP5F]] | -0.47 | -0.41 / -0.20 | both halves | 7e-04 |  |
| [[ARID3B]] | -0.47 | -0.47 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 23, C 2. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF38]] | B | ARHGEF38 activity raises HGD's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.08× lower at baseline in the lines without ARHGEF38 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises HGD's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.21× lower at baseline in the lines without HNF1A-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[NPSR1-AS1]] | B | NPSR1-AS1 activity raises HGD's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.59× lower at baseline in the lines without NPSR1-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[CYP4F3]] | B | CYP4F3 activity raises HGD's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 3.03× lower at baseline in the lines without CYP4F3 | 0.007 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[RASSF6]] | B | RASSF6 activity raises HGD's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 3.20× lower at baseline in the lines without RASSF6 | 0.007 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[A1CF]] | B | A1CF activity raises HGD's level | lines that do not express A1CF (35) vs lines expressing it (15) | 4.17× lower at baseline in the lines without A1CF | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13 |
| [[MGAM2]] | B | MGAM2 activity raises HGD's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 2.82× lower at baseline in the lines without MGAM2 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[AKR1C3]] | B | AKR1C3 activity raises HGD's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without AKR1C3 | 0.018 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[F5]] | B | F5 activity raises HGD's level | lines that do not express F5 (39) vs lines expressing it (11) | 2.76× lower at baseline in the lines without F5 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2 |
| [[C11orf52]] | B | C11orf52 activity raises HGD's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.37× lower at baseline in the lines without C11orf52 | 0.028 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[FRK]] | B | FRK activity raises HGD's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.39× lower at baseline in the lines without FRK | 0.030 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[DSCAML1]] | B | DSCAML1 activity raises HGD's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.96× lower at baseline in the lines without DSCAML1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF3A]] | B | HGD activity lowers KIF3A's level | lines that do not express HGD (15) vs lines expressing it (35) | 1.37× higher at baseline in the lines without HGD | 0.007 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[RASSF6]] | B | HGD activity raises RASSF6's level | lines that do not express HGD (15) vs lines expressing it (35) | 3.44× lower at baseline in the lines without HGD | 0.010 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[AKR1C3]] | B | HGD activity raises AKR1C3's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.41× lower at baseline in the lines without HGD | 0.028 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[TNK2]] | B | HGD activity lowers TNK2's level | lines that do not express HGD (15) vs lines expressing it (35) | 1.24× higher at baseline in the lines without HGD | 0.033 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[SNTB1]] | B | HGD activity raises SNTB1's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.82× lower at baseline in the lines without HGD | 0.033 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[FRK]] | B | HGD activity raises FRK's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.48× lower at baseline in the lines without HGD | 0.033 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[FRAS1]] | B | HGD activity raises FRAS1's level | lines that do not express HGD (15) vs lines expressing it (35) | 3.56× lower at baseline in the lines without HGD | 0.042 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[NPNT]] | B | HGD activity raises NPNT's level | lines that do not express HGD (15) vs lines expressing it (35) | 3.44× lower at baseline in the lines without HGD | 0.045 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[DPP4]] | B | HGD activity raises DPP4's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.69× lower at baseline in the lines without HGD | 0.065 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[NPSR1-AS1]] | B | HGD activity raises NPSR1-AS1's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.42× lower at baseline in the lines without HGD | 0.074 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[PIP5K1B]] | B | HGD activity raises PIP5K1B's level | lines that do not express HGD (15) vs lines expressing it (35) | 3.14× lower at baseline in the lines without HGD | 0.074 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[RAMP1]] | B | HGD activity raises RAMP1's level | lines that do not express HGD (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without HGD | 0.078 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 51.3); signed map (57.4, -0.1). **Vector** length 81.9, 18.7% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.0 | +15.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +13.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.0 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +9.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.3 | -10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -8.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.5 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | homogentisate 1,2-dioxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:120,628,172-120,682,269 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HGO; previously AKU |
| Gene groups (HGNC) | Oxygenases |
| Reactome | 3 pathways, smallest: Tyrosine catabolism; Phenylalanine and tyrosine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93099](https://www.uniprot.org/uniprotkb/Q93099) (Homogentisate 1,2-dioxygenase):

> Catalyzes the conversion of homogentisate to maleylacetoacetate.

**Summary**, from NCBI Gene [3081](https://www.ncbi.nlm.nih.gov/gene/3081):

> This gene encodes the enzyme homogentisate 1,2 dioxygenase. This enzyme is involved in the catabolism of the amino acids tyrosine and phenylalanine. Mutations in this gene are the cause of the autosomal recessive metabolism disorder alkaptonuria.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:4892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4892) · Entrez [3081](https://www.ncbi.nlm.nih.gov/gene/3081) · UniProt [Q93099](https://www.uniprot.org/uniprotkb/Q93099) · Ensembl [ENSG00000113924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113924)

## Data

Gene col 3511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3511); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3511]; `tensor/DDL_lfc|DDL_z.npy` [3511]; `embed/gene_vectors.npy` [3511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3511 or target_col == 3511). Every well: [[HGD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HGD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
