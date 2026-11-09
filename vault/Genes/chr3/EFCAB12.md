---
symbol: "EFCAB12"
type: "gene"
col: 10293
ensembl_id: "ENSG00000172771"
name: "EF-hand calcium binding domain 12"
location: "3q21.3"
module: 37
arm: "+"
pooled_cpm: 2.64
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# EFCAB12

*EF-hand calcium binding domain 12* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.45× (z +18.1, q 0e+00, up in 30 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Estrone sulfate (potassium) (drug)]] 5 µM: 0.611× (z -3.8, q 0.091, down in 10 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0931×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Brimonidine (drug)]] 0.5 µM in 1 line (A-427 0.0787×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BNIPL]] (+0.75, fdr 7e-06), [[MIA]] (+0.74, fdr 7e-06), [[DCAF4L1]] (+0.72, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.45×** | +18.1 | 0e+00 | 30/32 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.37×** | +12.7 | 2e-34 | 41/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.13×** | +10.3 | 1e-22 | 17/25 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +10.2 | 3e-22 | 23/35 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.78×** | +10.0 | 1e-21 | 38/43 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.69×** | +9.9 | 6e-21 | 32/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.87×** | +9.8 | 7e-21 | 11/12 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.42×** | +9.3 | 1e-18 | 38/43 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +9.1 | 4e-18 | 14/19 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.96×** | +8.2 | 1e-14 | 18/33 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +8.0 | 5e-14 | 23/34 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.41×** | +6.6 | 2e-09 | 22/43 (C-33 A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.30×** | +6.3 | 1e-08 | 22/41 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +5.7 | 4e-07 | 17/41 (SW480, SW48, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.00×** | +4.9 | 3e-05 | 14/40 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.8 | 5e-05 | 13/43 (A-172, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +4.3 | 7e-04 | 17/40 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10293.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0931×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Brimonidine (drug)]] 0.5 µM in 1 line (A-427 0.0787×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.611×** | -3.8 | 0.091 | 10/43 (HEC-1-A, CHP-212, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.619× | -3.5 | 0.12 | 14/36 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.658× | -3.2 | 0.23 | 11/41 (MIA PaCa-2, SNU-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | 0.663× | -3.2 | 0.23 | 9/43 (HS-578T, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.27 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0931× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 3.79 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +10.5) | — |
| [[A-172 (line)]] | wt | 2.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.96× (z +8.6) | — |
| [[A-427 (line)]] | wt | 7.25 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0787× (z -9.8) |
| [[PANC-1 (line)]] | alt | 1.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +8.7) | — |
| [[A498 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.983 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.856 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BNIPL]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[MIA]] | +0.74 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.72 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[WDR49]] | +0.72 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[SPX]] | +0.71 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.70 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TNXB]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[SNX31]] | +0.70 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[DRC1]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EFCAB12's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, -18.0); signed map (11.1, 5.8). **Vector** length 57.0, 8.05% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +18.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.3 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.1 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +3.1 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +0.3 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand calcium binding domain 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:129,401,321-129,428,636 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C3orf25 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

UniProt [Q6NXP0](https://www.uniprot.org/uniprotkb/Q6NXP0) carries no function annotation.

**Summary**, from NCBI Gene [90288](https://www.ncbi.nlm.nih.gov/gene/90288):

> Predicted to enable calcium ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28061) · Entrez [90288](https://www.ncbi.nlm.nih.gov/gene/90288) · UniProt [Q6NXP0](https://www.uniprot.org/uniprotkb/Q6NXP0) · Ensembl [ENSG00000172771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172771)

## Data

Gene col 10293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10293); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10293]; `tensor/DDL_lfc|DDL_z.npy` [10293]; `embed/gene_vectors.npy` [10293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10293 or target_col == 10293). Every well: [[EFCAB12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
