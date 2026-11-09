---
symbol: "CALB2"
type: "gene"
col: 10214
ensembl_id: "ENSG00000172137"
name: "calbindin 2"
location: "16q22.2"
module: 34
arm: "+"
pooled_cpm: 17.97
n_lines_expressing: 27
n_dd_up: 18
n_dd_down: 31
n_dd_up_clean: 9
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CALB2

*calbindin 2* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.75× (z +14.4, q 2e-44, up in 14 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.533× (z -6.3, q 1e-07, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C7orf57]] (+0.66, fdr 8e-06), [[MMP1]] (+0.66, fdr 7e-06), [[CDCP1]] (+0.65, fdr 1e-05); moves opposite to [[NNMT]] (-0.51, fdr 8e-05), [[COPS5]] (-0.50, fdr 2e-05), [[RNF115]] (-0.50, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 11 go from it, the strongest it → [[ITPR3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +14.4 | 2e-44 | 14/24 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.68×** | +14.0 | 2e-42 | 16/25 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.57×** | +12.8 | 2e-35 | 14/22 (J82, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.63×** | +9.4 | 1e-18 | 12/14 (NCI-H1792, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.70×** | +9.3 | 2e-18 | 13/19 (J82, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.49×** | +9.2 | 3e-18 | 14/25 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.39×** | +8.8 | 1e-16 | 14/24 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.00×** | +7.0 | 2e-10 | 10/25 (J82, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.94×** | +6.7 | 1e-09 | 11/24 (J82, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +5.7 | 8e-07 | 11/25 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +4.9 | 6e-05 | 12/23 (KATO III, LS 180, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.53×** | +4.3 | 9e-04 | 8/23 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +4.0 | 0.003 | 6/20 (KATO III, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.43×** | +3.6 | 0.013 | 5/20 (J82, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +3.3 | 0.043 | 5/24 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.075 | 11/24 (KATO III, NCI-H460, …) | all doses, flat | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.079 | 10/25 (J82, SNU-423, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10214.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.533×** | -6.3 | 1e-07 | 14/24 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.649×** | -6.2 | 2e-07 | 18/25 (Panc 03.27, RKO, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.689×** | -5.2 | 3e-05 | 14/25 (LS 180, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.562×** | -5.2 | 3e-05 | 13/25 (MIA PaCa-2, LS 180, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.637×** | -4.5 | 6e-04 | 15/23 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.642×** | -4.5 | 7e-04 | 9/23 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.623×** | -4.4 | 7e-04 | 9/25 (LS 180, RKO, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.646×** | -4.4 | 7e-04 | 13/24 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.643×** | -4.3 | 0.001 | 11/23 (RKO, LS 180, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.748×** | -4.0 | 0.003 | 13/25 (MIA PaCa-2, LS 180, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.682×** | -3.9 | 0.006 | 14/25 (AsPC-1, SNU-423, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.461×** | -3.8 | 0.006 | 9/25 (MIA PaCa-2, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.666×** | -3.8 | 0.006 | 11/23 (SNU-423, SW 900, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.688×** | -3.8 | 0.006 | 10/23 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.695×** | -3.8 | 0.006 | 13/25 (MIA PaCa-2, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.704×** | -3.7 | 0.007 | 10/25 (MIA PaCa-2, LS 180, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 140 | 1 (1 ⚠) | 18 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Adagrasib (drug)]] 0.05 µM 0.286× (z -30.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.166× (z -18.5) |
| [[KATO III (line)]] | alt | 102 | 2 (2 ⚠) | 15 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.25× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -16.8) |
| [[LS 180 (line)]] | wt | 54.2 | 0 | 11 | — | [[Trametinib (drug)]] 5 µM 0.145× (z -12.9) |
| [[RKO (line)]] | wt | 103 | 0 | 7 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.130× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.88× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -11.3) |
| [[J82 (line)]] | alt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.72× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.49× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H460 (line)]] | wt | 6.58 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.15× (z +8.7) | [[Dexamethasone (drug)]] 5 µM 0.135× (z -8.7) |
| [[A-427 (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.135× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[AsPC-1 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.98× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.150× (z -13.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 52.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -16.1) |
| [[A-172 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C7orf57]] | +0.66 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[MMP1]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[LHX1-DT]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[S100A16]] | +0.64 | +0.63 / +0.49 | both halves | 1e-05 | same gene group |
| [[WSCD1]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PKIA]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SHB]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[LPCAT2]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 | same gene group |
| [[ITGA6]] | +0.62 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[HMGA1]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNMT]] | -0.51 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[COPS5]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RNF115]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers CALB2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[GALNT12]] | B | GALNT12 activity raises CALB2's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 3.01× lower at baseline in the lines without GALNT12 | 0.066 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[MAP2K1]] | B | MAP2K1 activity raises CALB2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[CD44]] | C | CD44 activity raises CALB2's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.49× lower at baseline in the lines without CD44 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPR3]] | B | CALB2 activity raises ITPR3's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 2.05× lower at baseline in the lines without CALB2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[PAQR5]] | B | CALB2 activity raises PAQR5's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without CALB2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[SH3GL3]] | B | CALB2 activity raises SH3GL3's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.97× lower at baseline in the lines without CALB2 | 0.027 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[PLAUR]] | B | CALB2 activity raises PLAUR's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without CALB2 | 0.042 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[EIF5A2]] | B | CALB2 activity raises EIF5A2's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without CALB2 | 0.046 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[HBEGF]] | B | CALB2 activity raises HBEGF's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without CALB2 | 0.060 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[FXYD5]] | B | CALB2 activity raises FXYD5's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without CALB2 | 0.067 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[DCBLD2]] | B | CALB2 activity raises DCBLD2's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.73× lower at baseline in the lines without CALB2 | 0.079 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[CXCL8]] | B | CALB2 activity raises CXCL8's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 2.80× lower at baseline in the lines without CALB2 | 0.081 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[S100A16]] | B | CALB2 activity raises S100A16's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without CALB2 | 0.096 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[CD44]] | C | CALB2 activity raises CD44's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 2.91× lower at baseline in the lines without CALB2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, -0.2); signed map (1.9, 46.2). **Vector** length 83.0, 21.2% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +7.0 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +6.6 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +4.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.9 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | calbindin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:71,358,713-71,390,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAL2 |
| Gene groups (HGNC) | EF-hand domain containing |
| Hallmark sets | APICAL_JUNCTION, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [P22676](https://www.uniprot.org/uniprotkb/P22676) (Calretinin):

> Calcium-binding protein involved in calcium homeostasis and signal transduction. It plays a critical role in buffering intracellular calcium levels and modulating calcium-dependent signaling pathways. Predominantly expressed in specific neuronal populations, influences synaptic plasticity and neuronal excitability, contributing to learning and memory (By similarity). During embryonic development, it facilitates neuronal differentiation and maturation (By similarity).

**Summary**, from NCBI Gene [794](https://www.ncbi.nlm.nih.gov/gene/794):

> This gene encodes an intracellular calcium-binding protein belonging to the troponin C superfamily. Members of this protein family have six EF-hand domains which bind calcium. This protein plays a role in diverse cellular functions, including message targeting and intracellular calcium buffering. It also functions as a modulator of neuronal excitability, and is a diagnostic marker for some human diseases, including Hirschsprung disease and some cancers. Alternative splicing results in multiple …

**Accessions** — [HGNC:1435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1435) · Entrez [794](https://www.ncbi.nlm.nih.gov/gene/794) · UniProt [P22676](https://www.uniprot.org/uniprotkb/P22676) · Ensembl [ENSG00000172137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172137)

## Data

Gene col 10214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10214); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10214]; `tensor/DDL_lfc|DDL_z.npy` [10214]; `embed/gene_vectors.npy` [10214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10214 or target_col == 10214). Every well: [[CALB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
