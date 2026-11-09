---
symbol: "PLEKHF1"
type: "gene"
col: 9278
ensembl_id: "ENSG00000166289"
name: "pleckstrin homology and FYVE domain containing 1"
location: "19q12"
module: 3
arm: "+"
pooled_cpm: 2.13
n_lines_expressing: 45
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PLEKHF1

*pleckstrin homology and FYVE domain containing 1* — 19q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.65× (z +7.8, q 4e-12, up in 20 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.0394×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0618×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.0808×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALA]] (+0.58, fdr 3e-05), [[SIRT7]] (+0.58, fdr 7e-05), [[LARP6]] (+0.56, fdr 1e-05); moves opposite to [[ZNF577]] (-0.58, fdr 6e-05), [[ENSA]] (-0.51, fdr 4e-05), [[ABCE1]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF577]] → it (grade B ⚠); 3 go from it, the strongest it → [[FAM104A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.65×** | +7.8 | 4e-12 | 20/33 (NCI-H2030, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.62×** | +7.7 | 4e-12 | 22/40 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.52×** | +7.4 | 3e-11 | 20/35 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +7.1 | 2e-10 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +5.7 | 2e-06 | 1/5 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.6 | 2e-06 | 9/22 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +5.5 | 4e-06 | 7/12 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +5.2 | 1e-05 | 11/39 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +4.6 | 3e-04 | 9/26 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +4.2 | 0.002 | 5/16 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.8 | 0.008 | 2/10 (Hs 766T, HOP62) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +3.8 | 0.008 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +3.4 | 0.026 | 1/3 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.4 | 0.028 | 0/3 | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.037 | 6/38 (C32, H4, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.89×** | +3.3 | 0.040 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.046 | 4/34 (A498, A-172, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.068 | 2/22 (Panc 03.27, HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.50×** | +3.0 | 0.082 | 0/13 | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.086 | 5/37 (A498, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.100 | 3/37 (LOX-IMVI, SK-MEL-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9278.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.0394×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0618×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.0808×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.762× | -3.1 | 0.64 | 7/28 (SW 900, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0394× (z -17.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.916 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.958 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.745 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.585 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.561 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.827 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.803 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.867 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.632 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.959 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.123 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALA]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[SIRT7]] | +0.58 | +0.37 / +0.57 | both halves | 7e-05 |  |
| [[LARP6]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PLCD1]] | +0.55 | +0.32 / +0.50 | both halves | 2e-04 |  |
| [[DOK4]] | +0.54 | +0.27 / +0.57 | both halves | 3e-04 | same gene group |
| [[MPST]] | +0.54 | +0.31 / +0.48 | both halves | 2e-04 |  |
| [[RILP]] | +0.53 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[VPS37D]] | +0.53 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[WDFY1]] | +0.53 | +0.40 / +0.45 | both halves | 5e-05 | same gene group |
| [[CARD19]] | +0.53 | +0.29 / +0.52 | both halves | 3e-04 |  |
| [[TMEM185A]] | +0.52 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ARL8A]] | +0.52 | +0.29 / +0.62 | both halves | 2e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF577]] | -0.58 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[ENSA]] | -0.51 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[ABCE1]] | -0.51 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[ST7L]] | -0.51 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[TAF2]] | -0.50 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[NEK9]] | -0.50 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[MLH1]] | -0.49 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[LINC00641]] | -0.49 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.49 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[SRSF1]] | -0.48 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[SLC30A9]] | -0.48 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[DDX39B]] | -0.48 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[RBM12]] | -0.48 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF577]] | B | ZNF577 activity raises PLEKHF1's level | lines that do not express ZNF577 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without ZNF577 | 0.028 | ⚠ within organs, on part of the lines; also absent: ZNF649, ZNF724, ENSG00000283201 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM104A]] | B | PLEKHF1 activity raises FAM104A's level | lines that do not express PLEKHF1 (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without PLEKHF1 | 0.039 | ⚠ within organs, on part of the lines; also absent: E2F1, MCM10, DAGLA; maybe low, not absent |
| [[ZNF823]] | B | PLEKHF1 activity raises ZNF823's level | lines that do not express PLEKHF1 (5) vs lines expressing it (45) | 1.85× lower at baseline in the lines without PLEKHF1 | 0.063 | ⚠ within organs, on part of the lines; also absent: E2F1, MCM10, DAGLA; maybe low, not absent |
| [[FLYWCH1]] | B | PLEKHF1 activity weakens FLYWCH1's drug response | lines that do not express PLEKHF1 (5) vs lines expressing it (43) | the lines without PLEKHF1 respond 1.62× as strongly (z diff -1.76); rises at some drug-doses, falls at others (55% from rises): Ouabain (Octahydrate) 5 µM: 0.35x vs 0.64x (z diff -3.7); Ixazomib citrate 5 µM: 3.47x vs 2.15x (z diff -2.8); Ixazomib citrate 0.5 µM: 2.49x vs 1.87x (z diff -1.9) | 0.071 | ⚠ within organs, on part of the lines; also absent: E2F1, MCM10, DAGLA; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (25.4, -11.3); signed map (-24.0, 7.3). **Vector** length 35.1, 4.27% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.3 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.7 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.5 | +7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.0 | -3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and FYVE domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q12 — chr19:29,665,459-29,675,477 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APPD, MGC4090, PHAFIN1, ZFYVE15 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S99](https://www.uniprot.org/uniprotkb/Q96S99) (Pleckstrin homology domain-containing family F member 1):

> May play a role in endosome function.

**Summary**, from NCBI Gene [79156](https://www.ncbi.nlm.nih.gov/gene/79156):

> Enables phosphatidylinositol-3-phosphate binding activity; phosphatidylinositol-4-phosphate binding activity; and phosphatidylinositol-5-phosphate binding activity. Involved in endosome organization; positive regulation of autophagy; and protein localization to plasma membrane. Located in endosome and lysosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20764) · Entrez [79156](https://www.ncbi.nlm.nih.gov/gene/79156) · UniProt [Q96S99](https://www.uniprot.org/uniprotkb/Q96S99) · Ensembl [ENSG00000166289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166289)

## Data

Gene col 9278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9278); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9278]; `tensor/DDL_lfc|DDL_z.npy` [9278]; `embed/gene_vectors.npy` [9278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9278 or target_col == 9278). Every well: [[PLEKHF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
