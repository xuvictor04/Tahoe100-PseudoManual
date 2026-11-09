---
symbol: "DCAF4L1"
type: "gene"
col: 11271
ensembl_id: "ENSG00000182308"
name: "DDB1 and CUL4 associated factor 4 like 1"
location: "4p13"
module: 37
arm: "+"
pooled_cpm: 2.59
n_lines_expressing: 49
n_dd_up: 43
n_dd_down: 1
n_dd_up_clean: 28
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# DCAF4L1

*DDB1 and CUL4 associated factor 4 like 1* — 4p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.01× (z +14.2, q 3e-43, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.594× (z -3.8, q 0.072, down in 14 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRZB]] (+0.78, fdr 7e-06), [[SNX31]] (+0.78, fdr 7e-06), [[CCDC13]] (+0.77, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TMED6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.01×** | +14.2 | 3e-43 | 30/31 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **6.19×** | +13.2 | 2e-37 | 36/40 (SW480, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.60×** | +13.1 | 5e-37 | 27/35 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **5.83×** | +12.3 | 1e-32 | 11/11 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.90×** | +9.5 | 3e-19 | 15/25 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.66×** | +9.4 | 6e-19 | 24/32 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.68×** | +9.1 | 1e-17 | 0/1 | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +8.6 | 5e-16 | 17/23 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.27×** | +8.3 | 9e-15 | 28/35 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.43×** | +8.3 | 9e-15 | 4/5 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.14×** | +8.0 | 9e-14 | 12/17 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.97×** | +7.9 | 2e-13 | 35/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.68×** | +7.1 | 5e-11 | 28/41 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.61×** | +6.7 | 1e-09 | 20/39 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.51×** | +6.7 | 1e-09 | 6/13 (NCI-H460, SW 900, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.45×** | +6.5 | 3e-09 | 24/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.82×** | +6.1 | 3e-08 | 16/45 (HOP62, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.20×** | +5.7 | 4e-07 | 23/43 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.95×** | +4.5 | 2e-04 | 14/36 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +4.5 | 2e-04 | 16/43 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.86×** | +4.2 | 6e-04 | 15/40 (SW480, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11271.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.594×** | -3.8 | 0.072 | 14/45 (NCI-H1792, C32, …) | inconsistent across doses | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.629× | -3.3 | 0.24 | 7/45 (COLO 205, HepG2/C3A, …) | top dose only | plate-row cell shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.635× | -3.2 | 0.24 | 15/35 (J82, NCI-H1573, …) | top dose only |  |
| [[Furosemide (drug)]] 0.5 µM |  | 0.664× | -3.0 | 0.36 | 14/36 (SW 900, A-172, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.28 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.94× (z +9.0) | — |
| [[SW480 (line)]] | alt | 2.28 | 2 | 0 | [[Auranofin (drug)]] 5 µM 16.9× (z +10.1) | — |
| [[A-172 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRZB]] | +0.78 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[SNX31]] | +0.78 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[CCDC13]] | +0.77 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[CASS4]] | +0.76 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[GRK7]] | +0.76 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.76 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[LINC01618]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.75 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.74 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[MCF2]] | +0.73 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.73 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[DRC1]] | +0.73 | +0.78 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DCAF4L1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMED6]] | C | DCAF4L1's natural level weakens TMED6's drug response | DCAF4L1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.13; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.8, -15.6); signed map (13.5, 4.6). **Vector** length 63.6, 9.84% of its response variance represented; |z| ≥ 3 in 1,311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +12.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +4.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -1.9 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.8 | +3.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 4 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p13 — chr4:41,981,756-41,986,465 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously WDR21B |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q3SXM0](https://www.uniprot.org/uniprotkb/Q3SXM0) carries no function annotation.

**Summary**, from NCBI Gene [285429](https://www.ncbi.nlm.nih.gov/gene/285429):

> Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27723) · Entrez [285429](https://www.ncbi.nlm.nih.gov/gene/285429) · UniProt [Q3SXM0](https://www.uniprot.org/uniprotkb/Q3SXM0) · Ensembl [ENSG00000182308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182308)

## Data

Gene col 11271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11271); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11271]; `tensor/DDL_lfc|DDL_z.npy` [11271]; `embed/gene_vectors.npy` [11271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11271 or target_col == 11271). Every well: [[DCAF4L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF4L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
