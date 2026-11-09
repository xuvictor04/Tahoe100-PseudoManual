---
symbol: "GLYATL2"
type: "gene"
col: 8007
ensembl_id: "ENSG00000156689"
name: "glycine-N-acyltransferase like 2"
location: "11q12.1"
module: 13
arm: "+"
pooled_cpm: 6.07
n_lines_expressing: 13
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 17
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GLYATL2

*glycine-N-acyltransferase like 2* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.38× (z +12.6, q 9e-34, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +10.2, q 6e-22, up in 6 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (H4 0.104×, HOP62 0.331×, CHP-212 0.171×); [[Digitoxin (drug)]] 5 µM in 2 lines (HOP62 0.118×, SNU-423 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.147×; ⚠ cell-cycle shift, explains ~22% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 0.118×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0928×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01411]] (+0.65, fdr 7e-06), [[COL5A1]] (+0.61, fdr 2e-05), [[RARB]] (+0.60, fdr 2e-05); moves opposite to [[TBCEL]] (-0.48, fdr 6e-05), [[IQCH-AS1]] (-0.46, fdr 9e-05), [[JADE2]] (-0.46, fdr 6e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[ZNF439]] → it (grade B ⚠); 17 go from it, the strongest it → [[MANCR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.38×** | +12.6 | 9e-34 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.61×** | +11.4 | 1e-27 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +10.2 | 6e-22 | 6/11 (A549, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +8.0 | 2e-13 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +7.5 | 9e-12 | 6/11 (A498, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +6.5 | 6e-09 | 2/10 (HOP62, HS-578T) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.0 | 4e-05 | 4/11 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +4.8 | 1e-04 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +4.7 | 2e-04 | 5/10 (A498, H4, …) | two highest doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.01×** | +4.4 | 6e-04 | 1/9 (A498) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.57×** | +4.4 | 6e-04 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.3 | 6e-04 | 5/11 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.78×** | +3.6 | 0.013 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.019 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +3.5 | 0.019 | 0/8 | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.042 | 1/11 (COLO 205) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.042 | 0/11 | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.058 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8007.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (H4 0.104×, HOP62 0.331×, CHP-212 0.171×); [[Digitoxin (drug)]] 5 µM in 2 lines (HOP62 0.118×, SNU-423 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.147×; ⚠ cell-cycle shift, explains ~22% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HOP62 0.118×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0928×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.874× | -4.4 | 0.007 | 1/11 (A549) | inconsistent across doses |  |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.771× | -3.3 | 0.20 | 0/11 | top dose only |  |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.702× | -3.2 | 0.20 | 1/11 (SNU-423) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.702× | -3.2 | 0.20 | 0/11 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.698× | -3.1 | 0.20 | 9/11 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.673× | -3.1 | 0.20 | 0/11 | inconsistent across doses | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.677× | -3.0 | 0.20 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 106 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -20.3) |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.118× (z -11.8) |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0928× (z -10.6) |
| [[A-172 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.648 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.524 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01411]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[COL5A1]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[RARB]] | +0.60 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[LINC01615]] | +0.60 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[SYTL3]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.59 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SETBP1]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[DKK3]] | +0.58 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[VSTM4]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[KC6]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SLC8A1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LINC01242]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCEL]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[IQCH-AS1]] | -0.46 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[JADE2]] | -0.46 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ARFGEF2]] | -0.45 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[SRGN]] | -0.45 | -0.48 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 1, C 22. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF439]] | B | ZNF439 activity raises GLYATL2's level | lines that do not express ZNF439 (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without ZNF439 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, PPP2R2B, CSF1R |
| [[LINC01615]] | C | LINC01615 activity raises GLYATL2's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 4.18× lower at baseline in the lines without LINC01615 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[SLIT3]] | C | SLIT3 activity raises GLYATL2's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 4.49× lower at baseline in the lines without SLIT3 | 0.011 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises GLYATL2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 4.61× lower at baseline in the lines without PDGFRB | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises GLYATL2's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 4.58× lower at baseline in the lines without APCDD1L | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises GLYATL2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 5.73× lower at baseline in the lines without LINC01411 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[STAC]] | C | STAC activity raises GLYATL2's level | lines that do not express STAC (25) vs lines expressing it (25) | 3.09× lower at baseline in the lines without STAC | 0.047 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; co-absent with the target |
| [[ZNF208]] | C | ZNF208 activity raises GLYATL2's level | lines that do not express ZNF208 (41) vs lines expressing it (9) | 6.10× lower at baseline in the lines without ZNF208 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC01029, ENSG00000287598; co-absent with the target |
| [[LINC02476]] | C | LINC02476 activity raises GLYATL2's level | lines that do not express LINC02476 (40) vs lines expressing it (10) | 6.00× lower at baseline in the lines without LINC02476 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02335, ENSG00000234426, ENSG00000287598; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises GLYATL2's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 3.03× lower at baseline in the lines without SIRLNT | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises GLYATL2's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.18× lower at baseline in the lines without TIMP3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[COL6A3]] | C | COL6A3 activity raises GLYATL2's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 3.90× lower at baseline in the lines without COL6A3 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 4, C 13. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANCR]] | B | GLYATL2 activity raises MANCR's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 2.93× lower at baseline in the lines without GLYATL2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476 |
| [[LOXL2]] | B | GLYATL2 activity raises LOXL2's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 3.79× lower at baseline in the lines without GLYATL2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476 |
| [[SYTL3]] | B | GLYATL2 activity raises SYTL3's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 2.77× lower at baseline in the lines without GLYATL2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476 |
| [[CFAP20DC]] | B | GLYATL2 activity raises CFAP20DC's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 2.65× lower at baseline in the lines without GLYATL2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476 |
| [[LINC02476]] | C | GLYATL2 activity raises LINC02476's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 8.59× lower at baseline in the lines without GLYATL2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |
| [[SLIT3]] | C | GLYATL2 activity raises SLIT3's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 4.26× lower at baseline in the lines without GLYATL2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |
| [[APCDD1L]] | C | GLYATL2 activity raises APCDD1L's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 4.38× lower at baseline in the lines without GLYATL2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |
| [[LINC01583]] | C | GLYATL2 activity raises LINC01583's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 2.70× lower at baseline in the lines without GLYATL2 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |
| [[COL5A1]] | C | GLYATL2 activity raises COL5A1's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 7.95× lower at baseline in the lines without GLYATL2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |
| [[PDGFRB]] | C | GLYATL2 activity raises PDGFRB's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 5.26× lower at baseline in the lines without GLYATL2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |
| [[SYNDIG1]] | C | GLYATL2 activity raises SYNDIG1's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 3.42× lower at baseline in the lines without GLYATL2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |
| [[CA12]] | C | GLYATL2 activity raises CA12's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 4.95× lower at baseline in the lines without GLYATL2 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.9, 18.8); signed map (26.1, 45.9). **Vector** length 39.3, 12.4% of its response variance represented; |z| ≥ 3 in 311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | glycine-N-acyltransferase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:58,834,065-58,904,215 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BXMAS2-10, MGC24009 |
| Gene groups (HGNC) | Glycine-N-acyltransferase family |
| Reactome | 4 pathways, smallest: Aspirin ADME; Phase II - Conjugation of compounds; Drug ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WU03](https://www.uniprot.org/uniprotkb/Q8WU03) (Glycine N-acyltransferase-like protein 2):

> Mitochondrial acyltransferase which transfers the acyl group to the N-terminus of glycine. Conjugates numerous substrates, such as arachidonoyl-CoA and saturated medium and long-chain acyl-CoAs ranging from chain-length C8:0-CoA to C18:0-CoA, to form a variety of N-acylglycines. Shows a preference for monounsaturated fatty acid oleoyl-CoA (C18:1-CoA) as an acyl donor. Does not exhibit any activity toward C22:6-CoA and chenodeoxycholoyl-CoA, nor toward serine or alanine.

**Summary**, from NCBI Gene [219970](https://www.ncbi.nlm.nih.gov/gene/219970):

> Enables glycine N-acyltransferase activity. Involved in long-chain fatty acid catabolic process; medium-chain fatty acid catabolic process; and monounsaturated fatty acid catabolic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24178) · Entrez [219970](https://www.ncbi.nlm.nih.gov/gene/219970) · UniProt [Q8WU03](https://www.uniprot.org/uniprotkb/Q8WU03) · Ensembl [ENSG00000156689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156689)

## Data

Gene col 8007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8007); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8007]; `tensor/DDL_lfc|DDL_z.npy` [8007]; `embed/gene_vectors.npy` [8007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8007 or target_col == 8007). Every well: [[GLYATL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLYATL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
