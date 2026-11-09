---
symbol: "SVIP"
type: "gene"
col: 12544
ensembl_id: "ENSG00000198168"
name: "small VCP interacting protein"
location: "11p14.3"
module: 5
arm: "-"
pooled_cpm: 26.2
n_lines_expressing: 44
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SVIP

*small VCP interacting protein* — 11p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.08× (z +14.2, q 8e-43, up in 37 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +4.7, q 3e-04, up in 25 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 6.35×, HOP62 7.31×, LS 180 6.57×, NCI-H460 6.14×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 6.85×, C32 8.16×, A549 7.31×, PANC-1 5.70×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HOP62 6.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.316×; ⚠ cell-cycle shift, explains ~0% of this change); [[Macitentan (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0813×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC2]] (+0.60, fdr 1e-05), [[MYO6]] (+0.59, fdr 3e-05), [[GPX4]] (+0.57, fdr 1e-05); moves opposite to [[DUS2]] (-0.61, fdr 3e-04), [[DDX56]] (-0.61, fdr 2e-05), [[RPTOR]] (-0.60, fdr 3e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RAB3IP]] → it (grade B ⚠); 2 go from it, the strongest it → [[RAB3IP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12544.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 6.35×, HOP62 7.31×, LS 180 6.57×, NCI-H460 6.14×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 6.85×, C32 8.16×, A549 7.31×, PANC-1 5.70×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HOP62 6.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **5.08×** | +14.2 | 8e-43 | 37/38 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.64×** | +12.9 | 2e-35 | 28/30 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.78×** | +8.2 | 3e-14 | 34/35 (HOP62, C32, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.0 | 9e-05 | 31/39 (CFPAC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +4.7 | 3e-04 | 25/42 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.62×** | +4.2 | 0.003 | 29/38 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.51×** | +3.6 | 0.026 | 24/41 (C32, NCI-H23, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.49×** | +3.5 | 0.037 | 18/41 (NCI-H23, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.49×** | +3.4 | 0.045 | 20/40 (SK-MEL-2, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.49×** | +3.4 | 0.045 | 22/41 (C32, NCI-H460, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12544.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.316×; ⚠ cell-cycle shift, explains ~0% of this change); [[Macitentan (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0813×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.440× | -3.7 | 0.11 | 24/40 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.666× | -3.5 | 0.12 | 22/41 (HEC-1-A, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 22.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.31× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 17.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 19.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.31× (z +11.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 27.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.16× (z +11.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 20.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.4× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 60.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 25.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 47.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.50× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 21.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.71× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HCT15 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.05× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HEC-1-A (line)]] | alt | 42.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0813× (z -8.7) |
| [[KATO III (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.16× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.104× (z -9.8) |
| [[SW480 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC2]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MYO6]] | +0.59 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[GPX4]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[DENND4A]] | +0.56 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[MAPK8]] | +0.56 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[CD83]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SPOPL]] | +0.55 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[RAB3IP]] | +0.55 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[HMSD]] | +0.54 | +0.26 / +0.53 | both halves | 3e-04 |  |
| [[UNC13B]] | +0.53 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[TXNDC16]] | +0.53 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[CYRIA]] | +0.53 | +0.39 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUS2]] | -0.61 | -0.26 / -0.58 | both halves | 3e-04 |  |
| [[DDX56]] | -0.61 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[RPTOR]] | -0.60 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[DHX37]] | -0.59 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[COX10]] | -0.59 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[TSR1]] | -0.58 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[WDR81]] | -0.57 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[TRMT1]] | -0.55 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[LRRC41]] | -0.55 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[MCM3AP]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[METTL13]] | -0.54 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[GATB]] | -0.54 | -0.25 / -0.61 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB3IP]] | B | RAB3IP activity raises SVIP's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 2.23× lower at baseline in the lines without RAB3IP | 0.072 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SVIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB3IP]] | B | SVIP activity raises RAB3IP's level | lines that do not express SVIP (6) vs lines expressing it (44) | 2.16× lower at baseline in the lines without SVIP | 0.067 | ⚠ within organs, on part of the lines; also absent: PLEKHA5, LRRCC1, USP53; maybe low, not absent; its own permutation p |
| [[AFDN]] | B | SVIP activity raises AFDN's level | lines that do not express SVIP (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without SVIP | 0.067 | ⚠ within organs, on part of the lines; also absent: PLEKHA5, LRRCC1, USP53; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-7.7, -50.2); signed map (46.3, 2.0). **Vector** length 65.0, 17.1% of its response variance represented; |z| ≥ 3 in 595 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +1.7 | +14.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | -0.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | small VCP interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.3 — chr11:22,813,799-22,830,299 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313A2432 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHG7](https://www.uniprot.org/uniprotkb/Q8NHG7) (Small VCP/p97-interacting protein):

> Negative regulator of the ER-associated degradation pathway (ERAD) of misfolded proteins. It competes with AMFR/gp78 for binding VCP/p97, and inhibits AMFR/gp78-VCP/p97 complex formation that is required for degradation of ERAD substrates. Involved in the regulation of adrenal cortisol and dehydroepiandrosterone (DHEA) biosynthesis.

**Summary**, from NCBI Gene [258010](https://www.ncbi.nlm.nih.gov/gene/258010):

> Endoplasmic reticulum-associated degradation (ERAD) is the pathway by which misfolded proteins in the endoplasmic reticulum are targeted to the proteasome for degradation. Multiple specialized proteins interact with one another during ERAD to complete this process. The protein encoded by this gene is an inhibitor of ERAD, functioning to disrupt the interaction of these protein components. This downregulation of ERAD may be needed to protect the cell from overactive protein degradation. Several …

**Accessions** — [HGNC:25238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25238) · Entrez [258010](https://www.ncbi.nlm.nih.gov/gene/258010) · UniProt [Q8NHG7](https://www.uniprot.org/uniprotkb/Q8NHG7) · Ensembl [ENSG00000198168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198168)

## Data

Gene col 12544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12544); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12544]; `tensor/DDL_lfc|DDL_z.npy` [12544]; `embed/gene_vectors.npy` [12544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12544 or target_col == 12544). Every well: [[SVIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SVIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
