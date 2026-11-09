---
symbol: "ZG16B"
type: "gene"
col: 8479
ensembl_id: "ENSG00000162078"
name: "zymogen granule protein 16B"
location: "16p13.3"
module: 141
arm: "+"
pooled_cpm: 3.15
n_lines_expressing: 33
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 18
direction_downstream: 5
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# ZG16B

*zymogen granule protein 16B* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.12× (z +8.0, q 1e-12, up in 4 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +6.4, q 3e-08, up in 8 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.494× (z -4.6, q 0.003, down in 17 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP4]] (+0.64, fdr 1e-05), [[MAP2K3]] (+0.62, fdr 1e-05), [[CLDN10-AS1]] (+0.61, fdr 7e-06); moves opposite to [[MAP4]] (-0.53, fdr 2e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[CLDN10-AS1]] → it (grade B ⚠); 5 go from it, the strongest it → [[KRT15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +8.0 | 1e-12 | 4/14 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +7.5 | 2e-11 | 2/4 (LS 180, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +6.4 | 3e-08 | 8/23 (LoVo, HS-578T, …) | top dose only | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.49×** | +5.9 | 6e-07 | 1/7 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +4.6 | 5e-04 | 6/29 (MIA PaCa-2, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +4.4 | 0.001 | 10/25 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.004 | 12/29 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +3.9 | 0.007 | 4/12 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +3.8 | 0.007 | 5/29 (LS 180, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.3 | 0.056 | 4/13 (AsPC-1, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.59×** | +3.2 | 0.060 | 4/24 (HepG2/C3A, SNU-423, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.080 | 2/29 (PANC-1, MIA PaCa-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.494×** | -4.6 | 0.003 | 17/29 (PANC-1, NCI-H23, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.561×** | -4.1 | 0.011 | 13/29 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.604×** | -3.5 | 0.081 | 11/29 (NCI-H23, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[RMC-6236 (drug)]] 5 µM |  | 0.415× | -3.2 | 0.18 | 7/28 (PANC-1, HepG2/C3A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.643× | -3.1 | 0.23 | 12/29 (LS 180, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 18.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0886× (z -11.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.208× (z -10.5) |
| [[PANC-1 (line)]] | alt | 4.31 | 0 | 2 | — | [[Binimetinib (drug)]] 5 µM 0.0771× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 18.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.10× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0856× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 5.44 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0605× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 2.99 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.311× (z -9.1) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 3.51 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.367× (z -9.8) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 2.43 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.355× (z -8.9) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 4.16 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0698× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.589 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.955 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.918 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP4]] | +0.64 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MAP2K3]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CLDN10-AS1]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PLK3]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ETV4]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SHH]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[EPHA2]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.57 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[LINC00589]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LIPH]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PRDM8]] | +0.57 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[EGR2]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP4]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 14, C 4. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN10-AS1]] | B | CLDN10-AS1 activity raises ZG16B's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without CLDN10-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[MUC5B]] | B | MUC5B activity raises ZG16B's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.20× lower at baseline in the lines without MUC5B | 0.019 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[LIPH]] | B | LIPH activity raises ZG16B's level | lines that do not express LIPH (27) vs lines expressing it (23) | 1.97× lower at baseline in the lines without LIPH | 0.020 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[TNFSF15]] | B | TNFSF15 activity raises ZG16B's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without TNFSF15 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[TESC]] | B | TESC activity raises ZG16B's level | lines that do not express TESC (23) vs lines expressing it (27) | 1.73× lower at baseline in the lines without TESC | 0.031 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[GDA]] | B | GDA activity raises ZG16B's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.80× lower at baseline in the lines without GDA | 0.032 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[TMEM154]] | B | TMEM154 activity raises ZG16B's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.39× lower at baseline in the lines without TMEM154 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[BCAN-AS1]] | B | BCAN-AS1 activity raises ZG16B's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without BCAN-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[LINC00589]] | B | LINC00589 activity raises ZG16B's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 1.46× lower at baseline in the lines without LINC00589 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8 |
| [[MUC5B]] | B | MUC5B activity weakens ZG16B's drug response | lines that do not express MUC5B (20) vs lines expressing it (9) | the lines without MUC5B respond 1.85× as strongly (z diff -0.62); strongest at Homoharringtonine 5 µM: 1.74x vs 0.36x (z diff -6.4) | 0.063 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; target measured in part of the lines; both ways; artifact flags |
| [[ATP2A3]] | B | ATP2A3 activity raises ZG16B's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.20× lower at baseline in the lines without ATP2A3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |
| [[TCN1]] | B | TCN1 activity raises ZG16B's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.35× lower at baseline in the lines without TCN1 | 0.093 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT15]] | B | ZG16B activity raises KRT15's level | lines that do not express ZG16B (17) vs lines expressing it (33) | 2.16× lower at baseline in the lines without ZG16B | 0.073 | ⚠ within organs, on part of the lines; also absent: KRT19, CYBA, MIR4713HG; maybe low, not absent |
| [[BCAN-AS1]] | B | ZG16B activity raises BCAN-AS1's level | lines that do not express ZG16B (17) vs lines expressing it (33) | 1.73× lower at baseline in the lines without ZG16B | 0.084 | ⚠ within organs, on part of the lines; also absent: KRT19, CYBA, MIR4713HG; maybe low, not absent |
| [[TRIM15]] | C | ZG16B activity raises TRIM15's level | lines that do not express ZG16B (17) vs lines expressing it (33) | 2.87× lower at baseline in the lines without ZG16B | 0.084 | ⚠ within organs, on part of the lines; also absent: KRT19, CYBA, MIR4713HG; maybe low, not absent; co-absent with the target |
| [[KRT19]] | C | ZG16B activity raises KRT19's level | lines that do not express ZG16B (17) vs lines expressing it (33) | 5.41× lower at baseline in the lines without ZG16B | 0.085 | ⚠ within organs, on part of the lines; also absent: KRT19, CYBA, MIR4713HG; maybe low, not absent; co-absent with the target |
| [[SHH]] | C | ZG16B activity raises SHH's level | lines that do not express ZG16B (17) vs lines expressing it (33) | 2.62× lower at baseline in the lines without ZG16B | 0.098 | ⚠ within organs, on part of the lines; also absent: KRT19, CYBA, MIR4713HG; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.9, 2.2); signed map (6.4, 39.2). **Vector** length 48.3, 8.68% of its response variance represented; |z| ≥ 3 in 664 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -4.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | zymogen granule protein 16B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,830,253-2,839,585 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRPE773, PRO1567, JCLN2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DA0](https://www.uniprot.org/uniprotkb/Q96DA0) (Pancreatic adenocarcinoma up-regulated factor):

> Functions as a lectin that binds to selective commensal dental plaque bacteria, such as Streptococcus vestibularis. Contributes to maintain homeostasis in the oral microbiome by capturing commensal microbes and regulating their growth using a mucin-assisted clearance mechanism. Plays an important role in pancreatic tumor progression and metastasis. Promotes pancreatic cancer cells migration and invasion through the TLR4/MyD88/NF-kappaB signaling pathway, without the involvement of the TLR4/TRIF …

**Summary**, from NCBI Gene [124220](https://www.ncbi.nlm.nih.gov/gene/124220):

> Enables proteoglycan binding activity. Involved in several processes, including defense response to bacterium; positive regulation of angiogenesis; and positive regulation of vascular permeability. Located in apicolateral plasma membrane; cytoplasm; and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30456) · Entrez [124220](https://www.ncbi.nlm.nih.gov/gene/124220) · UniProt [Q96DA0](https://www.uniprot.org/uniprotkb/Q96DA0) · Ensembl [ENSG00000162078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162078)

## Data

Gene col 8479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8479); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8479]; `tensor/DDL_lfc|DDL_z.npy` [8479]; `embed/gene_vectors.npy` [8479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8479 or target_col == 8479). Every well: [[ZG16B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZG16B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
