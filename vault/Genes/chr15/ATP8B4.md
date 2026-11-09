---
symbol: "ATP8B4"
type: "gene"
col: 2407
ensembl_id: "ENSG00000104043"
name: "ATPase phospholipid transporting 8B4 (putative)"
location: "15q21.2"
module: 140
arm: "+"
pooled_cpm: 3.03
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# ATP8B4

*ATPase phospholipid transporting 8B4 (putative)* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.53× (z +22.0, q 0e+00, up in 29 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.879× (z -4.2, q 0.016, down in 22 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.665× (z -3.7, q 0.049, down in 9 of 38 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00534]] (+0.66, fdr 1e-05), [[ADD3-AS1]] (+0.63, fdr 1e-05), [[PAX5]] (+0.60, fdr 1e-05); moves opposite to [[GNAI2]] (-0.50, fdr 0.003, ⚠ not reproduced), [[HAUS3]] (-0.49, fdr 4e-04), [[ACAP2]] (-0.48, fdr 2e-04).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.53×** | +22.0 | 0e+00 | 29/31 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +9.6 | 1e-19 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +9.3 | 3e-18 | 11/32 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.41×** | +8.0 | 2e-13 | 26/40 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +7.8 | 6e-13 | 6/12 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +7.2 | 7e-11 | 15/42 (RPMI-7951, SK-MEL-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +6.6 | 3e-09 | 12/24 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +6.0 | 1e-07 | 12/30 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.0 | 1e-07 | 10/41 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +5.0 | 3e-05 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.3 | 9e-04 | 9/38 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.009 | 9/43 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.7 | 0.011 | 1/11 (SHP-77) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.027 | 7/42 (HEC-1-A, PANC-1, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.4 | 0.028 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.054 | 5/32 (NCI-H460, NCI-H23, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.879× | -4.2 | 0.016 | 22/47 (C32, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.665×** | -3.7 | 0.049 | 9/38 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.668×** | -3.7 | 0.049 | 11/42 (LOX-IMVI, SNU-423, …) | rises with dose | position effect removed |
| [[Pemetrexed (drug)]] 5 µM |  | **0.673×** | -3.4 | 0.079 | 6/28 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | 0.779× | -3.2 | 0.16 | 12/44 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.79 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0587× (z -11.8) |
| [[A549 (line)]] | wt | 2.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 1.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.28× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -8.5) |
| [[PANC-1 (line)]] | alt | 1.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +9.8) | — |
| [[SW480 (line)]] | alt | 2.07 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0665× (z -10.1) |
| [[A-172 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00534]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ADD3-AS1]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[PAX5]] | +0.60 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MYO3B]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[NINJ2]] | +0.59 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[C8orf34]] | +0.59 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[HTR1D]] | +0.59 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[GREB1]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SLC25A48]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[LINC00578]] | +0.57 | +0.37 / +0.65 | both halves | 8e-05 |  |
| [[ENPEP]] | +0.57 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[AQP4-AS1]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | -0.50 | -0.45 / -0.09 | ⚠ not reproduced | 0.003 |  |
| [[HAUS3]] | -0.49 | -0.38 / -0.25 | both halves | 4e-04 |  |
| [[ACAP2]] | -0.48 | -0.29 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP8B4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.1, 35.5); signed map (36.5, 12.3). **Vector** length 46.7, 5.80% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +22.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +0.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.7 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 8B4 (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:49,858,238-50,182,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPIM, KIAA1939 |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 5 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF62](https://www.uniprot.org/uniprotkb/Q8TF62) (Probable phospholipid-transporting ATPase IM):

> Component of a P4-ATPase flippase complex which catalyzes the hydrolysis of ATP coupled to the transport of aminophospholipids from the outer to the inner leaflet of various membranes and ensures the maintenance of asymmetric distribution of phospholipids. Phospholipid translocation also seems to be implicated in vesicle formation and in uptake of lipid signaling molecules (Probable).

**Summary**, from NCBI Gene [79895](https://www.ncbi.nlm.nih.gov/gene/79895):

> This gene encodes a member of the cation transport ATPase (P-type) family and type IV subfamily. The encoded protein is involved in phospholipid transport in the cell membrane. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:13536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13536) · Entrez [79895](https://www.ncbi.nlm.nih.gov/gene/79895) · UniProt [Q8TF62](https://www.uniprot.org/uniprotkb/Q8TF62) · Ensembl [ENSG00000104043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104043)

## Data

Gene col 2407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2407); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2407]; `tensor/DDL_lfc|DDL_z.npy` [2407]; `embed/gene_vectors.npy` [2407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2407 or target_col == 2407). Every well: [[ATP8B4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP8B4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
