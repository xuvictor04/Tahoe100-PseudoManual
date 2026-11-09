---
symbol: "ZNF385B"
type: "gene"
col: 6865
ensembl_id: "ENSG00000144331"
name: "zinc finger protein 385B"
location: "2q31.2-q31.3"
module: 115
arm: "+"
pooled_cpm: 6.66
n_lines_expressing: 31
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 32
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# ZNF385B

*zinc finger protein 385B* — 2q31.2-q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.83× (z +18.8, q 0e+00, up in 13 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 0.195×, A498 0.0889×, LoVo 0.259×); [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.0989×, Panc 03.27 0.101×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (LoVo 0.100×, A-427 0.0473×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.235×, HEC-1-A 0.242×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRSS12]] (+0.62, fdr 1e-05), [[CARMIL1]] (+0.56, fdr 3e-05), [[GPM6A]] (+0.54, fdr 1e-05); moves opposite to [[DZANK1]] (-0.48, fdr 4e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[RHEX]] → it (grade B ⚠); 2 go from it, the strongest it → [[PLXNC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.83×** | +18.8 | 0e+00 | 13/20 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.20×** | +16.3 | 0e+00 | 22/25 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.41×** | +12.1 | 2e-31 | 20/24 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +11.4 | 4e-28 | 2/7 (HOP62, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.99×** | +10.8 | 3e-25 | 4/9 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.01×** | +10.1 | 8e-22 | 2/8 (HOP62, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +9.1 | 1e-17 | 9/20 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.40×** | +8.6 | 4e-16 | 9/24 (A-172, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.29×** | +8.2 | 1e-14 | 8/24 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.29×** | +8.2 | 1e-14 | 19/25 (CFPAC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +7.8 | 3e-13 | 10/25 (J82, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +7.8 | 3e-13 | 16/25 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +6.6 | 2e-09 | 14/25 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +6.1 | 4e-08 | 12/25 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.82×** | +5.7 | 5e-07 | 8/21 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.80×** | +5.6 | 8e-07 | 10/23 (SW480, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.1 | 1e-05 | 2/25 (HOP62, A-172) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.0 | 2e-05 | 3/19 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6865.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 0.195×, A498 0.0889×, LoVo 0.259×); [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.0989×, Panc 03.27 0.101×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (LoVo 0.100×, A-427 0.0473×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.235×, HEC-1-A 0.242×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tadalafil (drug)]] 5 µM |  | 0.676× | -3.7 | 0.12 | 2/25 (A-172, RPMI-7951) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.704× | -3.5 | 0.15 | 7/24 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 54.0 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0989× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.100× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 37.4 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -16.8) |
| [[A-427 (line)]] | wt | 5.79 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0473× (z -11.2) |
| [[A498 (line)]] | wt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0889× (z -14.5) |
| [[C32 (line)]] | wt | 1.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.4× (z +9.7) | — |
| [[J82 (line)]] | alt | 14.6 | 1 | 0 | [[Selinexor (drug)]] 5 µM 4.05× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.2× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -10.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 1.80 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.29× (z +8.8) | — |
| [[A-172 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.958 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRSS12]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[CARMIL1]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[GPM6A]] | +0.54 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CAPN14]] | +0.54 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[PLXNC1]] | +0.54 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[STK33]] | +0.53 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PLCE1]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TMEM98]] | +0.51 | +0.24 / +0.62 | both halves | 4e-04 |  |
| [[CCDC85A]] | +0.51 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PRKCQ]] | +0.51 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[TBC1D1]] | +0.50 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[ANKS1B]] | +0.50 | +0.47 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZANK1]] | -0.48 | -0.25 / -0.45 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHEX]] | B | RHEX activity raises ZNF385B's level | lines that do not express RHEX (43) vs lines expressing it (7) | 3.44× lower at baseline in the lines without RHEX | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[STK33]] | B | STK33 activity raises ZNF385B's level | lines that do not express STK33 (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without STK33 | 0.048 | ⚠ within organs, on part of the lines; also absent: SDK1, PGBD5, NID1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ZNF385B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CELF2]] | B | CELF2 activity raises ZNF385B's level | lines that do not express CELF2 (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without CELF2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENPP5, LMO3, GNAT3 |
| [[ENTREP1]] | B | ENTREP1 activity raises ZNF385B's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without ENTREP1 | 0.074 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[WDR17]] | C | WDR17 activity raises ZNF385B's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without WDR17 | 0.091 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNC1]] | B | ZNF385B activity raises PLXNC1's level | lines that do not express ZNF385B (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without ZNF385B | 0.040 | ⚠ within organs, on part of the lines; also absent: DTNA, CFI, CYGB; maybe low, not absent |
| [[GCNT1]] | B | ZNF385B activity raises GCNT1's level | lines that do not express ZNF385B (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without ZNF385B | 0.083 | ⚠ within organs, on part of the lines; also absent: DTNA, CFI, CYGB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.0, 41.1); signed map (53.6, 15.2). **Vector** length 55.4, 11.8% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +16.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +5.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -3.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | +0.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 385B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2-q31.3 — chr2:179,441,982-179,861,612 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25270; previously ZNF533 |
| Gene groups (HGNC) | Zinc fingers matrin-type; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q569K4](https://www.uniprot.org/uniprotkb/Q569K4) (Zinc finger protein 385B):

> May play a role in p53/TP53-mediated apoptosis.

**Summary**, from NCBI Gene [151126](https://www.ncbi.nlm.nih.gov/gene/151126):

> Enables p53 binding activity. Involved in intrinsic apoptotic signaling pathway by p53 class mediator. Located in fibrillar center. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26332) · Entrez [151126](https://www.ncbi.nlm.nih.gov/gene/151126) · UniProt [Q569K4](https://www.uniprot.org/uniprotkb/Q569K4) · Ensembl [ENSG00000144331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144331)

## Data

Gene col 6865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6865); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6865]; `tensor/DDL_lfc|DDL_z.npy` [6865]; `embed/gene_vectors.npy` [6865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6865 or target_col == 6865). Every well: [[ZNF385B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF385B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
