---
symbol: "UQCR11"
type: "gene"
col: 4820
ensembl_id: "ENSG00000127540"
name: "ubiquinol-cytochrome c reductase, complex III subunit XI"
location: "19p13.3"
module: 48
arm: "+"
pooled_cpm: 29.71
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# UQCR11

*ubiquinol-cytochrome c reductase, complex III subunit XI* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.56× (z +8.9, q 3e-16, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 9.34×, NCI-H23 6.33×, NCI-H460 5.88×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.452× (z -6.8, q 8e-09, down in 42 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.274×, RKO 0.236×); [[Tadalafil (drug)]] 5 µM in 1 line (CFPAC-1 0.123×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCRQ]] (+0.86, fdr 7e-06, ⚠ UQCRQ in the vector space only through flagged drug-doses), [[ROMO1]] (+0.84, fdr 7e-06), [[MIF]] (+0.83, fdr 7e-06), [[UBL5]] (+0.83, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4820.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 9.34×, NCI-H23 6.33×, NCI-H460 5.88×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.56×** | +8.9 | 3e-16 | 43/43 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.71×** | +7.6 | 6e-12 | 34/36 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.57×** | +5.3 | 2e-05 | 37/41 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +4.8 | 3e-04 | 38/45 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.97×** | +4.1 | 0.004 | 38/47 (NCI-H460, LS 180, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.86×** | +3.8 | 0.015 | 32/46 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4820.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.274×, RKO 0.236×); [[Tadalafil (drug)]] 5 µM in 1 line (CFPAC-1 0.123×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.452×** | -6.8 | 8e-09 | 42/47 (Panc 03.27, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.582× | -3.3 | 0.30 | 27/47 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.568× | -3.2 | 0.30 | 36/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.123× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.34× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 45.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.7) |
| [[RKO (line)]] | wt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -8.9) |
| [[A-172 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRQ]] ⚠ | +0.86 | +0.82 / +0.84 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.84 | +0.78 / +0.84 | both halves | 7e-06 | STRING 717 |
| [[MIF]] | +0.83 | +0.82 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[NDUFB11]] ⚠ | +0.83 | +0.76 / +0.83 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 981; ⚠ in the vector space only through flagged drug-doses |
| [[UBL5]] | +0.83 | +0.86 / +0.76 | both halves | 7e-06 | STRING 515 |
| [[COX7C]] | +0.83 | +0.76 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 995 |
| [[COX6A1]] | +0.81 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 971 |
| [[ELOB]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[COX6C]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 994 |
| [[C4orf48]] | +0.80 | +0.68 / +0.80 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.79 | +0.67 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997 |
| [[ATP5MK]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 870 |
| [[MICOS13]] | +0.77 | +0.73 / +0.69 | both halves | 7e-06 | STRING 597 |
| [[ATP5MJ]] | +0.76 | +0.65 / +0.81 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 494 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.879). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.7, -21.7); signed map (-34.9, 9.2). **Vector** length 58.4, 19.3% of its response variance represented; |z| ≥ 3 in 461 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex IV assembly* (reactome, mean cos +0.70 to 11); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.74 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.72 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +3.7 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | +1.0 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | -0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.2 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.1 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.1 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase, complex III subunit XI |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,597,169-1,605,473 (-) |
| Ensembl biotype | protein_coding |
| Also known as | QCR10; previously UQCR |
| Gene groups (HGNC) | Mitochondrial complex III: ubiquinol-cytochrome c reductase complex subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O14957](https://www.uniprot.org/uniprotkb/O14957) (Cytochrome b-c1 complex subunit 10):

> Component of the ubiquinol-cytochrome c oxidoreductase, a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular …

**Summary**, from NCBI Gene [10975](https://www.ncbi.nlm.nih.gov/gene/10975):

> This gene encodes the smallest known component of the ubiquinol-cytochrome c reductase complex, which forms part of the mitochondrial respiratory chain. The encoded protein may function as a binding factor for the iron-sulfur protein in this complex. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:30862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30862) · Entrez [10975](https://www.ncbi.nlm.nih.gov/gene/10975) · UniProt [O14957](https://www.uniprot.org/uniprotkb/O14957) · Ensembl [ENSG00000127540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127540)

## Data

Gene col 4820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4820); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4820]; `tensor/DDL_lfc|DDL_z.npy` [4820]; `embed/gene_vectors.npy` [4820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4820 or target_col == 4820). Every well: [[UQCR11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCR11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
