---
symbol: "WASH9P"
type: "gene"
col: 15936
ensembl_id: "ENSG00000279457"
name: "WAS protein family homolog 9, pseudogene"
location: "1p36.33"
module: 153
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# WASH9P

*WAS protein family homolog 9, pseudogene* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +5.7, q 5e-06, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bosentan (hydrate) (drug)]] 5 µM: 1.65× (z +4.2, q 0.009, up in 4 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.642× (z -3.8, q 0.092, down in 18 of 43 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (LoVo 0.0696×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASH8P]] (+0.87, fdr 7e-06, ⚠ WASH8P in the vector space only through flagged drug-doses), [[BMS1P2]] (+0.72, fdr 7e-06), [[MTX1]] (+0.67, fdr 1e-05), [[ANAPC2]] (+0.66, fdr 1e-05); moves opposite to [[NDUFA7]] (-0.57, fdr 1e-05), [[ARIH1]] (-0.56, fdr 6e-05), [[HES1]] (-0.52, fdr 3e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARMCX6]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +5.7 | 5e-06 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.65×** | +4.2 | 0.009 | 4/28 (SW1417, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +3.7 | 0.031 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +3.7 | 0.031 | 0/2 | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.087 | 8/40 (COLO 205, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15936.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (LoVo 0.0696×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.642×** | -3.8 | 0.092 | 18/43 (SW48, C-33 A, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.669× | -3.3 | 0.23 | 13/39 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[Fusidic acid (drug)]] 0.5 µM |  | 0.663× | -3.2 | 0.23 | 10/41 (SK-MEL-2, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 2.51 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0696× (z -8.6) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASH8P]] ⚠ | +0.87 | +0.83 / +0.85 | both halves | 7e-06 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[BMS1P2]] | +0.72 | +0.67 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MTX1]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ANAPC2]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[LENG8]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NAXD]] | +0.63 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[CERS2]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SNHG22]] | +0.61 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[LINC03009]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[HFM1]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[STRN4]] | +0.60 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[TOP3B]] | +0.60 | +0.45 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA7]] | -0.57 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ARIH1]] | -0.56 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[HES1]] | -0.52 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[LAGE3]] | -0.51 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[ZSWIM6]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[H3-3B]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TMEM205]] | -0.50 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[FBXO11]] | -0.49 | -0.20 / -0.49 | both halves | 7e-04 |  |
| [[TLE4]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[TIMM17B]] ⚠ | -0.48 | -0.33 / -0.51 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARMCX6]] | C | ARMCX6 activity lowers WASH9P's level | lines that do not express ARMCX6 (3) vs lines expressing it (46) | 1.43× higher at baseline in the lines without ARMCX6 | 0.064 | ⚠ few lines (3 vs 46); across organs; also absent: ARMCX3, TRAF3IP2, SFXN3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.1, -24.9); signed map (-13.6, -32.5). **Vector** length 38.3, 3.61% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +5.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.1 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.5 | -0.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.2 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +1.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Altretamine (drug)]] 0.5 µM |  | +0.9 | +0.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.1 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.7 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.3 | -1.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | WAS protein family homolog 9, pseudogene |
| Locus type | pseudogene |
| Location | 1p36.33 — chr1:185,217-195,411 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53981) · Entrez [100996442](https://www.ncbi.nlm.nih.gov/gene/100996442) · Ensembl [ENSG00000279457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000279457)

## Data

Gene col 15936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15936); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15936]; `tensor/DDL_lfc|DDL_z.npy` [15936]; `embed/gene_vectors.npy` [15936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15936 or target_col == 15936). Every well: [[WASH9P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASH9P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
