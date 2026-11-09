---
symbol: "ARHGEF18"
type: "gene"
col: 2513
ensembl_id: "ENSG00000104880"
name: "Rho/Rac guanine nucleotide exchange factor 18"
location: "19p13.2"
module: 160
arm: "+"
pooled_cpm: 74.0
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# ARHGEF18

*Rho/Rac guanine nucleotide exchange factor 18* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.76× (z +11.6, q 3e-28, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.678× (z -7.9, q 1e-12, down in 28 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.717× (z -6.5, q 1e-08, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHM1P1]] (+0.65, fdr 9e-06), [[PLEK2]] (+0.64, fdr 7e-06), [[STARD3]] (+0.62, fdr 1e-05); moves opposite to [[ZXDA]] (-0.55, fdr 3e-05), [[CFAP418]] (-0.54, fdr 2e-04), [[TAF9]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GRIN2D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +11.6 | 3e-28 | 38/48 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +11.0 | 1e-25 | 42/48 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +9.9 | 1e-20 | 40/48 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +6.9 | 8e-10 | 28/49 (SW480, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +4.8 | 2e-04 | 23/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +4.6 | 4e-04 | 25/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +4.0 | 0.006 | 21/48 (A549, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2513.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.678×** | -7.9 | 1e-12 | 28/49 (A-427, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -7.2 | 2e-10 | 29/45 (SW 900, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.717×** | -6.5 | 1e-08 | 34/48 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -6.4 | 2e-08 | 26/43 (LOX-IMVI, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.753×** | -5.8 | 9e-07 | 24/48 (AsPC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.801×** | -4.5 | 6e-04 | 28/48 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.807×** | -4.4 | 0.001 | 21/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.822×** | -4.0 | 0.004 | 22/48 (A-427, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.815×** | -4.0 | 0.004 | 22/47 (SNU-1, C32, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.858× | -3.7 | 0.011 | 20/48 (HepG2/C3A, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.868× | -3.5 | 0.024 | 19/49 (PANC-1, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.838× | -3.5 | 0.026 | 16/48 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.889× | -3.4 | 0.029 | 23/48 (A-427, LoVo, …) | two highest doses | composition shift |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.836× | -3.4 | 0.029 | 14/47 (HepG2/C3A, SW48, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.851× | -3.3 | 0.039 | 16/47 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.856× | -3.2 | 0.053 | 17/49 (HepG2/C3A, RKO, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.864× | -3.0 | 0.090 | 18/48 (HepG2/C3A, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.887× | -3.0 | 0.090 | 17/48 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 64.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.3) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.60× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 38.3 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.12× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.455× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 126 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.7) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -8.9) |
| [[SW480 (line)]] | alt | 81.0 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.28× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.474× (z -9.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -11.2) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 237 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -12.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -12.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -22.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 70.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.5) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.10× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 57.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -8.8) |
| [[C-33 A (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -11.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 52.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.371× (z -9.2) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 94.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -17.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 118 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.0) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[HCT15 (line)]] | alt | 109 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.172× (z -8.5) |
| [[KATO III (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 92.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.1) ⚠ cell-cycle shift, explains ~64% of this change |
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 69.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.3) ⚠ cell-cycle shift, explains ~64% of this change |
| [[Panc 03.27 (line)]] | alt | 80.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.432× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 87.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.6) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SHP-77 (line)]] | alt | 62.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.241× (z -9.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHM1P1]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[PLEK2]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 | same gene group |
| [[STARD3]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LUZP1]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TBC1D2]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[GBA2]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 | pathway: RAC1 GTPase cycle |
| [[FRMD8]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[MAPKAPK2]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 | pathway: Death Receptor Signaling |
| [[BCAR3]] | +0.57 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[DUSP5]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CFAP418]] | -0.54 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[TAF9]] | -0.53 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[DNAJC27]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TIA1]] | -0.52 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZNF280D]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ZNF630]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[JHY]] | -0.50 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[MATR3]] | -0.49 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ZFR]] | -0.49 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[NFYB]] | -0.49 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SPINK5]] | -0.48 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIN2D]] | B | GRIN2D activity raises ARHGEF18's level | lines that do not express GRIN2D (20) vs lines expressing it (30) | 1.38× lower at baseline in the lines without GRIN2D | 0.037 | ⚠ within organs, on part of the lines; also absent: MUC3A, TMEM139, RASSF6 |
| [[HDAC6]] | B | HDAC6 activity lowers ARHGEF18's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (36.4, 4.9); signed map (-4.6, 42.0). **Vector** length 118, 31.5% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.5 | +11.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.2 | +9.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.8 | +11.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -5.3 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -6.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.5 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.4 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | Rho/Rac guanine nucleotide exchange factor 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,348,937-7,472,485 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P114-RhoGEF, KIAA0521, MGC15913, p114RhoGEF |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 15 pathways, smallest: TGF-beta receptor signaling in EMT (epithelial to mesenchymal transition); NRAGE signals death through JNK; G alpha (12/13) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZSZ5](https://www.uniprot.org/uniprotkb/Q6ZSZ5) (Rho guanine nucleotide exchange factor 18):

> Acts as a guanine nucleotide exchange factor (GEF) for RhoA GTPases. Its activation induces formation of actin stress fibers. Also acts as a GEF for RAC1, inducing production of reactive oxygen species (ROS). Does not act as a GEF for CDC42. The G protein beta-gamma (Gbetagamma) subunits of heterotrimeric G proteins act as activators, explaining the integrated effects of LPA and other G protein-coupled receptor agonists on actin stress fiber formation, cell shape change and ROS production. …

**Summary**, from NCBI Gene [23370](https://www.ncbi.nlm.nih.gov/gene/23370):

> Rho GTPases are GTP binding proteins that regulate a wide spectrum of cellular functions. These cellular processes include cytoskeletal rearrangements, gene transcription, cell growth and motility. Activation of Rho GTPases is under the direct control of guanine nucleotide exchange factors (GEFs). The protein encoded by this gene is a guanine nucleotide exchange factor and belongs to the Rho GTPase GEF family. Family members share a common feature, a Dbl (DH) homology domain followed by a …

**Accessions** — [HGNC:17090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17090) · Entrez [23370](https://www.ncbi.nlm.nih.gov/gene/23370) · UniProt [Q6ZSZ5](https://www.uniprot.org/uniprotkb/Q6ZSZ5) · Ensembl [ENSG00000104880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104880)

## Data

Gene col 2513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2513); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2513]; `tensor/DDL_lfc|DDL_z.npy` [2513]; `embed/gene_vectors.npy` [2513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2513 or target_col == 2513). Every well: [[ARHGEF18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
