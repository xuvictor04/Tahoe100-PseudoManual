---
symbol: "ETHE1"
type: "gene"
col: 2661
ensembl_id: "ENSG00000105755"
name: "ETHE1 persulfide dioxygenase"
location: "19q13.31"
module: 154
arm: "+"
pooled_cpm: 15.85
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# ETHE1

*ETHE1 persulfide dioxygenase* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.38× (z +9.8, q 8e-20, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.446× (z -9.1, q 6e-17, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIB1]] (+0.69, fdr 1e-05), [[MPG]] (+0.66, fdr 1e-05), [[CARD19]] (+0.66, fdr 2e-05); moves opposite to [[DDX6]] (-0.72, fdr 1e-05), [[RCN1]] (-0.70, fdr 7e-06), [[CRPPA]] (-0.68, fdr 3e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TNIK]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.38×** | +9.8 | 8e-20 | 40/47 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +7.8 | 2e-12 | 36/48 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +7.6 | 7e-12 | 35/48 (HEC-1-A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.93×** | +7.4 | 2e-11 | 34/43 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +6.8 | 9e-10 | 33/48 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.82×** | +6.8 | 1e-09 | 23/36 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.0 | 1e-07 | 29/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.60×** | +5.1 | 2e-05 | 15/29 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.43×** | +3.8 | 0.011 | 10/31 (RPMI-7951, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.022 | 14/47 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.5 | 0.022 | 13/45 (HEC-1-A, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.11 | 14/46 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.446×** | -9.1 | 6e-17 | 37/48 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.532×** | -7.1 | 4e-10 | 35/47 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.558×** | -6.6 | 1e-08 | 30/47 (SW 900, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.601×** | -5.7 | 1e-06 | 23/45 (HCT15, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.628×** | -5.2 | 2e-05 | 27/46 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.651×** | -4.8 | 1e-04 | 25/48 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.665×** | -4.0 | 0.005 | 21/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -4.0 | 0.005 | 20/48 (HOP62, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -3.6 | 0.020 | 19/43 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.712×** | -3.5 | 0.024 | 18/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.737×** | -3.4 | 0.032 | 13/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.542×** | -3.4 | 0.034 | 17/47 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.753×** | -3.2 | 0.064 | 15/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.756×** | -3.1 | 0.069 | 18/47 (A549, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.818×** | -3.1 | 0.069 | 14/48 (NCI-H460, AN3 CA, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -3.0 | 0.090 | 10/47 (C32, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0751× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -10.9) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIB1]] | +0.69 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MPG]] | +0.66 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CARD19]] | +0.66 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[FAM89B]] | +0.66 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[EML2]] | +0.65 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[MPST]] | +0.65 | +0.46 / +0.52 | both halves | 2e-05 | pathway: Degradation of cysteine and homocysteine; STRING 977 |
| [[STN1]] | +0.65 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TMEM191A-1]] | +0.64 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[CDKN2D]] | +0.64 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[FCHO1]] | +0.63 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[BMERB1]] | +0.63 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[TMEM256]] | +0.62 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX6]] | -0.72 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[RCN1]] | -0.70 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[CRPPA]] | -0.68 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SUCLG2-DT]] | -0.67 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ZNF532]] | -0.65 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[SCRN1]] | -0.65 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.65 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.64 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[ARFGAP2]] | -0.64 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ZMYND11]] | -0.64 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.63 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[ZFX]] | -0.63 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNIK]] | B | TNIK activity raises ETHE1's level | lines that do not express TNIK (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without TNIK | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ETHE1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ETHE1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.3, 3.3); signed map (-5.0, 46.0). **Vector** length 87.1, 19.9% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +7.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.5 | +3.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +1.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ETHE1 persulfide dioxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,506,719-43,527,230 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YF13H12, HSCO |
| Gene groups (HGNC) | MBL domain containing glyoxalase 2 subfamily; Oxygenases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 4 pathways, smallest: Sulfide oxidation to sulfate; Degradation of cysteine and homocysteine; Sulfur amino acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O95571](https://www.uniprot.org/uniprotkb/O95571) (Persulfide dioxygenase ETHE1, mitochondrial):

> Sulfur dioxygenase that plays an essential role in hydrogen sulfide catabolism in the mitochondrial matrix. Hydrogen sulfide (H(2)S) is first oxidized by SQRDL, giving rise to cysteine persulfide residues. ETHE1 consumes molecular oxygen to catalyze the oxidation of the persulfide, once it has been transferred to a thiophilic acceptor, such as glutathione (R-SSH). Plays an important role in metabolic homeostasis in mitochondria by metabolizing hydrogen sulfide and preventing the accumulation of …

**Summary**, from NCBI Gene [23474](https://www.ncbi.nlm.nih.gov/gene/23474):

> This gene encodes a member of the metallo beta-lactamase family of iron-containing proteins involved in the mitochondrial sulfide oxidation pathway. The encoded protein catalyzes the oxidation of a persulfide substrate to sulfite. Certain mutations in this gene cause ethylmalonic encephalopathy, an infantile metabolic disorder affecting the brain, gastrointestinal tract and peripheral vessels. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by …

**Accessions** — [HGNC:23287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23287) · Entrez [23474](https://www.ncbi.nlm.nih.gov/gene/23474) · UniProt [O95571](https://www.uniprot.org/uniprotkb/O95571) · Ensembl [ENSG00000105755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105755)

## Data

Gene col 2661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2661); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2661]; `tensor/DDL_lfc|DDL_z.npy` [2661]; `embed/gene_vectors.npy` [2661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2661 or target_col == 2661). Every well: [[ETHE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETHE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
