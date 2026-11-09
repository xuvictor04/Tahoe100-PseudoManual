---
symbol: "TMEM229B"
type: "gene"
col: 12537
ensembl_id: "ENSG00000198133"
name: "transmembrane protein 229B"
location: "14q24.1"
module: 87
arm: "+"
pooled_cpm: 2.57
n_lines_expressing: 47
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# TMEM229B

*transmembrane protein 229B* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.94× (z +9.8, q 4e-20, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +8.4, q 9e-15, up in 11 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.666× (z -4.3, q 0.008, down in 6 of 40 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCND3]] (+0.61, fdr 1e-05), [[CD200]] (+0.59, fdr 6e-05), [[PLEKHS1]] (+0.57, fdr 3e-05); moves opposite to [[DNAAF9]] (-0.51, fdr 7e-05), [[RAD17]] (-0.48, fdr 1e-04), [[RETREG2]] (-0.48, fdr 2e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[DOC2B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +9.8 | 4e-20 | 1/2 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +8.4 | 9e-15 | 11/24 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +7.6 | 5e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.2 | 6e-08 | 1/10 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.6 | 2e-06 | 3/42 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.011 | 3/35 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.026 | 3/33 (SW480, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.5 | 0.036 | 1/10 (PANC-1) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.036 | 5/33 (Panc 03.27, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.4 | 0.036 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.37×** | +3.4 | 0.036 | 3/38 (LoVo, LS 180, …) | rises with dose |  |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.040 | 1/20 (MIA PaCa-2) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.068 | 2/41 (MIA PaCa-2, RKO) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.068 | 2/18 (CFPAC-1, COLO 205) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.068 | 4/35 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.666×** | -4.3 | 0.008 | 6/40 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.675×** | -4.2 | 0.008 | 14/39 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.682×** | -4.1 | 0.008 | 11/41 (H4, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.698×** | -3.8 | 0.018 | 11/42 (LoVo, LS 180, …) | inconsistent across doses | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.669×** | -3.6 | 0.030 | 7/40 (NCI-H2030, SW48, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.741× | -3.2 | 0.13 | 7/37 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.746× | -3.1 | 0.14 | 4/32 (A-172, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.583× | -3.0 | 0.19 | 7/33 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.9 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0719× (z -15.5) |
| [[KATO III (line)]] | alt | 10.9 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0684× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 4.19 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0645× (z -8.7) |
| [[A-172 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.664 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.725 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.866 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.852 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.768 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.808 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.649 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.701 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.934 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCND3]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CD200]] | +0.59 | +0.65 / +0.38 | both halves | 6e-05 |  |
| [[PLEKHS1]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ARNT2-DT]] | +0.55 | +0.37 / +0.55 | both halves | 9e-05 |  |
| [[PLXNC1]] | +0.55 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[XKR9]] | +0.54 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[SP140]] | +0.54 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[TMCO4]] | +0.54 | +0.38 / +0.38 | both halves | 7e-05 |  |
| [[ZNF423]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SLC37A1]] | +0.52 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[HTR1D]] | +0.51 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[PAX5]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.51 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[RAD17]] | -0.48 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[RETREG2]] | -0.48 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[METTL26]] | -0.47 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[MFSD10]] | -0.47 | -0.42 / -0.26 | both halves | 4e-04 |  |
| [[KIAA1328]] | -0.46 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[VAT1]] | -0.46 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[CPNE3]] | -0.45 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[HEATR5B]] | -0.45 | -0.45 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[WASF2]] | -0.45 | -0.41 / -0.21 | both halves | 7e-04 |  |
| [[RRAS]] | -0.44 | -0.35 / -0.29 | both halves | 3e-04 |  |
| [[CLTCL1]] | -0.44 | -0.39 / -0.24 | both halves | 5e-04 |  |
| [[CFDP1]] | -0.44 | -0.41 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM229B's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CFTR]] | B | CFTR activity raises TMEM229B's level | lines that do not express CFTR (39) vs lines expressing it (11) | 1.99× lower at baseline in the lines without CFTR | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[NRIR]] | B | NRIR activity raises TMEM229B's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without NRIR | 0.022 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[BTC]] | B | BTC activity raises TMEM229B's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.18× lower at baseline in the lines without BTC | 0.053 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[CTSE]] | B | CTSE activity raises TMEM229B's level | lines that do not express CTSE (42) vs lines expressing it (8) | 2.19× lower at baseline in the lines without CTSE | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR |
| [[ATP10B]] | B | ATP10B activity raises TMEM229B's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.09× lower at baseline in the lines without ATP10B | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[MMP28]] | B | MMP28 activity raises TMEM229B's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.09× lower at baseline in the lines without MMP28 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[DSG4]] | B | DSG4 activity raises TMEM229B's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 1.86× lower at baseline in the lines without DSG4 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOC2B]] | C | TMEM229B activity lowers DOC2B's level | lines that do not express TMEM229B (3) vs lines expressing it (47) | 5.62× higher at baseline in the lines without TMEM229B | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |
| [[PCDH11X]] | C | TMEM229B activity lowers PCDH11X's level | lines that do not express TMEM229B (3) vs lines expressing it (47) | 3.48× higher at baseline in the lines without TMEM229B | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |
| [[ZC3HAV1]] | C | TMEM229B activity lowers ZC3HAV1's level | lines that do not express TMEM229B (3) vs lines expressing it (47) | 1.93× higher at baseline in the lines without TMEM229B | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.382). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.1, 58.0); signed map (67.3, 2.0). **Vector** length 45.1, 5.58% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +1.8 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | -1.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.3 | -4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 229B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:67,447,084-67,533,739 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33387; previously C14orf83 |
| Matched by | ensembl_id |

UniProt [Q8NBD8](https://www.uniprot.org/uniprotkb/Q8NBD8) carries no function annotation.

**Summary**, from NCBI Gene [161145](https://www.ncbi.nlm.nih.gov/gene/161145):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20130) · Entrez [161145](https://www.ncbi.nlm.nih.gov/gene/161145) · UniProt [Q8NBD8](https://www.uniprot.org/uniprotkb/Q8NBD8) · Ensembl [ENSG00000198133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198133)

## Data

Gene col 12537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12537); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12537]; `tensor/DDL_lfc|DDL_z.npy` [12537]; `embed/gene_vectors.npy` [12537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12537 or target_col == 12537). Every well: [[TMEM229B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM229B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
