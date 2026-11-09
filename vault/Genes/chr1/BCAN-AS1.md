---
symbol: "BCAN-AS1"
type: "gene"
col: 15708
ensembl_id: "ENSG00000272068"
name: "BCAN antisense RNA 1"
location: "1q23.1"
module: 158
arm: "+"
pooled_cpm: 7.7
n_lines_expressing: 39
n_dd_up: 19
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 8
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# BCAN-AS1

*BCAN antisense RNA 1* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.04× (z +6.7, q 7e-09, up in 22 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.371× (z -9.3, q 1e-17, down in 27 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAN-AS2]] (+0.74, fdr 7e-06, ⚠ same locus), [[LINC00460]] (+0.67, fdr 7e-06), [[FOSL1]] (+0.66, fdr 1e-05), [[LINC03042]] (+0.65, fdr 7e-06); moves opposite to [[ABCB10]] (-0.54, fdr 1e-05), [[GLB1]] (-0.53, fdr 1e-05), [[FHIP2A]] (-0.53, fdr 1e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PPP1R1C]] → it (grade B ⚠); 8 go from it, the strongest it → [[PMEPA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +6.7 | 7e-09 | 22/35 (HT-29, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.03×** | +6.6 | 7e-09 | 13/24 (NCI-H1573, NCI-H460, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +6.6 | 7e-09 | 22/36 (SW480, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +5.8 | 1e-06 | 22/35 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.83×** | +5.4 | 6e-06 | 7/10 (A-172, NCI-H460, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +4.9 | 9e-05 | 17/37 (A-172, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.71×** | +4.6 | 3e-04 | 8/19 (A-172, NCI-H2030, …) | all doses, flat | composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.4 | 8e-04 | 15/33 (NCI-H2030, A-172, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.58×** | +4.3 | 0.001 | 12/36 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.37×** | +4.2 | 0.002 | 16/32 (SK-MEL-2, C32, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +3.5 | 0.022 | 16/35 (A-172, A498, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.034 | 10/37 (SW480, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.036 | 13/32 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.94×** | +3.3 | 0.045 | 8/28 (SW480, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.40×** | +3.2 | 0.057 | 8/36 (A498, A-172, …) | rises with dose | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.063 | 6/32 (SW480, NCI-H23, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +3.0 | 0.090 | 1/30 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.090 | 9/37 (SK-MEL-2, A549, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.37×** | +2.9 | 0.100 | 5/35 (RPMI-7951, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15708.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.371×** | -9.3 | 1e-17 | 27/37 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.491×** | -6.6 | 9e-09 | 23/34 (SW480, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.524×** | -6.0 | 3e-07 | 20/35 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.526×** | -6.0 | 3e-07 | 26/35 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.331×** | -5.4 | 8e-06 | 18/31 (HCT15, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -5.0 | 5e-05 | 18/32 (LoVo, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.594×** | -4.9 | 1e-04 | 15/37 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.683×** | -4.5 | 5e-04 | 17/34 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.649×** | -4.2 | 0.002 | 12/36 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.631×** | -4.1 | 0.002 | 18/34 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.646×** | -4.1 | 0.002 | 13/36 (C32, SW480, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -3.8 | 0.007 | 16/34 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.647×** | -3.8 | 0.008 | 11/36 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.698×** | -3.7 | 0.009 | 12/36 (SW480, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.775×** | -3.3 | 0.030 | 8/37 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.715×** | -3.1 | 0.060 | 4/37 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.541×** | -3.0 | 0.081 | 12/36 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.9 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.192× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.221× (z -12.4) |
| [[LS 180 (line)]] | wt | 7.03 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0849× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.491× (z -11.2) ⚠ position not correctable · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.145× (z -9.2) |
| [[A-172 (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.29× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0990× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -14.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HT-29 (line)]] | alt | 15.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.97× (z +9.8) | — |
| [[LoVo (line)]] | wt | 7.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0803× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 7.75 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0612× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +8.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAN-AS2]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 | same gene group; ⚠ same locus (5.5 kb, same strand: neighbours can correlate without regulation) |
| [[LINC00460]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.66 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LINC03042]] | +0.65 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ZNF697]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[EGR3]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ERCC1]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ZFPM2-AS1]] | +0.61 | +0.51 / +0.68 | both halves | 1e-05 | same gene group |
| [[IL19]] | +0.61 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CD163L1]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[GOLT1A]] | +0.60 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[EGR1]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[BACH1]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB10]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[GLB1]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[FHIP2A]] | -0.53 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[MFSD14A]] | -0.52 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[BMPR1A]] | -0.52 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[NCOA2]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[RNPEP]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[USF1]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[NUP133]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TMEM94]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R1C]] | B | PPP1R1C activity raises BCAN-AS1's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 2.19× lower at baseline in the lines without PPP1R1C | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[DUSP5]] | B | DUSP5 activity raises BCAN-AS1's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.39× lower at baseline in the lines without DUSP5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises BCAN-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[ZG16B]] | B | ZG16B activity raises BCAN-AS1's level | lines that do not express ZG16B (17) vs lines expressing it (33) | 1.73× lower at baseline in the lines without ZG16B | 0.084 | ⚠ within organs, on part of the lines; also absent: KRT19, CYBA, MIR4713HG; maybe low, not absent |
| [[LUCAT1]] | B | LUCAT1 activity raises BCAN-AS1's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without LUCAT1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[SHH]] | B | SHH activity raises BCAN-AS1's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.85× lower at baseline in the lines without SHH | 0.095 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[LIF]] | B | LIF activity raises BCAN-AS1's level | lines that do not express LIF (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without LIF | 0.096 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[BCAN-AS2]] | C | BCAN-AS2 activity raises BCAN-AS1's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 3.60× lower at baseline in the lines without BCAN-AS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMEPA1]] | B | BCAN-AS1 activity raises PMEPA1's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 1.90× lower at baseline in the lines without BCAN-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[SVIL]] | B | BCAN-AS1 activity raises SVIL's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without BCAN-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[N4BP3]] | B | BCAN-AS1 activity raises N4BP3's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without BCAN-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[ZG16B]] | B | BCAN-AS1 activity raises ZG16B's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without BCAN-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[DIO3OS]] | B | BCAN-AS1 activity raises DIO3OS's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without BCAN-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[NTSR1]] | B | BCAN-AS1 activity raises NTSR1's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 3.31× lower at baseline in the lines without BCAN-AS1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[LIF]] | B | BCAN-AS1 activity raises LIF's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without BCAN-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[BCAN-AS2]] | C | BCAN-AS1 activity raises BCAN-AS2's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 3.61× lower at baseline in the lines without BCAN-AS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.5, 2.2); signed map (8.1, 39.8). **Vector** length 72.8, 15.9% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.6 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -9.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | BCAN antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q23.1 — chr1:156,637,783-156,641,004 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-284F21.9 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55233) · Entrez [105371453](https://www.ncbi.nlm.nih.gov/gene/105371453) · Ensembl [ENSG00000272068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272068)

## Data

Gene col 15708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15708); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15708]; `tensor/DDL_lfc|DDL_z.npy` [15708]; `embed/gene_vectors.npy` [15708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15708 or target_col == 15708). Every well: [[BCAN-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAN-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
