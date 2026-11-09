---
symbol: "CHODL"
type: "gene"
col: 7823
ensembl_id: "ENSG00000154645"
name: "chondrolectin"
location: "21q21.1"
module: 26
arm: "+"
pooled_cpm: 2.07
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 26
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CHODL

*chondrolectin* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.08× (z +22.3, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM: 0.618× (z -3.9, q 0.063, down in 8 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02208]] (+0.82, fdr 7e-06), [[UNC79]] (+0.81, fdr 7e-06), [[NEB]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.08×** | +22.3 | 0e+00 | 29/29 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.73×** | +11.4 | 7e-28 | 18/41 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +11.2 | 1e-26 | 20/33 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.91×** | +11.0 | 7e-26 | 4/6 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.12×** | +11.0 | 7e-26 | 12/18 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +9.7 | 3e-20 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +8.6 | 4e-16 | 15/30 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.66×** | +7.9 | 3e-13 | 19/36 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.62×** | +7.8 | 5e-13 | 17/34 (NCI-H23, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.53×** | +7.5 | 4e-12 | 13/31 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +7.4 | 7e-12 | 21/40 (A498, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +7.1 | 5e-11 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **2.33×** | +6.6 | 2e-09 | 14/23 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.19×** | +6.3 | 1e-08 | 15/33 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.84×** | +4.9 | 3e-05 | 17/44 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.81×** | +4.8 | 6e-05 | 9/44 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.76×** | +4.5 | 2e-04 | 11/37 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 6e-04 | 12/40 (NCI-H1573, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.618×** | -3.9 | 0.063 | 8/38 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.745× | -3.3 | 0.16 | 8/37 (NCI-H1573, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.659× | -3.3 | 0.16 | 13/38 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.752× | -3.2 | 0.17 | 5/41 (SW 900, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 2.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +12.8) | — |
| [[A-172 (line)]] | wt | 0.971 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.8× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 6.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 0.992 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +9.3) | — |
| [[SW48 (line)]] | wt | 5.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.5× (z +9.1) | — |
| [[SW480 (line)]] | alt | 1.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +9.8) | — |
| [[A-427 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.756 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.668 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.852 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.798 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.603 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.572 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.883 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.621 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.846 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02208]] | +0.82 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[UNC79]] | +0.81 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[NEB]] | +0.80 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[LINC01208]] | +0.78 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.76 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.75 | +0.80 / +0.47 | both halves | 2e-05 |  |
| [[CFAP418-AS1]] | +0.75 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[GUCY2C-AS1]] | +0.75 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.74 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[STPG2]] | +0.74 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[USP38-DT]] | +0.74 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.74 | +0.77 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHODL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[THBS4-AS1]] | B | THBS4-AS1 activity raises CHODL's level | lines that do not express THBS4-AS1 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without THBS4-AS1 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.786). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.4, 17.0); signed map (29.0, -4.6). **Vector** length 56.7, 8.65% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +22.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +7.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +6.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +4.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -0.0 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | chondrolectin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.1 — chr21:17,901,263-18,267,373 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12627, PRED12, MT75; previously C21orf68 |
| Gene groups (HGNC) | C-type lectin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9P2](https://www.uniprot.org/uniprotkb/Q9H9P2) (Chondrolectin):

> May play a role in the development of the nervous system such as in neurite outgrowth and elongation. May be involved in motor axon growth and guidance.

**Summary**, from NCBI Gene [140578](https://www.ncbi.nlm.nih.gov/gene/140578):

> This gene encodes a type I membrane protein with a carbohydrate recognition domain characteristic of C-type lectins in its extracellular portion. In other proteins, this domain is involved in endocytosis of glycoproteins and exogenous sugar-bearing pathogens. This protein localizes predominantly to the perinuclear region. Several transcript variants encoding a few different isoforms have been found for this gene. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:17807](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17807) · Entrez [140578](https://www.ncbi.nlm.nih.gov/gene/140578) · UniProt [Q9H9P2](https://www.uniprot.org/uniprotkb/Q9H9P2) · Ensembl [ENSG00000154645](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154645)

## Data

Gene col 7823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7823); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7823]; `tensor/DDL_lfc|DDL_z.npy` [7823]; `embed/gene_vectors.npy` [7823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7823 or target_col == 7823). Every well: [[CHODL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHODL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
