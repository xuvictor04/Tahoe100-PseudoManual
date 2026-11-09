---
symbol: "WDR83OS"
type: "gene"
col: 2623
ensembl_id: "ENSG00000105583"
name: "WD repeat domain 83 opposite strand"
location: "19p13.13"
module: 24
arm: "+"
pooled_cpm: 18.19
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# WDR83OS

*WD repeat domain 83 opposite strand* — 19p13.13

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.30× (z +6.4, q 1e-07, up in 38 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX6B1]] (+0.81, fdr 7e-06), [[SMIM26]] (+0.79, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[CWC15]] (+0.77, fdr 7e-06), [[LAMTOR5]] (+0.77, fdr 7e-06); moves opposite to [[NUP188]] (-0.65, fdr 1e-05), [[WDR1]] (-0.65, fdr 1e-05), [[MAPRE1]] (-0.63, fdr 5e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.30×** | +6.4 | 1e-07 | 38/41 (NCI-H460, SNU-423, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +4.9 | 3e-04 | 34/43 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.96×** | +3.6 | 0.066 | 28/44 (hTERT-HPNE, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.97×** | +3.5 | 0.075 | 26/32 (KATO III, RPMI-7951, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.00×** | +3.4 | 0.075 | 23/37 (SW480, A-172, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2623.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.542× | -3.2 | 0.64 | 31/47 (LS 180, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.74 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 18 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6B1]] | +0.81 | +0.70 / +0.83 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.79 | +0.74 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CWC15]] | +0.77 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.77 | +0.64 / +0.82 | both halves | 7e-06 | STRING 495 |
| [[RPL36AL]] ⚠ | +0.77 | +0.65 / +0.79 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB11]] ⚠ | +0.76 | +0.63 / +0.85 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS36]] ⚠ | +0.76 | +0.66 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM258]] | +0.75 | +0.59 / +0.79 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[NDUFA4]] | +0.74 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[UQCRB]] ⚠ | +0.74 | +0.70 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.74 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[POLR2J]] ⚠ | +0.74 | +0.63 / +0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ALKBH7]] | +0.74 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[RNF181]] | +0.74 | +0.51 / +0.81 | both halves | 1e-05 |  |
| [[COX14]] | +0.73 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[TOMM7]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 | pathway: Protein localization |
| [[IFI27L2]] | +0.72 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[CHCHD5]] | +0.72 | +0.55 / +0.74 | both halves | 1e-05 | pathway: Protein localization |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.65 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[WDR1]] | -0.65 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.63 | -0.39 / -0.70 | both halves | 5e-05 |  |
| [[EIF4G1]] | -0.63 | -0.49 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-43.8, -20.7); signed map (-32.0, 8.5). **Vector** length 62.8, 19.9% of its response variance represented; |z| ≥ 3 in 381 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.53 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +2.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -4.8 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -4.4 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.4 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 83 opposite strand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,668,073-12,669,415 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTD008, PAT10; previously C19orf56 |
| Gene groups (HGNC) | PAT complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y284](https://www.uniprot.org/uniprotkb/Q9Y284) (PAT complex subunit Asterix):

> Component of the multi-pass translocon (MPT) complex that mediates insertion of multi-pass membrane proteins into the lipid bilayer of membranes. The MPT complex takes over after the SEC61 complex: following membrane insertion of the first few transmembrane segments of proteins by the SEC61 complex, the MPT complex occludes the lateral gate of the SEC61 complex to promote insertion of subsequent transmembrane regions. Within the MPT complex, the PAT subcomplex sequesters any highly polar …

**Summary**, from NCBI Gene [51398](https://www.ncbi.nlm.nih.gov/gene/51398):

> Enables protein folding chaperone. Involved in multi-pass transmembrane protein insertion into ER membrane. Located in endoplasmic reticulum membrane. Part of multi-pass translocon complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30203) · Entrez [51398](https://www.ncbi.nlm.nih.gov/gene/51398) · UniProt [Q9Y284](https://www.uniprot.org/uniprotkb/Q9Y284) · Ensembl [ENSG00000105583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105583)

## Data

Gene col 2623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2623); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2623]; `tensor/DDL_lfc|DDL_z.npy` [2623]; `embed/gene_vectors.npy` [2623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2623 or target_col == 2623). Every well: [[WDR83OS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR83OS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
