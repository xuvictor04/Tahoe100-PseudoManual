---
symbol: "TMEM40"
type: "gene"
col: 1539
ensembl_id: "ENSG00000088726"
name: "transmembrane protein 40"
location: "3p25.2"
module: 125
arm: "+"
pooled_cpm: 3.61
n_lines_expressing: 26
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# TMEM40

*transmembrane protein 40* — 3p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.85× (z +10.0, q 7e-21, up in 3 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.36× (z +9.4, q 2e-18, up in 9 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 0.713× (z -3.7, q 0.067, down in 9 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.114×, NCI-H23 0.0976×; ⚠ cell-cycle shift, explains ~87% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.461×; ⚠ position not correctable); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.146×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.189×); [[Binimetinib (drug)]] 0.05 µM in 1 line (BT-474 0.153×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREB5]] (+0.57, fdr 1e-05), [[OLFM2]] (+0.56, fdr 2e-05), [[LIMA1]] (+0.54, fdr 3e-05); moves opposite to [[PHB2]] (-0.54, fdr 2e-05), [[ANGEL2]] (-0.48, fdr 5e-05), [[APEX1]] (-0.45, fdr 7e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RPLP0P2]] → it (grade B ⚠); 10 go from it, the strongest it → [[EPHA2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.85×** | +10.0 | 7e-21 | 3/8 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +9.4 | 2e-18 | 9/21 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.93×** | +7.7 | 3e-12 | 3/10 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +7.2 | 1e-10 | 3/12 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.44×** | +6.9 | 6e-10 | 8/18 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.43×** | +6.9 | 6e-10 | 9/22 (SW480, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.3 | 9e-06 | 3/19 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +4.8 | 9e-05 | 11/24 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.77×** | +4.2 | 0.001 | 7/22 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.27×** | +4.2 | 0.002 | 4/16 (NCI-H23, NCI-H2030, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.22×** | +4.1 | 0.002 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.005 | 7/22 (LOX-IMVI, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.012 | 7/23 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.023 | 5/24 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +3.4 | 0.026 | 1/5 (SNU-423) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +3.3 | 0.035 | 4/22 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.087 | 8/19 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +3.0 | 0.089 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.50×** | +2.9 | 0.095 | 1/17 (NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1539.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.114×, NCI-H23 0.0976×; ⚠ cell-cycle shift, explains ~87% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.461×; ⚠ position not correctable); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.146×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.189×); [[Binimetinib (drug)]] 0.05 µM in 1 line (BT-474 0.153×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.713×** | -3.7 | 0.067 | 9/24 (LOX-IMVI, HT-29, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.876× | -3.7 | 0.067 | 5/24 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.623× | -3.4 | 0.14 | 5/24 (LoVo, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 20.4 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +16.1) | [[Adagrasib (drug)]] 0.05 µM 0.461× (z -12.4) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -10.6) |
| [[BT-474 (line)]] | alt | 12.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.27× (z +10.7) | [[Binimetinib (drug)]] 0.05 µM 0.153× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -12.2) ⚠ cell-cycle shift, explains ~87% of this change |
| [[NCI-H1573 (line)]] | alt | 6.24 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 17.1× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.177× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.8× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 5.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +9.7) | — |
| [[A-172 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREB5]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[OLFM2]] | +0.56 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[LIMA1]] | +0.54 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[NGF]] | +0.53 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[ARVCF]] | +0.53 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[GLIPR2]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CD163L1]] | +0.53 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[ATP6V0A1]] | +0.53 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[CTTNBP2NL]] | +0.53 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[TSPAN2]] | +0.52 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[CPA4]] | +0.51 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[BIK]] | +0.50 | +0.37 / +0.48 | both halves | 9e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHB2]] | -0.54 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[ANGEL2]] | -0.48 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[APEX1]] | -0.45 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[NCOA2]] | -0.44 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[ANP32A]] | -0.44 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[PMS2]] | -0.44 | -0.24 / -0.37 | both halves | 5e-04 |  |
| [[CNOT1]] | -0.44 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[MFSD14A]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[USF1]] | -0.43 | -0.24 / -0.39 | both halves | 4e-04 |  |
| [[NUP133]] | -0.43 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[ARID1B]] | -0.42 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[RBBP4]] | -0.41 | -0.42 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPLP0P2]] | B | RPLP0P2 activity lowers TMEM40's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 1.62× higher at baseline in the lines without RPLP0P2 | 0.024 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[UNC5A]] | B | UNC5A activity raises TMEM40's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 1.39× lower at baseline in the lines without UNC5A | 0.046 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN |
| [[EPHA2-AS1]] | B | EPHA2-AS1 activity raises TMEM40's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 1.93× lower at baseline in the lines without EPHA2-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2-AS1]] | B | TMEM40 activity raises EPHA2-AS1's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without TMEM40 | 0.047 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |
| [[GDPD5]] | B | TMEM40 activity raises GDPD5's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.57× lower at baseline in the lines without TMEM40 | 0.048 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |
| [[TICAM1]] | B | TMEM40 activity strengthens TICAM1's drug response | lines that do not express TMEM40 (24) vs lines expressing it (25) | the lines without TMEM40 respond 0.70× as strongly (z diff +1.53); strongest at Dinaciclib 0.5 µM: 0.80x vs 0.52x (z diff +3.1) | 0.050 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TICAM1]] | B | TMEM40 activity raises TICAM1's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.49× lower at baseline in the lines without TMEM40 | 0.065 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |
| [[LINC00592]] | B | TMEM40 activity raises LINC00592's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.39× lower at baseline in the lines without TMEM40 | 0.082 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |
| [[BIK]] | B | TMEM40 activity raises BIK's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.69× lower at baseline in the lines without TMEM40 | 0.089 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |
| [[ARVCF]] | B | TMEM40 activity raises ARVCF's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.36× lower at baseline in the lines without TMEM40 | 0.093 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |
| [[DUSP14]] | B | TMEM40 activity raises DUSP14's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.30× lower at baseline in the lines without TMEM40 | 0.095 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |
| [[RNF223]] | C | TMEM40 activity raises RNF223's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.81× lower at baseline in the lines without TMEM40 | 0.033 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent; co-absent with the target |
| [[LINC02945]] | C | TMEM40 activity raises LINC02945's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 2.20× lower at baseline in the lines without TMEM40 | 0.092 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.1, 10.4); signed map (30.6, 24.0). **Vector** length 48.5, 10.2% of its response variance represented; |z| ≥ 3 in 552 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +6.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.2 — chr3:12,733,528-12,769,457 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11036 |
| Matched by | ensembl_id |

UniProt [Q8WWA1](https://www.uniprot.org/uniprotkb/Q8WWA1) carries no function annotation.

**Summary**, from NCBI Gene [55287](https://www.ncbi.nlm.nih.gov/gene/55287):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25620) · Entrez [55287](https://www.ncbi.nlm.nih.gov/gene/55287) · UniProt [Q8WWA1](https://www.uniprot.org/uniprotkb/Q8WWA1) · Ensembl [ENSG00000088726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088726)

## Data

Gene col 1539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1539); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1539]; `tensor/DDL_lfc|DDL_z.npy` [1539]; `embed/gene_vectors.npy` [1539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1539 or target_col == 1539). Every well: [[TMEM40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
