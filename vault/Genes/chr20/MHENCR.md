---
symbol: "MHENCR"
type: "gene"
col: 13848
ensembl_id: "ENSG00000232442"
name: "melanoma highly expressed competing endogenous lncRNA for miR-425 and miR-489"
location: "20q13.33"
module: 24
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MHENCR

*melanoma highly expressed competing endogenous lncRNA for miR-425 and miR-489* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.97× (z +6.9, q 3e-09, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.65× (z +4.7, q 4e-04, up in 9 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.565× (z -3.8, q 0.077, down in 15 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.195×, A549 0.115×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (A-172 0.0789×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MINCR]] (+0.80, fdr 7e-06), [[SNHG19]] (+0.75, fdr 7e-06), [[MALSU1]] (+0.74, fdr 7e-06); moves opposite to [[PSMC3]] (-0.73, fdr 7e-06), [[MAPRE1]] (-0.65, fdr 3e-05), [[TASOR]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EID2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.97×** | +6.9 | 3e-09 | 2/5 (Hs 766T, HS-578T) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +6.2 | 1e-07 | 2/8 (MIA PaCa-2, SW1417) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +5.3 | 2e-05 | 11/15 (KATO III, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.04×** | +4.7 | 4e-04 | 8/21 (HEC-1-A, PANC-1, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +4.7 | 4e-04 | 9/43 (Hs 766T, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +3.9 | 0.009 | 17/42 (A-172, KATO III, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.8 | 0.012 | 10/24 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +3.7 | 0.012 | 6/19 (A-172, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.7 | 0.012 | 11/31 (A549, KATO III, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.7 | 0.012 | 13/33 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **2.10×** | +3.4 | 0.041 | 9/34 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.071 | 10/32 (KATO III, A-172, …) | two highest doses | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13848.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.195×, A549 0.115×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (A-172 0.0789×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.565×** | -3.8 | 0.077 | 15/33 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.676×** | -3.6 | 0.077 | 18/34 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.595× | -3.2 | 0.23 | 18/39 (A-427, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.50 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0789× (z -8.7) |
| [[A549 (line)]] | wt | 4.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.8) |
| [[A-427 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINCR]] | +0.80 | +0.65 / +0.82 | both halves | 7e-06 | same gene group |
| [[SNHG19]] | +0.75 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.74 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[METRN]] | +0.73 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[B3GAT3]] | +0.73 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[ELP2]] | +0.73 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.72 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.71 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[DPM3]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 | same gene group |
| [[CNOT8]] | +0.69 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[STK32C]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC3]] | -0.73 | -0.67 / -0.71 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.65 | -0.44 / -0.73 | both halves | 3e-05 |  |
| [[TASOR]] | -0.63 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.63 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.63 | -0.48 / -0.71 | both halves | 2e-05 |  |
| [[DPP8]] | -0.62 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.62 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.62 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ZNF655]] | -0.61 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[CPSF2]] | -0.61 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[RNF6]] | -0.60 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[MED1]] | -0.60 | -0.61 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | EID2B activity raises MHENCR's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without EID2B | 0.006 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[CLEC11A]] | B | CLEC11A activity raises MHENCR's level | lines that do not express CLEC11A (21) vs lines expressing it (29) | 1.34× lower at baseline in the lines without CLEC11A | 0.044 | ⚠ within organs, on part of the lines; also absent: GABBR2, JAKMIP1, SHANK1 |
| [[SRP54-AS1]] | C | SRP54-AS1's natural level weakens MHENCR's drug response | SRP54-AS1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.70, reverse -0.04; direction not clear | 0.032 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.2, -5.3); signed map (-31.3, 7.1). **Vector** length 51.5, 7.99% of its response variance represented; |z| ≥ 3 in 635 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.3 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.0 | +3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | melanoma highly expressed competing endogenous lncRNA for miR-425 and miR-489 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q13.33 — chr20:63,627,179-63,628,824 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53110) · Entrez [100505771](https://www.ncbi.nlm.nih.gov/gene/100505771) · Ensembl [ENSG00000232442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232442)

## Data

Gene col 13848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13848); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13848]; `tensor/DDL_lfc|DDL_z.npy` [13848]; `embed/gene_vectors.npy` [13848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13848 or target_col == 13848). Every well: [[MHENCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MHENCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
