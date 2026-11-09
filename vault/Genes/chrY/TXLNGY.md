---
symbol: "TXLNGY"
type: "gene"
col: 5154
ensembl_id: "ENSG00000131002"
name: "taxilin gamma Y-linked (pseudogene)"
location: "Yq11.222-q11.223"
module: 5
arm: "+"
pooled_cpm: 12.07
n_lines_expressing: 20
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TXLNGY

*taxilin gamma Y-linked (pseudogene)* — Yq11.222-q11.223

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.32× (z +15.6, q 0e+00, up in 3 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Verteporfin (drug)]] 0.5 µM: 1.59× (z +6.0, q 2e-07, up in 0 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.725× (z -3.9, q 0.038, down in 0 of 18 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXLNGY-1]] (+0.92, fdr 7e-06, ⚠ same locus), [[MRPS25]] (+0.59, fdr 1e-05), [[ECHDC1]] (+0.55, fdr 4e-05), [[EDNRB]] (+0.55, fdr 3e-05); moves opposite to [[CASP9]] (-0.50, fdr 2e-04), [[RNASE4]] (-0.49, fdr 4e-05), [[RIOK3]] (-0.48, fdr 5e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[PYGO1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.32×** | +15.6 | 0e+00 | 3/16 (HCT15, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +14.9 | 0e+00 | 6/13 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +7.2 | 1e-10 | 1/14 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.59×** | +6.0 | 2e-07 | 0/17 | two highest doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.55×** | +5.5 | 4e-06 | 1/17 (SNU-423) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.3 | 1e-05 | 6/18 (COLO 205, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.8 | 1e-04 | 6/17 (A-172, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.002 | 0/18 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.002 | 7/18 (A-172, COLO 205, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.003 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.005 | 6/17 (J82, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.8 | 0.007 | 4/17 (A-172, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.7 | 0.009 | 3/17 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.015 | 4/17 (SK-MEL-2, A-172, …) | inconsistent across doses |  |
| [[Everolimus (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.031 | 0/18 | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.034 | 0/18 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.093 | 1/18 (hTERT-HPNE) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.099 | 0/17 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.725×** | -3.9 | 0.038 | 0/18 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.747×** | -3.8 | 0.038 | 6/18 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.744×** | -3.7 | 0.046 | 3/18 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.760×** | -3.6 | 0.046 | 7/18 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.4 | 0.065 | 0/18 | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.065 | 3/18 (SNU-423, SK-MEL-2, …) | two highest doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.772× | -3.1 | 0.15 | 1/18 (SW 1088) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.775× | -3.1 | 0.15 | 0/18 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -13.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.101× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -12.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.000 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.880 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXLNGY-1]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MRPS25]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ECHDC1]] | +0.55 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[EDNRB]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[GNL3L]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PYGO1]] | +0.52 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[METTL8]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[SNX5]] | +0.51 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[LIN28B]] | +0.50 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[ATR]] | +0.50 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[BAGE2]] | +0.50 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[PTPRG]] | +0.50 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[KCNK2]] | +0.49 | +0.50 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP9]] | -0.50 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[RNASE4]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[RIOK3]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TUBA1A]] | -0.47 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[CARHSP1]] | -0.46 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[TNNT1]] | -0.46 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[WASF2]] | -0.46 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[LGALS1]] | -0.44 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[GNAI3]] | -0.43 | -0.48 / -0.24 | both halves | 4e-04 |  |
| [[RETREG2]] | -0.43 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[OSER1]] | -0.43 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[PLA2G15]] | -0.43 | -0.33 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TXLNGY's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TTTY10]] | C | TTTY10 activity raises TXLNGY's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 14.61× lower at baseline in the lines without TTTY10 | 7e-07 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises TXLNGY's level | lines that do not express BCHE (35) vs lines expressing it (15) | 2.94× lower at baseline in the lines without BCHE | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYGO1]] | B | TXLNGY, [[TXLNGY-1]] activity raises PYGO1's level | lines that do not express TXLNGY, TXLNGY-1 (30) vs lines expressing them (20) | 2.28× lower at baseline in the lines without TXLNGY, TXLNGY-1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent genes |
| [[KCNK2]] | B | TXLNGY activity raises KCNK2's level | lines that do not express TXLNGY (30) vs lines expressing it (20) | 1.82× lower at baseline in the lines without TXLNGY | 0.065 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[COL4A5]] | B | TXLNGY activity raises COL4A5's level | lines that do not express TXLNGY (30) vs lines expressing it (20) | 1.82× lower at baseline in the lines without TXLNGY | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[TTTY10]] | C | TXLNGY, [[TXLNGY-1]] activity raises TTTY10's level | lines that do not express TXLNGY, TXLNGY-1 (30) vs lines expressing them (20) | 5.93× lower at baseline in the lines without TXLNGY, TXLNGY-1 | 8e-06 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target; co-absent genes |
| [[BCHE]] | C | TXLNGY activity raises BCHE's level | lines that do not express TXLNGY (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without TXLNGY | 0.012 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |
| [[EDNRB]] | C | TXLNGY, [[TXLNGY-1]] activity raises EDNRB's level | lines that do not express TXLNGY, TXLNGY-1 (30) vs lines expressing them (20) | 2.39× lower at baseline in the lines without TXLNGY, TXLNGY-1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.459). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (1.1, -53.0); signed map (-2.3, -51.3). **Vector** length 37.0, 8.10% of its response variance represented; |z| ≥ 3 in 310 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.2 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.3 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -0.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | taxilin gamma Y-linked (pseudogene) |
| Locus type | pseudogene |
| Location | Yq11.222-q11.223 — chrY:19,567,382-19,604,120 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously CYorf15A, CYorf15B, TXLNG2P |
| Matched by | ensembl_id |

UniProt [Q9BZA5](https://www.uniprot.org/uniprotkb/Q9BZA5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:18473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18473) · Entrez [246126](https://www.ncbi.nlm.nih.gov/gene/246126) · UniProt [Q9BZA5](https://www.uniprot.org/uniprotkb/Q9BZA5) · Ensembl [ENSG00000131002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131002)

## Data

Gene col 5154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5154); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5154]; `tensor/DDL_lfc|DDL_z.npy` [5154]; `embed/gene_vectors.npy` [5154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5154 or target_col == 5154). Every well: [[TXLNGY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXLNGY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
