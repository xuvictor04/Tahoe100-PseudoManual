---
symbol: "TMC6"
type: "gene"
col: 6536
ensembl_id: "ENSG00000141524"
name: "transmembrane channel like 6"
location: "17q25.3"
module: 31
arm: "+"
pooled_cpm: 20.34
n_lines_expressing: 38
n_dd_up: 1
n_dd_down: 23
n_dd_up_clean: 1
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 82
direction_downstream: 41
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TMC6

*transmembrane channel like 6* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.87× (z +4.1, q 0.023, up in 4 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.504× (z -9.7, q 2e-19, down in 30 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GNT3]] (+0.74, fdr 7e-06), [[RDH13]] (+0.74, fdr 7e-06), [[PTK6]] (+0.72, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 82 arrows point to it, the strongest [[CDH1]] → it (grade B ⚠); 41 go from it, the strongest it → [[LPAR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.87×** | +4.1 | 0.023 | 4/34 (AsPC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.2 | 0.33 | 8/36 (PANC-1, KATO III, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | 1.55× | +3.1 | 0.35 | 6/33 (SW480, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6536.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.504×** | -9.7 | 2e-19 | 30/36 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -8.6 | 2e-15 | 22/35 (NCI-H2347, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.550×** | -8.1 | 8e-14 | 23/35 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.487×** | -8.0 | 2e-13 | 19/32 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.600×** | -7.2 | 5e-11 | 21/35 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.368×** | -7.1 | 1e-10 | 24/35 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.4 | 9e-09 | 19/34 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.673×** | -5.6 | 1e-06 | 18/35 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -4.7 | 2e-04 | 15/33 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -4.7 | 2e-04 | 18/34 (COLO 205, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.731×** | -4.4 | 5e-04 | 17/35 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -4.4 | 5e-04 | 14/35 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.745×** | -4.2 | 0.001 | 14/36 (COLO 205, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -4.1 | 0.002 | 2/36 (HOP62, A-172) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.586×** | -3.8 | 0.006 | 12/35 (LoVo, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.770×** | -3.7 | 0.008 | 18/36 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.777×** | -3.7 | 0.009 | 12/36 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 34.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -14.6) |
| [[COLO 205 (line)]] | alt | 54.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.3) |
| [[LS 180 (line)]] | wt | 42.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.1) |
| [[SW480 (line)]] | alt | 47.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -13.7) |
| [[HT-29 (line)]] | alt | 62.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 72.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -17.2) |
| [[RKO (line)]] | wt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0632× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 32.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.7) |
| [[HCT15 (line)]] | alt | 51.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 45.4 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.160× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 8.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0880× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[Panc 03.27 (line)]] | alt | 43.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.7) |
| [[SHP-77 (line)]] | alt | 8.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[SW48 (line)]] | wt | 52.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.7) |
| [[A-172 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GNT3]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[RDH13]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[PTK6]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ONECUT3]] | +0.71 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[LINC00659]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[HS3ST1]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SH2D3A]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[TTC9]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.67 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ARHGAP27]] | +0.67 | +0.67 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 79, C 3. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH1]] | B | CDH1 activity raises TMC6's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 5.19× lower at baseline in the lines without CDH1 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[CLDN7]] | B | CLDN7 activity raises TMC6's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 4.49× lower at baseline in the lines without CLDN7 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises TMC6's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.50× lower at baseline in the lines without TMPRSS4 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[CBLC]] | B | CBLC activity raises TMC6's level | lines that do not express CBLC (31) vs lines expressing it (19) | 4.40× lower at baseline in the lines without CBLC | 4e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[PRSS22]] | B | PRSS22 activity raises TMC6's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 4.57× lower at baseline in the lines without PRSS22 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[ATP2C2]] | B | ATP2C2 activity raises TMC6's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.36× lower at baseline in the lines without ATP2C2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[B3GNT3]] | B | B3GNT3 activity raises TMC6's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.12× lower at baseline in the lines without B3GNT3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[S100A14]] | B | S100A14 activity raises TMC6's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 4.42× lower at baseline in the lines without S100A14 | 8e-04 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[C1orf116]] | B | C1orf116 activity raises TMC6's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.30× lower at baseline in the lines without C1orf116 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[SLC5A1]] | B | SLC5A1 activity raises TMC6's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 4.63× lower at baseline in the lines without SLC5A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[PRSS8]] | B | PRSS8 activity raises TMC6's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 4.60× lower at baseline in the lines without PRSS8 | 0.001 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[SH2D3A]] | B | SH2D3A activity raises TMC6's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.88× lower at baseline in the lines without SH2D3A | 0.001 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 39, C 2. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPAR2]] | B | TMC6 activity raises LPAR2's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without TMC6 | 0.006 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[ACOT11]] | B | TMC6 activity raises ACOT11's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.03× lower at baseline in the lines without TMC6 | 0.007 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[KRT18]] | B | TMC6 activity raises KRT18's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.86× lower at baseline in the lines without TMC6 | 0.008 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[PARD6B]] | B | TMC6 activity raises PARD6B's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.03× lower at baseline in the lines without TMC6 | 0.010 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[DMKN]] | B | TMC6 activity raises DMKN's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.39× lower at baseline in the lines without TMC6 | 0.027 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[SPIRE2]] | B | TMC6 activity raises SPIRE2's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 1.99× lower at baseline in the lines without TMC6 | 0.036 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[RHOF]] | B | TMC6 activity raises RHOF's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 2.75× lower at baseline in the lines without TMC6 | 0.036 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[UNC13D]] | B | TMC6 activity raises UNC13D's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without TMC6 | 0.038 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[CRYBG2]] | B | TMC6 activity raises CRYBG2's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.21× lower at baseline in the lines without TMC6 | 0.038 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[GRB7]] | B | TMC6 activity raises GRB7's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 4.55× lower at baseline in the lines without TMC6 | 0.039 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[CARD10]] | B | TMC6 activity raises CARD10's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 2.03× lower at baseline in the lines without TMC6 | 0.043 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[PSD4]] | B | TMC6 activity raises PSD4's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 2.30× lower at baseline in the lines without TMC6 | 0.043 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.842). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 54.9); signed map (0.2, 38.1). **Vector** length 85.3, 22.8% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +1.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -3.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -9.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -7.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane channel like 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,107,397-78,132,407 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAK-4P, EVIN1; previously EVER1, TNRC6C-AS1 |
| Gene groups (HGNC) | Transmembrane channel like family |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z403](https://www.uniprot.org/uniprotkb/Q7Z403) (Transmembrane channel-like protein 6):

> Acts as a regulatory protein involved in the regulation of numerous cellular processes. Together with its homolog TMC8/EVER2, forms a complex with CIB1 in lymphocytes and keratynocytes where TMC6 and TMC8 stabilize CIB1 and reciprocally. Together with TMC8, also forms a complex with and activates zinc transporter ZNT1 at the ER membrane of keratynocytes, thereby facilitating zinc uptake into the ER. Down-regulates the activity of transcription factors induced by zinc and cytokines. Also plays a …

**Summary**, from NCBI Gene [11322](https://www.ncbi.nlm.nih.gov/gene/11322):

> Epidermodysplasia verruciformis (EV) is an autosomal recessive dermatosis characterized by abnormal susceptibility to human papillomaviruses (HPVs) and a high rate of progression to squamous cell carcinoma on sun-exposed skin. EV is caused by mutations in either of two adjacent genes located on chromosome 17q25.3. Both of these genes encode integral membrane proteins that localize to the endoplasmic reticulum and are predicted to form transmembrane channels. This gene encodes a transmembrane …

**Accessions** — [HGNC:18021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18021) · Entrez [11322](https://www.ncbi.nlm.nih.gov/gene/11322) · UniProt [Q7Z403](https://www.uniprot.org/uniprotkb/Q7Z403) · Ensembl [ENSG00000141524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141524)

## Data

Gene col 6536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6536); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6536]; `tensor/DDL_lfc|DDL_z.npy` [6536]; `embed/gene_vectors.npy` [6536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6536 or target_col == 6536). Every well: [[TMC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
