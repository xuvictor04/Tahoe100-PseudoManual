---
symbol: "ORAI1"
type: "gene"
col: 15866
ensembl_id: "ENSG00000276045"
name: "ORAI calcium release-activated calcium modulator 1"
location: "12q24.31"
module: 29
arm: "-"
pooled_cpm: 4.79
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ORAI1

*ORAI calcium release-activated calcium modulator 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (18 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.76× (z +9.6, q 2e-19, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +9.6, q 2e-19, up in 25 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.322× (z -5.2, q 1e-04, down in 21 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0589×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H460 0.130×); [[Thymol (drug)]] 0.5 µM in 1 line (SHP-77 0.105×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA2L]] (+0.61, fdr 7e-05), [[TRAPPC4]] (+0.60, fdr 4e-05), [[ERVK3-1]] (+0.60, fdr 7e-06); moves opposite to [[CSDE1]] (-0.68, fdr 1e-05), [[MORF4L1]] (-0.64, fdr 1e-05), [[SMU1]] (-0.61, fdr 5e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ALDH3B1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.76×** | +9.6 | 2e-19 | 41/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +9.6 | 2e-19 | 25/40 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.67×** | +9.4 | 2e-18 | 38/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.31×** | +8.0 | 2e-13 | 36/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.06×** | +6.8 | 8e-10 | 23/36 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.62×** | +6.5 | 7e-09 | 22/40 (A549, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.87×** | +5.7 | 8e-07 | 24/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +5.1 | 3e-05 | 22/39 (A-172, C-33 A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.68×** | +4.7 | 1e-04 | 15/29 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.62×** | +4.4 | 7e-04 | 12/30 (A549, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.57×** | +4.3 | 9e-04 | 15/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.78×** | +3.9 | 0.004 | 6/29 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.004 | 12/46 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.49×** | +3.7 | 0.007 | 13/27 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.48×** | +3.7 | 0.008 | 10/43 (LOX-IMVI, SW 900, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.71×** | +3.7 | 0.009 | 4/37 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.012 | 14/37 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.017 | 9/46 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.046 | 5/37 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.061 | 8/46 (SNU-423, LoVo, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +2.9 | 0.078 | 4/34 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fluvoxamine (drug)]] 5 µM |  | **1.37×** | +2.8 | 0.090 | 6/42 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15866.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0589×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H460 0.130×); [[Thymol (drug)]] 0.5 µM in 1 line (SHP-77 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.322×** | -5.2 | 1e-04 | 21/42 (RKO, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -4.0 | 0.018 | 16/37 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.698× | -3.1 | 0.35 | 7/46 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 7.12 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0589× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 3.62 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.130× (z -9.3) |
| [[SHP-77 (line)]] | alt | 7.69 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[A-172 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA2L]] | +0.61 | +0.37 / +0.66 | both halves | 7e-05 |  |
| [[TRAPPC4]] | +0.60 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ERVK3-1]] | +0.60 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[HES6]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[FBXL6]] | +0.59 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[MAP1S]] | +0.59 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[PPP1R35]] ⚠ | +0.58 | +0.33 / +0.64 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL36]] | +0.58 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[BCAR1]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ZNF593]] | +0.57 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[CCNQ]] | +0.56 | +0.40 / +0.59 | both halves | 4e-05 |  |
| [[RNF166]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[EXOSC4]] | +0.56 | +0.29 / +0.69 | both halves | 3e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | -0.68 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[MORF4L1]] | -0.64 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[SMU1]] | -0.61 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[PAPOLA]] | -0.61 | -0.34 / -0.67 | both halves | 1e-04 |  |
| [[RTF2]] | -0.59 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[EIF3F]] | -0.57 | -0.32 / -0.63 | both halves | 2e-04 |  |
| [[PCBP2]] | -0.57 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[SELENOF]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[UBQLN1]] | -0.56 | -0.38 / -0.64 | both halves | 7e-05 |  |
| [[SH3BGRL]] | -0.56 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[SDHD]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CANX]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH3B1]] | B | ALDH3B1 activity lowers ORAI1's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 1.43× higher at baseline in the lines without ALDH3B1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ORAI1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANXA1]] | B | ANXA1 activity lowers ORAI1's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.40× higher at baseline in the lines without ANXA1 | 0.049 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[MYOF]] | B | MYOF activity lowers ORAI1's level | lines that do not express MYOF (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without MYOF | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-32.7, -23.9); signed map (-0.8, -8.4). **Vector** length 51.6, 7.09% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.6 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +2.6 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.0 | +3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | +1.7 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[vincristine (drug)]] 5 µM |  | +1.1 | +1.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.5 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ORAI calcium release-activated calcium modulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,626,509-121,643,218 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14466, CRACM1; previously TMEM142A |
| Gene groups (HGNC) | ORAI calcium release-activated calcium modulators |
| Reactome | 10 pathways, smallest: Elevation of cytosolic Ca2+ levels; Platelet calcium homeostasis; Antigen activates B Cell Receptor (BCR) leading to generation of second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D31](https://www.uniprot.org/uniprotkb/Q96D31) (Calcium release-activated calcium channel protein 1):

> Pore-forming subunit of two major inward rectifying Ca(2+) channels at the plasma membrane: Ca(2+) release-activated Ca(2+) (CRAC) channels and arachidonate-regulated Ca(2+)-selective (ARC) channels (Probable). Assembles with ORAI2 and ORAI3 to form hexameric CRAC channels that mediate Ca(2+) influx upon depletion of endoplasmic reticulum Ca(2+) store and channel activation by Ca(2+) sensor STIM1, a process known as store-operated Ca(2+) entry (SOCE). Various pore subunit combinations may …

**Summary**, from NCBI Gene [84876](https://www.ncbi.nlm.nih.gov/gene/84876):

> The protein encoded by this gene is a membrane calcium channel subunit that is activated by the calcium sensor STIM1 when calcium stores are depleted. This type of channel is the primary way for calcium influx into T-cells. Defects in this gene are a cause of immune dysfunction with T-cell inactivation due to calcium entry defect type 1 (IDTICED1). [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:25896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25896) · Entrez [84876](https://www.ncbi.nlm.nih.gov/gene/84876) · UniProt [Q96D31](https://www.uniprot.org/uniprotkb/Q96D31) · Ensembl [ENSG00000276045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276045)

## Data

Gene col 15866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15866); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15866]; `tensor/DDL_lfc|DDL_z.npy` [15866]; `embed/gene_vectors.npy` [15866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15866 or target_col == 15866). Every well: [[ORAI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORAI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
