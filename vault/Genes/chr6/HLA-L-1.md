---
symbol: "HLA-L-1"
type: "gene"
col: 16580
ensembl_id: "ENSG00000291097"
name: ""
location: ""
module: 14
arm: "+"
pooled_cpm: 11.18
n_lines_expressing: 40
n_dd_up: 23
n_dd_down: 8
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# HLA-L-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.17× (z +23.5, q 0e+00, up in 27 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.707× (z -4.8, q 9e-04, down in 15 of 32 measured lines) ⚠ toxic. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.570× (z -4.2, q 0.004, down in 9 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX11]] (+0.59, fdr 1e-05), [[RASGRP1]] (+0.58, fdr 3e-05), [[AMPD3]] (+0.57, fdr 1e-05); moves opposite to [[ATF7]] (-0.53, fdr 2e-05), [[TMEM245]] (-0.50, fdr 4e-05), [[MSH3]] (-0.45, fdr 3e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CAMK4]] → it (grade B ⚠); 4 go from it, the strongest it → [[STX11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.17×** | +23.5 | 0e+00 | 27/36 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +9.0 | 6e-17 | 23/36 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +8.7 | 8e-16 | 24/35 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +8.3 | 2e-14 | 19/37 (A-427, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.65×** | +7.3 | 3e-11 | 21/38 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +7.0 | 3e-10 | 17/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +6.2 | 5e-08 | 18/37 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.6 | 1e-06 | 14/38 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.48×** | +5.4 | 4e-06 | 18/37 (HOP62, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.4 | 5e-06 | 15/31 (SW 900, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.2 | 8e-06 | 15/38 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 1e-04 | 13/37 (NCI-H460, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.7 | 1e-04 | 9/26 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.83×** | +4.5 | 2e-04 | 9/33 (J82, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.004 | 11/37 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.007 | 10/36 (C-33 A, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.011 | 14/37 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.707×** | -4.8 | 9e-04 | 15/32 (C32, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -4.5 | 0.002 | 11/17 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.570×** | -4.2 | 0.004 | 9/32 (C32, A498, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.743×** | -4.1 | 0.006 | 15/36 (C32, NCI-H2347, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.758×** | -4.0 | 0.008 | 6/38 (NCI-H1573, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.766×** | -3.8 | 0.012 | 7/32 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.792×** | -3.4 | 0.065 | 3/38 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.646×** | -3.3 | 0.072 | 8/34 (NCI-H460, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 62.8 | 0 | 10 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -12.5) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.228× (z -10.1) |
| [[A-172 (line)]] | wt | 18.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +15.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.230× (z -8.6) ⚠ toxic |
| [[J82 (line)]] | alt | 38.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[NCI-H460 (line)]] | wt | 15.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 8.85 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +17.7) | — |
| [[A498 (line)]] | wt | 11.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +16.9) | — |
| [[HS-578T (line)]] | alt | 16.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +15.8) | — |
| [[NCI-H2347 (line)]] | alt | 7.48 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +11.9) | [[Belumosudil (drug)]] 5 µM 0.147× (z -9.3) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -10.4) ⚠ toxic |
| [[A549 (line)]] | wt | 8.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SNU-423 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +14.4) | — |
| [[SW 900 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +9.7) | — |
| [[SW480 (line)]] | alt | 3.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX11]] | +0.59 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[RASGRP1]] | +0.58 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[AMPD3]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CPAMD8]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[S1PR2]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[MCPH1-AS1]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[GATM]] | +0.54 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[TRAF1]] | +0.54 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[TMEFF1]] | +0.53 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[CTTNBP2]] | +0.53 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[OBI1-AS1]] | +0.53 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[FGFR1]] | +0.52 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF7]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[TMEM245]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[MSH3]] | -0.45 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[DROSHA]] | -0.44 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[RTTN]] | -0.44 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[TYW1]] | -0.42 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[RBM6]] | -0.42 | -0.33 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK4]] | B | CAMK4 activity raises HLA-L-1's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 2.59× lower at baseline in the lines without CAMK4 | 0.050 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12 |
| [[GCNT4]] | B | GCNT4 activity raises HLA-L-1's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without GCNT4 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STX11]] | B | HLA-L-1 activity raises STX11's level | lines that do not express HLA-L-1 (10) vs lines expressing it (40) | 2.25× lower at baseline in the lines without HLA-L-1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, SETD1B; also absent: DNAAF9, NR3C1, RIMKLB; maybe low, not absent |
| [[GRIA4]] | B | HLA-L-1 activity raises GRIA4's level | lines that do not express HLA-L-1 (10) vs lines expressing it (40) | 1.03× lower at baseline in the lines without HLA-L-1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, SETD1B; also absent: DNAAF9, NR3C1, RIMKLB; maybe low, not absent |
| [[ATF7]] | B | HLA-L-1 activity raises ATF7's level | lines that do not express HLA-L-1 (10) vs lines expressing it (40) | 1.24× lower at baseline in the lines without HLA-L-1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, SETD1B; also absent: DNAAF9, NR3C1, RIMKLB; maybe low, not absent |
| [[NFATC1]] | C | HLA-L-1 activity raises NFATC1's level | lines that do not express HLA-L-1 (10) vs lines expressing it (40) | 2.89× lower at baseline in the lines without HLA-L-1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, SETD1B; also absent: DNAAF9, NR3C1, RIMKLB; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.426). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.4, -1.1); signed map (39.9, 11.1). **Vector** length 82.9, 18.4% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +23.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.0 | -4.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.1 |

## What is on record

> [!warning] No registry record
> HLA-L-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16580); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16580]; `tensor/DDL_lfc|DDL_z.npy` [16580]; `embed/gene_vectors.npy` [16580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16580 or target_col == 16580). Every well: [[HLA-L-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-L-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
