---
symbol: "REXO1"
type: "gene"
col: 1250
ensembl_id: "ENSG00000079313"
name: "RNA exonuclease 1 homolog"
location: "19p13.3"
module: 204
arm: "+"
pooled_cpm: 20.83
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# REXO1

*RNA exonuclease 1 homolog* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.79× (z +13.2, q 5e-37, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.790× (z -5.4, q 4e-05, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.209×, C32 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.286×; ⚠ cell-cycle shift, explains ~0% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (BT-474 0.173×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRCAP]] (+0.77, fdr 7e-06), [[FEM1A]] (+0.71, fdr 7e-06), [[MCM3AP]] (+0.70, fdr 7e-06); moves opposite to [[PPP1R2]] (-0.70, fdr 7e-06), [[USP3]] (-0.68, fdr 9e-06), [[RAB8B]] (-0.65, fdr 7e-06).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +13.2 | 5e-37 | 39/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +9.2 | 1e-17 | 36/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +7.0 | 4e-10 | 33/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +7.0 | 4e-10 | 34/45 (MIA PaCa-2, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 4e-06 | 30/47 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +5.4 | 7e-06 | 27/47 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +5.3 | 9e-06 | 26/47 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +5.3 | 1e-05 | 23/47 (A-172, SW480, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.0 | 4e-05 | 1/48 (C32) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +4.9 | 4e-05 | 25/48 (COLO 205, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.003 | 19/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.9 | 0.005 | 15/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.007 | 9/48 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.8 | 0.007 | 15/46 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.22×** | +3.1 | 0.075 | 12/47 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.080 | 14/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1250.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.209×, C32 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.286×; ⚠ cell-cycle shift, explains ~0% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (BT-474 0.173×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -5.4 | 4e-05 | 22/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.786×** | -3.9 | 0.028 | 15/48 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.824× | -3.1 | 0.25 | 17/47 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Verteporfin (drug)]] 5 µM |  | 0.820× | -3.1 | 0.25 | 15/47 (HS-578T, SW 900, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.876× | -3.0 | 0.25 | 8/48 (LOX-IMVI, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 27.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 15.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +14.4) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.127× (z -8.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 19.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.9) | — |
| [[A-427 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.173× (z -9.2) |
| [[C32 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRCAP]] | +0.77 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[FEM1A]] | +0.71 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[MCM3AP]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[THOC6]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[BRD9]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[SCAF1]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 | STRING 815 |
| [[PUF60]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SSU72]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[CRK]] | +0.65 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[WDR82]] | +0.65 | +0.58 / +0.65 | both halves | 8e-06 | same gene group |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R2]] | -0.70 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[USP3]] | -0.68 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[RAB8B]] | -0.65 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[FHIP1A]] | -0.64 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[HDAC3]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[ARL3]] | -0.64 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[TBC1D12]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.62 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[SRP54-AS1]] | -0.62 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[TRIM33]] | -0.61 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[FNBP1L]] | -0.61 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[SGK3]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises REXO1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction -0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.0, -18.3); signed map (2.0, -33.4). **Vector** length 80.2, 15.0% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +9.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.9 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | +2.4 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | RNA exonuclease 1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,815,248-1,848,483 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EloA-BP1, KIAA1138; previously TCEB3BP1 |
| Gene groups (HGNC) | Exonucleases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N1G1](https://www.uniprot.org/uniprotkb/Q8N1G1) (RNA exonuclease 1 homolog):

> Seems to have no detectable effect on transcription elongation in vitro.

**Summary**, from NCBI Gene [57455](https://www.ncbi.nlm.nih.gov/gene/57455):

> Predicted to enable exonuclease activity. Predicted to be involved in rRNA 3'-end processing. Located in nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24616) · Entrez [57455](https://www.ncbi.nlm.nih.gov/gene/57455) · UniProt [Q8N1G1](https://www.uniprot.org/uniprotkb/Q8N1G1) · Ensembl [ENSG00000079313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079313)

## Data

Gene col 1250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1250); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1250]; `tensor/DDL_lfc|DDL_z.npy` [1250]; `embed/gene_vectors.npy` [1250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1250 or target_col == 1250). Every well: [[REXO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REXO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
