---
symbol: "TST"
type: "gene"
col: 4876
ensembl_id: "ENSG00000128311"
name: "thiosulfate sulfurtransferase"
location: "22q12.3"
module: 24
arm: "+"
pooled_cpm: 3.39
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TST

*thiosulfate sulfurtransferase* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.01× (z +11.7, q 6e-29, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.354× (z -7.8, q 2e-12, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (61 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 39 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF524]] (+0.63, fdr 1e-05), [[OXLD1]] (+0.58, fdr 2e-04), [[NUDT8]] (+0.57, fdr 4e-05); moves opposite to [[NONO]] (-0.48, fdr 0.001, ⚠ one half only (not replicated)), [[SRP9]] (-0.47, fdr 8e-04, ⚠ one half only (not replicated)), [[PTAR1]] (-0.47, fdr 0.002, ⚠ one half only (not replicated)), [[UBE2V1]] (-0.44, fdr 6e-04), [[DYNC1H1]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PRR15]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MPST]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +11.7 | 6e-29 | 27/32 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +8.8 | 4e-16 | 1/5 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.61×** | +7.2 | 1e-10 | 30/42 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.44×** | +6.7 | 3e-09 | 24/39 (HOP62, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.27×** | +6.2 | 8e-08 | 6/17 (AsPC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.22×** | +5.5 | 3e-06 | 2/7 (AsPC-1, CFPAC-1) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +5.0 | 5e-05 | 10/19 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +4.8 | 1e-04 | 12/26 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +4.5 | 4e-04 | 4/14 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.4 | 7e-04 | 12/41 (SW48, SW 900, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.76×** | +4.3 | 0.001 | 14/40 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.79×** | +4.2 | 0.001 | 11/30 (LS 180, A-172, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.001 | 10/41 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.8 | 0.005 | 6/30 (A549, HepG2/C3A, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.030 | 6/24 (HT-29, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.048 | 9/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.354×** | -7.8 | 2e-12 | 31/43 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.401×** | -6.9 | 1e-09 | 24/39 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.568×** | -4.3 | 0.003 | 18/39 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.347×** | -4.2 | 0.004 | 13/26 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -4.1 | 0.004 | 14/24 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.597×** | -3.7 | 0.022 | 16/39 (Panc 03.27, HCT15, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -3.2 | 0.091 | 12/36 (KATO III, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -3.2 | 0.091 | 10/37 (SW1417, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.66 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.128× (z -9.5) |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -9.0) ⚠ cell-cycle shift, explains ~77% of this change |
| [[HEC-1-A (line)]] | alt | 3.31 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0795× (z -8.9) |
| [[KATO III (line)]] | alt | 18.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0728× (z -13.3) |
| [[LoVo (line)]] | wt | 5.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0773× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.953 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 28 of them with an alert (⚠; 28 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF524]] | +0.63 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[OXLD1]] | +0.58 | +0.29 / +0.72 | both halves | 2e-04 |  |
| [[NUDT8]] | +0.57 | +0.40 / +0.63 | both halves | 4e-05 |  |
| [[TSTD1]] | +0.55 | +0.32 / +0.61 | both halves | 1e-04 | pathway: Degradation of cysteine and homocysteine; STRING 729 |
| [[C1orf122]] | +0.54 | +0.15 / +0.67 | ⚠ one half (not replicated) | 0.001 |  |
| [[TMEM54]] | +0.53 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[HDDC3]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[OCEL1]] | +0.53 | +0.26 / +0.64 | both halves | 3e-04 |  |
| [[AKAP1-DT]] | +0.53 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SP2-DT]] | +0.53 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[ABHD15]] | +0.52 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[MFSD3]] | +0.51 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[MILIP]] | +0.51 | +0.35 / +0.70 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NONO]] | -0.48 | -0.18 / -0.64 | ⚠ one half (not replicated) | 0.001 |  |
| [[SRP9]] | -0.47 | -0.19 / -0.55 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PTAR1]] | -0.47 | -0.14 / -0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[LIN7C]] | -0.45 | -0.00 / -0.62 | ⚠ one half (not replicated) | 0.009 |  |
| [[UBE2V1]] | -0.44 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[MRPL42]] | -0.44 | -0.07 / -0.56 | ⚠ one half (not replicated) | 0.004 |  |
| [[DYNC1H1]] | -0.44 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[DPY19L4]] | -0.44 | -0.01 / -0.62 | ⚠ one half (not replicated) | 0.008 |  |
| [[TMEM106B]] | -0.44 | -0.12 / -0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[RAB1B]] | -0.43 | -0.14 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[DHFR]] | -0.43 | -0.10 / -0.58 | ⚠ one half (not replicated) | 0.003 |  |
| [[MBTPS2]] | -0.43 | -0.06 / -0.58 | ⚠ one half (not replicated) | 0.004 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR15]] | B | PRR15 activity raises TST's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without PRR15 | 0.006 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[KDF1]] | B | KDF1 activity raises TST's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 2.04× lower at baseline in the lines without KDF1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[C11orf52]] | B | C11orf52 activity raises TST's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.86× lower at baseline in the lines without C11orf52 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[WFDC2]] | B | WFDC2 activity raises TST's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.98× lower at baseline in the lines without WFDC2 | 0.013 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[TOP2A]] | B | TOP2A activity lowers TST's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLDN3]] | B | CLDN3 activity raises TST's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without CLDN3 | 0.041 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[SPINT1]] | B | SPINT1 activity raises TST's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 1.81× lower at baseline in the lines without SPINT1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[CLDN7]] | B | CLDN7 activity raises TST's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 1.84× lower at baseline in the lines without CLDN7 | 0.050 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[WFDC2]] | B | WFDC2 activity strengthens TST's drug response | lines that do not express WFDC2 (33) vs lines expressing it (10) | the lines without WFDC2 respond 0.90× as strongly (z diff +0.11); strongest at Digitoxin 0.5 µM: 0.36x vs 0.26x (z diff +2.4) | 0.071 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPST]] | C | TST's natural level strengthens MPST's drug response | TST's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.15; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-45.4, -16.5); signed map (-11.0, -6.7). **Vector** length 42.7, 5.53% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.3 | +3.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.4 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | thiosulfate sulfurtransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:37,010,859-37,020,183 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RDS |
| Hallmark sets | UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE, ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Sulfide oxidation to sulfate; Degradation of cysteine and homocysteine; Sulfur amino acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16762](https://www.uniprot.org/uniprotkb/Q16762) (Thiosulfate sulfurtransferase):

> Catalyzes the transfer of sulfur ion from thiosulfate to cyanide, although other thiol compounds, besides cyanide, can act as sulfur ion acceptors (By similarity). It also has weak mercaptopyruvate sulfurtransferase (MST) activity (By similarity). Has a pivotal role in cyanide detoxification. Together with MRPL18, acts as a mitochondrial import factor for the cytosolic 5S rRNA. Only the nascent unfolded cytoplasmic form is able to bind to the 5S rRNA.

**Summary**, from NCBI Gene [7263](https://www.ncbi.nlm.nih.gov/gene/7263):

> This is one of two neighboring genes encoding similar proteins that each contain two rhodanese domains. The encoded protein is localized to the mitochondria and catalyzes the conversion of thiosulfate and cyanide to thiocyanate and sulfite. In addition, the protein interacts with 5S ribosomal RNA and facilitates its import into the mitochondria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:12388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12388) · Entrez [7263](https://www.ncbi.nlm.nih.gov/gene/7263) · UniProt [Q16762](https://www.uniprot.org/uniprotkb/Q16762) · Ensembl [ENSG00000128311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128311)

## Data

Gene col 4876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4876); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4876]; `tensor/DDL_lfc|DDL_z.npy` [4876]; `embed/gene_vectors.npy` [4876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4876 or target_col == 4876). Every well: [[TST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
