---
symbol: "KRT10"
type: "gene"
col: 11810
ensembl_id: "ENSG00000186395"
name: "keratin 10"
location: "17q21.2"
module: 24
arm: "+"
pooled_cpm: 36.05
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# KRT10

*keratin 10* — 17q21.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.06× (z +6.2, q 3e-07, up in 44 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.167×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.81, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[LAMTOR5]] (+0.80, fdr 7e-06), [[TMEM258]] (+0.78, fdr 7e-06), [[SAT2]] (+0.76, fdr 7e-06); moves opposite to [[ABCF2]] (-0.73, fdr 8e-06), [[PSME3]] (-0.73, fdr 1e-05), [[IPO5]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.06×** | +6.2 | 3e-07 | 44/47 (PANC-1, HCT15, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +3.6 | 0.075 | 27/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.86×** | +3.4 | 0.088 | 30/48 (NCI-H23, NCI-H2030, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.85×** | +3.4 | 0.088 | 33/48 (PANC-1, BT-474, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | 1.82× | +3.3 | 0.10 | 30/45 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.76× | +3.0 | 0.23 | 28/45 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11810.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.167×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.353× | -3.0 | 0.76 | 37/48 (C-33 A, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.89 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 28.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -10.7) |
| [[A-172 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.81 | +0.68 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | +0.80 | +0.58 / +0.86 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.78 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[SAT2]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | +0.76 | +0.65 / +0.81 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCR10]] ⚠ | +0.75 | +0.57 / +0.80 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | +0.75 | +0.57 / +0.82 | both halves | 1e-05 |  |
| [[KRTCAP2]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.75 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[MIEN1]] | +0.74 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.74 | +0.56 / +0.79 | both halves | 1e-05 |  |
| [[NDUFA1]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[ATP5MC2]] | +0.72 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[COX17]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[C19orf81]] | +0.72 | +0.51 / +0.76 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCF2]] | -0.73 | -0.58 / -0.71 | both halves | 8e-06 |  |
| [[PSME3]] | -0.73 | -0.52 / -0.78 | both halves | 1e-05 |  |
| [[IPO5]] | -0.72 | -0.67 / -0.77 | both halves | 7e-06 |  |
| [[DARS2]] | -0.72 | -0.58 / -0.69 | both halves | 8e-06 |  |
| [[MOB1A]] | -0.67 | -0.51 / -0.73 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.66 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[RNPS1]] | -0.65 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[WDR77]] | -0.65 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[NAA50]] | -0.64 | -0.57 / -0.65 | both halves | 9e-06 |  |
| [[EIF4G1]] | -0.64 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[CCT7]] | -0.64 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[CCT5]] | -0.64 | -0.69 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.811). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-42.9, -20.7); signed map (-13.5, -1.6). **Vector** length 85.6, 34.8% of its response variance represented; |z| ≥ 3 in 416 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.54 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.3 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.7 | +3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | keratin 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,818,117-40,822,614 (-) |
| Ensembl biotype | protein_coding |
| Also known as | K10, CK10; previously KPP |
| Gene groups (HGNC) | Keratins, type I |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P13645](https://www.uniprot.org/uniprotkb/P13645) (Keratin, type I cytoskeletal 10):

> Structural component of intermediate filaments in suprabasal keratinocytes of stratified epithelia. Forms heteropolymers primarily with the type II keratin KRT1, and also with KRT2, assembling into intermediate filament networks that support terminal differentiation, mechanical resilience, and epidermal barrier formation.; (Microbial infection) Acts as a mediator of S.aureus adherence to desquamated nasal epithelial cells via clfB, and hence may play a role in nasal colonization.; (Microbial …

**Summary**, from NCBI Gene [3858](https://www.ncbi.nlm.nih.gov/gene/3858):

> This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic hyperkeratosis. This gene is located within a cluster of keratin family members on chromosome …

**Accessions** — [HGNC:6413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6413) · Entrez [3858](https://www.ncbi.nlm.nih.gov/gene/3858) · UniProt [P13645](https://www.uniprot.org/uniprotkb/P13645) · Ensembl [ENSG00000186395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186395)

## Data

Gene col 11810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11810); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11810]; `tensor/DDL_lfc|DDL_z.npy` [11810]; `embed/gene_vectors.npy` [11810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11810 or target_col == 11810). Every well: [[KRT10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
