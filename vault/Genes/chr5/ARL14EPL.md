---
symbol: "ARL14EPL"
type: "gene"
col: 15594
ensembl_id: "ENSG00000268223"
name: "ARF like GTPase 14 effector protein like"
location: "5q23.1"
module: 181
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 39
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# ARL14EPL

*ARF like GTPase 14 effector protein like* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.71× (z +17.6, q 0e+00, up in 20 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.0914×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL12RB2]] (+0.65, fdr 1e-05), [[PKD1L1]] (+0.63, fdr 7e-06), [[PIWIL2]] (+0.61, fdr 1e-05); moves opposite to [[PXMP4]] (-0.56, fdr 4e-05), [[SKP2]] (-0.56, fdr 4e-05), [[NUDT21]] (-0.55, fdr 3e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[LINC01033]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.71×** | +17.6 | 0e+00 | 20/27 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.33×** | +13.4 | 9e-39 | 13/21 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.76×** | +12.5 | 9e-34 | 22/28 (HEC-1-A, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.67×** | +11.1 | 1e-26 | 22/32 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +10.3 | 9e-23 | 16/24 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +9.2 | 3e-18 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.14×** | +8.8 | 9e-17 | 21/30 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.82×** | +8.3 | 7e-15 | 20/28 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +7.3 | 2e-11 | 3/5 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +6.5 | 4e-09 | 6/12 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.10×** | +5.9 | 2e-07 | 3/4 (HEC-1-A, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +5.2 | 8e-06 | 14/33 (A549, J82, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +4.8 | 6e-05 | 14/34 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.8 | 6e-05 | 2/9 (AsPC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +4.3 | 7e-04 | 15/33 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +4.2 | 0.001 | 12/29 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.65×** | +4.0 | 0.002 | 9/28 (NCI-H1792, J82, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.005 | 5/19 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.005 | 13/35 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.60×** | +3.7 | 0.005 | 5/31 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.0914×; ⚠ toxic; transcription drop).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 5.65 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 38.8× (z +19.3) | [[Digitoxin (drug)]] 5 µM 0.0914× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 5.15 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.4× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.65× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 3.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.23× (z +8.6) | — |
| [[A-172 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.946 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.648 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.951 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.780 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.849 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.762 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL12RB2]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[PKD1L1]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[C11orf96]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[NPHS1]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[NANOS3]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[RNF103-CHMP3]] | +0.59 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[LINC01033]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SSUH2]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[HSD11B1-AS1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SNX31]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXMP4]] | -0.56 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[SKP2]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[NUDT21]] | -0.55 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[SNX4]] | -0.53 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[FAR1]] | -0.53 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ATP5F1A]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TTLL5]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[HTT]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[RPA1]] | -0.52 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[KDM1A]] | -0.52 | -0.63 / -0.38 | both halves | 7e-05 |  |
| [[TERF1]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[SLC35A3]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARL14EPL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01033]] | B | ARL14EPL activity raises LINC01033's level | lines that do not express ARL14EPL (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without ARL14EPL | 0.041 | ⚠ within organs, on part of the lines; also absent: MAMLD1, ENSG00000243797, ENSG00000253496; maybe low, not absent |
| [[KCNIP4]] | B | ARL14EPL activity raises KCNIP4's level | lines that do not express ARL14EPL (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without ARL14EPL | 0.056 | ⚠ within organs, on part of the lines; also absent: MAMLD1, ENSG00000243797, ENSG00000253496; maybe low, not absent |
| [[C11orf96]] | B | ARL14EPL activity raises C11orf96's level | lines that do not express ARL14EPL (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without ARL14EPL | 0.077 | ⚠ within organs, on part of the lines; also absent: MAMLD1, ENSG00000243797, ENSG00000253496; maybe low, not absent |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | B | ARL14EPL activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express ARL14EPL (11) vs lines expressing it (37) | the lines without ARL14EPL: 0.85× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: MAMLD1, ENSG00000243797, ENSG00000253496; maybe low, not absent |

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.8, -8.5); signed map (22.4, 8.1). **Vector** length 53.1, 8.68% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +13.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +3.7 |
| fall | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.7 | +3.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.4 | +4.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 14 effector protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:116,032,324-116,060,118 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [P0DKL9](https://www.uniprot.org/uniprotkb/P0DKL9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44201) · Entrez [644100](https://www.ncbi.nlm.nih.gov/gene/644100) · UniProt [P0DKL9](https://www.uniprot.org/uniprotkb/P0DKL9) · Ensembl [ENSG00000268223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268223)

## Data

Gene col 15594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15594); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15594]; `tensor/DDL_lfc|DDL_z.npy` [15594]; `embed/gene_vectors.npy` [15594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15594 or target_col == 15594). Every well: [[ARL14EPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL14EPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
