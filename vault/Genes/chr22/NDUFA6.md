---
symbol: "NDUFA6"
type: "gene"
col: 11599
ensembl_id: "ENSG00000184983"
name: "NADH:ubiquinone oxidoreductase subunit A6"
location: "22q13.2"
module: 24
arm: "+"
pooled_cpm: 31.25
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NDUFA6

*NADH:ubiquinone oxidoreductase subunit A6* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.81× (z +8.8, q 6e-16, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +5.4, q 9e-06, up in 36 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.228×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBX1]] (+0.65, fdr 2e-05), [[BLTP3B]] (+0.61, fdr 3e-05), [[FDX2]] (+0.59, fdr 1e-05); moves opposite to [[MAT2A]] (-0.59, fdr 4e-05), [[HNRNPA3]] (-0.56, fdr 4e-05), [[AGO1]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.81×** | +8.8 | 6e-16 | 42/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.31×** | +6.9 | 2e-09 | 31/37 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +5.7 | 3e-06 | 38/45 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.4 | 9e-06 | 36/47 (SK-MEL-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.80×** | +5.0 | 7e-05 | 37/47 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.87×** | +4.9 | 1e-04 | 30/41 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +4.2 | 0.003 | 37/48 (NCI-H1573, HOP62, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.015 | 28/48 (HOP62, NCI-H2030, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.52×** | +3.4 | 0.038 | 25/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.49×** | +3.3 | 0.053 | 23/48 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.49×** | +3.3 | 0.053 | 26/48 (NCI-H1573, NCI-H2030, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.49×** | +3.3 | 0.054 | 27/47 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.063 | 24/48 (HOP62, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11599.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.228×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.396× | -3.4 | 0.36 | 33/48 (SW 900, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.419× | -3.2 | 0.38 | 21/48 (A498, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 74.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.3) | — |
| [[A-172 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBX1]] | +0.65 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[BLTP3B]] | +0.61 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[FDX2]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 | STRING 666 |
| [[NDUFC1]] | +0.59 | +0.42 / +0.62 | both halves | 4e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[PQBP1]] | +0.59 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[COPS9]] | +0.59 | +0.32 / +0.77 | both halves | 2e-04 |  |
| [[ZCCHC10]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CDC37L1]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[FBXL15]] | +0.58 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[LSM8]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[KLHL22]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[MAP2K4]] | +0.57 | +0.30 / +0.52 | both halves | 2e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAT2A]] | -0.59 | -0.43 / -0.72 | both halves | 4e-05 |  |
| [[HNRNPA3]] | -0.56 | -0.41 / -0.70 | both halves | 4e-05 |  |
| [[AGO1]] | -0.54 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[FKBP1A]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[PABIR2]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[BAIAP2-DT]] | -0.52 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[PODXL2]] | -0.51 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[ADAMTSL5]] | -0.51 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ITGB1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[LINC03009]] | -0.51 | -0.37 / -0.59 | both halves | 7e-05 |  |
| [[SNRNP200]] | -0.50 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[APP]] | -0.50 | -0.39 / -0.67 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NDUFA6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.3, -21.8); signed map (-2.6, 1.1). **Vector** length 54.5, 13.6% of its response variance represented; |z| ≥ 3 in 533 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +3.0 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.8 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.6 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.2 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.0 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -2.9 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -0.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,085,526-42,090,884 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B14, LYRM6, CI-B14, NADHB14 |
| Gene groups (HGNC) | LYR motif containing; NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P56556](https://www.uniprot.org/uniprotkb/P56556) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed to be not involved in catalysis. Required for proper complex I assembly. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4700](https://www.ncbi.nlm.nih.gov/gene/4700):

> This gene encodes a member of the LYR family of proteins that contain a highly conserved tripeptide (LYR) motif near the N-terminus. The encoded protein is an accessory subunit of NADH: ubiquinone oxidorerductase (Complex I), which is the largest enzyme of the mitochondrial membrane respiratory chain. Complex I functions in electron transfer from NADH to the respiratory chain. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:7690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7690) · Entrez [4700](https://www.ncbi.nlm.nih.gov/gene/4700) · UniProt [P56556](https://www.uniprot.org/uniprotkb/P56556) · Ensembl [ENSG00000184983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184983)

## Data

Gene col 11599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11599); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11599]; `tensor/DDL_lfc|DDL_z.npy` [11599]; `embed/gene_vectors.npy` [11599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11599 or target_col == 11599). Every well: [[NDUFA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
