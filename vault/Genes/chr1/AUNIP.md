---
symbol: "AUNIP"
type: "gene"
col: 4809
ensembl_id: "ENSG00000127423"
name: "aurora kinase A and ninein interacting protein"
location: "1p36.11"
module: 6
arm: "+"
pooled_cpm: 6.92
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# AUNIP

*aurora kinase A and ninein interacting protein* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (19 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 3.41× (z +12.1, q 4e-31, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +9.4, q 8e-19, up in 26 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.612× (z -4.8, q 7e-04, down in 16 of 43 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Omeprazole (drug)]] 0.05 µM: 0.697× (z -3.6, q 0.060, down in 8 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Terfenadine (drug)]] 0.5 µM in 1 line (SHP-77 0.127×); [[Selinexor (drug)]] 5 µM in 1 line (SW480 0.354×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCMBP]] (+0.72, fdr 7e-06), [[DSCC1]] (+0.71, fdr 7e-06), [[RAD51]] (+0.70, fdr 7e-06); moves opposite to [[SQSTM1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **3.41×** | +12.1 | 4e-31 | 45/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.26×** | +11.4 | 1e-27 | 36/43 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **3.12×** | +11.3 | 4e-27 | 40/47 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +9.4 | 8e-19 | 26/42 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.57×** | +9.4 | 1e-18 | 38/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **5.99×** | +9.3 | 2e-18 | 36/44 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.49×** | +9.0 | 1e-17 | 28/40 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.43×** | +8.8 | 1e-16 | 30/47 (SW480, KATO III, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **2.30×** | +7.9 | 2e-13 | 22/32 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **2.20×** | +7.5 | 4e-12 | 24/35 (LoVo, J82, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.98×** | +7.1 | 5e-11 | 22/38 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.04×** | +7.1 | 7e-11 | 25/41 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.89×** | +6.3 | 1e-08 | 25/45 (PANC-1, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.77×** | +5.7 | 6e-07 | 13/30 (NCI-H460, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +5.5 | 1e-06 | 21/45 (SW480, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +5.3 | 4e-06 | 18/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.002 | 11/45 (HCT15, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.012 | 10/42 (HT-29, NCI-H460, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.013 | 10/38 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4809.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Terfenadine (drug)]] 0.5 µM in 1 line (SHP-77 0.127×); [[Selinexor (drug)]] 5 µM in 1 line (SW480 0.354×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.612×** | -4.8 | 7e-04 | 16/43 (A-427, LoVo, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.670×** | -4.0 | 0.021 | 17/46 (SW480, SNU-1, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.697×** | -3.6 | 0.060 | 8/47 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.699×** | -3.5 | 0.060 | 11/43 (A498, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -3.5 | 0.061 | 11/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.95 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.196× (z -8.5) ⚠ cell-cycle shift, explains ~58% of this change |
| [[C32 (line)]] | wt | 4.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 5.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 3.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.127× (z -8.7) |
| [[SW480 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.354× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCMBP]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 | STRING 420 |
| [[RAD51]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 | STRING 436 |
| [[DGCR8]] | +0.70 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[RFC4]] | +0.70 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[DDIAS]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[CDC25A]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 | STRING 469 |
| [[CDCA5]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 | STRING 491 |
| [[RAD54L]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 | STRING 409 |
| [[TRAIP]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[MFSD14CP]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[E2F2]] | +0.66 | +0.60 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SQSTM1]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises AUNIP's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without CDC25A | 0.048 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TP73]] | B | TP73 activity raises AUNIP's level | lines that do not express TP73 (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without TP73 | 0.065 | ⚠ within organs, on part of the lines; also absent: SPTB, PRR36, EMID1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises AUNIP's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.75× lower at baseline in the lines without E2F2 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises AUNIP's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.96× lower at baseline in the lines without CDCA7 | 0.097 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises AUNIP's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without ZNF367 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.4, -46.4); signed map (-38.3, -41.7). **Vector** length 68.9, 12.4% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.50 to 28); *DNA Replication* (reactome, mean cos +0.51 to 40); *E2F G1/S* (control, mean cos +0.51 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.4 | +11.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +4.2 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +7.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | +2.5 | +5.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +5.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -3.5 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.3 | -2.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.2 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | +0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | aurora kinase A and ninein interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,831,913-25,859,458 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2603, AIBp; previously C1orf135 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7T9](https://www.uniprot.org/uniprotkb/Q9H7T9) (Aurora kinase A- and ninein-interacting protein):

> DNA-binding protein that accumulates at DNA double-strand breaks (DSBs) following DNA damage and promotes DNA resection and homologous recombination. Serves as a sensor of DNA damage: binds DNA with a strong preference for DNA substrates that mimic structures generated at stalled replication forks, and anchors RBBP8/CtIP to DSB sites to promote DNA end resection and ensuing homologous recombination repair. Inhibits non-homologous end joining (NHEJ). Required for the dynamic movement of AURKA at …

**Summary**, from NCBI Gene [79000](https://www.ncbi.nlm.nih.gov/gene/79000):

> Enables damaged DNA binding activity. Involved in double-strand break repair via homologous recombination; negative regulation of double-strand break repair via nonhomologous end joining; and spindle organization. Located in centrosome; site of DNA damage; and spindle pole. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28363) · Entrez [79000](https://www.ncbi.nlm.nih.gov/gene/79000) · UniProt [Q9H7T9](https://www.uniprot.org/uniprotkb/Q9H7T9) · Ensembl [ENSG00000127423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127423)

## Data

Gene col 4809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4809); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4809]; `tensor/DDL_lfc|DDL_z.npy` [4809]; `embed/gene_vectors.npy` [4809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4809 or target_col == 4809). Every well: [[AUNIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AUNIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
