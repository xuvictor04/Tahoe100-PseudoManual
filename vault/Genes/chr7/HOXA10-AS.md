---
symbol: "HOXA10-AS"
type: "gene"
col: 14788
ensembl_id: "ENSG00000253187"
name: "HOXA10 antisense RNA"
location: "7p15.2"
module: 11
arm: "+"
pooled_cpm: 2.29
n_lines_expressing: 29
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# HOXA10-AS

*HOXA10 antisense RNA* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.23× (z +10.4, q 1e-22, up in 12 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.501× (z -4.3, q 0.008, down in 10 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA7]] (+0.76, fdr 7e-06, ⚠ same locus), [[HNF1A]] (+0.69, fdr 1e-05), [[PPCS]] (+0.67, fdr 1e-05), [[RPP25L]] (+0.64, fdr 1e-05); moves opposite to [[FAM91A1]] (-0.59, fdr 3e-05), [[INTS1]] (-0.57, fdr 2e-05), [[TPD52L2]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GASK1B-AS1]] → it (grade B ⚠); 7 go from it, the strongest it → [[MDP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +10.4 | 1e-22 | 12/14 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.69×** | +8.2 | 6e-14 | 3/9 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.24×** | +7.1 | 2e-10 | 1/4 (A498) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.18×** | +6.7 | 3e-09 | 2/5 (SW1417, HT-29) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +5.0 | 5e-05 | 7/9 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.01×** | +4.4 | 0.001 | 4/10 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.51×** | +3.7 | 0.020 | 9/19 (LS 180, SW48, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.023 | 1/25 (HEC-1-A) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.4 | 0.044 | 2/12 (SW480, LoVo) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.3 | 0.044 | 2/18 (SW 900, COLO 205) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.3 | 0.044 | 2/13 (HEC-1-A, SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.3 | 0.044 | 3/12 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.2 | 0.058 | 3/10 (KATO III, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14788.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.501×** | -4.3 | 0.008 | 10/24 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +11.4) | — |
| [[A-172 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.578 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.746 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.579 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.605 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.606 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.675 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA7]] | +0.76 | +0.62 / +0.80 | both halves | 7e-06 | ⚠ same locus (10.7 kb: neighbours can correlate without regulation) |
| [[HNF1A]] | +0.69 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PPCS]] | +0.67 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[RPP25L]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[FDX2]] | +0.63 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[STAP2]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SRSF8]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[HOXA10]] | +0.61 | +0.39 / +0.66 | both halves | 5e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[EID2]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[UQCRFS1]] | +0.59 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZNF827]] | +0.58 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[C1orf131]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[METTL18]] | +0.57 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM91A1]] | -0.59 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[INTS1]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.56 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[CALU]] | -0.55 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[GALNS]] | -0.55 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[GGCX]] | -0.53 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[APMAP]] | -0.52 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[ZNF731P]] | -0.52 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[RSU1]] | -0.51 | -0.32 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GASK1B-AS1]] | B | GASK1B-AS1 activity raises HOXA10-AS's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 1.23× lower at baseline in the lines without GASK1B-AS1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB |
| [[TOP2A]] | B | TOP2A activity lowers HOXA10-AS's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXA9]] | C | HOXA9 activity raises HOXA10-AS's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without HOXA9 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33; co-absent with the target |
| [[HOXA11]] | C | HOXA11 activity raises HOXA10-AS's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without HOXA11 | 0.016 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3; co-absent with the target |
| [[HOXA10]] | C | HOXA10 activity raises HOXA10-AS's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 1.72× lower at baseline in the lines without HOXA10 | 0.042 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDP1]] | B | HOXA10-AS activity lowers MDP1's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 1.21× higher at baseline in the lines without HOXA10-AS | 0.031 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent |
| [[SCAF11]] | B | HOXA10-AS activity raises SCAF11's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 1.11× lower at baseline in the lines without HOXA10-AS | 0.072 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent |
| [[PITX1]] | B | HOXA10-AS activity raises PITX1's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without HOXA10-AS | 0.086 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent |
| [[SCGB2B2]] | B | HOXA10-AS activity lowers SCGB2B2's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 1.33× higher at baseline in the lines without HOXA10-AS | 0.096 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent |
| [[HOXA10]] | C | HOXA10-AS activity raises HOXA10's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 3.95× lower at baseline in the lines without HOXA10-AS | 0.002 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent; co-absent with the target |
| [[HOXA9]] | C | HOXA10-AS activity raises HOXA9's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 4.77× lower at baseline in the lines without HOXA10-AS | 0.007 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent; co-absent with the target |
| [[HOXA11]] | C | HOXA10-AS activity raises HOXA11's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 3.09× lower at baseline in the lines without HOXA10-AS | 0.013 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-0.3, 28.1); signed map (2.0, -18.2). **Vector** length 32.7, 5.68% of its response variance represented; |z| ≥ 3 in 433 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.4 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.0 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | HOXA10 antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p15.2 — chr7:27,168,619-27,171,915 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously HOXA-AS4 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100874323](https://www.ncbi.nlm.nih.gov/gene/100874323):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:40281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40281) · Entrez [100874323](https://www.ncbi.nlm.nih.gov/gene/100874323) · Ensembl [ENSG00000253187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253187)

## Data

Gene col 14788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14788); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14788]; `tensor/DDL_lfc|DDL_z.npy` [14788]; `embed/gene_vectors.npy` [14788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14788 or target_col == 14788). Every well: [[HOXA10-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA10-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
