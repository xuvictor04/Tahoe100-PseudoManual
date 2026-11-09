---
symbol: "LUZP2"
type: "gene"
col: 11912
ensembl_id: "ENSG00000187398"
name: "leucine zipper protein 2"
location: "11p14.3"
module: 150
arm: "+"
pooled_cpm: 2.5
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# LUZP2

*leucine zipper protein 2* — 11p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.49× (z +23.4, q 0e+00, up in 26 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Futibatinib (drug)]] 0.05 µM: 0.661× (z -3.8, q 0.071, down in 9 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H2347 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTN5]] (+0.79, fdr 7e-06), [[GALNTL6]] (+0.78, fdr 7e-06), [[LINC02511]] (+0.78, fdr 7e-06).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.49×** | +23.4 | 0e+00 | 26/27 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.20×** | +13.9 | 1e-41 | 9/11 (J82, SW 900, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.68×** | +13.5 | 3e-39 | 18/31 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.40×** | +11.0 | 9e-26 | 3/5 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +10.8 | 6e-25 | 4/5 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.98×** | +10.6 | 3e-24 | 27/39 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +9.3 | 2e-18 | 22/44 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +6.8 | 6e-10 | 16/37 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +6.6 | 2e-09 | 16/37 (C32, BT-474, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.3 | 8e-06 | 9/44 (HOP62, SW 900, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.2 | 9e-06 | 13/30 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.8 | 8e-05 | 5/32 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.49×** | +4.6 | 2e-04 | 3/4 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.5 | 3e-04 | 6/24 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.3 | 5e-04 | 2/15 (J82, NCI-H2347) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.002 | 9/43 (NCI-H23, PANC-1, …) | two highest doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.005 | 9/44 (BT-474, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.012 | 5/37 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.022 | 5/27 (BT-474, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.079 | 9/44 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11912.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H2347 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Futibatinib (drug)]] 0.05 µM |  | **0.661×** | -3.8 | 0.071 | 9/40 (A498, H4, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 3.83 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 5.71× (z +9.3) | [[Clobetasol propionate (drug)]] 0.05 µM 0.105× (z -8.5) |
| [[HT-29 (line)]] | alt | 1.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +8.6) | — |
| [[LoVo (line)]] | wt | 1.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 2.45 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.34× (z +9.6) | — |
| [[SW480 (line)]] | alt | 1.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.37× (z +9.9) | — |
| [[A-172 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTN5]] | +0.79 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.78 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.78 | +0.66 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CNBD1]] | +0.77 | +0.63 / +0.81 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.75 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[FAT3]] | +0.75 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[SORCS1]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[XKR4]] | +0.75 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.75 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.75 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.74 | +0.67 / +0.81 | both halves | 7e-06 |  |
| [[GRID2]] | +0.74 | +0.61 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LUZP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | LUZP2's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | LUZP2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.360 over the table, 0.039 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.5, 29.4); signed map (33.2, 16.4). **Vector** length 50.2, 6.23% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +23.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +0.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine zipper protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.3 — chr11:24,496,970-25,082,638 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q86TE4](https://www.uniprot.org/uniprotkb/Q86TE4) carries no function annotation.

**Summary**, from NCBI Gene [338645](https://www.ncbi.nlm.nih.gov/gene/338645):

> This gene encodes a leucine zipper protein. This protein is deleted in some patients with Wilms tumor-Aniridia-Genitourinary anomalies-mental Retardation (WAGR) syndrome. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:23206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23206) · Entrez [338645](https://www.ncbi.nlm.nih.gov/gene/338645) · UniProt [Q86TE4](https://www.uniprot.org/uniprotkb/Q86TE4) · Ensembl [ENSG00000187398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187398)

## Data

Gene col 11912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11912); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11912]; `tensor/DDL_lfc|DDL_z.npy` [11912]; `embed/gene_vectors.npy` [11912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11912 or target_col == 11912). Every well: [[LUZP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LUZP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
