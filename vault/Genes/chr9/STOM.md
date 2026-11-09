---
symbol: "STOM"
type: "gene"
col: 7248
ensembl_id: "ENSG00000148175"
name: "stomatin"
location: "9q33.2"
module: 139
arm: "+"
pooled_cpm: 33.86
n_lines_expressing: 34
n_dd_up: 56
n_dd_down: 9
n_dd_up_clean: 43
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# STOM

*stomatin* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 56 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.06× (z +9.5, q 2e-18, up in 21 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 0.05 µM: 1.78× (z +6.9, q 4e-10, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Tofacitinib (citrate) (drug)]] 5 µM: 0.724× (z -5.2, q 1e-04, down in 17 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDLIM1]] (+0.70, fdr 7e-06), [[SAA2]] (+0.66, fdr 7e-06), [[SAA2-SAA4]] (+0.66, fdr 7e-06); moves opposite to [[AADACP1]] (-0.58, fdr 1e-05), [[TMEM158]] (-0.58, fdr 1e-05), [[ANTXR2]] (-0.55, fdr 1e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[FLOT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 56 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +9.5 | 2e-18 | 21/28 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.87×** | +8.2 | 9e-14 | 22/32 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +8.1 | 9e-14 | 17/24 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.85×** | +8.0 | 1e-13 | 21/32 (KATO III, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.80×** | +7.7 | 2e-12 | 20/31 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.78×** | +6.9 | 4e-10 | 19/31 (NCI-H460, A549, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +6.6 | 4e-09 | 23/32 (NCI-H2347, KATO III, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.63×** | +6.4 | 1e-08 | 19/32 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.59×** | +6.0 | 1e-07 | 19/31 (NCI-H460, A549, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +5.9 | 2e-07 | 16/31 (KATO III, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +5.9 | 2e-07 | 20/32 (hTERT-HPNE, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.57×** | +5.9 | 2e-07 | 16/31 (NCI-H460, A549, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +5.8 | 4e-07 | 19/32 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.55×** | +5.7 | 4e-07 | 18/32 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.5 | 2e-06 | 15/32 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.54×** | +5.4 | 2e-06 | 21/32 (A549, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 2e-06 | 16/32 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.39×** | +5.3 | 4e-06 | 17/32 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.50×** | +5.3 | 4e-06 | 16/31 (NCI-H460, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.49×** | +5.2 | 5e-06 | 18/31 (NCI-H460, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.724×** | -5.2 | 1e-04 | 17/32 (Hs 766T, C32, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.736×** | -5.1 | 1e-04 | 19/32 (Hs 766T, C32, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.694×** | -4.8 | 3e-04 | 19/32 (BT-474, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.714×** | -4.5 | 1e-03 | 19/31 (A498, C32, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.714×** | -4.5 | 1e-03 | 16/32 (LOX-IMVI, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.712×** | -4.2 | 0.002 | 17/32 (C32, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.731×** | -4.1 | 0.003 | 12/31 (H4, SNU-423, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.735×** | -4.1 | 0.003 | 16/31 (SW 900, SNU-423, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.760×** | -3.5 | 0.031 | 15/31 (SW 1271, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 72.7 | 19 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.81× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 20.7 | 19 (1 ⚠) | 0 | [[Dexamethasone (drug)]] 0.5 µM 6.81× (z +13.5) | — |
| [[SW 900 (line)]] | alt | 54.3 | 10 | 0 | [[Dexamethasone (drug)]] 0.5 µM 4.22× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 43.4 | 6 | 0 | [[Dexamethasone (drug)]] 0.5 µM 3.59× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 5 | 0 | [[Triamcinolone (drug)]] 0.5 µM 5.19× (z +9.4) | — |
| [[KATO III (line)]] | alt | 17.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 35.7 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.53× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 52.5 | 3 | 0 | [[Dexamethasone (drug)]] 0.5 µM 3.78× (z +9.2) | — |
| [[A498 (line)]] | wt | 208 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.387× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 50.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 71.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.297× (z -8.6) |
| [[Hs 766T (line)]] | wt | 42.9 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.206× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 17.8 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 9.48× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 88.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.37 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM1]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SAA2]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SAA2-SAA4]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[FKBP5]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[MAOA]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[BCL6]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[NNMT]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ACSL1]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[CPD]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[FGA]] | +0.65 | +0.58 / +0.64 | both halves | 8e-06 | **novel candidate** |
| [[B4GALT1]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[C3]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AADACP1]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TMEM158]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[ANTXR2]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MMP1]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[AADAC]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[GCKR]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[RABGEF1P3]] | -0.52 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[PTHLH]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ARID3B]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PLEKHG5]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 | pathway: RHOA GTPase cycle |
| [[EFL1]] | -0.51 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[GJA1]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 | pathway: RHOJ GTPase cycle; STRING 474 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STOM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[B4GALT1]] | C | B4GALT1 activity raises STOM's level | lines that do not express B4GALT1 (3) vs lines expressing it (47) | 4.12× lower at baseline in the lines without B4GALT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TIMP1, UGDH, ATXN1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLOT2]] | B | STOM activity lowers FLOT2's level | lines that do not express STOM (16) vs lines expressing it (34) | 1.35× higher at baseline in the lines without STOM | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000227355, TRIM6, AOX1 |
| [[IFNGR1]] | B | STOM activity lowers IFNGR1's level | lines that do not express STOM (16) vs lines expressing it (34) | 1.00× higher at baseline in the lines without STOM | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000227355, TRIM6, AOX1 |
| [[LINC02057]] | B | STOM activity raises LINC02057's level | lines that do not express STOM (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without STOM | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000227355, TRIM6, AOX1 |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, 16.4); signed map (17.4, 28.9). **Vector** length 118, 33.2% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.57 to 6); *interferon gamma response* (hallmark, mean cos +0.56 to 6); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.5 | +5.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.5 | +5.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.4 | +5.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +4.4 | +5.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -4.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | stomatin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:121,338,987-121,370,304 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BND7; previously EPB7, EPB72 |
| Gene groups (HGNC) | Stomatin family |
| Hallmark sets | ADIPOGENESIS, P53_PATHWAY |
| Reactome | 15 pathways, smallest: RHOH GTPase cycle; RHOJ GTPase cycle; RHOQ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P27105](https://www.uniprot.org/uniprotkb/P27105) (Stomatin):

> Regulates ion channel activity and transmembrane ion transport. Regulates ASIC2 and ASIC3 channel activity.

**Summary**, from NCBI Gene [2040](https://www.ncbi.nlm.nih.gov/gene/2040):

> This gene encodes a member of a highly conserved family of integral membrane proteins. The encoded protein localizes to the cell membrane of red blood cells and other cell types, where it may regulate ion channels and transporters. Loss of localization of the encoded protein is associated with hereditary stomatocytosis, a form of hemolytic anemia. There is a pseudogene for this gene on chromosome 6. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:3383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3383) · Entrez [2040](https://www.ncbi.nlm.nih.gov/gene/2040) · UniProt [P27105](https://www.uniprot.org/uniprotkb/P27105) · Ensembl [ENSG00000148175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148175)

## Data

Gene col 7248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7248); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7248]; `tensor/DDL_lfc|DDL_z.npy` [7248]; `embed/gene_vectors.npy` [7248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7248 or target_col == 7248). Every well: [[STOM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STOM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
