---
symbol: "APBB1IP"
type: "gene"
col: 1186
ensembl_id: "ENSG00000077420"
name: "amyloid beta precursor protein binding family B member 1 interacting protein"
location: "10p12.1"
module: 13
arm: "+"
pooled_cpm: 11.36
n_lines_expressing: 10
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 36
direction_downstream: 47
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# APBB1IP

*amyloid beta precursor protein binding family B member 1 interacting protein* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.06× (z +15.0, q 0e+00, up in 2 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +9.8, q 2e-20, up in 0 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 0.0919×, J82 0.350×, LOX-IMVI 0.327×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (A498 0.207×, LOX-IMVI 0.223×, J82 0.250×; ⚠ cell-cycle shift, explains ~48% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LOX-IMVI 0.294×, RPMI-7951 0.320×, A498 0.400×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0673×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSC-AS1]] (+0.69, fdr 7e-06), [[SLC8A1]] (+0.68, fdr 7e-06), [[ADAMTS12]] (+0.67, fdr 7e-06); moves opposite to [[RPH3AL]] (-0.43, fdr 1e-04), [[ITGB4]] (-0.43, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[ADAMTS12]] → it (grade C ⚠); 47 go from it, the strongest it → [[SLC8A1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.06×** | +15.0 | 0e+00 | 2/8 (A498, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +11.9 | 4e-30 | 2/8 (A549, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +9.8 | 2e-20 | 0/8 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +7.7 | 2e-12 | 2/8 (HS-578T, A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.9 | 1e-04 | 4/8 (J82, HS-578T, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.005 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.0 | 0.005 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.005 | 0/8 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.008 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.7 | 0.013 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +3.7 | 0.013 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.022 | 0/8 | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.5 | 0.022 | 0/8 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.072 | 2/8 (hTERT-HPNE, A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.073 | 0/8 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.086 | 1/8 (hTERT-HPNE) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.092 | 2/8 (A549, A498) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1186.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 0.0919×, J82 0.350×, LOX-IMVI 0.327×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (A498 0.207×, LOX-IMVI 0.223×, J82 0.250×; ⚠ cell-cycle shift, explains ~48% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LOX-IMVI 0.294×, RPMI-7951 0.320×, A498 0.400×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0673×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -3.8 | 0.086 | 0/8 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.713× | -3.3 | 0.22 | 0/8 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.713× | -3.2 | 0.22 | 0/8 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.711× | -3.0 | 0.35 | 1/8 (HS-578T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -25.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 77.6 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.3) |
| [[A498 (line)]] | wt | 96.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -15.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.7) |
| [[J82 (line)]] | alt | 67.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0673× (z -9.8) |
| [[SNU-423 (line)]] | alt | 31.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.945 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSC-AS1]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SLC8A1]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS12]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[KC6]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[LINC02377]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ZNF521]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[LINC01435]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[OR9Q1]] | +0.63 | +0.63 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[PSG5]] | +0.63 | +0.73 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[ABI3BP]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[LINC01615]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[MIR137HG]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPH3AL]] | -0.43 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[ITGB4]] | -0.43 | -0.45 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 0, C 36. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS12]] | C | ADAMTS12 activity raises APBB1IP's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 4.57× lower at baseline in the lines without ADAMTS12 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[MSC]] | C | MSC activity raises APBB1IP's level | lines that do not express MSC (34) vs lines expressing it (16) | 3.61× lower at baseline in the lines without MSC | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises APBB1IP's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 3.30× lower at baseline in the lines without PAPPA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises APBB1IP's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 3.24× lower at baseline in the lines without ADAM12 | 0.017 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises APBB1IP's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.24× lower at baseline in the lines without WNT5A | 0.021 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[PKD1L1-AS1]] | C | PKD1L1-AS1 activity raises APBB1IP's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 3.72× lower at baseline in the lines without PKD1L1-AS1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |
| [[LINC01435]] | C | LINC01435 activity raises APBB1IP's level | lines that do not express LINC01435 (37) vs lines expressing it (13) | 2.55× lower at baseline in the lines without LINC01435 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000203434, TMPRSS15, ENSG00000224865; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises APBB1IP's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.70× lower at baseline in the lines without PDGFRB | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises APBB1IP's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.90× lower at baseline in the lines without INSYN2B | 0.036 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[ADAMTS16]] | C | ADAMTS16 activity raises APBB1IP's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 2.77× lower at baseline in the lines without ADAMTS16 | 0.038 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises APBB1IP's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 3.65× lower at baseline in the lines without LINC01615 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises APBB1IP's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 3.33× lower at baseline in the lines without LINC01411 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 4, C 43. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC8A1-AS1]] | B | APBB1IP activity raises SLC8A1-AS1's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 1.89× lower at baseline in the lines without APBB1IP | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749 |
| [[EVC]] | B | APBB1IP activity raises EVC's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 3.60× lower at baseline in the lines without APBB1IP | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749 |
| [[SYTL3]] | B | APBB1IP activity raises SYTL3's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 2.15× lower at baseline in the lines without APBB1IP | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749 |
| [[SPEG]] | B | APBB1IP activity raises SPEG's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 2.46× lower at baseline in the lines without APBB1IP | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749 |
| [[PAPPA]] | C | APBB1IP activity raises PAPPA's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 10.01× lower at baseline in the lines without APBB1IP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[ADAMTS12]] | C | APBB1IP activity raises ADAMTS12's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 11.89× lower at baseline in the lines without APBB1IP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[SLC8A1]] | C | APBB1IP activity raises SLC8A1's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 7.06× lower at baseline in the lines without APBB1IP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[ABI3BP]] | C | APBB1IP activity raises ABI3BP's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 5.09× lower at baseline in the lines without APBB1IP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[CA12]] | C | APBB1IP activity raises CA12's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 6.23× lower at baseline in the lines without APBB1IP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[LINC01435]] | C | APBB1IP activity raises LINC01435's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 4.06× lower at baseline in the lines without APBB1IP | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[WNT5A]] | C | APBB1IP activity raises WNT5A's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 7.21× lower at baseline in the lines without APBB1IP | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[RARB]] | C | APBB1IP activity raises RARB's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 6.35× lower at baseline in the lines without APBB1IP | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.2, 20.4); signed map (29.0, 46.2). **Vector** length 36.7, 14.3% of its response variance represented; |z| ≥ 3 in 225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.8 | +1.0 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.7 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor protein binding family B member 1 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:26,438,341-26,567,803 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RARP1, PREL1, INAG1, RIAM |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MRL family adaptor proteins |
| Reactome | 19 pathways, smallest: GRB2:SOS provides linkage to MAPK signaling for Integrins; p130Cas linkage to MAPK signaling for integrins; Integrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5R6](https://www.uniprot.org/uniprotkb/Q7Z5R6) (Amyloid beta A4 precursor protein-binding family B member 1-interacting protein):

> Appears to function in the signal transduction from Ras activation to actin cytoskeletal remodeling. Suppresses insulin-induced promoter activities through AP1 and SRE. Mediates Rap1-induced adhesion.

**Summary**, from NCBI Gene [54518](https://www.ncbi.nlm.nih.gov/gene/54518):

> Predicted to enable protein-macromolecule adaptor activity. Predicted to be involved in intracellular signal transduction. Predicted to act upstream of or within T cell activation via T cell receptor contact with antigen bound to MHC molecule on antigen presenting cell and positive regulation of cell adhesion. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17379) · Entrez [54518](https://www.ncbi.nlm.nih.gov/gene/54518) · UniProt [Q7Z5R6](https://www.uniprot.org/uniprotkb/Q7Z5R6) · Ensembl [ENSG00000077420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077420)

## Data

Gene col 1186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1186); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1186]; `tensor/DDL_lfc|DDL_z.npy` [1186]; `embed/gene_vectors.npy` [1186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1186 or target_col == 1186). Every well: [[APBB1IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APBB1IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
