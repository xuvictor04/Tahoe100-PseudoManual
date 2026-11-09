---
symbol: "CHMP1B-AS1"
type: "gene"
col: 15527
ensembl_id: "ENSG00000267165"
name: "CHMP1B antisense RNA 1"
location: "18p11.21"
module: 21
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CHMP1B-AS1

*CHMP1B antisense RNA 1* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.03× (z +9.3, q 5e-18, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.72× (z +4.7, q 3e-04, up in 15 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLDN14]] (+0.67, fdr 1e-05), [[SLC13A4]] (+0.65, fdr 1e-05), [[CTBP1-AS]] (+0.61, fdr 2e-05, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[BMAL2-AS1]] (+0.60, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADAM7-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +9.3 | 5e-18 | 1/2 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +8.8 | 5e-16 | 11/16 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.95×** | +5.9 | 8e-07 | 17/43 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +4.7 | 3e-04 | 15/37 (SW480, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.2 | 0.002 | 4/13 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +4.2 | 0.002 | 3/8 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.8 | 0.012 | 5/22 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.5 | 0.029 | 7/26 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.4 | 0.043 | 3/13 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.087 | 5/36 (PANC-1, HCT15, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.11 | 3/32 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15527.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.685× | -3.4 | 0.26 | 8/26 (CFPAC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.688× | -3.3 | 0.26 | 5/41 (HT-29, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLDN14]] | +0.67 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SLC13A4]] | +0.65 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | +0.61 | +0.47 / +0.63 | both halves | 2e-05 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[BMAL2-AS1]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 | same gene group |
| [[VCAN-AS1]] | +0.59 | +0.44 / +0.54 | both halves | 3e-05 | same gene group |
| [[STARD13-AS]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 | same gene group |
| [[ACVR1C]] | +0.58 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[RN7SL2]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SLC8A1-AS1]] | +0.57 | +0.45 / +0.52 | both halves | 3e-05 | same gene group |
| [[OMG]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SLC9C1]] | +0.56 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[FILIP1]] | +0.56 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[HERC4]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM7-AS1]] | B | ADAM7-AS1 activity raises CHMP1B-AS1's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.31× lower at baseline in the lines without ADAM7-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises CHMP1B-AS1's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.23× lower at baseline in the lines without CLDN14-AS1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.540). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, 27.1); signed map (31.6, 7.6). **Vector** length 31.1, 2.56% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +2.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | +2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | CHMP1B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18p11.21 — chr18:11,851,414-11,852,751 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52778) · Entrez [109729129](https://www.ncbi.nlm.nih.gov/gene/109729129) · Ensembl [ENSG00000267165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267165)

## Data

Gene col 15527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15527); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15527]; `tensor/DDL_lfc|DDL_z.npy` [15527]; `embed/gene_vectors.npy` [15527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15527 or target_col == 15527). Every well: [[CHMP1B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP1B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
