---
symbol: "TTI2"
type: "gene"
col: 5000
ensembl_id: "ENSG00000129696"
name: "TELO2 interacting protein 2"
location: "8p12"
module: 149
arm: "+"
pooled_cpm: 14.78
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# TTI2

*TELO2 interacting protein 2* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +16.5, q 0e+00, up in 42 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LS 180 0.136×, NCI-H2347 0.298×, HEC-1-A 0.285×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Alpelisib (drug)]] 0.05 µM in 1 line (SNU-1 0.0645×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0738×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (BT-474 0.0777×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM29]] (+0.74, fdr 7e-06), [[ACOT8]] (+0.70, fdr 7e-06), [[EAPP]] (+0.69, fdr 7e-06); moves opposite to [[IPO7]] (-0.73, fdr 7e-06), [[MTHFD1]] (-0.62, fdr 1e-05), [[PRKDC]] (-0.61, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SACS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +16.5 | 0e+00 | 42/47 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.35×** | +13.2 | 2e-37 | 42/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +13.0 | 4e-36 | 44/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +12.4 | 6e-33 | 42/47 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +12.3 | 1e-32 | 43/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +11.2 | 3e-27 | 39/47 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.85×** | +10.9 | 6e-26 | 40/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +9.7 | 3e-20 | 31/43 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.75×** | +8.7 | 2e-16 | 29/46 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.66×** | +7.9 | 1e-13 | 28/48 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.56×** | +6.7 | 1e-09 | 25/47 (HEC-1-A, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.45×** | +5.8 | 3e-07 | 22/46 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +5.7 | 6e-07 | 25/47 (LOX-IMVI, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.7 | 6e-07 | 26/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.40×** | +5.2 | 7e-06 | 19/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.9 | 3e-05 | 20/47 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +4.7 | 7e-05 | 18/44 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 7e-05 | 18/47 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.5 | 2e-04 | 15/46 (LoVo, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.020 | 8/47 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.044 | 6/47 (NCI-H460, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5000.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LS 180 0.136×, NCI-H2347 0.298×, HEC-1-A 0.285×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Alpelisib (drug)]] 0.05 µM in 1 line (SNU-1 0.0645×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0738×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (BT-474 0.0777×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.795× | -3.4 | 0.45 | 9/48 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.819× | -3.1 | 0.57 | 8/48 (C32, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 17.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 15.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 15.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 16.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +11.2) | — |
| [[SW480 (line)]] | alt | 17.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.7) | — |
| [[A-172 (line)]] | wt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.3) | — |
| [[A498 (line)]] | wt | 27.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.0) | — |
| [[A549 (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0777× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0738× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.5) | — |
| [[RKO (line)]] | wt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0645× (z -11.9) |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM29]] | +0.74 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ACOT8]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[EAPP]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[KLHL20]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[CWC15]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[BRAP]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[PEX11B]] | +0.67 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[TERF2IP]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PEX13]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[YJU2B]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PSMD5]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | same gene group |
| [[ZNF766]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO7]] | -0.73 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[MTHFD1]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 | same gene group; STRING 533 |
| [[IPO5]] | -0.61 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.61 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[MAPRE1]] | -0.60 | -0.39 / -0.65 | both halves | 5e-05 |  |
| [[AHCY]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[HNRNPAB]] | -0.59 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[SERBP1]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[LRPPRC]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[NONO]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[DOCK1]] | -0.57 | -0.52 / -0.60 | both halves | 1e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SACS]] | B | SACS activity raises TTI2's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without SACS | 0.062 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.7, -6.2); signed map (-9.0, -10.8). **Vector** length 59.0, 9.18% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +9.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +16.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +12.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +4.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.4 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -1.8 | -2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -1.7 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | TELO2 interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:33,473,386-33,513,185 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23263; previously C8orf41 |
| Gene groups (HGNC) | TTT complex; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NXR4](https://www.uniprot.org/uniprotkb/Q6NXR4) (TELO2-interacting protein 2):

> Regulator of the DNA damage response (DDR). Part of the TTT complex that is required to stabilize protein levels of the phosphatidylinositol 3-kinase-related protein kinase (PIKK) family proteins. The TTT complex is involved in the cellular resistance to DNA damage stresses, like ionizing radiation (IR), ultraviolet (UV) and mitomycin C (MMC). Together with the TTT complex and HSP90 may participate in the proper folding of newly synthesized PIKKs.

**Summary**, from NCBI Gene [80185](https://www.ncbi.nlm.nih.gov/gene/80185):

> This gene encodes a regulator of the DNA damage response. The protein is a component of the Triple T complex (TTT) which also includes telomere length regulation protein and TELO2 interacting protein 1. The TTT complex is involved in cellular resistance to DNA damage stresses and may act as a regulator of phosphoinositide-3-kinase-related protein kinase (PIKK) abundance. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:26262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26262) · Entrez [80185](https://www.ncbi.nlm.nih.gov/gene/80185) · UniProt [Q6NXR4](https://www.uniprot.org/uniprotkb/Q6NXR4) · Ensembl [ENSG00000129696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129696)

## Data

Gene col 5000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5000); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5000]; `tensor/DDL_lfc|DDL_z.npy` [5000]; `embed/gene_vectors.npy` [5000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5000 or target_col == 5000). Every well: [[TTI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
