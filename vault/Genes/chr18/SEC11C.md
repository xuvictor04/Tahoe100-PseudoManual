---
symbol: "SEC11C"
type: "gene"
col: 9331
ensembl_id: "ENSG00000166562"
name: "SEC11 homolog C, signal peptidase complex subunit"
location: "18q21.32"
module: 49
arm: "+"
pooled_cpm: 30.17
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SEC11C

*SEC11 homolog C, signal peptidase complex subunit* — 18q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.20× (z +11.1, q 6e-26, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.72× (z +4.3, q 0.001, up in 30 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.364×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA4]] (+0.67, fdr 7e-06), [[XRRA1]] (+0.67, fdr 7e-06), [[EDF1]] (+0.63, fdr 2e-05); moves opposite to [[NUP50]] (-0.60, fdr 1e-05), [[SUMO3]] (-0.58, fdr 2e-05), [[FGD5-AS1]] (-0.57, fdr 1e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.20×** | +11.1 | 6e-26 | 44/44 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.18×** | +8.8 | 3e-16 | 33/35 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +6.7 | 3e-09 | 35/41 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.2 | 4e-05 | 36/44 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.76×** | +4.5 | 6e-04 | 32/48 (C32, HEC-1-A, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.75×** | +4.5 | 6e-04 | 39/48 (C32, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.75×** | +4.5 | 6e-04 | 36/44 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +4.3 | 0.001 | 30/47 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.58×** | +3.6 | 0.017 | 26/48 (HOP62, H4, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.026 | 31/48 (SW480, SW48, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.026 | 33/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.032 | 26/48 (BT-474, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.032 | 27/48 (NCI-H460, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.364×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 24.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 60.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 20.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 51.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.73× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 27.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +10.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.28× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA4]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[XRRA1]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[EDF1]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SEC22A]] | +0.63 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[FBXO16]] | +0.63 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[SEC61B]] | +0.62 | +0.58 / +0.57 | both halves | 9e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 732 |
| [[SELENOS]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[FICD]] | +0.62 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[HID1]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[GOLPH3L]] | +0.60 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[SLC33A1]] | +0.57 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PIGH]] | +0.56 | +0.36 / +0.56 | both halves | 9e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP50]] | -0.60 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[FGD5-AS1]] | -0.57 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[TOR1A]] | -0.54 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[DARS2]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[E2F3]] | -0.53 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[HCFC1]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[LARP4B]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[SUV39H2]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PSME3]] | -0.50 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[XRCC6]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[HASPIN]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, -38.1); signed map (-54.4, 14.8). **Vector** length 79.5, 23.4% of its response variance represented; |z| ≥ 3 in 584 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.9 | +0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SEC11 homolog C, signal peptidase complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.32 — chr18:59,139,866-59,158,832 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPC21, SPCS4C; previously SEC11L3 |
| Reactome | 22 pathways, smallest: Synthesis, secretion, and inactivation of Glucose-dependent Insulinotropic Polypeptide (GIP); Synthesis, secretion, and deacylation of Ghrelin; Synthesis, secretion, and inactivation of Glucagon-like Peptide-1 (GLP-1) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY50](https://www.uniprot.org/uniprotkb/Q9BY50) (Signal peptidase complex catalytic subunit SEC11C):

> Catalytic component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum. Specifically cleaves N-terminal signal peptides that contain a hydrophobic alpha-helix (h-region) shorter than 18-20 amino acids.

**Summary**, from NCBI Gene [90701](https://www.ncbi.nlm.nih.gov/gene/90701):

> Enables serine-type endopeptidase activity. Involved in obsolete signal peptide processing. Located in endoplasmic reticulum membrane. Part of signal peptidase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23400) · Entrez [90701](https://www.ncbi.nlm.nih.gov/gene/90701) · UniProt [Q9BY50](https://www.uniprot.org/uniprotkb/Q9BY50) · Ensembl [ENSG00000166562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166562)

## Data

Gene col 9331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9331); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9331]; `tensor/DDL_lfc|DDL_z.npy` [9331]; `embed/gene_vectors.npy` [9331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9331 or target_col == 9331). Every well: [[SEC11C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC11C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
