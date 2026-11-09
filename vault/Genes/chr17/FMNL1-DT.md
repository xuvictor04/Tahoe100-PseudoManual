---
symbol: "FMNL1-DT"
type: "gene"
col: 15523
ensembl_id: "ENSG00000267121"
name: "FMNL1 divergent transcript"
location: "17q21.31"
module: 13
arm: "+"
pooled_cpm: 10.41
n_lines_expressing: 27
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 13
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# FMNL1-DT

*FMNL1 divergent transcript* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.16× (z +10.8, q 2e-24, up in 4 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +7.8, q 2e-12, up in 6 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.479× (z -6.9, q 3e-09, down in 21 of 24 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Clobetasol propionate (drug)]] 5 µM: 0.612× (z -4.6, q 6e-04, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FMNL1]] (+0.71, fdr 7e-06, ⚠ same locus), [[GPR68]] (+0.64, fdr 8e-06), [[IGDCC4]] (+0.62, fdr 7e-06), [[IL11]] (+0.62, fdr 1e-05); moves opposite to [[IARS2]] (-0.54, fdr 4e-05), [[ALG6]] (-0.52, fdr 3e-05), [[PRDX3]] (-0.51, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CDH13]] → it (grade B ⚠); 13 go from it, the strongest it → [[LHX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +10.8 | 2e-24 | 4/16 (NCI-H2030, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.8 | 2e-12 | 6/21 (A549, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.66×** | +6.8 | 2e-09 | 6/20 (SNU-423, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +6.6 | 7e-09 | 2/14 (NCI-H2030, J82) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +5.8 | 8e-07 | 2/15 (NCI-H2030, LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.71×** | +5.0 | 5e-05 | 12/22 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.6 | 4e-04 | 12/22 (NCI-H460, CFPAC-1, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.4 | 7e-04 | 7/21 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +4.3 | 0.001 | 10/22 (SW480, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.52×** | +3.8 | 0.009 | 11/22 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.8 | 0.009 | 5/18 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +3.7 | 0.012 | 5/21 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.041 | 8/22 (SW480, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.63×** | +3.2 | 0.047 | 3/22 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.095 | 9/24 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15523.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.479×** | -6.9 | 3e-09 | 21/24 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.495×** | -6.6 | 1e-08 | 19/24 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.535×** | -5.8 | 1e-06 | 18/22 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.612×** | -4.6 | 6e-04 | 14/24 (NCI-H460, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.605×** | -4.4 | 0.002 | 15/23 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.670×** | -3.7 | 0.017 | 9/22 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.692×** | -3.4 | 0.042 | 15/22 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.475×** | -3.4 | 0.042 | 10/23 (CFPAC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.704×** | -3.3 | 0.066 | 13/24 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.712×** | -3.2 | 0.086 | 2/25 (PANC-1, LoVo) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.715×** | -3.1 | 0.088 | 11/22 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.698×** | -3.1 | 0.089 | 6/24 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.713× | -3.0 | 0.10 | 8/22 (HOP62, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 42.0 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0561× (z -15.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 39.1 | 6 (5 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.00× (z +12.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 5.59× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.104× (z -15.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW480 (line)]] | alt | 28.4 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0717× (z -17.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.199× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 35.1 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.120× (z -13.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 9.37 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0921× (z -11.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 29.4 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -12.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.4) |
| [[SNU-423 (line)]] | alt | 18.1 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +11.6) ⚠ cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 5 µM 0.0363× (z -17.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.499× (z -11.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -9.8) |
| [[A-172 (line)]] | wt | 14.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -9.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -10.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[PANC-1 (line)]] | alt | 4.06 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 10.7× (z +10.1) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A-427 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.69 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMNL1]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GPR68]] | +0.64 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[IGDCC4]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[IL11]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[POU2F2]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MDGA1]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ACVR1C]] | +0.59 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ZSWIM4]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PIK3CD]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[DNAH17]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[LINC00973]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TSPAN4]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IARS2]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ALG6]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PRDX3]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[RNPEP]] | -0.50 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SLC44A1]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[RPE]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[IFNGR1]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[HSD17B4]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[PTGFRN]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[DERL1]] | -0.48 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[CMPK1]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PHKA1]] | -0.48 | -0.37 / -0.56 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH13]] | B | CDH13 activity raises FMNL1-DT's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.29× lower at baseline in the lines without CDH13 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[ZNF469]] | B | ZNF469 activity raises FMNL1-DT's level | lines that do not express ZNF469 (20) vs lines expressing it (30) | 2.24× lower at baseline in the lines without ZNF469 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[MDGA1]] | B | MDGA1 activity raises FMNL1-DT's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without MDGA1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |
| [[FMNL1]] | C | FMNL1 activity raises FMNL1-DT's level | lines that do not express FMNL1 (18) vs lines expressing it (32) | 3.57× lower at baseline in the lines without FMNL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, WIPF1, SOGA3; co-absent with the target |
| [[RUNX3]] | C | RUNX3 activity raises FMNL1-DT's level | lines that do not express RUNX3 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without RUNX3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC6A15, IGF2BP1, ENSG00000286385; co-absent with the target |
| [[TRBC2]] | C | TRBC2 activity raises FMNL1-DT's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 2.93× lower at baseline in the lines without TRBC2 | 0.060 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHX1]] | B | FMNL1-DT activity raises LHX1's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without FMNL1-DT | 0.039 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | B | FMNL1-DT activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (protects the cells) | lines that do not express FMNL1-DT (23) vs lines expressing it (25) | the lines without FMNL1-DT: 0.83× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| cells under [[Fenofibrate (drug)]] 0.05 µM | B | FMNL1-DT activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express FMNL1-DT (23) vs lines expressing it (25) | the lines without FMNL1-DT: 1.29× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | B | FMNL1-DT activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express FMNL1-DT (23) vs lines expressing it (25) | the lines without FMNL1-DT: 0.87× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[PIK3CD]] | B | FMNL1-DT activity raises PIK3CD's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 2.33× lower at baseline in the lines without FMNL1-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[RASGRF2]] | B | FMNL1-DT activity raises RASGRF2's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 1.89× lower at baseline in the lines without FMNL1-DT | 0.080 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| cells under [[Erlotinib (drug)]] 0.05 µM | B | FMNL1-DT activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express FMNL1-DT (23) vs lines expressing it (25) | the lines without FMNL1-DT: 1.25× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[EMP3]] | B | FMNL1-DT activity raises EMP3's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without FMNL1-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[PLA2G4C]] | B | FMNL1-DT activity raises PLA2G4C's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 1.41× lower at baseline in the lines without FMNL1-DT | 0.099 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[FMNL1]] | C | FMNL1-DT activity raises FMNL1's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 5.90× lower at baseline in the lines without FMNL1-DT | 5e-05 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent; co-absent with the target |
| [[GCAWKR]] | C | FMNL1-DT activity raises GCAWKR's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 1.67× lower at baseline in the lines without FMNL1-DT | 0.027 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent; co-absent with the target |
| [[MRC2]] | C | FMNL1-DT activity raises MRC2's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 3.46× lower at baseline in the lines without FMNL1-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.374). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.6, -4.4); signed map (17.3, 49.2). **Vector** length 74.6, 21.3% of its response variance represented; |z| ≥ 3 in 635 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.0 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.8 | +3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.8 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -4.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -4.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | FMNL1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.31 — chr17:45,190,931-45,222,274 (-) |
| Ensembl biotype | lncRNA |
| Also known as | CTD-2020K17.1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55311) · Entrez [339192](https://www.ncbi.nlm.nih.gov/gene/339192) · Ensembl [ENSG00000267121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267121)

## Data

Gene col 15523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15523); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15523]; `tensor/DDL_lfc|DDL_z.npy` [15523]; `embed/gene_vectors.npy` [15523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15523 or target_col == 15523). Every well: [[FMNL1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMNL1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
