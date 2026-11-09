---
symbol: "FAM199X"
type: "gene"
col: 4445
ensembl_id: "ENSG00000123575"
name: "family with sequence similarity 199, X-linked"
location: "Xq22.2"
module: 25
arm: "+"
pooled_cpm: 50.17
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# FAM199X

*family with sequence similarity 199, X-linked* — Xq22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.64× (z +9.0, q 1e-16, up in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.33× (z +5.4, q 1e-05, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.833× (z -4.9, q 6e-04, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~0% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.324×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.230×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (H4 0.268×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLD]] (+0.69, fdr 7e-06), [[UBQLN1]] (+0.66, fdr 1e-05), [[MTMR6]] (+0.64, fdr 1e-05); moves opposite to [[KCNJ14]] (-0.64, fdr 1e-05), [[ZNF335]] (-0.64, fdr 8e-06), [[ARMC5]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IRX5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PHACTR4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +9.0 | 1e-16 | 37/42 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +7.9 | 8e-13 | 31/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +7.5 | 1e-11 | 30/47 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.9 | 5e-07 | 30/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +5.4 | 1e-05 | 32/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 1e-05 | 29/48 (SNU-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +5.0 | 5e-05 | 25/48 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.20×** | +4.9 | 8e-05 | 24/48 (SNU-423, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.0 | 0.004 | 21/48 (H4, A-427, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.23×** | +3.9 | 0.004 | 21/46 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.005 | 18/48 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.007 | 18/47 (SNU-423, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +3.6 | 0.014 | 18/48 (LOX-IMVI, PANC-1, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.21×** | +3.5 | 0.018 | 18/48 (LOX-IMVI, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.020 | 16/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lopinavir (drug)]] 5 µM |  | 1.18× | +3.1 | 0.063 | 7/47 (NCI-H2030, LS 180, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.072 | 16/49 (SW480, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.078 | 10/48 (SW1417, LS 180, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.100 | 6/48 (SNU-423, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 1.17× | +2.9 | 0.100 | 6/48 (HT-29, SW 900, …) | top dose only |  |
| [[Gallic acid (drug)]] 0.05 µM |  | 1.17× | +2.9 | 0.100 | 8/48 (COLO 205, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4445.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.324×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.230×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (H4 0.268×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.833× | -4.9 | 6e-04 | 28/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.797×** | -4.2 | 0.009 | 23/47 (NCI-H23, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.892× | -3.1 | 0.26 | 9/48 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.799× | -3.0 | 0.26 | 12/48 (NCI-H23, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 62.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 54.6 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.324× (z -11.1) |
| [[A-172 (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 52.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 38.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.268× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 58.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 77.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.66 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[MTMR6]] | +0.64 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[ZNF664]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[OCRL]] | +0.63 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[LIN7C]] | +0.63 | +0.36 / +0.76 | both halves | 9e-05 |  |
| [[MRS2]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.62 | +0.39 / +0.71 | both halves | 5e-05 | STRING 476 |
| [[DCTN1]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[PRELID3B]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[SGPL1]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ANKRD52]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNJ14]] | -0.64 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[ZNF335]] | -0.64 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[ARMC5]] | -0.61 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[UXT]] | -0.59 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[AK6]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.58 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[EMC6]] | -0.58 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[RBX1]] | -0.57 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[MTRFR]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ECSIT]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[HMGXB4]] | -0.56 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[SYCE2]] | -0.56 | -0.42 / -0.63 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRX5]] | B | IRX5 activity raises FAM199X's level | lines that do not express IRX5 (6) vs lines expressing it (44) | 1.29× lower at baseline in the lines without IRX5 | 0.095 | ⚠ within organs, on part of the lines; also absent: ADGRB2, HOXC8, HOXC4 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHACTR4]] | C | FAM199X's natural level strengthens PHACTR4's drug response | FAM199X's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.15; direction not clear | 0.058 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.4, -19.8); signed map (-16.1, -38.2). **Vector** length 101, 23.7% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +9.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.4 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.2 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Lopinavir (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.5 | +2.7 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.5 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +2.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.4 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -1.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.0 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 199, X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.2 — chrX:104,166,453-104,195,902 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CXorf39 |
| Matched by | ensembl_id |

UniProt [Q6PEV8](https://www.uniprot.org/uniprotkb/Q6PEV8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25195) · Entrez [139231](https://www.ncbi.nlm.nih.gov/gene/139231) · UniProt [Q6PEV8](https://www.uniprot.org/uniprotkb/Q6PEV8) · Ensembl [ENSG00000123575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123575)

## Data

Gene col 4445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4445); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4445]; `tensor/DDL_lfc|DDL_z.npy` [4445]; `embed/gene_vectors.npy` [4445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4445 or target_col == 4445). Every well: [[FAM199X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM199X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
