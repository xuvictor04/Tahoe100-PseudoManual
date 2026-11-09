---
symbol: "NDUFAF3"
type: "gene"
col: 10892
ensembl_id: "ENSG00000178057"
name: "NADH:ubiquinone oxidoreductase complex assembly factor 3"
location: "3p21.31"
module: 58
arm: "+"
pooled_cpm: 10.39
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# NDUFAF3

*NADH:ubiquinone oxidoreductase complex assembly factor 3* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.41× (z +10.9, q 1e-24, up in 31 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 8.57×, NCI-H460 11.1×, LS 180 9.53×, SW480 7.02×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 8.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.413× (z -5.2, q 1e-04, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM141]] (+0.70, fdr 1e-05), [[MRPL40]] (+0.66, fdr 7e-06), [[MIF4GD]] (+0.61, fdr 1e-05); moves opposite to [[WASH9P]] (-0.46, fdr 2e-04), [[LY6G5B]] (-0.43, fdr 2e-04), [[MCFD2]] (-0.43, fdr 1e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10892.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 8.57×, NCI-H460 11.1×, LS 180 9.53×, SW480 7.02×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 8.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **6.41×** | +10.9 | 1e-24 | 31/31 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.37×** | +7.8 | 2e-12 | 17/18 (SW480, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.69×** | +7.1 | 3e-10 | 23/25 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.93×** | +3.9 | 0.016 | 23/40 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +3.1 | 0.22 | 10/48 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.44× | +3.0 | 0.23 | 18/48 (CHP-212, CFPAC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10892.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.413×** | -5.2 | 1e-04 | 36/47 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.505×** | -4.0 | 0.019 | 29/46 (SW48, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.521×** | -3.8 | 0.027 | 28/46 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.588× | -3.1 | 0.28 | 20/46 (SW48, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.59 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.02× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HEC-1-A (line)]] | alt | 23.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.53× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 4.54 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.6× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 6.74 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 8.71 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.57× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 9.52 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0389× (z -9.9) |
| [[A-172 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 13 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM141]] | +0.70 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[MRPL40]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[MIF4GD]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[NDUFB3]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 897 |
| [[TIMM17B]] ⚠ | +0.61 | +0.53 / +0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC25A11]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[NDUFA7]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 901 |
| [[MFSD3]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[HDDC3]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[FIBP]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[HINT2]] | +0.56 | +0.38 / +0.66 | both halves | 6e-05 |  |
| [[ANTKMT]] | +0.55 | +0.27 / +0.63 | both halves | 3e-04 |  |
| [[SNAPIN]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASH9P]] | -0.46 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[LY6G5B]] | -0.43 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[MCFD2]] | -0.43 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SLC25A53]] | -0.42 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[BORCS7-ASMT]] | -0.41 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[SNHG22]] | -0.41 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[WASH8P]] ⚠ | -0.40 | -0.20 / -0.45 | ⚠ not reproduced | 7e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MESD]] | -0.40 | -0.52 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[CERS2]] | -0.40 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[ADAT3]] | -0.40 | -0.38 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.527). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.3, -11.8); signed map (-21.1, -4.6). **Vector** length 55.6, 12.0% of its response variance represented; |z| ≥ 3 in 540 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.4 | +10.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -0.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +1.2 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +1.4 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase complex assembly factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,020,459-49,023,495 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10527, DKFZP564J0123, E3-3, 2P1; previously C3orf60 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BU61](https://www.uniprot.org/uniprotkb/Q9BU61) (NADH dehydrogenase):

> Essential factor for the assembly of mitochondrial NADH:ubiquinone oxidoreductase complex (complex I).

**Summary**, from NCBI Gene [25915](https://www.ncbi.nlm.nih.gov/gene/25915):

> This gene encodes a mitochondrial complex I assembly protein that interacts with complex I subunits. Mutations in this gene cause mitochondrial complex I deficiency, a fatal neonatal disorder of the oxidative phosphorylation system. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:29918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29918) · Entrez [25915](https://www.ncbi.nlm.nih.gov/gene/25915) · UniProt [Q9BU61](https://www.uniprot.org/uniprotkb/Q9BU61) · Ensembl [ENSG00000178057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178057)

## Data

Gene col 10892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10892); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10892]; `tensor/DDL_lfc|DDL_z.npy` [10892]; `embed/gene_vectors.npy` [10892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10892 or target_col == 10892). Every well: [[NDUFAF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFAF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
