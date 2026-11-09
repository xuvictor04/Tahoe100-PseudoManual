---
symbol: "PAPPA"
type: "gene"
col: 11322
ensembl_id: "ENSG00000182752"
name: "pappalysin 1"
location: "9q33.1"
module: 13
arm: "+"
pooled_cpm: 66.05
n_lines_expressing: 17
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 46
direction_downstream: 74
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PAPPA

*pappalysin 1* — 9q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.48× (z +8.5, q 1e-14, up in 1 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.67× (z +4.9, q 1e-04, up in 7 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.429× (z -8.3, q 9e-14, down in 14 of 14 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EVC2]] (+0.71, fdr 7e-06), [[GLIS3]] (+0.70, fdr 7e-06), [[MIR137HG]] (+0.68, fdr 7e-06); moves opposite to [[ANXA11]] (-0.45, fdr 6e-05), [[DENND11]] (-0.42, fdr 3e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[NOXA1]] → it (grade B ⚠); 74 go from it, the strongest it → [[STEAP1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +8.5 | 1e-14 | 1/13 (H4) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +7.7 | 4e-12 | 2/14 (HOP62, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +6.0 | 4e-07 | 2/13 (J82, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.67×** | +4.9 | 1e-04 | 7/14 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.41×** | +3.3 | 0.094 | 7/15 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.41×** | +3.3 | 0.094 | 2/16 (J82, hTERT-HPNE) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.39× | +3.1 | 0.17 | 3/14 (J82, RPMI-7951, …) | top dose only |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.37× | +3.0 | 0.18 | 5/15 (J82, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.429×** | -8.3 | 9e-14 | 14/14 (NCI-H1792, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -7.0 | 7e-10 | 15/15 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.509×** | -6.6 | 9e-09 | 15/15 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -6.2 | 1e-07 | 13/15 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.548×** | -5.9 | 5e-07 | 12/14 (NCI-H1792, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.569×** | -5.5 | 4e-06 | 13/14 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.597×** | -5.0 | 4e-05 | 9/15 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.446×** | -4.1 | 0.003 | 12/16 (hTERT-HPNE, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.709×** | -3.4 | 0.048 | 11/14 (NCI-H1792, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~22% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 319 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0454× (z -18.3) |
| [[NCI-H1792 (line)]] | alt | 320 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0358× (z -22.0) |
| [[SNU-423 (line)]] | alt | 331 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0364× (z -18.8) |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 848 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0358× (z -19.2) |
| [[NCI-H2030 (line)]] | alt | 95.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -20.4) |
| [[A549 (line)]] | wt | 612 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0248× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 141 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0890× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 21.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.1) |
| [[CHP-212 (line)]] | wt | 60.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0622× (z -9.0) |
| [[J82 (line)]] | alt | 51.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -9.0) |
| [[HOP62 (line)]] | alt | 49.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.08 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.45 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.95 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.18 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.76 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.69 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.71 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.31 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EVC2]] | +0.71 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[GLIS3]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[MIR137HG]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MSC-AS1]] | +0.60 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[OR9Q1]] | +0.60 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[PRRX1]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[WNT5A]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[TRPA1]] | +0.58 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[PDE3A]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ODAD2]] | +0.57 | +0.58 / +0.35 | both halves | 1e-04 | **novel candidate** |
| [[VEGFC]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CLMP]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA11]] | -0.45 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[DENND11]] | -0.42 | -0.38 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 3, C 43. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | NOXA1 activity lowers PAPPA's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 5.53× higher at baseline in the lines without NOXA1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PAPPA's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TFPI]] | B | TFPI activity raises PAPPA's level | lines that do not express TFPI (14) vs lines expressing it (36) | 3.60× lower at baseline in the lines without TFPI | 0.089 | ⚠ within organs, on part of the lines; also absent: STC1, C2orf74-DT, CALCRL |
| [[APBB1IP]] | C | APBB1IP activity raises PAPPA's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 10.01× lower at baseline in the lines without APBB1IP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises PAPPA's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 6.57× lower at baseline in the lines without ADAM12 | 0.002 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises PAPPA's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 7.38× lower at baseline in the lines without MSC-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises PAPPA's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 5.89× lower at baseline in the lines without SPOCK1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises PAPPA's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 6.36× lower at baseline in the lines without CDH13 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises PAPPA's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 5.74× lower at baseline in the lines without ADAMTS12 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises PAPPA's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 6.52× lower at baseline in the lines without TRPA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[HTRA3]] | C | HTRA3 activity raises PAPPA's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 6.44× lower at baseline in the lines without HTRA3 | 0.007 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN; co-absent with the target |
| [[MSC]] | C | MSC activity raises PAPPA's level | lines that do not express MSC (34) vs lines expressing it (16) | 5.73× lower at baseline in the lines without MSC | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |

