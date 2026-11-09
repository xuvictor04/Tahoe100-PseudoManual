---
symbol: "MARVELD3"
type: "gene"
col: 6453
ensembl_id: "ENSG00000140832"
name: "MARVEL domain containing 3"
location: "16q22.2"
module: 8
arm: "+"
pooled_cpm: 9.42
n_lines_expressing: 22
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 17
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MARVELD3

*MARVEL domain containing 3* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.53× (z +9.0, q 1e-16, up in 2 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +7.3, q 5e-11, up in 3 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.0652×, NCI-H1573 0.255×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0988×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.0507×); [[Gallic acid (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0615×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRG4]] (+0.61, fdr 7e-06), [[ZCCHC10]] (+0.60, fdr 2e-05), [[PLEKHM2]] (+0.53, fdr 5e-05); moves opposite to [[UCHL5]] (-0.50, fdr 4e-05), [[ASPH]] (-0.47, fdr 9e-05), [[ILF2]] (-0.47, fdr 6e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TMPRSS2]] → it (grade C ⚠); 17 go from it, the strongest it → [[RNF103]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +9.0 | 1e-16 | 2/12 (HepG2/C3A, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +7.8 | 2e-12 | 2/15 (HCT15, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.3 | 5e-11 | 3/19 (AsPC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +7.0 | 3e-10 | 11/17 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.6 | 4e-09 | 10/20 (BT-474, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.8 | 6e-07 | 2/16 (LoVo, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +5.5 | 3e-06 | 6/19 (BT-474, AsPC-1, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +4.5 | 4e-04 | 11/20 (HT-29, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.9 | 0.006 | 4/20 (SW48, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.006 | 2/20 (SW480, LS 180) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.012 | 8/20 (BT-474, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.078 | 4/20 (NCI-H1573, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.1 | 0.089 | 4/19 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.099 | 3/20 (BT-474, SW48, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.099 | 6/20 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CFPAC-1 0.0652×, NCI-H1573 0.255×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0988×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.0507×); [[Gallic acid (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0615×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 42.1 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 5.34× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0988× (z -16.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0652× (z -13.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.125× (z -8.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 2.64 | 0 | 1 | — | [[Gallic acid (drug)]] 0.05 µM 0.0615× (z -8.8) |
| [[RKO (line)]] | wt | 4.61 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0401× (z -10.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW48 (line)]] | wt | 22.9 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0507× (z -13.0) |
| [[A-172 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.881 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRG4]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ZCCHC10]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[PLEKHM2]] | +0.53 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[SLC49A4]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[HDHD3]] | +0.52 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[RAB9A]] | +0.52 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[C11orf52]] | +0.48 | +0.32 / +0.61 | both halves | 2e-04 |  |
| [[LAMTOR4]] | +0.48 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[FOXC1]] | +0.48 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[RRAGC]] | +0.47 | +0.32 / +0.54 | both halves | 1e-04 |  |
| [[CDX2]] | +0.47 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[BEND7]] | +0.47 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UCHL5]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ASPH]] | -0.47 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[ILF2]] | -0.47 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[BPNT2]] | -0.46 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[ARHGAP4]] | -0.46 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[LRRC59]] | -0.45 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[CCAR2]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ANXA2]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[G6PD]] | -0.44 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[STT3A]] | -0.44 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[AMPD2]] | -0.43 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[GOLGA3]] | -0.43 | -0.44 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS2]] | C | TMPRSS2 activity raises MARVELD3's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 6.77× lower at baseline in the lines without TMPRSS2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[DAPP1]] | C | DAPP1 activity raises MARVELD3's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 5.21× lower at baseline in the lines without DAPP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[MTUS1-DT]] | C | MTUS1-DT activity raises MARVELD3's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 3.96× lower at baseline in the lines without MTUS1-DT | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3; co-absent with the target |
| [[RASSF6]] | C | RASSF6 activity raises MARVELD3's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 4.31× lower at baseline in the lines without RASSF6 | 0.005 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6; co-absent with the target |
| [[C11orf52]] | C | C11orf52 activity raises MARVELD3's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 3.58× lower at baseline in the lines without C11orf52 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39; co-absent with the target |
| [[PRRG4]] | C | PRRG4 activity raises MARVELD3's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 3.65× lower at baseline in the lines without PRRG4 | 0.021 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises MARVELD3's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 4.23× lower at baseline in the lines without TRIM31 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 9, C 8. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF103]] | B | MARVELD3 activity raises RNF103's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without MARVELD3 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[STX19]] | B | MARVELD3 activity raises STX19's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without MARVELD3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[STAP2]] | B | MARVELD3 activity raises STAP2's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 2.42× lower at baseline in the lines without MARVELD3 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[AMPD2]] | B | MARVELD3 activity lowers AMPD2's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.96× higher at baseline in the lines without MARVELD3 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[PRPF8]] | B | MARVELD3 activity lowers PRPF8's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.18× higher at baseline in the lines without MARVELD3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[LITAF]] | B | MARVELD3 activity raises LITAF's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.49× lower at baseline in the lines without MARVELD3 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | MARVELD3 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express MARVELD3 (28) vs lines expressing it (20) | the lines without MARVELD3: 0.84× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[DSTYK]] | B | MARVELD3 activity lowers DSTYK's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.39× higher at baseline in the lines without MARVELD3 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[BPNT2]] | B | MARVELD3 activity lowers BPNT2's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.39× higher at baseline in the lines without MARVELD3 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[MARVELD2]] | C | MARVELD3 activity raises MARVELD2's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 4.42× lower at baseline in the lines without MARVELD3 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2; co-absent with the target |
| [[DAPP1]] | C | MARVELD3 activity raises DAPP1's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 4.95× lower at baseline in the lines without MARVELD3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2; co-absent with the target |
| [[PRRG4]] | C | MARVELD3 activity raises PRRG4's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 4.48× lower at baseline in the lines without MARVELD3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.283). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.8, 7.7); signed map (-3.4, -9.1). **Vector** length 48.4, 12.8% of its response variance represented; |z| ≥ 3 in 298 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +6.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +7.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.4 | +2.8 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Lonafarnib (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | MARVEL domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:71,626,161-71,642,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MRVLDC3 |
| Gene groups (HGNC) | MARVEL domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A59](https://www.uniprot.org/uniprotkb/Q96A59) (MARVEL domain-containing protein 3):

> As a component of tight junctions, plays a role in paracellular ion conductivity.

**Summary**, from NCBI Gene [91862](https://www.ncbi.nlm.nih.gov/gene/91862):

> Enables mitogen-activated protein kinase kinase kinase binding activity. Involved in bicellular tight junction assembly. Acts upstream of or within several processes, including negative regulation of JNK cascade; negative regulation of epithelial cell migration; and negative regulation of epithelial cell proliferation. Located in bicellular tight junction and cytoplasmic vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30525) · Entrez [91862](https://www.ncbi.nlm.nih.gov/gene/91862) · UniProt [Q96A59](https://www.uniprot.org/uniprotkb/Q96A59) · Ensembl [ENSG00000140832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140832)

## Data

Gene col 6453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6453); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6453]; `tensor/DDL_lfc|DDL_z.npy` [6453]; `embed/gene_vectors.npy` [6453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6453 or target_col == 6453). Every well: [[MARVELD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARVELD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
