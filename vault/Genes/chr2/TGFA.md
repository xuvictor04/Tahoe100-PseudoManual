---
symbol: "TGFA"
type: "gene"
col: 8657
ensembl_id: "ENSG00000163235"
name: "transforming growth factor alpha"
location: "2p13.3"
module: 34
arm: "+"
pooled_cpm: 77.18
n_lines_expressing: 33
n_dd_up: 0
n_dd_down: 64
n_dd_up_clean: 0
n_dd_down_clean: 56
in_vector_space: true
direction_upstream: 56
direction_downstream: 58
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TGFA

*transforming growth factor alpha* — 2p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Daptomycin (drug)]] 0.5 µM in 1 line (NCI-H1573 3.43×; ⚠ unreliable plate only).
> Pooled over the cell lines (median), lowered significantly by 64 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.230× (z -20.0, q 0e+00, down in 29 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYEOV]] (+0.77, fdr 7e-06), [[KIAA0040]] (+0.68, fdr 7e-06), [[TINAGL1]] (+0.67, fdr 7e-06).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 56 arrows point to it, the strongest [[TINAGL1]] → it (grade B ⚠); 58 go from it, the strongest it → [[DCLK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8657.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Daptomycin (drug)]] 0.5 µM in 1 line (NCI-H1573 3.43×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | 1.67× | +3.6 | 0.14 | 16/31 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | 1.29× | +3.5 | 0.14 | 10/31 (HEC-1-A, LS 180, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.29 | 8/32 (A498, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 66 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 64 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8657.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.230×** | -20.0 | 0e+00 | 29/31 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.266×** | -18.0 | 0e+00 | 30/31 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.349×** | -14.3 | 5e-44 | 29/31 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -11.5 | 1e-28 | 21/31 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.524×** | -9.8 | 1e-20 | 25/32 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.612×** | -9.4 | 5e-19 | 22/31 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.578×** | -9.1 | 1e-17 | 27/31 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.517×** | -8.9 | 3e-17 | 27/32 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.506×** | -8.9 | 4e-17 | 23/30 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.522×** | -8.5 | 1e-15 | 24/31 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.588×** | -8.3 | 4e-15 | 24/32 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.525×** | -8.1 | 3e-14 | 18/26 (H4, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.551×** | -8.1 | 3e-14 | 18/31 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.552×** | -8.0 | 3e-14 | 21/31 (HOP62, RPMI-7951, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.544×** | -7.9 | 8e-14 | 23/30 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -7.7 | 3e-13 | 22/31 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.641×** | -7.3 | 7e-12 | 22/31 (SHP-77, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 98.1 | 0 | 27 (4 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0843× (z -14.9) |
| [[HOP62 (line)]] | alt | 90.5 | 0 | 26 (7 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.131× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 223 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -21.3) |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 8 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0389× (z -13.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.107× (z -9.7) |
| [[H4 (line)]] | wt | 93.7 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0514× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -10.8) |
| [[LoVo (line)]] | wt | 87.4 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -16.6) |
| [[SW 900 (line)]] | alt | 181 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 203 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0828× (z -15.7) |
| [[SW1417 (line)]] | alt | 266 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -14.7) |
| [[SW480 (line)]] | alt | 129 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -23.5) |
| [[CFPAC-1 (line)]] | alt | 170 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -14.6) |
| [[HT-29 (line)]] | alt | 167 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -15.6) |
| [[KATO III (line)]] | alt | 169 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -15.9) |
| [[LS 180 (line)]] | wt | 92.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 197 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 62.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -9.4) |
| [[SHP-77 (line)]] | alt | 48.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.7) |
| [[A-427 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 161 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.293× (z -8.6) |
| [[COLO 205 (line)]] | alt | 67.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -9.0) |
| [[Hs 766T (line)]] | wt | 113 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 45.0 | 1 (1 ⚠) | 0 | [[Daptomycin (drug)]] 0.5 µM 3.43× (z +8.8) ⚠ unreliable plate only | — |
| [[NCI-H1792 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.570× (z -12.4) ⚠ position not correctable |
| [[SW48 (line)]] | wt | 47.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.3) |
| [[A-172 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.43 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.57 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.28 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYEOV]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[TINAGL1]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[LAMA3]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 | pathway: Developmental Cell Lineages |
| [[EPHA2]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 730 |
| [[PTPRE]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[MIR4280HG]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PPARD]] | +0.62 | +0.65 / +0.62 | both halves | 7e-06 | pathway: Signaling by Nuclear Receptors |
| [[ITGA6]] | +0.62 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[SHB]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PADI1]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 43, C 13. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | TINAGL1 activity raises TGFA's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 4.48× lower at baseline in the lines without TINAGL1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[WNT7B]] | B | WNT7B activity raises TGFA's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without WNT7B | 0.005 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[TTC9]] | B | TTC9 activity raises TGFA's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without TTC9 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[PLEK2]] | B | PLEK2 activity raises TGFA's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.65× lower at baseline in the lines without PLEK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[GPR35]] | B | GPR35 activity raises TGFA's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 3.37× lower at baseline in the lines without GPR35 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[SHROOM4]] | B | SHROOM4 activity raises TGFA's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.66× lower at baseline in the lines without SHROOM4 | 0.016 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[SERPINB5]] | B | SERPINB5 activity raises TGFA's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.68× lower at baseline in the lines without SERPINB5 | 0.019 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[PTGS1]] | B | PTGS1 activity raises TGFA's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 2.25× lower at baseline in the lines without PTGS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[PTK2B]] | B | PTK2B activity raises TGFA's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.65× lower at baseline in the lines without PTK2B | 0.020 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MILR1]] | B | MILR1 activity raises TGFA's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.83× lower at baseline in the lines without MILR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[PRAG1]] | B | PRAG1 activity raises TGFA's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 3.33× lower at baseline in the lines without PRAG1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[MANCR]] | B | MANCR activity raises TGFA's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without MANCR | 0.022 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |

### Downstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 46, C 12. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCLK2]] | B | TGFA activity lowers DCLK2's level | lines that do not express TGFA (17) vs lines expressing it (33) | 3.01× higher at baseline in the lines without TGFA | 0.003 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[TINAGL1]] | B | TGFA activity raises TINAGL1's level | lines that do not express TGFA (17) vs lines expressing it (33) | 4.29× lower at baseline in the lines without TGFA | 0.005 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[PTK2B]] | B | TGFA activity raises PTK2B's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without TGFA | 0.006 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[BCL2L1-AS1]] | B | TGFA activity raises BCL2L1-AS1's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.42× lower at baseline in the lines without TGFA | 0.012 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[GPR35]] | B | TGFA activity raises GPR35's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.57× lower at baseline in the lines without TGFA | 0.013 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[PLK3]] | B | TGFA activity strengthens PLK3's drug response | lines that do not express TGFA (17) vs lines expressing it (31) | the lines without TGFA respond 0.77× as strongly (z diff +0.82); strongest at Trametinib (DMSO_TF solvate) 0.5 µM: 0.67x vs 0.40x (z diff +2.2) | 0.014 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1; target measured in part of the lines |
| [[TTC9]] | B | TGFA activity raises TTC9's level | lines that do not express TGFA (17) vs lines expressing it (33) | 3.11× lower at baseline in the lines without TGFA | 0.015 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[GALE]] | B | TGFA activity raises GALE's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without TGFA | 0.016 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[OSBPL3]] | B | TGFA activity weakens OSBPL3's drug response | lines that do not express TGFA (16) vs lines expressing it (30) | the lines without TGFA respond 1.57× as strongly (z diff -1.38); strongest at Homoharringtonine 5 µM: 2.70x vs 1.30x (z diff -4.6) | 0.020 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1; target measured in part of the lines; artifact flags |
| [[SELENOP]] | B | TGFA activity raises SELENOP's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.15× lower at baseline in the lines without TGFA | 0.020 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[ABHD17C]] | B | TGFA activity raises ABHD17C's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.68× lower at baseline in the lines without TGFA | 0.028 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[PDE2A]] | B | TGFA activity raises PDE2A's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without TGFA | 0.031 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, 52.0); signed map (3.0, 40.2). **Vector** length 118, 35.1% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | -0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | -5.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | -5.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.6 | -9.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.4 | -9.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.0 | -8.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.8 | -7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.8 | -8.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.6 | -8.3 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:70,447,284-70,554,193 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EGF ligand family |
| Hallmark sets | GLYCOLYSIS, P53_PATHWAY |
| Reactome | 41 pathways, smallest: Developmental Cell Lineages of the Integumentary System; Developmental Lineage of Mammary Gland Luminal Epithelial Cells; Developmental Lineage of Mammary Gland Myoepithelial Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P01135](https://www.uniprot.org/uniprotkb/P01135) (Protransforming growth factor alpha):

> TGF alpha is a mitogenic polypeptide that is able to bind to the EGF receptor/EGFR and to act synergistically with TGF beta to promote anchorage-independent cell proliferation in soft agar.

**Summary**, from NCBI Gene [7039](https://www.ncbi.nlm.nih.gov/gene/7039):

> This gene encodes a growth factor that is a ligand for the epidermal growth factor receptor, which activates a signaling pathway for cell proliferation, differentiation and development. This protein may act as either a transmembrane-bound ligand or a soluble ligand. This gene has been associated with many types of cancers, and it may also be involved in some cases of cleft lip/palate. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:11765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11765) · Entrez [7039](https://www.ncbi.nlm.nih.gov/gene/7039) · UniProt [P01135](https://www.uniprot.org/uniprotkb/P01135) · Ensembl [ENSG00000163235](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163235)

## Data

Gene col 8657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8657); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8657]; `tensor/DDL_lfc|DDL_z.npy` [8657]; `embed/gene_vectors.npy` [8657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8657 or target_col == 8657). Every well: [[TGFA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
