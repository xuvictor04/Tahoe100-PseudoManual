---
symbol: "TMEM156"
type: "gene"
col: 4302
ensembl_id: "ENSG00000121895"
name: "transmembrane protein 156"
location: "4p14"
module: 147
arm: "+"
pooled_cpm: 36.77
n_lines_expressing: 24
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 8
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 11
direction_downstream: 27
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# TMEM156

*transmembrane protein 156* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.13× (z +11.7, q 9e-29, up in 7 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.520× (z -6.6, q 3e-08, down in 12 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02454]] (+0.65, fdr 7e-06), [[LINC00941]] (+0.64, fdr 7e-06), [[ARHGAP31]] (+0.63, fdr 7e-06); moves opposite to [[NPEPPS]] (-0.49, fdr 6e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 27 go from it, the strongest it → [[CFAP58]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +11.7 | 9e-29 | 7/22 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +10.3 | 2e-22 | 7/20 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +9.0 | 5e-17 | 6/15 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +8.0 | 3e-13 | 14/22 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +6.8 | 1e-09 | 5/18 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.4 | 6e-06 | 13/22 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.002 | 3/22 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.63×** | +3.8 | 0.010 | 5/22 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.020 | 2/20 (NCI-H460, CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.026 | 6/22 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.098 | 3/22 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 0.05 µM |  | 1.32× | +3.0 | 0.12 | 6/22 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.520×** | -6.6 | 3e-08 | 12/22 (RKO, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.606×** | -6.4 | 4e-08 | 15/22 (RKO, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.566×** | -6.3 | 5e-08 | 18/22 (RKO, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.573×** | -6.0 | 2e-07 | 18/22 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.638×** | -6.0 | 2e-07 | 16/22 (RKO, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.575×** | -6.0 | 2e-07 | 18/22 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.563×** | -6.0 | 2e-07 | 12/21 (RKO, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.590×** | -5.7 | 8e-07 | 18/22 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.694×** | -5.5 | 2e-06 | 13/22 (RKO, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.638×** | -5.3 | 8e-06 | 18/22 (RKO, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.647×** | -4.7 | 1e-04 | 13/21 (RKO, H4, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.657×** | -4.6 | 3e-04 | 14/22 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.450×** | -4.5 | 3e-04 | 15/20 (NCI-H1792, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -4.4 | 5e-04 | 4/22 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.757×** | -4.2 | 0.001 | 13/22 (RKO, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.700×** | -3.9 | 0.004 | 16/22 (RKO, A549, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.523×** | -3.7 | 0.008 | 12/22 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 214 | 0 | 26 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 54.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0818× (z -21.1) |
| [[SW 900 (line)]] | alt | 719 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 61.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 35.6 | 0 | 5 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.518× (z -9.9) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.224× (z -8.9) |
| [[PANC-1 (line)]] | alt | 46.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -14.6) |
| [[A549 (line)]] | wt | 154 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 79.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 48.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 10.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.44× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 64.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -9.1) |
| [[H4 (line)]] | wt | 37.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0706× (z -11.6) |
| [[HOP62 (line)]] | alt | 14.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.86× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -11.7) |
| [[NCI-H661 (line)]] | alt | 30.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0334× (z -9.8) |
| [[A-172 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.80 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.74 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02454]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ARHGAP31]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ELK3]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[B4GALT6]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[HMGA2]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LNCOG]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[NT5E]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ADGRL4]] | +0.60 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[ERRFI1-DT]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[LTBP2]] | +0.58 | +0.46 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPEPPS]] | -0.49 | -0.39 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TMEM156's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 4.8% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds |
| [[MIR100HG]] | B | MIR100HG activity raises TMEM156's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 3.13× lower at baseline in the lines without MIR100HG | 0.025 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[HMGA2]] | B | HMGA2 activity raises TMEM156's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 3.90× lower at baseline in the lines without HMGA2 | 0.049 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[TOP2A]] | B | TOP2A activity lowers TMEM156's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC02454]] | B | LINC02454 activity raises TMEM156's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 3.42× lower at baseline in the lines without LINC02454 | 0.071 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[CTSL]] | B | CTSL activity raises TMEM156's level | lines that do not express CTSL (9) vs lines expressing it (41) | 4.25× lower at baseline in the lines without CTSL | 0.073 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[MSRB3]] | B | MSRB3 activity raises TMEM156's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without MSRB3 | 0.098 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[BCL2A1]] | C | BCL2A1 activity raises TMEM156's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 5.41× lower at baseline in the lines without BCL2A1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; co-absent with the target |
| [[IL31RA]] | C | IL31RA activity raises TMEM156's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 4.73× lower at baseline in the lines without IL31RA | 0.017 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1; co-absent with the target |
| [[HTR7]] | C | HTR7 activity raises TMEM156's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 3.73× lower at baseline in the lines without HTR7 | 0.058 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2; co-absent with the target |
| [[STC1]] | C | STC1 activity raises TMEM156's level | lines that do not express STC1 (24) vs lines expressing it (26) | 3.37× lower at baseline in the lines without STC1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 21, C 6. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFAP58]] | B | TMEM156 activity raises CFAP58's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.63× lower at baseline in the lines without TMEM156 | 0.009 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[MAP4K4]] | B | TMEM156 activity raises MAP4K4's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.92× lower at baseline in the lines without TMEM156 | 0.021 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[ANTXR2]] | B | TMEM156 activity raises ANTXR2's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without TMEM156 | 0.022 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[ACTN1]] | B | TMEM156 activity raises ACTN1's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.22× lower at baseline in the lines without TMEM156 | 0.023 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[ITPRIP]] | B | TMEM156 activity raises ITPRIP's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without TMEM156 | 0.029 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[MIR100HG]] | B | TMEM156 activity raises MIR100HG's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without TMEM156 | 0.034 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[HMGA2]] | B | TMEM156 activity raises HMGA2's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 2.58× lower at baseline in the lines without TMEM156 | 0.041 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[DDAH1]] | B | TMEM156 activity raises DDAH1's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.33× lower at baseline in the lines without TMEM156 | 0.045 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[DNMBP]] | B | TMEM156 activity raises DNMBP's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.45× lower at baseline in the lines without TMEM156 | 0.050 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[ARHGAP31]] | B | TMEM156 activity raises ARHGAP31's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without TMEM156 | 0.055 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[RPSAP52]] | B | TMEM156 activity raises RPSAP52's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 2.03× lower at baseline in the lines without TMEM156 | 0.062 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[ZFPM2-AS1]] | B | TMEM156 activity raises ZFPM2-AS1's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without TMEM156 | 0.063 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.9, 8.5); signed map (10.6, 46.7). **Vector** length 86.7, 25.9% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.3 | +1.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.6 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.1 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.6 | -5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 156 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:38,966,744-39,032,922 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23235 |
| Matched by | ensembl_id |

UniProt [Q8N614](https://www.uniprot.org/uniprotkb/Q8N614) carries no function annotation.

**Summary**, from NCBI Gene [80008](https://www.ncbi.nlm.nih.gov/gene/80008):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26260) · Entrez [80008](https://www.ncbi.nlm.nih.gov/gene/80008) · UniProt [Q8N614](https://www.uniprot.org/uniprotkb/Q8N614) · Ensembl [ENSG00000121895](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121895)

## Data

Gene col 4302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4302); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4302]; `tensor/DDL_lfc|DDL_z.npy` [4302]; `embed/gene_vectors.npy` [4302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4302 or target_col == 4302). Every well: [[TMEM156 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM156.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
