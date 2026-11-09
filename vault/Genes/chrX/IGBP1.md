---
symbol: "IGBP1"
type: "gene"
col: 1583
ensembl_id: "ENSG00000089289"
name: "immunoglobulin binding protein 1"
location: "Xq13.1"
module: 118
arm: "+"
pooled_cpm: 85.16
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# IGBP1

*immunoglobulin binding protein 1* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.31× (z +7.3, q 2e-10, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.765× (z -5.9, q 2e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR83OS]] (+0.71, fdr 7e-06, ⚠ WDR83OS in the vector space only through flagged drug-doses), [[CWC15]] (+0.70, fdr 7e-06), [[UXT]] (+0.69, fdr 2e-05), [[NGDN]] (+0.69, fdr 7e-06); moves opposite to [[IDH3A]] (-0.66, fdr 7e-06), [[EFR3A]] (-0.65, fdr 1e-05), [[VMA21]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.31×** | +7.3 | 2e-10 | 39/49 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +5.5 | 9e-06 | 35/48 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.2 | 4e-05 | 34/48 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.0 | 7e-05 | 30/47 (SW 900, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +4.7 | 3e-04 | 28/48 (HOP62, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.005 | 27/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.9 | 0.008 | 32/45 (A498, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.092 | 23/47 (A498, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.12 | 20/48 (SHP-77, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.12 | 17/48 (A498, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.765×** | -5.9 | 2e-06 | 31/48 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.723×** | -5.1 | 9e-05 | 25/43 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.754×** | -4.6 | 7e-04 | 32/48 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.748×** | -4.6 | 7e-04 | 29/48 (AN3 CA, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **0.791×** | -3.8 | 0.014 | 26/49 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -3.7 | 0.019 | 20/48 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **0.807×** | -3.2 | 0.088 | 21/45 (NCI-H23, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.809×** | -3.2 | 0.088 | 15/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.822×** | -3.2 | 0.088 | 23/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.830× | -3.0 | 0.13 | 22/48 (PANC-1, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 70.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.555× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 77.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.16× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 99.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[SNU-423 (line)]] | alt | 170 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -15.2) |
| [[A498 (line)]] | wt | 74.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -10.2) |
| [[AN3 CA (line)]] | alt | 71.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -12.1) |
| [[C32 (line)]] | wt | 67.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -8.8) |
| [[CHP-212 (line)]] | wt | 74.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -8.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 77.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -8.5) |
| [[HOP62 (line)]] | alt | 84.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[PANC-1 (line)]] | alt | 80.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.482× (z -8.8) |
| [[SW48 (line)]] | wt | 82.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[A-172 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 97.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 119 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 75.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR83OS]] ⚠ | +0.71 | +0.59 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CWC15]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[UXT]] | +0.69 | +0.48 / +0.79 | both halves | 2e-05 |  |
| [[NGDN]] | +0.69 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[TRAPPC2B]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[KLHL20]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[KIAA1143]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[NSA2]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CHCHD5]] | +0.66 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[RPS27]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[MTF1]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.65 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[SYF2]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH3A]] | -0.66 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[EFR3A]] | -0.65 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[VMA21]] | -0.65 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[AKAP11]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[LMNB2]] | -0.61 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[NUP188]] | -0.61 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[ELK4]] | -0.60 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[FH]] | -0.60 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[CBX5]] | -0.60 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[DNMT1]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TEX261]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers IGBP1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.5, -10.6); signed map (-6.6, -6.5). **Vector** length 127, 38.9% of its response variance represented; |z| ≥ 3 in 695 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.3 | +7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.8 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | -6.8 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | -5.7 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.2 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:70,133,447-70,166,324 (+) |
| Ensembl biotype | protein_coding |
| Also known as | α4; previously IBP1 |
| Gene groups (HGNC) | Protein phosphatase 2 modulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [P78318](https://www.uniprot.org/uniprotkb/P78318) (Immunoglobulin-binding protein 1):

> Associated to surface IgM-receptor; may be involved in signal transduction. Involved in regulation of the catalytic activity of the phosphatases PP2A, PP4 and PP6 by protecting their partially folded catalytic subunits from degradative polyubiquitination until they associate with regulatory subunits.

**Summary**, from NCBI Gene [3476](https://www.ncbi.nlm.nih.gov/gene/3476):

> The proliferation and differentiation of B cells is dependent upon a B-cell antigen receptor (BCR) complex. Binding of antigens to specific B-cell receptors results in a tyrosine phosphorylation reaction through the BCR complex and leads to multiple signal transduction pathways. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5461) · Entrez [3476](https://www.ncbi.nlm.nih.gov/gene/3476) · UniProt [P78318](https://www.uniprot.org/uniprotkb/P78318) · Ensembl [ENSG00000089289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089289)

## Data

Gene col 1583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1583); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1583]; `tensor/DDL_lfc|DDL_z.npy` [1583]; `embed/gene_vectors.npy` [1583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1583 or target_col == 1583). Every well: [[IGBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
