---
symbol: "SELENOM"
type: "gene"
col: 12697
ensembl_id: "ENSG00000198832"
name: "selenoprotein M"
location: "22q12.2"
module: 24
arm: "+"
pooled_cpm: 14.64
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SELENOM

*selenoprotein M* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +6.4, q 7e-08, up in 23 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 3.19×; ⚠ cell-cycle shift, would explain all of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.122×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0961×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SELENOK]] (+0.69, fdr 7e-06), [[NKAP]] (+0.67, fdr 1e-05), [[ZMYM5]] (+0.67, fdr 7e-06); moves opposite to [[NUP155]] (-0.67, fdr 7e-06), [[EFTUD2]] (-0.65, fdr 1e-05), [[PRKDC]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPRC5C]] → it (grade B ⚠); 5 go from it, the strongest it → [[F2R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12697.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 3.19×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.4 | 7e-08 | 23/32 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.30×** | +4.9 | 3e-04 | 15/25 (NCI-H2030, PANC-1, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.91×** | +4.7 | 5e-04 | 22/28 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.1 | 0.005 | 14/31 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.71×** | +3.8 | 0.018 | 20/33 (PANC-1, SW 900, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | 1.57× | +3.2 | 0.15 | 8/16 (SNU-423, NCI-H2030, …) | all doses, flat | composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.52× | +3.0 | 0.20 | 15/33 (A498, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12697.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.122×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0961×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.588× | -3.5 | 0.15 | 16/33 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.621× | -3.5 | 0.15 | 15/34 (NCI-H1573, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.416× | -3.3 | 0.16 | 18/30 (NCI-H1573, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.638× | -3.0 | 0.29 | 12/34 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 9.29 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0961× (z -8.7) |
| [[A-172 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 | same gene group; STRING 878 |
| [[NKAP]] | +0.67 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[FBXL15]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[MED19]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[RNF181]] | +0.65 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[TMEM106A]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TMEM205]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[IFI27L2]] | +0.65 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[TCEAL3]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.64 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[FKBP2]] ⚠ | +0.64 | +0.50 / +0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RABAC1]] | +0.63 | +0.39 / +0.72 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | -0.67 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.65 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.63 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.63 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[TFDP1]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[TMX3]] | -0.60 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.59 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[MAT2A]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[VMA21]] | -0.59 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[NUDT3]] | -0.58 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[TCOF1]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5C]] | B | GPRC5C activity lowers SELENOM's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.62× higher at baseline in the lines without GPRC5C | 0.051 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2R]] | B | SELENOM activity raises F2R's level | lines that do not express SELENOM (14) vs lines expressing it (36) | 1.99× lower at baseline in the lines without SELENOM | 0.027 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S |
| [[SYNGR2]] | B | SELENOM activity lowers SYNGR2's level | lines that do not express SELENOM (14) vs lines expressing it (36) | 1.48× higher at baseline in the lines without SELENOM | 0.071 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S |
| [[COX17]] | B | SELENOM activity lowers COX17's level | lines that do not express SELENOM (14) vs lines expressing it (36) | 1.21× higher at baseline in the lines without SELENOM | 0.074 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S |
| [[LACTB]] | B | SELENOM activity raises LACTB's level | lines that do not express SELENOM (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without SELENOM | 0.077 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S |
| [[STARD10]] | B | SELENOM activity weakens STARD10's drug response | lines that do not express SELENOM (12) vs lines expressing it (32) | the lines without SELENOM respond 1.14× as strongly (z diff -0.29); rises at some drug-doses, falls at others (46% from rises): Panobinostat 0.5 µM: 0.57x vs 0.62x (z diff -1.6); Dinaciclib 0.5 µM: 1.28x vs 1.00x (z diff -1.5); Adagrasib 0.05 µM: 1.16x vs 1.11x (z diff -1.1) | 0.086 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.6, -30.5); signed map (-11.9, -0.3). **Vector** length 59.8, 15.7% of its response variance represented; |z| ≥ 3 in 392 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.4 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.3 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +1.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.1 | +3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,104,772-31,120,069 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SELM, SEPM |
| Gene groups (HGNC) | Selenoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWX9](https://www.uniprot.org/uniprotkb/Q8WWX9) (Selenoprotein M):

> May function as a thiol-disulfide oxidoreductase that participates in disulfide bond formation.

**Summary**, from NCBI Gene [140606](https://www.ncbi.nlm.nih.gov/gene/140606):

> The protein encoded by this gene belongs to the selenoprotein M/SEP15 family. The exact function of this protein is not known. It is localized in the perinuclear region, is highly expressed in the brain, and may be involved in neurodegenerative disorders. Transgenic mice with targeted deletion of this gene exhibit increased weight gain, suggesting a role for this gene in the regulation of body weight and energy metabolism. This protein is a selenoprotein, containing the rare amino acid …

**Accessions** — [HGNC:30397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30397) · Entrez [140606](https://www.ncbi.nlm.nih.gov/gene/140606) · UniProt [Q8WWX9](https://www.uniprot.org/uniprotkb/Q8WWX9) · Ensembl [ENSG00000198832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198832)

## Data

Gene col 12697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12697); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12697]; `tensor/DDL_lfc|DDL_z.npy` [12697]; `embed/gene_vectors.npy` [12697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12697 or target_col == 12697). Every well: [[SELENOM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
