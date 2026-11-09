---
symbol: "LRGUK"
type: "gene"
col: 7901
ensembl_id: "ENSG00000155530"
name: "leucine rich repeats and guanylate kinase domain containing"
location: "7q33"
module: 26
arm: "+"
pooled_cpm: 9.6
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# LRGUK

*leucine rich repeats and guanylate kinase domain containing* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.77× (z +9.8, q 9e-20, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.449× (z -7.7, q 1e-11, down in 25 of 45 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.510× (z -6.4, q 2e-08, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSIP2-AS1]] (+0.76, fdr 7e-06), [[SEMA6A-AS1]] (+0.67, fdr 7e-06), [[EFCAB10]] (+0.66, fdr 1e-05); moves opposite to [[SLC35A1]] (-0.53, fdr 3e-05), [[COPG2]] (-0.52, fdr 1e-05), [[SRD5A1]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CD226]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.77×** | +9.8 | 9e-20 | 36/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.61×** | +9.2 | 1e-17 | 35/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +8.6 | 2e-15 | 25/44 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +6.9 | 6e-10 | 29/45 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.7 | 2e-06 | 21/42 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.46×** | +5.1 | 3e-05 | 22/46 (A-427, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +4.5 | 5e-04 | 22/45 (A-172, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.5 | 5e-04 | 8/16 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.005 | 18/44 (SW480, SW48, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +3.4 | 0.039 | 8/24 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.4 | 0.039 | 14/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.050 | 5/46 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.065 | 9/45 (NCI-H460, A549, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.084 | 12/46 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +3.0 | 0.098 | 5/45 (A498, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7901.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.449×** | -7.7 | 1e-11 | 25/45 (SNU-1, RPMI-7951, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.463×** | -7.4 | 5e-11 | 27/43 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.510×** | -6.4 | 2e-08 | 26/45 (COLO 205, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.348×** | -5.3 | 2e-05 | 23/42 (LOX-IMVI, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.363×** | -5.1 | 4e-05 | 26/46 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.612×** | -4.7 | 3e-04 | 22/45 (SW48, LOX-IMVI, …) | rises with dose |  |
| [[Irinotecan (drug)]] 5 µM |  | **0.454×** | -3.9 | 0.006 | 15/46 (LoVo, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -3.9 | 0.007 | 21/45 (hTERT-HPNE, COLO 205, …) | rises with dose | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.709× | -3.1 | 0.11 | 15/45 (C32, HepG2/C3A, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.539× | -3.1 | 0.11 | 12/41 (SW48, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.63 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 13.4× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0953× (z -9.3) |
| [[BT-474 (line)]] | alt | 7.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0866× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0895× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0327× (z -20.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 6.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 41.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 7.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0922× (z -13.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0894× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 24.0 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0745× (z -8.5) |
| [[SW480 (line)]] | alt | 8.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0273× (z -19.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSIP2-AS1]] | +0.76 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[SEMA6A-AS1]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[EFCAB10]] | +0.66 | +0.79 / +0.49 | both halves | 1e-05 |  |
| [[PMFBP1]] | +0.65 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[TMEM232]] | +0.65 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[LINC00907]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[LINC01031]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[LINC00486]] | +0.62 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ITPR2-AS1]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TIAM2]] | +0.62 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[PRR4]] | +0.60 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A1]] | -0.53 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[COPG2]] | -0.52 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SRD5A1]] | -0.52 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[SLC35D1]] | -0.51 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[NT5M]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[IDH2]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[POGLUT2]] | -0.49 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PDE7A]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[DCUN1D2]] | -0.49 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[ATP7B]] | -0.49 | -0.60 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD226]] | B | CD226 activity raises LRGUK's level | lines that do not express CD226 (7) vs lines expressing it (43) | 2.62× lower at baseline in the lines without CD226 | 0.009 | ⚠ within organs, on part of the lines; also absent: FRZB, GALNT16, KLRG1; maybe low, not absent |
| [[PMFBP1]] | B | PMFBP1 activity raises LRGUK's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 2.50× lower at baseline in the lines without PMFBP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[TPRG1]] | B | TPRG1 activity raises LRGUK's level | lines that do not express TPRG1 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without TPRG1 | 0.009 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SYCP2L; maybe low, not absent |
| [[ZNF474]] | B | ZNF474 activity raises LRGUK's level | lines that do not express ZNF474 (6) vs lines expressing it (44) | 2.48× lower at baseline in the lines without ZNF474 | 0.029 | ⚠ within organs, on part of the lines; also absent: RBFOX1, NEK10, LINC01524; maybe low, not absent |
| [[LINC01917]] | B | LINC01917 activity raises LRGUK's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without LINC01917 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises LRGUK's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.35× lower at baseline in the lines without FSIP2-AS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC02360]] | B | LINC02360 activity raises LRGUK's level | lines that do not express LINC02360 (33) vs lines expressing it (17) | 1.61× lower at baseline in the lines without LINC02360 | 0.088 | ⚠ within organs, on part of the lines; also absent: MAGEB2, LINC01905, AJAP1 |
| [[LINC02885]] | B | LINC02885 activity raises LRGUK's level | lines that do not express LINC02885 (15) vs lines expressing it (35) | 1.75× lower at baseline in the lines without LINC02885 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC01399, PCDHB2, ENSG00000258168; maybe low, not absent |
| [[LINC02133]] | C | LINC02133 activity raises LRGUK's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without LINC02133 | 0.056 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises LRGUK's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 3.49× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[IMPG2]] | C | IMPG2 activity raises LRGUK's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 2.51× lower at baseline in the lines without IMPG2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.9, 15.2); signed map (22.4, 3.3). **Vector** length 75.0, 13.8% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.6 | +5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.9 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.6 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and guanylate kinase domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:134,127,299-134,264,595 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32786, CFAP246 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M69](https://www.uniprot.org/uniprotkb/Q96M69) (Leucine-rich repeat and guanylate kinase domain-containing protein):

> Involved in multiple aspects of sperm assembly including acrosome attachment, shaping of the sperm head and in the early aspects of axoneme development. Not essential for primary cilium biogenesis.

**Summary**, from NCBI Gene [136332](https://www.ncbi.nlm.nih.gov/gene/136332):

> Predicted to enable GMP kinase activity. Predicted to be involved in axoneme assembly and spermatogenesis. Predicted to be located in acrosomal vesicle and manchette. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21964) · Entrez [136332](https://www.ncbi.nlm.nih.gov/gene/136332) · UniProt [Q96M69](https://www.uniprot.org/uniprotkb/Q96M69) · Ensembl [ENSG00000155530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155530)

## Data

Gene col 7901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7901); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7901]; `tensor/DDL_lfc|DDL_z.npy` [7901]; `embed/gene_vectors.npy` [7901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7901 or target_col == 7901). Every well: [[LRGUK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRGUK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
