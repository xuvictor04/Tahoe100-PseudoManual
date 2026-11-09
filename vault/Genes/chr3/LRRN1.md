---
symbol: "LRRN1"
type: "gene"
col: 10665
ensembl_id: "ENSG00000175928"
name: "leucine rich repeat neuronal 1"
location: "3p26.2"
module: 14
arm: "+"
pooled_cpm: 3.15
n_lines_expressing: 19
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 27
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# LRRN1

*leucine rich repeat neuronal 1* — 3p26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.62× (z +14.6, q 3e-45, up in 11 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM: 0.622× (z -3.9, q 0.062, down in 1 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (A-172 0.0631×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CABLES1]] (+0.60, fdr 4e-05), [[LITAF]] (+0.58, fdr 3e-05), [[PSG4]] (+0.55, fdr 3e-05); moves opposite to [[RNGTT]] (-0.51, fdr 8e-05), [[S100A16]] (-0.49, fdr 5e-05), [[ATG16L1]] (-0.43, fdr 3e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 27 go from it, the strongest it → [[STAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.62×** | +14.6 | 3e-45 | 11/15 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +12.3 | 4e-32 | 10/14 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.90×** | +10.9 | 2e-25 | 1/11 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +10.1 | 6e-22 | 1/5 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +6.5 | 1e-08 | 3/7 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +5.8 | 7e-07 | 3/10 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +5.8 | 7e-07 | 9/14 (CFPAC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +5.6 | 2e-06 | 4/12 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +5.4 | 4e-06 | 1/10 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +5.3 | 6e-06 | 5/12 (SW480, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.31×** | +4.8 | 9e-05 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.79×** | +4.6 | 2e-04 | 5/13 (A-172, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +4.5 | 3e-04 | 8/13 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.3 | 8e-04 | 4/15 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.001 | 8/16 (J82, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +4.1 | 0.002 | 7/15 (SW1417, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.63×** | +3.9 | 0.003 | 3/13 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.004 | 6/15 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.004 | 4/16 (J82, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.90×** | +3.7 | 0.007 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.015 | 4/16 (A-172, BT-474, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.017 | 2/16 (J82, CFPAC-1) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.025 | 9/16 (A-172, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10665.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (A-172 0.0631×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.622×** | -3.9 | 0.062 | 1/16 (SW480) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.28 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +9.9) | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0631× (z -9.8) |
| [[BT-474 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 3.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +8.7) | — |
| [[A-427 (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.957 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.889 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CABLES1]] | +0.60 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[LITAF]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[PSG4]] | +0.55 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[MTUS1-DT]] | +0.53 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[KMO]] | +0.52 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[SLC4A4]] | +0.51 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[FOXC1]] | +0.51 | +0.56 / +0.28 | both halves | 3e-04 |  |
| [[IL6]] | +0.51 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[BMF]] | +0.51 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[FBXO32]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CTSO]] | +0.50 | +0.44 / +0.29 | both halves | 2e-04 |  |
| [[SLC49A4]] | +0.50 | +0.60 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | -0.51 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[S100A16]] | -0.49 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ATG16L1]] | -0.43 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[S100A14]] | -0.43 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[ANO1]] | -0.42 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[MOB3A]] | -0.41 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[GJB3]] | -0.41 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[NIBAN2]] | -0.41 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[TPM3]] | -0.41 | -0.44 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRRN1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[BDKRB2]] | B | BDKRB2 activity raises LRRN1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without BDKRB2 | 0.063 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[STEAP4]] | C | STEAP4 activity raises LRRN1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.78× lower at baseline in the lines without STEAP4 | 0.014 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[QPCT]] | C | QPCT activity raises LRRN1's level | lines that do not express QPCT (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without QPCT | 0.015 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81; co-absent with the target |
| [[MTUS1-DT]] | C | MTUS1-DT activity raises LRRN1's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without MTUS1-DT | 0.032 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3; co-absent with the target |
| [[GPNMB]] | C | GPNMB activity raises LRRN1's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without GPNMB | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[CFB]] | C | CFB activity raises LRRN1's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without CFB | 0.056 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG; co-absent with the target |
| [[IDO1]] | C | IDO1 activity raises LRRN1's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.72× lower at baseline in the lines without IDO1 | 0.069 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3; co-absent with the target |
| [[MTUS1]] | C | MTUS1 activity raises LRRN1's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 1.93× lower at baseline in the lines without MTUS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3; co-absent with the target |
| [[SLC40A1]] | C | SLC40A1 activity raises LRRN1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.98× lower at baseline in the lines without SLC40A1 | 0.070 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3; co-absent with the target |
| [[GRHL2]] | C | GRHL2 activity raises LRRN1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.00× lower at baseline in the lines without GRHL2 | 0.078 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 18, C 9. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAP2]] | B | LRRN1 activity raises STAP2's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.82× lower at baseline in the lines without LRRN1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[SERTAD4]] | B | LRRN1 activity raises SERTAD4's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.72× lower at baseline in the lines without LRRN1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[FBXO32]] | B | LRRN1 activity raises FBXO32's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.63× lower at baseline in the lines without LRRN1 | 0.011 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[RASGEF1B]] | B | LRRN1 activity raises RASGEF1B's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.07× lower at baseline in the lines without LRRN1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[TNFAIP2]] | B | LRRN1 activity raises TNFAIP2's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.03× lower at baseline in the lines without LRRN1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[ZHX2]] | B | LRRN1 activity raises ZHX2's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without LRRN1 | 0.053 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[PTPRK]] | B | LRRN1 activity raises PTPRK's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without LRRN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[SCIN]] | B | LRRN1 activity raises SCIN's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.71× lower at baseline in the lines without LRRN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[COL28A1]] | B | LRRN1 activity raises COL28A1's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.47× lower at baseline in the lines without LRRN1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[SATB1]] | B | LRRN1 activity raises SATB1's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.08× lower at baseline in the lines without LRRN1 | 0.064 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[BMF]] | B | LRRN1 activity raises BMF's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.52× lower at baseline in the lines without LRRN1 | 0.065 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[LITAF]] | B | LRRN1 activity raises LITAF's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.62× lower at baseline in the lines without LRRN1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.456). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.1, 2.0); signed map (47.3, 11.3). **Vector** length 32.3, 6.80% of its response variance represented; |z| ≥ 3 in 344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +14.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.9 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.3 | +10.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +0.8 | +1.1 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.0 | +3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.7 | -1.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.7 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat neuronal 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.2 — chr3:3,799,431-3,849,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FIGLER3 |
| Gene groups (HGNC) | I-set domain containing |
| Matched by | ensembl_id |

UniProt [Q6UXK5](https://www.uniprot.org/uniprotkb/Q6UXK5) carries no function annotation.

**Summary**, from NCBI Gene [57633](https://www.ncbi.nlm.nih.gov/gene/57633):

> Predicted to enable signaling receptor activity. Predicted to act upstream of or within positive regulation of synapse assembly. Predicted to be located in membrane. Predicted to be active in plasma membrane. Biomarker of stomach cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20980) · Entrez [57633](https://www.ncbi.nlm.nih.gov/gene/57633) · UniProt [Q6UXK5](https://www.uniprot.org/uniprotkb/Q6UXK5) · Ensembl [ENSG00000175928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175928)

## Data

Gene col 10665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10665); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10665]; `tensor/DDL_lfc|DDL_z.npy` [10665]; `embed/gene_vectors.npy` [10665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10665 or target_col == 10665). Every well: [[LRRN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
