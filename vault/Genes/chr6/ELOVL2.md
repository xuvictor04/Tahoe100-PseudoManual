---
symbol: "ELOVL2"
type: "gene"
col: 12504
ensembl_id: "ENSG00000197977"
name: "ELOVL fatty acid elongase 2"
location: "6p24.2"
module: 19
arm: "+"
pooled_cpm: 11.78
n_lines_expressing: 19
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ELOVL2

*ELOVL fatty acid elongase 2* — 6p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.78× (z +19.7, q 0e+00, up in 11 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.08× (z +13.0, q 9e-37, up in 6 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (J82 0.0799×; ⚠ transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (A-427 0.315×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (A-172 0.170×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHD3]] (+0.61, fdr 1e-05), [[P3H2]] (+0.57, fdr 2e-05), [[PIEZO2]] (+0.57, fdr 1e-05); moves opposite to [[MIR4458HG]] (-0.47, fdr 8e-05), [[CCDC32]] (-0.44, fdr 6e-05), [[TTC9C]] (-0.43, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[EFR3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.78×** | +19.7 | 0e+00 | 11/13 (SNU-423, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.63×** | +15.1 | 0e+00 | 7/11 (SNU-423, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.40×** | +14.9 | 0e+00 | 10/11 (SNU-423, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +13.0 | 9e-37 | 6/16 (SNU-423, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +12.0 | 2e-31 | 4/16 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +10.2 | 2e-22 | 11/16 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +6.8 | 8e-10 | 13/16 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.2 | 1e-05 | 1/15 (J82) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.0 | 4e-05 | 1/15 (SHP-77) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.8 | 8e-05 | 12/17 (SK-MEL-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.3 | 8e-04 | 2/16 (SNU-423, PANC-1) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.41×** | +4.3 | 8e-04 | 6/16 (SK-MEL-2, J82, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.39×** | +4.2 | 0.001 | 6/17 (SK-MEL-2, SW 900, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.1 | 0.002 | 3/15 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.005 | 8/16 (SHP-77, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.036 | 7/16 (NCI-H23, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12504.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (J82 0.0799×; ⚠ transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (A-427 0.315×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (A-172 0.170×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.749× | -3.7 | 0.14 | 7/17 (A-172, C32, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.5 | 0.14 | 3/17 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.772× | -3.3 | 0.20 | 2/16 (NCI-H2030, HepG2/C3A) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.842× | -3.1 | 0.29 | 4/17 (PANC-1, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.170× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 4.37 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0799× (z -8.9) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 2.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +8.8) | — |
| [[A498 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD3]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[P3H2]] | +0.57 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[PIEZO2]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[NRXN3]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[NEGR1]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ADAMTS3]] | +0.55 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CNKSR2]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PDE1C]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ADD2]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[COL8A1]] | +0.53 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[EYA2]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[NCAM2]] | +0.52 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4458HG]] | -0.47 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[CCDC32]] | -0.44 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[TTC9C]] | -0.43 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[TRAPPC2L]] | -0.43 | -0.29 / -0.37 | both halves | 3e-04 |  |
| [[ORAI3]] | -0.42 | -0.22 / -0.54 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ELOVL2's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[P3H2]] | C | P3H2 activity raises ELOVL2's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without P3H2 | 0.080 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFR3B]] | B | ELOVL2 activity raises EFR3B's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 2.08× lower at baseline in the lines without ELOVL2 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046 |
| [[DCLK2]] | B | ELOVL2 activity raises DCLK2's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 2.87× lower at baseline in the lines without ELOVL2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046 |
| [[GABBR2]] | B | ELOVL2 activity raises GABBR2's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without ELOVL2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046 |
| [[CACNG6]] | B | ELOVL2 activity raises CACNG6's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 1.81× lower at baseline in the lines without ELOVL2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046 |
| [[CDH19]] | C | ELOVL2 activity raises CDH19's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 3.03× lower at baseline in the lines without ELOVL2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046; co-absent with the target |
| [[CNKSR2]] | C | ELOVL2 activity raises CNKSR2's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 3.77× lower at baseline in the lines without ELOVL2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046; co-absent with the target |
| [[ARNT2]] | C | ELOVL2 activity raises ARNT2's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 2.32× lower at baseline in the lines without ELOVL2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046; co-absent with the target |
| [[KCNQ5]] | C | ELOVL2 activity raises KCNQ5's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 4.58× lower at baseline in the lines without ELOVL2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046; co-absent with the target |
| [[ATRNL1]] | C | ELOVL2 activity raises ATRNL1's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 1.93× lower at baseline in the lines without ELOVL2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.8, 32.2); signed map (39.6, 45.4). **Vector** length 52.7, 16.0% of its response variance represented; |z| ≥ 3 in 453 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +19.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +15.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.6 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ELOVL fatty acid elongase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.2 — chr6:10,980,759-11,044,305 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ssc2 |
| Gene groups (HGNC) | ELOVL fatty acid elongase family |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 7 pathways, smallest: Linoleic acid (LA) metabolism; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism; alpha-linolenic acid (ALA) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXB9](https://www.uniprot.org/uniprotkb/Q9NXB9) (Very long chain fatty acid elongase 2):

> Catalyzes the first and rate-limiting reaction of the four reactions that constitute the long-chain fatty acids elongation cycle. This endoplasmic reticulum-bound enzymatic process allows the addition of 2 carbons to the chain of long- and very long-chain fatty acids (VLCFAs) per cycle. Condensing enzyme that catalyzes the synthesis of polyunsaturated very long chain fatty acid (C20- and C22-PUFA), acting specifically toward polyunsaturated acyl-CoA with the higher activity toward C20:4(n-6) …

**Summary**, from NCBI Gene [54898](https://www.ncbi.nlm.nih.gov/gene/54898):

> Enables fatty acid elongase activity. Involved in fatty acid elongation, polyunsaturated fatty acid and very long-chain fatty acid biosynthetic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14416) · Entrez [54898](https://www.ncbi.nlm.nih.gov/gene/54898) · UniProt [Q9NXB9](https://www.uniprot.org/uniprotkb/Q9NXB9) · Ensembl [ENSG00000197977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197977)

## Data

Gene col 12504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12504); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12504]; `tensor/DDL_lfc|DDL_z.npy` [12504]; `embed/gene_vectors.npy` [12504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12504 or target_col == 12504). Every well: [[ELOVL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOVL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
