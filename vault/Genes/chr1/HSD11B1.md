---
symbol: "HSD11B1"
type: "gene"
col: 3928
ensembl_id: "ENSG00000117594"
name: "hydroxysteroid 11-beta dehydrogenase 1"
location: "1q32.2"
module: 104
arm: "+"
pooled_cpm: 4.47
n_lines_expressing: 16
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 14
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# HSD11B1

*hydroxysteroid 11-beta dehydrogenase 1* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.56× (z +10.8, q 3e-24, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.17× (z +8.0, q 1e-13, up in 12 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.295×, NCI-H2347 0.283×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.279×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0549×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCN]] (+0.74, fdr 7e-06), [[PID1]] (+0.69, fdr 7e-06), [[LPAR1]] (+0.66, fdr 7e-06); moves opposite to [[LRIG1]] (-0.45, fdr 9e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LRIG1]] → it (grade B ⚠); 14 go from it, the strongest it → [[STAT4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.56×** | +10.8 | 3e-24 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.35×** | +8.9 | 1e-16 | 1/9 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.62×** | +8.8 | 4e-16 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.17×** | +8.0 | 1e-13 | 12/13 (HOP62, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +7.4 | 2e-11 | 2/12 (HOP62, A498) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.69×** | +7.3 | 3e-11 | 10/11 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +5.6 | 2e-06 | 2/10 (A498, HOP62) | top dose only | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.0 | 5e-05 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +4.7 | 1e-04 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.81×** | +4.3 | 8e-04 | 5/11 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +4.1 | 0.002 | 1/10 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.019 | 0/11 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.95×** | +3.5 | 0.020 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.022 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.1 | 0.069 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.069 | 2/10 (NCI-H1792, A498) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.089 | 2/11 (HOP62, A-172) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.50×** | +3.0 | 0.093 | 3/11 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3928.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.295×, NCI-H2347 0.283×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.279×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0549×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.601× | -3.6 | 0.16 | 2/11 (NCI-H1792, hTERT-HPNE) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.644× | -3.3 | 0.32 | 1/13 (H4) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 139 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -12.7) |
| [[HOP62 (line)]] | alt | 3.63 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.31× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 6.17 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0510× (z -9.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0549× (z -11.2) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.2) |
| [[A-172 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.575 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCN]] | +0.74 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PID1]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LPAR1]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[DNER]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[CACNA1C]] | +0.59 | +0.33 / +0.66 | both halves | 1e-04 | **novel candidate** |
| [[IRAK3]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CPM]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[DAAM2]] | +0.56 | +0.37 / +0.69 | both halves | 9e-05 |  |
| [[MGP]] | +0.56 | +0.41 / +0.62 | both halves | 4e-05 | **novel candidate** |
| [[ITGA10]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[IL1R1]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[ITGA8]] | +0.56 | +0.41 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIG1]] | -0.45 | -0.36 / -0.40 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRIG1]] | B | LRIG1 activity raises HSD11B1's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without LRIG1 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADAMTS9]] | B | ADAMTS9 activity raises HSD11B1's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without ADAMTS9 | 0.074 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[TLR2]] | C | TLR2 activity raises HSD11B1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without TLR2 | 0.015 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; co-absent with the target |
| [[CCBE1]] | C | CCBE1 activity raises HSD11B1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.48× lower at baseline in the lines without CCBE1 | 0.043 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1; co-absent with the target |
| [[TREM1]] | C | TREM1 activity raises HSD11B1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.31× lower at baseline in the lines without TREM1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 7, C 7. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAT4]] | B | HSD11B1 activity raises STAT4's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.18× lower at baseline in the lines without HSD11B1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[ADAMTS9]] | B | HSD11B1 activity raises ADAMTS9's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without HSD11B1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[LRIG1]] | B | HSD11B1 activity raises LRIG1's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 1.75× lower at baseline in the lines without HSD11B1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[PRDM1]] | B | HSD11B1 activity raises PRDM1's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.52× lower at baseline in the lines without HSD11B1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[ITGA5]] | B | HSD11B1 activity raises ITGA5's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 3.67× lower at baseline in the lines without HSD11B1 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[ABLIM3]] | B | HSD11B1 activity raises ABLIM3's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.74× lower at baseline in the lines without HSD11B1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[HIF1A]] | B | HSD11B1 activity raises HIF1A's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 1.65× lower at baseline in the lines without HSD11B1 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[PTPRM]] | C | HSD11B1 activity raises PTPRM's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 3.96× lower at baseline in the lines without HSD11B1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA; co-absent with the target |
| [[LOX]] | C | HSD11B1 activity raises LOX's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 9.12× lower at baseline in the lines without HSD11B1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA; co-absent with the target |
| [[TLR2]] | C | HSD11B1 activity raises TLR2's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without HSD11B1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA; co-absent with the target |
| [[SAA2-SAA4]] | C | HSD11B1 activity raises SAA2-SAA4's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.00× lower at baseline in the lines without HSD11B1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA; co-absent with the target |
| [[CCBE1]] | C | HSD11B1 activity raises CCBE1's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 3.26× lower at baseline in the lines without HSD11B1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 16.5); signed map (18.5, 32.9). **Vector** length 40.5, 12.2% of its response variance represented; |z| ≥ 3 in 362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +8.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.5 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.5 | +0.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | hydroxysteroid 11-beta dehydrogenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2 — chr1:209,686,178-209,734,949 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR26C1; previously HSD11B, HSD11 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | XENOBIOTIC_METABOLISM, KRAS_SIGNALING_UP |
| Reactome | 5 pathways, smallest: Prednisone ADME; Metabolism of steroid hormones; Drug ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P28845](https://www.uniprot.org/uniprotkb/P28845) (11-beta-hydroxysteroid dehydrogenase 1):

> Controls the reversible conversion of biologically active glucocorticoids such as cortisone to cortisol, and 11-dehydrocorticosterone to corticosterone in the presence of NADP(H). Participates in the corticosteroid receptor-mediated anti-inflammatory response, as well as metabolic and homeostatic processes. Plays a role in the secretion of aqueous humor in the eye, maintaining a normotensive, intraocular environment. Bidirectional in vitro, predominantly functions as a reductase in vivo, …

**Summary**, from NCBI Gene [3290](https://www.ncbi.nlm.nih.gov/gene/3290):

> The protein encoded by this gene is a microsomal enzyme that catalyzes the conversion of the stress hormone cortisol to the inactive metabolite cortisone. In addition, the encoded protein can catalyze the reverse reaction, the conversion of cortisone to cortisol. Too much cortisol can lead to central obesity, and a particular variation in this gene has been associated with obesity and insulin resistance in children. Mutations in this gene and H6PD (hexose-6-phosphate dehydrogenase (glucose …

**Accessions** — [HGNC:5208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5208) · Entrez [3290](https://www.ncbi.nlm.nih.gov/gene/3290) · UniProt [P28845](https://www.uniprot.org/uniprotkb/P28845) · Ensembl [ENSG00000117594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117594)

## Data

Gene col 3928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3928); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3928]; `tensor/DDL_lfc|DDL_z.npy` [3928]; `embed/gene_vectors.npy` [3928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3928 or target_col == 3928). Every well: [[HSD11B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD11B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
