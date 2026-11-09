---
symbol: "HECW1"
type: "gene"
col: 23
ensembl_id: "ENSG00000002746"
name: "HECT, C2 and WW domain containing E3 ubiquitin protein ligase 1"
location: "7p14.1-p13"
module: 72
arm: "+"
pooled_cpm: 13.04
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# HECW1

*HECT, C2 and WW domain containing E3 ubiquitin protein ligase 1* — 7p14.1-p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +11.4, q 1e-27, up in 21 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +10.3, q 3e-22, up in 29 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Glycyrrhizic acid (drug)]] 0.5 µM: 0.672× (z -4.1, q 0.021, down in 13 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.0948×, A549 0.268×, NCI-H460 0.309×; ⚠ cell-cycle shift, would explain all of this change); [[Flutamide (drug)]] 0.5 µM in 1 line (RKO 0.0956×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.113×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEGFD]] (+0.56, fdr 2e-05), [[LINC00607]] (+0.56, fdr 2e-05), [[ALDH2]] (+0.56, fdr 1e-05); moves opposite to [[MYBL1]] (-0.43, fdr 2e-04), [[AGRN]] (-0.42, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00871]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 23.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +11.4 | 1e-27 | 21/30 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +10.3 | 3e-22 | 29/42 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +9.1 | 1e-17 | 9/17 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.19×** | +7.6 | 3e-12 | 28/42 (H4, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +7.2 | 8e-11 | 11/22 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +6.9 | 5e-10 | 28/44 (KATO III, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +6.4 | 1e-08 | 26/43 (HOP62, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +6.3 | 2e-08 | 28/46 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +6.0 | 1e-07 | 21/44 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +4.9 | 6e-05 | 17/43 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.7 | 2e-04 | 13/37 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.23×** | +4.3 | 7e-04 | 11/29 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.3 | 8e-04 | 17/43 (BT-474, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.3 | 8e-04 | 20/45 (J82, RKO, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.001 | 14/44 (NCI-H1792, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.012 | 16/46 (SHP-77, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.018 | 9/42 (SW 900, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +2.9 | 0.087 | 18/44 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.098 | 3/44 (A-172, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 23.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.0948×, A549 0.268×, NCI-H460 0.309×; ⚠ cell-cycle shift, would explain all of this change); [[Flutamide (drug)]] 0.5 µM in 1 line (RKO 0.0956×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.672×** | -4.1 | 0.021 | 13/42 (NCI-H1792, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 23. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 48.8 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 7.15× (z +10.7) | — |
| [[H4 (line)]] | wt | 58.8 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 12.1× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 11.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.2× (z +11.4) | — |
| [[A549 (line)]] | wt | 27.0 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.68× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 8.53 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 18.0× (z +11.1) | — |
| [[A498 (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -16.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 4.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.43× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -8.7) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H2030 (line)]] | alt | 5.46 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.113× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 14.6 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0956× (z -10.5) |
| [[SNU-1 (line)]] | wt | 25.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 5.37 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 23), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEGFD]] | +0.56 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[LINC00607]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ALDH2]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 | same gene group |
| [[ANKRD23]] | +0.54 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[NMRAL2P]] | +0.54 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[SMIM20]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[AKR1C1]] | +0.53 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[TDO2]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[SOD1]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 | STRING 813 |
| [[PSMB4]] | +0.53 | +0.56 / +0.39 | both halves | 6e-05 | pathway: Degradation of DVL; STRING 444 |
| [[DYNC1I1]] | +0.52 | +0.56 / +0.55 | both halves | 1e-05 | STRING 465 |
| [[CMKLR2]] | +0.52 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYBL1]] | -0.43 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[AGRN]] | -0.42 | -0.40 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00871]] | B | LINC00871 activity raises HECW1's level | lines that do not express LINC00871 (12) vs lines expressing it (38) | 1.00× lower at baseline in the lines without LINC00871 | 0.041 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MGST1]] | B | MGST1 activity raises HECW1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without MGST1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.2, 50.5); signed map (-25.1, -22.3). **Vector** length 70.0, 12.3% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +2.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.8 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +2.0 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | HECT, C2 and WW domain containing E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1-p13 — chr7:43,112,629-43,566,001 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0322, NEDL1 |
| Gene groups (HGNC) | C2 domain containing; MicroRNA protein coding host genes; Nedd4 family E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Degradation of DVL; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76N89](https://www.uniprot.org/uniprotkb/Q76N89) (E3 ubiquitin-protein ligase HECW1):

> E3 ubiquitin-protein ligase that mediates ubiquitination and subsequent degradation of DVL1. Also targets the mutant SOD1 protein involved in familial amyotrophic lateral sclerosis (FALS). Forms cytotoxic aggregates with DVL1, SSR3 and mutant SOD1 that lead to motor neuron death in FALS.

**Summary**, from NCBI Gene [23072](https://www.ncbi.nlm.nih.gov/gene/23072):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in regulation of dendrite morphogenesis and ubiquitin-dependent protein catabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22195) · Entrez [23072](https://www.ncbi.nlm.nih.gov/gene/23072) · UniProt [Q76N89](https://www.uniprot.org/uniprotkb/Q76N89) · Ensembl [ENSG00000002746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000002746)

## Data

Gene col 23: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 23); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 23, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 23]; `tensor/DDL_lfc|DDL_z.npy` [23]; `embed/gene_vectors.npy` [23]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 23 or target_col == 23). Every well: [[HECW1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HECW1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
