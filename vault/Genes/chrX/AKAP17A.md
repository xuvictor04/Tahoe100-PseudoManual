---
symbol: "AKAP17A"
type: "gene"
col: 12503
ensembl_id: "ENSG00000197976"
name: "A-kinase anchoring protein 17A"
location: "Xp22.33 and Yp11.32"
module: 41
arm: "+"
pooled_cpm: 44.32
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# AKAP17A

*A-kinase anchoring protein 17A* — Xp22.33 and Yp11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +8.6, q 5e-15, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.669× (z -5.0, q 4e-04, down in 25 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 0.120×, KATO III 0.134×, LS 180 0.107×, H4 0.183×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.177×, Panc 03.27 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.199×, SK-MEL-2 0.318×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD3]] (+0.76, fdr 7e-06), [[DNAJC25]] (+0.75, fdr 7e-06), [[SPTY2D1]] (+0.75, fdr 7e-06); moves opposite to [[VMA21]] (-0.65, fdr 7e-06), [[IDH3A]] (-0.63, fdr 2e-05), [[G3BP1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF550]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +8.6 | 5e-15 | 41/48 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +8.2 | 8e-14 | 40/48 (BT-474, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.70×** | +6.6 | 6e-09 | 42/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +6.0 | 3e-07 | 33/47 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +5.4 | 9e-06 | 28/47 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.3 | 1e-05 | 28/46 (SW480, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.31×** | +4.9 | 9e-05 | 25/47 (NCI-H460, NCI-H1573, …) | two highest doses | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.4 | 0.045 | 21/44 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.049 | 22/48 (LoVo, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | 1.27× | +3.0 | 0.13 | 18/47 (LOX-IMVI, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12503.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 0.120×, KATO III 0.134×, LS 180 0.107×, H4 0.183×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.177×, Panc 03.27 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.199×, SK-MEL-2 0.318×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -5.0 | 4e-04 | 25/40 (SNU-423, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.755×** | -3.6 | 0.084 | 26/46 (SNU-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.773× | -3.3 | 0.17 | 23/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.786× | -3.1 | 0.27 | 17/48 (SW 1088, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.4 | 11 (9 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.39× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +12.4) | — |
| [[A549 (line)]] | wt | 41.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 37.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.04× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 61.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.36× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 41.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -15.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.04× (z +10.9) | — |
| [[A-172 (line)]] | wt | 61.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.90× (z +9.4) | — |
| [[A-427 (line)]] | wt | 36.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.93× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 40.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.37× (z +11.0) | — |
| [[H4 (line)]] | wt | 72.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -14.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 46.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD3]] | +0.76 | +0.72 / +0.79 | both halves | 7e-06 | same gene group |
| [[DNAJC25]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[SRP54]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[ZNF622]] | +0.71 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SSR2]] | +0.71 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[GOLGA5]] | +0.70 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[PGM3]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.70 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[YIPF5]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.65 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[IDH3A]] | -0.63 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[G3BP1]] | -0.59 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[GNG12]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF550]] | B | ZNF550 activity lowers AKAP17A's level | lines that do not express ZNF550 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without ZNF550 | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF551, ZNF264, KLHL3 |
| [[INTS4P1]] | B | INTS4P1 activity raises AKAP17A's level | lines that do not express INTS4P1 (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without INTS4P1 | 0.0996 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.4, -36.5); signed map (-50.3, 13.5). **Vector** length 109, 30.6% of its response variance represented; |z| ≥ 3 in 708 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.53 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +5.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | +3.1 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +2.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.5 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.1 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -3.7 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -3.7 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.7 | +0.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -2.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.5 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.2 | -2.8 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Adenine (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 17A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 and Yp11.32 — chrX:1,591,604-1,602,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XE7, XE7Y, DXYS155E, MGC39904, 721P, CCDC133; previously CXYorf3, SFRS17A |
| Gene groups (HGNC) | A-kinase anchoring proteins; Pseudoautosomal region 1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02040](https://www.uniprot.org/uniprotkb/Q02040) (A-kinase anchor protein 17A):

> Splice factor regulating alternative splice site selection for certain mRNA precursors. Mediates regulation of pre-mRNA splicing in a PKA-dependent manner.

**Summary**, from NCBI Gene [8227](https://www.ncbi.nlm.nih.gov/gene/8227):

> This locus encodes a protein kinase A anchoring protein. The encoded protein is part of the spliceosome complex and is involved in the regulation of alternate splicing in some mRNA precursors. Alternatively spliced transcript variants have been identified for this gene.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:18783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18783) · Entrez [8227](https://www.ncbi.nlm.nih.gov/gene/8227) · UniProt [Q02040](https://www.uniprot.org/uniprotkb/Q02040) · Ensembl [ENSG00000197976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197976)

## Data

Gene col 12503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12503); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12503]; `tensor/DDL_lfc|DDL_z.npy` [12503]; `embed/gene_vectors.npy` [12503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12503 or target_col == 12503). Every well: [[AKAP17A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP17A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
