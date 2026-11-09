---
symbol: "ADO"
type: "gene"
col: 11225
ensembl_id: "ENSG00000181915"
name: "2-aminoethanethiol dioxygenase"
location: "10q21.3"
module: 16
arm: "+"
pooled_cpm: 7.42
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ADO

*2-aminoethanethiol dioxygenase* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.41× (z +10.8, q 3e-24, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.669× (z -4.9, q 4e-04, down in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.0689×, hTERT-HPNE 0.0715×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.0835×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (SW 900 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX20]] (+0.76, fdr 7e-06), [[DNAAF2]] (+0.74, fdr 7e-06), [[CHAMP1]] (+0.71, fdr 7e-06); moves opposite to [[PIK3C2A]] (-0.61, fdr 7e-06), [[CBFA2T2]] (-0.61, fdr 1e-05), [[KDELR1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DLX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +10.8 | 3e-24 | 32/40 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.30×** | +10.2 | 6e-22 | 36/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +8.8 | 3e-16 | 23/36 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.92×** | +7.7 | 2e-12 | 28/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.45×** | +6.5 | 1e-08 | 21/39 (HOP62, HEC-1-A, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +6.0 | 1e-07 | 24/45 (LS 180, NCI-H460, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.5 | 4e-06 | 12/42 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.56×** | +5.0 | 3e-05 | 16/43 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +5.0 | 4e-05 | 14/45 (SW480, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 12/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.002 | 14/45 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.41×** | +3.9 | 0.005 | 9/21 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.37×** | +3.9 | 0.005 | 9/29 (SW480, HepG2/C3A, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.4 | 0.023 | 9/46 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.32×** | +3.4 | 0.027 | 11/36 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +3.4 | 0.027 | 8/43 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.63×** | +3.1 | 0.060 | 4/35 (NCI-H23, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11225.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.0689×, hTERT-HPNE 0.0715×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.0835×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pemetrexed (drug)]] 5 µM in 1 line (SW 900 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.669×** | -4.9 | 4e-04 | 17/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | 0.754× | -3.2 | 0.36 | 6/45 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.781× | -3.1 | 0.42 | 16/47 (A498, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 6.75 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0689× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 5.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0835× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 5.32 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0715× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 7.22 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.109× (z -8.6) |
| [[A-172 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX20]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[DNAAF2]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[CHAMP1]] | +0.71 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[RRS1]] | +0.70 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[UTP3]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[TRMT5]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.69 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[C7orf25]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[FANCF]] | +0.68 | +0.63 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3C2A]] | -0.61 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.61 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[PHF1]] | -0.61 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[TALAM1]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[RTN3]] | -0.60 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CRELD1]] | -0.60 | -0.57 / -0.58 | both halves | 8e-06 |  |
| [[RAB6A]] | -0.58 | -0.67 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX1]] | B | DLX1 activity raises ADO's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.11× lower at baseline in the lines without DLX1 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.2, 13.8); signed map (3.0, -38.0). **Vector** length 65.0, 10.1% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.8 | +7.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +5.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +3.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | -3.1 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.5 | -3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.3 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.4 | -0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | 2-aminoethanethiol dioxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:62,804,720-62,808,479 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14547; previously C10orf22 |
| Gene groups (HGNC) | Oxygenases |
| Reactome | 3 pathways, smallest: Degradation of cysteine and homocysteine; Sulfur amino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SZ5](https://www.uniprot.org/uniprotkb/Q96SZ5) (2-aminoethanethiol dioxygenase):

> Plays a vital role in regulating thiol metabolism and preserving oxygen homeostasis by oxidizing the sulfur of cysteamine and N-terminal cysteine-containing proteins to their corresponding sulfinic acids using O2 as a cosubstrate. Catalyzes the oxidation of cysteamine (2-aminoethanethiol) to hypotaurine. Catalyzes the oxidation of regulators of G protein signaling 4 (RGS4) and 5 (RGS5) and interleukin-32 (IL32).

**Summary**, from NCBI Gene [84890](https://www.ncbi.nlm.nih.gov/gene/84890):

> Human thiol dioxygenases include cysteine dioxygenase (CDO; MIM 603943) and cysteamine (2-aminoethanethiol) dioxygenase (ADO; EC 1.13.11.19). CDO adds 2 oxygen atoms to free cysteine, whereas ADO adds 2 oxygen atoms to free cysteamine to form hypotaurine (Dominy et al., 2007 [PubMed 17581819]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23506) · Entrez [84890](https://www.ncbi.nlm.nih.gov/gene/84890) · UniProt [Q96SZ5](https://www.uniprot.org/uniprotkb/Q96SZ5) · Ensembl [ENSG00000181915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181915)

## Data

Gene col 11225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11225); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11225]; `tensor/DDL_lfc|DDL_z.npy` [11225]; `embed/gene_vectors.npy` [11225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11225 or target_col == 11225). Every well: [[ADO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
