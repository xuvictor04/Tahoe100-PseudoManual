---
symbol: "SEM1"
type: "gene"
col: 4842
ensembl_id: "ENSG00000127922"
name: "SEM1 26S proteasome subunit"
location: "7q21.3"
module: 21
arm: "+"
pooled_cpm: 121.26
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SEM1

*SEM1 26S proteasome subunit* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.01× (z +11.9, q 9e-30, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.691× (z -6.2, q 2e-07, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCA]] (+0.67, fdr 7e-06), [[ZRANB2-AS1]] (+0.64, fdr 1e-05), [[ASB3]] (+0.64, fdr 7e-06); moves opposite to [[TTLL12]] (-0.59, fdr 3e-05), [[THEM6]] (-0.57, fdr 3e-05), [[DUSP7]] (-0.55, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.01×** | +11.9 | 9e-30 | 47/48 (NCI-H1573, HT-29, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.04×** | +11.4 | 7e-28 | 48/48 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +11.3 | 3e-27 | 48/48 (NCI-H1573, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +11.2 | 7e-27 | 47/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +10.4 | 3e-23 | 43/48 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.8 | 9e-17 | 41/49 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +7.2 | 6e-11 | 42/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +7.1 | 1e-10 | 44/49 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +6.3 | 2e-08 | 34/48 (NCI-H1573, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.30×** | +6.0 | 1e-07 | 28/48 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.8 | 3e-07 | 28/49 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.3 | 7e-06 | 30/44 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +5.2 | 7e-06 | 31/45 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.2 | 8e-06 | 29/48 (SW 900, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.50×** | +5.0 | 3e-05 | 38/49 (NCI-H1573, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.64×** | +4.4 | 3e-04 | 30/49 (C32, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 6e-04 | 34/48 (NCI-H23, A-172, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.002 | 26/48 (C32, NCI-H23, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.021 | 22/47 (hTERT-HPNE, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.029 | 25/48 (HT-29, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.691×** | -6.2 | 2e-07 | 35/48 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.753×** | -4.8 | 5e-04 | 32/48 (SW 900, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.800×** | -3.8 | 0.031 | 30/48 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.791×** | -3.5 | 0.079 | 29/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.827× | -3.2 | 0.13 | 22/48 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.806× | -3.2 | 0.13 | 21/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.807× | -3.1 | 0.13 | 22/48 (A-427, A-172, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.837× | -3.0 | 0.19 | 22/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 180 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 103 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.7) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.18× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 104 | 7 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.96× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.9) | — |
| [[C32 (line)]] | wt | 290 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.72× (z +15.6) | — |
| [[LoVo (line)]] | wt | 119 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 82.5 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.23× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 97.6 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 140 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 94.4 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +14.3) | — |
| [[SW 900 (line)]] | alt | 150 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +14.5) | — |
| [[A-172 (line)]] | wt | 109 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.08× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 89.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.85× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 112 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.00× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 83.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 110 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.63× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 70.9 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 98.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +11.0) | — |
| [[A549 (line)]] | wt | 96.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +13.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 177 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.17× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 110 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 92.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 109 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.0) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.36× (z +8.6) | — |
| [[SW48 (line)]] | wt | 115 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 3.43× (z +10.6) | — |
| [[SW480 (line)]] | alt | 127 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.24× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +8.9) | — |
| [[A-427 (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 99.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 118 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.6) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[A498 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 161 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 102 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 92.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 150 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCA]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ASB3]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SLC23A1]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PIN4]] | +0.63 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[GCNT7]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[EPM2AIP1]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[BIRC6-AS2-1]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[VPS39-DT]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.60 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[UBOX5-AS1]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ZNF547]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL12]] | -0.59 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[THEM6]] | -0.57 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[DUSP7]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 | pathway: MAPK family signaling cascades |
| [[AKAP11]] | -0.54 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PGM2]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[SSX2IP]] | -0.53 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SEM1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.2, 27.6); signed map (5.4, 5.6). **Vector** length 110, 37.2% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.6 | +11.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +11.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.7 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.8 | +5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.4 | +4.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -4.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | SEM1 26S proteasome subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:96,481,626-96,709,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DSS1, Shfdg1, ECD, SHSF1, FLJ42280, PSMD15; previously SHFD1, SHFM1, C7orf76 |
| Gene groups (HGNC) | Proteasome; Transcription and export complex 2 |
| Reactome | 185 pathways, smallest: Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function; Defective homologous recombination repair (HRR) due to BRCA1 loss of function |
| Matched by | ensembl_id |

**Function**, from UniProt [P60896](https://www.uniprot.org/uniprotkb/P60896) (26S proteasome complex subunit SEM1):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. Component of the …

**Summary**, from NCBI Gene [7979](https://www.ncbi.nlm.nih.gov/gene/7979):

> The product of this gene has been localized within the split hand/split foot malformation locus SHFM1 at chromosome 7. It has been proposed to be a candidate gene for the autosomal dominant form of the heterogeneous limb developmental disorder split hand/split foot malformation type 1. In addition, it has been shown to directly interact with BRCA2. It also may play a role in the completion of the cell cycle. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10845) · Entrez [7979](https://www.ncbi.nlm.nih.gov/gene/7979) · UniProt [P60896](https://www.uniprot.org/uniprotkb/P60896) · Ensembl [ENSG00000127922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127922)

## Data

Gene col 4842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4842); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4842]; `tensor/DDL_lfc|DDL_z.npy` [4842]; `embed/gene_vectors.npy` [4842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4842 or target_col == 4842). Every well: [[SEM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
