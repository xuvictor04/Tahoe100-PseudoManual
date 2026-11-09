---
symbol: "MSS51"
type: "gene"
col: 9289
ensembl_id: "ENSG00000166343"
name: "MSS51 mitochondrial translational activator"
location: "10q22.2"
module: 38
arm: "+"
pooled_cpm: 4.48
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# MSS51

*MSS51 mitochondrial translational activator* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +4.8, q 0.001, up in 18 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.357× (z -10.0, q 5e-21, down in 31 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.450× (z -7.8, q 2e-12, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP3CB]] (+0.75, fdr 7e-06, ⚠ read-through risk), [[TECPR2]] (+0.69, fdr 7e-06), [[EPHX3]] (+0.66, fdr 7e-06), [[ZNF577]] (+0.59, fdr 1e-05); moves opposite to [[PLAAT3]] (-0.54, fdr 3e-05), [[GALM]] (-0.53, fdr 6e-05), [[DENND4C]] (-0.53, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NEK10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +4.8 | 0.001 | 18/35 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.024 | 11/45 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.024 | 5/45 (HOP62, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +3.7 | 0.030 | 0/4 | top dose only | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +3.6 | 0.030 | 11/44 (A498, CFPAC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.357×** | -10.0 | 5e-21 | 31/37 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.450×** | -7.8 | 2e-12 | 25/45 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.466×** | -7.4 | 2e-11 | 27/46 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.507×** | -6.6 | 5e-09 | 24/45 (HepG2/C3A, LS 180, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.313×** | -5.9 | 4e-07 | 22/41 (RKO, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.549×** | -5.8 | 5e-07 | 20/45 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.572×** | -5.4 | 5e-06 | 24/44 (PANC-1, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.597×** | -5.0 | 4e-05 | 21/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.535×** | -4.6 | 2e-04 | 17/30 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.414×** | -4.5 | 4e-04 | 16/34 (A549, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.549×** | -4.4 | 5e-04 | 16/43 (A-427, HEC-1-A, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.613×** | -4.1 | 0.002 | 12/45 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.664×** | -3.8 | 0.008 | 9/41 (HS-578T, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.534×** | -3.2 | 0.057 | 14/38 (NCI-H2347, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.734×** | -3.0 | 0.099 | 7/45 (BT-474, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.60 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0481× (z -17.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.149× (z -10.8) |
| [[HOP62 (line)]] | alt | 7.33 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0586× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.113× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 4.68 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0295× (z -14.5) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.138× (z -9.4) |
| [[SW480 (line)]] | alt | 4.99 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0876× (z -12.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 6.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0457× (z -13.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 4.66 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0779× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 4.14 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0849× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 2.80 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0354× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 4.14 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0637× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 6.40 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 5.85 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.119× (z -9.1) |
| [[SNU-423 (line)]] | alt | 6.78 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0559× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB]] | +0.75 | +0.78 / +0.73 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 2.9 kb 3′ of PPP3CB on the same strand (can correlate by spillover, not regulation) |
| [[TECPR2]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZNF577]] | +0.59 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[EP400P1]] | +0.58 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[TMED6]] | +0.58 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[STAC3]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ADCY10P1]] | +0.57 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[SLC22A20P]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CFAP251]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[LINC01355]] | +0.56 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[LINC01191]] | +0.56 | +0.65 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAAT3]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[GALM]] | -0.53 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[DENND4C]] | -0.53 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[PRKAG2]] | -0.52 | -0.64 / -0.36 | both halves | 9e-05 |  |
| [[RRAGD]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HMGN3]] | -0.51 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[SLC25A27]] | -0.51 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[THRA]] | -0.50 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TENT4B]] | -0.50 | -0.20 / -0.47 | ⚠ not reproduced | 7e-04 |  |
| [[PIK3C2B]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[LGR4]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[PLEKHH3]] | -0.48 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[CLN3]] | -0.48 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEK10]] | B | NEK10 activity raises MSS51's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without NEK10 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises MSS51's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without LINC00334 | 0.036 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[PARVG]] | B | PARVG activity raises MSS51's level | lines that do not express PARVG (15) vs lines expressing it (35) | 1.17× lower at baseline in the lines without PARVG | 0.091 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[MPP4]] | C | MPP4 activity raises MSS51's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without MPP4 | 0.071 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent |
| [[MMP25]] | C | MMP25 activity raises MSS51's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.58× lower at baseline in the lines without MMP25 | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.505). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.5, -15.1); signed map (13.3, 0.8). **Vector** length 51.5, 6.46% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.7 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | -0.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +1.1 | +0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.1 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.0 | -0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.1 | -6.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.2 | -4.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MSS51 mitochondrial translational activator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,423,579-73,433,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39565; previously ZMYND17 |
| Gene groups (HGNC) | Zinc fingers MYND-type |
| Matched by | ensembl_id |

UniProt [Q4VC12](https://www.uniprot.org/uniprotkb/Q4VC12) carries no function annotation.

**Summary**, from NCBI Gene [118490](https://www.ncbi.nlm.nih.gov/gene/118490):

> Predicted to enable zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21000) · Entrez [118490](https://www.ncbi.nlm.nih.gov/gene/118490) · UniProt [Q4VC12](https://www.uniprot.org/uniprotkb/Q4VC12) · Ensembl [ENSG00000166343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166343)

## Data

Gene col 9289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9289); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9289]; `tensor/DDL_lfc|DDL_z.npy` [9289]; `embed/gene_vectors.npy` [9289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9289 or target_col == 9289). Every well: [[MSS51 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSS51.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
