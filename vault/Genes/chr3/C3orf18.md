---
symbol: "C3orf18"
type: "gene"
col: 1537
ensembl_id: "ENSG00000088543"
name: "chromosome 3 open reading frame 18"
location: "3p21.31"
module: 128
arm: "+"
pooled_cpm: 2.63
n_lines_expressing: 40
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 21
direction_downstream: 8
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# C3orf18

*chromosome 3 open reading frame 18* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.52× (z +8.2, q 9e-14, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.46× (z +3.5, q 0.051, up in 6 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.206× (z -14.5, q 6e-45, down in 30 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BARX1]] (+0.58, fdr 1e-04), [[BOLA3-DT]] (+0.58, fdr 4e-05), [[SEPTIN5]] (+0.55, fdr 2e-05); moves opposite to [[LEMD1]] (-0.50, fdr 1e-05), [[CUEDC1]] (-0.46, fdr 3e-05), [[POU5F1B]] (-0.46, fdr 7e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); 8 go from it, the strongest it → [[BOLA3-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +8.2 | 9e-14 | 1/4 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.44×** | +4.8 | 4e-04 | 4/32 (HOP62, RKO, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.2 | 0.005 | 6/13 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.1 | 0.006 | 5/17 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.051 | 6/34 (NCI-H23, LS 180, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.61× | +3.2 | 0.15 | 1/15 (NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.17 | 4/29 (LoVo, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.206×** | -14.5 | 6e-45 | 30/34 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.328×** | -10.2 | 4e-22 | 24/29 (PANC-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.334×** | -10.1 | 2e-21 | 24/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.579×** | -7.0 | 3e-10 | 15/27 (HOP62, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.484×** | -6.6 | 4e-09 | 18/34 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.483×** | -6.4 | 1e-08 | 15/32 (NCI-H23, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.519×** | -6.0 | 2e-07 | 19/24 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.532×** | -5.8 | 6e-07 | 16/29 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.562×** | -5.3 | 9e-06 | 17/29 (hTERT-HPNE, PANC-1, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.335×** | -5.3 | 9e-06 | 15/32 (HOP62, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.565×** | -5.2 | 1e-05 | 14/24 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -4.7 | 1e-04 | 13/30 (HS-578T, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.612×** | -4.5 | 3e-04 | 15/35 (SNU-423, SNU-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.596×** | -4.5 | 3e-04 | 9/30 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -4.1 | 0.002 | 13/23 (NCI-H2030, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -3.9 | 0.003 | 11/24 (A-427, HS-578T, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.671×** | -3.4 | 0.020 | 9/31 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **0.719×** | -3.0 | 0.079 | 5/26 (HS-578T, SW1417, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.72 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0854× (z -12.6) |
| [[A-427 (line)]] | wt | 8.73 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -10.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 2.63 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0486× (z -11.4) |
| [[HOP62 (line)]] | alt | 5.42 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0209× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 5.21 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0467× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 5.48 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0262× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 5.09 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0478× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 7.42 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0837× (z -10.0) |
| [[SW480 (line)]] | alt | 2.26 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0226× (z -13.8) |
| [[HS-578T (line)]] | alt | 4.23 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0252× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 1.76 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0287× (z -9.0) |
| [[SHP-77 (line)]] | alt | 3.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0486× (z -9.2) |
| [[A-172 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.768 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.952 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.663 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.705 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BARX1]] | +0.58 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[BOLA3-DT]] | +0.58 | +0.57 / +0.40 | both halves | 4e-05 |  |
| [[SEPTIN5]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ARHGEF25]] | +0.55 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[BASP1-AS1]] | +0.52 | +0.60 / +0.36 | both halves | 9e-05 |  |
| [[DUSP9]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[NEFL]] | +0.50 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[RNF220]] | +0.50 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[STRA6LP]] | +0.49 | +0.51 / +0.29 | both halves | 2e-04 |  |
| [[ADAMTS10]] | +0.49 | +0.51 / +0.30 | both halves | 2e-04 |  |
| [[PTPN20]] | +0.49 | +0.31 / +0.40 | both halves | 2e-04 |  |
| [[EFEMP2]] | +0.48 | +0.47 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEMD1]] | -0.50 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CUEDC1]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[POU5F1B]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[B4GALNT3]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PKP4]] | -0.45 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[CATSPERB]] | -0.45 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[PLEKHS1]] | -0.44 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[SYK]] | -0.44 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[NPSR1-AS1]] | -0.44 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[SAMD12-AS1]] | -0.44 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[PCAT1]] | -0.44 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[RAPGEF5]] | -0.44 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity raises C3orf18's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without BOLA3-DT | 0.003 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[CATSPERB]] | B | CATSPERB activity lowers C3orf18's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 1.48× higher at baseline in the lines without CATSPERB | 0.009 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[BLACAT1]] | B | BLACAT1 activity lowers C3orf18's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 1.56× higher at baseline in the lines without BLACAT1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[LEMD1]] | B | LEMD1 activity lowers C3orf18's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.60× higher at baseline in the lines without LEMD1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[TMPRSS4]] | B | TMPRSS4 activity lowers C3orf18's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 1.58× higher at baseline in the lines without TMPRSS4 | 0.016 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[SLC6A14]] | B | SLC6A14 activity lowers C3orf18's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 1.58× higher at baseline in the lines without SLC6A14 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[FBXO15]] | B | FBXO15 activity raises C3orf18's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without FBXO15 | 0.023 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[LEMD1]] | B | LEMD1 activity weakens C3orf18's drug response | lines that do not express LEMD1 (16) vs lines expressing it (18) | the lines without LEMD1 respond 2.30× as strongly (z diff -2.18); strongest at Homoharringtonine 5 µM: 0.26x vs 0.70x (z diff -5.0) | 0.033 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2; target measured in part of the lines; artifact flags |
| [[SYK]] | B | SYK activity lowers C3orf18's level | lines that do not express SYK (30) vs lines expressing it (20) | 1.42× higher at baseline in the lines without SYK | 0.048 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[ATP10B]] | B | ATP10B activity lowers C3orf18's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 1.72× higher at baseline in the lines without ATP10B | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[HSD17B2]] | B | HSD17B2 activity lowers C3orf18's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 1.50× higher at baseline in the lines without HSD17B2 | 0.050 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[LINC00888]] | B | LINC00888 activity raises C3orf18's level | lines that do not express LINC00888 (7) vs lines expressing it (43) | 1.84× lower at baseline in the lines without LINC00888 | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | C3orf18 activity raises BOLA3-DT's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without C3orf18 | 0.014 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[STS]] | B | C3orf18 activity lowers STS's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 3.33× higher at baseline in the lines without C3orf18 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[SAMD12-AS1]] | B | C3orf18 activity lowers SAMD12-AS1's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 3.54× higher at baseline in the lines without C3orf18 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[ZNF25]] | B | C3orf18 activity raises ZNF25's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 1.41× lower at baseline in the lines without C3orf18 | 0.042 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[ZKSCAN3]] | B | C3orf18 activity raises ZKSCAN3's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 1.26× lower at baseline in the lines without C3orf18 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[HNF4G]] | B | C3orf18 activity lowers HNF4G's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 1.89× higher at baseline in the lines without C3orf18 | 0.072 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[PCAT1]] | B | C3orf18 activity lowers PCAT1's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 2.15× higher at baseline in the lines without C3orf18 | 0.074 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[ZNF18]] | B | C3orf18 activity raises ZNF18's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 1.37× lower at baseline in the lines without C3orf18 | 0.079 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.496). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.5, 40.8); signed map (22.7, 26.7). **Vector** length 48.0, 7.25% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.6 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +1.6 | +4.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.0 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +3.5 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +0.8 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +0.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -10.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -2.9 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -14.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -10.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -5.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -0.9 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 3 open reading frame 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,558,025-50,571,027 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G20 |
| Matched by | ensembl_id |

UniProt [Q9UK00](https://www.uniprot.org/uniprotkb/Q9UK00) carries no function annotation.

**Summary**, from NCBI Gene [51161](https://www.ncbi.nlm.nih.gov/gene/51161):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24837) · Entrez [51161](https://www.ncbi.nlm.nih.gov/gene/51161) · UniProt [Q9UK00](https://www.uniprot.org/uniprotkb/Q9UK00) · Ensembl [ENSG00000088543](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088543)

## Data

Gene col 1537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1537); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1537]; `tensor/DDL_lfc|DDL_z.npy` [1537]; `embed/gene_vectors.npy` [1537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1537 or target_col == 1537). Every well: [[C3orf18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C3orf18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
