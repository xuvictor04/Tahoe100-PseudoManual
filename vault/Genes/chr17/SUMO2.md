---
symbol: "SUMO2"
type: "gene"
col: 12031
ensembl_id: "ENSG00000188612"
name: "small ubiquitin like modifier 2"
location: "17q25"
module: 7
arm: "-"
pooled_cpm: 54.8
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SUMO2

*small ubiquitin like modifier 2* — 17q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.30× (z +12.7, q 4e-34, up in 46 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.29× (z +3.4, q 0.027, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 2.73×, A549 4.20×, NCI-H1573 4.49×, NCI-H460 2.99×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Adagrasib (drug)]] 0.05 µM in 4 lines (SW480 1.33×, MIA PaCa-2 1.51×, NCI-H2347 1.31×, HEC-1-A 1.33×; ⚠ position not correctable); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 2.75×, PANC-1 3.40×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0805×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPPL3]] (+0.58, fdr 1e-05), [[PTMS]] (+0.57, fdr 3e-05), [[USP33]] (+0.57, fdr 1e-05); moves opposite to [[ZNF222]] (-0.58, fdr 3e-05), [[KCTD5]] (-0.55, fdr 3e-05), [[PRKAG1]] (-0.55, fdr 2e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BCAN-AS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12031.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 2.73×, A549 4.20×, NCI-H1573 4.49×, NCI-H460 2.99×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Adagrasib (drug)]] 0.05 µM in 4 lines (SW480 1.33×, MIA PaCa-2 1.51×, NCI-H2347 1.31×, HEC-1-A 1.33×; ⚠ position not correctable); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 2.75×, PANC-1 3.40×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.30×** | +12.7 | 4e-34 | 46/49 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +11.5 | 3e-28 | 45/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.24×** | +11.0 | 5e-26 | 35/42 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.29×** | +9.9 | 6e-21 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.85×** | +8.7 | 2e-16 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.71×** | +7.3 | 3e-11 | 39/47 (PANC-1, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.62×** | +6.8 | 8e-10 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.66×** | +6.6 | 3e-09 | 33/45 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.43×** | +5.1 | 2e-05 | 32/48 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.4 | 5e-04 | 35/47 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.71×** | +4.0 | 0.003 | 28/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.31×** | +3.9 | 0.005 | 25/46 (RPMI-7951, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Arbutin (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.027 | 23/48 (NCI-H460, A498, …) | top dose only | position effect removed |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.047 | 12/49 (HOP62, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12031.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0805×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | 0.775× | -3.6 | 0.15 | 23/48 (NCI-H2347, CFPAC-1, …) | top dose only | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.776× | -3.5 | 0.15 | 25/48 (HEC-1-A, RPMI-7951, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.791× | -3.1 | 0.28 | 17/48 (SHP-77, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.806× | -3.1 | 0.28 | 18/48 (KATO III, HOP62, …) | inconsistent across doses |  |
| [[Finasteride (drug)]] 5 µM |  | 0.802× | -3.0 | 0.28 | 14/47 (A549, J82, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 60.2 | 6 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.75× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 46.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 59.7 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.40× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 52.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 61.5 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.37× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 52.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 64.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +10.6) ⚠ position not correctable | — |
| [[NCI-H1573 (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.86× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 56.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0805× (z -8.6) |
| [[A-172 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPPL3]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PTMS]] | +0.57 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[USP33]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[AMBRA1]] | +0.56 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[STK38]] | +0.55 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[H3-3A]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[ELF2]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[BMPR2]] | +0.53 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[TWSG1]] | +0.53 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[CHASERR]] | +0.52 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[TLE5]] | +0.52 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[ILKAP]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF222]] | -0.58 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[KCTD5]] | -0.55 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[PRKAG1]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[DNTTIP2]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[FERMT3]] | -0.53 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[LRIF1]] | -0.53 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[FAM83G]] | -0.53 | -0.52 / -0.49 | both halves | 2e-05 |  |
| [[SAP30BP]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 | pathway: Epigenetic regulation of gene expression |
| [[JMJD6]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[EMG1]] | -0.52 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[GNL2]] | -0.51 | -0.53 / -0.38 | both halves | 6e-05 | STRING 562 |
| [[DNAJA3]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAN-AS2]] | B | BCAN-AS2 activity lowers SUMO2's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 1.17× higher at baseline in the lines without BCAN-AS2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.310). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-13.3, -48.2); signed map (-23.7, -5.4). **Vector** length 63.5, 14.5% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +11.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.8 | +8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.4 | +6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | -0.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.9 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.8 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | +1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | +0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | small ubiquitin like modifier 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25 — chr17:75,165,586-75,182,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMT3B; previously SMT3H2 |
| Gene groups (HGNC) | Small ubiquitin like modifier family |
| Reactome | 28 pathways, smallest: SUMO is conjugated to E1 (UBA2:SAE1); SUMO is proteolytically processed; SUMO is transferred from E1 to E2 (UBE2I, UBC9) |
| Matched by | ensembl_id |

**Function**, from UniProt [P61956](https://www.uniprot.org/uniprotkb/P61956) (Small ubiquitin-related modifier 2):

> Ubiquitin-like protein that can be covalently attached to proteins as a monomer or as a lysine-linked polymer. Covalent attachment via an isopeptide bond to its substrates requires prior activation by the E1 complex SAE1-SAE2 and linkage to the E2 enzyme UBE2I, and can be promoted by an E3 ligase such as PIAS1-4, RANBP2, CBX4 or ZNF451. This post-translational modification on lysine residues of proteins plays a crucial role in a number of cellular processes such as nuclear transport, DNA …

**Summary**, from NCBI Gene [6613](https://www.ncbi.nlm.nih.gov/gene/6613):

> This gene encodes a protein that is a member of the SUMO (small ubiquitin-like modifier) protein family. It functions in a manner similar to ubiquitin in that it is bound to target proteins as part of a post-translational modification system. However, unlike ubiquitin which targets proteins for degradation, this protein is involved in a variety of cellular processes, such as nuclear transport, transcriptional regulation, apoptosis, and protein stability. It is not active until the last two …

**Accessions** — [HGNC:11125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11125) · Entrez [6613](https://www.ncbi.nlm.nih.gov/gene/6613) · UniProt [P61956](https://www.uniprot.org/uniprotkb/P61956) · Ensembl [ENSG00000188612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188612)

## Data

Gene col 12031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12031); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12031]; `tensor/DDL_lfc|DDL_z.npy` [12031]; `embed/gene_vectors.npy` [12031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12031 or target_col == 12031). Every well: [[SUMO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUMO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
