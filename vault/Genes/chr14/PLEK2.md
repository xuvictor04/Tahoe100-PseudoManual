---
symbol: "PLEK2"
type: "gene"
col: 1984
ensembl_id: "ENSG00000100558"
name: "pleckstrin 2"
location: "14q23.3-q24.1"
module: 34
arm: "+"
pooled_cpm: 34.4
n_lines_expressing: 33
n_dd_up: 3
n_dd_down: 50
n_dd_up_clean: 3
n_dd_down_clean: 46
in_vector_space: true
direction_upstream: 52
direction_downstream: 57
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PLEK2

*pleckstrin 2* — 14q23.3-q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.46× (z +4.3, q 0.009, up in 17 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.260× (z -21.6, q 0e+00, down in 31 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A16]] (+0.79, fdr 7e-06), [[CDCP1]] (+0.77, fdr 7e-06), [[PLEKHG5]] (+0.77, fdr 7e-06); moves opposite to [[MTUS1-DT]] (-0.61, fdr 2e-05), [[TNS3]] (-0.61, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[LINC02725]] → it (grade B ⚠); 57 go from it, the strongest it → [[S100A16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 0.009 | 17/31 (SW48, LOX-IMVI, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.084 | 15/31 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.084 | 17/31 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.33× | +3.3 | 0.13 | 15/31 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.32× | +3.0 | 0.28 | 13/31 (Hs 766T, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 4 with an alert ⚠; shown: the 15 strongest. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.260×** | -21.6 | 0e+00 | 31/31 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.326×** | -18.0 | 0e+00 | 30/31 (SW48, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.472×** | -10.8 | 7e-25 | 28/31 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.376×** | -10.8 | 7e-25 | 31/31 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.464×** | -10.6 | 3e-24 | 27/31 (AsPC-1, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.431×** | -9.7 | 4e-20 | 25/31 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.432×** | -9.5 | 2e-19 | 27/32 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.456×** | -8.9 | 5e-17 | 23/31 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.462×** | -8.4 | 2e-15 | 24/31 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.461×** | -8.1 | 3e-14 | 25/31 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.497×** | -7.9 | 1e-13 | 25/31 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.486×** | -7.9 | 2e-13 | 27/31 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.597×** | -7.6 | 9e-13 | 26/31 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.496×** | -7.6 | 9e-13 | 21/31 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.616×** | -7.2 | 2e-11 | 24/31 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 201 | 0 | 27 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -25.2) |
| [[HOP62 (line)]] | alt | 48.9 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0877× (z -24.0) |
| [[LoVo (line)]] | wt | 67.1 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -21.1) |
| [[SW48 (line)]] | wt | 118 | 1 | 11 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.91× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0947× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 76.4 | 0 | 11 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0628× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 98.1 | 0 | 10 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -17.8) |
| [[Hs 766T (line)]] | wt | 86.4 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -19.3) |
| [[LS 180 (line)]] | wt | 111 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -22.8) |
| [[NCI-H2347 (line)]] | alt | 47.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 48.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 51.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -18.3) |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0696× (z -19.4) |
| [[SW480 (line)]] | alt | 40.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.0) |
| [[KATO III (line)]] | alt | 68.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -24.8) |
| [[RKO (line)]] | wt | 26.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -17.1) |
| [[COLO 205 (line)]] | alt | 50.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -13.8) |
| [[HCT15 (line)]] | alt | 32.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -14.6) |
| [[HT-29 (line)]] | alt | 28.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -13.8) |
| [[J82 (line)]] | alt | 13.2 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0993× (z -9.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 29.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -20.0) |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.8) |
| [[A549 (line)]] | wt | 20.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 46.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 9.27 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -9.3) |
| [[SW 1271 (line)]] | alt | 145 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -11.9) |
| [[A-172 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A16]] | +0.79 | +0.81 / +0.72 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.77 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[PLEKHG5]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 | same gene group; STRING 681 |
| [[ITGA2]] | +0.76 | +0.77 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[FERMT1]] | +0.75 | +0.74 / +0.78 | both halves | 7e-06 | same gene group; STRING 800 |
| [[LAMC2]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[LYPD3]] | +0.73 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[PPARD]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TOR4A]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[GJB3]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TINAGL1]] | +0.70 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTUS1-DT]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[TNS3]] | -0.61 | -0.51 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 39, C 13. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02725]] | B | LINC02725 activity raises PLEK2's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 2.84× lower at baseline in the lines without LINC02725 | 0.002 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425 |
| [[TMCC3]] | B | TMCC3 activity raises PLEK2's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.90× lower at baseline in the lines without TMCC3 | 0.006 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[DHRS9]] | B | DHRS9 activity raises PLEK2's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 4.41× lower at baseline in the lines without DHRS9 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[KRT15]] | B | KRT15 activity raises PLEK2's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 3.06× lower at baseline in the lines without KRT15 | 0.014 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[GTF2IP7]] | B | GTF2IP7 activity raises PLEK2's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without GTF2IP7 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[KLK10]] | B | KLK10 activity raises PLEK2's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 4.62× lower at baseline in the lines without KLK10 | 0.015 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[S100A16]] | B | S100A16 activity raises PLEK2's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 4.50× lower at baseline in the lines without S100A16 | 0.016 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[ITGA2]] | B | ITGA2 activity raises PLEK2's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.80× lower at baseline in the lines without ITGA2 | 0.016 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[TOR4A]] | B | TOR4A activity raises PLEK2's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 4.33× lower at baseline in the lines without TOR4A | 0.017 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[SCEL]] | B | SCEL activity raises PLEK2's level | lines that do not express SCEL (35) vs lines expressing it (15) | 4.08× lower at baseline in the lines without SCEL | 0.022 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[F3]] | B | F3 activity raises PLEK2's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.32× lower at baseline in the lines without F3 | 0.030 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[SCAT1]] | B | SCAT1 activity raises PLEK2's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 2.62× lower at baseline in the lines without SCAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 48, C 9. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A16]] | B | PLEK2 activity raises S100A16's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.80× lower at baseline in the lines without PLEK2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[WNT7B]] | B | PLEK2 activity raises WNT7B's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without PLEK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[PLEKHM1P1]] | B | PLEK2 activity raises PLEKHM1P1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without PLEK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[TMCC3]] | B | PLEK2 activity raises TMCC3's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 3.11× lower at baseline in the lines without PLEK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[SLCO4A1]] | B | PLEK2 activity raises SLCO4A1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.18× lower at baseline in the lines without PLEK2 | 0.010 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[SERPINB1]] | B | PLEK2 activity raises SERPINB1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 3.05× lower at baseline in the lines without PLEK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[TGFA]] | B | PLEK2 activity raises TGFA's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.65× lower at baseline in the lines without PLEK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[NIBAN2]] | B | PLEK2 activity raises NIBAN2's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without PLEK2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[HPCAL1]] | B | PLEK2 activity raises HPCAL1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without PLEK2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[CIB1]] | B | PLEK2 activity raises CIB1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.00× lower at baseline in the lines without PLEK2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[GRB10]] | B | PLEK2 activity raises GRB10's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.48× lower at baseline in the lines without PLEK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[ABHD17C]] | B | PLEK2 activity raises ABHD17C's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.68× lower at baseline in the lines without PLEK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.903). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.7, 2.6); signed map (0.2, 45.3). **Vector** length 137, 46.7% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.8 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.6 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.7 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.7 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -7.9 | -10.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.8 | -10.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.7 | -9.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.6 | -10.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.5 | -8.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.4 | -9.5 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3-q24.1 — chr14:67,386,984-67,412,167 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; DEP domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYT0](https://www.uniprot.org/uniprotkb/Q9NYT0) (Pleckstrin-2):

> May help orchestrate cytoskeletal arrangement. Contribute to lamellipodia formation.

**Summary**, from NCBI Gene [26499](https://www.ncbi.nlm.nih.gov/gene/26499):

> The protein encoded by this gene associates with membrane-bound phosphatidylinositols generated by phosphatidylinositol 3-kinase. The encoded protein then interacts with the actin cytoskeleton to induce cell spreading. In conjunction with complement component 1, q subcomponent, B chain (C1QB), this gene shows an increase in expression in melanoma cells and may serve as an accurate biomarker for the disease. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:19238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19238) · Entrez [26499](https://www.ncbi.nlm.nih.gov/gene/26499) · UniProt [Q9NYT0](https://www.uniprot.org/uniprotkb/Q9NYT0) · Ensembl [ENSG00000100558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100558)

## Data

Gene col 1984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1984); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1984]; `tensor/DDL_lfc|DDL_z.npy` [1984]; `embed/gene_vectors.npy` [1984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1984 or target_col == 1984). Every well: [[PLEK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
