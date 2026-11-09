---
symbol: "PDLIM3"
type: "gene"
col: 7815
ensembl_id: "ENSG00000154553"
name: "PDZ and LIM domain 3"
location: "4q35.1"
module: 61
arm: "+"
pooled_cpm: 9.05
n_lines_expressing: 32
n_dd_up: 31
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# PDLIM3

*PDZ and LIM domain 3* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.15× (z +21.6, q 0e+00, up in 20 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.886× (z -5.8, q 5e-06, down in 8 of 30 measured lines) ⚠ position not correctable. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.745× (z -5.5, q 1e-05, down in 15 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3GL2]] (+0.66, fdr 7e-06), [[PCSK2]] (+0.60, fdr 1e-05), [[TMEM47]] (+0.59, fdr 2e-05); moves opposite to [[ANAPC10]] (-0.54, fdr 2e-05), [[ERCC3]] (-0.53, fdr 3e-05), [[TRMT44]] (-0.52, fdr 5e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[STXBP5L]] → it (grade B ⚠); 5 go from it, the strongest it → [[ZFP36]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.15×** | +21.6 | 0e+00 | 20/23 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.23×** | +15.2 | 0e+00 | 25/27 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.29×** | +11.0 | 4e-26 | 22/29 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +10.6 | 3e-24 | 20/27 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.16×** | +10.3 | 9e-23 | 23/26 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +9.4 | 5e-19 | 17/24 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +9.2 | 2e-18 | 21/29 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +9.2 | 2e-18 | 19/28 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +8.3 | 5e-15 | 18/29 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.3 | 8e-15 | 12/24 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.8 | 4e-10 | 5/18 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +6.7 | 1e-09 | 13/29 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +5.8 | 3e-07 | 11/25 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.54×** | +5.6 | 1e-06 | 13/26 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +5.4 | 3e-06 | 10/26 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 6e-06 | 10/29 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7815.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.886× | -5.8 | 5e-06 | 8/30 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.745×** | -5.5 | 1e-05 | 15/28 (HepG2/C3A, SHP-77, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.568×** | -3.9 | 0.016 | 9/25 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.758×** | -3.7 | 0.033 | 3/28 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.607×** | -3.5 | 0.058 | 10/25 (SK-MEL-2, CFPAC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -3.3 | 0.077 | 6/25 (A498, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.02 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +14.4) | — |
| [[SW 900 (line)]] | alt | 9.54 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 18.0× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +15.8) | [[Docetaxel (drug)]] 0.05 µM 0.0736× (z -13.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 36.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 7.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +8.8) | — |
| [[A498 (line)]] | wt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 6.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +9.4) | — |
| [[J82 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -10.8) |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -10.8) |
| [[A-427 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.926 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3GL2]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[PCSK2]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TMEM47]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[STXBP5L]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ELOVL7]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[STX11]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[C11orf96]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[ELAVL2]] | +0.53 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[RGS7]] | +0.53 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[ENPP1]] | +0.53 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[SPTB]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[NTN1]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC10]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ERCC3]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TRMT44]] | -0.52 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[TYW1]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[GTF3C2]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PARGP1]] | -0.50 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[IPO11]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SAMM50]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[MIGA1]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[LRRC47]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[EDRF1]] | -0.47 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[COASY]] | -0.47 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STXBP5L]] | B | STXBP5L activity raises PDLIM3's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.88× lower at baseline in the lines without STXBP5L | 0.046 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[CHST8]] | B | CHST8 activity raises PDLIM3's level | lines that do not express CHST8 (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without CHST8 | 0.052 | ⚠ within organs, on part of the lines; also absent: PLEKHG4B, JAKMIP1, SNAP91 |
| [[RORB]] | C | RORB activity raises PDLIM3's level | lines that do not express RORB (27) vs lines expressing it (23) | 2.48× lower at baseline in the lines without RORB | 0.045 | ⚠ within organs, on part of the lines; also absent: JAM2, NEGR1, PTPRN; maybe low, not absent; co-absent with the target |
| [[C11orf96]] | C | C11orf96 activity raises PDLIM3's level | lines that do not express C11orf96 (17) vs lines expressing it (33) | 3.00× lower at baseline in the lines without C11orf96 | 0.057 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, ZNF569, PPP1R3C; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFP36]] | B | PDLIM3 activity lowers ZFP36's level | lines that do not express PDLIM3 (18) vs lines expressing it (32) | 1.37× higher at baseline in the lines without PDLIM3 | 0.078 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, SOX5, PTX3 |
| [[IVD]] | B | PDLIM3 activity lowers IVD's level | lines that do not express PDLIM3 (18) vs lines expressing it (32) | 1.08× higher at baseline in the lines without PDLIM3 | 0.080 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, SOX5, PTX3 |
| [[CLSTN2]] | B | PDLIM3 activity raises CLSTN2's level | lines that do not express PDLIM3 (18) vs lines expressing it (32) | 2.08× lower at baseline in the lines without PDLIM3 | 0.084 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, SOX5, PTX3 |
| [[FAM185A]] | B | PDLIM3 activity raises FAM185A's level | lines that do not express PDLIM3 (18) vs lines expressing it (32) | 1.11× lower at baseline in the lines without PDLIM3 | 0.096 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, SOX5, PTX3 |
| [[ZNF568]] | C | PDLIM3 activity raises ZNF568's level | lines that do not express PDLIM3 (18) vs lines expressing it (32) | 4.68× lower at baseline in the lines without PDLIM3 | 0.022 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, SOX5, PTX3; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.5, 32.8); signed map (33.8, 25.3). **Vector** length 58.7, 12.4% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +15.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +21.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +2.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.5 | -5.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -5.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | PDZ and LIM domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,500,660-185,535,507 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALP |
| Gene groups (HGNC) | LIM domain containing; PDZ domain containing |
| Hallmark sets | UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53GG5](https://www.uniprot.org/uniprotkb/Q53GG5) (PDZ and LIM domain protein 3):

> May play a role in the organization of actin filament arrays within muscle cells.

**Summary**, from NCBI Gene [27295](https://www.ncbi.nlm.nih.gov/gene/27295):

> The protein encoded by this gene contains a PDZ domain and a LIM domain, indicating that it may be involved in cytoskeletal assembly. In support of this, the encoded protein has been shown to bind the spectrin-like repeats of alpha-actinin-2 and to colocalize with alpha-actinin-2 at the Z lines of skeletal muscle. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. Aberrant alternative splicing of this gene may play a role in myotonic …

**Accessions** — [HGNC:20767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20767) · Entrez [27295](https://www.ncbi.nlm.nih.gov/gene/27295) · UniProt [Q53GG5](https://www.uniprot.org/uniprotkb/Q53GG5) · Ensembl [ENSG00000154553](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154553)

## Data

Gene col 7815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7815); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7815]; `tensor/DDL_lfc|DDL_z.npy` [7815]; `embed/gene_vectors.npy` [7815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7815 or target_col == 7815). Every well: [[PDLIM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDLIM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
