---
symbol: "ACHE"
type: "gene"
col: 1480
ensembl_id: "ENSG00000087085"
name: "acetylcholinesterase (Yt blood group)"
location: "7q22.1"
module: 61
arm: "+"
pooled_cpm: 3.36
n_lines_expressing: 33
n_dd_up: 41
n_dd_down: 0
n_dd_up_clean: 30
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ACHE

*acetylcholinesterase (Yt blood group)* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.9× (z +28.5, q 0e+00, up in 17 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0900×; ⚠ toxic; transcription drop); [[Hydroxyurea (drug)]] 5 µM in 1 line (NCI-H2030 0.0874×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XKR4]] (+0.68, fdr 7e-06), [[CDIP1]] (+0.66, fdr 7e-06), [[KRTAP5-AS1]] (+0.64, fdr 1e-05); moves opposite to [[MRPS27]] (-0.57, fdr 1e-05), [[IPO11]] (-0.55, fdr 1e-05), [[PMS1]] (-0.55, fdr 1e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RHOD]] → it (grade B ⚠); 3 go from it, the strongest it → [[NTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.9×** | +28.5 | 0e+00 | 17/19 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **10.4×** | +17.7 | 0e+00 | 20/22 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.90×** | +12.5 | 1e-33 | 15/20 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +9.8 | 3e-20 | 3/11 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +9.3 | 1e-18 | 1/4 (PANC-1) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +8.8 | 1e-16 | 2/5 (PANC-1, A498) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +8.6 | 4e-16 | 10/18 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.71×** | +7.8 | 3e-13 | 11/23 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.33×** | +6.6 | 2e-09 | 13/27 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +6.4 | 7e-09 | 8/26 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +6.3 | 2e-08 | 4/10 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +6.2 | 2e-08 | 12/25 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +6.1 | 4e-08 | 8/27 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.15×** | +6.0 | 7e-08 | 13/18 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +5.9 | 2e-07 | 6/16 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +5.8 | 3e-07 | 8/25 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +4.7 | 8e-05 | 10/27 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +4.3 | 4e-04 | 8/23 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.002 | 9/26 (LS 180, A498, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.01×** | +3.9 | 0.003 | 4/15 (A549, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0900×; ⚠ toxic; transcription drop); [[Hydroxyurea (drug)]] 5 µM in 1 line (NCI-H2030 0.0874×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +19.4) | — |
| [[NCI-H2347 (line)]] | alt | 8.05 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0900× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 1.32 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.4× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 2.53 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.4× (z +18.5) | — |
| [[A-172 (line)]] | wt | 8.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +14.2) | — |
| [[A549 (line)]] | wt | 4.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +14.9) | — |
| [[NCI-H2030 (line)]] | alt | 3.62 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +12.2) | [[Hydroxyurea (drug)]] 5 µM 0.0874× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 6.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.2× (z +8.8) | — |
| [[J82 (line)]] | alt | 0.868 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.7× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 4.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +10.2) | — |
| [[A-427 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.898 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XKR4]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[CDIP1]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[KRTAP5-AS1]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[TCEAL3]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SLC31A2]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[S100A3]] | +0.59 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[MUC12]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[STX11]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SMPD3]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[BBC3]] | +0.58 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SLC35F1]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SLC9C1]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS27]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[IPO11]] | -0.55 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PMS1]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[HAUS6]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TAS2R30]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[DROSHA]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[POLA1]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[HERC2P3]] | -0.49 | -0.39 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOD]] | B | RHOD activity raises ACHE's level | lines that do not express RHOD (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without RHOD | 0.032 | ⚠ within organs, on part of the lines; also absent: EPHA2, LINC00857, TFCP2L1 |
| [[SRRM3]] | B | SRRM3 activity raises ACHE's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.88× lower at baseline in the lines without SRRM3 | 0.049 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[KRTAP5-AS1]] | B | KRTAP5-AS1 activity raises ACHE's level | lines that do not express KRTAP5-AS1 (12) vs lines expressing it (38) | 1.73× lower at baseline in the lines without KRTAP5-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: LLGL2, TFR2, USP43; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ACHE's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KREMEN2]] | C | KREMEN2 activity raises ACHE's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without KREMEN2 | 0.009 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN1]] | B | ACHE activity raises NTN1's level | lines that do not express ACHE (17) vs lines expressing it (33) | 1.74× lower at baseline in the lines without ACHE | 0.037 | ⚠ within organs, on part of the lines; also absent: DKK1, KREMEN2; maybe low, not absent |
| [[ICAM5]] | B | ACHE activity strengthens ICAM5's drug response | lines that do not express ACHE (10) vs lines expressing it (24) | the lines without ACHE respond 0.36× as strongly (z diff +1.85); strongest at Niclosamide (olamine) 5 µM: 0.74x vs 2.00x (z diff +4.0) | 0.091 | ⚠ within organs, on part of the lines; also absent: DKK1, KREMEN2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[KREMEN2]] | C | ACHE activity raises KREMEN2's level | lines that do not express ACHE (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without ACHE | 0.083 | ⚠ within organs, on part of the lines; also absent: DKK1, KREMEN2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.8, 9.4); signed map (43.2, -3.4). **Vector** length 57.7, 13.2% of its response variance represented; |z| ≥ 3 in 633 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +28.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +17.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +7.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | acetylcholinesterase (Yt blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,889,994-100,896,974 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously YT |
| Gene groups (HGNC) | Blood group antigens; Cholinesterase family |
| Hallmark sets | HEDGEHOG_SIGNALING, ALLOGRAFT_REJECTION, MYOGENESIS |
| Reactome | 9 pathways, smallest: Neurotransmitter clearance; Synthesis, secretion, and deacylation of Ghrelin; Synthesis of PC |
| Matched by | ensembl_id |

**Function**, from UniProt [P22303](https://www.uniprot.org/uniprotkb/P22303) (Acetylcholinesterase):

> Hydrolyzes rapidly the acetylcholine neurotransmitter released into the synaptic cleft allowing to terminate the signal transduction at the neuromuscular junction. Role in neuronal apoptosis.

**Summary**, from NCBI Gene [43](https://www.ncbi.nlm.nih.gov/gene/43):

> Acetylcholinesterase hydrolyzes the neurotransmitter, acetylcholine at neuromuscular junctions and brain cholinergic synapses, and thus terminates signal transmission. It is also found on the red blood cell membranes, where it constitutes the Yt blood group antigen. Acetylcholinesterase exists in multiple molecular forms which possess similar catalytic properties, but differ in their oligomeric assembly and mode of cell attachment to the cell surface. It is encoded by the single ACHE gene, and …

**Accessions** — [HGNC:108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:108) · Entrez [43](https://www.ncbi.nlm.nih.gov/gene/43) · UniProt [P22303](https://www.uniprot.org/uniprotkb/P22303) · Ensembl [ENSG00000087085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087085)

## Data

Gene col 1480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1480); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1480]; `tensor/DDL_lfc|DDL_z.npy` [1480]; `embed/gene_vectors.npy` [1480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1480 or target_col == 1480). Every well: [[ACHE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACHE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
