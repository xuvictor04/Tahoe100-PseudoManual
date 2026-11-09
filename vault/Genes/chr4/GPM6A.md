---
symbol: "GPM6A"
type: "gene"
col: 7446
ensembl_id: "ENSG00000150625"
name: "glycoprotein M6A"
location: "4q34.2"
module: 61
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# GPM6A

*glycoprotein M6A* — 4q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.61× (z +19.5, q 0e+00, up in 24 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02511]] (+0.78, fdr 7e-06), [[LUZP2]] (+0.73, fdr 7e-06), [[SGCZ]] (+0.72, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NBEAP1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.61×** | +19.5 | 0e+00 | 24/28 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.56×** | +16.2 | 0e+00 | 32/41 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.64×** | +15.1 | 0e+00 | 3/4 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.00×** | +14.0 | 1e-42 | 17/27 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.70×** | +14.0 | 2e-42 | 4/7 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.47×** | +10.4 | 3e-23 | 1/4 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.08×** | +10.2 | 2e-22 | 22/31 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.59×** | +8.6 | 6e-16 | 23/41 (NCI-H2347, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.57×** | +8.5 | 1e-15 | 21/34 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +7.5 | 4e-12 | 5/40 (J82, CHP-212, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +7.1 | 5e-11 | 16/40 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +6.7 | 8e-10 | 9/28 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +6.2 | 2e-08 | 17/42 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.7 | 5e-07 | 7/41 (A-172, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.6 | 6e-07 | 5/9 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.85×** | +5.6 | 1e-06 | 12/42 (A-172, A-427, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +5.5 | 1e-06 | 16/40 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +5.5 | 1e-06 | 7/15 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +4.2 | 8e-04 | 5/26 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.05× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 4.52 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.44× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 1.22 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 1.04 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.0× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 0.881 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +8.7) | — |
| [[A-427 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.756 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.721 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.735 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.715 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.991 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.863 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.744 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.668 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.932 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.704 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.793 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.765 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.710 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02511]] | +0.78 | +0.71 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LUZP2]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.72 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.70 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[GRID2]] | +0.70 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[SNAP91]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[FAT3]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NRXN1]] | +0.69 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[CNBD1]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[TMEFF2]] | +0.68 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.67 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[KCNH1]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBEAP1]] | B | NBEAP1 activity lowers GPM6A's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.16× higher at baseline in the lines without NBEAP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B |
| [[TOP2A]] | B | TOP2A activity lowers GPM6A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PDGFD]] | B | PDGFD activity raises GPM6A's level | lines that do not express PDGFD (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without PDGFD | 0.093 | ⚠ within organs, on part of the lines; also absent: LRRC63, ZFHX4, FGF14; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | GPM6A's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | GPM6A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.491 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.3, 30.3); signed map (33.7, 17.4). **Vector** length 52.3, 7.91% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +16.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +19.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +4.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | +0.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | +0.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | glycoprotein M6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.2 — chr4:175,632,934-176,002,664 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GPM6 |
| Matched by | ensembl_id |

**Function**, from UniProt [P51674](https://www.uniprot.org/uniprotkb/P51674) (Neuronal membrane glycoprotein M6-a):

> Involved in neuronal differentiation, including differentiation and migration of neuronal stem cells. Plays a role in neuronal plasticity and is involved in neurite and filopodia outgrowth, filopodia motility and probably synapse formation. GPM6A-induced filopodia formation involves mitogen-activated protein kinase (MAPK) and Src signaling pathways. May be involved in neuronal NGF-dependent Ca(2+) influx. May be involved in regulation of endocytosis and intracellular trafficking of G …

**Summary**, from NCBI Gene [2823](https://www.ncbi.nlm.nih.gov/gene/2823):

> Predicted to enable calcium channel activity. Involved in neuron migration and stem cell differentiation. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4460) · Entrez [2823](https://www.ncbi.nlm.nih.gov/gene/2823) · UniProt [P51674](https://www.uniprot.org/uniprotkb/P51674) · Ensembl [ENSG00000150625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150625)

## Data

Gene col 7446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7446); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7446]; `tensor/DDL_lfc|DDL_z.npy` [7446]; `embed/gene_vectors.npy` [7446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7446 or target_col == 7446). Every well: [[GPM6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPM6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
