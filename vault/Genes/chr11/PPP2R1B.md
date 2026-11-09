---
symbol: "PPP2R1B"
type: "gene"
col: 6053
ensembl_id: "ENSG00000137713"
name: "protein phosphatase 2 scaffold subunit Abeta"
location: "11q23.1"
module: 29
arm: "+"
pooled_cpm: 35.77
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PPP2R1B

*protein phosphatase 2 scaffold subunit Abeta* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.17× (z +10.7, q 4e-24, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.264×; ⚠ transcription drop; cell-cycle shift, explains ~52% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.263×; ⚠ cell-cycle shift, explains ~50% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPT1]] (+0.72, fdr 7e-06), [[CIPC]] (+0.72, fdr 7e-06), [[DHFR]] (+0.71, fdr 7e-06); moves opposite to [[ATF4]] (-0.66, fdr 7e-06), [[CCDC174]] (-0.63, fdr 7e-06), [[MED19]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PTGFRN]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ULK-101 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +10.7 | 4e-24 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +7.0 | 5e-10 | 35/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +7.0 | 5e-10 | 40/47 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +6.0 | 3e-07 | 33/48 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.9 | 4e-07 | 30/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +5.1 | 3e-05 | 30/49 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 3e-05 | 29/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +5.0 | 4e-05 | 33/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +4.4 | 8e-04 | 27/48 (A498, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 8e-04 | 28/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +4.2 | 0.001 | 25/48 (SNU-423, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.007 | 24/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.024 | 22/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.027 | 22/48 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.18× | +3.2 | 0.050 | 12/48 (CFPAC-1, CHP-212, …) | rises with dose | low cells (technical?) |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.068 | 14/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.264×; ⚠ transcription drop; cell-cycle shift, explains ~52% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.263×; ⚠ cell-cycle shift, explains ~50% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 47.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.16× (z +14.4) | — |
| [[A498 (line)]] | wt | 28.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.48× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 84.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -8.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 50.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 22.1 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 34.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 33.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.264× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SHP-77 (line)]] | alt | 99.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 58.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +8.9) | — |
| [[SW480 (line)]] | alt | 46.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +11.4) | — |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[CIPC]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[DHFR]] | +0.71 | +0.63 / +0.75 | both halves | 7e-06 | pathway: G1/S Transition |
| [[PFKM]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 | pathway: Glucose metabolism |
| [[TMX1]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[VMA21]] | +0.66 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[RPE]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[PRDX3]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.64 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[PGRMC1]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[PGAM1]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 | pathway: Glucose metabolism |
| [[NONO]] | +0.62 | +0.56 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF4]] | -0.66 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.63 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[MED19]] | -0.62 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[TINCR]] | -0.61 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[RAB5A]] | -0.61 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[NPIPP1]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[MTHFR]] | -0.59 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[OSBP]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[GGNBP2]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MIDN]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[NKAP]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGFRN]] | B | PTGFRN activity lowers PPP2R1B's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.23× higher at baseline in the lines without PTGFRN | 0.095 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ULK-101 (drug)]] 5 µM | C | PPP2R1B's natural level lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | PPP2R1B's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.033 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.7, -22.8); signed map (-20.4, -38.3). **Vector** length 80.6, 17.5% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.5 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.3 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.9 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.2 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +4.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +1.9 |
|  | [[Adenine (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | +1.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | +3.8 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 scaffold subunit Abeta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:111,726,908-111,766,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PR65B, PP2A-Abeta |
| Gene groups (HGNC) | Protein phosphatase 2 scaffold subunits; STRIPAK complex; Armadillo like helical domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 113 pathways, smallest: PP2A-mediated dephosphorylation of key metabolic factors; MASTL Facilitates Mitotic Progression; Regulation of glycolysis by fructose 2,6-bisphosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P30154](https://www.uniprot.org/uniprotkb/P30154) (Serine/threonine-protein phosphatase 2A 65 kDa regulatory subunit A beta isoform):

> The PR65 subunit of protein phosphatase 2A serves as a scaffolding molecule to coordinate the assembly of the catalytic subunit and a variable regulatory B subunit.

**Summary**, from NCBI Gene [5519](https://www.ncbi.nlm.nih.gov/gene/5519):

> This gene encodes a constant regulatory subunit of protein phosphatase 2. Protein phosphatase 2 is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The constant regulatory subunit A serves as a scaffolding molecule to coordinate the assembly of the …

**Accessions** — [HGNC:9303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9303) · Entrez [5519](https://www.ncbi.nlm.nih.gov/gene/5519) · UniProt [P30154](https://www.uniprot.org/uniprotkb/P30154) · Ensembl [ENSG00000137713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137713)

## Data

Gene col 6053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6053); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6053]; `tensor/DDL_lfc|DDL_z.npy` [6053]; `embed/gene_vectors.npy` [6053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6053 or target_col == 6053). Every well: [[PPP2R1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
