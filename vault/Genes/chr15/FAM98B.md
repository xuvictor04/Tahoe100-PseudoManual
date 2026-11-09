---
symbol: "FAM98B"
type: "gene"
col: 10082
ensembl_id: "ENSG00000171262"
name: "tRNA splicing ligase complex subunit 3B"
location: "15q14"
module: 4
arm: "+"
pooled_cpm: 27.59
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# FAM98B

*tRNA splicing ligase complex subunit 3B* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.59× (z +12.1, q 8e-31, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.740× (z -7.7, q 8e-12, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-1 0.338×, NCI-H23 0.427×, NCI-H2030 0.485×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.190×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.101×); [[Capmatinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0742×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX9]] (+0.77, fdr 7e-06), [[MRPL42]] (+0.74, fdr 7e-06), [[DLD]] (+0.71, fdr 7e-06); moves opposite to [[FAM177A1]] (-0.66, fdr 7e-06), [[INAFM1]] (-0.63, fdr 7e-06), [[PHKG1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARHGDIB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10082.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.59×** | +12.1 | 8e-31 | 44/48 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +9.4 | 1e-18 | 38/47 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +8.6 | 1e-15 | 35/47 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +7.3 | 3e-11 | 35/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.31×** | +6.9 | 8e-10 | 25/48 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.38×** | +5.8 | 5e-07 | 26/48 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.43×** | +5.8 | 5e-07 | 22/42 (KATO III, SW480, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +5.1 | 2e-05 | 22/47 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.8 | 1e-04 | 20/48 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.30×** | +4.8 | 1e-04 | 23/47 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.7 | 1e-04 | 20/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +4.5 | 3e-04 | 20/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.30×** | +4.5 | 3e-04 | 18/38 (SW480, Hs 766T, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +3.8 | 0.006 | 14/47 (NCI-H460, H4, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.23×** | +3.7 | 0.009 | 21/45 (MIA PaCa-2, A549, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.010 | 14/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.061 | 6/47 (NCI-H2030, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10082.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-1 0.338×, NCI-H23 0.427×, NCI-H2030 0.485×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.190×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.101×); [[Capmatinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0742×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -7.7 | 8e-12 | 32/48 (SNU-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -5.3 | 3e-05 | 3/48 (CHP-212, NCI-H661, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.776× | -3.3 | 0.15 | 15/48 (LS 180, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.777× | -3.3 | 0.15 | 18/46 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.0 | 0.25 | 17/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.793× | -3.0 | 0.25 | 11/48 (SW480, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10082. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 32.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.81× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.101× (z -10.6) |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.235× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0742× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.7) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H2030 (line)]] | alt | 57.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.9) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SNU-1 (line)]] | wt | 52.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.6) |
| [[SW48 (line)]] | wt | 35.3 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 5.46× (z +9.6) | — |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10082), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX9]] | +0.77 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[MRPL42]] | +0.74 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[DLD]] | +0.71 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[IPO8]] | +0.71 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[CSTF2]] | +0.70 | +0.70 / +0.68 | both halves | 7e-06 | pathway: tRNA processing |
| [[AGPS]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[PPP5C]] | +0.69 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[MTMR2]] | +0.69 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[MRPL19]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[DLAT]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ZDHHC21]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[ALKBH8]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | pathway: tRNA processing |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM177A1]] | -0.66 | -0.59 / -0.71 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.63 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[PHKG1]] | -0.63 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.63 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[CATSPERG]] | -0.62 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[STX5]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[TOB2]] | -0.60 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[HIC2]] | -0.60 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[RAB5A]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | -0.60 | -0.54 / -0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM106A]] | -0.59 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.59 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.58 | -0.45 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGDIB]] | B | ARHGDIB activity lowers FAM98B's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.27× higher at baseline in the lines without ARHGDIB | 0.051 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.6, -34.9); signed map (-16.2, -44.3). **Vector** length 87.9, 18.6% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.54 to 15); *mRNA Polyadenylation* (reactome, mean cos +0.54 to 10); *Folding of actin by CCT/TriC* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.9 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.6 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | +4.3 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -3.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | tRNA splicing ligase complex subunit 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:38,454,127-38,487,710 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38426; previously FAM98B |
| Gene groups (HGNC) | tRNA splicing ligase complex |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q52LJ0](https://www.uniprot.org/uniprotkb/Q52LJ0) (tRNA splicing ligase complex subunit 3B):

> Accessory subunit of the tRNA-splicing ligase complex that acts by directly joining spliced tRNA halves to mature-sized tRNAs by incorporating the precursor-derived splice junction phosphate into the mature tRNA as a canonical 3',5'-phosphodiester. May act as an RNA ligase with broad substrate specificity and may function toward other RNAs. Could regulate the expression of PRMT1, a protein arginine N-methyltransferase.

**Summary**, from NCBI Gene [283742](https://www.ncbi.nlm.nih.gov/gene/283742):

> Enables identical protein binding activity and protein methyltransferase activity. Involved in positive regulation of cell population proliferation; positive regulation of gene expression; and protein methylation. Located in cytoplasm and nucleoplasm. Part of tRNA-splicing ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26773) · Entrez [283742](https://www.ncbi.nlm.nih.gov/gene/283742) · UniProt [Q52LJ0](https://www.uniprot.org/uniprotkb/Q52LJ0) · Ensembl [ENSG00000171262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171262)

## Data

Gene col 10082: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10082); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10082, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10082]; `tensor/DDL_lfc|DDL_z.npy` [10082]; `embed/gene_vectors.npy` [10082]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10082 or target_col == 10082). Every well: [[FAM98B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM98B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
