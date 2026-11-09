---
symbol: "C9orf78"
type: "gene"
col: 5909
ensembl_id: "ENSG00000136819"
name: "chromosome 9 open reading frame 78"
location: "9q34.11"
module: 76
arm: "+"
pooled_cpm: 52.22
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# C9orf78

*chromosome 9 open reading frame 78* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.92× (z +11.2, q 1e-26, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.345×; ⚠ cell-cycle shift, explains ~98% of this change).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNHIT3]] (+0.67, fdr 7e-06), [[SPSB3]] (+0.62, fdr 3e-04), [[LCMT1]] (+0.60, fdr 3e-04); moves opposite to [[ADAMTS3]] (-0.53, fdr 9e-04, ⚠ one half only (not replicated)), [[HNRNPL]] (-0.53, fdr 0.001, ⚠ one half only (not replicated)), [[ATF7IP]] (-0.52, fdr 8e-04, ⚠ not reproduced), [[CTSC]] (-0.50, fdr 4e-05), [[TUBA1B]] (-0.47, fdr 2e-05), [[HEXB]] (-0.47, fdr 1e-04).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.92×** | +11.2 | 1e-26 | 48/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.81×** | +10.8 | 7e-25 | 47/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.50×** | +9.6 | 2e-19 | 48/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +8.9 | 6e-17 | 47/47 (MIA PaCa-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.56×** | +8.4 | 5e-15 | 45/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.15×** | +7.7 | 9e-13 | 36/40 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.7 | 9e-13 | 45/48 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.91×** | +6.3 | 3e-08 | 36/45 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.61×** | +4.8 | 1e-04 | 39/47 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.57×** | +4.5 | 3e-04 | 36/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.50×** | +4.2 | 0.001 | 34/47 (Panc 03.27, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 0.001 | 38/48 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.29×** | +3.7 | 0.008 | 25/48 (COLO 205, C32, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.010 | 32/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.031 | 29/48 (SW 900, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5909.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.345×; ⚠ cell-cycle shift, explains ~98% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.794× | -3.4 | 0.34 | 30/48 (HT-29, CFPAC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 45.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.89× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 53.4 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.70× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 29.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.65× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.95× (z +8.6) | — |
| [[SW480 (line)]] | alt | 65.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +10.5) | — |
| [[A549 (line)]] | wt | 43.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 43.2 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 35.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 43.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 46.1 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +8.6) | — |
| [[A-427 (line)]] | wt | 43.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.6) ⚠ cell-cycle shift, explains ~98% of this change |
| [[BT-474 (line)]] | alt | 56.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 54.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.39× (z +8.9) | — |
| [[KATO III (line)]] | alt | 60.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +8.6) | — |
| [[LoVo (line)]] | wt | 36.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 43.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.89× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SNU-1 (line)]] | wt | 41.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.90× (z +8.7) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 141 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 21 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT3]] | +0.67 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.62 | +0.26 / +0.62 | both halves | 3e-04 |  |
| [[LCMT1]] | +0.60 | +0.27 / +0.60 | both halves | 3e-04 |  |
| [[RALBP1]] | +0.60 | +0.26 / +0.58 | both halves | 4e-04 |  |
| [[HEATR5B]] | +0.59 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[WIPI2]] | +0.58 | +0.26 / +0.55 | both halves | 4e-04 |  |
| [[ZBTB49]] | +0.57 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[SHARPIN]] | +0.57 | +0.36 / +0.51 | both halves | 9e-05 |  |
| [[SCNM1]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LINC01881]] | +0.56 | +0.28 / +0.56 | both halves | 3e-04 |  |
| [[ZYG11B]] | +0.55 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[CLASRP]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS3]] | -0.53 | -0.18 / -0.50 | ⚠ one half (not replicated) | 9e-04 |  |
| [[HNRNPL]] | -0.53 | -0.16 / -0.52 | ⚠ one half (not replicated) | 0.001 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ATF7IP]] | -0.52 | -0.19 / -0.43 | ⚠ not reproduced | 8e-04 |  |
| [[CTSC]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TENM3]] | -0.48 | -0.15 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[ZNF462]] | -0.47 | -0.11 / -0.46 | ⚠ not reproduced | 0.002 |  |
| [[TUBA1B]] | -0.47 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[HEXB]] | -0.47 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | C | C9orf78's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | C9orf78's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.071 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.3, -44.3); signed map (-20.4, 10.6). **Vector** length 66.3, 19.0% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +11.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | +10.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +1.9 | +9.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 9 open reading frame 78 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,827,290-129,835,863 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC220, HCA59, CSU2 |
| Gene groups (HGNC) | Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ63](https://www.uniprot.org/uniprotkb/Q9NZ63) (Splicing factor C9orf78):

> Plays a role in pre-mRNA splicing by promoting usage of the upstream 3'-splice site at alternative NAGNAG splice sites; these are sites featuring alternative acceptor motifs separated by only a few nucleotides. May also modulate exon inclusion events. Plays a role in spliceosomal remodeling by displacing WBP4 from SNRNP200 and may act to inhibit SNRNP200 helicase activity. Binds U5 snRNA. Required for proper chromosome segregation. Not required for splicing of shelterin components.

**Summary**, from NCBI Gene [51759](https://www.ncbi.nlm.nih.gov/gene/51759):

> Enables U5 snRNA binding activity. Involved in mRNA cis splicing, via spliceosome and regulation of homologous chromosome segregation. Located in chromosome, centromeric region and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24932) · Entrez [51759](https://www.ncbi.nlm.nih.gov/gene/51759) · UniProt [Q9NZ63](https://www.uniprot.org/uniprotkb/Q9NZ63) · Ensembl [ENSG00000136819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136819)

## Data

Gene col 5909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5909); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5909]; `tensor/DDL_lfc|DDL_z.npy` [5909]; `embed/gene_vectors.npy` [5909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5909 or target_col == 5909). Every well: [[C9orf78 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C9orf78.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
