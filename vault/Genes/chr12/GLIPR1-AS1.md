---
symbol: "GLIPR1-AS1"
type: "gene"
col: 15045
ensembl_id: "ENSG00000257497"
name: "GLIPR1 antisense RNA 1"
location: "12q21.2"
module: 83
arm: "+"
pooled_cpm: 4.54
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# GLIPR1-AS1

*GLIPR1 antisense RNA 1* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.04× (z +16.5, q 0e+00, up in 34 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFHX2-AS1]] (+0.82, fdr 7e-06), [[SMIM15-AS1]] (+0.80, fdr 7e-06), [[PPP1R3F]] (+0.79, fdr 7e-06); moves opposite to [[PAFAH1B3]] (-0.70, fdr 4e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.04×** | +16.5 | 0e+00 | 34/37 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.05×** | +11.7 | 4e-29 | 30/42 (SW480, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +10.0 | 2e-21 | 25/40 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +8.2 | 2e-14 | 22/38 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +7.8 | 5e-13 | 18/31 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.4 | 1e-11 | 7/11 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +7.3 | 2e-11 | 22/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.9 | 3e-10 | 15/45 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +6.5 | 6e-09 | 10/18 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.53×** | +6.3 | 2e-08 | 10/44 (NCI-H2347, NCI-H460, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +5.7 | 7e-07 | 19/46 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.2 | 1e-05 | 2/7 (NCI-H460, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +4.7 | 1e-04 | 20/43 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +4.4 | 4e-04 | 9/44 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.3 | 6e-04 | 10/42 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.47×** | +4.0 | 0.002 | 12/43 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.50×** | +4.0 | 0.002 | 10/43 (A-427, RKO, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.002 | 14/43 (SNU-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.008 | 5/44 (NCI-H460, SW480, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 2.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.77× (z +8.8) | — |
| [[A-172 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFHX2-AS1]] | +0.82 | +0.73 / +0.63 | both halves | 7e-06 | same gene group |
| [[SMIM15-AS1]] | +0.80 | +0.70 / +0.63 | both halves | 7e-06 | same gene group |
| [[PPP1R3F]] | +0.79 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.78 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[TAS2R4]] | +0.77 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[BAAT]] | +0.76 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[LINC00880]] | +0.75 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[MSH4]] | +0.75 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[KLRA1P]] | +0.74 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.74 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[PELO-AS1]] | +0.74 | +0.67 / +0.59 | both halves | 7e-06 | same gene group |
| [[ZNF596]] | +0.74 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAFAH1B3]] | -0.70 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GLIPR1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ST8SIA5]] | B | ST8SIA5 activity raises GLIPR1-AS1's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.54× lower at baseline in the lines without ST8SIA5 | 0.079 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[FRZB]] | C | FRZB activity raises GLIPR1-AS1's level | lines that do not express FRZB (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without FRZB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.827). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.1, 8.5); signed map (19.4, -1.6). **Vector** length 64.4, 9.61% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | GLIPR1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q21.2 — chr12:75,483,454-75,489,820 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-585P4.5 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56075) · Entrez [123706544](https://www.ncbi.nlm.nih.gov/gene/123706544) · Ensembl [ENSG00000257497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257497)

## Data

Gene col 15045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15045); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15045]; `tensor/DDL_lfc|DDL_z.npy` [15045]; `embed/gene_vectors.npy` [15045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15045 or target_col == 15045). Every well: [[GLIPR1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLIPR1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
