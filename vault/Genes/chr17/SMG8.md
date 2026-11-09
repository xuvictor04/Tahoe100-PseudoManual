---
symbol: "SMG8"
type: "gene"
col: 9466
ensembl_id: "ENSG00000167447"
name: "SMG8 nonsense mediated mRNA decay factor"
location: "17q22"
module: 7
arm: "+"
pooled_cpm: 8.7
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SMG8

*SMG8 nonsense mediated mRNA decay factor* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.76× (z +10.9, q 6e-25, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.650× (z -5.9, q 3e-06, down in 19 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.768× (z -5.1, q 1e-04, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.190×, SNU-423 0.108×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 0.272×, PANC-1 0.197×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0676×; ⚠ toxic); [[Irinotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0618×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SHP-77 0.0750×); [[Resveratrol (drug)]] 0.5 µM in 1 line (SHP-77 0.0923×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB6]] (+0.83, fdr 7e-06), [[GTF3C4]] (+0.79, fdr 7e-06), [[CBLL1]] (+0.78, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9466.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +10.9 | 6e-25 | 35/47 (CFPAC-1, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +10.5 | 3e-23 | 29/37 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.00×** | +9.4 | 8e-19 | 38/46 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +9.3 | 2e-18 | 29/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.23×** | +8.3 | 9e-15 | 33/46 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +8.0 | 2e-13 | 28/45 (BT-474, SW480, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.6 | 2e-12 | 22/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +7.5 | 5e-12 | 27/46 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +7.0 | 2e-10 | 23/42 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +6.7 | 9e-10 | 4/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +6.4 | 1e-08 | 18/43 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.6 | 1e-06 | 17/38 (A549, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +5.0 | 3e-05 | 12/45 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.8 | 7e-05 | 10/47 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +4.8 | 7e-05 | 13/43 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.4 | 4e-04 | 19/46 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.022 | 9/44 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.023 | 15/43 (PANC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9466.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.190×, SNU-423 0.108×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 0.272×, PANC-1 0.197×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0676×; ⚠ toxic); [[Irinotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0618×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SHP-77 0.0750×); [[Resveratrol (drug)]] 0.5 µM in 1 line (SHP-77 0.0923×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.650×** | -5.9 | 3e-06 | 19/32 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.768×** | -5.1 | 1e-04 | 16/47 (SW480, HOP62, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.736×** | -4.0 | 0.011 | 13/44 (A-172, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.735×** | -3.9 | 0.015 | 12/22 (HEC-1-A, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -3.6 | 0.037 | 9/16 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.772×** | -3.4 | 0.065 | 15/40 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Baicalin (drug)]] 5 µM |  | 0.851× | -3.1 | 0.15 | 4/48 (HEC-1-A, BT-474, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 7.06 | 0 | 3 | — | [[Roxadustat (drug)]] 0.05 µM 0.0750× (z -9.5) |
| [[A498 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 8.99 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0618× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 4.37 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0850× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 5.49 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0676× (z -10.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 6.22 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.157× (z -8.5) |
| [[PANC-1 (line)]] | alt | 4.55 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 10.00 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -10.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 6.71 | 0 | 1 | — | [[Indacaterol (maleate) (drug)]] 0.5 µM 0.0559× (z -8.8) |
| [[SW480 (line)]] | alt | 9.21 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB6]] | +0.83 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[GTF3C4]] | +0.79 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.78 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.77 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.75 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[ZNF646]] | +0.74 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[MRM3]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[CHD8]] | +0.73 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.73 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[TSSC4]] | +0.72 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CHTF8]] | +0.71 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZNF304]] | +0.71 | +0.68 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SMG8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PGAP4]] | B | PGAP4 activity raises SMG8's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.01× lower at baseline in the lines without PGAP4 | 0.096 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.869). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.4, 10.6); signed map (-1.7, -26.3). **Vector** length 74.5, 12.5% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.7 | +10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +9.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +8.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.3 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SMG8 nonsense mediated mRNA decay factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:59,209,400-59,215,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10587, FLJ23205; previously C17orf71 |
| Gene groups (HGNC) | SMG1 complex |
| Reactome | 3 pathways, smallest: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD); Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8ND04](https://www.uniprot.org/uniprotkb/Q8ND04) (Nonsense-mediated mRNA decay factor SMG8):

> Involved in nonsense-mediated decay (NMD) of mRNAs containing premature stop codons. Is recruited by release factors to stalled ribosomes together with SMG1 and SMG9 (forming the SMG1C protein kinase complex) and, in the SMG1C complex, is required to mediate the recruitment of SMG1 to the ribosome:SURF complex and to suppress SMG1 kinase activity until the ribosome:SURF complex locates the exon junction complex (EJC). Acts as a regulator of kinase activity.

**Summary**, from NCBI Gene [55181](https://www.ncbi.nlm.nih.gov/gene/55181):

> Involved in nuclear-transcribed mRNA catabolic process, nonsense-mediated decay and regulation of protein kinase activity. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25551) · Entrez [55181](https://www.ncbi.nlm.nih.gov/gene/55181) · UniProt [Q8ND04](https://www.uniprot.org/uniprotkb/Q8ND04) · Ensembl [ENSG00000167447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167447)

## Data

Gene col 9466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9466); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9466]; `tensor/DDL_lfc|DDL_z.npy` [9466]; `embed/gene_vectors.npy` [9466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9466 or target_col == 9466). Every well: [[SMG8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
