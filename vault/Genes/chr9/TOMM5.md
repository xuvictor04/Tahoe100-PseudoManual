---
symbol: "TOMM5"
type: "gene"
col: 10646
ensembl_id: "ENSG00000175768"
name: "translocase of outer mitochondrial membrane 5"
location: "9p13.2"
module: 54
arm: "+"
pooled_cpm: 43.73
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TOMM5

*translocase of outer mitochondrial membrane 5* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +7.8, q 5e-12, up in 43 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.64× (z +3.5, q 0.033, up in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1792 6.30×, NCI-H460 5.34×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.662× (z -4.1, q 0.020, down in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.0946×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.278×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.228×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCRH]] (+0.71, fdr 7e-06), [[SNRPD2]] (+0.71, fdr 7e-06), [[TMEM120B]] (+0.70, fdr 7e-06); moves opposite to [[CGGBP1]] (-0.71, fdr 1e-05), [[SCRN1]] (-0.70, fdr 1e-05), [[BMI1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CUZD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10646.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1792 6.30×, NCI-H460 5.34×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.98×** | +7.8 | 5e-12 | 43/46 (NCI-H1792, NCI-H460, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +5.9 | 1e-06 | 43/46 (Hs 766T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.26×** | +5.6 | 5e-06 | 30/41 (HOP62, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.28×** | +5.4 | 9e-06 | 38/44 (SNU-423, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.97×** | +4.8 | 2e-04 | 38/47 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.93×** | +4.5 | 7e-04 | 38/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.86×** | +4.4 | 8e-04 | 39/47 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.033 | 35/48 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.53× | +3.0 | 0.15 | 29/47 (A-427, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10646.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.0946×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.278×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.228×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.662×** | -4.1 | 0.020 | 30/47 (SNU-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.632× | -3.0 | 0.68 | 30/48 (NCI-H23, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0946× (z -11.4) |
| [[AN3 CA (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0797× (z -8.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H1792 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H460 (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[RKO (line)]] | wt | 53.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 | STRING 413 |
| [[SNRPD2]] | +0.71 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[RPL22L1]] ⚠ | +0.69 | +0.58 / +0.71 | both halves | 7e-06 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[SNU13]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SHQ1]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[COG5]] | +0.65 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[WRN]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[IQCB1]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SDF2L1]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[COX6C]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ISOC2]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.71 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[SCRN1]] | -0.70 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[BMI1]] | -0.69 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[ZNF436]] | -0.68 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.68 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[DDX6]] | -0.67 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[RIMOC1]] | -0.66 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[NCOA4]] | -0.65 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | -0.64 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PDCL3P4]] | -0.64 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[TUG1]] | -0.64 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.64 | -0.68 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CUZD1]] | B | CUZD1 activity raises TOMM5's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without CUZD1 | 0.045 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.0, 2.1); signed map (-55.0, -2.8). **Vector** length 76.7, 27.7% of its response variance represented; |z| ≥ 3 in 628 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.52 to 9); *Mitochondrial translation* (reactome, mean cos +0.52 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | translocase of outer mitochondrial membrane 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:37,582,646-37,592,604 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA613M10.3, Tom5; previously C9orf105 |
| Gene groups (HGNC) | Translocase of outer mitochondrial membrane complex |
| Reactome | 7 pathways, smallest: PINK1-PRKN Mediated Mitophagy; Mitophagy; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4H5](https://www.uniprot.org/uniprotkb/Q8N4H5) (Mitochondrial import receptor subunit TOM5 homolog):

> Component of the translocase of the outer membrane of mitochondria (TOM) complex essential for the recognition and translocation of cytosolically synthesized mitochondrial preproteins. The TOM complex associates with the ion channel VDAC2 and PINK1 kinase at depolarized mitochondria, this interaction stabilizes PINK1 at the outer mitochondrial membrane and triggers downstream mitophagy by the recruitment of the E3 ubiquitin ligase PRKN.

**Summary**, from NCBI Gene [401505](https://www.ncbi.nlm.nih.gov/gene/401505):

> Predicted to be involved in obsolete protein targeting to mitochondrion and protein insertion into mitochondrial outer membrane. Located in mitochondrion. Part of mitochondrial outer membrane translocase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31369) · Entrez [401505](https://www.ncbi.nlm.nih.gov/gene/401505) · UniProt [Q8N4H5](https://www.uniprot.org/uniprotkb/Q8N4H5) · Ensembl [ENSG00000175768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175768)

## Data

Gene col 10646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10646); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10646]; `tensor/DDL_lfc|DDL_z.npy` [10646]; `embed/gene_vectors.npy` [10646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10646 or target_col == 10646). Every well: [[TOMM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOMM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
