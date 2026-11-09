---
symbol: "LRRC17"
type: "gene"
col: 4903
ensembl_id: "ENSG00000128606"
name: "leucine rich repeat containing 17"
location: "7q22.1"
module: 10
arm: "+"
pooled_cpm: 5.94
n_lines_expressing: 23
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# LRRC17

*leucine rich repeat containing 17* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.82× (z +11.5, q 1e-27, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.74× (z +10.4, q 1e-22, up in 11 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Rifaximin (drug)]] 5 µM: 0.504× (z -4.9, q 6e-04, down in 6 of 19 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP38-DT]] (+0.62, fdr 3e-05), [[ZBED5-AS1]] (+0.60, fdr 3e-05), [[CAPN3]] (+0.58, fdr 2e-05); moves opposite to [[FAM118A]] (-0.55, fdr 9e-05), [[GRAMD4]] (-0.48, fdr 2e-04), [[MINK1]] (-0.48, fdr 4e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC01358]] → it (grade B ⚠); 9 go from it, the strongest it → [[AHI1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +11.5 | 1e-27 | 2/5 (A-172, CHP-212) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +10.4 | 1e-22 | 11/13 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.11×** | +9.9 | 7e-21 | 1/1 (A-172) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.80×** | +9.0 | 3e-17 | 1/2 (A-172) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +8.5 | 2e-15 | 5/10 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +7.6 | 3e-12 | 8/16 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.85×** | +6.3 | 2e-08 | 4/20 (A498, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +5.7 | 9e-07 | 7/20 (A498, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +5.1 | 3e-05 | 2/9 (A-172, CHP-212) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +4.5 | 4e-04 | 3/14 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.89×** | +4.4 | 4e-04 | 4/11 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.11×** | +4.3 | 7e-04 | 1/2 (A-172) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +3.9 | 0.005 | 3/20 (KATO III, SW 1088, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.017 | 2/21 (CHP-212, C32) | inconsistent across doses | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.038 | 3/21 (A-172, A498, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +3.3 | 0.040 | 3/14 (SW480, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.0 | 0.078 | 4/19 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +3.0 | 0.086 | 5/20 (A498, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +2.9 | 0.099 | 4/18 (HCT15, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +2.9 | 0.099 | 3/21 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rifaximin (drug)]] 5 µM |  | **0.504×** | -4.9 | 6e-04 | 6/19 (hTERT-HPNE, NCI-H23, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.538×** | -4.0 | 0.019 | 8/17 (A-172, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.608×** | -3.6 | 0.050 | 6/20 (SNU-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Pimitespib (drug)]] 0.05 µM |  | 0.637× | -3.2 | 0.23 | 2/18 (SW480, SW 1088) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 176 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.8) |
| [[A-427 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.952 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP38-DT]] | +0.62 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ZBED5-AS1]] | +0.60 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[CAPN3]] | +0.58 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SLCO1B1]] | +0.56 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[CFAP20DC-DT]] | +0.55 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[THBS4-AS1]] | +0.55 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[ST8SIA5]] | +0.54 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[CCDC162P]] | +0.54 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[NEB]] | +0.54 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[DYNLRB2-AS1]] | +0.54 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[B3GNT9]] | +0.54 | +0.43 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.55 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[GRAMD4]] | -0.48 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[MINK1]] | -0.48 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[ETHE1]] | -0.47 | -0.36 / -0.21 | both halves | 7e-04 |  |
| [[ANKS6]] | -0.46 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[ZFYVE28]] | -0.46 | -0.46 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[LPCAT1]] | -0.46 | -0.45 / -0.19 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01358]] | B | LINC01358 activity raises LRRC17's level | lines that do not express LINC01358 (14) vs lines expressing it (36) | 1.19× lower at baseline in the lines without LINC01358 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LRRC17's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC2-AS2]] | B | HDAC2-AS2 activity raises LRRC17's level | lines that do not express HDAC2-AS2 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without HDAC2-AS2 | 0.073 | ⚠ within organs, on part of the lines; also absent: OPN3, ACVR1C, METTL21EP-1; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHI1-DT]] | B | LRRC17 activity raises AHI1-DT's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.54× lower at baseline in the lines without LRRC17 | 0.024 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[MINK1]] | B | LRRC17 activity raises MINK1's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.27× lower at baseline in the lines without LRRC17 | 0.026 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[CFAP20DC-DT]] | B | LRRC17 activity raises CFAP20DC-DT's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without LRRC17 | 0.028 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[DNAH12]] | B | LRRC17 activity raises DNAH12's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.50× lower at baseline in the lines without LRRC17 | 0.037 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[IPO9-AS1]] | B | LRRC17 activity raises IPO9-AS1's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.30× lower at baseline in the lines without LRRC17 | 0.042 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[COPZ2]] | B | LRRC17 activity raises COPZ2's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without LRRC17 | 0.051 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | B | LRRC17 activity raises XNDC1N-ZNF705EP-ALG1L9P's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.36× lower at baseline in the lines without LRRC17 | 0.077 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[THBS4-AS1]] | B | LRRC17 activity raises THBS4-AS1's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.61× lower at baseline in the lines without LRRC17 | 0.088 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[DIRAS3]] | C | LRRC17 activity raises DIRAS3's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.73× lower at baseline in the lines without LRRC17 | 0.050 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.547). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.2, 17.3); signed map (29.1, -11.2). **Vector** length 26.4, 3.83% of its response variance represented; |z| ≥ 3 in 475 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.5 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.9 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.6 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -1.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -0.5 | -2.4 |
|  | [[Tirabrutinib (drug)]] 5 µM |  | -0.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,913,000-102,945,111 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P37NB, H_RG318M05.3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6Y2](https://www.uniprot.org/uniprotkb/Q8N6Y2) (Leucine-rich repeat-containing protein 17):

> Involved in bone homeostasis. Acts as a negative regulator of RANKL-induced osteoclast precursor differentiation from bone marrow precursors (By similarity).

**Summary**, from NCBI Gene [10234](https://www.ncbi.nlm.nih.gov/gene/10234):

> Predicted to enable signaling receptor activity. Predicted to be involved in bone marrow development and negative regulation of osteoclast differentiation. Predicted to be located in obsolete extracellular space. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16895) · Entrez [10234](https://www.ncbi.nlm.nih.gov/gene/10234) · UniProt [Q8N6Y2](https://www.uniprot.org/uniprotkb/Q8N6Y2) · Ensembl [ENSG00000128606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128606)

## Data

Gene col 4903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4903); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4903]; `tensor/DDL_lfc|DDL_z.npy` [4903]; `embed/gene_vectors.npy` [4903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4903 or target_col == 4903). Every well: [[LRRC17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
