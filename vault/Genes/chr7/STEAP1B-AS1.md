---
symbol: "STEAP1B-AS1"
type: "gene"
col: 13867
ensembl_id: "ENSG00000232759"
name: "STEAP1B antisense RNA 1"
location: "7p15.3"
module: 19
arm: "+"
pooled_cpm: 4.77
n_lines_expressing: 20
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 10
direction_downstream: 17
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# STEAP1B-AS1

*STEAP1B antisense RNA 1* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.95× (z +12.2, q 3e-31, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 1.58× (z +3.6, q 0.031, up in 1 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.346× (z -8.4, q 2e-14, down in 16 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL6]] (+0.67, fdr 7e-06), [[VEGFC]] (+0.65, fdr 7e-06), [[SERPIND1]] (+0.64, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[IL6]] → it (grade C ⚠); 17 go from it, the strongest it → [[RMDN2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.95×** | +12.2 | 3e-31 | 3/10 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.93×** | +10.8 | 8e-25 | 6/12 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.85×** | +9.9 | 1e-20 | 5/11 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.3 | 2e-05 | 2/12 (HOP62, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.54×** | +5.2 | 2e-05 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.031 | 1/15 (HOP62) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.5 | 0.033 | 1/15 (J82) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.035 | 6/18 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.052 | 1/14 (NCI-H460) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.2 | 0.079 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.2 | 0.079 | 0/13 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.72× | +3.0 | 0.11 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.346×** | -8.4 | 2e-14 | 16/17 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.415×** | -7.0 | 9e-10 | 15/16 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.438×** | -6.5 | 1e-08 | 16/17 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.532×** | -5.0 | 8e-05 | 12/17 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.608×** | -4.0 | 0.008 | 8/17 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.627×** | -3.7 | 0.020 | 8/17 (HOP62, SNU-423, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.642×** | -3.5 | 0.034 | 5/17 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.663×** | -3.3 | 0.075 | 6/17 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.665×** | -3.2 | 0.088 | 8/18 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.662×** | -3.2 | 0.088 | 9/16 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.653×** | -3.1 | 0.088 | 0/17 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.9 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0330× (z -22.6) |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0175× (z -16.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0290× (z -15.4) |
| [[HOP62 (line)]] | alt | 9.25 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0895× (z -11.0) |
| [[J82 (line)]] | alt | 8.21 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0936× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.109× (z -10.8) |
| [[SNU-423 (line)]] | alt | 29.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0430× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0912× (z -10.3) |
| [[HS-578T (line)]] | alt | 7.19 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0223× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 6.31 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -8.8) |
| [[PANC-1 (line)]] | alt | 5.56 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -9.3) |
| [[A-172 (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.312 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL6]] | +0.67 | +0.61 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[VEGFC]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SERPIND1]] | +0.64 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[CDH11]] | +0.64 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PDCD1LG2]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[GJA1]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CRLF2]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[NCKAP5]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SLC16A6]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[GNG11]] | +0.60 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[BMPER]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PDE7B]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL6]] | C | IL6 activity raises STEAP1B-AS1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 4.42× lower at baseline in the lines without IL6 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[GLIS3]] | C | GLIS3 activity raises STEAP1B-AS1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.13× lower at baseline in the lines without GLIS3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO; co-absent with the target |
| [[ODAD2]] | C | ODAD2 activity raises STEAP1B-AS1's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without ODAD2 | 0.025 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[FENDRR]] | C | FENDRR activity raises STEAP1B-AS1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 2.95× lower at baseline in the lines without FENDRR | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[LINC02742]] | C | LINC02742 activity raises STEAP1B-AS1's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without LINC02742 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227; co-absent with the target |
| [[GNG11]] | C | GNG11 activity raises STEAP1B-AS1's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 2.90× lower at baseline in the lines without GNG11 | 0.048 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises STEAP1B-AS1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 3.09× lower at baseline in the lines without PAPPA | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[FLI1]] | C | FLI1 activity raises STEAP1B-AS1's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 2.99× lower at baseline in the lines without FLI1 | 0.079 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615; co-absent with the target |
| [[ABCC9]] | C | ABCC9 activity raises STEAP1B-AS1's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 2.33× lower at baseline in the lines without ABCC9 | 0.083 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[LYPLAL1-DT]] | C | LYPLAL1-DT activity raises STEAP1B-AS1's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without LYPLAL1-DT | 0.086 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 2, C 15. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RMDN2-AS1]] | B | STEAP1B-AS1 activity raises RMDN2-AS1's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without STEAP1B-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1 |
| [[EXT1]] | B | STEAP1B-AS1 activity raises EXT1's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without STEAP1B-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1 |
| [[GLIS3]] | C | STEAP1B-AS1 activity raises GLIS3's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 6.02× lower at baseline in the lines without STEAP1B-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[IL6]] | C | STEAP1B-AS1 activity raises IL6's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 9.97× lower at baseline in the lines without STEAP1B-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[DNAH11]] | C | STEAP1B-AS1 activity raises DNAH11's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 4.57× lower at baseline in the lines without STEAP1B-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[INHBA]] | C | STEAP1B-AS1 activity raises INHBA's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 5.06× lower at baseline in the lines without STEAP1B-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[CYP1B1]] | C | STEAP1B-AS1 activity raises CYP1B1's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 3.77× lower at baseline in the lines without STEAP1B-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[SHISAL1]] | C | STEAP1B-AS1 activity raises SHISAL1's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 3.05× lower at baseline in the lines without STEAP1B-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[LYPLAL1-DT]] | C | STEAP1B-AS1 activity raises LYPLAL1-DT's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 2.19× lower at baseline in the lines without STEAP1B-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[BMPER]] | C | STEAP1B-AS1 activity raises BMPER's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 3.53× lower at baseline in the lines without STEAP1B-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[PDCD1LG2]] | C | STEAP1B-AS1 activity raises PDCD1LG2's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 2.64× lower at baseline in the lines without STEAP1B-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[HMGN2P46]] | C | STEAP1B-AS1 activity raises HMGN2P46's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without STEAP1B-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.4, 16.2); signed map (20.1, 52.5). **Vector** length 63.5, 20.7% of its response variance represented; |z| ≥ 3 in 535 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.9 | +0.3 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | -7.0 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | STEAP1B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p15.3 — chr7:22,563,337-22,573,996 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56137) · Entrez [100506178](https://www.ncbi.nlm.nih.gov/gene/100506178) · Ensembl [ENSG00000232759](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232759)

## Data

Gene col 13867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13867); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13867]; `tensor/DDL_lfc|DDL_z.npy` [13867]; `embed/gene_vectors.npy` [13867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13867 or target_col == 13867). Every well: [[STEAP1B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STEAP1B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
