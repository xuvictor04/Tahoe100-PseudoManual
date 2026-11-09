---
symbol: "ETFB"
type: "gene"
col: 2593
ensembl_id: "ENSG00000105379"
name: "electron transfer flavoprotein subunit beta"
location: "19q13.41"
module: 48
arm: "+"
pooled_cpm: 34.17
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ETFB

*electron transfer flavoprotein subunit beta* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.18× (z +8.6, q 5e-15, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (MIA PaCa-2 7.72×, NCI-H460 5.34×, NCI-H1573 6.61×, HEC-1-A 4.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 4.81×, PANC-1 4.36×, A549 6.19×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.554× (z -6.3, q 2e-07, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPM3]] (+0.70, fdr 9e-06), [[CHMP2A]] (+0.67, fdr 1e-05), [[TRAPPC5]] (+0.64, fdr 3e-05); moves opposite to [[KCTD15]] (-0.59, fdr 4e-05), [[EPM2A]] (-0.57, fdr 2e-04), [[TMEM117]] (-0.56, fdr 9e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00511]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2593.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (MIA PaCa-2 7.72×, NCI-H460 5.34×, NCI-H1573 6.61×, HEC-1-A 4.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 4.81×, PANC-1 4.36×, A549 6.19×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.18×** | +8.6 | 5e-15 | 43/43 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.79×** | +7.4 | 4e-11 | 31/33 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +5.9 | 5e-07 | 26/36 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.72×** | +4.1 | 0.007 | 32/45 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.57×** | +3.4 | 0.074 | 26/48 (KATO III, A549, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.37×** | +3.3 | 0.080 | 24/48 (HT-29, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.554×** | -6.3 | 2e-07 | 36/47 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.521×** | -4.9 | 3e-04 | 30/48 (H4, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.566×** | -4.3 | 0.004 | 32/47 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.595×** | -3.9 | 0.014 | 35/48 (NCI-H1792, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.342×** | -3.6 | 0.036 | 30/45 (BT-474, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.665× | -3.1 | 0.21 | 19/47 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.658× | -3.0 | 0.21 | 26/47 (hTERT-HPNE, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 52.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 30.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.4) |
| [[COLO 205 (line)]] | alt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -12.5) |
| [[H4 (line)]] | wt | 60.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 192 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.6) |
| [[KATO III (line)]] | alt | 60.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.72× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 51.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 21.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 63.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 15 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM3]] | +0.70 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[CHMP2A]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[TRAPPC5]] | +0.64 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[NDUFB11]] ⚠ | +0.64 | +0.50 / +0.69 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA3]] | +0.64 | +0.48 / +0.65 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[TMEM256]] | +0.63 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[ELOB]] | +0.61 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[ATP5ME]] | +0.61 | +0.43 / +0.62 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[DDT]] | +0.60 | +0.46 / +0.54 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[ANAPC11]] | +0.60 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[ATP5F1D]] ⚠ | +0.59 | +0.30 / +0.58 | both halves | 2e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; ⚠ in the vector space only through flagged drug-doses |
| [[UQCR10]] ⚠ | +0.59 | +0.39 / +0.63 | both halves | 5e-05 | pathway: HALLMARK_ADIPOGENESIS; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5PD]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 417 |
| [[NDUFB3]] | +0.59 | +0.39 / +0.67 | both halves | 6e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[POLR2I]] | +0.58 | +0.27 / +0.63 | both halves | 3e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD15]] | -0.59 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[EPM2A]] | -0.57 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[TMEM117]] | -0.56 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[EIF4G2]] | -0.55 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[NPEPL1]] | -0.54 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[FKBP4]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[FBXO30]] | -0.53 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[PRDM11]] | -0.52 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[EIF5]] | -0.52 | -0.39 / -0.26 | both halves | 4e-04 |  |
| [[WNT3]] | -0.52 | -0.39 / -0.26 | both halves | 4e-04 |  |
| [[CRPPA]] | -0.51 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[RNASEH1]] | -0.51 | -0.28 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00511]] | B | LINC00511 activity raises ETFB's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without LINC00511 | 0.079 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[PITPNA-AS1]] | C | PITPNA-AS1's natural level strengthens ETFB's drug response | PITPNA-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.20; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[RPA3]] | C | RPA3's natural level strengthens ETFB's drug response | RPA3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.29; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.6, -20.0); signed map (-35.3, 7.3). **Vector** length 62.0, 16.6% of its response variance represented; |z| ≥ 3 in 621 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.8 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +0.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.3 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | electron transfer flavoprotein subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:51,345,169-51,366,388 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Protein methylation; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P38117](https://www.uniprot.org/uniprotkb/P38117) (Electron transfer flavoprotein subunit beta):

> Heterodimeric electron transfer flavoprotein that accepts electrons from several mitochondrial dehydrogenases, including acyl-CoA dehydrogenases, glutaryl-CoA and sarcosine dehydrogenase. It transfers the electrons to the main mitochondrial respiratory chain via ETF-ubiquinone oxidoreductase (Probable). Required for normal mitochondrial fatty acid oxidation and normal amino acid metabolism. ETFB binds an AMP molecule that probably has a purely structural role.

**Summary**, from NCBI Gene [2109](https://www.ncbi.nlm.nih.gov/gene/2109):

> This gene encodes electron-transfer-flavoprotein, beta polypeptide, which shuttles electrons between primary flavoprotein dehydrogenases involved in mitochondrial fatty acid and amino acid catabolism and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. The gene deficiencies have been implicated in type II glutaricaciduria. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3482) · Entrez [2109](https://www.ncbi.nlm.nih.gov/gene/2109) · UniProt [P38117](https://www.uniprot.org/uniprotkb/P38117) · Ensembl [ENSG00000105379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105379)

## Data

Gene col 2593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2593); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2593]; `tensor/DDL_lfc|DDL_z.npy` [2593]; `embed/gene_vectors.npy` [2593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2593 or target_col == 2593). Every well: [[ETFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
