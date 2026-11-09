---
symbol: "NPHS1"
type: "gene"
col: 8427
ensembl_id: "ENSG00000161270"
name: "NPHS1 adhesion molecule, nephrin"
location: "19q13.12"
module: 181
arm: "+"
pooled_cpm: 4.1
n_lines_expressing: 46
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 18
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# NPHS1

*NPHS1 adhesion molecule, nephrin* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 55.8× (z +45.0, q 0e+00, up in 31 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW1417 0.0724×); [[OTS514 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0749×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD11B1-AS1]] (+0.75, fdr 7e-06), [[FEZ1]] (+0.72, fdr 7e-06), [[IL34]] (+0.72, fdr 7e-06); moves opposite to [[WDR5]] (-0.68, fdr 7e-06), [[ACTR5]] (-0.64, fdr 3e-05), [[SKP2]] (-0.63, fdr 3e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAPK8IP2]] → it (grade B ⚠); 18 go from it, the strongest it → [[SMPD3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **55.8×** | +45.0 | 0e+00 | 31/32 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **36.5×** | +40.2 | 0e+00 | 32/32 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **13.8×** | +19.9 | 0e+00 | 33/38 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **11.7×** | +19.5 | 0e+00 | 30/31 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **11.0×** | +18.2 | 0e+00 | 24/29 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **9.33×** | +17.0 | 0e+00 | 25/30 (HEC-1-A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **6.36×** | +14.6 | 0e+00 | 31/36 (HOP62, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.58×** | +11.6 | 5e-29 | 2/6 (HEC-1-A, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.62×** | +10.8 | 3e-25 | 21/42 (A-172, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.36×** | +9.6 | 5e-20 | 30/42 (PANC-1, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.03×** | +8.8 | 1e-16 | 26/42 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +8.7 | 1e-16 | 15/27 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.75×** | +8.0 | 6e-14 | 25/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.47×** | +7.1 | 4e-11 | 23/42 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.43×** | +7.0 | 1e-10 | 19/40 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.36×** | +6.8 | 5e-10 | 21/37 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.16×** | +6.1 | 3e-08 | 22/40 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +5.1 | 1e-05 | 18/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.83×** | +4.7 | 5e-05 | 15/39 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW1417 0.0724×); [[OTS514 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0749×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.652× | -3.4 | 0.20 | 5/42 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.636× | -3.4 | 0.20 | 11/33 (A-427, NCI-H23, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 16.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 79.0× (z +22.8) | — |
| [[A-172 (line)]] | wt | 3.87 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 90.5× (z +20.2) | — |
| [[PANC-1 (line)]] | alt | 5.13 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.6× (z +26.5) | — |
| [[HOP62 (line)]] | alt | 2.93 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 201× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 3.01 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 142× (z +21.5) | — |
| [[A498 (line)]] | wt | 4.59 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.4× (z +19.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.75 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.3× (z +15.7) | [[OTS514 (drug)]] 0.05 µM 0.0749× (z -8.5) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 3.64 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.0× (z +17.2) | — |
| [[C32 (line)]] | wt | 1.58 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 114× (z +12.1) | — |
| [[LoVo (line)]] | wt | 2.72 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 73.3× (z +17.5) | — |
| [[NCI-H1573 (line)]] | alt | 5.99 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +16.2) | — |
| [[RPMI-7951 (line)]] | alt | 4.32 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 73.7× (z +14.1) | — |
| [[SW 900 (line)]] | alt | 4.97 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.1× (z +16.6) | — |
| [[SW1417 (line)]] | alt | 4.06 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +11.2) | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0724× (z -8.5) |
| [[SW48 (line)]] | wt | 5.26 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 89.5× (z +12.3) | — |
| [[A549 (line)]] | wt | 19.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.7× (z +21.6) | — |
| [[BT-474 (line)]] | alt | 4.98 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 36.9× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 82.8× (z +14.9) | — |
| [[HCT15 (line)]] | alt | 11.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 2.53 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 48.7× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 2.44 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 235× (z +14.1) | — |
| [[J82 (line)]] | alt | 2.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 74.7× (z +14.9) | — |
| [[NCI-H2030 (line)]] | alt | 5.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +13.0) | — |
| [[NCI-H23 (line)]] | alt | 4.84 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.8× (z +15.7) | — |
| [[NCI-H2347 (line)]] | alt | 2.96 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 33.4× (z +17.8) | — |
| [[SNU-423 (line)]] | alt | 1.35 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.6× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 1.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 124× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 5.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.6× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 2.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 64.3× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 1.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 64.2× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 1.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 61.3× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 2.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 45.3× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 6.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +9.2) | — |
| [[A-427 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD11B1-AS1]] | +0.75 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[FEZ1]] | +0.72 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[IL34]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.71 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[KCNN1]] | +0.71 | +0.67 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[PLA2G4C]] | +0.70 | +0.74 / +0.57 | both halves | 8e-06 |  |
| [[SNX31]] | +0.70 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.70 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[PIK3IP1-DT]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[ACVR1C]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR5]] | -0.68 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[ACTR5]] | -0.64 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[SKP2]] | -0.63 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[HERC2P9]] | -0.63 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[POFUT1]] | -0.62 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MRPS27]] | -0.62 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ORC5]] | -0.62 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[HERC2]] | -0.61 | -0.43 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK8IP2]] | B | MAPK8IP2 activity raises NPHS1's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without MAPK8IP2 | 0.015 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[EDIL3-DT]] | B | EDIL3-DT activity lowers NPHS1's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 1.27× higher at baseline in the lines without EDIL3-DT | 0.024 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[TOP2A]] | B | TOP2A activity lowers NPHS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00944]] | B | LINC00944 activity lowers NPHS1's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.40× higher at baseline in the lines without LINC00944 | 0.079 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[ACVR1C]] | C | ACVR1C activity lowers NPHS1's level | lines that do not express ACVR1C (4) vs lines expressing it (46) | 1.98× higher at baseline in the lines without ACVR1C | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CORIN, HDAC2-AS2, ENSG00000249951; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMPD3]] | C | NPHS1 activity strengthens SMPD3's drug response | lines that do not express NPHS1 (4) vs lines expressing it (34) | the lines without NPHS1 respond 0.34× as strongly (z diff +2.84); strongest at Idarubicin (hydrochloride) 5 µM: 1.41x vs 11x (z diff +6.2) | 0.010 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[GABBR1]] | C | NPHS1 activity raises GABBR1's level | lines that do not express NPHS1 (4) vs lines expressing it (46) | 4.02× lower at baseline in the lines without NPHS1 | 0.018 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |
| cells under [[Almonertinib (hydrochloride) (drug)]] 5 µM | C | NPHS1 activity raises the cells' numbers under Almonertinib (hydrochloride) 5 µM (protects the cells) | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1: 0.82× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |
| [[PPP1R36]] | C | NPHS1 activity strengthens PPP1R36's drug response | lines that do not express NPHS1 (4) vs lines expressing it (41) | the lines without NPHS1 respond 0.17× as strongly (z diff +2.21); strongest at Idarubicin (hydrochloride) 5 µM: 1.41x vs 5.67x (z diff +4.7) | 0.037 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CCNP]] | C | NPHS1 activity lowers CCNP's level | lines that do not express NPHS1 (4) vs lines expressing it (46) | 2.43× higher at baseline in the lines without NPHS1 | 0.043 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |
| [[LINC02363]] | C | NPHS1 activity strengthens LINC02363's drug response | lines that do not express NPHS1 (4) vs lines expressing it (41) | the lines without NPHS1 respond 0.24× as strongly (z diff +1.22); strongest at Homoharringtonine 0.5 µM: 0.50x vs 3.21x (z diff +4.6) | 0.051 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CEACAM16-AS1]] | C | NPHS1 activity weakens CEACAM16-AS1's drug response | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1 respond 0.52× as strongly (z diff +0.84); strongest at Tucidinostat 0.5 µM: 3.18x vs 1.77x (z diff -3.8) | 0.052 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| cells under [[Glycyrrhizic acid (drug)]] 0.5 µM | C | NPHS1 activity lowers the cells' numbers under Glycyrrhizic acid 0.5 µM (makes them more sensitive) | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1: 1.36× the cells of the other lines | 0.057 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |
| [[PDE4C]] | C | NPHS1 activity strengthens PDE4C's drug response | lines that do not express NPHS1 (4) vs lines expressing it (40) | the lines without NPHS1 respond the other way (z diff +2.88); strongest at Harringtonine 5 µM: 0.19x vs 2.91x (z diff +8.0) | 0.059 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Binimetinib (drug)]] 0.05 µM | C | NPHS1 activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1: 0.75× the cells of the other lines | 0.061 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | C | NPHS1 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1: 1.29× the cells of the other lines | 0.066 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |
| cells under [[AZD-7648 (drug)]] 5 µM | C | NPHS1 activity raises the cells' numbers under AZD-7648 5 µM (protects the cells) | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1: 0.68× the cells of the other lines | 0.068 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.0, -6.5); signed map (23.9, 7.7). **Vector** length 77.2, 14.4% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +40.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +45.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +14.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.5 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | +7.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | NPHS1 adhesion molecule, nephrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,825,372-35,869,287 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CNF, NPHN |
| Gene groups (HGNC) | Fibronectin type III domain containing; V-set domain containing; C2-set domain containing |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 2 pathways, smallest: Nephrin family interactions; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [O60500](https://www.uniprot.org/uniprotkb/O60500) (Nephrin):

> Seems to play a role in the development or function of the kidney glomerular filtration barrier. Regulates glomerular vascular permeability. May anchor the podocyte slit diaphragm to the actin cytoskeleton. Plays a role in skeletal muscle formation through regulation of myoblast fusion (By similarity).

**Summary**, from NCBI Gene [4868](https://www.ncbi.nlm.nih.gov/gene/4868):

> This gene encodes a member of the immunoglobulin family of cell adhesion molecules that functions in the glomerular filtration barrier in the kidney. The gene is primarily expressed in renal tissues, and the protein is a type-1 transmembrane protein found at the slit diaphragm of glomerular podocytes. The slit diaphragm is thought to function as an ultrafilter to exclude albumin and other plasma macromolecules in the formation of urine. Mutations in this gene result in Finnish-type congenital …

**Accessions** — [HGNC:7908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7908) · Entrez [4868](https://www.ncbi.nlm.nih.gov/gene/4868) · UniProt [O60500](https://www.uniprot.org/uniprotkb/O60500) · Ensembl [ENSG00000161270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161270)

## Data

Gene col 8427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8427); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8427]; `tensor/DDL_lfc|DDL_z.npy` [8427]; `embed/gene_vectors.npy` [8427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8427 or target_col == 8427). Every well: [[NPHS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPHS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
