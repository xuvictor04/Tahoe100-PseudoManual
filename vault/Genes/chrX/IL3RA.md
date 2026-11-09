---
symbol: "IL3RA"
type: "gene"
col: 11655
ensembl_id: "ENSG00000185291"
name: "interleukin 3 receptor subunit alpha"
location: "Xp22.33 and Yp11.2"
module: 61
arm: "+"
pooled_cpm: 5.69
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# IL3RA

*interleukin 3 receptor subunit alpha* — Xp22.33 and Yp11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.16× (z +19.9, q 0e+00, up in 39 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (HOP62 0.0799×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.101×); [[Canagliflozin (drug)]] 5 µM in 1 line (NCI-H2030 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTUS2]] (+0.67, fdr 7e-06), [[SGCZ]] (+0.67, fdr 1e-05), [[DLGAP2]] (+0.65, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KCNN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.16×** | +19.9 | 0e+00 | 39/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +10.2 | 9e-22 | 27/41 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.34×** | +10.0 | 3e-21 | 5/9 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.22×** | +9.7 | 3e-20 | 30/47 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +9.2 | 3e-18 | 27/46 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.06×** | +8.8 | 9e-17 | 15/26 (LoVo, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +8.4 | 3e-15 | 26/45 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.0 | 2e-10 | 25/42 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.65×** | +5.7 | 9e-07 | 6/19 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.1 | 2e-05 | 18/47 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.0 | 3e-05 | 15/33 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.45×** | +4.5 | 3e-04 | 14/47 (NCI-H460, J82, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.42×** | +4.3 | 9e-04 | 14/43 (J82, AsPC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.026 | 15/45 (SNU-423, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (HOP62 0.0799×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.101×); [[Canagliflozin (drug)]] 5 µM in 1 line (NCI-H2030 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -4.0 | 0.039 | 10/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.837× | -3.1 | 0.55 | 15/48 (C32, PANC-1, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.12 | 7 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 12.5× (z +21.2) | — |
| [[Hs 766T (line)]] | wt | 7.25 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +11.9) | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.101× (z -9.4) |
| [[J82 (line)]] | alt | 7.12 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.85× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 4.09 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.29× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 6.64 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.36× (z +10.6) | — |
| [[A-172 (line)]] | wt | 9.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.59× (z +9.7) | — |
| [[A549 (line)]] | wt | 9.43 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.71× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 9.50 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0966× (z -9.0) |
| [[C32 (line)]] | wt | 5.40 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.57× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 8.99 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.78× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 3.82 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0799× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 5.40 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0674× (z -8.8) |
| [[LoVo (line)]] | wt | 7.75 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 5.99 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.110× (z -9.1) |
| [[SW480 (line)]] | alt | 6.53 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.68× (z +13.0) | — |
| [[A-427 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTUS2]] | +0.67 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.67 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.65 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CELF5]] | +0.65 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[COL26A1]] | +0.64 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[RBFOX3]] | +0.63 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[ATP6V1C2]] | +0.63 | +0.41 / +0.77 | both halves | 4e-05 |  |
| [[ISM1]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[LINC02511]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[SYN1]] | +0.62 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[MYO1F]] | +0.62 | +0.46 / +0.70 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNN3]] | B | KCNN3 activity raises IL3RA's level | lines that do not express KCNN3 (8) vs lines expressing it (42) | 1.30× lower at baseline in the lines without KCNN3 | 0.073 | ⚠ within organs, on part of the lines; also absent: VLDLR-AS1, ADGRG2, SLC17A7; maybe low, not absent |
| [[HS6ST3]] | B | HS6ST3 activity strengthens IL3RA's drug response | lines that do not express HS6ST3 (19) vs lines expressing it (29) | the lines without HS6ST3 respond 0.71× as strongly (z diff +1.16); strongest at Panobinostat 5 µM: 1.55x vs 2.61x (z diff +2.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NTRK3]] | B | NTRK3 activity raises IL3RA's level | lines that do not express NTRK3 (32) vs lines expressing it (18) | 1.25× lower at baseline in the lines without NTRK3 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF732, SYNDIG1, LINC00648; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.5, 33.0); signed map (28.3, 18.4). **Vector** length 56.4, 7.21% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +19.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.5 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.4 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.8 | -3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 3 receptor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 and Yp11.2 — chrX:1,336,616-1,382,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD123 |
| Gene groups (HGNC) | CD molecules; Interleukin receptors; Pseudoautosomal region 1 |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, IL2_STAT5_SIGNALING |
| Reactome | 8 pathways, smallest: Interleukin receptor SHC signaling; Interleukin-2 family signaling; Interleukin-3, Interleukin-5 and GM-CSF signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P26951](https://www.uniprot.org/uniprotkb/P26951) (Interleukin-3 receptor subunit alpha):

> Cell surface receptor for IL3 expressed on hematopoietic progenitor cells, monocytes and B-lymphocytes that controls the production and differentiation of hematopoietic progenitor cells into lineage-restricted cells. Ligand stimulation rapidly induces hetrodimerization with IL3RB, phosphorylation and enzyme activity of effector proteins such as JAK2 and PI3K that play a role in signaling cell proliferation and differentiation. Activation of JAK2 leads to STAT5-mediated transcriptional program …

**Summary**, from NCBI Gene [3563](https://www.ncbi.nlm.nih.gov/gene/3563):

> The protein encoded by this gene is an interleukin 3 specific subunit of a heterodimeric cytokine receptor. The receptor is comprised of a ligand specific alpha subunit and a signal transducing beta subunit shared by the receptors for interleukin 3 (IL3), colony stimulating factor 2 (CSF2/GM-CSF), and interleukin 5 (IL5). The binding of this protein to IL3 depends on the beta subunit. The beta subunit is activated by the ligand binding, and is required for the biological activities of IL3. This …

**Accessions** — [HGNC:6012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6012) · Entrez [3563](https://www.ncbi.nlm.nih.gov/gene/3563) · UniProt [P26951](https://www.uniprot.org/uniprotkb/P26951) · Ensembl [ENSG00000185291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185291)

## Data

Gene col 11655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11655); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11655]; `tensor/DDL_lfc|DDL_z.npy` [11655]; `embed/gene_vectors.npy` [11655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11655 or target_col == 11655). Every well: [[IL3RA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL3RA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
