---
symbol: "PI4KAP1-1"
type: "gene"
col: 16474
ensembl_id: "ENSG00000290425"
name: ""
location: ""
module: 131
arm: "+"
pooled_cpm: 5.5
n_lines_expressing: 24
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# PI4KAP1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.17× (z +8.2, q 1e-13, up in 14 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.91× (z +6.9, q 1e-09, up in 8 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (MIA PaCa-2 0.0988×, SNU-423 0.146×, KATO III 0.144×, HS-578T 0.128×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.113×, SNU-423 0.0936×, SW480 0.161×, HS-578T 0.112×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.184×, SNU-423 0.235×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.110×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.0923×); [[Belumosudil (drug)]] 5 µM in 1 line (COLO 205 0.116×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PI4KAP1]] (+0.74, fdr 7e-06, ⚠ same locus), [[CBFA2T2]] (+0.70, fdr 3e-05), [[DDT]] (+0.66, fdr 3e-05), [[VKORC1]] (+0.63, fdr 1e-05); moves opposite to [[RNF6]] (-0.65, fdr 2e-05), [[PSME3IP1]] (-0.63, fdr 4e-05), [[CYREN]] (-0.62, fdr 1e-04).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PI4KAP1]] → it (grade C ⚠); 5 go from it, the strongest it → [[PMEL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +8.2 | 1e-13 | 14/20 (BT-474, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.4 | 5e-11 | 1/8 (NCI-H2030) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +6.9 | 1e-09 | 8/21 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.36×** | +4.6 | 7e-04 | 0/21 | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +4.5 | 7e-04 | 11/22 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 8e-04 | 9/20 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pentoxifylline (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.1 | 0.003 | 0/20 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.003 | 6/20 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.003 | 6/21 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.9 | 0.006 | 7/17 (NCI-H2030, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +3.8 | 0.008 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pentoxifylline (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.035 | 0/21 | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.073 | 1/19 (BT-474) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16474.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (MIA PaCa-2 0.0988×, SNU-423 0.146×, KATO III 0.144×, HS-578T 0.128×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.113×, SNU-423 0.0936×, SW480 0.161×, HS-578T 0.112×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.184×, SNU-423 0.235×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.110×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.0923×); [[Belumosudil (drug)]] 5 µM in 1 line (COLO 205 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.726× | -3.4 | 0.33 | 9/20 (SW48, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.743× | -3.1 | 0.51 | 11/20 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Mozavaptan (drug)]] 0.05 µM |  | 0.739× | -3.0 | 0.51 | 12/20 (KATO III, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0936× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -11.4) |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0863× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0923× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0988× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[KATO III (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[LoVo (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SW48 (line)]] | wt | 13.3 | 0 | 1 | — | [[Posaconazole (drug)]] 0.05 µM 0.0682× (z -8.7) |
| [[SW480 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.881 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.942 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PI4KAP1]] | +0.74 | +0.79 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CBFA2T2]] | +0.70 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[DDT]] | +0.66 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[VKORC1]] | +0.63 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[STK32C]] | +0.62 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PI4KAP2]] | +0.62 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[SNHG25]] | +0.61 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[COX6A1]] | +0.61 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[ABCB9]] | +0.61 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SUFU]] | +0.60 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[LLGL2]] | +0.60 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[KYAT1]] | +0.60 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[RPLP2]] | +0.60 | +0.55 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | -0.65 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[PSME3IP1]] | -0.63 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[CYREN]] | -0.62 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[TASOR]] | -0.61 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.61 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[PDAP1]] | -0.60 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.59 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MAGOHB]] | -0.58 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TRIM44]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MTHFSD]] | -0.57 | -0.51 / -0.26 | both halves | 3e-04 |  |
| [[KICS2]] | -0.57 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[ANAPC13]] | -0.57 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PI4KAP1]] | C | PI4KAP1 activity raises PI4KAP1-1's level | lines that do not express PI4KAP1 (24) vs lines expressing it (26) | 5.86× lower at baseline in the lines without PI4KAP1 | 5e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1-1, ENSG00000260573, LCK; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMEL]] | B | PI4KAP1-1 activity lowers PMEL's level | lines that do not express PI4KAP1-1 (26) vs lines expressing it (24) | 1.08× higher at baseline in the lines without PI4KAP1-1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1, ENSG00000260573, LCK |
| [[RBM6]] | B | PI4KAP1-1 activity raises RBM6's level | lines that do not express PI4KAP1-1 (26) vs lines expressing it (24) | 1.16× lower at baseline in the lines without PI4KAP1-1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1, ENSG00000260573, LCK |
| [[SLC25A33]] | B | PI4KAP1-1 activity raises SLC25A33's level | lines that do not express PI4KAP1-1 (26) vs lines expressing it (24) | 1.35× lower at baseline in the lines without PI4KAP1-1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1, ENSG00000260573, LCK |
| [[PHAF1]] | B | PI4KAP1-1 activity raises PHAF1's level | lines that do not express PI4KAP1-1 (26) vs lines expressing it (24) | 1.18× lower at baseline in the lines without PI4KAP1-1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1, ENSG00000260573, LCK |
| [[PI4KAP1]] | C | PI4KAP1-1 activity raises PI4KAP1's level | lines that do not express PI4KAP1-1 (26) vs lines expressing it (24) | 3.77× lower at baseline in the lines without PI4KAP1-1 | 7e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1, ENSG00000260573, LCK; co-absent with the target |

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.9, 0.7); signed map (-33.2, 13.8). **Vector** length 36.9, 6.72% of its response variance represented; |z| ≥ 3 in 397 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.52 to 20); *Peptide chain elongation* (reactome, mean cos +0.52 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.52 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.6 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.5 | +6.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.3 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +0.7 | +1.9 |
|  | [[Decitabine (drug)]] 0.5 µM |  | +0.7 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +0.7 | +1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +0.7 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.0 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -1.7 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -0.9 | -1.6 |

## What is on record

> [!warning] No registry record
> PI4KAP1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16474); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16474]; `tensor/DDL_lfc|DDL_z.npy` [16474]; `embed/gene_vectors.npy` [16474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16474 or target_col == 16474). Every well: [[PI4KAP1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PI4KAP1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