### Downstream of this gene

*74 arrows, 74 of them with an alert ⚠; grade A 0, B 24, C 50. Shown: the 12 strongest; 62 more arrows (62 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP1B]] | B | PAPPA activity raises STEAP1B's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without PAPPA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[SLCO1C1]] | B | PAPPA activity raises SLCO1C1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 2.04× lower at baseline in the lines without PAPPA | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[TFPI]] | B | PAPPA activity raises TFPI's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 3.87× lower at baseline in the lines without PAPPA | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[CCDC102B]] | B | PAPPA activity strengthens CCDC102B's drug response | lines that do not express PAPPA (25) vs lines expressing it (14) | the lines without PAPPA respond 0.66× as strongly (z diff +1.37); strongest at Vinblastine (sulfate) 5 µM: 0.71x vs 0.43x (z diff +3.0) | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; target measured in part of the lines; artifact flags |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | PAPPA activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 1.54× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| cells under [[Arbutin (drug)]] 5 µM | B | PAPPA activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.79× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | PAPPA activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 1.20× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[WIPF1]] | B | PAPPA activity raises WIPF1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 4.64× lower at baseline in the lines without PAPPA | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | PAPPA activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.81× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | B | PAPPA activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 1.34× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| cells under [[Malotilate (drug)]] 0.05 µM | B | PAPPA activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.79× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| cells under [[γ-Oryzanol (drug)]] 0.05 µM | B | PAPPA activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.6, 20.6); signed map (27.4, 48.2). **Vector** length 74.3, 29.2% of its response variance represented; |z| ≥ 3 in 508 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.4 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -5.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | pappalysin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.1 — chr9:116,153,791-116,402,321 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAPP-A, PAPPA1, IGFBP-4ase, PAPA, ASBABP2, DIPLA1 |
| Gene groups (HGNC) | Pappalysins; Sushi domain containing |
| Reactome | 1 pathways, smallest: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13219](https://www.uniprot.org/uniprotkb/Q13219) (Pappalysin-1):

> Metalloproteinase which specifically cleaves IGFBP-4 and IGFBP-5, resulting in release of bound IGF. Cleavage of IGFBP-4 is dramatically enhanced by the presence of IGF, whereas cleavage of IGFBP-5 is slightly inhibited by the presence of IGF.

**Summary**, from NCBI Gene [5069](https://www.ncbi.nlm.nih.gov/gene/5069):

> This gene encodes a secreted metalloproteinase which cleaves insulin-like growth factor binding proteins (IGFBPs). Following IGFBP cleavage, insulin growth factors dissociate from IGFBPs and bind to IGF receptors, resulting in activation of the IGF pathway. The encoded protein plays a role in bone formation, inflammation, wound healing and female fertility. Enhanced expression of this protein is associated with diabetic nephropathy in human patients and this protein may promote tumor invasion …

**Accessions** — [HGNC:8602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8602) · Entrez [5069](https://www.ncbi.nlm.nih.gov/gene/5069) · UniProt [Q13219](https://www.uniprot.org/uniprotkb/Q13219) · Ensembl [ENSG00000182752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182752)

## Data

Gene col 11322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11322); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11322]; `tensor/DDL_lfc|DDL_z.npy` [11322]; `embed/gene_vectors.npy` [11322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11322 or target_col == 11322). Every well: [[PAPPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAPPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
