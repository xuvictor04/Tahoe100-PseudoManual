---
symbol: "STUB1"
type: "gene"
col: 2348
ensembl_id: "ENSG00000103266"
name: "STIP1 homology and U-box containing protein 1"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 18.74
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# STUB1

*STIP1 homology and U-box containing protein 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.95× (z +9.2, q 3e-17, up in 38 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.69× (z +4.4, q 7e-04, up in 31 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 4.98×, PANC-1 4.04×, A498 3.44×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 3.61×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.603× (z -6.0, q 9e-07, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (37 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 66 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPUSD1]] (+0.73, fdr 1e-05), [[WRAP73]] (+0.72, fdr 5e-05), [[PUSL1]] (+0.71, fdr 3e-05); moves opposite to [[MFF-DT]] (-0.72, fdr 7e-04), [[GALNT7-DT]] (-0.71, fdr 0.001, ⚠ not reproduced), [[OXA1L-DT]] (-0.70, fdr 0.002, ⚠ one half only (not replicated)), [[PNISR-AS1]] (-0.69, fdr 4e-04), [[SEC24B-AS1]] (-0.62, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2348.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 4.98×, PANC-1 4.04×, A498 3.44×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 3.61×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.95×** | +9.2 | 3e-17 | 38/42 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.60×** | +8.1 | 2e-13 | 47/48 (A549, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.65×** | +7.9 | 4e-13 | 26/31 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.51×** | +7.8 | 1e-12 | 46/48 (A549, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.18×** | +6.6 | 4e-09 | 42/47 (A549, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.98×** | +5.0 | 5e-05 | 24/36 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.77×** | +4.8 | 1e-04 | 32/43 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +4.4 | 7e-04 | 31/46 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.48×** | +3.3 | 0.058 | 24/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2348.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.603×** | -6.0 | 9e-07 | 37/47 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -4.4 | 0.003 | 28/48 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.638×** | -3.8 | 0.028 | 29/47 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.647×** | -3.7 | 0.034 | 25/48 (J82, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -3.6 | 0.034 | 23/47 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.380×** | -3.5 | 0.034 | 22/45 (LoVo, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -3.5 | 0.034 | 26/48 (LoVo, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.673×** | -3.3 | 0.059 | 22/47 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 31.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LoVo (line)]] | wt | 18.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -10.3) |
| [[PANC-1 (line)]] | alt | 30.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.1) |
| [[A-427 (line)]] | wt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -17.8) |
| [[H4 (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -8.5) |
| [[A-172 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 11 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPUSD1]] | +0.73 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[WRAP73]] | +0.72 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[PUSL1]] | +0.71 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[METTL26]] | +0.71 | +0.35 / +0.55 | both halves | 1e-04 | ⚠ same locus (43.9 kb: neighbours can correlate without regulation) |
| [[C20orf27]] | +0.69 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[SMYD3]] | +0.69 | +0.31 / +0.39 | both halves | 2e-04 |  |
| [[SNRNP25]] | +0.69 | +0.43 / +0.53 | both halves | 4e-05 |  |
| [[NAA10]] ⚠ | +0.68 | +0.39 / +0.48 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KCTD17]] | +0.68 | +0.54 / +0.26 | both halves | 4e-04 |  |
| [[HDGFL2]] | +0.68 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[YIF1B]] | +0.67 | +0.36 / +0.28 | both halves | 3e-04 |  |
| [[ANTKMT]] | +0.67 | +0.33 / +0.53 | both halves | 1e-04 | ⚠ same locus (37.7 kb, same strand: neighbours can correlate without regulation) |
| [[CPTP]] | +0.67 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[DVL1]] | +0.66 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[PAFAH1B3]] | +0.66 | +0.33 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 55 of them with an alert (⚠; 55 not replicated); shown: the 12 strongest and the 7 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF-DT]] | -0.72 | -0.42 / -0.21 | both halves | 7e-04 |  |
| [[GALNT7-DT]] | -0.71 | -0.42 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[OXA1L-DT]] | -0.70 | -0.54 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[TMEM202-AS1]] | -0.69 | -0.43 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[PNISR-AS1]] | -0.69 | -0.41 / -0.24 | both halves | 4e-04 |  |
| [[PBLD]] | -0.69 | -0.41 / -0.00 | ⚠ not reproduced | 0.009 |  |
| [[EFCAB5]] | -0.68 | -0.48 / -0.07 | ⚠ not reproduced | 0.004 |  |
| [[LRRC37A3]] | -0.68 | -0.42 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[TSTD3]] | -0.67 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[SEPTIN7-DT]] | -0.67 | -0.49 / -0.08 | ⚠ not reproduced | 0.003 |  |
| [[MAILR]] | -0.67 | -0.50 / +0.00 | ⚠ one half (not replicated) | 1.00 |  |
| [[KMT2E-AS1]] | -0.66 | -0.47 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[SEC24B-AS1]] | -0.62 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[LRP2BP]] | -0.62 | -0.43 / -0.24 | both halves | 4e-04 |  |
| [[LINC00938]] | -0.61 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[GLIPR1-AS1]] | -0.61 | -0.31 / -0.23 | both halves | 5e-04 |  |
| [[GIPC2]] | -0.60 | -0.40 / -0.21 | both halves | 7e-04 |  |
| [[CYB5D2]] | -0.60 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[HLA-DMA]] | -0.60 | -0.41 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers STUB1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LY96]] | B | LY96 activity lowers STUB1's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.26× higher at baseline in the lines without LY96 | 0.064 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, 13.7); signed map (-31.6, 2.9). **Vector** length 62.6, 14.6% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.1 | +8.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.1 | +7.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.0 | +6.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.2 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +0.9 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +0.9 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -3.4 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | STIP1 homology and U-box containing protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:680,224-682,870 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBOX1, CHIP, SDCCAG7, HSPABP2, NY-CO-7 |
| Gene groups (HGNC) | U-box domain containing; Tetratricopeptide repeat domain containing |
| Reactome | 23 pathways, smallest: Downregulation of TGF-beta receptor signaling; Downregulation of ERBB2 signaling; RIPK1-mediated regulated necrosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNE7](https://www.uniprot.org/uniprotkb/Q9UNE7) (E3 ubiquitin-protein ligase CHIP):

> E3 ubiquitin-protein ligase which targets misfolded chaperone substrates towards proteasomal degradation. Plays a role in the maintenance of mitochondrial morphology and promotes mitophagic removal of dysfunctional mitochondria; thereby acts as a protector against apoptosis in response to cellular stress (By similarity). Negatively regulates vascular smooth muscle contraction, via degradation of the transcriptional activator MYOCD and subsequent loss of transcription of genes involved in …

**Summary**, from NCBI Gene [10273](https://www.ncbi.nlm.nih.gov/gene/10273):

> This gene encodes a protein containing tetratricopeptide repeat and a U-box that functions as a ubiquitin ligase/cochaperone. The encoded protein binds to and ubiquitinates shock cognate 71 kDa protein (Hspa8) and DNA polymerase beta (Polb), among other targets. Mutations in this gene cause spinocerebellar ataxia, autosomal recessive 16. Alternative splicing results in multiple transcript variants. There is a pseudogene for this gene on chromosome 2. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:11427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11427) · Entrez [10273](https://www.ncbi.nlm.nih.gov/gene/10273) · UniProt [Q9UNE7](https://www.uniprot.org/uniprotkb/Q9UNE7) · Ensembl [ENSG00000103266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103266)

## Data

Gene col 2348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2348); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2348]; `tensor/DDL_lfc|DDL_z.npy` [2348]; `embed/gene_vectors.npy` [2348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2348 or target_col == 2348). Every well: [[STUB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STUB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
