---
symbol: "AKR1E2"
type: "gene"
col: 9146
ensembl_id: "ENSG00000165568"
name: "aldo-keto reductase family 1 member E2"
location: "10p15.1"
module: 78
arm: "+"
pooled_cpm: 5.12
n_lines_expressing: 31
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# AKR1E2

*aldo-keto reductase family 1 member E2* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.02× (z +7.7, q 6e-12, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.49× (z +6.5, q 2e-08, up in 12 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.578× (z -6.3, q 2e-07, down in 16 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.111×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0948×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.156×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.168×); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.182×); [[Omeprazole (drug)]] 0.5 µM in 1 line (LoVo 0.161×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42EP2]] (+0.52, fdr 4e-05), [[SLC4A3]] (+0.51, fdr 3e-05), [[NES]] (+0.50, fdr 4e-05); moves opposite to [[CCDC115]] (-0.50, fdr 1e-04), [[WDR83OS]] (-0.49, fdr 1e-04, ⚠ WDR83OS in the vector space only through flagged drug-doses), [[ARF5]] (-0.49, fdr 3e-05), [[SOS1]] (-0.48, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[CNTNAP3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +7.7 | 6e-12 | 3/10 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.2 | 2e-10 | 8/19 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +6.5 | 2e-08 | 12/27 (SW480, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +6.2 | 1e-07 | 7/13 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +5.8 | 9e-07 | 16/29 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.003 | 7/25 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.010 | 5/27 (HOP62, HS-578T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.015 | 5/28 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.37×** | +3.6 | 0.021 | 10/28 (SW480, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +3.6 | 0.021 | 6/28 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.4 | 0.040 | 2/24 (CFPAC-1, PANC-1) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.068 | 4/25 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.1 | 0.076 | 3/22 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9146.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.111×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0948×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.156×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.168×); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.182×); [[Omeprazole (drug)]] 0.5 µM in 1 line (LoVo 0.161×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.578×** | -6.3 | 2e-07 | 16/28 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.635×** | -5.2 | 5e-05 | 10/24 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.537×** | -3.7 | 0.037 | 9/24 (SHP-77, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.749× | -3.1 | 0.25 | 7/23 (SNU-423, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.770× | -3.0 | 0.30 | 8/28 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 49.0 | 0 | 5 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -9.7) |
| [[LoVo (line)]] | wt | 6.47 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0948× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Omeprazole (drug)]] 0.5 µM 0.161× (z -9.2) |
| [[A-172 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42EP2]] | +0.52 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[SLC4A3]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[NES]] | +0.50 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[ARAP3]] | +0.50 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[LINC01204]] | +0.50 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[LINC03004]] | +0.50 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[MELTF]] | +0.50 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[BCAN-AS2]] | +0.49 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[ULBP3]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[MCF2L2]] | +0.48 | +0.30 / +0.47 | both halves | 2e-04 |  |
| [[FABP5]] | +0.48 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[RANGAP1]] | +0.48 | +0.51 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC115]] | -0.50 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[WDR83OS]] ⚠ | -0.49 | -0.34 / -0.49 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ARF5]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SOS1]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ISCU]] | -0.47 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[CDK19]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[PRPF18]] | -0.46 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[FBXL20]] | -0.46 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[SELENOM]] | -0.46 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[HECTD4]] | -0.45 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[NKAP]] | -0.45 | -0.32 / -0.38 | both halves | 1e-04 |  |
| [[NCOA1]] | -0.45 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[CDK13]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTNAP3B]] | B | AKR1E2 activity raises CNTNAP3B's level | lines that do not express AKR1E2 (19) vs lines expressing it (31) | 1.94× lower at baseline in the lines without AKR1E2 | 0.053 | ⚠ within organs, on part of the lines; also absent: FLNC, AFAP1L1, CACNA2D1 |
| cells under [[Docetaxel (Trihydrate) (drug)]] 0.5 µM | B | AKR1E2 activity raises the cells' numbers under Docetaxel (Trihydrate) 0.5 µM (protects the cells) | lines that do not express AKR1E2 (19) vs lines expressing it (29) | the lines without AKR1E2: 0.87× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: FLNC, AFAP1L1, CACNA2D1 |
| cells under [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM | B | AKR1E2 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express AKR1E2 (19) vs lines expressing it (29) | the lines without AKR1E2: 1.13× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: FLNC, AFAP1L1, CACNA2D1 |
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | B | AKR1E2 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express AKR1E2 (19) vs lines expressing it (29) | the lines without AKR1E2: 1.20× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: FLNC, AFAP1L1, CACNA2D1 |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (57.0, 6.5); signed map (13.8, 46.6). **Vector** length 31.0, 3.89% of its response variance represented; |z| ≥ 3 in 496 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +3.7 |
|  | [[vincristine (drug)]] 5 µM |  | +0.8 | +1.9 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -0.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.7 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.7 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.7 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | aldo-keto reductase family 1 member E2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:4,786,629-4,848,062 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10612, HTSP1, htAKR; previously AKRDC1, AKR1CL2 |
| Gene groups (HGNC) | Aldo-keto reductases |
| Reactome | 3 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JD6](https://www.uniprot.org/uniprotkb/Q96JD6) (1,5-anhydro-D-fructose reductase):

> Catalyzes the NADPH-dependent reduction of 1,5-anhydro-D-fructose (AF) to 1,5-anhydro-D-glucitol (By similarity). Has low NADPH-dependent reductase activity towards 9,10-phenanthrenequinone (in vitro).

**Summary**, from NCBI Gene [83592](https://www.ncbi.nlm.nih.gov/gene/83592):

> The protein encoded by this gene is a member of the aldo-keto reductase superfamily. Members in this family are characterized by their structure (evolutionarily highly conserved TIM barrel) and function (NAD(P)H-dependent oxido-reduction of carbonyl groups). Transcripts of this gene have been reported in specimens of human testis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:23437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23437) · Entrez [83592](https://www.ncbi.nlm.nih.gov/gene/83592) · UniProt [Q96JD6](https://www.uniprot.org/uniprotkb/Q96JD6) · Ensembl [ENSG00000165568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165568)

## Data

Gene col 9146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9146); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9146]; `tensor/DDL_lfc|DDL_z.npy` [9146]; `embed/gene_vectors.npy` [9146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9146 or target_col == 9146). Every well: [[AKR1E2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKR1E2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
