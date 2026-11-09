---
symbol: "GKAP1"
type: "gene"
col: 9069
ensembl_id: "ENSG00000165113"
name: "G kinase anchoring protein 1"
location: "9q21.32"
module: 222
arm: "+"
pooled_cpm: 18.26
n_lines_expressing: 47
n_dd_up: 32
n_dd_down: 5
n_dd_up_clean: 26
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/222"]
generated_by: "tahoemap"
---

# GKAP1

*G kinase anchoring protein 1* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 2.06× (z +11.2, q 4e-26, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.368× (z -8.1, q 4e-13, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND5B]] (+0.68, fdr 7e-06), [[PHIP]] (+0.66, fdr 1e-05), [[TTBK2]] (+0.64, fdr 7e-06); moves opposite to [[PDCD6]] (-0.60, fdr 1e-05), [[PIGG]] (-0.55, fdr 1e-05), [[NSUN2]] (-0.54, fdr 1e-05).
> It is in [[Module 222]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RETREG1]] → it (grade B ⚠); 5 go from it, the strongest it → [[SUV39H2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +11.2 | 4e-26 | 34/44 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +10.6 | 7e-24 | 29/44 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +10.4 | 4e-23 | 33/44 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +9.9 | 4e-21 | 32/44 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +9.5 | 4e-19 | 27/44 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +8.6 | 6e-16 | 29/44 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +7.6 | 3e-12 | 27/44 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.45×** | +7.2 | 4e-11 | 31/44 (A498, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +6.7 | 1e-09 | 24/44 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +5.7 | 6e-07 | 26/44 (A498, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +5.6 | 1e-06 | 21/44 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 2e-06 | 22/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.4 | 4e-06 | 20/44 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.2 | 7e-06 | 21/40 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.9 | 5e-05 | 19/44 (A498, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 2e-04 | 12/44 (SW480, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9069.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.368×** | -8.1 | 4e-13 | 28/44 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.382×** | -7.8 | 2e-12 | 30/44 (HEC-1-A, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -5.2 | 4e-05 | 21/44 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.785×** | -3.6 | 0.046 | 13/44 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.706×** | -3.5 | 0.046 | 6/44 (SW480, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -3.4 | 0.066 | 4/45 (RPMI-7951, RKO, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.820× | -3.1 | 0.17 | 5/44 (NCI-H460, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.82 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.62× (z +9.8) | — |
| [[A-427 (line)]] | wt | 35.6 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0531× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 17.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 39.4 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -9.9) ⚠ cell-cycle shift, explains ~79% of this change |
| [[C-33 A (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 6.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +8.6) | — |
| [[LoVo (line)]] | wt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 7.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +8.5) | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0441× (z -8.5) |
| [[A-172 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND5B]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[PHIP]] | +0.66 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TTBK2]] | +0.64 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[BEND7]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ITSN2]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PFDN4]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[RALGAPA1]] | +0.55 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[TUT4]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[GABARAPL1]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[DTNB]] | +0.53 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TBL1X]] | +0.52 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[CCDC126]] | +0.52 | +0.57 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[PIGG]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TBRG4]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PMPCA]] | -0.53 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[ARHGAP1]] | -0.52 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[B4GALT7]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[CCAR2]] | -0.51 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[URB1]] | -0.50 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[SLC35C1]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[APEX2]] | -0.50 | -0.50 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RETREG1]] | B | RETREG1 activity raises GKAP1's level | lines that do not express RETREG1 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without RETREG1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC02269, FILIP1, C19orf81 |
| [[DOCK3]] | B | DOCK3 activity raises GKAP1's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without DOCK3 | 0.069 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUV39H2]] | C | GKAP1 activity raises SUV39H2's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without GKAP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent; its own permutation p |
| [[TRIM37]] | C | GKAP1 activity raises TRIM37's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without GKAP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent; its own permutation p |
| [[WDSUB1]] | C | GKAP1 activity raises WDSUB1's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without GKAP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent; its own permutation p |
| [[SFXN2]] | C | GKAP1 activity raises SFXN2's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without GKAP1 | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent |
| [[IPO4]] | C | GKAP1 activity raises IPO4's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without GKAP1 | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 222]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, 12.7); signed map (8.0, -6.7). **Vector** length 95.5, 21.6% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -5.9 | -0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -5.4 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -8.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | G kinase anchoring protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:83,739,425-83,829,516 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GKAP42, FKSG21 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VSY0](https://www.uniprot.org/uniprotkb/Q5VSY0) (G kinase-anchoring protein 1):

> Regulates insulin-dependent IRS1 tyrosine phosphorylation in adipocytes by modulating the availability of IRS1 to IR tyrosine kinase. Its association with IRS1 is required for insulin-induced translocation of SLC2A4 to the cell membrane. Involved in TNF-induced impairment of insulin-dependent IRS1 tyrosine phosphorylation.

**Summary**, from NCBI Gene [80318](https://www.ncbi.nlm.nih.gov/gene/80318):

> This gene encodes a protein that is highly similar to the mouse cGMP-dependent protein kinase anchoring protein 42kDa. The mouse protein has been found to localize with the Golgi and recruit cGMP-dependent protein kinase I alpha to the Golgi in mouse testes. It is thought to play a role in germ cell development. Transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:17496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17496) · Entrez [80318](https://www.ncbi.nlm.nih.gov/gene/80318) · UniProt [Q5VSY0](https://www.uniprot.org/uniprotkb/Q5VSY0) · Ensembl [ENSG00000165113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165113)

## Data

Gene col 9069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9069); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9069]; `tensor/DDL_lfc|DDL_z.npy` [9069]; `embed/gene_vectors.npy` [9069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9069 or target_col == 9069). Every well: [[GKAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GKAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
