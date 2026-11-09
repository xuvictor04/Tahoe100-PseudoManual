---
symbol: "C1QL1"
type: "gene"
col: 5169
ensembl_id: "ENSG00000131094"
name: "complement C1q like 1"
location: "17q21.31"
module: 215
arm: "+"
pooled_cpm: 3.97
n_lines_expressing: 28
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 9
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# C1QL1

*complement C1q like 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.06× (z +10.3, q 3e-22, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 4.42× (z +9.8, q 2e-20, up in 20 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.466× (z -5.1, q 2e-04, down in 13 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METRN]] (+0.63, fdr 1e-05), [[SLC17A7]] (+0.61, fdr 3e-05), [[B3GAT3]] (+0.60, fdr 1e-05); moves opposite to [[ZXDA]] (-0.65, fdr 1e-05), [[ZXDB]] (-0.65, fdr 1e-05), [[FBXO30]] (-0.65, fdr 2e-05).
> It is in [[Module 215]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 9 go from it, the strongest it → [[AFG1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.06×** | +10.3 | 3e-22 | 4/5 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.42×** | +9.8 | 2e-20 | 20/24 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.09×** | +9.3 | 2e-18 | 20/22 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.53×** | +8.3 | 1e-14 | 14/24 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.41×** | +8.1 | 6e-14 | 7/9 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +5.7 | 1e-06 | 8/23 (HOP62, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.48×** | +5.6 | 2e-06 | 1/4 (A498) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +5.0 | 4e-05 | 8/24 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.0 | 4e-05 | 7/17 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.8 | 8e-05 | 6/11 (A498, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +3.9 | 0.004 | 4/11 (A-172, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +3.7 | 0.009 | 5/19 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.74×** | +3.7 | 0.011 | 5/15 (SK-MEL-2, A498, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.69×** | +3.5 | 0.021 | 6/12 (NCI-H460, A498, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.16×** | +3.2 | 0.053 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.466×** | -5.1 | 2e-04 | 13/22 (NCI-H2030, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -4.9 | 3e-04 | 12/15 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.499×** | -4.4 | 0.002 | 16/20 (HOP62, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.564×** | -3.5 | 0.056 | 5/23 (NCI-H2030, A-172, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.575×** | -3.5 | 0.056 | 12/19 (A498, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.701×** | -3.4 | 0.075 | 13/17 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 45.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -9.9) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0785× (z -11.6) |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -13.4) |
| [[J82 (line)]] | alt | 5.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -8.8) |
| [[SNU-423 (line)]] | alt | 3.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -9.5) |
| [[A-427 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.508 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METRN]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SLC17A7]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[B3GAT3]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ANAPC11]] | +0.60 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[A1BG]] | +0.60 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ATG4B]] | +0.59 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[CARHSP1]] | +0.59 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[RPA3]] | +0.59 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[PCSK1N]] | +0.58 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[CABLES2]] | +0.58 | +0.47 / +0.38 | both halves | 7e-05 |  |
| [[COX6A1]] | +0.58 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[NUDT1]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | -0.65 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.65 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[FBXO30]] | -0.65 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[RNF6]] | -0.62 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[GTF3C4]] | -0.61 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[ZNF507]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[C17orf80]] | -0.60 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[HSPB8]] | -0.60 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[MRPL45]] | -0.60 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[TYW3]] | -0.60 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[DNAJC11]] | -0.59 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[HDDC2]] | -0.58 | -0.49 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFG1L]] | B | C1QL1 activity raises AFG1L's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without C1QL1 | 0.033 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[KDM4A-AS1]] | B | C1QL1 activity raises KDM4A-AS1's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.34× lower at baseline in the lines without C1QL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[ARSA]] | B | C1QL1 activity raises ARSA's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without C1QL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[LARS1]] | B | C1QL1 activity raises LARS1's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.26× lower at baseline in the lines without C1QL1 | 0.084 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[SLC17A7]] | B | C1QL1 activity raises SLC17A7's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without C1QL1 | 0.087 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[MATR3-1]] | B | C1QL1 activity raises MATR3-1's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.15× lower at baseline in the lines without C1QL1 | 0.088 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[ARL3]] | B | C1QL1 activity raises ARL3's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.32× lower at baseline in the lines without C1QL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[ZXDA]] | B | C1QL1 activity raises ZXDA's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.35× lower at baseline in the lines without C1QL1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[ZNF507]] | B | C1QL1 activity raises ZNF507's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.28× lower at baseline in the lines without C1QL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction -0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.3, 9.9); signed map (-31.7, 13.5). **Vector** length 39.0, 7.49% of its response variance represented; |z| ≥ 3 in 511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.0 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +10.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +0.8 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.8 | +3.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +0.8 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.7 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | complement C1q like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,959,693-44,968,303 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRF, C1QRF, C1QTNF14, CTRP14 |
| Gene groups (HGNC) | C1q and TNF related |
| Matched by | ensembl_id |

**Function**, from UniProt [O75973](https://www.uniprot.org/uniprotkb/O75973) (C1q-related factor):

> May regulate the number of excitatory synapses that are formed on hippocampus neurons. Has no effect on inhibitory synapses (By similarity).

**Summary**, from NCBI Gene [10882](https://www.ncbi.nlm.nih.gov/gene/10882):

> Predicted to enable signaling receptor binding activity. Predicted to be involved in maintenance of synapse structure and trans-synaptic signaling, modulating synaptic transmission. Predicted to act upstream of or within motor learning and neuron remodeling. Predicted to be located in several cellular components, including climbing fiber; extracellular region; and presynapse. Predicted to be active in obsolete extracellular space; synapse; and synaptic cleft. [provided by Alliance of Genome …

**Accessions** — [HGNC:24182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24182) · Entrez [10882](https://www.ncbi.nlm.nih.gov/gene/10882) · UniProt [O75973](https://www.uniprot.org/uniprotkb/O75973) · Ensembl [ENSG00000131094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131094)

## Data

Gene col 5169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5169); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5169]; `tensor/DDL_lfc|DDL_z.npy` [5169]; `embed/gene_vectors.npy` [5169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5169 or target_col == 5169). Every well: [[C1QL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1QL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
