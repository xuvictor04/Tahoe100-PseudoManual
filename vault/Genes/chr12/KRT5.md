---
symbol: "KRT5"
type: "gene"
col: 11774
ensembl_id: "ENSG00000186081"
name: "keratin 5"
location: "12q13.13"
module: 27
arm: "+"
pooled_cpm: 7.64
n_lines_expressing: 4
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 19
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# KRT5

*keratin 5* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.81× (z +11.1, q 4e-26, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +5.4, q 1e-05, up in 0 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.263×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1]] (+0.56, fdr 6e-05), [[SERPINF1]] (+0.55, fdr 2e-05), [[FGF20]] (+0.54, fdr 2e-05); moves opposite to [[KISS1]] (-0.52, fdr 1e-04), [[SLC14A1]] (-0.46, fdr 1e-04), [[HBEGF]] (-0.46, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PSG1]] → it (grade C ⚠); 19 go from it, the strongest it → [[JAKMIP2-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.81×** | +11.1 | 4e-26 | 2/2 (SW480, Hs 766T) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.43×** | +9.9 | 1e-20 | 2/2 (SW480, Hs 766T) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.74×** | +9.0 | 3e-17 | 2/2 (SW480, Hs 766T) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +5.4 | 1e-05 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.81×** | +5.3 | 1e-05 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.92×** | +5.3 | 1e-05 | 1/2 (Hs 766T) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +4.5 | 4e-04 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +4.5 | 4e-04 | 0/2 | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.81×** | +4.3 | 0.001 | 1/2 (SW480) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.01×** | +4.0 | 0.003 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +3.8 | 0.007 | 0/2 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.63×** | +3.5 | 0.020 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.58×** | +3.5 | 0.023 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.4 | 0.023 | 1/2 (Hs 766T) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.90×** | +3.3 | 0.038 | 1/2 (Hs 766T) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.041 | 2/2 (Hs 766T, SW480) | inconsistent across doses | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.52×** | +3.0 | 0.067 | 0/2 | rises with dose |  |
| [[Erythromycin (drug)]] 5 µM |  | **1.77×** | +2.9 | 0.094 | 0/2 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11774.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 0.263×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.477× | -3.5 | 0.24 | 0/2 | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.543× | -3.0 | 0.62 | 0/2 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 93.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.69× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.6) |
| [[A-172 (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 94.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.806 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1]] | +0.56 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[SERPINF1]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[FGF20]] | +0.54 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[JAKMIP2-AS1]] | +0.50 | +0.63 / +0.30 | both halves | 2e-04 |  |
| [[B3GAT1-DT]] | +0.49 | +0.52 / +0.31 | both halves | 2e-04 |  |
| [[NELL2]] | +0.49 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[SLC30A10]] | +0.49 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[MSI2]] | +0.48 | +0.32 / +0.33 | both halves | 2e-04 |  |
| [[TRIM29]] | +0.48 | +0.45 / +0.41 | both halves | 4e-05 | STRING 802 |
| [[CHDH]] | +0.46 | +0.44 / +0.29 | both halves | 3e-04 |  |
| [[VIL1]] | +0.46 | +0.32 / +0.45 | both halves | 2e-04 |  |
| [[CCR3]] | +0.46 | +0.49 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KISS1]] | -0.52 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[SLC14A1]] | -0.46 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[HBEGF]] | -0.46 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[DUSP5-DT]] | -0.44 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[PTHLH]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[PPP1R14B]] | -0.44 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[PPP1R14B-AS1]] | -0.43 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[GRIA1]] | -0.43 | -0.17 / -0.43 | ⚠ not reproduced | 0.001 |  |
| [[PRDM8]] | -0.42 | -0.36 / -0.33 | both halves | 1e-04 | pathway: Cell junction organization |
| [[GPAT3]] | -0.41 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[TPBG]] | -0.41 | -0.22 / -0.32 | both halves | 6e-04 |  |
| [[ANTXR2]] | -0.41 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[CLCF1]] | -0.41 | -0.27 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSG1]] | C | PSG1 activity raises KRT5's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 3.32× lower at baseline in the lines without PSG1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[DOK5]] | C | DOK5 activity raises KRT5's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.75× lower at baseline in the lines without DOK5 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[F5]] | C | F5 activity raises KRT5's level | lines that do not express F5 (39) vs lines expressing it (11) | 2.55× lower at baseline in the lines without F5 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2; co-absent with the target |
| [[KISS1]] | C | KISS1 activity raises KRT5's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 2.07× lower at baseline in the lines without KISS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1; co-absent with the target |
| [[APOB]] | C | APOB activity raises KRT5's level | lines that do not express APOB (47) vs lines expressing it (3) | 1.91× lower at baseline in the lines without APOB | 0.089 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAKMIP2-AS1]] | C | KRT5 activity raises JAKMIP2-AS1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 6.37× lower at baseline in the lines without KRT5 | 4e-04 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[PSG1]] | C | KRT5 activity raises PSG1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 1.47× lower at baseline in the lines without KRT5 | 0.001 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[F10]] | C | KRT5 activity raises F10's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.06× lower at baseline in the lines without KRT5 | 0.005 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |
| [[NKD1]] | C | KRT5 activity raises NKD1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 6.67× lower at baseline in the lines without KRT5 | 0.005 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[LINC01622]] | C | KRT5 activity raises LINC01622's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 2.64× lower at baseline in the lines without KRT5 | 0.006 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[GRIA1]] | C | KRT5 activity raises GRIA1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.55× lower at baseline in the lines without KRT5 | 0.007 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |
| [[DOK5]] | C | KRT5 activity raises DOK5's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 5.30× lower at baseline in the lines without KRT5 | 0.008 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[VWA2]] | C | KRT5 activity raises VWA2's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.48× lower at baseline in the lines without KRT5 | 0.009 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[GJB1]] | C | KRT5 activity raises GJB1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.00× lower at baseline in the lines without KRT5 | 0.011 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[KISS1]] | C | KRT5 activity raises KISS1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.74× lower at baseline in the lines without KRT5 | 0.013 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[APOB]] | C | KRT5 activity raises APOB's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 2.29× lower at baseline in the lines without KRT5 | 0.021 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[SLC14A1]] | C | KRT5 activity raises SLC14A1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.09× lower at baseline in the lines without KRT5 | 0.027 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.6, 42.8); signed map (62.2, 17.2). **Vector** length 11.2, 5.34% of its response variance represented; |z| ≥ 3 in 54 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.8 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.5 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.4 | +0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.4 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.3 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.3 | +1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +0.3 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.4 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.3 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.3 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.3 | -0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.2 | -0.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.2 | -1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | keratin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:52,514,575-52,520,530 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KRT5A, CK-5; previously EBS2 |
| Gene groups (HGNC) | Keratins, type II |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 5 pathways, smallest: Type I hemidesmosome assembly; Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P13647](https://www.uniprot.org/uniprotkb/P13647) (Keratin, type II cytoskeletal 5):

> Structural component of intermediate filaments in basal keratinocytes of stratified epithelia. Forms heteropolymers with type I partners including KRT14 and KRT15, contributing to the formation of the keratin intermediate filament network that provides mechanical stability and resilience to the basal layer of the epidermis. Regulates the recruitment of Langerhans cells to the epidermis, potentially by modulation of the abundance of macrophage chemotactic cytokines, macrophage inflammatory …

**Summary**, from NCBI Gene [3852](https://www.ncbi.nlm.nih.gov/gene/3852):

> The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in these genes have been associated with a complex of diseases termed epidermolysis bullosa simplex. …

**Accessions** — [HGNC:6442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6442) · Entrez [3852](https://www.ncbi.nlm.nih.gov/gene/3852) · UniProt [P13647](https://www.uniprot.org/uniprotkb/P13647) · Ensembl [ENSG00000186081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186081)

## Data

Gene col 11774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11774); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11774]; `tensor/DDL_lfc|DDL_z.npy` [11774]; `embed/gene_vectors.npy` [11774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11774 or target_col == 11774). Every well: [[KRT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
