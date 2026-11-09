---
symbol: "GAA"
type: "gene"
col: 10085
ensembl_id: "ENSG00000171298"
name: "alpha glucosidase"
location: "17q25.3"
module: 50
arm: "+"
pooled_cpm: 15.16
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# GAA

*alpha glucosidase* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.20× (z +11.4, q 4e-27, up in 19 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 1.20× (z +3.7, q 0.022, up in 13 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 3.50×, SHP-77 3.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 2.99×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.408× (z -13.4, q 3e-38, down in 40 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6AP1]] (+0.64, fdr 9e-06), [[LAMP1]] (+0.64, fdr 1e-05), [[SUMF2]] (+0.63, fdr 1e-05); moves opposite to [[CCDC137]] (-0.53, fdr 4e-05), [[PPP1R12A]] (-0.52, fdr 3e-05), [[EIF5B]] (-0.51, fdr 5e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GSTM2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10085.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 3.50×, SHP-77 3.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 2.99×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +11.4 | 4e-27 | 19/26 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +9.4 | 1e-18 | 29/38 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +8.1 | 8e-14 | 21/33 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.7 | 2e-06 | 19/41 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +3.7 | 0.022 | 13/46 (C-33 A, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.6 | 0.036 | 13/46 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.088 | 8/45 (C-33 A, SNU-423, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.15 | 8/45 (HEC-1-A, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10085.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.408×** | -13.4 | 3e-38 | 40/45 (SW48, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.500×** | -10.0 | 6e-21 | 31/45 (Panc 03.27, H4, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.634×** | -9.6 | 1e-19 | 33/45 (H4, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -7.8 | 1e-12 | 27/45 (H4, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.612×** | -7.3 | 3e-11 | 26/46 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -5.9 | 3e-07 | 23/45 (RPMI-7951, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -5.9 | 4e-07 | 21/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -5.7 | 6e-07 | 22/45 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.722×** | -4.9 | 7e-05 | 21/44 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -4.7 | 1e-04 | 20/46 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.730×** | -4.7 | 1e-04 | 15/46 (C-33 A, SW480, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.724×** | -4.6 | 2e-04 | 18/44 (NCI-H2030, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.563×** | -4.5 | 3e-04 | 16/36 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -4.4 | 4e-04 | 16/45 (SW48, Panc 03.27, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.744×** | -4.4 | 4e-04 | 17/45 (NCI-H23, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.580×** | -4.3 | 7e-04 | 22/42 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -3.5 | 0.013 | 18/46 (SW 1088, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.784×** | -3.4 | 0.019 | 14/45 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.024 | 7/46 (BT-474, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.790×** | -3.3 | 0.028 | 7/43 (MIA PaCa-2, NCI-H661, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.805×** | -3.2 | 0.028 | 18/45 (SW48, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 39.0 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -8.9) |
| [[HOP62 (line)]] | alt | 27.4 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0359× (z -13.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.4) |
| [[A549 (line)]] | wt | 18.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 26.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 28.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +8.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.229× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW48 (line)]] | wt | 15.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0685× (z -11.2) |
| [[A498 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.104× (z -8.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 8.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0517× (z -10.8) |
| [[LoVo (line)]] | wt | 11.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.226× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -9.2) |
| [[A-172 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6AP1]] | +0.64 | +0.57 / +0.61 | both halves | 9e-06 | pathway: HALLMARK_MYOGENESIS |
| [[LAMP1]] | +0.64 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[SUMF2]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[LAMB2]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[SELENON]] | +0.63 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ABCA2]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[GANAB]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 | same gene group; STRING 429 |
| [[PLBD2]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ZBED6]] | +0.61 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[EMC10]] | +0.61 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[LENG8]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[RPL10]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC137]] | -0.53 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[PPP1R12A]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[EIF5B]] | -0.51 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[KIFBP]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PSMA7]] | -0.50 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[DNTTIP2]] | -0.49 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[FAM32A]] | -0.48 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[MIS18A]] | -0.48 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSTM2]] | C | GSTM2 activity raises GAA's level | lines that do not express GSTM2 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without GSTM2 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLEC2D, IMPG2, ENSG00000286952; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.8, -22.0); signed map (-25.8, -36.8). **Vector** length 65.5, 10.7% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +5.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -13.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.0 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | alpha glucosidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:80,101,533-80,119,881 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycoside hydrolase family 31 |
| Hallmark sets | MYOGENESIS, HYPOXIA |
| Reactome | 8 pathways, smallest: Glycogen storage diseases; Glycogen breakdown (glycogenolysis); Glycogen metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P10253](https://www.uniprot.org/uniprotkb/P10253) (Lysosomal alpha-glucosidase):

> Essential for the degradation of glycogen in lysosomes. Has highest activity on alpha-1,4-linked glycosidic linkages, but can also hydrolyze alpha-1,6-linked glucans.

**Summary**, from NCBI Gene [2548](https://www.ncbi.nlm.nih.gov/gene/2548):

> This gene encodes lysosomal alpha-glucosidase, which is essential for the degradation of glycogen to glucose in lysosomes. The encoded preproprotein is proteolytically processed to generate multiple intermediate forms and the mature form of the enzyme. Defects in this gene are the cause of glycogen storage disease II, also known as Pompe's disease, which is an autosomal recessive disorder with a broad clinical spectrum. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:4065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4065) · Entrez [2548](https://www.ncbi.nlm.nih.gov/gene/2548) · UniProt [P10253](https://www.uniprot.org/uniprotkb/P10253) · Ensembl [ENSG00000171298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171298)

## Data

Gene col 10085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10085); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10085]; `tensor/DDL_lfc|DDL_z.npy` [10085]; `embed/gene_vectors.npy` [10085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10085 or target_col == 10085). Every well: [[GAA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
