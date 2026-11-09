---
symbol: "METTL27"
type: "gene"
col: 9079
ensembl_id: "ENSG00000165171"
name: "methyltransferase like 27"
location: "7q11.23"
module: 148
arm: "-"
pooled_cpm: 5.19
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# METTL27

*methyltransferase like 27* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.79× (z +5.3, q 6e-05, up in 1 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.43× (z +4.8, q 4e-04, up in 14 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.443× (z -10.8, q 2e-24, down in 32 of 35 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDHD3]] (+0.57, fdr 2e-05), [[HES2]] (+0.55, fdr 1e-05), [[ABTB1]] (+0.53, fdr 8e-05); moves opposite to [[COX18]] (-0.49, fdr 9e-05), [[MLH1]] (-0.47, fdr 2e-04), [[MRPL30]] (-0.47, fdr 1e-04).
> It sits in the **-** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HES2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.3 | 6e-05 | 1/9 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.8 | 4e-04 | 14/43 (KATO III, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +4.7 | 5e-04 | 14/44 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.048 | 11/39 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.048 | 10/36 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.5 | 0.048 | 6/20 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.060 | 11/42 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.060 | 4/40 (SNU-1, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.060 | 10/43 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.060 | 7/43 (A-427, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.060 | 14/42 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.073 | 10/43 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.59×** | +3.1 | 0.076 | 5/37 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.37× | +3.0 | 0.10 | 4/30 (SW48, COLO 205, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9079.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.443×** | -10.8 | 2e-24 | 32/35 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.321×** | -10.7 | 4e-24 | 36/45 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.409×** | -8.4 | 1e-14 | 29/34 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -8.1 | 1e-13 | 25/33 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.432×** | -7.9 | 4e-13 | 30/40 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.464×** | -7.2 | 6e-11 | 26/43 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.454×** | -7.1 | 8e-11 | 22/39 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.500×** | -6.5 | 6e-09 | 22/41 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -5.1 | 2e-05 | 20/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.356×** | -5.1 | 2e-05 | 21/40 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.360×** | -5.0 | 3e-05 | 17/31 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.586×** | -4.3 | 0.001 | 11/44 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.447×** | -3.9 | 0.003 | 12/38 (NCI-H460, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.583×** | -3.6 | 0.013 | 12/43 (H4, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.703×** | -3.3 | 0.038 | 11/41 (C-33 A, HS-578T, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.721×** | -3.0 | 0.076 | 6/43 (AN3 CA, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.683×** | -3.0 | 0.081 | 15/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.19 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0867× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 5.70 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -12.6) |
| [[KATO III (line)]] | alt | 17.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0977× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -11.4) |
| [[A549 (line)]] | wt | 4.34 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0730× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -9.7) ⚠ cell-cycle shift, explains ~7% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.82 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 7.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.8) |
| [[HT-29 (line)]] | alt | 6.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0647× (z -12.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 6.20 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0384× (z -12.8) |
| [[SNU-1 (line)]] | wt | 6.13 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0486× (z -9.1) |
| [[SNU-423 (line)]] | alt | 5.07 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -9.4) ⚠ cell-cycle shift, explains ~7% of this change |
| [[SW1417 (line)]] | alt | 9.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0564× (z -13.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 9.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -9.0) |
| [[SW480 (line)]] | alt | 6.03 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -10.5) |
| [[A-172 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDHD3]] | +0.57 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[HES2]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ABTB1]] | +0.53 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[LMTK2]] | +0.53 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[OSBPL9]] | +0.52 | +0.41 / +0.39 | both halves | 6e-05 |  |
| [[MLXIPL]] | +0.52 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[NOXA1]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[KCTD17]] | +0.50 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[ACBD4]] | +0.48 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[C2orf68]] | +0.48 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[YPEL3]] | +0.47 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[CBLC]] | +0.47 | +0.41 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX18]] | -0.49 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[MLH1]] | -0.47 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[MRPL30]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[SNX5]] | -0.47 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[NDUFS1]] | -0.46 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[CYB5D1]] | -0.46 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[MPDU1]] | -0.45 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[ARCN1]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[AGL]] | -0.45 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[PUS10]] | -0.44 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[ZNF34]] | -0.44 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[RAB27A]] | -0.44 | -0.25 / -0.45 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES2]] | B | HES2 activity raises METTL27's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without HES2 | 0.048 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[MEGF6]] | B | MEGF6 activity raises METTL27's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without MEGF6 | 0.054 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers METTL27's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers METTL27's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **-** arm (projection on the module's main direction -0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.1, 41.9); signed map (-19.5, 31.6). **Vector** length 57.3, 9.10% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.0 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -7.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase like 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,834,590-73,842,516 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously WBSCR27 |
| Gene groups (HGNC) | 7BS orphan methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6F8](https://www.uniprot.org/uniprotkb/Q8N6F8) (Probable methyltransferase-like protein 27):

> Probable S-adenosyl-L-methionine-dependent methyltransferase.

**Summary**, from NCBI Gene [155368](https://www.ncbi.nlm.nih.gov/gene/155368):

> This gene encodes a protein belonging to ubiE/COQ5 methyltransferase family. The gene is deleted in Williams syndrome, a multisystem developmental disorder caused by the deletion of contiguous genes at 7q11.22-q11.23. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19068) · Entrez [155368](https://www.ncbi.nlm.nih.gov/gene/155368) · UniProt [Q8N6F8](https://www.uniprot.org/uniprotkb/Q8N6F8) · Ensembl [ENSG00000165171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165171)

## Data

Gene col 9079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9079); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9079]; `tensor/DDL_lfc|DDL_z.npy` [9079]; `embed/gene_vectors.npy` [9079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9079 or target_col == 9079). Every well: [[METTL27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
