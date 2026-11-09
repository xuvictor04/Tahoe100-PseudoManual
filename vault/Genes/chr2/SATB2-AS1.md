---
symbol: "SATB2-AS1"
type: "gene"
col: 13497
ensembl_id: "ENSG00000225953"
name: "SATB2 antisense RNA 1"
location: "2q33.1"
module: 201
arm: "+"
pooled_cpm: 3.01
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# SATB2-AS1

*SATB2 antisense RNA 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.96× (z +21.6, q 0e+00, up in 29 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.534× (z -6.6, q 3e-08, down in 19 of 37 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB-AS1]] (+0.59, fdr 3e-05), [[HOXB5]] (+0.59, fdr 1e-05), [[DCAF5]] (+0.59, fdr 2e-05); moves opposite to [[WDR70]] (-0.55, fdr 1e-04), [[RRP7BP-1]] (-0.53, fdr 8e-05), [[ACSF3]] (-0.53, fdr 2e-04).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.96×** | +21.6 | 0e+00 | 29/30 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +11.1 | 3e-26 | 2/2 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +8.1 | 9e-14 | 7/14 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +8.0 | 1e-13 | 2/3 (LS 180, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.3 | 1e-05 | 5/25 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.3 | 1e-05 | 2/18 (LS 180, A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.006 | 6/43 (SW480, LOX-IMVI, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.89×** | +3.9 | 0.006 | 1/14 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.8 | 0.010 | 3/15 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.7 | 0.012 | 2/31 (HS-578T, SW480) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.018 | 5/41 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.77×** | +3.5 | 0.020 | 0/8 | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.020 | 8/43 (HOP62, RKO, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.534×** | -6.6 | 3e-08 | 19/37 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.641×** | -4.6 | 0.001 | 17/40 (SW480, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.679×** | -4.3 | 0.003 | 13/45 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.716×** | -3.7 | 0.029 | 10/43 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.722×** | -3.6 | 0.032 | 7/32 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.720×** | -3.4 | 0.056 | 9/41 (SW1417, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -3.4 | 0.062 | 11/38 (NCI-H2030, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.72 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0683× (z -8.8) |
| [[A498 (line)]] | wt | 3.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.75× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 4.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +9.4) | — |
| [[A-172 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.961 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.829 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB-AS1]] | +0.59 | +0.46 / +0.59 | both halves | 3e-05 | same gene group |
| [[HOXB5]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[DCAF5]] | +0.59 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[EMSY-DT]] | +0.58 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[ACVR2A]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[HOXB-AS3]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 | same gene group |
| [[TRIM7]] | +0.56 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[UPK2]] | +0.56 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[DNAJC3-DT]] | +0.55 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TAPT1]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[PSD]] | +0.54 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[ZBTB18]] | +0.54 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR70]] | -0.55 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[RRP7BP-1]] | -0.53 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[ACSF3]] | -0.53 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[METTL2B]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[RBM28]] | -0.49 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[EEFSEC]] | -0.49 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[HERC2]] | -0.47 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[HERC2P9-1]] | -0.47 | -0.21 / -0.54 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises SATB2-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers SATB2-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.2, 26.2); signed map (16.4, -5.6). **Vector** length 37.5, 3.86% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +21.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.8 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +11.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.8 | +0.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.1 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.0 | -4.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.8 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | SATB2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q33.1 — chr2:199,457,689-199,476,935 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26490) · Entrez [150538](https://www.ncbi.nlm.nih.gov/gene/150538) · Ensembl [ENSG00000225953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225953)

## Data

Gene col 13497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13497); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13497]; `tensor/DDL_lfc|DDL_z.npy` [13497]; `embed/gene_vectors.npy` [13497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13497 or target_col == 13497). Every well: [[SATB2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SATB2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
