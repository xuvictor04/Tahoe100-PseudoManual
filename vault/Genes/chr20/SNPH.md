---
symbol: "SNPH"
type: "gene"
col: 2111
ensembl_id: "ENSG00000101298"
name: "syntaphilin"
location: "20p13"
module: 132
arm: "+"
pooled_cpm: 4.61
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# SNPH

*syntaphilin* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.68× (z +15.9, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.365× (z -11.4, q 1e-27, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP4K2]] (+0.62, fdr 3e-05), [[ADGRB2]] (+0.60, fdr 4e-05), [[DAGLA]] (+0.59, fdr 1e-05); moves opposite to [[CSNK1G1]] (-0.49, fdr 9e-05), [[FBXW9]] (-0.49, fdr 1e-03, ⚠ not reproduced), [[ACAD9]] (-0.48, fdr 4e-04), [[ELP4]] (-0.47, fdr 8e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM167A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[OSBPL7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.68×** | +15.9 | 0e+00 | 39/42 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.14×** | +13.0 | 2e-36 | 37/42 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.94×** | +12.3 | 2e-32 | 31/38 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.43×** | +10.1 | 6e-22 | 23/35 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.27×** | +9.4 | 1e-18 | 30/42 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.04×** | +8.3 | 9e-15 | 24/41 (HOP62, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +7.9 | 2e-13 | 22/42 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +7.6 | 2e-12 | 23/42 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +4.6 | 3e-04 | 14/42 (RKO, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.002 | 10/42 (A-172, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.63×** | +4.0 | 0.004 | 4/41 (SW480, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.037 | 7/42 (SW48, BT-474, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.049 | 5/42 (BT-474, SNU-423, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.071 | 4/41 (SNU-423, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.365×** | -11.4 | 1e-27 | 27/42 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.448×** | -9.1 | 3e-17 | 29/42 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.463×** | -8.7 | 4e-16 | 20/34 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.537×** | -7.1 | 2e-10 | 20/41 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.542×** | -6.9 | 4e-10 | 20/42 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.668×** | -4.6 | 5e-04 | 11/40 (H4, J82, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.499×** | -4.1 | 0.003 | 9/37 (RPMI-7951, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -3.9 | 0.006 | 13/38 (HS-578T, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.719×** | -3.7 | 0.012 | 11/41 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.721×** | -3.7 | 0.012 | 12/43 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.719×** | -3.6 | 0.017 | 12/41 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Resveratrol (drug)]] 5 µM |  | 0.828× | -3.0 | 0.12 | 10/43 (HCT15, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 9.30 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 3.47 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 120× (z +19.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Cabozantinib (S-malate) (drug)]] 0.05 µM 0.0468× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 6.10 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Menadione (drug)]] 0.05 µM 0.0704× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 4.39 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Docetaxel (drug)]] 0.05 µM 0.0964× (z -10.6) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 8.48 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 41.8× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 2.24 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 6.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0706× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 2.93 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0608× (z -8.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0890× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 3.11 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0625× (z -8.8) |
| [[SW480 (line)]] | alt | 2.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0964× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP4K2]] | +0.62 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ADGRB2]] | +0.60 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[DAGLA]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[RNF2]] | +0.58 | +0.52 / +0.40 | both halves | 4e-05 |  |
| [[TMOD2]] | +0.58 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ANO8]] | +0.57 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[ANXA6]] | +0.55 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[GRHL1]] | +0.53 | +0.37 / +0.60 | both halves | 9e-05 |  |
| [[KIF3A]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SPEG]] | +0.52 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[EHD3]] | +0.52 | +0.38 / +0.44 | both halves | 6e-05 |  |
| [[REEP2]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK1G1]] | -0.49 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[FBXW9]] | -0.49 | -0.18 / -0.49 | ⚠ not reproduced | 1e-03 |  |
| [[ACAD9]] | -0.48 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[RABL2A]] | -0.47 | -0.15 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[ELP4]] | -0.47 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[C1orf54]] | -0.47 | -0.24 / -0.53 | both halves | 5e-04 |  |
| [[PPP4R3B]] | -0.47 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[LINC00630]] | -0.46 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[PHC2-AS1]] | -0.46 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[ZFYVE26]] | -0.46 | -0.20 / -0.51 | both halves | 7e-04 |  |
| [[ASH1L]] | -0.46 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[SLC25A17]] | -0.46 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[LARP4B]] | -0.45 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[ANKHD1-EIF4EBP3]] | -0.45 | -0.22 / -0.32 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM167A]] | B | FAM167A activity raises SNPH's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without FAM167A | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[SYT7]] | B | SYT7 activity lowers SNPH's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.29× higher at baseline in the lines without SYT7 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMOD2]] | C | TMOD2 activity raises SNPH's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 2.97× lower at baseline in the lines without TMOD2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL7]] | B | SNPH activity raises OSBPL7's level | lines that do not express SNPH (5) vs lines expressing it (45) | 2.19× lower at baseline in the lines without SNPH | 0.098 | ⚠ within organs, on part of the lines; also absent: E2F7, SPDL1, TMOD2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.7, 30.2); signed map (-37.3, -17.3). **Vector** length 65.3, 10.0% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +15.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +12.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +13.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +8.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +10.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.4 | +4.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | +0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.1 | +1.0 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.1 | -3.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | syntaphilin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:1,266,280-1,309,328 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA314N13.5 |
| Matched by | ensembl_id |

**Function**, from UniProt [O15079](https://www.uniprot.org/uniprotkb/O15079) (Syntaphilin):

> Inhibits SNARE complex formation by absorbing free STX1A.

**Summary**, from NCBI Gene [9751](https://www.ncbi.nlm.nih.gov/gene/9751):

> Syntaxin-1, synaptobrevin/VAMP, and SNAP25 interact to form the SNARE complex, which is required for synaptic vesicle docking and fusion. The protein encoded by this gene is membrane-associated and inhibits SNARE complex formation by binding free syntaxin-1. Expression of this gene appears to be brain-specific. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:15931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15931) · Entrez [9751](https://www.ncbi.nlm.nih.gov/gene/9751) · UniProt [O15079](https://www.uniprot.org/uniprotkb/O15079) · Ensembl [ENSG00000101298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101298)

## Data

Gene col 2111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2111); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2111]; `tensor/DDL_lfc|DDL_z.npy` [2111]; `embed/gene_vectors.npy` [2111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2111 or target_col == 2111). Every well: [[SNPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
