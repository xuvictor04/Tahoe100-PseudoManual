---
symbol: "PLAAT1"
type: "gene"
col: 4796
ensembl_id: "ENSG00000127252"
name: "phospholipase A and acyltransferase 1"
location: "3q29"
module: 61
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 30
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# PLAAT1

*phospholipase A and acyltransferase 1* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.56× (z +15.9, q 0e+00, up in 23 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 0.220×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P2RY1]] (+0.57, fdr 1e-05), [[CRYBG3]] (+0.56, fdr 3e-05), [[ARFGEF3]] (+0.56, fdr 7e-05); moves opposite to [[KAT6B]] (-0.52, fdr 6e-05), [[ATF7]] (-0.50, fdr 2e-05), [[MED25]] (-0.48, fdr 6e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CREB5]] → it (grade B ⚠); 3 go from it, the strongest it → [[FABP5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.56×** | +15.9 | 0e+00 | 23/27 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.24×** | +9.6 | 2e-19 | 23/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.3 | 2e-18 | 3/10 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +9.1 | 1e-17 | 20/27 (A-172, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +9.1 | 2e-17 | 3/10 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.09×** | +8.8 | 2e-16 | 15/27 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.00×** | +8.3 | 1e-14 | 18/27 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +8.3 | 1e-14 | 12/22 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +7.1 | 6e-11 | 6/14 (SNU-423, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +7.0 | 2e-10 | 15/26 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +6.6 | 2e-09 | 12/27 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +6.5 | 4e-09 | 11/25 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +6.1 | 6e-08 | 11/19 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +6.0 | 6e-08 | 12/24 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.7 | 1e-04 | 12/27 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +4.6 | 1e-04 | 9/21 (H4, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.6 | 2e-04 | 10/27 (A-172, H4, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +4.3 | 5e-04 | 6/24 (A-172, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +4.3 | 5e-04 | 8/24 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.002 | 9/23 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4796.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 0.220×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 0.767× | -3.2 | 0.40 | 3/27 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.822× | -3.2 | 0.40 | 5/27 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RY1]] | +0.57 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CRYBG3]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ARFGEF3]] | +0.56 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[DTNA]] | +0.52 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[PTCHD1]] | +0.52 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[CACNB4]] | +0.51 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[HS6ST3]] | +0.51 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[POLR3G]] | +0.51 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[CHRM3]] | +0.50 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[NIPAL1]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[XACT]] | +0.50 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[AFF2]] | +0.50 | +0.46 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT6B]] | -0.52 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[ATF7]] | -0.50 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[MED25]] | -0.48 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[BCAS3]] | -0.48 | -0.18 / -0.51 | ⚠ one half (not replicated) | 1e-03 |  |
| [[DZANK1]] | -0.47 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[ATF6B]] | -0.46 | -0.32 / -0.57 | both halves | 1e-04 |  |
| [[WBP11]] | -0.46 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[CDKAL1]] | -0.45 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ALDH6A1]] | -0.45 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[TCTN2]] | -0.45 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[EFCAB11]] | -0.45 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[ZNF487]] | -0.45 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ZZEF1]] | -0.42 | -0.26 / -0.49 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB5]] | B | CREB5 activity raises PLAAT1's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without CREB5 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FABP5]] | B | PLAAT1 activity raises FABP5's level | lines that do not express PLAAT1 (20) vs lines expressing it (30) | 1.52× lower at baseline in the lines without PLAAT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SDK1, PDGFD, SNCA |
| [[GPR63]] | B | PLAAT1 activity raises GPR63's level | lines that do not express PLAAT1 (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without PLAAT1 | 0.036 | ⚠ within organs, on part of the lines; also absent: SDK1, PDGFD, SNCA |
| [[CREB5]] | B | PLAAT1 activity raises CREB5's level | lines that do not express PLAAT1 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without PLAAT1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SDK1, PDGFD, SNCA |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.3, 29.7); signed map (31.4, 22.0). **Vector** length 50.2, 9.76% of its response variance represented; |z| ≥ 3 in 633 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +15.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +3.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -2.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -0.1 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -0.8 | -1.2 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -0.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A and acyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:193,241,128-193,277,738 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H-REV107, HRASLS1, A-C1, PLA/AT1, PLAAT-1; previously HRASLS |
| Gene groups (HGNC) | Phospholipase A and acyltransferase family |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PE; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HDD0](https://www.uniprot.org/uniprotkb/Q9HDD0) (Phospholipase A and acyltransferase 1):

> Exhibits both phospholipase A1/2 and acyltransferase activities. Shows phospholipase A1 (PLA1) and A2 (PLA2) activity, catalyzing the calcium-independent release of fatty acids from the sn-1 or sn-2 position of glycerophospholipids. Shows O-acyltransferase activity, catalyzing the transfer of a fatty acyl group from glycerophospholipid to the hydroxyl group of lysophospholipid. Shows N-acyltransferase activity, catalyzing the calcium-independent transfer of a fatty acyl group at the sn-1 …

**Summary**, from NCBI Gene [57110](https://www.ncbi.nlm.nih.gov/gene/57110):

> Enables acyltransferase activity, transferring groups other than amino-acyl groups and glycerophospholipase activity. Involved in N-acylphosphatidylethanolamine metabolic process and phosphatidylcholine metabolic process. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14922) · Entrez [57110](https://www.ncbi.nlm.nih.gov/gene/57110) · UniProt [Q9HDD0](https://www.uniprot.org/uniprotkb/Q9HDD0) · Ensembl [ENSG00000127252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127252)

## Data

Gene col 4796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4796); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4796]; `tensor/DDL_lfc|DDL_z.npy` [4796]; `embed/gene_vectors.npy` [4796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4796 or target_col == 4796). Every well: [[PLAAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
