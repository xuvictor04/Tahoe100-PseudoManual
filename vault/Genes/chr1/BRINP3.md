---
symbol: "BRINP3"
type: "gene"
col: 8559
ensembl_id: "ENSG00000162670"
name: "BMP/retinoic acid inducible neural specific 3"
location: "1q31.1"
module: 9
arm: "+"
pooled_cpm: 4.92
n_lines_expressing: 18
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 16
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# BRINP3

*BMP/retinoic acid inducible neural specific 3* — 1q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.98× (z +20.4, q 0e+00, up in 5 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK10]] (+0.65, fdr 7e-06), [[CDH18]] (+0.64, fdr 7e-06), [[ADGRL3]] (+0.64, fdr 1e-05); moves opposite to [[TBC1D16]] (-0.56, fdr 3e-05), [[FBH1]] (-0.56, fdr 3e-05), [[AXIN1]] (-0.55, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 16 go from it, the strongest it → [[KLHL13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.98×** | +20.4 | 0e+00 | 5/11 (SNU-423, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +9.3 | 3e-18 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.66×** | +8.8 | 3e-16 | 5/15 (BT-474, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +8.7 | 5e-16 | 1/8 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +8.1 | 5e-14 | 1/6 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +7.6 | 2e-12 | 8/15 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +7.4 | 1e-11 | 8/15 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +5.8 | 4e-07 | 7/15 (NCI-H23, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.5 | 3e-06 | 3/16 (SNU-423, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +5.1 | 2e-05 | 5/13 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +4.9 | 4e-05 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.68×** | +4.6 | 2e-04 | 7/15 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.91×** | +4.1 | 0.002 | 1/7 (SK-MEL-2) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.008 | 0/13 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.6 | 0.012 | 0/9 | top dose only | cell-cycle shift (explains ~1% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.033 | 1/11 (LOX-IMVI) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.035 | 5/15 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.035 | 1/14 (SNU-423) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.036 | 1/13 (SNU-423) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.046 | 3/15 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.058 | 2/13 (MIA PaCa-2, SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 95.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.76× (z +9.5) ⚠ position not correctable | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.39× (z +10.0) ⚠ position not correctable | — |
| [[SNU-423 (line)]] | alt | 4.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.02× (z +10.1) | — |
| [[A-172 (line)]] | wt | 0.922 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.917 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.870 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.772 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK10]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CDH18]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | STRING 410 |
| [[ADGRL3]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CRISPLD1]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ARHGEF26-AS1]] | +0.61 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LINC01122]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[GRID2]] | +0.60 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CA11]] | +0.60 | +0.49 / +0.49 | both halves | 2e-05 |  |
| [[LINC02211]] | +0.60 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CADM2]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[IGSF1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CDH8]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D16]] | -0.56 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[FBH1]] | -0.56 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[AXIN1]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[CCM2]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[NTAQ1]] | -0.50 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[TMEM181]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BRINP3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADGRL3]] | C | ADGRL3 activity raises BRINP3's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without ADGRL3 | 0.046 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises BRINP3's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without CDH18 | 0.063 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises BRINP3's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 1.90× lower at baseline in the lines without KCNH7 | 0.076 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises BRINP3's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 1.74× lower at baseline in the lines without CDH12 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 4, C 12. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL13]] | B | BRINP3 activity raises KLHL13's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without BRINP3 | 0.038 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent |
| [[AGBL4]] | B | BRINP3 activity raises AGBL4's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.32× lower at baseline in the lines without BRINP3 | 0.064 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent |
| [[MAPK10]] | B | BRINP3 activity raises MAPK10's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.41× lower at baseline in the lines without BRINP3 | 0.079 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent |
| [[NXPH1]] | B | BRINP3 activity raises NXPH1's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without BRINP3 | 0.093 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent |
| [[MIR2052HG]] | C | BRINP3 activity raises MIR2052HG's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 3.61× lower at baseline in the lines without BRINP3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[ERBB4]] | C | BRINP3 activity raises ERBB4's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 4.35× lower at baseline in the lines without BRINP3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[ADGRL3]] | C | BRINP3 activity raises ADGRL3's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 3.31× lower at baseline in the lines without BRINP3 | 0.025 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | BRINP3 activity raises FUT9's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.64× lower at baseline in the lines without BRINP3 | 0.027 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[NCAM2]] | C | BRINP3 activity raises NCAM2's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 4.11× lower at baseline in the lines without BRINP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[ZFHX4-AS1]] | C | BRINP3 activity raises ZFHX4-AS1's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without BRINP3 | 0.055 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[CDH18]] | C | BRINP3 activity raises CDH18's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.88× lower at baseline in the lines without BRINP3 | 0.059 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[CDH8]] | C | BRINP3 activity raises CDH8's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 1.87× lower at baseline in the lines without BRINP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.2, 32.6); signed map (40.7, 34.0). **Vector** length 29.7, 5.87% of its response variance represented; |z| ≥ 3 in 376 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.8 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.8 | +2.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.0 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.8 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | BMP/retinoic acid inducible neural specific 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.1 — chr1:190,097,658-190,478,404 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DBCCR1L, DBCCR1L1; previously FAM5C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76B58](https://www.uniprot.org/uniprotkb/Q76B58) (BMP/retinoic acid-inducible neural-specific protein 3):

> Inhibits neuronal cell proliferation by negative regulation of the cell cycle transition. Promotes pituitary gonadotrope cell proliferation, migration and invasion, when overexpressed. May play a role in cell pituitary tumor development.

**Summary**, from NCBI Gene [339479](https://www.ncbi.nlm.nih.gov/gene/339479):

> This gene is overexpressed in pituitary tumors but is underexpressed in tongue squamous cell carcinomas, ulcerative colitis, and peri-implantitis. Polymorphisms that increase expression of this gene have been shown to increase vascular inflammation, and an association of this gene with myocardial infarction has been demonstrated. Finally, hypermethylation of this gene may find usefulness as a biomarker for gastric cancer. Two transcript variants encoding different isoforms have been found for …

**Accessions** — [HGNC:22393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22393) · Entrez [339479](https://www.ncbi.nlm.nih.gov/gene/339479) · UniProt [Q76B58](https://www.uniprot.org/uniprotkb/Q76B58) · Ensembl [ENSG00000162670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162670)

## Data

Gene col 8559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8559); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8559]; `tensor/DDL_lfc|DDL_z.npy` [8559]; `embed/gene_vectors.npy` [8559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8559 or target_col == 8559). Every well: [[BRINP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRINP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
