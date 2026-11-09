---
symbol: "FAM217A"
type: "gene"
col: 7047
ensembl_id: "ENSG00000145975"
name: "family with sequence similarity 217 member A"
location: "6p25.2"
module: 21
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# FAM217A

*family with sequence similarity 217 member A* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.90× (z +9.6, q 3e-19, up in 17 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +6.3, q 6e-08, up in 21 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.805× (z -6.6, q 3e-08, down in 31 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Darinaparsin (drug)]] 0.5 µM in 1 line (HT-29 0.0644×); [[Proglumide (drug)]] 5 µM in 1 line (BT-474 0.0415×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZRANB2-AS1]] (+0.89, fdr 7e-06), [[TICAM2-AS1]] (+0.88, fdr 7e-06), [[EOGT-DT]] (+0.86, fdr 7e-06); moves opposite to [[BBS10]] (-0.62, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PAN3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +9.6 | 3e-19 | 17/21 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +8.8 | 5e-16 | 5/6 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.3 | 6e-08 | 21/38 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +5.8 | 1e-06 | 7/8 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.5 | 7e-04 | 18/37 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +4.3 | 0.002 | 12/25 (LS 180, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.0 | 0.005 | 7/28 (Panc 03.27, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.5 | 0.030 | 7/22 (AsPC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +3.4 | 0.039 | 13/46 (SW480, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.29×** | +3.3 | 0.052 | 6/35 (HS-578T, LoVo, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +3.2 | 0.066 | 5/39 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.097 | 2/31 (PANC-1, A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7047.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Darinaparsin (drug)]] 0.5 µM in 1 line (HT-29 0.0644×); [[Proglumide (drug)]] 5 µM in 1 line (BT-474 0.0415×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.805×** | -6.6 | 3e-08 | 31/48 (KATO III, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.688× | -3.2 | 0.41 | 7/45 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 3.30 | 0 | 1 | — | [[Proglumide (drug)]] 5 µM 0.0415× (z -8.7) |
| [[HT-29 (line)]] | alt | 3.39 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.5 µM 0.0644× (z -9.2) |
| [[A-172 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZRANB2-AS1]] | +0.89 | +0.82 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[TICAM2-AS1]] | +0.88 | +0.81 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[EOGT-DT]] | +0.86 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[RN7SL1]] | +0.86 | +0.70 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[FLJ40194]] | +0.85 | +0.72 / +0.82 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.85 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[MAL2-AS1]] | +0.85 | +0.73 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[BIRC6-AS2-1]] | +0.84 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.84 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | +0.83 | +0.77 / +0.84 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.82 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.82 | +0.76 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS10]] | -0.62 | -0.44 / -0.65 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAN3]] | C | FAM217A's natural level strengthens PAN3's drug response | FAM217A's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.08; direction not clear | 0.030 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.889). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 28.6); signed map (34.4, 5.6). **Vector** length 35.2, 3.24% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.3 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -6.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 217 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:4,049,434-4,087,344 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC43581; previously C6orf146 |
| Matched by | ensembl_id |

UniProt [Q8IXS0](https://www.uniprot.org/uniprotkb/Q8IXS0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21362) · Entrez [222826](https://www.ncbi.nlm.nih.gov/gene/222826) · UniProt [Q8IXS0](https://www.uniprot.org/uniprotkb/Q8IXS0) · Ensembl [ENSG00000145975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145975)

## Data

Gene col 7047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7047); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7047]; `tensor/DDL_lfc|DDL_z.npy` [7047]; `embed/gene_vectors.npy` [7047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7047 or target_col == 7047). Every well: [[FAM217A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM217A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
