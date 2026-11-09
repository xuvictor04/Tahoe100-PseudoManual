---
symbol: "FOXL1"
type: "gene"
col: 10740
ensembl_id: "ENSG00000176678"
name: "forkhead box L1"
location: "16q24.1"
module: 147
arm: "+"
pooled_cpm: 8.35
n_lines_expressing: 25
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# FOXL1

*forkhead box L1* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +10.2, q 1e-21, up in 6 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.558× (z -5.8, q 5e-06, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLMP]] (+0.68, fdr 7e-06), [[HMGA2]] (+0.66, fdr 7e-06), [[AKAP12]] (+0.66, fdr 7e-06); moves opposite to [[EPB41]] (-0.59, fdr 1e-05), [[PSME1]] (-0.50, fdr 6e-05), [[CLN3]] (-0.49, fdr 4e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → [[ITGA5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +10.2 | 1e-21 | 6/22 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +8.9 | 1e-16 | 2/14 (NCI-H1792, J82) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +8.5 | 4e-15 | 0/13 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +8.3 | 2e-14 | 3/16 (NCI-H1792, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.4 | 0.001 | 9/22 (NCI-H1792, HOP62, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.55×** | +4.0 | 0.007 | 12/22 (NCI-H1792, A-172, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.53×** | +3.9 | 0.009 | 13/22 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.51×** | +3.7 | 0.013 | 7/22 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.7 | 0.015 | 7/21 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.023 | 12/22 (NCI-H1792, A-172, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.3 | 0.058 | 0/19 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Econazole (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.077 | 10/22 (NCI-H1792, HOP62, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.558×** | -5.8 | 5e-06 | 14/22 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.616×** | -5.4 | 2e-05 | 16/22 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.323×** | -5.2 | 4e-05 | 15/20 (HOP62, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.641×** | -5.0 | 1e-04 | 12/22 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.567×** | -4.8 | 2e-04 | 9/22 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.599×** | -4.7 | 3e-04 | 16/22 (HOP62, AsPC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -4.3 | 0.001 | 12/21 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.650×** | -3.9 | 0.006 | 10/22 (HOP62, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -3.8 | 0.008 | 11/22 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.438×** | -3.8 | 0.008 | 5/22 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.666×** | -3.7 | 0.012 | 14/22 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.666×** | -3.6 | 0.017 | 14/21 (AsPC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.676×** | -3.5 | 0.018 | 12/22 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.785×** | -3.4 | 0.024 | 16/22 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.688×** | -3.4 | 0.024 | 11/22 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.769×** | -3.3 | 0.030 | 7/22 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 45.1 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.0818× (z -14.3) |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.125× (z -12.1) |
| [[HOP62 (line)]] | alt | 25.8 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.101× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 50.2 | 1 | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.42× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.127× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 37.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0575× (z -18.6) |
| [[A-172 (line)]] | wt | 13.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0446× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0889× (z -10.6) |
| [[Hs 766T (line)]] | wt | 24.0 | 0 | 1 | — | [[Binimetinib (drug)]] 0.05 µM 0.289× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 2.25 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0370× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 5.32 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLMP]] | +0.68 | +0.73 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[HMGA2]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[AKAP12]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[TOP1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MAP4K4]] | +0.63 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[LINC00941]] | +0.62 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[SH3RF3]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CAPRIN2]] | +0.62 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[FOXC2]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 | same gene group; STRING 563; ⚠ same locus (6.6 kb, same strand: neighbours can correlate without regulation) |
| [[ABLIM3]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ELK3]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[IL1RL1]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[MCL1]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PSME1]] | -0.50 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[CLN3]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[GPRC5B]] | -0.48 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[CD5L]] | -0.47 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[NR6A1]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[C4orf19]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TPD52]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[GBP2]] | -0.45 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[BCL2L14]] | -0.45 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[EMC2]] | -0.44 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[TMPRSS3]] | -0.44 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises FOXL1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FOXC2]] | C | FOXC2 activity raises FOXL1's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 3.34× lower at baseline in the lines without FOXC2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[CLMP]] | C | CLMP activity raises FOXL1's level | lines that do not express CLMP (25) vs lines expressing it (25) | 2.92× lower at baseline in the lines without CLMP | 0.021 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10; co-absent with the target |
| [[FLI1]] | C | FLI1 activity raises FOXL1's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 3.05× lower at baseline in the lines without FLI1 | 0.051 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615; co-absent with the target |
| [[GAB3]] | C | GAB3 activity raises FOXL1's level | lines that do not express GAB3 (17) vs lines expressing it (33) | 2.78× lower at baseline in the lines without GAB3 | 0.068 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, SOGA3; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA5]] | B | FOXL1 activity raises ITGA5's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 4.17× lower at baseline in the lines without FOXL1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A |
| [[PRDM1]] | B | FOXL1 activity raises PRDM1's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without FOXL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A |
| [[ABLIM3]] | B | FOXL1 activity raises ABLIM3's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 3.06× lower at baseline in the lines without FOXL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A |
| [[CD59]] | B | FOXL1 activity raises CD59's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without FOXL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A |
| [[C11orf91]] | B | FOXL1 activity raises C11orf91's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without FOXL1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A |
| cells under [[9-ING-41 (drug)]] 0.05 µM | B | FOXL1 activity raises the cells' numbers under 9-ING-41 0.05 µM (protects the cells) | lines that do not express FOXL1 (25) vs lines expressing it (23) | the lines without FOXL1: 0.84× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A |
| [[CLMP]] | C | FOXL1 activity raises CLMP's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 6.21× lower at baseline in the lines without FOXL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A; co-absent with the target |
| [[FOXC2]] | C | FOXL1 activity raises FOXC2's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 3.24× lower at baseline in the lines without FOXL1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A; co-absent with the target |
| [[JCAD]] | C | FOXL1 activity raises JCAD's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 3.38× lower at baseline in the lines without FOXL1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A; co-absent with the target |
| [[THBD]] | C | FOXL1 activity raises THBD's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 2.23× lower at baseline in the lines without FOXL1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A; co-absent with the target |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, 12.3); signed map (11.3, 46.2). **Vector** length 80.7, 23.1% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +4.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.2 | +2.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.7 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:86,576,368-86,583,478 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FREAC7, FKH6; previously FKHL11 |
| Gene groups (HGNC) | Forkhead boxes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12952](https://www.uniprot.org/uniprotkb/Q12952) (Forkhead box protein L1):

> Transcription factor required for proper proliferation and differentiation in the gastrointestinal epithelium. Target gene of the hedgehog (Hh) signaling pathway via GLI2 and GLI3 transcription factors (By similarity).

**Summary**, from NCBI Gene [2300](https://www.ncbi.nlm.nih.gov/gene/2300):

> This gene encodes a member of the forkhead/winged helix-box (FOX) family of transcription factors. FOX transcription factors are characterized by a distinct DNA-binding forkhead domain and play critical roles in the regulation of multiple processes including metabolism, cell proliferation and gene expression during ontogenesis. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:3817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3817) · Entrez [2300](https://www.ncbi.nlm.nih.gov/gene/2300) · UniProt [Q12952](https://www.uniprot.org/uniprotkb/Q12952) · Ensembl [ENSG00000176678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176678)

## Data

Gene col 10740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10740); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10740]; `tensor/DDL_lfc|DDL_z.npy` [10740]; `embed/gene_vectors.npy` [10740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10740 or target_col == 10740). Every well: [[FOXL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
