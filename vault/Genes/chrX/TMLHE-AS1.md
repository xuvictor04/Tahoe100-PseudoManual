---
symbol: "TMLHE-AS1"
type: "gene"
col: 13402
ensembl_id: "ENSG00000224533"
name: "TMLHE antisense RNA 1"
location: "Xq28"
module: 35
arm: "+"
pooled_cpm: 3.8
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# TMLHE-AS1

*TMLHE antisense RNA 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +15.2, q 0e+00, up in 28 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.619× (z -5.4, q 4e-05, down in 12 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STARD4-AS1]] (+0.69, fdr 2e-05), [[HPSE2]] (+0.66, fdr 1e-05), [[PAXBP1-AS1]] (+0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +15.2 | 0e+00 | 28/35 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +13.2 | 3e-37 | 15/21 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +10.5 | 3e-23 | 2/6 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +8.2 | 5e-14 | 2/10 (HOP62, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +6.0 | 3e-07 | 12/31 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.8 | 2e-04 | 11/36 (LS 180, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.001 | 8/44 (NCI-H460, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.8 | 0.011 | 5/20 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.014 | 2/40 (SNU-423, SW 900) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.022 | 4/43 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.036 | 15/43 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.21× | +3.1 | 0.10 | 7/44 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.31× | +3.0 | 0.11 | 4/39 (NCI-H2030, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.619×** | -5.4 | 4e-05 | 12/45 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.624×** | -5.3 | 4e-05 | 15/46 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.667×** | -4.5 | 0.001 | 12/44 (C-33 A, H4, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -4.3 | 0.003 | 18/42 (SW 900, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.710×** | -3.7 | 0.026 | 14/42 (NCI-H1792, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.741×** | -3.4 | 0.076 | 7/43 (NCI-H2347, SNU-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.763× | -3.0 | 0.21 | 12/36 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.19 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0719× (z -9.3) |
| [[A498 (line)]] | wt | 2.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.48 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.05 µM 0.0537× (z -9.4) |
| [[HOP62 (line)]] | alt | 5.20 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[HT-29 (line)]] | alt | 5.34 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0853× (z -8.8) |
| [[J82 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0659× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[LS 180 (line)]] | wt | 2.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -11.9) ⚠ cell-cycle shift, explains ~82% of this change |
| [[NCI-H460 (line)]] | wt | 4.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 7.13 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.2) ⚠ cell-cycle shift, explains ~82% of this change |
| [[SW 900 (line)]] | alt | 6.31 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0767× (z -9.0) |
| [[A-172 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD4-AS1]] | +0.69 | +0.57 / +0.47 | both halves | 2e-05 | same gene group |
| [[HPSE2]] | +0.66 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PAXBP1-AS1]] | +0.65 | +0.44 / +0.61 | both halves | 3e-05 | same gene group |
| [[RNPC3-DT]] | +0.65 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SLC27A6]] | +0.65 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[ZNF561-AS1]] | +0.65 | +0.60 / +0.44 | both halves | 3e-05 | same gene group |
| [[CCDC26]] | +0.64 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[TAFA2]] | +0.64 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ARL14EP-DT]] | +0.64 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[DLGAP4-AS1]] | +0.64 | +0.53 / +0.50 | both halves | 1e-05 | same gene group |
| [[CDNF]] | +0.64 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[FLG-AS1]] | +0.64 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMLHE-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CFAP58]] | B | CFAP58 activity raises TMLHE-AS1's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 1.12× lower at baseline in the lines without CFAP58 | 0.079 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises TMLHE-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (15.5, 20.1); signed map (31.9, -4.6). **Vector** length 46.7, 5.29% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +13.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +1.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -0.9 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | TMLHE antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq28 — chrX:155,466,540-155,611,616 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44261) · Entrez [100507404](https://www.ncbi.nlm.nih.gov/gene/100507404) · Ensembl [ENSG00000224533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224533)

## Data

Gene col 13402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13402); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13402]; `tensor/DDL_lfc|DDL_z.npy` [13402]; `embed/gene_vectors.npy` [13402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13402 or target_col == 13402). Every well: [[TMLHE-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMLHE-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
