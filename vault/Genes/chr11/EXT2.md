---
symbol: "EXT2"
type: "gene"
col: 7510
ensembl_id: "ENSG00000151348"
name: "exostosin glycosyltransferase 2"
location: "11p11.2"
module: 36
arm: "+"
pooled_cpm: 56.79
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# EXT2

*exostosin glycosyltransferase 2* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.83× (z +10.8, q 1e-24, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.742× (z -5.4, q 4e-05, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.184×, HT-29 0.379×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.173×, SW1417 0.413×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.523×, J82 0.532×; ⚠ cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW48 0.155×); [[Pentagastrin (drug)]] 0.5 µM in 1 line (SW 1088 0.0696×); [[Tadalafil (drug)]] 0.05 µM in 1 line (SW 1271 0.0876×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPR1]] (+0.69, fdr 1e-05), [[MAPK9]] (+0.66, fdr 7e-06), [[HERC2]] (+0.64, fdr 1e-05); moves opposite to [[FAM117A]] (-0.62, fdr 8e-06), [[ZNF397]] (-0.61, fdr 1e-05), [[OFD1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HEG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +10.8 | 1e-24 | 45/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +9.4 | 1e-18 | 43/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +9.0 | 5e-17 | 43/49 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +8.8 | 1e-16 | 44/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +8.3 | 2e-14 | 45/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +8.0 | 1e-13 | 38/48 (HOP62, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +7.9 | 2e-13 | 38/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +7.5 | 6e-12 | 34/48 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +7.1 | 8e-11 | 39/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +6.1 | 7e-08 | 36/48 (SW480, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +5.8 | 5e-07 | 38/48 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +5.5 | 2e-06 | 31/48 (NCI-H1792, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 1e-05 | 30/48 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 3e-05 | 26/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.014 | 19/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7510.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.184×, HT-29 0.379×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.173×, SW1417 0.413×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.523×, J82 0.532×; ⚠ cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW48 0.155×); [[Pentagastrin (drug)]] 0.5 µM in 1 line (SW 1088 0.0696×); [[Tadalafil (drug)]] 0.05 µM in 1 line (SW 1271 0.0876×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -5.4 | 4e-05 | 34/48 (SW 1088, SHP-77, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.745× | -3.4 | 0.17 | 19/48 (HT-29, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -3.1 | 0.35 | 19/48 (SW1417, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 27.7 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.64× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 47.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.4) | — |
| [[A498 (line)]] | wt | 70.8 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.40× (z +11.0) | — |
| [[C32 (line)]] | wt | 86.5 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 47.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.55× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 84.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 65.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Roxadustat (drug)]] 0.05 µM 0.155× (z -12.4) |
| [[A-427 (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 23.8 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.90× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 47.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.140× (z -8.8) |
| [[HCT15 (line)]] | alt | 56.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.328× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.404× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 68.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 46.2 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.62× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 49.3 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.47× (z +10.0) | — |
| [[RKO (line)]] | wt | 96.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.34× (z +9.1) | — |
| [[SW 1088 (line)]] | alt | 66.6 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0696× (z -9.0) |
| [[SW 1271 (line)]] | alt | 72.2 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0876× (z -8.9) |
| [[SW480 (line)]] | alt | 75.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.37× (z +9.8) | — |
| [[A-172 (line)]] | wt | 82.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPR1]] | +0.69 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[HERC2]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TMTC3]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PTK2]] | +0.63 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[NUTF2]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[GOT2]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[SPATA5]] | +0.60 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[SELENON]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[HACD3]] | +0.60 | +0.70 / +0.38 | both halves | 7e-05 |  |
| [[MRTFB]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ACTR1A]] | +0.59 | +0.64 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.62 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[ZNF397]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[OFD1]] | -0.59 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[KRBOX5]] | -0.59 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[GOSR1]] | -0.59 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[BET1]] | -0.59 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[ZNF547]] | -0.58 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[TXNL4B]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[SAFB2]] | -0.57 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[ZNF585A]] | -0.57 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TMEM106A]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises EXT2's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.19× lower at baseline in the lines without HEG1 | 0.098 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-23.3, -27.7); signed map (-20.4, -48.0). **Vector** length 106, 28.3% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.8 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +7.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.7 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +5.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.8 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.0 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.7 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | exostosin glycosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:44,095,648-44,251,962 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SOTV |
| Gene groups (HGNC) | Exostosin glycosyltransferase family |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 9 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; HS-GAG biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93063](https://www.uniprot.org/uniprotkb/Q93063) (Exostosin-2):

> Glycosyltransferase forming with EXT1 the heterodimeric heparan sulfate polymerase which catalyzes the elongation of the heparan sulfate glycan backbone. Glycan backbone extension consists in the alternating transfer of (1->4)-beta-D-GlcA and (1->4)-alpha-D-GlcNAc residues from their respective UDP-sugar donors. Both EXT1 and EXT2 are required for the full activity of the polymerase since EXT1 bears the N-acetylglucosaminyl-proteoglycan 4-beta-glucuronosyltransferase activity within the complex …

**Summary**, from NCBI Gene [2132](https://www.ncbi.nlm.nih.gov/gene/2132):

> This gene encodes one of two glycosyltransferases involved in the chain elongation step of heparan sulfate biosynthesis. Mutations in this gene cause the type II form of multiple exostoses. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3513) · Entrez [2132](https://www.ncbi.nlm.nih.gov/gene/2132) · UniProt [Q93063](https://www.uniprot.org/uniprotkb/Q93063) · Ensembl [ENSG00000151348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151348)

## Data

Gene col 7510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7510); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7510]; `tensor/DDL_lfc|DDL_z.npy` [7510]; `embed/gene_vectors.npy` [7510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7510 or target_col == 7510). Every well: [[EXT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
