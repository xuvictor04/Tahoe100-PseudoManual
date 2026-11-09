---
symbol: "DPH6-DT"
type: "gene"
col: 14515
ensembl_id: "ENSG00000248079"
name: "DPH6 divergent transcript"
location: "15q14"
module: 10
arm: "+"
pooled_cpm: 13.46
n_lines_expressing: 47
n_dd_up: 34
n_dd_down: 17
n_dd_up_clean: 31
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# DPH6-DT

*DPH6 divergent transcript* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.84× (z +11.8, q 1e-29, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.350× (z -8.5, q 2e-14, down in 38 of 44 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.367× (z -8.1, q 1e-13, down in 35 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX4-DT]] (+0.83, fdr 7e-06), [[TMEM202-AS1]] (+0.83, fdr 1e-05), [[MAD2L1-DT]] (+0.81, fdr 1e-05); moves opposite to [[FAM118A]] (-0.66, fdr 3e-04), [[TPST2]] (-0.66, fdr 1e-04), [[TCF3]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[KATNAL2]] → it (grade B ⚠); 12 go from it, the strongest it → [[ACCS]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +11.8 | 1e-29 | 36/41 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +8.2 | 1e-13 | 31/42 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.58×** | +7.6 | 6e-12 | 37/44 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.86×** | +7.0 | 3e-10 | 33/45 (J82, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +5.8 | 7e-07 | 23/42 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +5.4 | 7e-06 | 22/40 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +5.3 | 8e-06 | 27/44 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.3 | 8e-06 | 26/41 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.85×** | +4.9 | 5e-05 | 25/43 (LoVo, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.87×** | +4.8 | 8e-05 | 26/43 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.80×** | +4.7 | 1e-04 | 23/44 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.005 | 22/44 (LoVo, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.69×** | +3.9 | 0.005 | 20/44 (SK-MEL-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.005 | 21/44 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.006 | 17/43 (LS 180, HT-29, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.007 | 16/43 (NCI-H460, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.350×** | -8.5 | 2e-14 | 38/44 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.364×** | -8.1 | 1e-13 | 27/41 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.367×** | -8.1 | 1e-13 | 35/44 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.408×** | -7.2 | 7e-11 | 34/44 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.474×** | -6.0 | 2e-07 | 29/44 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.485×** | -5.8 | 5e-07 | 28/44 (AN3 CA, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.467×** | -5.8 | 6e-07 | 25/43 (Hs 766T, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.276×** | -5.0 | 5e-05 | 22/40 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.282×** | -4.9 | 7e-05 | 24/44 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.557×** | -4.7 | 1e-04 | 23/44 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.586×** | -4.3 | 8e-04 | 20/44 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.588×** | -4.3 | 8e-04 | 24/44 (AN3 CA, MIA PaCa-2, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.521×** | -3.7 | 0.008 | 19/45 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.622×** | -3.7 | 0.009 | 17/39 (NCI-H23, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.597×** | -3.7 | 0.009 | 21/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.728×** | -3.6 | 0.010 | 22/45 (MIA PaCa-2, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.8 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.148× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 20.3 | 1 (1 ⚠) | 4 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +8.9) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.115× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.185× (z -8.6) |
| [[Hs 766T (line)]] | wt | 30.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0926× (z -9.9) |
| [[LoVo (line)]] | wt | 11.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 6.74 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.177× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0754× (z -10.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0797× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HT-29 (line)]] | alt | 4.61 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0710× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 9.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0653× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0370× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +9.0) | — |
| [[RKO (line)]] | wt | 4.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.99× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.114× (z -9.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 6.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +8.7) | — |
| [[A-172 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | +0.83 | +0.84 / +0.63 | both halves | 7e-06 | same gene group |
| [[TMEM202-AS1]] | +0.83 | +0.85 / +0.50 | both halves | 1e-05 |  |
| [[MAD2L1-DT]] | +0.81 | +0.84 / +0.49 | both halves | 1e-05 | same gene group |
| [[EIF1B-AS1]] | +0.81 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[SUCLG2-DT]] | +0.81 | +0.82 / +0.48 | both halves | 2e-05 | same gene group |
| [[OXA1L-DT]] | +0.80 | +0.81 / +0.58 | both halves | 8e-06 | same gene group |
| [[PKN2-AS1]] | +0.80 | +0.82 / +0.46 | both halves | 2e-05 |  |
| [[USP38-DT]] | +0.78 | +0.79 / +0.57 | both halves | 9e-06 | same gene group |
| [[LINC00240]] | +0.77 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[ZRANB2-DT]] | +0.77 | +0.76 / +0.58 | both halves | 7e-06 | same gene group |
| [[SEPTIN7-DT]] | +0.77 | +0.81 / +0.39 | both halves | 5e-05 | same gene group |
| [[EPM2A-DT]] | +0.76 | +0.82 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.66 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[TPST2]] | -0.66 | -0.69 / -0.35 | both halves | 1e-04 |  |
| [[TCF3]] | -0.65 | -0.64 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL2]] | B | KATNAL2 activity raises DPH6-DT's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.64× lower at baseline in the lines without KATNAL2 | 0.025 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[SUCLG2-DT]] | B | SUCLG2-DT activity raises DPH6-DT's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without SUCLG2-DT | 0.028 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[ZNF391]] | B | ZNF391 activity raises DPH6-DT's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 2.96× lower at baseline in the lines without ZNF391 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |
| [[FLRT2]] | B | FLRT2 activity raises DPH6-DT's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without FLRT2 | 0.036 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[TOP2A]] | B | TOP2A activity lowers DPH6-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RMEL3]] | B | RMEL3 activity raises DPH6-DT's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without RMEL3 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent |
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises DPH6-DT's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without CYP1B1-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[LINC03002]] | B | LINC03002 activity raises DPH6-DT's level | lines that do not express LINC03002 (18) vs lines expressing it (32) | 1.35× lower at baseline in the lines without LINC03002 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC01010, NRN1, ODAD2; maybe low, not absent |
| [[ABCA6]] | B | ABCA6 activity raises DPH6-DT's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 1.49× lower at baseline in the lines without ABCA6 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |
| [[LRRIQ3]] | C | LRRIQ3 activity raises DPH6-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without LRRIQ3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACCS]] | C | DPH6-DT activity raises ACCS's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 3.38× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |
| [[SUCLG2-DT]] | C | DPH6-DT activity raises SUCLG2-DT's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.76× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |
| [[CCDC122]] | C | DPH6-DT activity raises CCDC122's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |
| [[BDNF-AS]] | C | DPH6-DT activity raises BDNF-AS's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |
| [[HECTD2]] | C | DPH6-DT activity raises HECTD2's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |
| [[MYL5]] | C | DPH6-DT activity raises MYL5's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without DPH6-DT | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |
| [[HHAT]] | C | DPH6-DT activity raises HHAT's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 3.17× lower at baseline in the lines without DPH6-DT | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |
| [[EIF1B-AS1]] | C | DPH6-DT activity raises EIF1B-AS1's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.24× lower at baseline in the lines without DPH6-DT | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |
| [[PARD3B]] | C | DPH6-DT activity raises PARD3B's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 7.36× lower at baseline in the lines without DPH6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |
| [[UGDH-AS1]] | C | DPH6-DT activity raises UGDH-AS1's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 1.41× lower at baseline in the lines without DPH6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |
| [[PATL2]] | C | DPH6-DT activity raises PATL2's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without DPH6-DT | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |
| [[ENTPD3-AS1]] | C | DPH6-DT activity raises ENTPD3-AS1's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without DPH6-DT | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.857). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.0, 16.6); signed map (30.1, -10.0). **Vector** length 95.0, 24.7% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.5 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +0.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -4.3 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | DPH6 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q14 — chr15:35,546,154-35,860,199 (+) |
| Ensembl biotype | lncRNA |
| Also known as | uc.382; previously ATPBD4-AS1, DPH6-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44147](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44147) · Entrez [100507466](https://www.ncbi.nlm.nih.gov/gene/100507466) · Ensembl [ENSG00000248079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248079)

## Data

Gene col 14515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14515); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14515]; `tensor/DDL_lfc|DDL_z.npy` [14515]; `embed/gene_vectors.npy` [14515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14515 or target_col == 14515). Every well: [[DPH6-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPH6-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
