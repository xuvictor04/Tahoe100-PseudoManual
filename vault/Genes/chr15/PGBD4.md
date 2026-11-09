---
symbol: "PGBD4"
type: "gene"
col: 11285
ensembl_id: "ENSG00000182405"
name: "piggyBac transposable element derived 4"
location: "15q14"
module: 10
arm: "+"
pooled_cpm: 3.14
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PGBD4

*piggyBac transposable element derived 4* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +16.6, q 0e+00, up in 26 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX19A-DT]] (+0.76, fdr 1e-05), [[PDCL3P4]] (+0.74, fdr 4e-05), [[C2orf49-DT]] (+0.73, fdr 1e-05); moves opposite to [[RALGPS1]] (-0.60, fdr 6e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LAMA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +16.6 | 0e+00 | 26/36 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.00×** | +13.5 | 5e-39 | 8/14 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +12.5 | 8e-34 | 25/37 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +12.0 | 4e-31 | 3/5 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +11.1 | 1e-26 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +10.7 | 2e-24 | 22/46 (A549, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +9.6 | 4e-20 | 12/20 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +9.1 | 6e-18 | 15/35 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +8.3 | 4e-15 | 23/42 (LOX-IMVI, RKO, …) | rises with dose | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.59×** | +5.9 | 2e-07 | 5/21 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +5.8 | 3e-07 | 16/41 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.8 | 4e-07 | 12/46 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +5.5 | 2e-06 | 11/44 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.50×** | +5.2 | 1e-05 | 10/46 (A549, J82, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +5.1 | 2e-05 | 7/43 (NCI-H23, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 5e-04 | 5/40 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 6e-04 | 3/28 (SHP-77, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Nafamostat (mesylate) (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.005 | 1/42 (NCI-H2347) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.008 | 3/17 (A549, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.016 | 6/42 (NCI-H1792, BT-474, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.036 | 5/42 (NCI-H23, RKO, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.828× | -3.4 | 0.38 | 3/47 (Hs 766T, AN3 CA, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -3.0 | 0.66 | 10/47 (HEC-1-A, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 6.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 3.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 3.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +9.0) | — |
| [[A-172 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.914 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX19A-DT]] | +0.76 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[PDCL3P4]] | +0.74 | +0.82 / +0.42 | both halves | 4e-05 |  |
| [[C2orf49-DT]] | +0.73 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.72 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[ACAD9-DT]] | +0.72 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[TIGD6]] | +0.71 | +0.78 / +0.41 | both halves | 4e-05 |  |
| [[RBM26-AS1]] | +0.70 | +0.78 / +0.42 | both halves | 4e-05 |  |
| [[FNBP1P1]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[PJVK]] | +0.70 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[TRAM2-AS1]] | +0.70 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.70 | +0.75 / +0.42 | both halves | 4e-05 |  |
| [[UBE2D3-AS1]] | +0.70 | +0.71 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGPS1]] | -0.60 | -0.51 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA2]] | B | LAMA2 activity lowers PGBD4's level | lines that do not express LAMA2 (9) vs lines expressing it (41) | 1.13× higher at baseline in the lines without LAMA2 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC00243, DCBLD2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.6, 14.4); signed map (28.9, -13.6). **Vector** length 43.3, 4.42% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.3 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +16.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +5.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +2.6 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | piggyBac transposable element derived 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,102,083-34,108,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32638, FLJ37497 |
| Gene groups (HGNC) | PiggyBac transposable element derived family |
| Matched by | ensembl_id |

UniProt [Q96DM1](https://www.uniprot.org/uniprotkb/Q96DM1) carries no function annotation.

**Summary**, from NCBI Gene [161779](https://www.ncbi.nlm.nih.gov/gene/161779):

> The piggyBac family of proteins, found in diverse animals, are transposases related to the transposase of the canonical piggyBac transposon from the moth, Trichoplusia ni. This family also includes genes in several genomes, including human, that appear to have been derived from the piggyBac transposons. This gene belongs to the subfamily of piggyBac transposable element derived (PGBD) genes. The PGBD proteins appear to be novel, with no obvious relationship to other transposases, or other known …

**Accessions** — [HGNC:19401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19401) · Entrez [161779](https://www.ncbi.nlm.nih.gov/gene/161779) · UniProt [Q96DM1](https://www.uniprot.org/uniprotkb/Q96DM1) · Ensembl [ENSG00000182405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182405)

## Data

Gene col 11285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11285); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11285]; `tensor/DDL_lfc|DDL_z.npy` [11285]; `embed/gene_vectors.npy` [11285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11285 or target_col == 11285). Every well: [[PGBD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGBD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
