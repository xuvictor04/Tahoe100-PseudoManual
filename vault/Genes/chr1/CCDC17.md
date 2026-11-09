---
symbol: "CCDC17"
type: "gene"
col: 8261
ensembl_id: "ENSG00000159588"
name: "coiled-coil domain containing 17"
location: "1p34.1"
module: 181
arm: "+"
pooled_cpm: 2.15
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# CCDC17

*coiled-coil domain containing 17* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.93× (z +10.8, q 1e-24, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.504× (z -4.9, q 6e-04, down in 17 of 41 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.607× (z -3.6, q 0.068, down in 12 of 23 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02936]] (+0.76, fdr 7e-06), [[MCF2]] (+0.75, fdr 1e-05), [[NLGN3]] (+0.75, fdr 7e-06); moves opposite to [[PAFAH1B3]] (-0.64, fdr 2e-04), [[GGCT]] (-0.63, fdr 5e-05), [[CBR1]] (-0.61, fdr 5e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +10.8 | 1e-24 | 30/31 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +7.4 | 5e-11 | 13/24 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +5.7 | 2e-06 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +5.6 | 3e-06 | 17/32 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +5.5 | 5e-06 | 13/31 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.92×** | +4.7 | 3e-04 | 10/45 (RKO, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.016 | 6/41 (LOX-IMVI, NCI-H2347, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +3.5 | 0.031 | 7/28 (A-427, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +3.4 | 0.045 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +3.3 | 0.064 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.53× | +3.0 | 0.13 | 5/23 (SW480, BT-474, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.504×** | -4.9 | 6e-04 | 17/41 (RKO, LOX-IMVI, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.579×** | -3.9 | 0.027 | 16/41 (LOX-IMVI, SW1417, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.607×** | -3.6 | 0.068 | 12/23 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.629×** | -3.3 | 0.096 | 9/42 (SW1417, PANC-1, …) | all doses, flat |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.721×** | -3.3 | 0.096 | 8/44 (SHP-77, HT-29, …) | top dose only | position effect removed |
| [[Hesperidin (drug)]] 0.5 µM |  | **0.631×** | -3.3 | 0.096 | 15/39 (A-427, Hs 766T, …) | two highest doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.437× | -3.1 | 0.16 | 12/34 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 3.30 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.05 µM 0.0558× (z -9.8) |
| [[A-172 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.610 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02936]] | +0.76 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[MCF2]] | +0.75 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.75 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[LRRC37A3]] | +0.72 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[LINC02955]] | +0.72 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[SMIM15-AS1]] | +0.72 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R3F]] | +0.72 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[PSMD6-AS1]] | +0.72 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[PXDNL]] | +0.72 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | +0.71 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[GLIPR1-AS1]] | +0.71 | +0.72 / +0.37 | both halves | 7e-05 |  |
| [[TMED6]] | +0.71 | +0.70 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAFAH1B3]] | -0.64 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[GGCT]] | -0.63 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[CBR1]] | -0.61 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC17's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises CCDC17's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.3, -13.8); signed map (18.8, 3.0). **Vector** length 56.1, 7.56% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -3.6 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.1 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,620,044-45,624,057 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33084 |
| Matched by | ensembl_id |

UniProt [Q96LX7](https://www.uniprot.org/uniprotkb/Q96LX7) carries no function annotation.

**Summary**, from NCBI Gene [149483](https://www.ncbi.nlm.nih.gov/gene/149483):

> Located in axoneme. Implicated in colorectal adenocarcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26574) · Entrez [149483](https://www.ncbi.nlm.nih.gov/gene/149483) · UniProt [Q96LX7](https://www.uniprot.org/uniprotkb/Q96LX7) · Ensembl [ENSG00000159588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159588)

## Data

Gene col 8261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8261); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8261]; `tensor/DDL_lfc|DDL_z.npy` [8261]; `embed/gene_vectors.npy` [8261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8261 or target_col == 8261). Every well: [[CCDC17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
