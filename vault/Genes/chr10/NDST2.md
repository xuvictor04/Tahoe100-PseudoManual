---
symbol: "NDST2"
type: "gene"
col: 9322
ensembl_id: "ENSG00000166507"
name: "N-deacetylase and N-sulfotransferase 2"
location: "10q22.2"
module: 157
arm: "+"
pooled_cpm: 5.1
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# NDST2

*N-deacetylase and N-sulfotransferase 2* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.13× (z +4.9, q 6e-04, up in 7 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +3.7, q 0.042, up in 12 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.626× (z -5.4, q 4e-05, down in 16 of 31 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.662× (z -4.9, q 2e-04, down in 19 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSK3A]] (+0.61, fdr 1e-05), [[ULK3]] (+0.61, fdr 1e-05), [[ADCK5]] (+0.61, fdr 7e-06); moves opposite to [[SMIM30]] (-0.53, fdr 4e-05), [[SSH2]] (-0.48, fdr 5e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.9 | 6e-04 | 7/48 (Hs 766T, A-172, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.5 | 0.002 | 11/31 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.042 | 12/40 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.051 | 10/39 (SW48, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.051 | 8/47 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | 1.21× | +3.2 | 0.13 | 4/47 (MIA PaCa-2, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.626×** | -5.4 | 4e-05 | 16/31 (C32, A498, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -4.9 | 2e-04 | 19/45 (SNU-423, LOX-IMVI, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.679×** | -4.5 | 0.002 | 13/44 (LOX-IMVI, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -4.2 | 0.003 | 11/45 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.710×** | -4.1 | 0.004 | 7/45 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |
| [[Furosemide (drug)]] 0.5 µM |  | **0.745×** | -3.5 | 0.032 | 10/44 (Panc 03.27, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.746×** | -3.5 | 0.032 | 12/47 (HOP62, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.747×** | -3.5 | 0.032 | 10/44 (SNU-1, SW48, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.734×** | -3.4 | 0.038 | 9/42 (LoVo, C32, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.755×** | -3.3 | 0.064 | 5/45 (RPMI-7951, SK-MEL-2, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.610× | -3.1 | 0.10 | 5/43 (MIA PaCa-2, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 4.50 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0851× (z -8.8) |
| [[LS 180 (line)]] | wt | 4.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 5.13 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.103× (z -8.7) |
| [[SW1417 (line)]] | alt | 6.25 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSK3A]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ULK3]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[OPLAH]] ⚠ | +0.57 | +0.55 / +0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MAN2C1]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[SBF1]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[AKT1]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ANAPC2]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PRSS53]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[FHIP2B]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[FAM219B]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[IRGQ]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[GLI4]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM30]] | -0.53 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SSH2]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity lowers NDST2's level | compounds that target TOP1: 2 of 3 raise it (Doxorubicin, Topotecan) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.2, -23.6); signed map (-25.5, -1.0). **Vector** length 41.8, 4.10% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.7 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +0.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.4 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Ivermectin (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -2.2 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.9 | -5.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | N-deacetylase and N-sulfotransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,801,911-73,811,798 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NST2, HSST2 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | HYPOXIA |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P52849](https://www.uniprot.org/uniprotkb/P52849) (Bifunctional heparan sulfate N-deacetylase/N-sulfotransferase 2):

> Essential bifunctional enzyme that catalyzes both the N-deacetylation and the N-sulfation of glucosamine (GlcNAc) of the glycosaminoglycan in heparan sulfate (By similarity). Exhibits N-deacetylase activity. Modifies the GlcNAc-GlcA disaccharide repeating sugar backbone to make N-sulfated heparosan, a prerequisite substrate for later modifications in heparin biosynthesis (By similarity). Plays a role in determining the extent and pattern of sulfation of heparan sulfate (By similarity). Required …

**Summary**, from NCBI Gene [8509](https://www.ncbi.nlm.nih.gov/gene/8509):

> This gene encodes a member of the N-deacetylase/N-sulfotransferase subfamily of the sulfotransferase 1 proteins. The encoded enzyme has dual functions in processing glucosamine and heparin polymers, including N-deacetylation and N-sulfation. The encoded protein may be localized to the Golgi. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:7681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7681) · Entrez [8509](https://www.ncbi.nlm.nih.gov/gene/8509) · UniProt [P52849](https://www.uniprot.org/uniprotkb/P52849) · Ensembl [ENSG00000166507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166507)

## Data

Gene col 9322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9322); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9322]; `tensor/DDL_lfc|DDL_z.npy` [9322]; `embed/gene_vectors.npy` [9322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9322 or target_col == 9322). Every well: [[NDST2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDST2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
