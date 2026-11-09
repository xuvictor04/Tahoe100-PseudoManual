---
symbol: "PRKCH-AS1"
type: "gene"
col: 14491
ensembl_id: "ENSG00000247287"
name: "PRKCH antisense RNA 1"
location: "14q23.1"
module: 44
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 16
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 27
direction_downstream: 34
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PRKCH-AS1

*PRKCH antisense RNA 1* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.26× (z +15.7, q 0e+00, up in 11 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.176×, HT-29 0.120×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.0517×; ⚠ toxic); [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.0864×; ⚠ cell-cycle shift, explains ~14% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.260×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.181×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS15-AS1]] (+0.63, fdr 1e-05), [[GRHL2]] (+0.63, fdr 1e-05), [[OVOL2]] (+0.60, fdr 2e-05); moves opposite to [[SH3PXD2B]] (-0.47, fdr 2e-04), [[CFAP20DC]] (-0.44, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 34 go from it, the strongest it → [[PRKCH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.26×** | +15.7 | 0e+00 | 11/13 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.01×** | +11.9 | 3e-30 | 2/5 (NCI-H2347, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.66×** | +10.0 | 4e-21 | 1/9 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +7.9 | 6e-13 | 1/6 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +6.5 | 6e-09 | 8/13 (Panc 03.27, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +6.5 | 6e-09 | 7/13 (Panc 03.27, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +6.5 | 7e-09 | 7/13 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.3 | 3e-08 | 5/14 (BT-474, NCI-H2347, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.66×** | +5.3 | 6e-06 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.6 | 2e-04 | 3/13 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.3 | 7e-04 | 2/10 (LS 180, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +4.2 | 0.001 | 1/13 (BT-474) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +4.2 | 0.001 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.84×** | +4.2 | 0.001 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +3.9 | 0.003 | 5/13 (Panc 03.27, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.003 | 5/14 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.92×** | +3.6 | 0.013 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.021 | 5/13 (HCT15, LS 180, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.021 | 1/13 (BT-474) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.052 | 0/13 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +3.0 | 0.056 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.073 | 0/14 | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.084 | 0/13 | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.176×, HT-29 0.120×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.0517×; ⚠ toxic); [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.0864×; ⚠ cell-cycle shift, explains ~14% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.260×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.181×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 14.0 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0517× (z -14.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.181× (z -8.5) |
| [[LoVo (line)]] | wt | 17.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -8.7) |
| [[LS 180 (line)]] | wt | 7.65 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0763× (z -11.3) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.702 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS15-AS1]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 | same gene group |
| [[GRHL2]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[OVOL2]] | +0.60 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[MUC12]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[LINC01133]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[STEAP4]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[KBTBD12]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[CLIC5]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[EDN1]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[C4orf19]] | +0.54 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[CRACDL]] | +0.53 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[TNFSF15]] | +0.53 | +0.50 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.47 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[CFAP20DC]] | -0.44 | -0.41 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 4, C 23. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRKCH-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL16A1]] | B | COL16A1 activity raises PRKCH-AS1's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without COL16A1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises PRKCH-AS1's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without HTR1D | 0.058 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[PLAAT4]] | B | PLAAT4 activity raises PRKCH-AS1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without PLAAT4 | 0.062 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[C6orf132]] | C | C6orf132 activity raises PRKCH-AS1's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 2.81× lower at baseline in the lines without C6orf132 | 0.003 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |
| [[GRHL2]] | C | GRHL2 activity raises PRKCH-AS1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 3.39× lower at baseline in the lines without GRHL2 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises PRKCH-AS1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.84× lower at baseline in the lines without STEAP4 | 0.006 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[PRR15L]] | C | PRR15L activity raises PRKCH-AS1's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 3.43× lower at baseline in the lines without PRR15L | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881; co-absent with the target |
| [[PLEKHG6]] | C | PLEKHG6 activity raises PRKCH-AS1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.77× lower at baseline in the lines without PLEKHG6 | 0.006 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises PRKCH-AS1's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 4.06× lower at baseline in the lines without FAM3D | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[PRR15]] | C | PRR15 activity raises PRKCH-AS1's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.71× lower at baseline in the lines without PRR15 | 0.008 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C; co-absent with the target |
| [[VIPR1]] | C | VIPR1 activity raises PRKCH-AS1's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 2.55× lower at baseline in the lines without VIPR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 11, C 23. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCH]] | B | PRKCH-AS1 activity raises PRKCH's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 3.14× lower at baseline in the lines without PRKCH-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[PLAAT4]] | B | PRKCH-AS1 activity raises PLAAT4's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without PRKCH-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[SLC37A1]] | B | PRKCH-AS1 activity raises SLC37A1's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 3.49× lower at baseline in the lines without PRKCH-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[SMIM14]] | B | PRKCH-AS1 activity raises SMIM14's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 1.87× lower at baseline in the lines without PRKCH-AS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[STX19]] | B | PRKCH-AS1 activity raises STX19's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 2.14× lower at baseline in the lines without PRKCH-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[GNA14]] | B | PRKCH-AS1 activity raises GNA14's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 1.93× lower at baseline in the lines without PRKCH-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| cells under [[Afatinib (drug)]] 0.5 µM | B | PRKCH-AS1 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express PRKCH-AS1 (34) vs lines expressing it (14) | the lines without PRKCH-AS1: 1.15× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[MFSD6]] | B | PRKCH-AS1 activity raises MFSD6's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without PRKCH-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[C4orf19]] | B | PRKCH-AS1 activity raises C4orf19's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without PRKCH-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | PRKCH-AS1 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express PRKCH-AS1 (34) vs lines expressing it (14) | the lines without PRKCH-AS1: 0.79× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[PCAT1]] | B | PRKCH-AS1 activity raises PCAT1's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without PRKCH-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[C11orf52]] | C | PRKCH-AS1 activity raises C11orf52's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 2.68× lower at baseline in the lines without PRKCH-AS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.437). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.9, 50.6); signed map (57.4, 1.6). **Vector** length 33.7, 8.28% of its response variance represented; |z| ≥ 3 in 274 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +15.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.7 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.5 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -0.9 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | PRKCH antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q23.1 — chr14:61,294,909-61,322,838 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55588) · Entrez [121233923](https://www.ncbi.nlm.nih.gov/gene/121233923) · Ensembl [ENSG00000247287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247287)

## Data

Gene col 14491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14491); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14491]; `tensor/DDL_lfc|DDL_z.npy` [14491]; `embed/gene_vectors.npy` [14491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14491 or target_col == 14491). Every well: [[PRKCH-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCH-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
