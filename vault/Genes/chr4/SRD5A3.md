---
symbol: "SRD5A3"
type: "gene"
col: 4858
ensembl_id: "ENSG00000128039"
name: "steroid 5 alpha-reductase 3"
location: "4q12"
module: 61
arm: "+"
pooled_cpm: 17.81
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 34
n_dd_up_clean: 5
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SRD5A3

*steroid 5 alpha-reductase 3* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +7.9, q 2e-12, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.280× (z -23.1, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF470]] (+0.52, fdr 3e-05), [[SLFN11]] (+0.48, fdr 6e-05), [[GPRIN1]] (+0.48, fdr 1e-04); moves opposite to [[CTPS2]] (-0.49, fdr 7e-05), [[ARFGEF2]] (-0.49, fdr 1e-04), [[ITPKB]] (-0.46, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.9 | 2e-12 | 28/46 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +5.8 | 2e-06 | 24/44 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +5.3 | 2e-05 | 22/45 (C32, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.0 | 7e-05 | 17/34 (A-427, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.9 | 1e-04 | 22/45 (CFPAC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.090 | 15/42 (HT-29, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 1.27× | +3.1 | 0.16 | 12/44 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.16 | 9/45 (HT-29, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.16 | 8/39 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4858.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.280×** | -23.1 | 0e+00 | 42/43 (H4, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.276×** | -16.5 | 0e+00 | 44/46 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.311×** | -15.0 | 0e+00 | 41/44 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.375×** | -12.6 | 4e-34 | 37/45 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -11.9 | 8e-31 | 36/43 (H4, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.418×** | -11.2 | 4e-27 | 35/44 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.403×** | -10.8 | 3e-25 | 37/44 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.438×** | -10.6 | 3e-24 | 33/43 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.452×** | -10.2 | 2e-22 | 37/45 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.501×** | -8.4 | 3e-15 | 34/44 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.553×** | -7.6 | 2e-12 | 32/46 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.332×** | -7.4 | 7e-12 | 30/45 (SHP-77, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.575×** | -7.1 | 6e-11 | 28/45 (PANC-1, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.682×** | -6.9 | 2e-10 | 26/46 (A-427, BT-474, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -6.9 | 3e-10 | 28/41 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.378×** | -6.5 | 2e-09 | 27/43 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -6.2 | 2e-08 | 25/44 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.616×** | -6.2 | 2e-08 | 27/46 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 52.4 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0339× (z -29.5) |
| [[BT-474 (line)]] | alt | 50.2 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -17.8) |
| [[PANC-1 (line)]] | alt | 18.9 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -24.7) |
| [[NCI-H1573 (line)]] | alt | 44.3 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -22.7) |
| [[A-172 (line)]] | wt | 25.4 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -19.9) |
| [[SW 900 (line)]] | alt | 39.3 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -24.7) |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0649× (z -24.0) |
| [[LoVo (line)]] | wt | 29.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.3) |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 33.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0490× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -13.1) |
| [[A-427 (line)]] | wt | 27.1 | 0 | 5 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.328× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0746× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 9.56 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.0) |
| [[A549 (line)]] | wt | 12.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -14.7) |
| [[LS 180 (line)]] | wt | 36.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -14.6) |
| [[RKO (line)]] | wt | 8.72 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0763× (z -9.1) |
| [[C32 (line)]] | wt | 8.93 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 15.7× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.0662× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 30.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -18.8) |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 6.80× (z +9.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -8.6) |
| [[SW480 (line)]] | alt | 5.77 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.0266× (z -10.4) |
| [[A498 (line)]] | wt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 6.16 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.72× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -9.4) |
| [[HT-29 (line)]] | alt | 9.51 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.9× (z +10.4) | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -18.5) |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.4) |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0865× (z -8.9) |
| [[SW48 (line)]] | wt | 9.69 | 1 | 0 | [[Auranofin (drug)]] 5 µM 16.5× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF470]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SLFN11]] | +0.48 | +0.38 / +0.41 | both halves | 6e-05 |  |
| [[GPRIN1]] | +0.48 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[AFF2]] | +0.48 | +0.38 / +0.41 | both halves | 6e-05 |  |
| [[ABCB1]] | +0.46 | +0.25 / +0.36 | both halves | 4e-04 |  |
| [[MIR493HG]] | +0.44 | +0.33 / +0.34 | both halves | 1e-04 |  |
| [[RNF223]] | +0.44 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[TSC22D2]] | +0.44 | +0.30 / +0.41 | both halves | 2e-04 |  |
| [[CCDC33]] | +0.44 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[ELL2]] | +0.43 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[SLC39A3]] | +0.43 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[MEG3]] | +0.42 | +0.37 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS2]] | -0.49 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[ARFGEF2]] | -0.49 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[ITPKB]] | -0.46 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[PDHX]] | -0.44 | -0.26 / -0.42 | both halves | 3e-04 |  |
| [[UVRAG]] | -0.44 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[TBC1D5]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[EXOC4]] | -0.44 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[FARS2]] | -0.43 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[MCCC2]] | -0.42 | -0.26 / -0.48 | both halves | 4e-04 | pathway: Diseases of metabolism |
| [[LRRC37A4P]] | -0.42 | -0.18 / -0.39 | ⚠ not reproduced | 9e-04 |  |
| [[NNT]] | -0.42 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[FOXP4-AS1]] | -0.42 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[EIF2D]] | -0.42 | -0.27 / -0.36 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SRD5A3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PKIA]] | B | PKIA activity raises SRD5A3's level | lines that do not express PKIA (22) vs lines expressing it (28) | 1.64× lower at baseline in the lines without PKIA | 0.084 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.219). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.1, 15.8); signed map (32.0, 31.6). **Vector** length 74.5, 16.3% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.3 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -11.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.5 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.4 | -5.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | -3.4 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -15.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -6.9 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | steroid 5 alpha-reductase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:55,346,213-55,373,100 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13352, SRD5A2L, SRD5A2L1 |
| Gene groups (HGNC) | Steroid 5-alpha reductase family |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 11 pathways, smallest: Androgen biosynthesis; Synthesis of dolichyl-phosphate; Diseases associated with glycosylation precursor biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8P0](https://www.uniprot.org/uniprotkb/Q9H8P0) (Polyprenal reductase):

> Plays a key role in early steps of protein N-linked glycosylation by being involved in the conversion of polyprenol into dolichol. Acts as a polyprenal reductase that mediates the reduction of polyprenal into dolichal in a NADP-dependent mechanism. Dolichols are required for the synthesis of dolichol-linked monosaccharides and the oligosaccharide precursor used for N-glycosylation. Also able to convert testosterone (T) into 5-alpha-dihydrotestosterone (DHT).

**Summary**, from NCBI Gene [79644](https://www.ncbi.nlm.nih.gov/gene/79644):

> The protein encoded by this gene belongs to the steroid 5-alpha reductase family, and polyprenol reductase subfamily. It is involved in the production of androgen 5-alpha-dihydrotestosterone (DHT) from testosterone, and maintenance of the androgen-androgen receptor activation pathway. This protein is also necessary for the conversion of polyprenol into dolichol, which is required for the synthesis of dolichol-linked monosaccharides and the oligosaccharide precursor used for N-linked …

**Accessions** — [HGNC:25812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25812) · Entrez [79644](https://www.ncbi.nlm.nih.gov/gene/79644) · UniProt [Q9H8P0](https://www.uniprot.org/uniprotkb/Q9H8P0) · Ensembl [ENSG00000128039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128039)

## Data

Gene col 4858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4858); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4858]; `tensor/DDL_lfc|DDL_z.npy` [4858]; `embed/gene_vectors.npy` [4858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4858 or target_col == 4858). Every well: [[SRD5A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRD5A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
