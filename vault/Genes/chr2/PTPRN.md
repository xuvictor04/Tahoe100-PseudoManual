---
symbol: "PTPRN"
type: "gene"
col: 608
ensembl_id: "ENSG00000054356"
name: "protein tyrosine phosphatase receptor type N"
location: "2q35"
module: 13
arm: "+"
pooled_cpm: 5.98
n_lines_expressing: 19
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 19
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PTPRN

*protein tyrosine phosphatase receptor type N* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.60× (z +10.5, q 6e-23, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.11× (z +6.1, q 1e-07, up in 7 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.567× (z -4.3, q 0.011, down in 1 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBB2A]] (+0.58, fdr 1e-05), [[LINC01060]] (+0.57, fdr 1e-05), [[TIMP3]] (+0.57, fdr 1e-05); moves opposite to [[PANK1]] (-0.47, fdr 4e-05), [[AGAP13P]] (-0.46, fdr 7e-05), [[NFIA]] (-0.45, fdr 8e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCDC3]] → it (grade B ⚠); 19 go from it, the strongest it → [[CLIP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.60×** | +10.5 | 6e-23 | 3/9 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +10.1 | 2e-21 | 4/9 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +7.6 | 7e-12 | 4/9 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +6.1 | 1e-07 | 7/15 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.95×** | +5.2 | 3e-05 | 7/15 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.30×** | +4.8 | 1e-04 | 5/10 (SHP-77, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +4.8 | 1e-04 | 4/16 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +4.5 | 4e-04 | 8/15 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.00×** | +4.0 | 0.004 | 1/9 (A-172) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +3.5 | 0.024 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.024 | 4/13 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.027 | 1/14 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.4 | 0.033 | 1/11 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.039 | 4/11 (A-172, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.2 | 0.046 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.055 | 8/15 (NCI-H460, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.095 | 6/15 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 608.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.567×** | -4.3 | 0.011 | 1/16 (A498) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.592×** | -4.0 | 0.021 | 0/17 | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.616×** | -3.8 | 0.028 | 1/13 (SNU-423) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.681× | -3.1 | 0.25 | 6/15 (C-33 A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.767× | -3.1 | 0.25 | 6/16 (C-33 A, NCI-H460, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.671× | -3.0 | 0.25 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.87× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 27.9 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.657 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB2A]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[LINC01060]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TIMP3]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[APCDD1L-DT]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TUBA1A]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[IGFBP6]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TCTA]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[CRMP1]] | +0.53 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[ARMCX2]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ALK]] | +0.53 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[LINC01615]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PANK1]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 | same gene group |
| [[AGAP13P]] | -0.46 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[NFIA]] | -0.45 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[PDCD6P1]] | -0.43 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[CAVIN2]] | -0.43 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC3]] | B | CCDC3 activity lowers PTPRN's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 1.47× higher at baseline in the lines without CCDC3 | 0.095 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent |
| [[CRMP1]] | C | CRMP1 activity raises PTPRN's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 3.16× lower at baseline in the lines without CRMP1 | 0.084 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLIP3]] | B | PTPRN activity raises CLIP3's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.29× lower at baseline in the lines without PTPRN | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1 |
| [[ZFPM2]] | B | PTPRN activity raises ZFPM2's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.21× lower at baseline in the lines without PTPRN | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1 |
| [[SORCS1]] | B | PTPRN activity raises SORCS1's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.69× lower at baseline in the lines without PTPRN | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1 |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | B | PTPRN activity lowers the cells' numbers under Docetaxel (Trihydrate) 5 µM (makes them more sensitive) | lines that do not express PTPRN (31) vs lines expressing it (17) | the lines without PTPRN: 1.23× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1 |
| [[CSPG4]] | C | PTPRN activity raises CSPG4's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 3.55× lower at baseline in the lines without PTPRN | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[CRMP1]] | C | PTPRN activity raises CRMP1's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 3.07× lower at baseline in the lines without PTPRN | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[MEG8]] | C | PTPRN activity raises MEG8's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.48× lower at baseline in the lines without PTPRN | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[MEG3]] | C | PTPRN activity raises MEG3's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.70× lower at baseline in the lines without PTPRN | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[ARMCX2]] | C | PTPRN activity raises ARMCX2's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without PTPRN | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[MAP1A]] | C | PTPRN activity raises MAP1A's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 3.68× lower at baseline in the lines without PTPRN | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[APCDD1L]] | C | PTPRN activity raises APCDD1L's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.80× lower at baseline in the lines without PTPRN | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[GPR173]] | C | PTPRN activity raises GPR173's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 3.23× lower at baseline in the lines without PTPRN | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (57.1, 17.1); signed map (23.6, 49.1). **Vector** length 38.8, 9.75% of its response variance represented; |z| ≥ 3 in 371 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.8 | -0.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type N |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,289,623-219,309,648 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IA-2, ICA512 |
| Gene groups (HGNC) | Protein tyrosine phosphatases receptor type; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16849](https://www.uniprot.org/uniprotkb/Q16849) (Receptor-type tyrosine-protein phosphatase-like N):

> Plays a role in vesicle-mediated secretory processes. Required for normal accumulation of secretory vesicles in hippocampus, pituitary and pancreatic islets (By similarity). Required for the accumulation of normal levels of insulin-containing vesicles and preventing their degradation. Plays a role in insulin secretion in response to glucose stimuli. Required for normal accumulation of the neurotransmitters norepinephrine, dopamine and serotonin in the brain (By similarity). In females, but not …

**Summary**, from NCBI Gene [5798](https://www.ncbi.nlm.nih.gov/gene/5798):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and a single catalytic domain, and thus represents a receptor-type PTP. This PTP was found to be an autoantigen that is reactive with insulin-dependent …

**Accessions** — [HGNC:9676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9676) · Entrez [5798](https://www.ncbi.nlm.nih.gov/gene/5798) · UniProt [Q16849](https://www.uniprot.org/uniprotkb/Q16849) · Ensembl [ENSG00000054356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054356)

## Data

Gene col 608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 608); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 608]; `tensor/DDL_lfc|DDL_z.npy` [608]; `embed/gene_vectors.npy` [608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 608 or target_col == 608). Every well: [[PTPRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
