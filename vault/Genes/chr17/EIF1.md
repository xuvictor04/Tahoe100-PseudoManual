---
symbol: "EIF1"
type: "gene"
col: 10429
ensembl_id: "ENSG00000173812"
name: "eukaryotic translation initiation factor 1"
location: "17q21.2"
module: 20
arm: "-"
pooled_cpm: 620.12
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EIF1

*eukaryotic translation initiation factor 1* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.02× (z +6.0, q 1e-06, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.75× (z +4.8, q 2e-04, up in 47 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (AsPC-1 3.64×, COLO 205 3.19×, C32 3.34×, NCI-H1573 2.79×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (NCI-H1573 4.05×, NCI-H460 3.87×, AsPC-1 2.99×, COLO 205 3.71×; ⚠ cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 4.29×, SHP-77 3.46×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 3.36×).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.596× (z -4.4, q 0.005, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF1B]] (+0.80, fdr 7e-06), [[SNHG8]] (+0.73, fdr 7e-06), [[ATF4]] (+0.73, fdr 7e-06); moves opposite to [[NUP155]] (-0.71, fdr 7e-06), [[SLC25A10]] (-0.66, fdr 1e-05), [[NCBP1]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10429.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (AsPC-1 3.64×, COLO 205 3.19×, C32 3.34×, NCI-H1573 2.79×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (NCI-H1573 4.05×, NCI-H460 3.87×, AsPC-1 2.99×, COLO 205 3.71×; ⚠ cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 4.29×, SHP-77 3.46×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 3.36×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +6.0 | 1e-06 | 48/48 (NCI-H1573, SNU-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.93×** | +5.6 | 5e-06 | 48/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +5.4 | 1e-05 | 40/44 (C-33 A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +4.8 | 2e-04 | 47/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +4.4 | 0.001 | 47/49 (C-33 A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.64×** | +4.3 | 0.002 | 39/48 (C32, AsPC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.59×** | +4.0 | 0.006 | 44/48 (SW 900, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.9 | 0.007 | 34/48 (AsPC-1, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.007 | 40/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Adagrasib (drug)]] 5 µM |  | 1.45× | +3.1 | 0.12 | 45/48 (A498, CHP-212, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.44× | +3.0 | 0.13 | 35/47 (HepG2/C3A, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10429.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.596×** | -4.4 | 0.005 | 43/48 (hTERT-HPNE, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.608×** | -4.3 | 0.006 | 40/48 (hTERT-HPNE, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -3.7 | 0.047 | 41/49 (H4, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.663×** | -3.5 | 0.061 | 38/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.694× | -3.1 | 0.20 | 39/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.511× | -3.0 | 0.23 | 37/49 (LOX-IMVI, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 585 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +16.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 559 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 634 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +10.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.36× (z +9.1) | — |
| [[C32 (line)]] | wt | 272 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 505 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 517 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.50× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 279 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +10.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 400 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 602 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 263 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 495 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 642 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 605 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 909 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 285 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1,391 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 761 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 668 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 610 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 530 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 390 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 682 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 644 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 555 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 820 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 965 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 829 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 560 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 593 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 619 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1,124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 539 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 850 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 578 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 761 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 582 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 461 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 651 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 661 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 543 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 520 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 423 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 602 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 635 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 497 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 13 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1B]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | STRING 924 |
| [[SNHG8]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[ATF4]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 | STRING 470 |
| [[SNHG12]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.70 | +0.62 / +0.80 | both halves | 7e-06 |  |
| [[ZNNT1]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[NACA4P]] ⚠ | +0.69 | +0.69 / +0.72 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG6]] | +0.68 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[PQBP1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RPS13]] ⚠ | +0.66 | +0.59 / +0.80 | both halves | 7e-06 | STRING 974; ⚠ in the vector space only through flagged drug-doses |
| [[FAU]] | +0.65 | +0.67 / +0.72 | both halves | 7e-06 | STRING 994 |
| [[ZFAS1]] | +0.65 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.64 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[SAT2]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | -0.71 | -0.67 / -0.72 | both halves | 7e-06 |  |
| [[SLC25A10]] | -0.66 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[NCBP1]] | -0.66 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[RPE]] | -0.64 | -0.58 / -0.64 | both halves | 8e-06 |  |
| [[PRKDC]] | -0.64 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[GOT2]] | -0.63 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[CSTF2]] | -0.63 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[PDHA1]] | -0.62 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[DLAT]] | -0.62 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[BANF1]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[PHB1]] | -0.62 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises EIF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NUPR1]] | B | NUPR1 activity lowers EIF1's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.13× higher at baseline in the lines without NUPR1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.2, -29.1); signed map (-14.6, -2.0). **Vector** length 116, 64.8% of its response variance represented; |z| ≥ 3 in 807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.4 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.9 | -0.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.0 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.8 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.1 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | +2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | +4.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,688,885-41,692,668 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EIF-1, ISO1, A121, SUI1, EIF1A |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [P41567](https://www.uniprot.org/uniprotkb/P41567) (Eukaryotic translation initiation factor 1):

> Component of the 43S pre-initiation complex (43S PIC), which binds to the mRNA cap-proximal region, scans mRNA 5'-untranslated region, and locates the initiation codon. Together with eIF1A (EIF1AX), EIF1 facilitates scanning and is essential for start codon recognition on the basis of AUG nucleotide context and location relative to the 5'-cap. Participates to initiation codon selection by influencing the conformation of the 40S ribosomal subunit and the positions of bound mRNA and initiator …

**Summary**, from NCBI Gene [10209](https://www.ncbi.nlm.nih.gov/gene/10209):

> Enables ribosomal small subunit binding activity and translation initiation factor activity. Involved in regulation of translational initiation and translational initiation. Located in cytoplasm and nucleus. Part of eukaryotic 43S preinitiation complex; eukaryotic 48S preinitiation complex; and multi-eIF complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3249) · Entrez [10209](https://www.ncbi.nlm.nih.gov/gene/10209) · UniProt [P41567](https://www.uniprot.org/uniprotkb/P41567) · Ensembl [ENSG00000173812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173812)

## Data

Gene col 10429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10429); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10429]; `tensor/DDL_lfc|DDL_z.npy` [10429]; `embed/gene_vectors.npy` [10429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10429 or target_col == 10429). Every well: [[EIF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
