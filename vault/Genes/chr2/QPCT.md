---
symbol: "QPCT"
type: "gene"
col: 3725
ensembl_id: "ENSG00000115828"
name: "glutaminyl-peptide cyclotransferase"
location: "2p22.2"
module: 19
arm: "+"
pooled_cpm: 11.22
n_lines_expressing: 25
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# QPCT

*glutaminyl-peptide cyclotransferase* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.20× (z +16.4, q 0e+00, up in 15 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.62× (z +13.6, q 9e-40, up in 15 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.210×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.229×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.281×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGA]] (+0.64, fdr 1e-05), [[CLDN16]] (+0.63, fdr 3e-05), [[CCN3]] (+0.60, fdr 2e-05); moves opposite to [[SELENOO]] (-0.55, fdr 6e-05), [[NUDCD3]] (-0.53, fdr 7e-05), [[HERC2P2]] (-0.52, fdr 9e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TNFAIP2]] → it (grade B ⚠); 8 go from it, the strongest it → [[TNFAIP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.20×** | +16.4 | 0e+00 | 15/16 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.64×** | +14.7 | 0e+00 | 12/12 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +13.6 | 9e-40 | 15/22 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +10.6 | 3e-24 | 13/15 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +7.4 | 1e-11 | 20/22 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +6.8 | 1e-09 | 20/22 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +5.3 | 8e-06 | 11/22 (SK-MEL-2, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.0 | 3e-05 | 9/21 (CFPAC-1, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.9 | 5e-05 | 8/22 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.59×** | +4.6 | 2e-04 | 10/22 (HOP62, NCI-H460, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.010 | 9/22 (HOP62, A-172, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.7 | 0.011 | 3/12 (SNU-423, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.46×** | +3.6 | 0.012 | 4/21 (SW 900, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.41×** | +3.4 | 0.024 | 7/20 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.3 | 0.036 | 8/21 (NCI-H2347, HCT15, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.0 | 0.086 | 4/20 (SW480, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3725.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.210×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.229×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.281×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.728× | -3.1 | 0.37 | 3/22 (HT-29, A-172, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.716× | -3.1 | 0.37 | 1/22 (NCI-H23) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.0 | 0.37 | 4/23 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 107 | 1 (1 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.281× (z -10.3) |
| [[HOP62 (line)]] | alt | 5.98 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.6× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +9.9) | — |
| [[SW480 (line)]] | alt | 14.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.92× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.57× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGA]] | +0.64 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CLDN16]] | +0.63 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[CCN3]] | +0.60 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[CXCL1]] | +0.59 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[ADGRL3]] | +0.57 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[MKLN1-AS]] | +0.57 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SALL4]] | +0.56 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[MALRD1]] | +0.55 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[PDE8B]] | +0.55 | +0.28 / +0.46 | both halves | 3e-04 |  |
| [[CD74]] | +0.54 | +0.30 / +0.60 | both halves | 2e-04 |  |
| [[LINC02605]] | +0.54 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[PCDH17]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOO]] | -0.55 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[NUDCD3]] | -0.53 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[HERC2P2]] | -0.52 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[PHRF1]] | -0.51 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[ACOX3]] | -0.50 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[TELO2]] | -0.46 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[TANGO2]] | -0.46 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[MLXIP]] | -0.46 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[DIP2A]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[CCM2]] | -0.45 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[PIGU]] | -0.45 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[ZNF765]] | -0.45 | -0.36 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFAIP2]] | B | TNFAIP2 activity raises QPCT's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.45× lower at baseline in the lines without TNFAIP2 | 0.056 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[SLC16A4]] | B | SLC16A4 activity raises QPCT's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 1.89× lower at baseline in the lines without SLC16A4 | 0.057 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[SALL4]] | B | SALL4 activity raises QPCT's level | lines that do not express SALL4 (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without SALL4 | 0.085 | ⚠ within organs, on part of the lines; also absent: CHST8, PAX7, SLC6A11 |
| [[CXCL5]] | C | CXCL5 activity raises QPCT's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.11× lower at baseline in the lines without CXCL5 | 0.025 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2; co-absent with the target |
| [[NKAIN2]] | C | NKAIN2 activity raises QPCT's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 1.99× lower at baseline in the lines without NKAIN2 | 0.056 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFAIP2]] | B | QPCT activity raises TNFAIP2's level | lines that do not express QPCT (25) vs lines expressing it (25) | 2.01× lower at baseline in the lines without QPCT | 0.006 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81 |
| [[TMSB4X]] | B | QPCT activity raises TMSB4X's level | lines that do not express QPCT (25) vs lines expressing it (25) | 1.35× lower at baseline in the lines without QPCT | 0.046 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81 |
| [[CRISPLD1]] | B | QPCT activity lowers CRISPLD1's level | lines that do not express QPCT (25) vs lines expressing it (25) | 1.57× higher at baseline in the lines without QPCT | 0.049 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81 |
| [[HHLA3]] | B | QPCT activity lowers HHLA3's level | lines that do not express QPCT (25) vs lines expressing it (25) | 1.31× higher at baseline in the lines without QPCT | 0.051 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81 |
| [[SLC7A7]] | B | QPCT activity raises SLC7A7's level | lines that do not express QPCT (25) vs lines expressing it (25) | 1.23× lower at baseline in the lines without QPCT | 0.072 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81 |
| [[LRRN1]] | C | QPCT activity raises LRRN1's level | lines that do not express QPCT (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without QPCT | 0.015 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81; co-absent with the target |
| [[CXCL5]] | C | QPCT activity raises CXCL5's level | lines that do not express QPCT (25) vs lines expressing it (25) | 2.56× lower at baseline in the lines without QPCT | 0.017 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81; co-absent with the target |
| [[EREG]] | C | QPCT activity raises EREG's level | lines that do not express QPCT (25) vs lines expressing it (25) | 3.02× lower at baseline in the lines without QPCT | 0.042 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.0, 27.1); signed map (42.7, 16.6). **Vector** length 43.2, 9.38% of its response variance represented; |z| ≥ 3 in 378 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.1 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.9 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | glutaminyl-peptide cyclotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:37,342,827-37,373,322 (+) |
| Ensembl biotype | protein_coding |
| Also known as | QC, GCT |
| Gene groups (HGNC) | M28 metallopeptidases; Glutaminyl-peptide cyclotransferase family |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16769](https://www.uniprot.org/uniprotkb/Q16769) (Glutaminyl-peptide cyclotransferase):

> Responsible for the biosynthesis of pyroglutamyl peptides. Has a bias against acidic and tryptophan residues adjacent to the N-terminal glutaminyl residue and a lack of importance of chain length after the second residue. Also catalyzes N-terminal pyroglutamate formation. In vitro, catalyzes pyroglutamate formation of N-terminally truncated form of APP amyloid-beta peptides [Glu-3]-amyloid-beta. May be involved in the N-terminal pyroglutamate formation of several amyloid-related plaque-forming …

**Summary**, from NCBI Gene [25797](https://www.ncbi.nlm.nih.gov/gene/25797):

> This gene encodes human pituitary glutaminyl cyclase, which is responsible for the presence of pyroglutamyl residues in many neuroendocrine peptides. The amino acid sequence of this enzyme is 86% identical to that of bovine glutaminyl cyclase. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9753) · Entrez [25797](https://www.ncbi.nlm.nih.gov/gene/25797) · UniProt [Q16769](https://www.uniprot.org/uniprotkb/Q16769) · Ensembl [ENSG00000115828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115828)

## Data

Gene col 3725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3725); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3725]; `tensor/DDL_lfc|DDL_z.npy` [3725]; `embed/gene_vectors.npy` [3725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3725 or target_col == 3725). Every well: [[QPCT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QPCT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
