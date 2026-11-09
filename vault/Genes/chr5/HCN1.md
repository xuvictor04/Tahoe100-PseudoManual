---
symbol: "HCN1"
type: "gene"
col: 8966
ensembl_id: "ENSG00000164588"
name: "hyperpolarization activated cyclic nucleotide gated potassium channel 1"
location: "5p12"
module: 55
arm: "+"
pooled_cpm: 10.38
n_lines_expressing: 13
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 13
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# HCN1

*hyperpolarization activated cyclic nucleotide gated potassium channel 1* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.69× (z +14.9, q 0e+00, up in 2 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (COLO 205 0.117×, LS 180 0.0885×, A-427 0.159×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (COLO 205 0.0510×, LS 180 0.0385×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.122×, LS 180 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Binimetinib (drug)]] 5 µM in 2 lines (COLO 205 0.116×, LS 180 0.135×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.0825×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACSL5]] (+0.62, fdr 1e-05), [[C9orf152]] (+0.61, fdr 9e-06), [[KLK6]] (+0.60, fdr 5e-05); moves opposite to [[TMCO3]] (-0.43, fdr 7e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02058]] → it (grade C ⚠); 13 go from it, the strongest it → [[AATK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.69×** | +14.9 | 0e+00 | 2/9 (HT-29, C32) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.39×** | +9.8 | 2e-20 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +7.9 | 7e-13 | 1/5 (A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +6.4 | 2e-08 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +5.1 | 5e-05 | 3/10 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +4.6 | 4e-04 | 1/10 (HT-29) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +3.5 | 0.032 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.49× | +3.1 | 0.16 | 0/8 | top dose only | cell-cycle shift (explains ~10% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8966.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (COLO 205 0.117×, LS 180 0.0885×, A-427 0.159×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (COLO 205 0.0510×, LS 180 0.0385×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.122×, LS 180 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Binimetinib (drug)]] 5 µM in 2 lines (COLO 205 0.116×, LS 180 0.135×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.0825×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.5 µM |  | 0.671× | -3.7 | 0.13 | 4/9 (LS 180, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.746× | -3.3 | 0.30 | 3/10 (LS 180, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.655× | -3.2 | 0.30 | 4/10 (LS 180, COLO 205, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.673× | -3.0 | 0.34 | 2/9 (MIA PaCa-2, A-427) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 21.5 | 0 | 14 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0385× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.0947× (z -11.7) |
| [[COLO 205 (line)]] | alt | 452 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0825× (z -17.5) |
| [[A-427 (line)]] | wt | 35.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.159× (z -9.8) |
| [[A-172 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 588 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.52 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL5]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[C9orf152]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[KLK6]] | +0.60 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[BMP4]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[GPA33]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[TFF3]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ASB4]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[PHGR1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[LCK]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[IL20RA]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[IQGAP2]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[PPP1R1B]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCO3]] | -0.43 | -0.42 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02058]] | C | LINC02058 activity raises HCN1's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 3.69× lower at baseline in the lines without LINC02058 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises HCN1's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 4.75× lower at baseline in the lines without LGR5 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 5, C 8. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AATK]] | B | HCN1 activity weakens AATK's drug response | lines that do not express HCN1 (36) vs lines expressing it (9) | (z diff -2.52); strongest at Dinaciclib 0.05 µM: 2.68x vs 0.49x (z diff -7.3) | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[KCNQ1]] | B | HCN1 activity raises KCNQ1's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 1.79× lower at baseline in the lines without HCN1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent |
| [[KCNQ1]] | B | HCN1 activity weakens KCNQ1's drug response | lines that do not express HCN1 (37) vs lines expressing it (11) | the lines without HCN1 respond 4.07× as strongly (z diff -1.68); strongest at Homoharringtonine 5 µM: 2.33x vs 0.97x (z diff -6.7) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[AATK]] | B | HCN1 activity raises AATK's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 1.73× lower at baseline in the lines without HCN1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent |
| [[SPIRE2]] | B | HCN1 activity raises SPIRE2's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 1.31× lower at baseline in the lines without HCN1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent |
| [[LYZ]] | C | HCN1 activity raises LYZ's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 2.39× lower at baseline in the lines without HCN1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; co-absent with the target |
| [[PHGR1]] | C | HCN1 activity raises PHGR1's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 2.14× lower at baseline in the lines without HCN1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; co-absent with the target |
| [[MUC5B]] | C | HCN1 activity raises MUC5B's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 2.10× lower at baseline in the lines without HCN1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; co-absent with the target |
| [[C9orf152]] | C | HCN1 activity raises C9orf152's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 1.80× lower at baseline in the lines without HCN1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; co-absent with the target |
| [[LGALS4]] | C | HCN1 activity raises LGALS4's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 2.25× lower at baseline in the lines without HCN1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; co-absent with the target |
| [[AZGP1]] | C | HCN1 activity raises AZGP1's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 1.99× lower at baseline in the lines without HCN1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; co-absent with the target |
| [[NPSR1]] | C | HCN1 activity raises NPSR1's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 2.20× lower at baseline in the lines without HCN1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.3, 48.0); signed map (64.9, 11.1). **Vector** length 35.8, 11.6% of its response variance represented; |z| ≥ 3 in 257 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +14.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.0 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -0.9 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | hyperpolarization activated cyclic nucleotide gated potassium channel 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:45,254,948-45,696,498 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCNG-1, HAC-2; previously BCNG1 |
| Gene groups (HGNC) | Cyclic nucleotide gated channels |
| Reactome | 3 pathways, smallest: HCN channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [O60741](https://www.uniprot.org/uniprotkb/O60741) (Potassium/sodium hyperpolarization-activated cyclic nucleotide-gated channel 1):

> Hyperpolarization-activated ion channel that are permeable to sodium and potassium ions. Displays lower selectivity for K(+) over Na(+) ions. Contributes to the native pacemaker currents in heart (If) and in the generation of the I(h) current which controls neuron excitability. Participates in cerebellar mechanisms of motor learning (By similarity). May mediate responses to sour stimuli (By similarity).

**Summary**, from NCBI Gene [348980](https://www.ncbi.nlm.nih.gov/gene/348980):

> The membrane protein encoded by this gene is a hyperpolarization-activated cation channel that contributes to the native pacemaker currents in heart and neurons. The encoded protein can homodimerize or heterodimerize with other pore-forming subunits to form a potassium channel. This channel may act as a receptor for sour tastes. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:4845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4845) · Entrez [348980](https://www.ncbi.nlm.nih.gov/gene/348980) · UniProt [O60741](https://www.uniprot.org/uniprotkb/O60741) · Ensembl [ENSG00000164588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164588)

## Data

Gene col 8966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8966); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8966]; `tensor/DDL_lfc|DDL_z.npy` [8966]; `embed/gene_vectors.npy` [8966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8966 or target_col == 8966). Every well: [[HCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
