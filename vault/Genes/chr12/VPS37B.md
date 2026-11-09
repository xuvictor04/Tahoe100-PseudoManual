---
symbol: "VPS37B"
type: "gene"
col: 6339
ensembl_id: "ENSG00000139722"
name: "VPS37B subunit of ESCRT-I"
location: "12q24.31"
module: 141
arm: "+"
pooled_cpm: 100.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 20
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# VPS37B

*VPS37B subunit of ESCRT-I* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.16× (z +11.5, q 6e-28, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.488× (z -10.7, q 6e-24, down in 37 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.812× (z -4.4, q 0.002, down in 24 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA2]] (+0.65, fdr 7e-06), [[MAP2K3]] (+0.65, fdr 7e-06), [[EPHA2-AS1]] (+0.63, fdr 7e-06); moves opposite to [[SHPRH]] (-0.51, fdr 3e-05), [[RUFY2]] (-0.47, fdr 2e-04), [[MAP2K5]] (-0.47, fdr 5e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[F2RL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +11.5 | 6e-28 | 48/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +10.5 | 1e-23 | 44/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.83×** | +9.0 | 4e-17 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +7.6 | 3e-12 | 41/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.13×** | +5.9 | 4e-07 | 36/49 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +5.8 | 7e-07 | 36/48 (SW480, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.5 | 5e-04 | 21/38 (Panc 03.27, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.4 | 1e-03 | 31/48 (MIA PaCa-2, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.488×** | -10.7 | 6e-24 | 37/49 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -10.5 | 3e-23 | 39/43 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -4.5 | 0.001 | 5/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -4.4 | 0.002 | 24/49 (HT-29, COLO 205, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.783×** | -3.8 | 0.014 | 27/48 (SW48, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.656×** | -3.7 | 0.019 | 28/48 (MIA PaCa-2, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.842× | -3.6 | 0.023 | 18/48 (SW48, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.028 | 25/48 (MIA PaCa-2, SW48, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.804×** | -3.3 | 0.070 | 22/49 (SW48, NCI-H23, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.854× | -3.2 | 0.070 | 18/49 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.070 | 23/48 (SW48, NCI-H23, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.803×** | -3.1 | 0.078 | 22/49 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.827×** | -3.1 | 0.095 | 22/48 (HOP62, SW48, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 69.8 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.68× (z +21.0) | — |
| [[AsPC-1 (line)]] | alt | 132 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.85× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 189 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 98.1 | 2 (1 ⚠) | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.73× (z +12.5) | [[Adagrasib (drug)]] 0.05 µM 0.627× (z -15.5) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 69.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0992× (z -19.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 139 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 97.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -14.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 99.4 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.70× (z +12.1) | — |
| [[LoVo (line)]] | wt | 186 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 91.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 304 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -11.3) |
| [[LS 180 (line)]] | wt | 119 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -8.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 135 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +10.2) | — |
| [[C32 (line)]] | wt | 123 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -8.6) |
| [[Hs 766T (line)]] | wt | 55.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +9.9) | — |
| [[J82 (line)]] | alt | 55.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 62.1 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.30× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 82.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.07× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.1) | — |
| [[A549 (line)]] | wt | 99.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.171× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0826× (z -17.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 82.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +9.8) | — |
| [[KATO III (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 84.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.600× (z -16.1) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA2]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MAP2K3]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[EPHA2-AS1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[MIR222HG]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.59 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[DUSP5]] | +0.58 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[TMC6]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PRSS22]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SFT2D1]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[B3GNT3]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LINC00659]] | +0.54 | +0.59 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHPRH]] | -0.51 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[RUFY2]] | -0.47 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[MAP2K5]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ZNF451]] | -0.46 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[DHX29]] | -0.46 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2RL1]] | B | F2RL1 activity raises VPS37B's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without F2RL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises VPS37B's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 1.69× lower at baseline in the lines without TMPRSS4 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[PRSS22]] | B | PRSS22 activity raises VPS37B's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without PRSS22 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[LIPG]] | B | LIPG activity raises VPS37B's level | lines that do not express LIPG (25) vs lines expressing it (25) | 1.44× lower at baseline in the lines without LIPG | 0.011 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH |
| [[SHH]] | B | SHH activity raises VPS37B's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without SHH | 0.012 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[RNF39]] | B | RNF39 activity raises VPS37B's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without RNF39 | 0.020 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[GPR35]] | B | GPR35 activity raises VPS37B's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without GPR35 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[AFAP1L2]] | B | AFAP1L2 activity raises VPS37B's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without AFAP1L2 | 0.038 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[B3GNT3]] | B | B3GNT3 activity raises VPS37B's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 1.55× lower at baseline in the lines without B3GNT3 | 0.039 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[LEMD1]] | B | LEMD1 activity raises VPS37B's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.41× lower at baseline in the lines without LEMD1 | 0.040 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[HS3ST1]] | B | HS3ST1 activity raises VPS37B's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 1.50× lower at baseline in the lines without HS3ST1 | 0.048 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[PADI1]] | B | PADI1 activity raises VPS37B's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 1.47× lower at baseline in the lines without PADI1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.6, 51.1); signed map (5.4, 39.6). **Vector** length 94.4, 28.1% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +1.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.1 | -0.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -1.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | VPS37B subunit of ESCRT-I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,865,330-122,896,127 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12750 |
| Gene groups (HGNC) | ESCRT-I |
| Hallmark sets | DNA_REPAIR |
| Reactome | 15 pathways, smallest: Membrane binding and targetting of GAG proteins; Synthesis And Processing Of GAG, GAGPOL Polyproteins; Assembly Of The HIV Virion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9H4](https://www.uniprot.org/uniprotkb/Q9H9H4) (Vacuolar protein sorting-associated protein 37B):

> Component of the ESCRT-I complex, a regulator of vesicular trafficking process. Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies. May be involved in cell growth and differentiation.

**Summary**, from NCBI Gene [79720](https://www.ncbi.nlm.nih.gov/gene/79720):

> Enables calcium-dependent protein binding activity. Predicted to be involved in protein targeting to membrane; protein targeting to vacuole; and ubiquitin-dependent protein catabolic process via the multivesicular body sorting pathway. Located in endosome membrane; midbody; and plasma membrane. Part of ESCRT I complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25754) · Entrez [79720](https://www.ncbi.nlm.nih.gov/gene/79720) · UniProt [Q9H9H4](https://www.uniprot.org/uniprotkb/Q9H9H4) · Ensembl [ENSG00000139722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139722)

## Data

Gene col 6339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6339); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6339]; `tensor/DDL_lfc|DDL_z.npy` [6339]; `embed/gene_vectors.npy` [6339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6339 or target_col == 6339). Every well: [[VPS37B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS37B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
