---
symbol: "RPP25"
type: "gene"
col: 10951
ensembl_id: "ENSG00000178718"
name: "ribonuclease P/MRP subunit p25"
location: "15q24.2"
module: 7
arm: "+"
pooled_cpm: 3.87
n_lines_expressing: 36
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RPP25

*ribonuclease P/MRP subunit p25* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.30× (z +8.2, q 1e-13, up in 16 of 18 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +5.2, q 6e-05, up in 20 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.0584×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX28]] (+0.65, fdr 7e-06), [[YDJC]] (+0.64, fdr 7e-06), [[ADO]] (+0.64, fdr 7e-06); moves opposite to [[SNAP23]] (-0.61, fdr 5e-05), [[CHP1]] (-0.58, fdr 3e-04), [[TM9SF2]] (-0.58, fdr 9e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HSD11B2]] → it (grade B ⚠); 7 go from it, the strongest it → [[RAC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.30×** | +8.2 | 1e-13 | 16/18 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.2 | 6e-05 | 20/28 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.98×** | +4.9 | 2e-04 | 16/33 (LOX-IMVI, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.92×** | +4.5 | 0.001 | 0/6 | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +4.4 | 0.002 | 10/33 (RKO, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.3 | 0.002 | 14/33 (Hs 766T, CFPAC-1, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +4.0 | 0.004 | 13/34 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +4.0 | 0.005 | 16/33 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.74×** | +3.9 | 0.005 | 9/18 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.034 | 11/33 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.61×** | +3.4 | 0.035 | 4/16 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +3.1 | 0.096 | 12/33 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.35× | +3.0 | 0.12 | 8/33 (SW48, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.0584×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.158×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.68 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0584× (z -10.2) |
| [[PANC-1 (line)]] | alt | 7.59 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[A-172 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX28]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[YDJC]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ADO]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[CCDC137]] | +0.62 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 | STRING 911 |
| [[GEMIN4]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[DNAAF2]] | +0.61 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[OXLD1]] | +0.61 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[TP53RK]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 | pathway: tRNA processing |
| [[GEMIN6]] | +0.60 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[HPS6]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAP23]] | -0.61 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[CHP1]] | -0.58 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[TM9SF2]] | -0.58 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[SEPTIN2]] | -0.57 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[VAMP7]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SAR1B]] | -0.55 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[OS9]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[DNAL1]] | -0.52 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[MORF4L1]] | -0.52 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[TMEM219]] | -0.51 | -0.65 / -0.36 | both halves | 9e-05 |  |
| [[MAGT1]] | -0.51 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD11B2]] | B | HSD11B2 activity raises RPP25's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without HSD11B2 | 0.089 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAC1]] | B | RPP25 activity raises RAC1's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without RPP25 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| [[NOP16]] | B | RPP25 activity raises NOP16's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.28× lower at baseline in the lines without RPP25 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| [[RPP38]] | B | RPP25 activity raises RPP38's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without RPP25 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| [[TLCD1]] | B | RPP25 activity raises TLCD1's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without RPP25 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| cells under [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM | B | RPP25 activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (protects the cells) | lines that do not express RPP25 (14) vs lines expressing it (34) | the lines without RPP25: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| [[SFT2D3]] | B | RPP25 activity raises SFT2D3's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.12× lower at baseline in the lines without RPP25 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| [[LBHD1]] | B | RPP25 activity raises LBHD1's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without RPP25 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-49.5, -1.7); signed map (-2.9, -36.3). **Vector** length 50.2, 9.53% of its response variance represented; |z| ≥ 3 in 553 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.2 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | -3.1 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -2.9 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -0.7 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -2.5 |
|  | [[Capivasertib (drug)]] 0.5 µM |  | -0.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease P/MRP subunit p25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:74,954,418-74,956,772 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20374 |
| Gene groups (HGNC) | Nuclear RNase P complex subunits; RNase MRP complex subunits |
| Reactome | 6 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Major pathway of rRNA processing in the nucleolus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUL9](https://www.uniprot.org/uniprotkb/Q9BUL9) (Ribonuclease P protein subunit p25):

> Component of ribonuclease P, a ribonucleoprotein complex that generates mature tRNA molecules by cleaving their 5'-ends. Also a component of the MRP ribonuclease complex, which cleaves pre-rRNA sequences.

**Summary**, from NCBI Gene [54913](https://www.ncbi.nlm.nih.gov/gene/54913):

> Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Located in nucleoplasm. Part of multimeric ribonuclease P complex and ribonuclease MRP complex. Biomarker of autistic disorder. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30361) · Entrez [54913](https://www.ncbi.nlm.nih.gov/gene/54913) · UniProt [Q9BUL9](https://www.uniprot.org/uniprotkb/Q9BUL9) · Ensembl [ENSG00000178718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178718)

## Data

Gene col 10951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10951); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10951]; `tensor/DDL_lfc|DDL_z.npy` [10951]; `embed/gene_vectors.npy` [10951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10951 or target_col == 10951). Every well: [[RPP25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPP25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
